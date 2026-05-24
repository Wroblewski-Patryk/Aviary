from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from query_architecture_graph import build_indexes, default_graph_path, gap_report, load_graph


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def summarize(nodes: list[dict[str, str]]) -> dict[str, Any]:
    total = len(nodes)
    curated = [node for node in nodes if "#auto" not in node.get("tags", "")]
    auto = [node for node in nodes if "#auto" in node.get("tags", "")]

    def pct(value: int, base: int) -> float:
        if base <= 0:
            return 0.0
        return round((value / base) * 100.0, 2)

    def status_counts(items: list[dict[str, str]]) -> dict[str, int]:
        counter: Counter[str] = Counter()
        for item in items:
            counter[item.get("status", "missing")] += 1
        return dict(sorted(counter.items(), key=lambda pair: pair[0]))

    def verification_counts(items: list[dict[str, str]]) -> dict[str, int]:
        counter: Counter[str] = Counter()
        for item in items:
            counter[item.get("verification_status", "missing")] += 1
        return dict(sorted(counter.items(), key=lambda pair: pair[0]))

    by_type: dict[str, int] = dict(
        sorted(Counter(node.get("type", "missing") for node in nodes).items(), key=lambda pair: pair[0])
    )

    by_layer: dict[str, int] = dict(
        sorted(Counter(node.get("layer", "missing") for node in nodes).items(), key=lambda pair: pair[0])
    )

    by_module: dict[str, int] = dict(
        sorted(Counter(node.get("module", "missing") for node in nodes).items(), key=lambda pair: pair[0])
    )

    return {
        "total_nodes": total,
        "curated_nodes": len(curated),
        "auto_nodes": len(auto),
        "auto_share_percent": pct(len(auto), total),
        "curated_share_percent": pct(len(curated), total),
        "status_counts": status_counts(nodes),
        "verification_counts": verification_counts(nodes),
        "status_counts_curated": status_counts(curated),
        "verification_counts_curated": verification_counts(curated),
        "status_counts_auto": status_counts(auto),
        "verification_counts_auto": verification_counts(auto),
        "by_type": by_type,
        "by_layer": by_layer,
        "by_module": by_module,
    }


def gap_summary(items: list[dict[str, Any]]) -> dict[str, Any]:
    gap_counter: Counter[str] = Counter()
    node_type_counter: Counter[str] = Counter()
    risk_counter: Counter[str] = Counter()
    by_node: dict[str, list[str]] = {}
    by_type_top_examples: dict[str, list[str]] = defaultdict(list)
    by_risk_top_examples: dict[str, list[str]] = defaultdict(list)

    for item in items:
        node = item["node"]
        node_id = node.get("id", "unknown")
        node_type = node.get("type", "missing")
        risk = node.get("risk_level", "unknown")
        node_type_counter[node_type] += 1
        risk_counter[risk] += 1
        by_node[node_id] = item["gaps"]
        if len(by_type_top_examples[node_type]) < 10:
            by_type_top_examples[node_type].append(node_id)
        if len(by_risk_top_examples[risk]) < 10:
            by_risk_top_examples[risk].append(node_id)
        for gap in item["gaps"]:
            gap_counter[gap] += 1

    top_gap_patterns = [
        {"gap": gap, "count": count}
        for gap, count in sorted(gap_counter.items(), key=lambda pair: (-pair[1], pair[0]))[:20]
    ]

    return {
        "gap_node_count": len(items),
        "gap_patterns_top": top_gap_patterns,
        "gap_nodes_by_type": dict(sorted(node_type_counter.items(), key=lambda pair: pair[0])),
        "gap_nodes_by_risk": dict(sorted(risk_counter.items(), key=lambda pair: pair[0])),
        "example_gap_nodes_by_type": dict(sorted(by_type_top_examples.items(), key=lambda pair: pair[0])),
        "example_gap_nodes_by_risk": dict(sorted(by_risk_top_examples.items(), key=lambda pair: pair[0])),
        "gap_map_by_node": by_node,
    }


def build_report(graph_path: Path, *, all_gap_mode: str = "strict") -> dict[str, Any]:
    graph = load_graph(graph_path)
    indexes = build_indexes(graph)
    nodes = list(indexes.nodes_by_id.values())

    curated_gaps = gap_report(indexes, include_auto=False, limit=len(nodes), gap_mode="strict")
    all_gaps = gap_report(indexes, include_auto=True, limit=len(nodes), gap_mode=all_gap_mode)

    return {
        "kind": "architecture_coverage_report",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "graph_path": str(graph_path),
        "all_gap_mode": all_gap_mode,
        "summary": summarize(nodes),
        "curated_gap_summary": gap_summary(curated_gaps),
        "all_gap_summary": gap_summary(all_gaps),
    }


def render_markdown(report: dict[str, Any]) -> str:
    s = report["summary"]
    curated = report["curated_gap_summary"]
    all_scope = report["all_gap_summary"]

    lines = [
        "# Architecture Coverage Report",
        "",
        f"- generated_at: `{report['generated_at']}`",
        f"- graph_path: `{report['graph_path']}`",
        f"- all_gap_mode: `{report['all_gap_mode']}`",
        "",
        "## Node Summary",
        "",
        f"- total nodes: `{s['total_nodes']}`",
        f"- curated nodes: `{s['curated_nodes']}` ({s['curated_share_percent']}%)",
        f"- auto nodes: `{s['auto_nodes']}` ({s['auto_share_percent']}%)",
        "",
        "## Coverage Reality",
        "",
        f"- curated nodes with gaps: `{curated['gap_node_count']}`",
        f"- all-scope nodes with gaps (curated + auto): `{all_scope['gap_node_count']}`",
        "",
        "## Top Gap Patterns (All Scope)",
        "",
    ]
    if not all_scope["gap_patterns_top"]:
        lines.append("- no gaps detected")
    else:
        for item in all_scope["gap_patterns_top"]:
            lines.append(f"- `{item['count']}` x {item['gap']}")

    lines.extend(
        [
            "",
            "## Gap Nodes by Type (All Scope)",
            "",
        ]
    )
    for node_type, count in all_scope["gap_nodes_by_type"].items():
        lines.append(f"- `{node_type}`: `{count}`")

    lines.extend(
        [
            "",
            "## Gap Nodes by Risk (All Scope)",
            "",
        ]
    )
    for risk, count in all_scope["gap_nodes_by_risk"].items():
        lines.append(f"- `{risk}`: `{count}`")

    lines.extend(
        [
            "",
            "## Status Counts (Curated)",
            "",
        ]
    )
    for status, count in s["status_counts_curated"].items():
        lines.append(f"- `{status}`: `{count}`")

    lines.extend(
        [
            "",
            "## Verification Counts (Curated)",
            "",
        ]
    )
    for status, count in s["verification_counts_curated"].items():
        lines.append(f"- `{status}`: `{count}`")

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate architecture coverage report for curated and auto-inventory scope."
    )
    parser.add_argument(
        "--graph-path",
        type=Path,
        default=default_graph_path(),
        help="Path to generated architecture graph JSON.",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=repo_root() / "docs" / "status" / "architecture-coverage-report.json",
        help="Where to write JSON report.",
    )
    parser.add_argument(
        "--md-out",
        type=Path,
        default=repo_root() / "docs" / "status" / "architecture-coverage-report.md",
        help="Where to write Markdown report.",
    )
    parser.add_argument(
        "--all-gap-mode",
        choices=["strict", "operational"],
        default="strict",
        help="Gap mode used for all-scope (curated + auto) audit.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(args.graph_path, all_gap_mode=args.all_gap_mode)

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.write_text(render_markdown(report), encoding="utf-8")

    print(f"json_report={args.json_out}")
    print(f"markdown_report={args.md_out}")
    print(f"curated_gap_nodes={report['curated_gap_summary']['gap_node_count']}")
    print(f"all_gap_nodes={report['all_gap_summary']['gap_node_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
