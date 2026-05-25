---
id: "FEAT-DATA-MODEL"
name: "Data Model"
type: "feature"
status: "verified"
layer: "database"
module: "data"
feature: "data_model"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-11"
verification_status: "verified"
file_path: "docs/data/index.md"
related_files: ["backend/app/memory/models.py", "backend/migrations/versions"]
tags: ["aviary", "feature", "data"]
---

# Data Model

ID: `FEAT-DATA-MODEL`

## Summary

ORM models migrations and generated ERD/columns reference

## Links

- parent: none
- children: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- depends_on: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]], [[feat-profile-settings|FEAT-PROFILE-SETTINGS]], [[feat-learned-state|FEAT-LEARNED-STATE]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-app-me|API-APP-ME]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-schema-baseline|TEST-SCHEMA-BASELINE]]
- docs_related: [[doc-data-reference|DOC-DATA-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[model-aion-memory|MODEL-AION-MEMORY]]: Data model feature owns AionMemory seed node
- `parent_of` -> [[model-aion-profile|MODEL-AION-PROFILE]]: Data model feature owns AionProfile seed node

Incoming:
- [[test-schema-baseline|TEST-SCHEMA-BASELINE]] -> `verifies`: Schema baseline tests verify data model contracts
- [[doc-data-reference|DOC-DATA-REFERENCE]] -> `documents`: Data model reference documents ORM tables migrations repository ownership feature usage and schema change checklist

## Chains

- `CHAIN-DATA-MODEL-SCHEMA` Data model schema proof chain (verified, high)

## Evidence

- `EVID-DATA-MODEL-SCHEMA-CHAIN` behavior verified: Data model schema chain refreshed with expected table inventory named unique constraints payload column and Alembic head schema parity tests (`backend/tests/test_schema_baseline.py`). Command: `python -m pytest -q tests/test_schema_baseline.py`.

## Theory Claims

- none

## Notes

Initial graph seeds only core models; full model coverage remains next graph expansion.
