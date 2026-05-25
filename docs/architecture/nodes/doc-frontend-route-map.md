---
id: "DOC-FRONTEND-ROUTE-MAP"
name: "Frontend Route And Component Map"
type: "documentation"
status: "verified"
layer: "docs"
module: "frontend"
feature: "web_shell"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-11"
verification_status: "verified"
file_path: "docs/frontend/route-component-map.md"
related_files: []
tags: ["aviary", "docs", "frontend"]
---

# Frontend Route And Component Map

ID: `DOC-FRONTEND-ROUTE-MAP`

## Summary

Web shell route state API helper and gap map

## Links

- parent: [[comp-web-app|COMP-WEB-APP]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]]
- used_by: [[feat-web-shell|FEAT-WEB-SHELL]]
- ui_related: [[comp-web-app|COMP-WEB-APP]]
- api_related: none
- database_related: none
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing:
- `documents` -> [[comp-web-app|COMP-WEB-APP]]: Frontend route map documents web shell

Incoming: none

## Chains

- `CHAIN-CHAT-COGNITIVE-BELT` Chat cognitive belt context-strip chain (verified, medium)
- `CHAIN-WEB-ROUTE-SMOKE` Web shell route proof chain (verified, high)

## Evidence

- `EVID-DOC-FRONTEND-ROUTE-MAP-PROOF` documentation verified: Frontend route map proof refreshed as canonical shell route/component reference linked into verified chains and smoke contracts (`docs/frontend/route-component-map.md`).

## Theory Claims

- none

## Notes

Frontend map is still coarse but graph-linked.
