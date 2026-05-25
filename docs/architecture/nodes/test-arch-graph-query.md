---
id: "TEST-ARCH-GRAPH-QUERY"
name: "Architecture Graph Query Tests"
type: "test"
status: "verified"
layer: "test"
module: "architecture"
feature: "architecture_graph"
risk_level: "medium"
completion_percent: "100"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/tests/test_architecture_graph_query.py"
related_files: ["backend/scripts/query_architecture_graph.py"]
tags: ["aviary", "test", "architecture_graph", "query", "verified"]
---

# Architecture Graph Query Tests

ID: `TEST-ARCH-GRAPH-QUERY`

## Summary

Focused pytest coverage for the architecture graph query CLI

## Links

- parent: [[workflow-arch-graph|WORKFLOW-ARCH-GRAPH]]
- children: none
- depends_on: [[script-query-arch-graph|SCRIPT-QUERY-ARCH-GRAPH]]
- used_by: [[script-query-arch-graph|SCRIPT-QUERY-ARCH-GRAPH]]
- ui_related: none
- api_related: none
- database_related: none
- tests_related: [[test-arch-graph-query|TEST-ARCH-GRAPH-QUERY]]
- docs_related: [[doc-arch-graph-system|DOC-ARCH-GRAPH-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[script-query-arch-graph|SCRIPT-QUERY-ARCH-GRAPH]]: Focused query tests verify node lookup search impact chains evidence theory claims gap detection JSON output and suggestions

Incoming:
- [[file-backend-tests-conftest-py-516a9fbf|FILE-BACKEND-TESTS-CONFTEST-PY-516A9FBF]] -> `used_by`: Backend pytest fixture setup in `conftest.py` is used by architecture graph query tests

## Chains

- `CHAIN-ARCH-GRAPH-WORKFLOW` Architecture graph evidence generation chain (verified, high)

## Evidence

- `EVID-TEST-ARCH-GRAPH-QUERY-PROOF` test verified: Architecture graph query tests proof refreshed with node lookup impact chain evidence claim and gap-audit contract coverage (`backend/tests/test_architecture_graph_query.py`). Command: `python -m pytest -q tests/test_architecture_graph_query.py -m not slow`.

## Theory Claims

- none

## Notes

Tests cover node impact chains evidence theory claims gap detection CLI JSON and missing-node suggestions.
