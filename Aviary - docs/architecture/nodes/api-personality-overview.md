---
id: "API-PERSONALITY-OVERVIEW"
name: "GET /app/personality/overview"
type: "api_route"
status: "verified"
layer: "api"
module: "backend"
feature: "learned_state"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/api/routes.py"
related_files: ["backend/app/core/learned_state_policy.py"]
tags: ["aviary", "api", "personality"]
---

# GET /app/personality/overview

ID: `API-PERSONALITY-OVERVIEW`

## Summary

Learned-state and personality overview API

## Links

- parent: [[feat-learned-state|FEAT-LEARNED-STATE]]
- children: none
- depends_on: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[page-personality|PAGE-PERSONALITY]]
- ui_related: [[page-personality|PAGE-PERSONALITY]]
- api_related: [[api-personality-overview|API-PERSONALITY-OVERVIEW]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-memory-repository|TEST-MEMORY-REPOSITORY]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]], [[doc-memory-system|DOC-MEMORY-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `reads` -> [[model-aion-memory|MODEL-AION-MEMORY]]: Personality overview reads recent activity and learned state

Incoming:
- [[page-personality|PAGE-PERSONALITY]] -> `calls`: Personality route consumes learned-state overview API

## Chains

- `CHAIN-PERSONALITY-OVERVIEW` Personality learned-state overview chain (verified, high)

## Evidence

- missing

## Theory Claims

- none

## Notes

Includes recent activity projection.
