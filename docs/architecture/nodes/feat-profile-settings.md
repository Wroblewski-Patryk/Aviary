---
id: "FEAT-PROFILE-SETTINGS"
name: "Profile Settings"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "profile"
feature: "profile_settings"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "docs/pipelines/index.md"
related_files: ["web/src/App.tsx", "web/src/lib/api.ts", "backend/app/api/routes.py", "backend/app/memory/models.py"]
tags: ["aviary", "feature", "profile"]
---

# Profile Settings

ID: `FEAT-PROFILE-SETTINGS`

## Summary

Current user profile settings read and update flow

## Links

- parent: none
- children: [[api-app-me|API-APP-ME]], [[model-aion-profile|MODEL-AION-PROFILE]]
- depends_on: [[api-app-me|API-APP-ME]], [[comp-web-app|COMP-WEB-APP]]
- used_by: [[comp-web-app|COMP-WEB-APP]]
- ui_related: [[page-settings|PAGE-SETTINGS]]
- api_related: [[api-app-me|API-APP-ME]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-preferences|TEST-PREFERENCES]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]], [[doc-data-reference|DOC-DATA-REFERENCE]]
- agent_related: none

## Relations

Outgoing: none

Incoming: none

## Chains

- `CHAIN-APP-AUTH` App auth session execution chain (verified, high)
- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)

## Evidence

- `EVID-PROFILE-SETTINGS-CHAIN-REFRESH` behavior verified: Profile settings chain refreshed with focused backend API and preference tests web build and route smoke including the Settings route marker (`.codex/tasks/PRJ-1279-profile-settings-chain-refresh.md`).

## Theory Claims

- none

## Notes

Profile settings are linked to web Settings and runtime preferences.
