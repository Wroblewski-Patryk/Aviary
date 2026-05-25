---
id: "API-APP-CHAT-MESSAGE"
name: "POST /app/chat/message"
type: "api_route"
status: "verified"
layer: "api"
module: "backend"
feature: "app_chat"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/app/api/routes.py"
related_files: ["backend/app/api/schemas.py", "web/src/lib/api.ts"]
tags: ["aviary", "api", "chat"]
---

# POST /app/chat/message

ID: `API-APP-CHAT-MESSAGE`

## Summary

Authenticated app chat ingress route that hands browser chat text into runtime

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[api-app-auth|API-APP-AUTH]], [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]], [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: none

## Relations

Outgoing:
- `calls` -> [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]: Chat route hands text/event into runtime orchestrator

Incoming:
- [[ui-chat-composer|UI-CHAT-COMPOSER]] -> `calls`: Composer submits messages through the existing app chat message API
- [[test-api-routes|TEST-API-ROUTES]] -> `verifies`: Backend API tests cover app chat route contracts
- [[doc-api-reference|DOC-API-REFERENCE]] -> `documents`: API reference documents chat route

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)

## Evidence

- `EVID-APPCHAT-API-PROOF` behavior verified: App chat message API proof refreshed with authenticated user runtime handoff localized timestamp and pending connector confirmation contract tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_app_chat_message_runs_runtime_under_authenticated_user tests/test_api_routes.py::test_app_chat_message_localizes_runtime_timestamp_from_profile_utc_offset tests/test_api_routes.py::test_app_chat_message_exposes_bounded_pending_connector_confirmation`.

## Theory Claims

- none

## Notes

Current attachment implementation serializes attachment context into existing text payload.
