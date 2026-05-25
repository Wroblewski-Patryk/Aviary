---
id: "TEST-SCHEMA-BASELINE"
name: "Schema Baseline Tests"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "data_model"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/tests/test_schema_baseline.py"
related_files: []
tags: ["aviary", "test", "schema"]
---

# Schema Baseline Tests

ID: `TEST-SCHEMA-BASELINE`

## Summary

Database schema baseline tests

## Links

- parent: [[feat-data-model|FEAT-DATA-MODEL]]
- children: none
- depends_on: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[feat-data-model|FEAT-DATA-MODEL]]
- ui_related: none
- api_related: none
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-schema-baseline|TEST-SCHEMA-BASELINE]]
- docs_related: [[doc-data-reference|DOC-DATA-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[feat-data-model|FEAT-DATA-MODEL]]: Schema baseline tests verify data model contracts

Incoming: none

## Chains

- `CHAIN-DATA-MODEL-SCHEMA` Data model schema proof chain (verified, high)

## Evidence

- `EVID-TEST-SCHEMA-BASELINE-PROOF` test verified: Schema baseline test node proof refreshed with structured memory payload column check (`backend/tests/test_schema_baseline.py`). Command: `python -m pytest -q tests/test_schema_baseline.py::test_schema_baseline_tracks_structured_memory_payload_column`.

## Theory Claims

- none

## Notes

Schema proof must run after migrations/model changes.
