---
id: "SCRIPT-QUERY-ARCH-GRAPH"
name: "Query Architecture Graph Script"
type: "script"
status: "verified"
layer: "ops"
module: "architecture"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/scripts/query_architecture_graph.py"
related_files: ["docs/architecture/graphs/architecture-graph.json"]
tags: ["aviary", "script", "architecture_graph", "query", "verified"]
---

# Query Architecture Graph Script

ID: `SCRIPT-QUERY-ARCH-GRAPH`

## Summary

Read-only CLI for querying generated architecture graph nodes search results impact chains evidence research claims and proof gaps

## Links

- parent: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- children: none
- depends_on: [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]], [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- used_by: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-query|TEST-ARCH-GRAPH-QUERY]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `depends_on` -> [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]]: Query CLI reads the generated graph JSON produced by the graph generator
- `documents` -> [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]: Graph-system documentation describes the local query workflow

Incoming:
- [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]] -> `parent_of`: Architecture graph workflow owns the local query utility for systemic analysis
- [[test-arch-graph-query|TEST-ARCH-GRAPH-QUERY]] -> `verifies`: Focused query tests verify node lookup search impact chains evidence theory claims gap detection JSON output and suggestions

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-ARCH-GRAPH-QUERY-CLI` behavior verified: Architecture graph query CLI can inspect node details incoming and outgoing impact chains evidence theory claims and missing-proof gaps from generated graph JSON (`backend/scripts/query_architecture_graph.py`). Command: `python scripts/query_architecture_graph.py --node WORKFLOW-ARCH-GRAPH --show-gaps`.
- `EVID-ARCH-GRAPH-GAP-AUDIT` behavior verified: Architecture graph query CLI can produce a curated missing-proof audit report for nodes with evidence test docs chain or research-support gaps (`backend/scripts/query_architecture_graph.py`). Command: `python scripts/query_architecture_graph.py --gaps --limit 10`.

## Theory Claims

- none

## Notes

CLI supports exact node lookup search markdown/json output and missing-proof gap detection for systemic agent analysis.
