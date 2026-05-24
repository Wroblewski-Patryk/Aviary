from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROOF_COLUMNS = [
    "tests_related",
    "docs_related",
]

VERIFIED_STATUSES = {"verified", "tested"}
GAP_MODES = {"strict", "operational"}


@dataclass(frozen=True)
class GraphIndexes:
    graph: dict[str, Any]
    nodes_by_id: dict[str, dict[str, str]]
    outgoing_by_id: dict[str, list[dict[str, str]]]
    incoming_by_id: dict[str, list[dict[str, str]]]
    chains_by_node_id: dict[str, list[dict[str, str]]]
    evidence_by_node_id: dict[str, list[dict[str, str]]]
    claims_by_node_id: dict[str, list[dict[str, str]]]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_graph_path() -> Path:
    return repo_root() / "docs" / "architecture" / "graphs" / "architecture-graph.json"


def split_refs(value: str) -> list[str]:
    if not value:
        return []
    parts = value.replace(";", "|").split("|")
    return [part.strip() for part in parts if part.strip()]


def split_chain_nodes(value: str) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(">") if part.strip()]


def load_graph(path: Path | None = None) -> dict[str, Any]:
    graph_path = path or default_graph_path()
    if not graph_path.exists():
        raise FileNotFoundError(f"Architecture graph export not found: {graph_path}")
    return json.loads(graph_path.read_text(encoding="utf-8"))


def build_indexes(graph: dict[str, Any]) -> GraphIndexes:
    nodes_by_id = {node["id"]: node for node in graph.get("nodes", [])}
    outgoing_by_id: dict[str, list[dict[str, str]]] = {}
    incoming_by_id: dict[str, list[dict[str, str]]] = {}
    chains_by_node_id: dict[str, list[dict[str, str]]] = {}
    evidence_by_node_id: dict[str, list[dict[str, str]]] = {}
    claims_by_node_id: dict[str, list[dict[str, str]]] = {}

    for relation in graph.get("relations", []):
        outgoing_by_id.setdefault(relation["source_id"], []).append(relation)
        incoming_by_id.setdefault(relation["target_id"], []).append(relation)

    for chain in graph.get("chains", []):
        node_ids = {chain["feature_id"], chain["trigger_node_id"], *split_chain_nodes(chain["ordered_node_ids"])}
        for node_id in node_ids:
            chains_by_node_id.setdefault(node_id, []).append(chain)

    for evidence in graph.get("evidence", []):
        evidence_by_node_id.setdefault(evidence["node_id"], []).append(evidence)

    for claim in graph.get("theory_claims", []):
        claims_by_node_id.setdefault(claim["node_id"], []).append(claim)

    return GraphIndexes(
        graph=graph,
        nodes_by_id=nodes_by_id,
        outgoing_by_id=outgoing_by_id,
        incoming_by_id=incoming_by_id,
        chains_by_node_id=chains_by_node_id,
        evidence_by_node_id=evidence_by_node_id,
        claims_by_node_id=claims_by_node_id,
    )


def search_nodes(indexes: GraphIndexes, term: str, *, limit: int = 20) -> list[dict[str, str]]:
    needle = term.casefold()
    searchable_fields = ["id", "name", "type", "module", "feature", "description", "file_path", "tags"]
    matches = [
        node
        for node in indexes.nodes_by_id.values()
        if any(needle in str(node.get(field, "")).casefold() for field in searchable_fields)
    ]
    return sorted(
        matches,
        key=lambda node: (
            "#auto" in node.get("tags", ""),
            not node["id"].casefold().startswith(needle),
            node["id"].casefold(),
            node["name"].casefold(),
        ),
    )[:limit]


def suggest_nodes(indexes: GraphIndexes, node_id: str, *, limit: int = 8) -> list[dict[str, str]]:
    pieces = [piece for piece in node_id.replace("_", "-").split("-") if piece]
    matches: dict[str, dict[str, str]] = {}
    for piece in pieces or [node_id]:
        for node in search_nodes(indexes, piece, limit=limit):
            matches[node["id"]] = node
    return list(matches.values())[:limit]


def find_node(indexes: GraphIndexes, node_id: str) -> dict[str, str]:
    try:
        return indexes.nodes_by_id[node_id]
    except KeyError as exc:
        suggestions = ", ".join(node["id"] for node in suggest_nodes(indexes, node_id)) or "none"
        raise KeyError(f"Unknown architecture node {node_id!r}. Suggestions: {suggestions}") from exc


def detect_gaps(
    node: dict[str, str],
    evidence: list[dict[str, str]],
    chains: list[dict[str, str]],
    claims: list[dict[str, str]],
    *,
    incoming_count: int,
    outgoing_count: int,
    mode: str = "strict",
) -> list[str]:
    if mode not in GAP_MODES:
        raise ValueError(f"Unsupported gap mode: {mode}")

    gaps: list[str] = []
    is_auto = "#auto" in node.get("tags", "")

    # Operational mode treats auto-inventory rows as structural coverage unless
    # they are promoted to higher-risk workflow/feature surfaces.
    if mode == "operational" and is_auto:
        if incoming_count + outgoing_count <= 0:
            gaps.append("auto node has no relation coverage")
        if node.get("type") in {"feature", "workflow", "api_route"} and not chains:
            gaps.append("no function chains include this node")
        for claim in claims:
            if claim.get("status") in {"needs_sources", "proposed", "disputed"}:
                gaps.append(f"{claim['id']} research status is {claim.get('status')}")
        return gaps

    if node.get("status") not in VERIFIED_STATUSES:
        gaps.append(f"node status is {node.get('status') or 'missing'}")
    if node.get("verification_status") != "verified":
        gaps.append(f"verification status is {node.get('verification_status') or 'missing'}")
    for column in PROOF_COLUMNS:
        if not split_refs(node.get(column, "")):
            gaps.append(f"{column} is empty")
    if not evidence:
        gaps.append("no evidence rows")
    if node.get("type") in {"feature", "workflow", "api_route", "ui_element"} and not chains:
        gaps.append("no function chains include this node")
    chain_gap_node_types = {"feature", "api_route", "ui_element", "event", "workflow"}
    for chain in chains:
        missing_links = chain.get("missing_links", "").strip()
        if missing_links and missing_links.lower() != "none" and node.get("type") in chain_gap_node_types:
            gaps.append(f"{chain['id']} missing links: {missing_links}")
        if chain.get("status") not in {"verified", "complete"}:
            gaps.append(f"{chain['id']} status is {chain.get('status')}")
    for claim in claims:
        if claim.get("status") in {"needs_sources", "proposed", "disputed"}:
            gaps.append(f"{claim['id']} research status is {claim.get('status')}")
    return gaps


def query_node(indexes: GraphIndexes, node_id: str, *, gap_mode: str = "strict") -> dict[str, Any]:
    node = find_node(indexes, node_id)
    outgoing = indexes.outgoing_by_id.get(node_id, [])
    incoming = indexes.incoming_by_id.get(node_id, [])
    chains = sorted(
        {chain["id"]: chain for chain in indexes.chains_by_node_id.get(node_id, [])}.values(),
        key=lambda chain: chain["id"],
    )
    evidence = sorted(indexes.evidence_by_node_id.get(node_id, []), key=lambda item: item["id"])
    claims = sorted(indexes.claims_by_node_id.get(node_id, []), key=lambda item: item["id"])
    return {
        "node": node,
        "outgoing_relations": sorted(outgoing, key=lambda relation: relation["id"]),
        "incoming_relations": sorted(incoming, key=lambda relation: relation["id"]),
        "chains": chains,
        "evidence": evidence,
        "theory_claims": claims,
        "gaps": detect_gaps(
            node,
            evidence,
            chains,
            claims,
            incoming_count=len(incoming),
            outgoing_count=len(outgoing),
            mode=gap_mode,
        ),
    }


def gap_report(
    indexes: GraphIndexes,
    *,
    include_auto: bool = False,
    limit: int = 50,
    gap_mode: str = "strict",
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for node in indexes.nodes_by_id.values():
        if not include_auto and "#auto" in node.get("tags", ""):
            continue
        result = query_node(indexes, node["id"], gap_mode=gap_mode)
        if result["gaps"]:
            results.append(
                {
                    "node": result["node"],
                    "gaps": result["gaps"],
                    "evidence_count": len(result["evidence"]),
                    "chain_count": len(result["chains"]),
                    "incoming_count": len(result["incoming_relations"]),
                    "outgoing_count": len(result["outgoing_relations"]),
                }
            )
    return sorted(
        results,
        key=lambda item: (
            item["node"].get("risk_level") != "high",
            -len(item["gaps"]),
            item["node"]["id"].casefold(),
        ),
    )[:limit]


def relation_line(relation: dict[str, str], *, direction: str) -> str:
    if direction == "outgoing":
        return f"- `{relation['relation_type']}` -> `{relation['target_id']}`: {relation['description']}"
    return f"- `{relation['source_id']}` -> `{relation['relation_type']}`: {relation['description']}"


def render_search_markdown(matches: list[dict[str, str]], term: str) -> str:
    lines = [f"# Architecture Graph Search: {term}", ""]
    if not matches:
        lines.append("- no matches")
        return "\n".join(lines) + "\n"
    for node in matches:
        lines.append(f"- `{node['id']}` {node['name']} ({node['type']}, {node['status']})")
    return "\n".join(lines) + "\n"


def render_gap_report_markdown(items: list[dict[str, Any]], *, include_auto: bool) -> str:
    scope = "curated and auto-inventory nodes" if include_auto else "curated nodes"
    lines = [f"# Architecture Graph Gap Audit ({scope})", ""]
    if not items:
        lines.append("- no gaps detected")
        return "\n".join(lines) + "\n"
    for item in items:
        node = item["node"]
        lines.extend(
            [
                f"## {node['id']} - {node['name']}",
                "",
                f"- type/status: `{node['type']}` / `{node['status']}`",
                f"- verification: `{node['verification_status']}`",
                f"- risk: `{node['risk_level']}`",
                f"- evidence/chains/relations: `{item['evidence_count']}` / `{item['chain_count']}` / `{item['incoming_count'] + item['outgoing_count']}`",
                "- gaps:",
            ]
        )
        lines.extend(f"  - {gap}" for gap in item["gaps"])
        lines.append("")
    return "\n".join(lines)


def render_node_markdown(result: dict[str, Any], *, show_gaps: bool) -> str:
    node = result["node"]
    lines = [
        f"# Architecture Node: {node['id']}",
        "",
        f"- name: {node['name']}",
        f"- type: `{node['type']}`",
        f"- status: `{node['status']}`",
        f"- verification: `{node['verification_status']}`",
        f"- layer/module/feature: `{node['layer']}` / `{node['module']}` / `{node['feature']}`",
        f"- file: `{node['file_path']}`",
        f"- description: {node['description']}",
        "",
        "## Impact",
        "",
        "Outgoing:",
    ]
    lines.extend([relation_line(relation, direction="outgoing") for relation in result["outgoing_relations"]] or ["- none"])
    lines.extend(["", "Incoming:"])
    lines.extend([relation_line(relation, direction="incoming") for relation in result["incoming_relations"]] or ["- none"])
    lines.extend(["", "## Function Chains", ""])
    if result["chains"]:
        for chain in result["chains"]:
            lines.append(f"- `{chain['id']}` {chain['name']} ({chain['status']}, {chain['confidence']})")
    else:
        lines.append("- none")
    lines.extend(["", "## Evidence", ""])
    if result["evidence"]:
        for item in result["evidence"]:
            command = f" command: `{item['command']}`" if item["command"] else ""
            lines.append(f"- `{item['id']}` {item['evidence_type']} {item['status']}: {item['summary']}{command}")
    else:
        lines.append("- missing")
    lines.extend(["", "## Theory Claims", ""])
    if result["theory_claims"]:
        for claim in result["theory_claims"]:
            source_count = len(split_refs(claim["source_ids"]))
            lines.append(f"- `{claim['id']}` {claim['status']} with {source_count} sources: {claim['claim']}")
    else:
        lines.append("- none")
    if show_gaps:
        lines.extend(["", "## Gaps", ""])
        lines.extend([f"- {gap}" for gap in result["gaps"]] or ["- none"])
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query the generated Aviary architecture graph export.")
    parser.add_argument("--graph", type=Path, default=default_graph_path(), help="Path to architecture-graph.json.")
    parser.add_argument("--node", help="Exact architecture node id to inspect.")
    parser.add_argument("--search", help="Case-insensitive node search term.")
    parser.add_argument("--gaps", action="store_true", help="Report nodes with missing proof or incomplete chain signals.")
    parser.add_argument("--include-auto", action="store_true", help="Include auto-inventory rows in --gaps output.")
    parser.add_argument(
        "--fail-on-gaps",
        action="store_true",
        help="Return exit code 1 when --gaps output contains at least one item.",
    )
    parser.add_argument("--limit", type=int, default=20, help="Maximum search results.")
    parser.add_argument("--show-gaps", action="store_true", help="Include missing-proof and incomplete-chain gaps.")
    parser.add_argument(
        "--gap-mode",
        choices=sorted(GAP_MODES),
        default="strict",
        help="Gap policy mode: strict for full proof expectations, operational for structural auto-inventory posture.",
    )
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format.")
    args = parser.parse_args(argv)
    if sum(bool(value) for value in [args.node, args.search, args.gaps]) != 1:
        parser.error("Provide exactly one of --node, --search, or --gaps.")
    if args.include_auto and not args.gaps:
        parser.error("--include-auto can only be used with --gaps.")
    if args.fail_on_gaps and not args.gaps:
        parser.error("--fail-on-gaps can only be used with --gaps.")
    return args


def run(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        indexes = build_indexes(load_graph(args.graph))
        if args.search:
            matches = search_nodes(indexes, args.search, limit=args.limit)
            output: Any = {"search": args.search, "matches": matches}
            text = json.dumps(output, indent=2) if args.format == "json" else render_search_markdown(matches, args.search)
            exit_code = 0
        elif args.gaps:
            items = gap_report(indexes, include_auto=args.include_auto, limit=args.limit, gap_mode=args.gap_mode)
            output = {"include_auto": args.include_auto, "gap_mode": args.gap_mode, "items": items}
            text = json.dumps(output, indent=2) if args.format == "json" else render_gap_report_markdown(items, include_auto=args.include_auto)
            exit_code = 1 if args.fail_on_gaps and items else 0
        else:
            result = query_node(indexes, args.node, gap_mode=args.gap_mode)
            text = json.dumps(result, indent=2) if args.format == "json" else render_node_markdown(result, show_gaps=args.show_gaps)
            exit_code = 0
        print(text, end="" if text.endswith("\n") else "\n")
        return exit_code
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


def main() -> int:
    return run(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
