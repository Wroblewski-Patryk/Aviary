---
id: "FILE-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-0D89869E"
name: "test_architecture_graph_query.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_architecture_graph_query.py"
related_files: []
tags: ["auto", "test"]
---

# test_architecture_graph_query.py

ID: `FILE-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-0D89869E`

## Summary

Repository file `backend/tests/test_architecture_graph_query.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-load-query-modul-a977c9dc|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-LOAD-QUERY-MODUL-A977C9DC]]: `backend/tests/test_architecture_graph_query.py` contains function `load_query_module`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-sample-graph-5ace7cc6|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-SAMPLE-GRAPH-5ACE7CC6]]: `backend/tests/test_architecture_graph_query.py` contains function `sample_graph`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-query-node-eccaa35a|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-QUERY-NODE-ECCAA35A]]: `backend/tests/test_architecture_graph_query.py` contains function `test_query_node_includes_impact_chain_evidence_and_theory_claims`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-search-node-d6cb7c76|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-SEARCH-NODE-D6CB7C76]]: `backend/tests/test_architecture_graph_query.py` contains function `test_search_nodes_matches_description_and_tags`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-gap-detecti-9fad9999|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-GAP-DETECTI-9FAD9999]]: `backend/tests/test_architecture_graph_query.py` contains function `test_gap_detection_flags_missing_proof_for_incomplete_ui_node`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-operational-19ec0b2a|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-OPERATIONAL-19EC0B2A]]: `backend/tests/test_architecture_graph_query.py` contains function `test_operational_gap_mode_ignores_strict_proof_requirements_for_auto_nodes`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-chain-missi-6b97f801|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CHAIN-MISSI-6B97F801]]: `backend/tests/test_architecture_graph_query.py` contains function `test_chain_missing_links_do_not_overreport_on_model_nodes`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-gap-report-577ba02e|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-GAP-REPORT-577BA02E]]: `backend/tests/test_architecture_graph_query.py` contains function `test_gap_report_excludes_auto_inventory_rows_by_default`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-gap-report-2720e403|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-GAP-REPORT-2720E403]]: `backend/tests/test_architecture_graph_query.py` contains function `test_gap_report_can_include_auto_inventory_rows`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-cli-json-ou-a1734a56|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CLI-JSON-OU-A1734A56]]: `backend/tests/test_architecture_graph_query.py` contains function `test_cli_json_output_for_known_node`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-cli-gap-rep-c2261e3e|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CLI-GAP-REP-C2261E3E]]: `backend/tests/test_architecture_graph_query.py` contains function `test_cli_gap_report_json_output_excludes_auto_rows_by_default`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-cli-fail-on-1b34c904|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CLI-FAIL-ON-1B34C904]]: `backend/tests/test_architecture_graph_query.py` contains function `test_cli_fail_on_gaps_returns_nonzero_when_gaps_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-cli-fail-on-ef505f5d|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CLI-FAIL-ON-EF505F5D]]: `backend/tests/test_architecture_graph_query.py` contains function `test_cli_fail_on_gaps_returns_zero_when_no_gaps_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-cli-missing-10b63c5e|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CLI-MISSING-10B63C5E]]: `backend/tests/test_architecture_graph_query.py` contains function `test_cli_missing_node_returns_nonzero_with_suggestions`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-35344a9a|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-35344A9A]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_query_smoke_for_architecture_workflow`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-0eca5d40|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-0ECA5D40]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_gap_audit_smoke_returns_curated_rows_or_zero_gap_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-59e1cf70|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-59E1CF70]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_event_ingress_has_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-a04a5897|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-A04A5897]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_app_chat_api_and_event_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-691a95aa|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-691A95AA]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_runtime_memory_docs_and_features_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-90a48c79|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-90A48C79]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_service_test_prompt_nodes_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-57c4bd78|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-57C4BD78]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_curated_medium_risk_cleanup_nodes_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-bf794956|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-BF794956]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_runtime_agent_stage_nodes_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-e00dac3a|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-E00DAC3A]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_profile_settings_direct_proof_nodes_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-8deb58cb|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-8DEB58CB]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_personality_overview_direct_proof_nodes_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-95c11554|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-95C11554]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_web_shell_component_node_has_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-fe0c9331|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-FE0C9331]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_telegram_feature_node_has_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-025a073a|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-025A073A]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_docs_pages_service_and_test_nodes_have_no_gaps`.
- `parent_of` -> [[pyfunc-backend-tests-test-architecture-graph-query-py-test-current-gra-44c56d94|PYFUNC-BACKEND-TESTS-TEST-ARCHITECTURE-GRAPH-QUERY-PY-TEST-CURRENT-GRA-44C56D94]]: `backend/tests/test_architecture_graph_query.py` contains function `test_current_graph_ui_and_workflow_nodes_have_no_gaps`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
