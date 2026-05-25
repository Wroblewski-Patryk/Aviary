---
id: "SERVICE-RUNTIME-ORCHESTRATOR"
name: "RuntimeOrchestrator"
type: "service"
status: "verified"
layer: "backend"
module: "runtime"
feature: "foreground_runtime"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/core/runtime.py"
related_files: ["backend/app/core/runtime_graph.py", "backend/app/core/contracts.py", "backend/app/core/graph_adapters.py"]
tags: ["aviary", "runtime", "service", "aion"]
---

# RuntimeOrchestrator

ID: `SERVICE-RUNTIME-ORCHESTRATOR`

## Summary

Coordinates canonical AION runtime stages for event and chat turns

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: [[event-app-chat-turn|EVENT-APP-CHAT-TURN]], [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]], [[service-delivery-router|SERVICE-DELIVERY-ROUTER]]
- depends_on: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-event-ingress|API-EVENT-INGRESS]]
- used_by: [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]], [[service-delivery-router|SERVICE-DELIVERY-ROUTER]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-perception|AGENT-PERCEPTION]], [[agent-context|AGENT-CONTEXT]], [[agent-planning|AGENT-PLANNING]]

## Relations

Outgoing:
- `calls` -> [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]]: Runtime retrieves and writes memory through repository boundary
- `calls` -> [[service-delivery-router|SERVICE-DELIVERY-ROUTER]]: Runtime uses delivery routing for response transport
- `consumes` -> [[event-app-chat-turn|EVENT-APP-CHAT-TURN]]: Runtime consumes normalized chat turns
- `owned_by` -> [[agent-perception|AGENT-PERCEPTION]]: Perception stage participates in runtime pipeline
- `owned_by` -> [[agent-context|AGENT-CONTEXT]]: Context stage participates in runtime pipeline
- `owned_by` -> [[agent-planning|AGENT-PLANNING]]: Planning stage participates in runtime pipeline
- `owned_by` -> [[agent-affective-assessment|AGENT-AFFECTIVE-ASSESSMENT]]: Affective assessment stage participates in runtime pipeline
- `owned_by` -> [[agent-motivation|AGENT-MOTIVATION]]: Motivation stage participates in runtime pipeline
- `owned_by` -> [[agent-role|AGENT-ROLE]]: Role stage participates in runtime pipeline

Incoming:
- [[api-app-chat-message|API-APP-CHAT-MESSAGE]] -> `calls`: Chat route hands text/event into runtime orchestrator
- [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]] -> `verifies`: Runtime pipeline tests verify orchestrator composition
- [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]] -> `parent_of`: Foreground runtime feature owns orchestrator

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)
- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-SERVICE-RUNTIME-ORCHESTRATOR-PROOF` test verified: Runtime orchestrator proof refreshed with API source and stage/action-boundary contract smoke tests (`backend/tests/test_runtime_pipeline.py`). Command: `python -m pytest -q tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source tests/test_runtime_pipeline.py::test_runtime_pipeline_contract_smoke_pins_stage_and_action_boundary_invariants`.

## Theory Claims

- none

## Notes

Canonical stage path is covered by runtime pipeline tests and module confidence ledger.
