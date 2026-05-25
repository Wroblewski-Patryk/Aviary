---
id: "FEAT-APP-CHAT"
name: "App Chat"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "chat"
feature: "app_chat"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "docs/pipelines/app-chat.md"
related_files: ["web/src/App.tsx", "web/src/lib/api.ts", "backend/app/api/routes.py", "backend/app/core/runtime.py"]
tags: ["aviary", "feature", "chat", "verified"]
---

# App Chat

ID: `FEAT-APP-CHAT`

## Summary

Authenticated chat from browser UI through runtime response and transcript evidence

## Links

- parent: none
- children: [[ui-chat-composer|UI-CHAT-COMPOSER]], [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[model-aion-memory|MODEL-AION-MEMORY]], [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]]
- depends_on: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- used_by: none
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]]
- docs_related: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[ui-chat-composer|UI-CHAT-COMPOSER]]: App chat owns the chat composer surface
- `parent_of` -> [[ui-chat-cognitive-belt|UI-CHAT-COGNITIVE-BELT]]: App chat owns the cognitive belt context strip

Incoming:
- [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]] -> `documents`: App chat pipeline doc documents the chain

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)
- `CHAIN-CHAT-COGNITIVE-BELT` Chat cognitive belt context-strip chain (verified, medium)

## Evidence

- `EVID-APPCHAT-IMPLEMENTATION` implementation verified: Functional chat attachment pass implemented under existing backend text contract (`.codex/tasks/PRJ-1265-chat-attachments-functional-pass.md`).
- `EVID-APPCHAT-TEST` test verified: Chat transcript characterization passed (`web/scripts/chat-transcript-characterization.mjs`). Command: `npm run test:chat-transcript`.

## Theory Claims

- none

## Notes

Seeded from traceability matrix and PRJ-1265 evidence.
