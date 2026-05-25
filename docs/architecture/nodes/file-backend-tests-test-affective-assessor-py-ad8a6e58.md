---
id: "FILE-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-AD8A6E58"
name: "test_affective_assessor.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_affective_assessor.py"
related_files: []
tags: ["auto", "test"]
---

# test_affective_assessor.py

ID: `FILE-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-AD8A6E58`

## Summary

Repository file `backend/tests/test_affective_assessor.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-tests-test-affective-assessor-py-fakeclassifierclient-b58b2a3a|PYCLASS-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-FAKECLASSIFIERCLIENT-B58B2A3A]]: `backend/tests/test_affective_assessor.py` contains class `FakeClassifierClient`.
- `parent_of` -> [[pyfunc-backend-tests-test-affective-assessor-py-test-affective-assesso-559bce57|PYFUNC-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-TEST-AFFECTIVE-ASSESSO-559BCE57]]: `backend/tests/test_affective_assessor.py` contains function `test_affective_assessor_falls_back_without_classifier_client`.
- `parent_of` -> [[pyfunc-backend-tests-test-affective-assessor-py-test-affective-assesso-3dd1e8b2|PYFUNC-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-TEST-AFFECTIVE-ASSESSO-3DD1E8B2]]: `backend/tests/test_affective_assessor.py` contains function `test_affective_assessor_uses_ai_classifier_when_payload_is_valid`.
- `parent_of` -> [[pyfunc-backend-tests-test-affective-assessor-py-test-affective-assesso-8d56175d|PYFUNC-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-TEST-AFFECTIVE-ASSESSO-8D56175D]]: `backend/tests/test_affective_assessor.py` contains function `test_affective_assessor_uses_fallback_when_ai_payload_is_invalid`.
- `parent_of` -> [[pyfunc-backend-tests-test-affective-assessor-py-test-affective-assesso-0f163899|PYFUNC-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-TEST-AFFECTIVE-ASSESSO-0F163899]]: `backend/tests/test_affective_assessor.py` contains function `test_affective_assessor_preserves_structured_fallback_reason_from_classifier_payload`.
- `parent_of` -> [[pyfunc-backend-tests-test-affective-assessor-py-test-affective-assesso-a4b87b3a|PYFUNC-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-TEST-AFFECTIVE-ASSESSO-A4B87B3A]]: `backend/tests/test_affective_assessor.py` contains function `test_affective_assessor_adds_reason_marker_for_invalid_affective_label_payload`.
- `parent_of` -> [[pyfunc-backend-tests-test-affective-assessor-py-test-affective-assesso-7448738b|PYFUNC-BACKEND-TESTS-TEST-AFFECTIVE-ASSESSOR-PY-TEST-AFFECTIVE-ASSESSO-7448738B]]: `backend/tests/test_affective_assessor.py` contains function `test_affective_assessor_respects_disabled_policy_even_with_classifier_client`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
