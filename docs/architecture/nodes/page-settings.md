---
id: "PAGE-SETTINGS"
name: "Settings Route"
type: "page"
status: "verified"
layer: "frontend"
module: "web"
feature: "profile_settings"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/App.tsx"
related_files: ["web/src/components/settings.tsx", "web/src/lib/api.ts"]
tags: ["aviary", "page", "settings"]
---

# Settings Route

ID: `PAGE-SETTINGS`

## Summary

Authenticated Settings route for user and runtime preferences

## Links

- parent: [[comp-web-app|COMP-WEB-APP]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]], [[api-app-me|API-APP-ME]]
- used_by: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- ui_related: [[page-settings|PAGE-SETTINGS]]
- api_related: [[api-app-me|API-APP-ME]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]], [[test-preferences|TEST-PREFERENCES]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing: none

Incoming:
- [[comp-web-app|COMP-WEB-APP]] -> `renders`: App shell renders Settings route

## Chains

- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)

## Evidence

- `EVID-PAGE-SETTINGS-PROOF` behavior verified: Settings route proof refreshed with route smoke marker aion-settings-canvas in a 14-route successful run (`web/scripts/route-smoke.mjs`). Command: `npm run smoke:routes`.

## Theory Claims

- none

## Notes

Included in route smoke and simplification passes.
