---
id: "TEST-API-ROUTES"
name: "Backend API Routes Tests"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "api_contracts"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/tests/test_api_routes.py"
related_files: []
tags: ["aviary", "test", "api"]
---

# Backend API Routes Tests

ID: `TEST-API-ROUTES`

## Summary

Main backend route contract suite

## Links

- parent: [[doc-api-reference|DOC-API-REFERENCE]]
- children: none
- depends_on: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-app-me|API-APP-ME]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]], [[feat-profile-settings|FEAT-PROFILE-SETTINGS]], [[feat-tools|FEAT-TOOLS]]
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-app-me|API-APP-ME]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[api-app-chat-message|API-APP-CHAT-MESSAGE]]: Backend API tests cover app chat route contracts
- `verifies` -> [[api-event-ingress|API-EVENT-INGRESS]]: Focused backend API tests verify public event response API boundary normalization debug gate contract and runtime handoff
- `verifies` -> [[api-app-auth|API-APP-AUTH]]: Focused backend API tests verify register session requirement login logout and me roundtrip contracts
- `verifies` -> [[feat-telegram|FEAT-TELEGRAM]]: Focused API route tests verify Telegram link start confirm and linked identity behavior

Incoming: none

## Chains

- `CHAIN-APP-AUTH` App auth session execution chain (verified, high)
- `CHAIN-PERSONALITY-OVERVIEW` Personality learned-state overview chain (verified, high)
- `CHAIN-TELEGRAM-LINK-DELIVERY` Telegram link and delivery chain (verified, high)

## Evidence

- `EVID-TEST-API-ROUTES-PROOF` test verified: Backend API routes test node proof refreshed with public/debug event endpoint contract smoke test (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_event_endpoint_contract_smoke_pins_public_shape_and_debug_gate`.

## Theory Claims

- none

## Notes

Full backend baseline has current historical evidence; rerun for backend changes.
