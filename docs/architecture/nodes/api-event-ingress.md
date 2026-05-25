---
id: "API-EVENT-INGRESS"
name: "POST /event"
type: "api_route"
status: "verified"
layer: "api"
module: "backend"
feature: "event_ingress"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/api/routes.py"
related_files: ["backend/app/core/events.py"]
tags: ["aviary", "api", "event"]
---

# POST /event

ID: `API-EVENT-INGRESS`

## Summary

General event ingress API route

## Links

- parent: [[feat-event-ingress|FEAT-EVENT-INGRESS]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]], [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: none

## Relations

Outgoing:
- `emits` -> [[event-app-chat-turn|EVENT-APP-CHAT-TURN]]: External event ingress normalizes events for runtime

Incoming:
- [[test-api-routes|TEST-API-ROUTES]] -> `verifies`: Focused backend API tests verify public event response API boundary normalization debug gate contract and runtime handoff

## Chains

- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-EVENT-INGRESS-API-PROOF` behavior verified: Event ingress API proof refreshed with public response normalization API boundary debug gate contract and runtime pipeline API source tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_event_endpoint_returns_public_response_and_normalizes_event tests/test_api_routes.py::test_event_endpoint_enforces_api_boundary_for_source_and_payload_shape tests/test_api_routes.py::test_event_endpoint_contract_smoke_pins_public_shape_and_debug_gate tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source`.

## Theory Claims

- none

## Notes

General external event entrypoint.
