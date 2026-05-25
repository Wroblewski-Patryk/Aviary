---
id: "FEAT-TOOLS"
name: "Tools Overview And Preferences"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "tools"
feature: "tools"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "docs/pipelines/tools.md"
related_files: ["web/src/App.tsx", "web/src/lib/api.ts", "backend/app/api/routes.py", "backend/app/core/capability_catalog.py"]
tags: ["aviary", "feature", "tools"]
---

# Tools Overview And Preferences

ID: `FEAT-TOOLS`

## Summary

Tool readiness preferences and Telegram link controls

## Links

- parent: none
- children: [[api-tools-overview|API-TOOLS-OVERVIEW]], [[page-tools|PAGE-TOOLS]]
- depends_on: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- used_by: [[comp-web-app|COMP-WEB-APP]]
- ui_related: [[page-tools|PAGE-TOOLS]]
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-connector-policy|TEST-CONNECTOR-POLICY]]
- docs_related: [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing: none

Incoming: none

## Chains

- `CHAIN-TOOLS-OVERVIEW` Tools overview execution chain (verified, high)

## Evidence

- `EVID-TOOLS-OVERVIEW-CHAIN-REFRESH` behavior verified: Tools overview chain refreshed with focused backend tools API connector policy tests web build route smoke and Tools directory characterization covering full toggle telegram link loading empty and error states (`.codex/tasks/PRJ-1280-tools-overview-chain-refresh.md`).

## Theory Claims

- none

## Notes

Provider activation remains deferred but tools overview is verified locally.
