---
id: "SERVICE-DELIVERY-ROUTER"
name: "Delivery Router"
type: "service"
status: "verified"
layer: "backend"
module: "integrations"
feature: "delivery"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/integrations/delivery_router.py"
related_files: []
tags: ["aviary", "delivery", "integration"]
---

# Delivery Router

ID: `SERVICE-DELIVERY-ROUTER`

## Summary

Routes generated replies to app and Telegram transport boundaries

## Links

- parent: [[feat-app-chat|FEAT-APP-CHAT]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: none
- tests_related: [[test-delivery-router|TEST-DELIVERY-ROUTER]]
- docs_related: [[doc-pipeline-app-chat|DOC-PIPELINE-APP-CHAT]]
- agent_related: none

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `calls`: Runtime uses delivery routing for response transport

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)

## Evidence

- missing

## Theory Claims

- none

## Notes

Chat and Telegram delivery boundaries are covered in tests.
