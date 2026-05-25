---
id: "FEAT-WEB-SHELL"
name: "Web Shell Routes"
type: "feature"
status: "verified"
layer: "frontend"
module: "web"
feature: "web_shell"
risk_level: "medium"
completion_percent: "95"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "docs/frontend/route-component-map.md"
related_files: ["web/src/App.tsx", "web/src/routes.ts", "web/src/route-manifest.json", "web/scripts/route-smoke.mjs"]
tags: ["aviary", "feature", "web"]
---

# Web Shell Routes

ID: `FEAT-WEB-SHELL`

## Summary

Public and authenticated route shell rendering and navigation

## Links

- parent: none
- children: [[comp-web-app|COMP-WEB-APP]], [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]]
- depends_on: [[comp-web-app|COMP-WEB-APP]]
- used_by: [[comp-web-app|COMP-WEB-APP]]
- ui_related: [[comp-web-app|COMP-WEB-APP]]
- api_related: none
- database_related: none
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[comp-web-app|COMP-WEB-APP]]: Web shell feature owns React app shell

Incoming:
- [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]] -> `verifies`: Route smoke validates current route markers and basic route state

## Chains

- `CHAIN-WEB-ROUTE-SMOKE` Web shell route proof chain (verified, high)

## Evidence

- `EVID-WEB-ROUTES` behavior verified: Route smoke passed route_count=14 status=ok (`web/scripts/route-smoke.mjs`). Command: `npm run smoke:routes`.

## Theory Claims

- none

## Notes

Route count 14 proof from smoke harness.
