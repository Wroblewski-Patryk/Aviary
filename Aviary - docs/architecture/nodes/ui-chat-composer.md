---
id: "UI-CHAT-COMPOSER"
name: "Chat Composer"
type: "ui_element"
status: "verified"
layer: "frontend"
module: "web"
feature: "app_chat"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/App.tsx"
related_files: ["web/src/components/chat.tsx", "web/src/lib/chat-transcript.ts"]
tags: ["aviary", "ui", "chat", "composer"]
---

# Chat Composer

ID: `UI-CHAT-COMPOSER`

## Summary

Composer surface for text and current attachment context serialization

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]], [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- used_by: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- ui_related: [[comp-web-app|COMP-WEB-APP]]
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: none
- tests_related: [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]]
- docs_related: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: none

## Relations

Outgoing:
- `calls` -> [[api-app-chat-message|API-APP-CHAT-MESSAGE]]: Composer submits messages through the existing app chat message API

Incoming:
- [[feat-app-chat|FEAT-APP-CHAT]] -> `parent_of`: App chat owns the chat composer surface
- [[test-chat-transcript|TEST-CHAT-TRANSCRIPT]] -> `verifies`: Chat transcript characterization verifies transcript/source behavior

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)

## Evidence

- missing

## Theory Claims

- none

## Notes

PRJ-1265 added bounded file picker and attachment chips without backend contract change.
