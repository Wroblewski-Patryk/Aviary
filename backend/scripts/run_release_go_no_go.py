from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BACKEND_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = BACKEND_ROOT.parent


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _run_command(command: list[str]) -> tuple[int, str, str]:
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.returncode, completed.stdout, completed.stderr


def _load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _audit_command(args: argparse.Namespace, audit_output: Path) -> list[str]:
    command = [
        sys.executable,
        str(BACKEND_ROOT / "scripts" / "audit_release_reality.py"),
        "--base-url",
        str(args.base_url),
        "--timeout-seconds",
        str(args.timeout_seconds),
        "--output",
        str(audit_output),
    ]
    if args.selected_sha:
        command.extend(["--selected-sha", str(args.selected_sha)])
    if args.selected_tag:
        command.extend(["--selected-tag", str(args.selected_tag)])
    if args.monitor_mode:
        command.append("--monitor-mode")
    return command


def _smoke_command(args: argparse.Namespace) -> list[str]:
    command = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(BACKEND_ROOT / "scripts" / "run_release_smoke.ps1"),
        "-BaseUrl",
        str(args.base_url),
        "-HealthRetryMaxAttempts",
        str(args.health_retry_max_attempts),
        "-HealthRetryDelaySeconds",
        str(args.health_retry_delay_seconds),
    ]
    if args.enforce_local_head_parity:
        command.extend(
            [
                "-WaitForDeployParity",
                "-DeployParityMaxWaitSeconds",
                str(args.deploy_parity_max_wait_seconds),
                "-DeployParityPollSeconds",
                str(args.deploy_parity_poll_seconds),
            ]
        )
    return command


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run release reality audit plus production smoke and print GO/HOLD.")
    parser.add_argument("--base-url", default="https://aviary.luckysparrow.ch")
    parser.add_argument("--selected-sha", default="")
    parser.add_argument("--selected-tag", default="")
    parser.add_argument("--monitor-mode", action="store_true")
    parser.add_argument("--skip-smoke", action="store_true")
    parser.add_argument("--enforce-local-head-parity", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=20)
    parser.add_argument("--deploy-parity-max-wait-seconds", type=int, default=300)
    parser.add_argument("--deploy-parity-poll-seconds", type=int, default=15)
    parser.add_argument("--health-retry-max-attempts", type=int, default=5)
    parser.add_argument("--health-retry-delay-seconds", type=int, default=5)
    parser.add_argument("--output", default="")
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    with tempfile.TemporaryDirectory() as tmp_dir:
        audit_output = Path(tmp_dir) / "release-reality-audit.json"
        audit_command = _audit_command(args, audit_output)
        audit_exit_code, audit_stdout, audit_stderr = _run_command(audit_command)
        audit_report = _load_json(audit_output)
        selected_sha = str(audit_report.get("selected_sha", "") or "")
        local_head = str(audit_report.get("local_head", "") or "")
        selected_sha_is_local_head = bool(selected_sha and local_head and selected_sha == local_head)
        auto_skip_smoke_reason = ""
        if (
            audit_exit_code == 0
            and not args.skip_smoke
            and not args.enforce_local_head_parity
            and selected_sha
            and local_head
            and selected_sha != local_head
        ):
            auto_skip_smoke_reason = "selected_sha_differs_from_local_head_release_smoke_is_local_head_bound"

        smoke_exit_code: int | None = None
        smoke_stdout = ""
        smoke_stderr = ""
        smoke_report: dict[str, Any] = {}
        smoke_command: list[str] = []
        smoke_skipped = bool(args.skip_smoke or auto_skip_smoke_reason)
        if audit_exit_code == 0 and not smoke_skipped:
            smoke_command = _smoke_command(args)
            smoke_exit_code, smoke_stdout, smoke_stderr = _run_command(smoke_command)
            try:
                parsed_smoke = json.loads(smoke_stdout)
                if isinstance(parsed_smoke, dict):
                    smoke_report = parsed_smoke
            except json.JSONDecodeError:
                smoke_report = {}

    audit_ok = audit_exit_code == 0
    smoke_ok = smoke_skipped or smoke_exit_code == 0
    verdict = "GO" if audit_ok and smoke_ok else "HOLD"
    report = {
        "kind": "release_go_no_go_report",
        "schema_version": 1,
        "generated_at": _utc_now_iso(),
        "base_url": str(args.base_url),
        "verdict": verdict,
        "audit": {
            "exit_code": audit_exit_code,
            "stdout": audit_stdout,
            "stderr": audit_stderr,
            "report": audit_report,
        },
        "smoke": {
            "skipped": smoke_skipped,
            "skip_reason": "operator_requested_skip_smoke" if args.skip_smoke else auto_skip_smoke_reason,
            "exit_code": smoke_exit_code,
            "stdout": smoke_stdout,
            "stderr": smoke_stderr,
            "report": smoke_report,
            "enforce_local_head_parity": bool(args.enforce_local_head_parity),
            "selected_sha_is_local_head": selected_sha_is_local_head,
        },
        "next_action": "release_claim_allowed_for_selected_sha" if verdict == "GO" else "resolve_audit_or_smoke_hold",
    }

    if args.output:
        output_path = Path(str(args.output))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if verdict == "GO" else 1


if __name__ == "__main__":
    raise SystemExit(main())
