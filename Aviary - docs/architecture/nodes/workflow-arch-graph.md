---
id: "WORKFLOW-ARCH-GRAPH"
name: "Architecture Graph Evidence Workflow"
type: "workflow"
status: "verified"
layer: "docs"
module: "architecture"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "docs/architecture/graph-system.md"
related_files: ["docs/architecture/registry/nodes.csv", "docs/architecture/registry/relations.csv", "backend/scripts/generate_architecture_graph.py"]
tags: ["aviary", "workflow", "architecture_graph", "verified"]
---

# Architecture Graph Evidence Workflow

ID: `WORKFLOW-ARCH-GRAPH`

## Summary

CSV-first Obsidian-compatible architecture graph and evidence workflow

## Links

- parent: none
- children: [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]], [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- depends_on: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]], [[feat-web-shell|FEAT-WEB-SHELL]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `generated_from` -> `docs/architecture/registry/nodes.csv`: Graph workflow is generated from registry CSV
- `parent_of` -> [[workflow-arch-graph-ci|WORKFLOW-ARCH-GRAPH-CI]]: Architecture graph workflow owns the CI validation policy
- `parent_of` -> [[script-query-arch-graph|SCRIPT-QUERY-ARCH-GRAPH]]: Architecture graph workflow owns the local query utility for systemic analysis
- `parent_of` -> [[workflow-research-evidence|WORKFLOW-RESEARCH-EVIDENCE]]: Architecture graph workflow owns the research evidence mapping extension

Incoming:
- [[doc-pr-template|DOC-PR-TEMPLATE]] -> `documents`: PR template asks authors to disclose graph registry chain evidence research and graph gate updates

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-ARCH-GRAPH-WORKFLOW-CLOSURE` behavior verified: Architecture graph workflow mechanics are verified with generator validation generated artifact parity all-node parity fast and heavy gates and research evidence mapping (`.codex/tasks/PRJ-1278-architecture-graph-workflow-closure.md`).

## Theory Claims

- none

## Notes

Workflow has generator tests fast/heavy validation generated artifacts research mapping and source-of-truth state updates; full project semantic curation remains iterative expansion.
