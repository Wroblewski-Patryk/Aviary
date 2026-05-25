---
id: "FILE-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-CFF77632"
name: "test_delivery_router.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_delivery_router.py"
related_files: []
tags: ["auto", "test"]
---

# test_delivery_router.py

ID: `FILE-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-CFF77632`

## Summary

Repository file `backend/tests/test_delivery_router.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-tests-test-delivery-router-py-faketelegramclient-92912ffc|PYCLASS-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-FAKETELEGRAMCLIENT-92912FFC]]: `backend/tests/test_delivery_router.py` contains class `FakeTelegramClient`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-hand-8ee4c5bd|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-HAND-8EE4C5BD]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_handles_api_channel`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-appe-8288dcc6|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-APPE-8288DCC6]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_appends_execution_envelope_note_for_connector_safe_delivery`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-hand-45f8639b|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-HAND-45F8639B]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_handles_telegram_channel`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-requ-0545b9bf|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-REQU-0545B9BF]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_requires_chat_id_for_telegram`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-surf-0e57252e|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-SURF-0E57252E]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_surfaces_telegram_api_errors`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-hand-d1278b3a|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-HAND-D1278B3A]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_handles_telegram_delivery_exception_as_fail_result`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-segm-5de770be|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-SEGM-5DE770BE]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_segments_long_telegram_messages`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-pref-51167c22|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-PREF-51167C22]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_prefers_sentence_boundary_for_telegram_segments`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-uses-cfdcd5be|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-USES-CFDCD5BE]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_uses_word_boundary_before_hard_split`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-hard-c7ab7310|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-HARD-C7AB7310]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_hard_splits_only_when_no_safe_boundary_exists`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-appl-4201d49a|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-APPL-4201D49A]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_applies_safe_html_formatting_for_supported_markdown`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-appl-d28cebf1|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-APPL-D28CEBF1]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_applies_safe_italic_formatting_for_supported_markdown`.
- `parent_of` -> [[pyfunc-backend-tests-test-delivery-router-py-test-delivery-router-fall-20104bac|PYFUNC-BACKEND-TESTS-TEST-DELIVERY-ROUTER-PY-TEST-DELIVERY-ROUTER-FALL-20104BAC]]: `backend/tests/test_delivery_router.py` contains function `test_delivery_router_falls_back_to_plain_text_when_markdown_is_unsafe`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
