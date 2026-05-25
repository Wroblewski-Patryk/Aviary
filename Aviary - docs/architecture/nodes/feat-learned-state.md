---
id: "FEAT-LEARNED-STATE"
name: "Personality Learned State Overview"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "personality"
feature: "learned_state"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "docs/pipelines/index.md"
related_files: ["web/src/App.tsx", "backend/app/api/routes.py", "backend/app/core/learned_state_policy.py"]
tags: ["aviary", "feature", "personality", "memory"]
---

# Personality Learned State Overview

ID: `FEAT-LEARNED-STATE`

## Summary

Backend-backed overview of learned state recent activity and personality signals

## Links

- parent: none
- children: [[page-personality|PAGE-PERSONALITY]], [[api-personality-overview|API-PERSONALITY-OVERVIEW]]
- depends_on: [[api-personality-overview|API-PERSONALITY-OVERVIEW]]
- used_by: [[page-personality|PAGE-PERSONALITY]]
- ui_related: [[page-personality|PAGE-PERSONALITY]]
- api_related: [[api-personality-overview|API-PERSONALITY-OVERVIEW]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-memory-repository|TEST-MEMORY-REPOSITORY]]
- docs_related: [[doc-memory-system|DOC-MEMORY-SYSTEM]]
- agent_related: none

## Relations

Outgoing: none

Incoming: none

## Chains

- `CHAIN-PERSONALITY-OVERVIEW` Personality learned-state overview chain (verified, high)

## Evidence

- `EVID-PERSONALITY-OVERVIEW-CHAIN-REFRESH` behavior verified: Personality learned-state overview chain refreshed with focused backend personality API test memory repository tests web build and route smoke including the Personality route marker (`.codex/tasks/PRJ-1281-personality-overview-chain-refresh.md`).

## Theory Claims

- none

## Notes

Personality overview is part of traceability matrix.
