---
id: "COMP-WEB-APP"
name: "Web App Shell"
type: "component"
status: "verified"
layer: "frontend"
module: "web"
feature: "web_shell"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/App.tsx"
related_files: ["web/src/routes.ts", "web/src/route-manifest.json", "web/src/index.css"]
tags: ["aviary", "frontend", "shell"]
---

# Web App Shell

ID: `COMP-WEB-APP`

## Summary

React/Vite public and authenticated shell with route rendering and API client usage

## Links

- parent: none
- children: [[ui-chat-composer|UI-CHAT-COMPOSER]], [[page-dashboard|PAGE-DASHBOARD]], [[page-personality|PAGE-PERSONALITY]], [[page-tools|PAGE-TOOLS]], [[page-settings|PAGE-SETTINGS]]
- depends_on: [[api-app-me|API-APP-ME]], [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- used_by: [[ui-chat-composer|UI-CHAT-COMPOSER]], [[page-dashboard|PAGE-DASHBOARD]], [[page-personality|PAGE-PERSONALITY]], [[page-tools|PAGE-TOOLS]], [[page-settings|PAGE-SETTINGS]]
- ui_related: [[ui-chat-composer|UI-CHAT-COMPOSER]]
- api_related: [[api-app-me|API-APP-ME]]
- database_related: none
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing:
- `renders` -> [[ui-chat-cognitive-belt|UI-CHAT-COGNITIVE-BELT]]: Web shell renders the chat cognitive belt through the chat component
- `calls` -> [[api-app-me|API-APP-ME]]: Web shell reads and updates current user settings
- `calls` -> [[api-app-auth|API-APP-AUTH]]: Web shell uses auth API for register login logout and current session boundary
- `renders` -> [[page-dashboard|PAGE-DASHBOARD]]: App shell renders Dashboard route
- `renders` -> [[page-personality|PAGE-PERSONALITY]]: App shell renders Personality route
- `renders` -> [[page-tools|PAGE-TOOLS]]: App shell renders Tools route
- `renders` -> [[page-settings|PAGE-SETTINGS]]: App shell renders Settings route

Incoming:
- [[feat-web-shell|FEAT-WEB-SHELL]] -> `parent_of`: Web shell feature owns React app shell
- [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]] -> `documents`: Frontend route map documents web shell

## Chains

- `CHAIN-APP-AUTH` App auth session execution chain (verified, high)
- `CHAIN-CHAT-COGNITIVE-BELT` Chat cognitive belt context-strip chain (verified, medium)
- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)
- `CHAIN-WEB-ROUTE-SMOKE` Web shell route proof chain (verified, high)

## Evidence

- `EVID-COMP-WEB-APP-PROOF` behavior verified: Web app shell proof refreshed with successful production build and 14-route smoke pass covering public and authenticated route markers (`web/scripts/route-smoke.mjs`). Command: `npm run build and npm run smoke:routes`.

## Theory Claims

- none

## Notes

Route smoke and web build are recurring validation gates.
