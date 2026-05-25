---
id: "FILE-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-95244421"
name: "test_planning_agent.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_planning_agent.py"
related_files: []
tags: ["auto", "test"]
---

# test_planning_agent.py

ID: `FILE-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-95244421`

## Summary

Repository file `backend/tests/test_planning_agent.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-event-d9d9a171|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-EVENT-D9D9A171]]: `backend/tests/test_planning_agent.py` contains function `_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-scheduler-event-b432fb81|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-SCHEDULER-EVENT-B432FB81]]: `backend/tests/test_planning_agent.py` contains function `_scheduler_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-context-cc065591|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-CONTEXT-CC065591]]: `backend/tests/test_planning_agent.py` contains function `_context`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-builds-d8f59565|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-BUILDS-D8F59565]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_builds_support_plan`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-keeps-0e89af67|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-KEEPS-0E89AF67]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_keeps_supportive_steps_inside_documented_contract`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-carrie-07d959c6|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-CARRIE-07D959C6]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_carries_work_partner_skills_and_tool_intents`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-infers-3f386ee0|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-INFERS-3F386EE0]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_infers_weather_lookup_without_explicit_search_marker`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-infers-f8a05451|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-INFERS-F8A05451]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_infers_page_read_for_bare_domain_without_read_page_marker`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-f4c7dfb6|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-F4C7DFB6]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_goal_upsert_domain_intent`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-5a1eef3c|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-5A1EEF3C]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_goal_and_task_upsert_intents_for_inline_command_phrasing`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-1f33a720|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-1F33A720]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_task_status_domain_intent`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-infers-03288b80|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-INFERS-03288B80]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_infers_task_from_repeated_blocker_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-infers-cf10f8c2|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-INFERS-CF10F8C2]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_infers_goal_and_task_when_repeated_evidence_has_no_active_goal`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-blocks-790faf21|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-BLOCKS-790FAF21]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_blocks_inferred_promotion_on_low_trust_with_borderline_importance`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-allows-2c141953|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ALLOWS-2C141953]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_allows_inferred_promotion_on_high_trust_with_lower_importance`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-requir-c4eb3901|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-REQUIR-C4EB3901]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_requires_explicit_repeated_signal_under_low_trust_even_with_memory_hint`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-allows-161a1b0f|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ALLOWS-161A1B0F]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_allows_memory_hint_repetition_gate_for_medium_trust`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-30701dd9|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-30701DD9]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_maintenance_task_status_intent_when_repeated_blocker_matches_existing_task`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-does-n-7648517e|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-DOES-N-7648517E]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_does_not_infer_promotion_without_repeated_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-does-n-ed4a8723|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-DOES-N-ED4A8723]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_does_not_infer_promotion_when_repeated_signal_is_weak`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-avoids-963879d4|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-AVOIDS-963879D4]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_avoids_duplicate_inferred_promotions_for_matching_active_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-af3158f2|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-AF3158F2]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_preference_domain_intents_from_explicit_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-05b376bd|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-05B376BD]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_reminder_task_and_proactive_preference_from_explicit_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-07c8baea|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-07C8BAEA]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_recurring_routine_planned_work_from_daily_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-813299af|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-813299AF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_custom_recurring_planned_work_rule_from_interval_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-9c287234|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-9C287234]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_planned_work_reschedule_cancel_and_complete_intents`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-6c3a3123|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-6C3A3123]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_daily_planning_task_from_explicit_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-emits-56d563e0|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-EMITS-56D563E0]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_emits_noop_domain_intent_when_no_domain_change_detected`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-accept-df74a878|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ACCEPT-DF74A878]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_accepts_single_subconscious_clarifier_and_merges_secondary_nudge`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-accept-e2017921|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ACCEPT-E2017921]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_accepts_read_only_research_proposal_when_user_explicitly_requests_research`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-builds-4b27f59e|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-BUILDS-4B27F59E]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_builds_connector_permission_gates_for_calendar_and_task_connectors`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-builds-bd4c4502|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-BUILDS-BD4C4502]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_builds_connected_drive_intent_and_permission_gate`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-builds-a1cc44ef|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-BUILDS-A1CC44EF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_builds_allowed_connector_permission_gates_for_read_and_suggestion_posture`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-select-00ce72b9|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-SELECT-00CE72B9]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_selects_google_drive_for_bounded_list_files_baseline`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-promot-1cca4214|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-PROMOT-1CCA4214]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_promotes_connector_expansion_proposal_into_discovery_intent`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-skips-533ce9c6|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-SKIPS-533CE9C6]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_skips_non_retriable_subconscious_proposal_statuses`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-c-8579bcc6|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-C-8579BCC6]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_concise_step_from_semantic_preference`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-s-2ebb1e04|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-S-2EBB1E04]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_structured_step_from_semantic_preference`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-t-2668de69|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-T-2668DE69]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_telegram_delivery_step_when_needed`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-t-a7913fdf|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-T-A7913FDF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_theta_reasoning_step_for_generic_turn`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-ignore-c095c602|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-IGNORE-C095C602]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_ignores_subthreshold_theta_for_generic_turn`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-uses-g-2d09b560|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-USES-G-2D09B560]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_uses_guided_collaboration_preference_for_generic_turn`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-uses-h-1db66789|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-USES-H-1DB66789]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_uses_hands_on_collaboration_preference_for_generic_turn`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-uses-r-21c2bcaf|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-USES-R-21C2BCAF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_uses_relation_signals_for_collaboration_and_support_steps`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-ignore-e065bf30|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-IGNORE-E065BF30]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_ignores_subthreshold_relation_signals_for_collaboration_and_support_steps`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-calibr-5b908db4|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-CALIBR-5B908DB4]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_calibrates_planning_confidence_from_delivery_reliability`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-aligns-c848e603|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ALIGNS-C848E603]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_aligns_with_active_goal_and_blocked_task`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-target-45f6a484|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-TARGET-45F6A484]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_targets_matching_goal_when_multiple_goals_are_active`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-aligns-dd5961bf|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ALIGNS-DD5961BF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_aligns_with_active_milestone`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-uses-a-d712cbe7|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-USES-A-D712CBE7]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_uses_active_milestone_risk_and_completion_criteria`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-r-43b077bf|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-R-43B077BF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_recover_goal_progress_step_from_reflected_blocked_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-c-246e68d1|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-C-246E68D1]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_completion_window_step_from_goal_milestone_transition`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-g-5d639ca9|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-G-5D639CA9]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_goal_closure_step_from_milestone_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-r-de3b45ab|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-R-DE3B45AB]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_reduce_milestone_risk_step`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-c-8b300bef|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-C-8B300BEF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_confirm_goal_completion_step`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-m-d9113237|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-M-D9113237]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_milestone_arc_step_for_closure_momentum`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-m-6b18df17|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-M-6B18DF17]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_milestone_arc_step_for_reentered_completion_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-m-be29a7a1|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-M-BE29A7A1]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_milestone_pressure_step_for_lingering_completion`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-m-6d4ecb52|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-M-6D4ECB52]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_milestone_dependency_step_for_blocked_dependency`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-m-dbed440a|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-M-DBED440A]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_milestone_due_step_for_dependency_due_next`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-m-a6142f22|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-M-A6142F22]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_milestone_due_window_step_for_overdue_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-p-c176fba1|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-P-C176FBA1]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_preserve_goal_momentum_step_from_reflected_progress_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-r-86640a07|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-R-86640A07]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_restart_goal_progress_step_from_stagnating_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-s-b692aa86|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-S-B692AA86]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_stabilize_goal_recovery_step_from_recovering_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-c-9ac50716|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-C-9AC50716]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_continue_goal_execution_step_from_advancing_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-i-1e84e53c|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-I-1E84E53C]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_increase_goal_progress_step_for_early_progress_score`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-p-db3ad1a3|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-P-DB3AD1A3]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_push_goal_to_completion_step_for_high_progress_score`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-c-bd6a1011|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-C-BD6A1011]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_correct_goal_drift_step_for_slipping_progress_trend`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-p-63eebf4c|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-P-63EEBF4C]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_protect_goal_trajectory_step_for_lift_history`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-adds-c-fbc9d84a|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ADDS-C-FBC9D84A]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_adds_consolidate_goal_recovery_step_for_progress_arc`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-builds-123707ff|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-BUILDS-123707FF]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_builds_proactive_warning_plan_when_interrupt_is_allowed`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-persis-3a24f936|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-PERSIS-3A24F936]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_persists_communication_boundary_directives_as_relations`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-persis-67dc6e18|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-PERSIS-67DC6E18]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_persists_observed_repeated_greeting_feedback_as_relation`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-persis-cba59d60|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-PERSIS-CBA59D60]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_persists_loose_feedback_as_boundary_relations`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-routes-5a793de1|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ROUTES-5A793DE1]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_routes_structured_behavior_feedback_as_relation_intent`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-keeps-b647f068|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-KEEPS-B647F068]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_keeps_low_confidence_behavior_feedback_descriptive`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-does-n-7801e63e|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-DOES-N-7801E63E]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_does_not_persist_unclear_behavior_feedback_as_relation`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-defers-54ae86f9|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-DEFERS-54AE86F9]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_defers_proactive_outreach_when_contact_cadence_is_on_demand`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-calibr-e1d9c49f|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-CALIBR-E1D9C49F]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_calibrates_proactive_outreach_tone_for_low_trust_relation`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-defers-da912c0c|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-DEFERS-DA912C0C]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_defers_proactive_outreach_when_interruption_cost_is_high`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-keeps-c10d7dd4|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-KEEPS-C10D7DD4]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_keeps_plain_time_checkin_silent_without_active_work_or_strong_relation_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-defers-5a755cd6|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-DEFERS-5A755CD6]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_defers_proactive_outreach_when_opt_in_is_missing`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-respec-e8ddefd5|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-RESPEC-E8DDEFD5]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_respects_attention_gate_before_other_proactive_delivery_logic`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-keeps-1cee7ec0|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-KEEPS-1CEE7EC0]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_keeps_proactive_path_separate_from_proposal_handoff_and_connector_intents`.
- `parent_of` -> [[pyfunc-backend-tests-test-planning-agent-py-test-planning-agent-accept-4a5f1be2|PYFUNC-BACKEND-TESTS-TEST-PLANNING-AGENT-PY-TEST-PLANNING-AGENT-ACCEPT-4A5F1BE2]]: `backend/tests/test_planning_agent.py` contains function `test_planning_agent_accepts_scheduler_due_planned_work_handoff_for_foreground_delivery`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
