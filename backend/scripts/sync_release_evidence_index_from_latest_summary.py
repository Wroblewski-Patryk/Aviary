from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _latest_summary_path(status_dir: Path) -> Path:
    candidates = sorted(
        status_dir.glob("production-release-evidence-summary-*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError("No production-release-evidence-summary-*.json found.")
    return candidates[0]


def _build_summary_block(summary_rel_path: str, summary: dict[str, object]) -> str:
    return "\n".join(
        [
            "Latest production evidence capture summary (auto-synced):",
            "",
            f"- runtime build revision: `{summary.get('runtime_build_revision', '')}`",
            f"- web shell build revision: `{summary.get('web_shell_build_revision', '')}`",
            f"- health status: `{summary.get('health_status', '')}`",
            f"- release readiness: `{summary.get('release_ready', '')}`",
            f"- release violations: `{summary.get('release_violations', [])}`",
            "- summary artifact:",
            f"  - `{summary_rel_path}`",
        ]
    )


def _update_release_index(content: str, block: str, date_iso: str) -> str:
    content = re.sub(
        r"^Last updated:\s+\d{4}-\d{2}-\d{2}$",
        f"Last updated: {date_iso}",
        content,
        flags=re.MULTILINE,
    )
    pattern = re.compile(
        r"Latest production evidence capture summary \(.*?\):\n(?:.*\n)*?(?=\n## |\Z)",
        re.MULTILINE,
    )
    if pattern.search(content):
        return pattern.sub(block + "\n", content)

    marker = "| Organizer daily-use extension | `daily_use_workflows_blocked_by_provider_activation` |"
    if marker in content:
        return content.replace(marker, marker + "\n\n" + block)
    return content.rstrip() + "\n\n" + block + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync release-evidence-index.md from latest summary JSON.")
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format.")
    args = parser.parse_args()

    root = _repo_root()
    status_dir = root / "docs" / "status"
    index_path = root / "docs" / "operations" / "release-evidence-index.md"

    summary_path = _latest_summary_path(status_dir)
    summary = json.loads(summary_path.read_text(encoding="utf-8-sig"))
    summary_rel = str(summary_path.relative_to(root)).replace("\\", "/")

    block = _build_summary_block(summary_rel, summary)
    content = index_path.read_text(encoding="utf-8")
    updated = _update_release_index(content, block, args.date)
    index_path.write_text(updated, encoding="utf-8")

    print(
        json.dumps(
            {
                "index_path": str(index_path),
                "summary_path": str(summary_path),
                "date": args.date,
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
