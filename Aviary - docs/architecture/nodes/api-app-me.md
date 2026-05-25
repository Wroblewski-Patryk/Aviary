---
id: "API-APP-ME"
name: "GET/PATCH /app/me"
type: "api_route"
status: "verified"
layer: "api"
module: "backend"
feature: "profile_settings"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/api/routes.py"
related_files: ["web/src/lib/api.ts"]
tags: ["aviary", "api", "profile"]
---

# GET/PATCH /app/me

ID: `API-APP-ME`

## Summary

Current app user and settings endpoints

## Links

- parent: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- children: none
- depends_on: [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[comp-web-app|COMP-WEB-APP]]
- ui_related: none
- api_related: [[api-app-me|API-APP-ME]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-preferences|TEST-PREFERENCES]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `writes` -> [[model-aion-profile|MODEL-AION-PROFILE]]: Settings API persists profile data

Incoming:
- [[comp-web-app|COMP-WEB-APP]] -> `calls`: Web shell reads and updates current user settings

## Chains

- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)

## Evidence

- `EVID-API-APP-ME-PROOF` behavior verified: App me/settings API proof refreshed with authenticated-session guard settings profile/preference update and proactive opt-in persistence tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_app_me_requires_authenticated_session tests/test_api_routes.py::test_app_patch_settings_updates_profile_preferences_and_display_name tests/test_api_routes.py::test_app_patch_settings_persists_proactive_opt_in_without_semantic_side_effects`.

## Theory Claims

- none

## Notes

Combines current user and settings profile operations for initial graph.
