---
id: "FEAT-TELEGRAM"
name: "Telegram Linking And Delivery"
type: "feature"
status: "implemented"
layer: "cross_layer"
module: "integrations"
feature: "telegram"
risk_level: "medium"
completion_percent: "75"
last_verified_at: "2026-05-14"
verification_status: "connection_evidence"
file_path: "docs/pipelines/index.md"
related_files: ["backend/app/integrations/telegram/client.py", "backend/app/integrations/delivery_router.py"]
tags: ["aviary", "feature", "telegram", "partial"]
---

# Telegram Linking And Delivery

ID: `FEAT-TELEGRAM`

## Summary

Telegram link and transport delivery path through app tools and event ingress

## Links

- parent: none
- children: [[service-delivery-router|SERVICE-DELIVERY-ROUTER]]
- depends_on: [[feat-app-chat|FEAT-APP-CHAT]]
- used_by: [[feat-tools|FEAT-TOOLS]]
- ui_related: [[page-tools|PAGE-TOOLS]]
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-delivery-router|TEST-DELIVERY-ROUTER]]
- docs_related: [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing: none

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Local delivery/linking is mapped; live Telegram operator credentials remain scope-dependent.
