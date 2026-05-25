---
id: "PAGE-DASHBOARD"
name: "Dashboard Route"
type: "page"
status: "verified"
layer: "frontend"
module: "web"
feature: "dashboard"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "web/src/App.tsx"
related_files: ["web/src/components/dashboard.tsx", "web/src/index.css"]
tags: ["aviary", "page", "dashboard", "ui"]
---

# Dashboard Route

ID: `PAGE-DASHBOARD`

## Summary

Authenticated Dashboard flagship route

## Links

- parent: [[comp-web-app|COMP-WEB-APP]]
- children: none
- depends_on: [[comp-web-app|COMP-WEB-APP]], [[api-app-me|API-APP-ME]]
- used_by: [[feat-web-shell|FEAT-WEB-SHELL]]
- ui_related: [[page-dashboard|PAGE-DASHBOARD]]
- api_related: [[api-app-me|API-APP-ME]]
- database_related: none
- tests_related: [[test-web-route-smoke|TEST-WEB-ROUTE-SMOKE]]
- docs_related: [[doc-frontend-route-map|DOC-FRONTEND-ROUTE-MAP]]
- agent_related: none

## Relations

Outgoing: none

Incoming:
- [[comp-web-app|COMP-WEB-APP]] -> `renders`: App shell renders Dashboard route

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

PRJ-1263 provides latest route-focused proof.
