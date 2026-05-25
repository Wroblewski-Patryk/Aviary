---
id: "FILE-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-1498FF5F"
name: "test_adaptive_policy.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_adaptive_policy.py"
related_files: []
tags: ["auto", "test"]
---

# test_adaptive_policy.py

ID: `FILE-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-1498FF5F`

## Summary

Repository file `backend/tests/test_adaptive_policy.py` auto-discovered for architecture graph inventory.

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
- `verifies` -> [[file-backend-app-core-adaptive-policy-py-e59cf6d6|FILE-BACKEND-APP-CORE-ADAPTIVE-POLICY-PY-E59CF6D6]]: Test file `backend/tests/test_adaptive_policy.py` appears to verify `FILE-BACKEND-APP-CORE-ADAPTIVE-POLICY-PY-E59CF6D6`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-relation-value-respe-86103ef4|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-RELATION-VALUE-RESPE-86103EF4]]: `backend/tests/test_adaptive_policy.py` contains function `test_relation_value_respects_default_and_override_confidence_thresholds`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-preferred-role-allow-22526aaf|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-PREFERRED-ROLE-ALLOW-22526AAF]]: `backend/tests/test_adaptive_policy.py` contains function `test_preferred_role_allowed_requires_supported_role_and_documented_confidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-dominant-theta-chann-0ccdbdd9|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-DOMINANT-THETA-CHANN-0CCDBDD9]]: `backend/tests/test_adaptive_policy.py` contains function `test_dominant_theta_channel_uses_documented_threshold`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-role-adaptive-tie-br-c8b03f7d|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-ROLE-ADAPTIVE-TIE-BR-C8B03F7D]]: `backend/tests/test_adaptive_policy.py` contains function `test_role_adaptive_tie_break_turn_matches_documented_ambiguous_posture`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-motivation-adaptive-8447138c|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-MOTIVATION-ADAPTIVE-8447138C]]: `backend/tests/test_adaptive_policy.py` contains function `test_motivation_adaptive_tie_break_requires_ambiguous_turn_and_no_stronger_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-proactive-relevance-9384da25|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-PROACTIVE-RELEVANCE-9384DA25]]: `backend/tests/test_adaptive_policy.py` contains function `test_proactive_relevance_adjustment_uses_relation_and_theta_policy_context`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-proactive-relevance-bd9cfbf5|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-PROACTIVE-RELEVANCE-BD9CFBF5]]: `backend/tests/test_adaptive_policy.py` contains function `test_proactive_relevance_adjustment_can_reduce_low_trust_outreach_relevance`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-proactive-interrupti-42e16a46|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-PROACTIVE-INTERRUPTI-42E16A46]]: `backend/tests/test_adaptive_policy.py` contains function `test_proactive_interruption_adjustment_is_higher_for_low_trust_than_high_trust`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-proactive-attention-0945499e|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-PROACTIVE-ATTENTION-0945499E]]: `backend/tests/test_adaptive_policy.py` contains function `test_proactive_attention_limits_only_tighten_guardrails`.
- `parent_of` -> [[pyfunc-backend-tests-test-adaptive-policy-py-test-proactive-attention-f613424b|PYFUNC-BACKEND-TESTS-TEST-ADAPTIVE-POLICY-PY-TEST-PROACTIVE-ATTENTION-F613424B]]: `backend/tests/test_adaptive_policy.py` contains function `test_proactive_attention_limits_are_strictest_for_low_trust_delivery`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
