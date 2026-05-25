---
id: "TEST-CHAT-TRANSCRIPT"
name: "Chat Transcript Characterization"
type: "test"
status: "verified"
layer: "test"
module: "web"
feature: "app_chat"
risk_level: "medium"
completion_percent: "100"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/scripts/chat-transcript-characterization.mjs"
related_files: []
tags: ["aviary", "test", "chat"]
---

# Chat Transcript Characterization

ID: `TEST-CHAT-TRANSCRIPT`

## Summary

Web characterization proof for chat transcript source markers and transcript behavior

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[ui-chat-composer|UI-CHAT-COMPOSER]], [[comp-web-app|COMP-WEB-APP]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]]
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: none
- database_related: none
- tests_related: [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]]
- docs_related: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[ui-chat-composer|UI-CHAT-COMPOSER]]: Chat transcript characterization verifies transcript/source behavior

Incoming: none

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)
- `CHAIN-CHAT-COGNITIVE-BELT` Chat cognitive belt context-strip chain (verified, medium)

## Evidence

- `EVID-TEST-CHAT-TRANSCRIPT-PROOF` test verified: Chat transcript characterization proof refreshed with preview full and send-state checks including app and Telegram source markers (`web/scripts/chat-transcript-characterization.mjs`). Command: `npm run test:chat-transcript`.

## Theory Claims

- none

## Notes

Latest PRJ-1265 run passed npm run test:chat-transcript.
