---
id: "FILE-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-919D5389"
name: "test_main_runtime_policy.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_main_runtime_policy.py"
related_files: []
tags: ["auto", "test"]
---

# test_main_runtime_policy.py

ID: `FILE-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-919D5389`

## Summary

Repository file `backend/tests/test_main_runtime_policy.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-war-49122d68|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-WAR-49122D68]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_warning_when_production_runs_with_debug_payload_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-ref-50acc21c|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-REF-50ACC21C]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_reflection_external_driver_policy_for_deferred_mode`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-ref-5fe15ef7|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-REF-5FE15EF7]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_reflection_supervision_policy_snapshot`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-ext-3df8e374|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EXT-3DF8E374]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_external_scheduler_policy_snapshot`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-war-4236718d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-WAR-4236718D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_warning_when_production_enables_query_compat_debug_route`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-wa-7d96bc4d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-WA-7D96BC4D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_warning_when_debug_payload_is_disabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-de-ecddf5ef|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-DE-ECDDF5EF]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_debug_warning_when_production_uses_environment_default_disable`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-war-64957f1e|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-WAR-64957F1E]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_warning_when_production_runs_with_schema_compatibility_mode`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-sc-60fa6eca|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-SC-60FA6ECA]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_schema_compatibility_warning_outside_production`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-w-7741a012|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-W-7741A012]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_when_strict_enforcement_and_debug_payload_enabled_in_production`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-w-f861ab6d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-W-F861AB6D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_when_strict_enforcement_and_schema_compatibility_mode_in_production`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-w-1a387f91|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-W-1A387F91]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_when_strict_enforcement_and_multiple_mismatches_in_production`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-w-3fa5842d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-W-3FA5842D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_when_strict_enforcement_and_query_compat_is_enabled_in_production`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-warn-mod-5ff631c5|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-WARN-MOD-5FF631C5]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_warn_mode_does_not_block_when_multiple_mismatches_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-str-f2d1794e|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-STR-F2D1794E]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_strict_rollout_hint_when_production_warn_mode_is_ready`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-tra-85bfa7b4|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-TRA-85BFA7B4]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_transitional_debug_ingress_blockers_when_shared_compat_paths_remain`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-w-ee13979f|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-W-EE13979F]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_with_production_default_strict_policy_when_enforcement_is_unset`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-de-1fc8a1c9|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-DE-1FC8A1C9]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_debug_token_warning_when_debug_token_is_configured`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-de-6fd4ddea|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-DE-6FD4DDEA]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_debug_token_warning_when_production_token_requirement_is_disabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-ebd3b60d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-EBD3B60D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_strategy_warning_when_provider_falls_back_to_deterministic`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-e-24173869|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-E-24173869]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_embedding_provider_fallback_when_ownership_enforcement_is_strict`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-76db5e5c|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-76DB5E5C]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_strategy_warning_when_requested_provider_is_effective`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-5cef24a3|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-5CEF24A3]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_strategy_warning_when_openai_provider_is_configured`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-0674d47d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-0674D47D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_model_governance_warning_when_deterministic_custom_model_is_requested`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-d-118d9a8e|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-D-118D9A8E]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_deterministic_custom_model_when_governance_enforcement_is_strict`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-57cb3789|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-57CB3789]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_model_governance_warning_for_deterministic_baseline_model`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-8d772dda|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-8D772DDA]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_strategy_warning_when_vectors_are_disabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-2bd882a9|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-2BD882A9]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_source_coverage_warning_when_semantic_and_affective_sources_are_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-103a0163|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-103A0163]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_source_coverage_warning_when_semantic_and_affective_sources_are_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-d11775f7|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-D11775F7]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_source_rollout_hint_when_next_source_is_pending`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-ecbb886f|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-ECBB886F]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_source_rollout_hint_when_all_sources_are_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-ba8815fb|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-BA8815FB]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_source_rollout_warning_when_rollout_enforcement_is_warn`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-blocks-e-4c51efad|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-BLOCKS-E-4C51EFAD]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_blocks_embedding_source_rollout_when_enforcement_is_strict`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-6cdb65e5|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-6CDB65E5]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_source_rollout_enforcement_hint_when_alignment_is_aligned`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-b643e24e|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-B643E24E]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_source_rollout_enforcement_hint_when_alignment_is_below_recommendation`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-6d4ae8b5|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-6D4AE8B5]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_refresh_warning_when_manual_refresh_mode_is_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-skips-em-f2b1e8bd|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-SKIPS-EM-F2B1E8BD]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_skips_embedding_refresh_warning_when_on_write_refresh_mode_is_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-5568f69d|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-5568F69D]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_refresh_hint_when_manual_mode_overrides_active_rollout_recommendation`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-47f9cecc|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-47F9CECC]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_refresh_hint_when_on_write_precedes_manual_recommendation_for_mature_rollout`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-3d867690|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-3D867690]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_strategy_hint_when_strict_rollout_is_ready_but_enforcement_is_warn`.
- `parent_of` -> [[pyfunc-backend-tests-test-main-runtime-policy-py-test-startup-logs-emb-ac5690e1|PYFUNC-BACKEND-TESTS-TEST-MAIN-RUNTIME-POLICY-PY-TEST-STARTUP-LOGS-EMB-AC5690E1]]: `backend/tests/test_main_runtime_policy.py` contains function `test_startup_logs_embedding_strategy_hint_when_enforcement_alignment_is_aligned`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
