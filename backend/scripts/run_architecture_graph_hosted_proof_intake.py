from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate hosted architecture-graph artifacts and build a hosted evidence packet.",
    )
    parser.add_argument("--fast-artifact", type=Path, required=True)
    parser.add_argument("--heavy-artifact", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, required=True)
    return parser.parse_args(argv)


def _run_step(step: list[str]) -> int:
    completed = subprocess.run(step, check=False)
    return completed.returncode


def run(argv: list[str]) -> int:
    args = parse_args(argv)
    script_dir = Path(__file__).resolve().parent
    python = sys.executable

    verify = script_dir / "verify_architecture_gap_artifact.py"
    packet = script_dir / "build_architecture_graph_hosted_evidence_packet.py"

    if _run_step([python, str(verify), "--artifact", str(args.fast_artifact)]) != 0:
        return 1
    if args.heavy_artifact and _run_step([python, str(verify), "--artifact", str(args.heavy_artifact)]) != 0:
        return 1

    build_cmd = [
        python,
        str(packet),
        "--fast-artifact",
        str(args.fast_artifact),
        "--out-dir",
        str(args.out_dir),
    ]
    if args.heavy_artifact:
        build_cmd.extend(["--heavy-artifact", str(args.heavy_artifact)])
    if _run_step(build_cmd) != 0:
        return 1

    summary = {
        "status": "PASSED",
        "fast_artifact": str(args.fast_artifact),
        "heavy_artifact": str(args.heavy_artifact) if args.heavy_artifact else "",
        "out_dir": str(args.out_dir),
    }
    print(json.dumps(summary))
    return 0


def main() -> int:
    return run(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
