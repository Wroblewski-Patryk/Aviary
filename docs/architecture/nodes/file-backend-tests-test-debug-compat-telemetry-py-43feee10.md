---
id: "FILE-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-43FEEE10"
name: "test_debug_compat_telemetry.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_debug_compat_telemetry.py"
related_files: []
tags: ["auto", "test"]
---

# test_debug_compat_telemetry.py

ID: `FILE-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-43FEEE10`

## Summary

Repository file `backend/tests/test_debug_compat_telemetry.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-75a6a8ea|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-75A6A8EA]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_telemetry_defaults_to_empty_snapshot`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-03456ba1|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-03456BA1]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_telemetry_tracks_allowed_and_blocked_attempts`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-d9d70c59|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-D9D70C59]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_telemetry_uses_configured_recent_window_size`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-593dec4d|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-593DEC4D]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_telemetry_rejects_non_positive_recent_window_size`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-499f7e1f|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-499F7E1F]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_sunset_snapshot_defaults_to_zero_rates`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-bf13d3b4|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-BF13D3B4]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_sunset_snapshot_marks_migration_when_traffic_exists`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-d891d144|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-D891D144]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_sunset_snapshot_marks_migration_when_only_blocked_attempts_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-1e7630ec|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-1E7630EC]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_sunset_snapshot_marks_disabled_state_when_compat_is_off`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-a2461c21|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-A2461C21]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_recent_snapshot_defaults_when_no_attempts_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-c69493fd|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-C69493FD]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_recent_snapshot_marks_mixed_state_for_balanced_outcomes`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-da59720a|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-DA59720A]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_recent_snapshot_marks_disabled_state_when_compat_is_off`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-62fe3b32|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-62FE3B32]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_freshness_snapshot_defaults_when_no_attempts_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-f473f6f5|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-F473F6F5]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_freshness_snapshot_marks_fresh_state_when_last_attempt_is_recent`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-177b45e2|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-177B45E2]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_freshness_snapshot_marks_stale_state_when_last_attempt_age_crosses_threshold`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-acfd4db1|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-ACFD4DB1]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_freshness_snapshot_rejects_non_positive_stale_threshold`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-ada2997d|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-ADA2997D]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_activity_snapshot_marks_compat_disabled_state_when_route_is_off`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-c44441ca|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-C44441CA]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_activity_snapshot_marks_no_attempts_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-51475684|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-51475684]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_activity_snapshot_marks_stale_historical_state_when_last_attempt_is_stale`.
- `parent_of` -> [[pyfunc-backend-tests-test-debug-compat-telemetry-py-test-debug-query-c-61a64a13|PYFUNC-BACKEND-TESTS-TEST-DEBUG-COMPAT-TELEMETRY-PY-TEST-DEBUG-QUERY-C-61A64A13]]: `backend/tests/test_debug_compat_telemetry.py` contains function `test_debug_query_compat_activity_snapshot_marks_recent_attempts_state_when_last_attempt_is_fresh`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
