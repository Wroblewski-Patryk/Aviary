---
id: "FILE-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EE694E9A"
name: "runtime_policy.py"
type: "backend_file"
status: "implemented"
layer: "backend"
module: "backend"
feature: "backend"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/app/core/runtime_policy.py"
related_files: []
tags: ["auto", "backend"]
---

# runtime_policy.py

ID: `FILE-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EE694E9A`

## Summary

Repository file `backend/app/core/runtime_policy.py` auto-discovered for architecture graph inventory.

## Links

- parent: none
- children: none
- depends_on: none
- used_by: none
- ui_related: none
- api_related: none
- database_related: none
- tests_related: none
- docs_related: none
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-app-environment-66527c6d|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-APP-ENVIRONMENT-66527C6D]]: `backend/app/core/runtime_policy.py` contains function `app_environment`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-enabled-58a2fb92|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-ENABLED-58A2FB92]]: `backend/app/core/runtime_policy.py` contains function `event_debug_enabled`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-token-required-29b6a58e|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-TOKEN-REQUIRED-29B6A58E]]: `backend/app/core/runtime_policy.py` contains function `event_debug_token_required`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-production-debug-token-requi-46f8ca5b|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-PRODUCTION-DEBUG-TOKEN-REQUI-46F8CA5B]]: `backend/app/core/runtime_policy.py` contains function `production_debug_token_required`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-query-compat-ena-fad29912|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-QUERY-COMPAT-ENA-FAD29912]]: `backend/app/core/runtime_policy.py` contains function `event_debug_query_compat_enabled`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-query-compat-sou-045fbb9d|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-QUERY-COMPAT-SOU-045FBB9D]]: `backend/app/core/runtime_policy.py` contains function `event_debug_query_compat_source`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-shared-ingress-m-8b8ec0e4|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-SHARED-INGRESS-M-8B8EC0E4]]: `backend/app/core/runtime_policy.py` contains function `event_debug_shared_ingress_mode`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-shared-ingress-m-6e8b9444|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-SHARED-INGRESS-M-6E8B9444]]: `backend/app/core/runtime_policy.py` contains function `event_debug_shared_ingress_mode_source`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-shared-ingress-p-38117e04|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-SHARED-INGRESS-P-38117E04]]: `backend/app/core/runtime_policy.py` contains function `event_debug_shared_ingress_posture`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-token-missing-in-bfae7e65|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-TOKEN-MISSING-IN-BFAE7E65]]: `backend/app/core/runtime_policy.py` contains function `event_debug_token_missing_in_production`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-query-compat-ena-80e084d2|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-QUERY-COMPAT-ENA-80E084D2]]: `backend/app/core/runtime_policy.py` contains function `event_debug_query_compat_enabled_in_production`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-debug-access-posture-56fc3573|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-DEBUG-ACCESS-POSTURE-56FC3573]]: `backend/app/core/runtime_policy.py` contains function `debug_access_posture`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-debug-token-policy-hint-b2725bc1|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-DEBUG-TOKEN-POLICY-HINT-B2725BC1]]: `backend/app/core/runtime_policy.py` contains function `debug_token_policy_hint`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-source-1c5bd383|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-SOURCE-1C5BD383]]: `backend/app/core/runtime_policy.py` contains function `event_debug_source`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-startup-schema-mode-f6d13db7|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STARTUP-SCHEMA-MODE-F6D13DB7]]: `backend/app/core/runtime_policy.py` contains function `startup_schema_mode`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-production-policy-enforcemen-dd30b22a|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-PRODUCTION-POLICY-ENFORCEMEN-DD30B22A]]: `backend/app/core/runtime_policy.py` contains function `production_policy_enforcement`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-production-policy-mismatches-c2b5433b|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-PRODUCTION-POLICY-MISMATCHES-C2B5433B]]: `backend/app/core/runtime_policy.py` contains function `production_policy_mismatches`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-production-policy-mismatch-c-57c9e777|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-PRODUCTION-POLICY-MISMATCH-C-57C9E777]]: `backend/app/core/runtime_policy.py` contains function `production_policy_mismatch_count`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-strict-startup-blocked-0fe53136|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STRICT-STARTUP-BLOCKED-0FE53136]]: `backend/app/core/runtime_policy.py` contains function `strict_startup_blocked`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-strict-rollout-ready-4ef91157|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STRICT-ROLLOUT-READY-4EF91157]]: `backend/app/core/runtime_policy.py` contains function `strict_rollout_ready`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-recommended-production-polic-d40a78d3|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-RECOMMENDED-PRODUCTION-POLIC-D40A78D3]]: `backend/app/core/runtime_policy.py` contains function `recommended_production_policy_enforcement`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-strict-rollout-hint-fbb0ad17|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STRICT-ROLLOUT-HINT-FBB0AD17]]: `backend/app/core/runtime_policy.py` contains function `strict_rollout_hint`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-startup-schema-compatibility-8684773c|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STARTUP-SCHEMA-COMPATIBILITY-8684773C]]: `backend/app/core/runtime_policy.py` contains function `startup_schema_compatibility_posture`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-startup-schema-compatibility-e3b2cd6f|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STARTUP-SCHEMA-COMPATIBILITY-E3B2CD6F]]: `backend/app/core/runtime_policy.py` contains function `startup_schema_compatibility_sunset_ready`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-startup-schema-compatibility-81bfa216|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STARTUP-SCHEMA-COMPATIBILITY-81BFA216]]: `backend/app/core/runtime_policy.py` contains function `startup_schema_compatibility_sunset_reason`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-shared-ingress-s-e6af77dd|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-SHARED-INGRESS-S-E6AF77DD]]: `backend/app/core/runtime_policy.py` contains function `event_debug_shared_ingress_sunset_ready`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-event-debug-shared-ingress-s-e6405d41|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EVENT-DEBUG-SHARED-INGRESS-S-E6405D41]]: `backend/app/core/runtime_policy.py` contains function `event_debug_shared_ingress_sunset_reason`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-compatibility-sunset-blocker-e2d23425|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-COMPATIBILITY-SUNSET-BLOCKER-E2D23425]]: `backend/app/core/runtime_policy.py` contains function `compatibility_sunset_blockers`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-compatibility-sunset-ready-fb8298b1|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-COMPATIBILITY-SUNSET-READY-FB8298B1]]: `backend/app/core/runtime_policy.py` contains function `compatibility_sunset_ready`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-startup-schema-removal-windo-790c1061|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-STARTUP-SCHEMA-REMOVAL-WINDO-790C1061]]: `backend/app/core/runtime_policy.py` contains function `startup_schema_removal_window`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-shared-debug-ingress-enforce-7a6a6c3f|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-SHARED-DEBUG-INGRESS-ENFORCE-7A6A6C3F]]: `backend/app/core/runtime_policy.py` contains function `shared_debug_ingress_enforcement_window`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-release-readiness-violations-43782470|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-RELEASE-READINESS-VIOLATIONS-43782470]]: `backend/app/core/runtime_policy.py` contains function `release_readiness_violations`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-release-readiness-snapshot-c8ecc954|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-RELEASE-READINESS-SNAPSHOT-C8ECC954]]: `backend/app/core/runtime_policy.py` contains function `release_readiness_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-core-runtime-policy-py-runtime-policy-snapshot-e63f8c21|PYFUNC-BACKEND-APP-CORE-RUNTIME-POLICY-PY-RUNTIME-POLICY-SNAPSHOT-E63F8C21]]: `backend/app/core/runtime_policy.py` contains function `runtime_policy_snapshot`.

Incoming:
- [[file-backend-tests-test-runtime-policy-py-b6603348|FILE-BACKEND-TESTS-TEST-RUNTIME-POLICY-PY-B6603348]] -> `verifies`: Test file `backend/tests/test_runtime_policy.py` appears to verify `FILE-BACKEND-APP-CORE-RUNTIME-POLICY-PY-EE694E9A`.

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
