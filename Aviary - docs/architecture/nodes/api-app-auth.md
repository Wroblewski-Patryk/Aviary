---
id: "API-APP-AUTH"
name: "App Auth API"
type: "api_route"
status: "verified"
layer: "api"
module: "backend"
feature: "auth"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/api/routes.py"
related_files: ["web/src/lib/api.ts"]
tags: ["aviary", "api", "auth"]
---

# App Auth API

ID: `API-APP-AUTH`

## Summary

Registration login logout and current-session API boundary

## Links

- parent: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- children: none
- depends_on: [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[comp-web-app|COMP-WEB-APP]]
- ui_related: none
- api_related: [[api-app-auth|API-APP-AUTH]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `writes` -> [[model-aion-profile|MODEL-AION-PROFILE]]: Auth API creates and resolves the authenticated app user profile and session boundary

Incoming:
- [[comp-web-app|COMP-WEB-APP]] -> `calls`: Web shell uses auth API for register login logout and current session boundary
- [[test-api-routes|TEST-API-ROUTES]] -> `verifies`: Focused backend API tests verify register session requirement login logout and me roundtrip contracts
- [[doc-api-reference|DOC-API-REFERENCE]] -> `documents`: API reference documents authenticated app endpoint posture

## Chains

- `CHAIN-APP-AUTH` App auth session execution chain (verified, high)

## Evidence

- `EVID-AUTH-API-CHAIN-REFRESH` behavior verified: App auth API chain refreshed with focused register session requirement login logout and current user roundtrip tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_app_auth_register_sets_session_cookie_and_returns_user_snapshot tests/test_api_routes.py::test_app_me_requires_authenticated_session tests/test_api_routes.py::test_app_login_logout_and_me_roundtrip`.

## Theory Claims

- none

## Notes

Grouped auth endpoints for initial graph dependency mapping.
