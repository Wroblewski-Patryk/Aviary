---
id: "WORKFLOW-ARCH-GRAPH-CI"
name: "Architecture Graph CI Policy"
type: "workflow"
status: "verified"
layer: "ops"
module: "architecture"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: ".github/workflows/architecture-graph.yml"
related_files: ["backend/tests/test_architecture_graph_generator.py", "backend/scripts/generate_architecture_inventory.py", "backend/scripts/generate_architecture_graph.py"]
tags: ["aviary", "workflow", "architecture_graph", "ci", "verified"]
---

# Architecture Graph CI Policy

ID: `WORKFLOW-ARCH-GRAPH-CI`

## Summary

GitHub Actions policy that runs committed-artifact freshness and fast graph pytest gates automatically with a manual heavy graph gate

## Links

- parent: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- children: none
- depends_on: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]], [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- used_by: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `depends_on` -> [[test-arch-graph-generator|TEST-ARCH-GRAPH-GENERATOR]]: CI policy runs the same graph generator pytest gates used locally
- `documents` -> [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]: Graph-system docs describe the CI fast and heavy gate policy

Incoming:
- [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]] -> `parent_of`: Architecture graph workflow owns the CI validation policy
- [[doc-pr-template|DOC-PR-TEMPLATE]] -> `depends_on`: PR checklist complements the automatic graph CI gate by making graph evidence visible in review

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-ARCH-GRAPH-CI-POLICY` test verified: Architecture graph CI policy runs inventory and graph regeneration stale-artifact diff checks and fast graph pytest automatically for graph-relevant changes with a manual heavy all-node parity gate (`.github/workflows/architecture-graph.yml`). Command: `GitHub Actions fast graph gate plus manual heavy graph gate`.

## Theory Claims

- none

## Notes

Fast gate is automatic for graph-relevant PR and main changes; heavy all-node parity gate is manual workflow_dispatch because it is intentionally slower.
