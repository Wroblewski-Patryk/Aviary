---
id: "PAGE-PERSONALITY"
name: "Personality Route"
type: "page"
status: "verified"
layer: "frontend"
module: "web"
feature: "personality"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/App.tsx"
related_files: ["web/src/components/personality.tsx", "backend/app/api/routes.py"]
tags: ["aviary", "page", "personality"]
---

# Personality Route

ID: `PAGE-PERSONALITY`

## Summary

Authenticated Personality and learned-state route

## Links

- parent: [[comp-web-app|COMP-WEB-APP]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]], [[api-personality-overview|API-PERSONALITY-OVERVIEW]]
- used_by: [[feat-learned-state|FEAT-LEARNED-STATE]]
- ui_related: [[page-personality|PAGE-PERSONALITY]]
- api_related: [[api-personality-overview|API-PERSONALITY-OVERVIEW]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]], [[test-api-routes|TEST-API-ROUTES]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing:
- `calls` -> [[api-personality-overview|API-PERSONALITY-OVERVIEW]]: Personality route consumes learned-state overview API

Incoming:
- [[comp-web-app|COMP-WEB-APP]] -> `renders`: App shell renders Personality route

## Chains

- `CHAIN-PERSONALITY-OVERVIEW` Personality learned-state overview chain (verified, high)

## Evidence

- `EVID-PAGE-PERSONALITY-PROOF` behavior verified: Personality route proof refreshed with route smoke marker aion-personality-canvas in a 14-route successful run (`web/scripts/route-smoke.mjs`). Command: `npm run smoke:routes`.

## Theory Claims

- none

## Notes

PRJ-1262 and PRJ-1261 provide recent UI proof.
