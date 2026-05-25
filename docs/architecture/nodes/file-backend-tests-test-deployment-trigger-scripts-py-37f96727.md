---
id: "FILE-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-37F96727"
name: "test_deployment_trigger_scripts.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_deployment_trigger_scripts.py"
related_files: []
tags: ["auto", "test"]
---

# test_deployment_trigger_scripts.py

ID: `FILE-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-37F96727`

## Summary

Repository file `backend/tests/test_deployment_trigger_scripts.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-powershell-exe-b3191e90|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-POWERSHELL-EXE-B3191E90]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_powershell_exe`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-backend-o-9c009c96|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-BACKEND-O-9C009C96]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_backend_operator_scripts_expose_help_from_backend_working_directory`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-organizer-tool-8254b937|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-ORGANIZER-TOOL-8254B937]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_organizer_tool_activation_snapshot`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-organizer-dail-151ec98b|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-ORGANIZER-DAIL-151EC98B]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_organizer_daily_use_workflows`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-capability-cat-2b1e870a|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-CAPABILITY-CAT-2B1E870A]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_capability_catalog_snapshot`.
- `parent_of` -> [[pyclass-backend-tests-test-deployment-trigger-scripts-py-stubaionhandle-368ea91c|PYCLASS-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-STUBAIONHANDLE-368EA91C]]: `backend/tests/test_deployment_trigger_scripts.py` contains class `_StubAionHandler`.
- `parent_of` -> [[pyclass-backend-tests-test-deployment-trigger-scripts-py-stubaionserver-b98473b5|PYCLASS-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-STUBAIONSERVER-B98473B5]]: `backend/tests/test_deployment_trigger_scripts.py` contains class `_StubAionServer`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-stub-aion-serv-5421adad|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-STUB-AION-SERV-5421ADAD]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `stub_aion_server`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-run-release-sm-bc79fe2f|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-RUN-RELEASE-SM-BC79FE2F]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_run_release_smoke`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-behavior-0b6cfa61|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-BEHAVIOR-0B6CFA61]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_behavior_validation_powershell_wrapper_resolves_python_from_repo_root`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-write-evidence-55aff25f|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-WRITE-EVIDENCE-55AFF25F]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_write_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-write-incident-e22eea58|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-WRITE-INCIDENT-E22EEA58]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `_write_incident_bundle`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-trigger-m-edc73ddc|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-TRIGGER-M-EDC73DDC]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_trigger_main_writes_success_evidence_file`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-trigger-m-799b5db7|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-TRIGGER-M-799B5DB7]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_trigger_main_writes_failure_evidence_file_and_returns_non_zero`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-coolify-f-7d038c57|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-COOLIFY-F-7D038C57]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_coolify_fallback_readiness_report_is_ready_with_required_inputs`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-coolify-f-8c60cae1|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-COOLIFY-F-8C60CAE1]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_coolify_fallback_readiness_report_blocks_missing_or_unsafe_inputs`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-coolify-f-52dbcc77|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-COOLIFY-F-52DBCC77]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_coolify_fallback_readiness_main_writes_blocked_report`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-g-2cb22fa1|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-G-2CB22FA1]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_go_no_go_main_goes_when_audit_and_smoke_pass`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-g-82f5aff7|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-G-82F5AFF7]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_go_no_go_main_holds_when_audit_fails`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-g-68ee14ae|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-G-68EE14AE]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_go_no_go_skips_local_head_bound_smoke_for_historical_selected_sha`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-f76de4be|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-F76DE4BE]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_allows_optional_deployment_evidence_to_be_omitted`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-9fedfeb3|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-9FEDFEB3]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_proactive_observer_posture_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-f532e15d|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-F532E15D]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_relation_source_policy_evidence_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-61d06c6d|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-61D06C6D]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_retrieval_provider_alignment_drifts`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-ba2ae687|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-BA2AE687]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_telegram_conversation_health_surface_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-948060e1|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-948060E1]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_telegram_delivery_adaptation_posture_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-f5ceba61|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-F5CEBA61]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_attention_health_surface_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-f2eea699|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-F2EEA699]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_proactive_health_surface_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-b4e566ef|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-B4E566EF]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_organizer_tool_stack_health_surface_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-c3961eea|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-C3961EEA]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_verifies_fresh_successful_deployment_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-486c7f11|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-486C7F11]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_validates_exported_incident_evidence_when_debug_mode_is_requested`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-43390f83|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-43390F83]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_verifies_incident_evidence_bundle_when_bundle_path_is_provided`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-d23425f0|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-D23425F0]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_bundle_is_partial`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-631202d5|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-631202D5]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_bundle_organizer_tool_stack_is_partial`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-530359fb|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-530359FB]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_bundle_capability_catalog_is_partial`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-34399273|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-34399273]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_debug_posture_is_not_dedicated_admin_only`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-52118c3b|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-52118C3B]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_retrieval_alignment_drifts`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-00d4a76e|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-00D4A76E]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_learned_state_health_contract_is_partial`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-ee409da5|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-EE409DA5]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_learned_state_contract_is_partial`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-0c8f6ce0|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-0C8F6CE0]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_v1_readiness_time_aware_planned_work_contract_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-cad97105|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-CAD97105]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_v1_time_aware_planned_work_contract_drifts`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-d65ec0f2|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-D65EC0F2]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_v1_readiness_treats_extension_posture_as_core_bundle_blocker`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-8798f8e7|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-8798F8E7]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_v1_readiness_treats_extension_posture_as_core_bundle_blocker`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-39ebbef7|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-39EBBEF7]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_v1_readiness_deploy_gate_drifts_from_deployment_surface`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-07d61b72|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-07D61B72]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_learned_state_tool_grounded_contract_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-3569bfc2|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-3569BFC2]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_capability_catalog_health_contract_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-182b8bad|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-182B8BAD]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_incident_evidence_organizer_tool_stack_contract_is_partial`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-51089516|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-51089516]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_organizer_tool_activation_snapshot_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-debfe94e|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-DEBFE94E]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_deployment_evidence_is_stale`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-21341f03|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-21341F03]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_deployment_evidence_response_is_unsuccessful`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-d124b913|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-D124B913]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_runtime_build_revision_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-1d613ac3|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-1D613AC3]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_runtime_build_revision_does_not_match_local_repo_head`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-6d73d47c|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-6D73D47C]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_can_wait_for_deploy_parity_until_runtime_revision_matches_local_head`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-884cee50|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-884CEE50]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_wait_for_deploy_parity_times_out_when_runtime_revision_stays_stale`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-e01125c2|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-E01125C2]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_retries_transient_health_503_before_succeeding`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-346be5de|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-346BE5DE]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_transient_health_503_exceeds_retry_budget`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-f83588d4|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-F83588D4]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_web_shell_build_revision_meta_tag_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-71e64e62|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-71E64E62]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_web_shell_build_revision_drifts_from_runtime_build_revision`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-c96355a4|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-C96355A4]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_deployment_evidence_after_sha_does_not_match_runtime_build_revision`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-a290efad|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-A290EFAD]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_compatibility_sunset_evidence_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-s-c7e3b4f3|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-S-C7E3B4F3]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_smoke_fails_when_external_cadence_cutover_fields_are_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-r-dfdcba1b|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-R-DFDCBA1B]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_reality_audit_reports_go_when_selected_sha_matches_stub_production`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-r-7a0ee8ed|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-R-7A0EE8ED]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_reality_audit_reports_revision_drift_when_production_sha_is_stale`.
- `parent_of` -> [[pyfunc-backend-tests-test-deployment-trigger-scripts-py-test-release-r-6cdda1fe|PYFUNC-BACKEND-TESTS-TEST-DEPLOYMENT-TRIGGER-SCRIPTS-PY-TEST-RELEASE-R-6CDDA1FE]]: `backend/tests/test_deployment_trigger_scripts.py` contains function `test_release_reality_audit_monitor_mode_allows_newer_local_head_when_release_sha_matches_production`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
