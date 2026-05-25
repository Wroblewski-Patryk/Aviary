---
id: "DOC-DATA-REFERENCE"
name: "Data Model Reference"
type: "documentation"
status: "verified"
layer: "docs"
module: "data"
feature: "data_model"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-11"
verification_status: "verified"
file_path: "docs/data/index.md"
related_files: ["docs/data/columns.md", "docs/data/erd.mmd"]
tags: ["aviary", "docs", "data"]
---

# Data Model Reference

ID: `DOC-DATA-REFERENCE`

## Summary

ORM tables migrations repository capability groups feature usage and data-change checklist

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
- `documents` -> [[feat-data-model|FEAT-DATA-MODEL]]: Data model reference documents ORM tables migrations repository ownership feature usage and schema change checklist
- `documents` -> [[model-aion-memory|MODEL-AION-MEMORY]]: Data reference documents AionMemory

Incoming: none

## Chains

- `CHAIN-DATA-MODEL-SCHEMA` Data model schema proof chain (verified, high)
- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)

## Evidence

- `EVID-DATA-DOCS` documentation verified: Data model reference maps ORM tables migrations feature usage and tests (`docs/data/index.md`).

## Theory Claims

- none

## Notes

Data model map is existing source for DB nodes.
