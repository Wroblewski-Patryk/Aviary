---
id: "FILE-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-3105CC20"
name: "test_event_normalization.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_event_normalization.py"
related_files: []
tags: ["auto", "test"]
---

# test_event_normalization.py

ID: `FILE-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-3105CC20`

## Summary

Repository file `backend/tests/test_event_normalization.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-bafe583f|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-BAFE583F]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-d654e3d9|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-D654E3D9]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event_ignores_internal_source_fields_from_client_payload`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-a81c5e1e|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-A81C5E1E]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event_uses_payload_text_when_top_level_text_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-a5a48102|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-A5A48102]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event_normalizes_text_and_limits_length`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-1ac763a0|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-1AC763A0]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event_normalizes_meta_field_lengths`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-coalesce-turn-te-e39a8fc8|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-COALESCE-TURN-TE-E39A8FC8]]: `backend/tests/test_event_normalization.py` contains function `test_coalesce_turn_text_normalizes_and_skips_empty_parts`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-coalesce-turn-te-7d1d760d|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-COALESCE-TURN-TE-7D1D760D]]: `backend/tests/test_event_normalization.py` contains function `test_coalesce_turn_text_applies_max_length_limit`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-d969f135|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-D969F135]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event_uses_default_user_id_when_meta_user_id_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-api-ev-3185b4aa|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-API-EV-3185B4AA]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_api_event_prefers_meta_user_id_over_default_user_id`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-normalize-telegr-6bdd7dbf|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-NORMALIZE-TELEGR-6BDD7DBF]]: `backend/tests/test_event_normalization.py` contains function `test_normalize_telegram_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-looks-like-teleg-7fedef20|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-LOOKS-LIKE-TELEG-7FEDEF20]]: `backend/tests/test_event_normalization.py` contains function `test_looks_like_telegram_update_requires_message_shape`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-build-scheduler-210486eb|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-BUILD-SCHEDULER-210486EB]]: `backend/tests/test_event_normalization.py` contains function `test_build_scheduler_event_normalizes_source_cadence_and_runtime_boundary`.
- `parent_of` -> [[pyfunc-backend-tests-test-event-normalization-py-test-build-scheduler-52989fb6|PYFUNC-BACKEND-TESTS-TEST-EVENT-NORMALIZATION-PY-TEST-BUILD-SCHEDULER-52989FB6]]: `backend/tests/test_event_normalization.py` contains function `test_build_scheduler_event_normalizes_proactive_payload_contract`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
