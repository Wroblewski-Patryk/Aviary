from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify architecture gap audit artifact contains no curated gap rows."
    )
    parser.add_argument(
        "--artifact",
        type=Path,
        required=True,
        help="Path to architecture-gaps-*.json artifact file.",
    )
    return parser.parse_args(argv)


def run(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.artifact.exists():
        print(f"ERROR: artifact not found: {args.artifact}", file=sys.stderr)
        return 1

    data = json.loads(args.artifact.read_text(encoding="utf-8-sig"))
    items = data.get("items")
    if not isinstance(items, list):
        print("ERROR: invalid artifact format: missing list field 'items'", file=sys.stderr)
        return 1

    print(f"artifact={args.artifact}")
    print(f"curated_gap_count={len(items)}")
    if items:
        print("status=FAILED")
        return 1
    print("status=PASSED")
    return 0


def main() -> int:
    return run(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
