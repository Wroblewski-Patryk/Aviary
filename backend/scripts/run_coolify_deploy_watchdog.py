from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import requests

ROOT = Path(__file__).resolve().parents[2]
BACKEND_ROOT = Path(__file__).resolve().parents[1]

if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from scripts.check_production_revision_parity import git_head_sha


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def fetch_health_requests(base_url: str) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/health"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.json()


def fetch_health_urllib(base_url: str) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/health"
    with urlopen(url, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_health_with_fallback(base_url: str) -> tuple[dict[str, Any], str]:
    request_errors: list[str] = []
    try:
        return fetch_health_requests(base_url), "requests"
    except requests.RequestException as exc:
        request_errors.append(f"requests:{exc}")

    try:
        return fetch_health_urllib(base_url), "urllib"
    except (URLError, HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        request_errors.append(f"urllib:{exc}")

    raise RuntimeError("; ".join(request_errors))


def decide_next_action(
    *,
    parity: bool,
    trigger_enabled: bool,
    already_triggered: bool,
    webhook_ready: bool,
) -> str:
    if parity:
        return "done"
    if not trigger_enabled:
        return "wait"
    if already_triggered:
        return "wait"
    if not webhook_ready:
        return "needs_manual_coolify_deploy"
    return "trigger_webhook"


def trigger_webhook(
    *,
    webhook_url: str,
    webhook_secret: str,
    repository: str,
    branch: str,
    evidence_path: Path,
) -> dict[str, Any]:
    trigger_script = BACKEND_ROOT / "scripts" / "trigger_coolify_deploy_webhook.py"
    command = [
        sys.executable,
        str(trigger_script),
        "--webhook-url",
        webhook_url,
        "--webhook-secret",
        webhook_secret,
        "--branch",
        branch,
        "--evidence-path",
        str(evidence_path),
    ]
    if repository:
        command.extend(["--repository", repository])

    completed = subprocess.run(command, cwd=ROOT, check=False, capture_output=True, text=True)
    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Watch production revision parity and trigger Coolify webhook fallback on drift."
    )
    parser.add_argument("--base-url", default="https://aviary.luckysparrow.ch")
    parser.add_argument("--max-wait-seconds", type=int, default=300)
    parser.add_argument("--poll-seconds", type=int, default=15)
    parser.add_argument("--trigger-on-drift", action="store_true")
    parser.add_argument("--webhook-url", default=os.environ.get("COOLIFY_DEPLOY_WEBHOOK_URL", ""))
    parser.add_argument("--webhook-secret", default=os.environ.get("COOLIFY_DEPLOY_WEBHOOK_SECRET", ""))
    parser.add_argument("--repository", default="")
    parser.add_argument("--branch", default="main")
    parser.add_argument(
        "--out",
        default=str(ROOT / "artifacts" / "deploy" / "coolify-deploy-watchdog-latest.json"),
    )
    parser.add_argument(
        "--webhook-evidence-path",
        default=str(ROOT / "artifacts" / "deploy" / "coolify-webhook-watchdog.json"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    webhook_evidence_path = Path(args.webhook_evidence_path)
    webhook_evidence_path.parent.mkdir(parents=True, exist_ok=True)

    local_head = git_head_sha(ROOT)
    deadline = time.monotonic() + max(args.max_wait_seconds, 1)
    trigger_attempted = False
    trigger_result: dict[str, Any] | None = None

    report: dict[str, Any] = {
        "kind": "coolify_deploy_watchdog_report",
        "generated_at": utc_now_iso(),
        "base_url": args.base_url,
        "local_head_sha": local_head,
        "trigger_on_drift": bool(args.trigger_on_drift),
        "webhook_ready": bool(args.webhook_url and args.webhook_secret),
        "trigger_attempted": False,
        "trigger_result": None,
        "attempts": [],
        "final_status": "unknown",
        "parity": False,
        "connectivity_blocked": False,
    }

    while True:
        attempt: dict[str, Any] = {
            "at": utc_now_iso(),
            "production_status": "",
            "production_runtime_sha": "",
            "parity": False,
            "error": "",
            "decision": "",
            "health_fetch_method": "",
        }
        try:
            health, fetch_method = fetch_health_with_fallback(args.base_url)
            production_status = str(health.get("status") or "")
            deployment = health.get("deployment") or {}
            production_runtime_sha = str(deployment.get("runtime_build_revision") or "")
            parity = production_status == "ok" and production_runtime_sha == local_head
            attempt["production_status"] = production_status
            attempt["production_runtime_sha"] = production_runtime_sha
            attempt["parity"] = parity
            attempt["health_fetch_method"] = fetch_method
        except (URLError, HTTPError, TimeoutError, json.JSONDecodeError, requests.RequestException, RuntimeError) as exc:
            parity = False
            attempt["error"] = str(exc)

        decision = decide_next_action(
            parity=parity,
            trigger_enabled=bool(args.trigger_on_drift),
            already_triggered=trigger_attempted,
            webhook_ready=bool(args.webhook_url and args.webhook_secret),
        )
        attempt["decision"] = decision
        report["attempts"].append(attempt)

        if parity:
            report["parity"] = True
            report["final_status"] = "parity_confirmed"
            break

        if decision == "trigger_webhook":
            trigger_attempted = True
            trigger_result = trigger_webhook(
                webhook_url=str(args.webhook_url),
                webhook_secret=str(args.webhook_secret),
                repository=str(args.repository),
                branch=str(args.branch),
                evidence_path=webhook_evidence_path,
            )
            report["trigger_attempted"] = True
            report["trigger_result"] = trigger_result
            if not trigger_result["ok"]:
                report["final_status"] = "trigger_failed"
                break
        elif decision == "needs_manual_coolify_deploy":
            report["final_status"] = "needs_manual_coolify_deploy"
            break

        if time.monotonic() >= deadline:
            if all(not a["production_status"] and a["error"] for a in report["attempts"]):
                report["connectivity_blocked"] = True
                report["final_status"] = "connectivity_blocked"
                break
            report["final_status"] = "timeout_without_parity"
            break

        time.sleep(max(args.poll_seconds, 1))

    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"report={out_path}")
    print(f"final_status={report['final_status']}")
    print(f"parity={report['parity']}")

    if report["parity"]:
        return 0
    if report["final_status"] in {"trigger_failed", "needs_manual_coolify_deploy", "connectivity_blocked"}:
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
