---
id: "FEAT-TELEGRAM"
name: "Telegram Linking And Delivery"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "integrations"
feature: "telegram"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "docs/pipelines/index.md"
related_files: ["backend/app/integrations/telegram/client.py", "backend/app/integrations/delivery_router.py", "backend/app/api/routes.py"]
tags: ["aviary", "feature", "telegram", "verified"]
---

# Telegram Linking And Delivery

ID: `FEAT-TELEGRAM`

## Summary

Telegram link and transport delivery path through app tools and event ingress

## Links

- parent: none
- children: [[service-delivery-router|SERVICE-DELIVERY-ROUTER]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- depends_on: [[service-delivery-router|SERVICE-DELIVERY-ROUTER]], [[feat-app-chat|FEAT-APP-CHAT]]
- used_by: [[feat-tools|FEAT-TOOLS]]
- ui_related: [[page-tools|PAGE-TOOLS]]
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-delivery-router|TEST-DELIVERY-ROUTER]]
- docs_related: [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing:
- `depends_on` -> [[page-tools|PAGE-TOOLS]]: Telegram flow depends on tools route controls and status posture
- `depends_on` -> [[api-tools-overview|API-TOOLS-OVERVIEW]]: Telegram flow depends on tools API readiness and link-state contracts
- `depends_on` -> [[service-delivery-router|SERVICE-DELIVERY-ROUTER]]: Telegram flow depends on delivery routing transport boundaries

Incoming:
- [[test-delivery-router|TEST-DELIVERY-ROUTER]] -> `verifies`: Delivery router tests verify Telegram channel success failure missing chat id and segmentation behavior
- [[test-api-routes|TEST-API-ROUTES]] -> `verifies`: Focused API route tests verify Telegram link start confirm and linked identity behavior
- [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]] -> `documents`: Tools pipeline documents Telegram link and readiness path

## Chains

- `CHAIN-TELEGRAM-LINK-DELIVERY` Telegram link and delivery chain (verified, high)

## Evidence

- `EVID-FEAT-TELEGRAM-PROOF` behavior verified: Telegram feature proof refreshed with focused link start confirm linked identity expired-code handling and delivery transport contract tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_app_start_telegram_link_creates_pending_link_code tests/test_api_routes.py::test_event_endpoint_confirms_telegram_link_code_and_updates_tools_overview tests/test_api_routes.py::test_event_endpoint_uses_linked_auth_user_id_for_telegram_events_after_linking tests/test_api_routes.py::test_event_endpoint_rejects_expired_telegram_link_code tests/test_delivery_router.py::test_delivery_router_handles_telegram_channel tests/test_delivery_router.py::test_delivery_router_segments_long_telegram_messages tests/test_delivery_router.py::test_delivery_router_requires_chat_id_for_telegram`.

## Theory Claims

- none

## Notes

Local Telegram link start confirm and delivery transport behavior are verified through focused API and delivery router tests; live operator credentials remain deployment-specific.
