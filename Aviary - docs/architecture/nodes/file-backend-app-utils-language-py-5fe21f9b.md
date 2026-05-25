---
id: "FILE-BACKEND-APP-UTILS-LANGUAGE-PY-5FE21F9B"
name: "language.py"
type: "backend_file"
status: "implemented"
layer: "backend"
module: "backend"
feature: "backend"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/app/utils/language.py"
related_files: []
tags: ["auto", "backend"]
---

# language.py

ID: `FILE-BACKEND-APP-UTILS-LANGUAGE-PY-5FE21F9B`

## Summary

Repository file `backend/app/utils/language.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-app-utils-language-py-languagedecision-38e6523a|PYCLASS-BACKEND-APP-UTILS-LANGUAGE-PY-LANGUAGEDECISION-38E6523A]]: `backend/app/utils/language.py` contains class `LanguageDecision`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-normalize-for-matching-9873fb31|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-NORMALIZE-FOR-MATCHING-9873FB31]]: `backend/app/utils/language.py` contains function `normalize_for_matching`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-tokenize-normalized-5a30f09b|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-TOKENIZE-NORMALIZED-5A30F09B]]: `backend/app/utils/language.py` contains function `tokenize_normalized`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-language-name-583665a9|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-LANGUAGE-NAME-583665A9]]: `backend/app/utils/language.py` contains function `language_name`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-preferred-language-for-templates-1fcee12f|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-PREFERRED-LANGUAGE-FOR-TEMPLATES-1FCEE12F]]: `backend/app/utils/language.py` contains function `preferred_language_for_templates`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-fallback-message-86da2bf9|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-FALLBACK-MESSAGE-86DA2BF9]]: `backend/app/utils/language.py` contains function `fallback_message`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-detect-language-77988dd7|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-DETECT-LANGUAGE-77988DD7]]: `backend/app/utils/language.py` contains function `detect_language`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-language-continuity-policy-snapsh-ccf9258d|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-LANGUAGE-CONTINUITY-POLICY-SNAPSH-CCF9258D]]: `backend/app/utils/language.py` contains function `language_continuity_policy_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-detect-language-with-diagnostics-7804d546|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-DETECT-LANGUAGE-WITH-DIAGNOSTICS-7804D546]]: `backend/app/utils/language.py` contains function `detect_language_with_diagnostics`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-infer-language-from-memory-8f05dd08|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-INFER-LANGUAGE-FROM-MEMORY-8F05DD08]]: `backend/app/utils/language.py` contains function `infer_language_from_memory`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-infer-language-from-profile-c04928ce|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-INFER-LANGUAGE-FROM-PROFILE-C04928CE]]: `backend/app/utils/language.py` contains function `infer_language_from_profile`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-contains-polish-diacritic-c5d96da0|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-CONTAINS-POLISH-DIACRITIC-C5D96DA0]]: `backend/app/utils/language.py` contains function `_contains_polish_diacritic`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-detect-explicit-language-request-d98e7739|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-DETECT-EXPLICIT-LANGUAGE-REQUEST-D98E7739]]: `backend/app/utils/language.py` contains function `_detect_explicit_language_request`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-keyword-language-decision-bc6482b1|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-KEYWORD-LANGUAGE-DECISION-BC6482B1]]: `backend/app/utils/language.py` contains function `_keyword_language_decision`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-memory-language-decision-64977296|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-MEMORY-LANGUAGE-DECISION-64977296]]: `backend/app/utils/language.py` contains function `_memory_language_decision`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-extract-memory-language-e7f59268|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-EXTRACT-MEMORY-LANGUAGE-E7F59268]]: `backend/app/utils/language.py` contains function `_extract_memory_language`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-profile-language-decision-fa7ad720|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-PROFILE-LANGUAGE-DECISION-FA7AD720]]: `backend/app/utils/language.py` contains function `_profile_language_decision`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-resolve-continuity-decision-ce846603|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-RESOLVE-CONTINUITY-DECISION-CE846603]]: `backend/app/utils/language.py` contains function `_resolve_continuity_decision`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-resolve-continuity-decision-with-e9834e16|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-RESOLVE-CONTINUITY-DECISION-WITH-E9834E16]]: `backend/app/utils/language.py` contains function `_resolve_continuity_decision_with_reason`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-is-ambiguous-follow-up-d1ffa8e6|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-IS-AMBIGUOUS-FOLLOW-UP-D1FFA8E6]]: `backend/app/utils/language.py` contains function `_is_ambiguous_follow_up`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-normalize-language-code-f9e3af59|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-NORMALIZE-LANGUAGE-CODE-F9E3AF59]]: `backend/app/utils/language.py` contains function `_normalize_language_code`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-build-language-diagnostics-9d0c532b|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-BUILD-LANGUAGE-DIAGNOSTICS-9D0C532B]]: `backend/app/utils/language.py` contains function `_build_language_diagnostics`.
- `parent_of` -> [[pyfunc-backend-app-utils-language-py-decision-payload-b5262ccb|PYFUNC-BACKEND-APP-UTILS-LANGUAGE-PY-DECISION-PAYLOAD-B5262CCB]]: `backend/app/utils/language.py` contains function `_decision_payload`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
