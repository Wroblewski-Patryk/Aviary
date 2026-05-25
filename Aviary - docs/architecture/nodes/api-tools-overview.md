---
id: "API-TOOLS-OVERVIEW"
name: "GET/PATCH /app/tools"
type: "api_route"
status: "verified"
layer: "api"
module: "backend"
feature: "tools"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/api/routes.py"
related_files: ["backend/app/core/capability_catalog.py", "backend/app/core/connector_policy.py", "web/src/lib/api.ts"]
tags: ["aviary", "api", "tools"]
---

# GET/PATCH /app/tools

ID: `API-TOOLS-OVERVIEW`

## Summary

Tools overview and preferences API surface

## Links

- parent: [[feat-tools|FEAT-TOOLS]]
- children: none
- depends_on: [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[page-tools|PAGE-TOOLS]]
- ui_related: [[page-tools|PAGE-TOOLS]]
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-connector-policy|TEST-CONNECTOR-POLICY]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]], [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing:
- `reads` -> [[model-aion-profile|MODEL-AION-PROFILE]]: Tools preferences are profile-backed

Incoming:
- [[page-tools|PAGE-TOOLS]] -> `calls`: Tools route consumes tools overview and preferences endpoints
- [[test-connector-policy|TEST-CONNECTOR-POLICY]] -> `verifies`: Connector policy tests verify tools permission posture

## Chains

- `CHAIN-TOOLS-OVERVIEW` Tools overview execution chain (verified, high)

## Evidence

- `EVID-API-TOOLS-OVERVIEW-PROOF` behavior verified: Tools overview API proof refreshed with grouped backend truth provider-backed readiness and preferences update contract tests (`backend/tests/test_api_routes.py`). Command: `python -m pytest -q tests/test_api_routes.py::test_app_tools_overview_exposes_grouped_backend_truth tests/test_api_routes.py::test_app_tools_overview_marks_provider_backed_integrations_ready_when_configured tests/test_api_routes.py::test_app_patch_tools_preferences_updates_requested_enablement_state`.

## Theory Claims

- none

## Notes

Initial graph groups overview and preferences together.
