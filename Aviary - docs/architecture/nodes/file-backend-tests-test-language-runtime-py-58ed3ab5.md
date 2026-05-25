---
id: "FILE-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-58ED3AB5"
name: "test_language_runtime.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_language_runtime.py"
related_files: []
tags: ["auto", "test"]
---

# test_language_runtime.py

ID: `FILE-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-58ED3AB5`

## Summary

Repository file `backend/tests/test_language_runtime.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-event-a5943a5c|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-EVENT-A5943A5C]]: `backend/tests/test_language_runtime.py` contains function `_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-pre-563e5809|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-PRE-563E5809]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_prefers_explicit_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-use-5d12cdc4|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-USE-5D12CDC4]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_uses_polish_thanks_keyword_without_diacritics`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-language-continuity-c7960c43|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-LANGUAGE-CONTINUITY-C7960C43]]: `backend/tests/test_language_runtime.py` contains function `test_language_continuity_policy_snapshot_pins_supported_language_boundary`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-wit-c874a888|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-WIT-C874A888]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_with_diagnostics_exposes_explicit_request_posture`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-use-e27f9e81|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-USE-E27F9E81]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_uses_recent_memory_for_short_follow_up`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-use-026b005d|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-USE-026B005D]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_uses_user_profile_when_recent_memory_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-wit-88983f77|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-WIT-88983F77]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_with_diagnostics_ignores_unsupported_profile_language_and_falls_back_to_default`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-pre-6bfd1683|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-PRE-6BFD1683]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_prefers_recent_memory_over_user_profile`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-use-45cd8ff5|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-USE-45CD8FF5]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_uses_payload_language_from_recent_memory`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-ign-33fe51bc|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-IGN-33FE51BC]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_ignores_unsupported_memory_language_and_falls_back_to_profile`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-detect-language-can-70c95d91|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-DETECT-LANGUAGE-CAN-70C95D91]]: `backend/tests/test_language_runtime.py` contains function `test_detect_language_can_prefer_explicit_profile_preference_on_ambiguous_follow_up`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-perception-agent-pr-7d485ea1|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-PERCEPTION-AGENT-PR-7D485EA1]]: `backend/tests/test_language_runtime.py` contains function `test_perception_agent_propagates_detected_language`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-perception-agent-us-9e1f9753|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-PERCEPTION-AGENT-US-9E1F9753]]: `backend/tests/test_language_runtime.py` contains function `test_perception_agent_uses_memory_language_for_ambiguous_text`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-perception-agent-us-8bffb3a4|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-PERCEPTION-AGENT-US-8BFFB3A4]]: `backend/tests/test_language_runtime.py` contains function `test_perception_agent_uses_profile_language_for_ambiguous_text_without_recent_memory`.
- `parent_of` -> [[pyfunc-backend-tests-test-language-runtime-py-test-perception-agent-em-d0b096ca|PYFUNC-BACKEND-TESTS-TEST-LANGUAGE-RUNTIME-PY-TEST-PERCEPTION-AGENT-EM-D0B096CA]]: `backend/tests/test_language_runtime.py` contains function `test_perception_agent_emits_topic_tags_for_planning_and_production`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
