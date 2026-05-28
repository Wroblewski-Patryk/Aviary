from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


NODE_COLUMNS = [
    "id",
    "name",
    "type",
    "status",
    "layer",
    "module",
    "feature",
    "description",
    "file_path",
    "related_files",
    "parent_id",
    "child_ids",
    "depends_on",
    "used_by",
    "ui_related",
    "api_related",
    "database_related",
    "tests_related",
    "docs_related",
    "agent_related",
    "risk_level",
    "completion_percent",
    "last_verified_at",
    "verification_status",
    "notes",
    "tags",
]

RELATION_COLUMNS = [
    "id",
    "source_id",
    "relation_type",
    "target_id",
    "status",
    "description",
    "evidence",
    "notes",
    "tags",
]

CHAIN_COLUMNS = [
    "id",
    "name",
    "feature_id",
    "status",
    "confidence",
    "trigger_node_id",
    "ordered_node_ids",
    "implementation_evidence",
    "test_evidence",
    "behavior_evidence",
    "connection_evidence",
    "documentation_evidence",
    "missing_links",
    "risk_level",
    "last_verified_at",
    "notes",
    "tags",
]

EVIDENCE_COLUMNS = [
    "id",
    "node_id",
    "evidence_type",
    "status",
    "evidence_path",
    "command",
    "last_verified_at",
    "summary",
    "notes",
    "tags",
]

RESEARCH_SOURCE_COLUMNS = [
    "id",
    "title",
    "authors",
    "year",
    "field",
    "source_type",
    "publication",
    "doi",
    "url",
    "relevance_summary",
    "review_status",
    "last_reviewed_at",
    "notes",
    "tags",
]

THEORY_CLAIM_COLUMNS = [
    "id",
    "node_id",
    "claim",
    "claim_type",
    "status",
    "confidence",
    "source_ids",
    "code_expression",
    "applicability_scope",
    "limitations",
    "last_reviewed_at",
    "reviewer",
    "notes",
    "tags",
]

VALID_NODE_STATUSES = {
    "planned",
    "in_progress",
    "implemented",
    "broken",
    "missing",
    "deprecated",
    "tested",
    "verified",
    "blocked",
}

VALID_VERIFICATION_STATUSES = {
    "missing_evidence",
    "implementation_evidence",
    "test_evidence",
    "behavior_evidence",
    "connection_evidence",
    "documentation_evidence",
    "verified",
    "blocked",
}

VALID_RELATION_TYPES = {
    "depends_on",
    "used_by",
    "calls",
    "renders",
    "routes_to",
    "reads",
    "writes",
    "emits",
    "consumes",
    "tests",
    "documents",
    "verifies",
    "parent_of",
    "child_of",
    "configured_by",
    "generated_from",
    "owned_by",
}

VALID_CHAIN_STATUSES = {"complete", "partial", "blocked", "missing", "verified", "in_progress"}

VALID_RESEARCH_REVIEW_STATUSES = {"candidate", "reviewed", "superseded", "rejected"}

VALID_THEORY_CLAIM_STATUSES = {"proposed", "mapped", "needs_sources", "reviewed", "disputed", "retired"}


@dataclass(frozen=True)
class Registry:
    nodes: list[dict[str, str]]
    relations: list[dict[str, str]]
    chains: list[dict[str, str]]
    evidence: list[dict[str, str]]
    research_sources: list[dict[str, str]]
    theory_claims: list[dict[str, str]]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def read_csv(path: Path, required_columns: list[str]) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [column for column in required_columns if column not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"{path.relative_to(repo_root())} missing columns: {', '.join(missing)}")
        return [{key: (value or "").strip() for key, value in row.items()} for row in reader]


def split_refs(value: str) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in re.split(r"[|;]", value) if part.strip()]


def slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-").lower() or "node"


def md_link(node_id: str, known_ids: set[str]) -> str:
    if node_id in known_ids:
        return f"[[{slug(node_id)}|{node_id}]]"
    return f"`{node_id}`"


def yaml_list(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(json.dumps(value) for value in values) + "]"


def validate_registry(registry: Registry) -> list[str]:
    errors: list[str] = []
    node_ids = [row["id"] for row in registry.nodes]
    duplicates = [node_id for node_id, count in Counter(node_ids).items() if count > 1]
    if duplicates:
        errors.append("Duplicate node ids: " + ", ".join(sorted(duplicates)))

    relation_ids = [row["id"] for row in registry.relations]
    relation_duplicates = [relation_id for relation_id, count in Counter(relation_ids).items() if count > 1]
    if relation_duplicates:
        errors.append("Duplicate relation ids: " + ", ".join(sorted(relation_duplicates)))

    chain_ids = [row["id"] for row in registry.chains]
    chain_duplicates = [chain_id for chain_id, count in Counter(chain_ids).items() if count > 1]
    if chain_duplicates:
        errors.append("Duplicate chain ids: " + ", ".join(sorted(chain_duplicates)))

    evidence_ids = [row["id"] for row in registry.evidence]
    evidence_duplicates = [evidence_id for evidence_id, count in Counter(evidence_ids).items() if count > 1]
    if evidence_duplicates:
        errors.append("Duplicate evidence ids: " + ", ".join(sorted(evidence_duplicates)))

    known = set(node_ids)
    for row in registry.nodes:
        if not row["id"]:
            errors.append("Node row with missing id")
        if row["status"] not in VALID_NODE_STATUSES:
            errors.append(f"{row['id']} invalid status {row['status']!r}")
        if row["verification_status"] not in VALID_VERIFICATION_STATUSES:
            errors.append(f"{row['id']} invalid verification_status {row['verification_status']!r}")
        for column in [
            "parent_id",
            "child_ids",
            "depends_on",
            "used_by",
            "ui_related",
            "api_related",
            "database_related",
            "tests_related",
            "docs_related",
            "agent_related",
        ]:
            for ref in split_refs(row[column]):
                if ref and ref not in known:
                    errors.append(f"{row['id']} references missing node {ref} in {column}")

    for row in registry.relations:
        if row["relation_type"] not in VALID_RELATION_TYPES:
            errors.append(f"{row['id']} invalid relation_type {row['relation_type']!r}")
        if row["source_id"] not in known:
            errors.append(f"{row['id']} missing source node {row['source_id']}")
        if row["target_id"] not in known and not row["target_id"].startswith("docs/"):
            errors.append(f"{row['id']} missing target node {row['target_id']}")

    for row in registry.chains:
        if row["status"] not in VALID_CHAIN_STATUSES:
            errors.append(f"{row['id']} invalid chain status {row['status']!r}")
        if row["feature_id"] not in known:
            errors.append(f"{row['id']} missing feature node {row['feature_id']}")
        if row["trigger_node_id"] not in known:
            errors.append(f"{row['id']} missing trigger node {row['trigger_node_id']}")
        for ref in [part.strip() for part in row["ordered_node_ids"].split(">") if part.strip()]:
            if ref not in known and not ref.startswith("docs/"):
                errors.append(f"{row['id']} missing ordered node {ref}")

    for row in registry.evidence:
        if row["node_id"] not in known:
            errors.append(f"{row['id']} missing evidence node {row['node_id']}")

    research_ids = [row["id"] for row in registry.research_sources]
    research_duplicates = [source_id for source_id, count in Counter(research_ids).items() if count > 1]
    if research_duplicates:
        errors.append("Duplicate research source ids: " + ", ".join(sorted(research_duplicates)))
    research_known = set(research_ids)
    for row in registry.research_sources:
        if row["review_status"] not in VALID_RESEARCH_REVIEW_STATUSES:
            errors.append(f"{row['id']} invalid review_status {row['review_status']!r}")

    theory_ids = [row["id"] for row in registry.theory_claims]
    theory_duplicates = [claim_id for claim_id, count in Counter(theory_ids).items() if count > 1]
    if theory_duplicates:
        errors.append("Duplicate theory claim ids: " + ", ".join(sorted(theory_duplicates)))
    for row in registry.theory_claims:
        if row["node_id"] not in known:
            errors.append(f"{row['id']} missing claim node {row['node_id']}")
        if row["status"] not in VALID_THEORY_CLAIM_STATUSES:
            errors.append(f"{row['id']} invalid claim status {row['status']!r}")
        source_refs = split_refs(row["source_ids"])
        if row["status"] in {"mapped", "reviewed"} and len(source_refs) < 3:
            errors.append(f"{row['id']} needs at least 3 research sources for status {row['status']!r}")
        for ref in source_refs:
            if ref not in research_known:
                errors.append(f"{row['id']} references missing research source {ref}")

    return errors


def load_registry(root: Path) -> Registry:
    registry_dir = root / "docs" / "architecture" / "registry"
    curated_nodes = read_csv(registry_dir / "nodes.csv", NODE_COLUMNS)
    auto_nodes = read_csv(registry_dir / "auto_nodes.csv", NODE_COLUMNS)
    curated_relations = read_csv(registry_dir / "relations.csv", RELATION_COLUMNS)
    auto_relations = read_csv(registry_dir / "auto_relations.csv", RELATION_COLUMNS)
    return Registry(
        nodes=curated_nodes + auto_nodes,
        relations=curated_relations + auto_relations,
        chains=read_csv(registry_dir / "chains.csv", CHAIN_COLUMNS),
        evidence=read_csv(registry_dir / "evidence.csv", EVIDENCE_COLUMNS),
        research_sources=read_csv(registry_dir / "research_sources.csv", RESEARCH_SOURCE_COLUMNS),
        theory_claims=read_csv(registry_dir / "theory_claims.csv", THEORY_CLAIM_COLUMNS),
    )


def relation_maps(relations: list[dict[str, str]]) -> tuple[dict[str, list[dict[str, str]]], dict[str, list[dict[str, str]]]]:
    outgoing: dict[str, list[dict[str, str]]] = defaultdict(list)
    incoming: dict[str, list[dict[str, str]]] = defaultdict(list)
    for relation in relations:
        outgoing[relation["source_id"]].append(relation)
        incoming[relation["target_id"]].append(relation)
    return outgoing, incoming


def evidence_map(evidence: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    mapped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for item in evidence:
        mapped[item["node_id"]].append(item)
    return mapped


def chain_map(chains: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    mapped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for chain in chains:
        mapped[chain["feature_id"]].append(chain)
        mapped[chain["trigger_node_id"]].append(chain)
        for ref in [part.strip() for part in chain["ordered_node_ids"].split(">") if part.strip()]:
            mapped[ref].append(chain)
    return mapped


def theory_claim_map(claims: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    mapped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for claim in claims:
        mapped[claim["node_id"]].append(claim)
    return mapped


def write_node_pages(root: Path, registry: Registry) -> None:
    nodes_dir = root / "docs" / "architecture" / "nodes"
    nodes_dir.mkdir(parents=True, exist_ok=True)
    known = {row["id"] for row in registry.nodes}
    expected_filenames = {f"{slug(row['id'])}.md" for row in registry.nodes}
    for stale_path in nodes_dir.glob("*.md"):
        if stale_path.name not in expected_filenames:
            stale_path.unlink()
    outgoing, incoming = relation_maps(registry.relations)
    evidence_by_node = evidence_map(registry.evidence)
    chains_by_node = chain_map(registry.chains)
    claims_by_node = theory_claim_map(registry.theory_claims)
    research_by_id = {source["id"]: source for source in registry.research_sources}

    for row in registry.nodes:
        node_id = row["id"]
        path = nodes_dir / f"{slug(node_id)}.md"
        tags = [tag.lstrip("#") for tag in split_refs(row["tags"].replace(" ", "|")) if tag.startswith("#")]
        frontmatter = [
            "---",
            f"id: {json.dumps(node_id)}",
            f"name: {json.dumps(row['name'])}",
            f"type: {json.dumps(row['type'])}",
            f"status: {json.dumps(row['status'])}",
            f"layer: {json.dumps(row['layer'])}",
            f"module: {json.dumps(row['module'])}",
            f"feature: {json.dumps(row['feature'])}",
            f"risk_level: {json.dumps(row['risk_level'])}",
            f"completion_percent: {json.dumps(row['completion_percent'])}",
            f"last_verified_at: {json.dumps(row['last_verified_at'])}",
            f"verification_status: {json.dumps(row['verification_status'])}",
            f"file_path: {json.dumps(row['file_path'])}",
            f"related_files: {yaml_list(split_refs(row['related_files']))}",
            f"tags: {yaml_list(tags)}",
            "---",
            "",
        ]
        lines = frontmatter + [
            f"# {row['name']}",
            "",
            f"ID: `{node_id}`",
            "",
            "## Summary",
            "",
            row["description"],
            "",
            "## Links",
            "",
            f"- parent: {md_link(row['parent_id'], known) if row['parent_id'] else 'none'}",
            "- children: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["child_ids"])) or "none"),
            "- depends_on: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["depends_on"])) or "none"),
            "- used_by: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["used_by"])) or "none"),
            "- ui_related: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["ui_related"])) or "none"),
            "- api_related: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["api_related"])) or "none"),
            "- database_related: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["database_related"])) or "none"),
            "- tests_related: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["tests_related"])) or "none"),
            "- docs_related: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["docs_related"])) or "none"),
            "- agent_related: "
            + (", ".join(md_link(ref, known) for ref in split_refs(row["agent_related"])) or "none"),
            "",
            "## Relations",
            "",
        ]
        if outgoing[node_id]:
            lines.append("Outgoing:")
            for relation in outgoing[node_id]:
                target = md_link(relation["target_id"], known)
                lines.append(f"- `{relation['relation_type']}` -> {target}: {relation['description']}")
        else:
            lines.append("Outgoing: none")
        lines.append("")
        if incoming[node_id]:
            lines.append("Incoming:")
            for relation in incoming[node_id]:
                source = md_link(relation["source_id"], known)
                lines.append(f"- {source} -> `{relation['relation_type']}`: {relation['description']}")
        else:
            lines.append("Incoming: none")
        lines.extend(["", "## Chains", ""])
        unique_chains = {chain["id"]: chain for chain in chains_by_node[node_id]}.values()
        if unique_chains:
            for chain in sorted(unique_chains, key=lambda item: item["id"]):
                lines.append(f"- `{chain['id']}` {chain['name']} ({chain['status']}, {chain['confidence']})")
        else:
            lines.append("- none")
        lines.extend(["", "## Evidence", ""])
        if evidence_by_node[node_id]:
            for item in evidence_by_node[node_id]:
                command = f" Command: `{item['command']}`." if item["command"] else ""
                lines.append(
                    f"- `{item['id']}` {item['evidence_type']} {item['status']}: "
                    f"{item['summary']} (`{item['evidence_path']}`).{command}"
                )
        else:
            lines.append("- missing")
        lines.extend(["", "## Theory Claims", ""])
        if claims_by_node[node_id]:
            for claim in claims_by_node[node_id]:
                source_links = []
                for source_id in split_refs(claim["source_ids"]):
                    source = research_by_id.get(source_id)
                    if source:
                        source_links.append(f"[{source_id}]({source['url']})")
                    else:
                        source_links.append(f"`{source_id}`")
                lines.extend(
                    [
                        f"### {claim['id']}",
                        "",
                        claim["claim"],
                        "",
                        f"- status: `{claim['status']}`",
                        f"- confidence: `{claim['confidence']}`",
                        f"- code expression: `{claim['code_expression']}`",
                        f"- applicability: {claim['applicability_scope']}",
                        f"- limitations: {claim['limitations']}",
                        "- sources: " + (", ".join(source_links) or "none"),
                        "",
                    ]
                )
        else:
            lines.append("- none")
        lines.extend(["", "## Notes", "", row["notes"] or "none", ""])
        path.write_text("\n".join(lines), encoding="utf-8")


def write_relations_index(root: Path, registry: Registry) -> None:
    known = {row["id"] for row in registry.nodes}
    path = root / "docs" / "architecture" / "relations" / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Architecture Relations",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "| ID | Source | Type | Target | Status | Description |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for relation in registry.relations:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{relation['id']}`",
                    md_link(relation["source_id"], known),
                    f"`{relation['relation_type']}`",
                    md_link(relation["target_id"], known),
                    relation["status"],
                    relation["description"],
                ]
            )
            + " |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_chains_index(root: Path, registry: Registry) -> None:
    known = {row["id"] for row in registry.nodes}
    path = root / "docs" / "architecture" / "chains" / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Function Chains",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
    ]
    for chain in registry.chains:
        ordered = [part.strip() for part in chain["ordered_node_ids"].split(">") if part.strip()]
        lines.extend(
            [
                f"## {chain['name']}",
                "",
                f"- ID: `{chain['id']}`",
                f"- feature: {md_link(chain['feature_id'], known)}",
                f"- status: `{chain['status']}`",
                f"- confidence: `{chain['confidence']}`",
                f"- risk: `{chain['risk_level']}`",
                f"- trigger: {md_link(chain['trigger_node_id'], known)}",
                f"- last verified: `{chain['last_verified_at']}`",
                "",
                "Execution chain:",
                "",
                " -> ".join(md_link(ref, known) for ref in ordered),
                "",
                "Evidence:",
                "",
                f"- implementation: {chain['implementation_evidence']}",
                f"- test: {chain['test_evidence']}",
                f"- behavior: {chain['behavior_evidence']}",
                f"- connection: {chain['connection_evidence']}",
                f"- documentation: {chain['documentation_evidence']}",
                f"- missing links: {chain['missing_links'] or 'none'}",
                "",
                chain["notes"],
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_graph_exports(root: Path, registry: Registry) -> None:
    graph_dir = root / "docs" / "architecture" / "graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)
    graph = {
        "generated_at": date.today().isoformat(),
        "nodes": registry.nodes,
        "relations": registry.relations,
        "chains": registry.chains,
        "evidence": registry.evidence,
        "research_sources": registry.research_sources,
        "theory_claims": registry.theory_claims,
    }
    (graph_dir / "architecture-graph.json").write_text(json.dumps(graph, indent=2), encoding="utf-8")

    known = {row["id"] for row in registry.nodes}
    lines = ["graph TD"]
    for node in registry.nodes:
        safe = slug(node["id"]).replace("-", "_")
        label = f"{node['id']}\\n{node['name']}"
        lines.append(f'  {safe}["{label}"]')
    for relation in registry.relations:
        if relation["source_id"] in known and relation["target_id"] in known:
            source = slug(relation["source_id"]).replace("-", "_")
            target = slug(relation["target_id"]).replace("-", "_")
            label = relation["relation_type"]
            lines.append(f"  {source} -- {label} --> {target}")
    (graph_dir / "architecture-graph.mmd").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_status_rollup(root: Path, registry: Registry) -> None:
    path = root / "docs" / "status" / "architecture-map-status.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    by_status = Counter(row["status"] for row in registry.nodes)
    by_type = Counter(row["type"] for row in registry.nodes)
    by_verification = Counter(row["verification_status"] for row in registry.nodes)
    curated_non_verified = [
        row
        for row in registry.nodes
        if "#auto" not in row["tags"] and (row["status"] != "verified" or row["verification_status"] != "verified")
    ]
    auto_nodes = [row for row in registry.nodes if "#auto" in row["tags"]]
    auto_by_type = Counter(row["type"] for row in auto_nodes)
    lines = [
        "# Architecture Map Status",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Counts By Status",
        "",
        "| Status | Count |",
        "| --- | --- |",
    ]
    for key, value in sorted(by_status.items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## Counts By Type", "", "| Type | Count |", "| --- | --- |"])
    for key, value in sorted(by_type.items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## Counts By Verification Status", "", "| Verification | Count |", "| --- | --- |"])
    for key, value in sorted(by_verification.items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## Curated Non-Verified Nodes", "", "| ID | Name | Status | Verification | Next note |", "| --- | --- | --- | --- | --- |"])
    for row in curated_non_verified:
        lines.append(
            f"| [[{slug(row['id'])}|{row['id']}]] | {row['name']} | `{row['status']}` | "
            f"`{row['verification_status']}` | {row['notes']} |"
        )
    if not curated_non_verified:
        lines.append("| none | none | none | none | none |")
    lines.extend(["", "## Auto Inventory Coverage", "", f"- auto nodes: `{len(auto_nodes)}`", ""])
    lines.extend(["| Type | Count |", "| --- | --- |"])
    for key, value in sorted(auto_by_type.items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "Auto-discovered rows are broad map coverage. Promote them into curated CSVs when a feature, release gate, or agent mission depends on them.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_evidence_rollup(root: Path, registry: Registry) -> None:
    known = {row["id"] for row in registry.nodes}
    path = root / "docs" / "testing" / "architecture-evidence-map.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Architecture Evidence Map",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "| Evidence | Node | Type | Status | Path | Command | Summary |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in registry.evidence:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['id']}`",
                    md_link(item["node_id"], known),
                    item["evidence_type"],
                    item["status"],
                    f"`{item['evidence_path']}`",
                    f"`{item['command']}`" if item["command"] else "",
                    item["summary"],
                ]
            )
            + " |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_research_rollup(root: Path, registry: Registry) -> None:
    known = {row["id"] for row in registry.nodes}
    sources = {row["id"]: row for row in registry.research_sources}
    path = root / "docs" / "testing" / "architecture-research-map.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Architecture Research Map",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "Research evidence is not runtime proof. It records whether a code-level cognitive or neuroscience-inspired claim has literature support, scope, and limitations.",
        "",
        "## Theory Claims",
        "",
        "| Claim | Node | Status | Confidence | Sources | Code Expression | Scope | Limitations |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for claim in registry.theory_claims:
        source_links = []
        for source_id in split_refs(claim["source_ids"]):
            source = sources.get(source_id)
            if source:
                source_links.append(f"[{source_id}]({source['url']})")
            else:
                source_links.append(f"`{source_id}`")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{claim['id']}`",
                    md_link(claim["node_id"], known),
                    claim["status"],
                    claim["confidence"],
                    ", ".join(source_links),
                    f"`{claim['code_expression']}`",
                    claim["applicability_scope"],
                    claim["limitations"],
                ]
            )
            + " |"
        )
    lines.extend(["", "## Research Sources", "", "| Source | Year | Field | Publication | DOI | Review | Relevance |", "| --- | --- | --- | --- | --- | --- | --- |"])
    for source in registry.research_sources:
        doi = f"[{source['doi']}](https://doi.org/{source['doi']})" if source["doi"] else ""
        lines.append(
            "| "
            + " | ".join(
                [
                    f"[{source['id']}]({source['url']})",
                    source["year"],
                    source["field"],
                    source["publication"],
                    doi,
                    source["review_status"],
                    source["relevance_summary"],
                ]
            )
            + " |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    root = repo_root()
    registry = load_registry(root)
    errors = validate_registry(registry)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    write_node_pages(root, registry)
    write_relations_index(root, registry)
    write_chains_index(root, registry)
    write_graph_exports(root, registry)
    write_status_rollup(root, registry)
    write_evidence_rollup(root, registry)
    write_research_rollup(root, registry)

    print(f"nodes={len(registry.nodes)}")
    print(f"relations={len(registry.relations)}")
    print(f"chains={len(registry.chains)}")
    print(f"evidence={len(registry.evidence)}")
    print(f"research_sources={len(registry.research_sources)}")
    print(f"theory_claims={len(registry.theory_claims)}")
    print("wrote docs/architecture/nodes")
    print("wrote docs/architecture/relations/index.md")
    print("wrote docs/architecture/chains/index.md")
    print("wrote docs/architecture/graphs/architecture-graph.json")
    print("wrote docs/architecture/graphs/architecture-graph.mmd")
    print("wrote docs/status/architecture-map-status.md")
    print("wrote docs/testing/architecture-evidence-map.md")
    print("wrote docs/testing/architecture-research-map.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
