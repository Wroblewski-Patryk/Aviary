from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def run_cmd(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def main() -> int:
    steps: list[dict[str, object]] = []

    checks = [
        {
            "id": "graph_tests_fast",
            "cmd": [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                "tests/test_build_architecture_graph_hosted_evidence_packet.py",
                "tests/test_verify_architecture_gap_artifact.py",
                "tests/test_architecture_graph_ci_policy.py",
                "tests/test_architecture_graph_query.py",
                "tests/test_architecture_graph_generator.py",
                "-m",
                "not slow",
            ],
            "cwd": PROJECT_ROOT / "backend",
        },
        {
            "id": "gap_gate_zero",
            "cmd": [
                sys.executable,
                "backend/scripts/query_architecture_graph.py",
                "--gaps",
                "--format",
                "json",
                "--fail-on-gaps",
            ],
            "cwd": PROJECT_ROOT,
        },
    ]

    overall_ok = True
    for check in checks:
        code, out, err = run_cmd(check["cmd"], check["cwd"])
        ok = code == 0
        overall_ok = overall_ok and ok
        steps.append(
            {
                "id": check["id"],
                "ok": ok,
                "exit_code": code,
                "stdout_tail": out.strip().splitlines()[-20:],
                "stderr_tail": err.strip().splitlines()[-20:],
            }
        )

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall_status": "PASSED" if overall_ok else "FAILED",
        "steps": steps,
    }

    out_dir = PROJECT_ROOT / "docs" / "status"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "architecture-graph-local-release-gate.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"report={out_path}")
    print(f"overall_status={report['overall_status']}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
