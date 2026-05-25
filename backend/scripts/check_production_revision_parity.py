from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def git_head_sha(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def fetch_health(base_url: str) -> dict:
    url = f"{base_url.rstrip('/')}/health"
    with urlopen(url, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Check production runtime revision parity against local git HEAD.")
    parser.add_argument("--base-url", default="https://aviary.luckysparrow.ch")
    parser.add_argument(
        "--out",
        default=str(repo_root() / "docs" / "status" / "production-revision-parity.json"),
        help="Output JSON report path.",
    )
    args = parser.parse_args()

    root = repo_root()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    head = git_head_sha(root)
    report: dict = {
        "kind": "production_revision_parity",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_url": args.base_url,
        "local_head_sha": head,
        "production_runtime_sha": "",
        "production_status": "",
        "parity": False,
        "error": "",
    }

    try:
        health = fetch_health(args.base_url)
        report["production_status"] = str(health.get("status") or "")
        deployment = health.get("deployment") or {}
        runtime_sha = str(deployment.get("runtime_build_revision") or "")
        report["production_runtime_sha"] = runtime_sha
        report["parity"] = runtime_sha == head and report["production_status"] == "ok"
    except (URLError, HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        report["error"] = str(exc)

    out_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"report={out_path}")
    print(f"parity={report['parity']}")
    print(f"local_head_sha={report['local_head_sha']}")
    print(f"production_runtime_sha={report['production_runtime_sha']}")
    if report["error"]:
        print(f"error={report['error']}")
        return 1
    return 0 if report["parity"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
