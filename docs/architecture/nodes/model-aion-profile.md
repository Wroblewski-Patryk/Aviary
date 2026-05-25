---
id: "MODEL-AION-PROFILE"
name: "AionProfile"
type: "model"
status: "verified"
layer: "database"
module: "memory"
feature: "profile_settings"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/memory/models.py"
related_files: ["backend/migrations/versions/20260425_0010_add_telegram_link_fields_to_profile.py", "backend/migrations/versions/20260425_0011_add_ui_language_to_profile.py", "backend/migrations/versions/20260426_0012_add_utc_offset_to_profile.py"]
tags: ["aviary", "database", "profile"]
---

# AionProfile

ID: `MODEL-AION-PROFILE`

## Summary

User profile language timezone Telegram link and tool preference state

## Links

- parent: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- children: none
- depends_on: [[model-aion-memory|MODEL-AION-MEMORY]]
- used_by: [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]]
- ui_related: none
- api_related: [[api-app-me|API-APP-ME]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-preferences|TEST-PREFERENCES]], [[test-api-routes|TEST-API-ROUTES]]
- docs_related: [[doc-data-reference|DOC-DATA-REFERENCE]]
- agent_related: none

## Relations

Outgoing: none

Incoming:
- [[api-app-me|API-APP-ME]] -> `writes`: Settings API persists profile data
- [[test-preferences|TEST-PREFERENCES]] -> `verifies`: Preferences tests verify profile preference parsing/persistence
- [[api-app-auth|API-APP-AUTH]] -> `writes`: Auth API creates and resolves the authenticated app user profile and session boundary
- [[api-tools-overview|API-TOOLS-OVERVIEW]] -> `reads`: Tools preferences are profile-backed
- [[feat-data-model|FEAT-DATA-MODEL]] -> `parent_of`: Data model feature owns AionProfile seed node

## Chains

- `CHAIN-APP-AUTH` App auth session execution chain (verified, high)
- `CHAIN-DATA-MODEL-SCHEMA` Data model schema proof chain (verified, high)
- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)
- `CHAIN-TOOLS-OVERVIEW` Tools overview execution chain (verified, high)

## Evidence

- `EVID-MODEL-AION-PROFILE-PROOF` test verified: AionProfile model proof refreshed with Alembic head profile language UI language and UTC offset column checks (`backend/tests/test_schema_baseline.py`). Command: `python -m pytest -q tests/test_schema_baseline.py::test_alembic_head_includes_ui_language_on_profile`.

## Theory Claims

- none

## Notes

Profile settings and Telegram linking depend on this model.
