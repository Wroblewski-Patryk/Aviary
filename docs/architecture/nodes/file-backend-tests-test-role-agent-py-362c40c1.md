---
id: "FILE-BACKEND-TESTS-TEST-ROLE-AGENT-PY-362C40C1"
name: "test_role_agent.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_role_agent.py"
related_files: []
tags: ["auto", "test"]
---

# test_role_agent.py

ID: `FILE-BACKEND-TESTS-TEST-ROLE-AGENT-PY-362C40C1`

## Summary

Repository file `backend/tests/test_role_agent.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-event-05938cf1|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-EVENT-05938CF1]]: `backend/tests/test_role_agent.py` contains function `_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-perception-f199f80b|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-PERCEPTION-F199F80B]]: `backend/tests/test_role_agent.py` contains function `_perception`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-context-0dfd951b|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-CONTEXT-0DFD951B]]: `backend/tests/test_role_agent.py` contains function `_context`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-friend-fo-39ec6e95|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-FRIEND-FO-39EC6E95]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_friend_for_affective_support_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-analyst-f-59c83e7f|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-ANALYST-F-59C83E7F]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_analyst_for_planning_topics`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-executor-9f10de18|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-EXECUTOR-9F10DE18]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_executor_for_direct_action_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-selects-work-p-5c40d0c0|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-SELECTS-WORK-P-5C40D0C0]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_selects_work_partner_for_explicit_work_orchestration_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-skill-registry-exposes-to-b0e514c2|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-SKILL-REGISTRY-EXPOSES-TO-B0E514C2]]: `backend/tests/test_role_agent.py` contains function `test_skill_registry_exposes_tool_aware_metadata_without_execution_authority`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-selects-tool-a-6356d244|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-SELECTS-TOOL-A-6356D244]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_selects_tool_aware_skills_as_metadata_only_hints`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-mentor-fo-aa9ec819|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-MENTOR-FO-AA9EC819]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_mentor_for_general_questions`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-handles-polish-fe3e842f|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-HANDLES-POLISH-FE3E842F]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_handles_polish_executor_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-preferred-5a30a25d|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-PREFERRED-5A30A25D]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_preferred_role_as_tie_breaker_for_ambiguous_question`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-active-go-06e42ff6|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-ACTIVE-GO-06E42FF6]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_active_goal_risk_context_for_ambiguous_help_turn`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-raises-analyst-cbde8b3c|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-RAISES-ANALYST-CBDE8B3C]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_raises_analyst_confidence_when_planning_turn_has_active_goal_context`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-does-not-overr-a7d0411a|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-DOES-NOT-OVERR-A7D0411A]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_does_not_override_explicit_executor_signal_with_preference`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-theta-bia-369a5f7d|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-THETA-BIA-369A5F7D]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_theta_bias_when_no_preferred_role_exists`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-keeps-explicit-b589c9ce|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-KEEPS-EXPLICIT-B589C9CE]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_keeps_explicit_emotional_signal_over_theta_bias`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-guided-co-2c6927ac|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-GUIDED-CO-2C6927AC]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_guided_collaboration_preference_for_ambiguous_question`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-hands-on-93949b3f|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-HANDS-ON-93949B3F]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_hands_on_collaboration_preference_before_theta`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-uses-relation-0a45f7ef|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-USES-RELATION-0A45F7EF]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_uses_relation_collaboration_signal_for_ambiguous_question`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-ignores-subthr-4bb0f4ab|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-IGNORES-SUBTHR-4BB0F4AB]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_ignores_subthreshold_relation_collaboration_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-role-agent-py-test-role-agent-ignores-subthr-ad50b29c|PYFUNC-BACKEND-TESTS-TEST-ROLE-AGENT-PY-TEST-ROLE-AGENT-IGNORES-SUBTHR-AD50B29C]]: `backend/tests/test_role_agent.py` contains function `test_role_agent_ignores_subthreshold_theta_bias_for_ambiguous_question`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
