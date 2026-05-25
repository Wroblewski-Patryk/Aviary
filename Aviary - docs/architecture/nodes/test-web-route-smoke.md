---
id: "TEST-WEB-ROUTE-SMOKE"
name: "Web Route Smoke"
type: "test"
status: "verified"
layer: "test"
module: "web"
feature: "web_shell"
risk_level: "medium"
completion_percent: "95"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/scripts/route-smoke.mjs"
related_files: ["web/src/route-manifest.json"]
tags: ["aviary", "test", "routes"]
---

# Web Route Smoke

ID: `TEST-WEB-ROUTE-SMOKE`

## Summary

Route-state smoke harness for public and authenticated web routes

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
- `verifies` -> [[ui-chat-cognitive-belt|UI-CHAT-COGNITIVE-BELT]]: Route smoke covers authenticated chat route rendering where the belt is present
- `verifies` -> [[feat-web-shell|FEAT-WEB-SHELL]]: Route smoke validates current route markers and basic route state

Incoming: none

## Chains

- `CHAIN-WEB-ROUTE-SMOKE` Web shell route proof chain (verified, high)

## Evidence

- `EVID-TEST-WEB-ROUTE-SMOKE-PROOF` test verified: Web route smoke test node proof refreshed with route_count=14 status=ok and no route marker failures (`web/scripts/route-smoke.mjs`). Command: `npm run smoke:routes`.

## Theory Claims

- none

## Notes

Latest PRJ-1293 run passed npm run smoke:routes route_count=14 status=ok.
