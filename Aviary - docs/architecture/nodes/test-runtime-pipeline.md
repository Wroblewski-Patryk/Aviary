---
id: "TEST-RUNTIME-PIPELINE"
name: "Runtime Pipeline Tests"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "foreground_runtime"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/tests/test_runtime_pipeline.py"
related_files: []
tags: ["aviary", "test", "runtime"]
---

# Runtime Pipeline Tests

ID: `TEST-RUNTIME-PIPELINE`

## Summary

End-to-end runtime composition tests with fakes

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]: Runtime pipeline tests verify orchestrator composition

Incoming: none

## Chains

- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-TEST-RUNTIME-PIPELINE-PROOF` test verified: Runtime pipeline test node proof refreshed with API source and stage/action-boundary contract checks (`backend/tests/test_runtime_pipeline.py`). Command: `python -m pytest -q tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source tests/test_runtime_pipeline.py::test_runtime_pipeline_contract_smoke_pins_stage_and_action_boundary_invariants`.

## Theory Claims

- none

## Notes

Runtime pipeline is high-confidence in module ledger.
