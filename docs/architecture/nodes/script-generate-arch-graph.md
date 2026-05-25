---
id: "SCRIPT-GENERATE-ARCH-GRAPH"
name: "Generate Architecture Graph Script"
type: "script"
status: "verified"
layer: "ops"
module: "architecture"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/scripts/generate_architecture_graph.py"
related_files: ["docs/architecture/registry/nodes.csv"]
tags: ["aviary", "script", "architecture_graph", "verified"]
---

# Generate Architecture Graph Script

ID: `SCRIPT-GENERATE-ARCH-GRAPH`

## Summary

Generator and validator for registry CSV to Obsidian nodes graph JSON Mermaid and rollups

## Links

- parent: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- children: none
- depends_on: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- used_by: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `depends_on` -> [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]: Generator follows graph-system contract

Incoming:
- [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]] -> `verifies`: Generator pytest validates registry references research claims generated artifacts and node-page parity
- [[script-query-arch-graph|SCRIPT-QUERY-ARCH-GRAPH]] -> `depends_on`: Query CLI reads the generated graph JSON produced by the graph generator

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-GRAPH-GENERATOR` implementation verified: Generator script added to validate registries and generate Obsidian/graph artifacts (`backend/scripts/generate_architecture_graph.py`).

## Theory Claims

- none

## Notes

Script validates references research claims generated artifacts and node-page parity through pytest coverage.
