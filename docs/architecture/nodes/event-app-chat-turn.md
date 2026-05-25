---
id: "EVENT-APP-CHAT-TURN"
name: "App Chat Turn"
type: "event"
status: "verified"
layer: "runtime"
module: "chat"
feature: "app_chat"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/core/events.py"
related_files: ["backend/app/api/routes.py", "backend/app/core/runtime.py"]
tags: ["aviary", "event", "chat"]
---

# App Chat Turn

ID: `EVENT-APP-CHAT-TURN`

## Summary

Normalized chat event consumed by runtime pipeline

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: [[agent-perception|AGENT-PERCEPTION]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `consumes`: Runtime consumes normalized chat turns
- [[api-event-ingress|API-EVENT-INGRESS]] -> `emits`: External event ingress normalizes events for runtime

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)
- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-APPCHAT-EVENT-PROOF` behavior verified: App chat turn event proof refreshed through authenticated app chat runtime handoff and runtime API source pipeline tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_app_chat_message_runs_runtime_under_authenticated_user tests/test_runtime_pipeline.py::test_runtime_pipeline_api_source`.

## Theory Claims

- none

## Notes

Event participates in app chat and general event ingress chains.
