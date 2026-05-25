from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a hosted architecture-graph evidence packet from downloaded CI artifacts."
    )
    parser.add_argument(
        "--fast-artifact",
        type=Path,
        required=True,
        help="Path to downloaded architecture-gaps-fast JSON artifact.",
    )
    parser.add_argument(
        "--heavy-artifact",
        type=Path,
        default=None,
        help="Optional path to downloaded architecture-gaps-heavy JSON artifact.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        required=True,
        help="Output directory for packet files.",
    )
    return parser.parse_args(argv)


def _load_gap_artifact(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"artifact not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    items = data.get("items")
    if not isinstance(items, list):
        raise ValueError(f"invalid artifact format for {path}: expected list field 'items'")
    return {"path": str(path), "include_auto": bool(data.get("include_auto", False)), "gap_count": len(items)}


def run(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        fast = _load_gap_artifact(args.fast_artifact)
        heavy = _load_gap_artifact(args.heavy_artifact) if args.heavy_artifact else None
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    packet = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "fast_artifact": fast,
        "heavy_artifact": heavy,
        "status": "PASSED" if fast["gap_count"] == 0 and (heavy is None or heavy["gap_count"] == 0) else "FAILED",
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "architecture-graph-hosted-evidence.json"
    md_path = args.out_dir / "architecture-graph-hosted-evidence.md"
    json_path.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    lines = [
        "# Architecture Graph Hosted Evidence",
        "",
        f"- generated_at_utc: `{packet['generated_at']}`",
        f"- overall_status: `{packet['status']}`",
        "",
        "## Fast Artifact",
        "",
        f"- path: `{fast['path']}`",
        f"- include_auto: `{fast['include_auto']}`",
        f"- curated_gap_count: `{fast['gap_count']}`",
    ]
    if heavy:
        lines.extend(
            [
                "",
                "## Heavy Artifact",
                "",
                f"- path: `{heavy['path']}`",
                f"- include_auto: `{heavy['include_auto']}`",
                f"- curated_gap_count: `{heavy['gap_count']}`",
            ]
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"packet_json={json_path}")
    print(f"packet_md={md_path}")
    print(f"overall_status={packet['status']}")
    return 0 if packet["status"] == "PASSED" else 1


def main() -> int:
    return run(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
