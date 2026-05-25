---
id: "DOC-PIPELINE-APP-CHAT"
name: "App Chat Pipeline Doc"
type: "documentation"
status: "verified"
layer: "docs"
module: "chat"
feature: "app_chat"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "docs/pipelines/app-chat.md"
related_files: []
tags: ["aviary", "docs", "pipeline", "chat"]
---

# App Chat Pipeline Doc

ID: `DOC-PIPELINE-APP-CHAT`

## Summary

Dedicated app chat pipeline map

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[feat-app-chat|FEAT-APP-CHAT]]
- used_by: [[ui-chat-composer|UI-CHAT-COMPOSER]], [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]], [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: none

## Relations

Outgoing:
- `documents` -> [[feat-app-chat|FEAT-APP-CHAT]]: App chat pipeline doc documents the chain

Incoming: none

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)

## Evidence

- `EVID-DOC-PIPELINE-APP-CHAT-PROOF` documentation verified: App chat pipeline documentation proof refreshed as the dedicated chain map for UI composer app chat API runtime memory delivery tests and docs (`docs/pipelines/app-chat.md`).

## Theory Claims

- none

## Notes

Direct documentation evidence refreshed in PRJ-1293; existing pipeline doc is linked into graph seed.
