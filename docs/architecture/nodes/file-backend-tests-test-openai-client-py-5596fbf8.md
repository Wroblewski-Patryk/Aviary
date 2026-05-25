---
id: "FILE-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-5596FBF8"
name: "test_openai_client.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_openai_client.py"
related_files: []
tags: ["auto", "test"]
---

# test_openai_client.py

ID: `FILE-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-5596FBF8`

## Summary

Repository file `backend/tests/test_openai_client.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-tests-test-openai-client-py-fakeresponses-f64ff4a1|PYCLASS-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-FAKERESPONSES-F64FF4A1]]: `backend/tests/test_openai_client.py` contains class `_FakeResponses`.
- `parent_of` -> [[pyclass-backend-tests-test-openai-client-py-fakeclient-a0bdeea4|PYCLASS-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-FAKECLIENT-A0BDEEA4]]: `backend/tests/test_openai_client.py` contains class `_FakeClient`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-classify-cd4b7425|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-CLASSIFY-CD4B7425]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_classify_affective_state_accepts_valid_structured_payload`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-classify-d63045b5|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-CLASSIFY-D63045B5]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_classify_affective_state_extracts_json_object_from_wrapped_text`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-classify-be535fd9|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-CLASSIFY-BE535FD9]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_classify_affective_state_returns_diagnostic_when_schema_keys_are_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-classify-92e53ba4|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-CLASSIFY-92E53BA4]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_classify_affective_state_returns_diagnostic_when_schema_type_is_invalid`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-classify-1d84e17f|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-CLASSIFY-1D84E17F]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_classify_affective_state_returns_diagnostic_when_parse_fails`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-generate-6a879bb0|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-GENERATE-6A879BB0]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_generate_reply_uses_api_chat_response_budget`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-generate-ae728f41|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-GENERATE-AE728F41]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_generate_reply_keeps_concise_api_style_bounded_with_buffer`.
- `parent_of` -> [[pyfunc-backend-tests-test-openai-client-py-test-openai-client-generate-6a9563e6|PYFUNC-BACKEND-TESTS-TEST-OPENAI-CLIENT-PY-TEST-OPENAI-CLIENT-GENERATE-6A9563E6]]: `backend/tests/test_openai_client.py` contains function `test_openai_client_generate_reply_uses_telegram_budget_for_telegram_turn`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
