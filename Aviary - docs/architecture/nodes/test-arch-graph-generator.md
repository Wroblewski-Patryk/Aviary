---
id: "TEST-ARCH-GRAPH-GENERATOR"
name: "Architecture Graph Generator Check"
type: "test"
status: "verified"
layer: "test"
module: "architecture"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/tests/test_architecture_graph_generator.py"
related_files: ["docs/architecture/registry/nodes.csv"]
tags: ["aviary", "test", "architecture_graph", "verified"]
---

# Architecture Graph Generator Check

ID: `TEST-ARCH-GRAPH-GENERATOR`

## Summary

Generator execution and registry validation proof

## Links

- parent: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- children: none
- depends_on: [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]]
- used_by: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[script-generate-arch-graph|SCRIPT-GENERATE-ARCH-GRAPH]]: Generator pytest validates registry references research claims generated artifacts and node-page parity
- `verifies` -> [[workflow-research-evidence|WORKFLOW-RESEARCH-EVIDENCE]]: Graph generator validates research source and theory claim registry integrity

Incoming:
- [[workflow-arch-graph-ci|WORKFLOW-ARCH-GRAPH-CI]] -> `depends_on`: CI policy runs the same graph generator pytest gates used locally

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-GRAPH-GENERATOR-PYTEST` test verified: Pytest coverage verifies research claim 3-source validation graph export research payloads current repository registry validation temp research rollup generation generated JSON freshness latest rollup evidence key generated artifact parity all generated node-page parity and fast versus heavy validation modes (`backend/tests/test_architecture_graph_generator.py`). Command: `python -m pytest -q tests/test_architecture_graph_generator.py`.

## Theory Claims

- none

## Notes

Fast and heavy pytest gates cover research validation generated artifact parity and all-node page parity.
