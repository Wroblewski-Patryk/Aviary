---
id: "FILE-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-CE379915"
name: "test_behavior_validation_script.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_behavior_validation_script.py"
related_files: []
tags: ["auto", "test"]
---

# test_behavior_validation_script.py

ID: `FILE-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-CE379915`

## Summary

Repository file `backend/tests/test_behavior_validation_script.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-summary-c80f4c40|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-SUMMARY-C80F4C40]]: `backend/tests/test_behavior_validation_script.py` contains function `_summary`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-valid-v1-readi-b3181d94|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-VALID-V1-READI-B3181D94]]: `backend/tests/test_behavior_validation_script.py` contains function `_valid_v1_readiness_policy`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-ci-gate-f-36d91b4f|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-CI-GATE-F-36D91B4F]]: `backend/tests/test_behavior_validation_script.py` contains function `test_ci_gate_fails_when_no_tests_collected_and_tests_are_required`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-ci-gate-a-78efcc3e|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-CI-GATE-A-78EFCC3E]]: `backend/tests/test_behavior_validation_script.py` contains function `test_ci_gate_allows_empty_collection_when_requirement_is_disabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-ci-gate-u-fcf00c35|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-CI-GATE-U-FCF00C35]]: `backend/tests/test_behavior_validation_script.py` contains function `test_ci_gate_uses_normalized_reason_codes_for_failed_and_error_paths`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-operator-806d79c3|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-OPERATOR-806D79C3]]: `backend/tests/test_behavior_validation_script.py` contains function `test_operator_gate_tracks_pytest_exit_only`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-incl-5839ab8e|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-INCL-5839AB8E]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_includes_gate_payload_and_returns_ci_failure_on_gate_violation`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-incl-07171ccd|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-INCL-07171CCD]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_includes_gate_payload_and_keeps_operator_mode_exit_code`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-eval-466ea68f|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-EVAL-466EA68F]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_evaluates_existing_artifact_without_running_pytest`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-d3222797|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-D3222797]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_ci_gate_when_existing_artifact_schema_major_version_is_incompatible`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-keep-0a01e6ad|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-KEEP-0A01E6AD]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_keeps_operator_mode_backward_compatible_for_schema_major_version_mismatch`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-mark-5811ef12|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-MARK-5811EF12]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_marks_ci_gate_failed_when_existing_artifact_summary_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-mark-56a7ccdc|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-MARK-56A7CCDC]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_marks_artifact_input_unreadable_for_missing_artifact_path`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-mark-fb16fbbb|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-MARK-FB16FBBB]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_marks_artifact_summary_invalid_when_existing_summary_is_not_numeric`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-reco-03f84f89|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-RECO-03F84F89]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_records_incident_evidence_summary_when_valid_input_is_provided`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-2723b3ca|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-2723B3CA]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_durable_attention_posture_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-bea1b363|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-BEA1B363]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_policy_surface_is_incomplete`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-23854bf3|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-23854BF3]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_tool_grounded_learning_contract_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-4a3a4e96|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-4A3A4E96]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_debug_posture_does_not_match_dedicated_admin_only_baseline`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-8f2ba66c|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-8F2BA66C]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_external_cadence_cutover_proof_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-bc665e67|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-BC665E67]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_telegram_conversation_surface_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-c235ed4c|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-C235ED4C]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_proactive_posture_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-behavior-validation-script-py-test-main-fail-c4a511ee|PYFUNC-BACKEND-TESTS-TEST-BEHAVIOR-VALIDATION-SCRIPT-PY-TEST-MAIN-FAIL-C4A511EE]]: `backend/tests/test_behavior_validation_script.py` contains function `test_main_fails_when_incident_evidence_retrieval_alignment_drifts`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
