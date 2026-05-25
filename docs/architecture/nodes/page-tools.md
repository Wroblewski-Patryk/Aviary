---
id: "PAGE-TOOLS"
name: "Tools Route"
type: "page"
status: "verified"
layer: "frontend"
module: "web"
feature: "tools"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/App.tsx"
related_files: ["web/src/components/tools.tsx", "web/src/lib/api.ts"]
tags: ["aviary", "page", "tools"]
---

# Tools Route

ID: `PAGE-TOOLS`

## Summary

Authenticated Tools route capability directory and preferences UI

## Links

- parent: [[feat-tools|FEAT-TOOLS]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- used_by: [[feat-tools|FEAT-TOOLS]]
- ui_related: [[page-tools|PAGE-TOOLS]]
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]], [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing:
- `calls` -> [[api-tools-overview|API-TOOLS-OVERVIEW]]: Tools route consumes tools overview and preferences endpoints

Incoming:
- [[feat-telegram|FEAT-TELEGRAM]] -> `depends_on`: Telegram flow depends on tools route controls and status posture
- [[comp-web-app|COMP-WEB-APP]] -> `renders`: App shell renders Tools route

## Chains

- `CHAIN-TELEGRAM-LINK-DELIVERY` Telegram link and delivery chain (verified, high)
- `CHAIN-TOOLS-OVERVIEW` Tools overview execution chain (verified, high)

## Evidence

- `EVID-PAGE-TOOLS-PROOF` behavior verified: Tools route proof refreshed with route smoke marker aion-tools-canvas in a 14-route successful run (`web/scripts/route-smoke.mjs`). Command: `npm run smoke:routes`.

## Theory Claims

- none

## Notes

Route is included in route smoke and recent UI simplification passes.
