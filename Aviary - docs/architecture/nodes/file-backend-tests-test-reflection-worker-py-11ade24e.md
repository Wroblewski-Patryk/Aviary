---
id: "FILE-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-11ADE24E"
name: "test_reflection_worker.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_reflection_worker.py"
related_files: []
tags: ["auto", "test"]
---

# test_reflection_worker.py

ID: `FILE-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-11ADE24E`

## Summary

Repository file `backend/tests/test_reflection_worker.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-tests-test-reflection-worker-py-fakememoryrepository-e1ef7a30|PYCLASS-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-FAKEMEMORYREPOSITORY-E1EF7A30]]: `backend/tests/test_reflection_worker.py` contains class `FakeMemoryRepository`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-960af4d3|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-960AF4D3]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_consolidates_explicit_preference_update_in_background`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-643c5b17|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-643C5B17]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_reads_structured_episode_payload_before_legacy_summary`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-97a28c14|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-97A28C14]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_consolidates_repeated_memory_topics_into_semantic_summary`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-69cc80d1|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-69CC80D1]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_keeps_unrelated_memory_topic_summaries_in_separate_buckets`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-d036e1f2|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-D036E1F2]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_read_only_subconscious_proposals_from_recent_memory`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-0b6a7915|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-0B6A7915]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_connector_expansion_proposal_from_repeated_unmet_connector_needs`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-df82d1ee|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-DF82D1EE]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_preferred_role_from_repeated_role_usage`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-06d39e5c|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-06D39E5C]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_concise_style_from_repeated_short_successful_outputs`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-70416b8a|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-70416B8A]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_skips_when_recent_memory_has_no_consistent_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-742a886a|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-742A886A]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_updates_theta_from_mixed_recent_roles`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-9b1babc2|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-9B1BABC2]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_guided_collaboration_preference`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-8f62389f|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-8F62389F]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_hands_on_collaboration_preference`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-00aba6f5|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-00ABA6F5]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_prefers_explicit_guided_collaboration_update`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-ff0bd532|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-FF0BD532]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_relation_updates_from_recent_memory`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-4f815852|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-4F815852]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_consolidates_repeated_behavior_feedback_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-0fbcd1c1|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-0FBCD1C1]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_low_trust_relation_when_delivery_quality_drops`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-cece0ccb|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-CECE0CCB]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_medium_trust_relation_at_balanced_delivery_ratio`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-b63f688e|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-B63F688E]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_avoids_adaptive_inference_without_outcome_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-ca765ee7|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-CA765EE7]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_recurring_distress_affective_pattern`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-101f4ba7|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-101F4BA7]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_confidence_recovery_affective_pattern`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-d3ca03a3|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-D3CA03A3]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_blocked_goal_execution_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-b3fd99aa|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-B3FD99AA]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_writes_goal_operational_conclusions_with_goal_scope`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-ea0d054f|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-EA0D054F]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_keeps_global_reflection_outputs_global_even_with_active_goal`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-e105852c|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-E105852C]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_goal_milestone_transition_into_completion_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-0ba1bc7b|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-0BA1BC7B]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_goal_milestone_transition_out_of_completion_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-2430cdf1|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-2430CDF1]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_goal_milestone_recovery_phase`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-b1f29a3d|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-B1F29A3D]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_early_stage_completion_criteria`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-7b01681b|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-7B01681B]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_appends_distinct_goal_milestone_history_snapshots`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-6eb776b1|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-6EB776B1]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_reentered_completion_window_milestone_arc`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-370731d1|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-370731D1]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_lingering_completion_milestone_pressure`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-e06bfde0|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-E06BFDE0]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_prunes_time_only_lingering_completion_pressure_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-946c2004|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-946C2004]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_multi_step_milestone_dependency_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-25d7c41b|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-25D7C41B]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_dependency_due_next_milestone_due_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-b3c49210|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-B3C49210]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_overdue_due_window_from_lingering_completion`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-6a4eb18b|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-6A4EB18B]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_progressing_goal_execution_state_from_done_update`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-d8ee4b07|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-D8EE4B07]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_recovering_goal_execution_state_after_recent_done_with_remaining_work`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-c65b190d|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-C65B190D]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_scopes_goal_conclusions_to_goal_matched_by_recent_turn_hints`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-15b91308|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-15B91308]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_advancing_goal_execution_state_from_in_progress_task`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-50a80a9a|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-50A80A9A]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_goal_progress_score_from_task_mix`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-ba9eb838|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-BA9EB838]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_improving_goal_progress_trend_against_previous_score`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-577665e6|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-577665E6]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_slipping_goal_progress_trend_against_previous_score`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-66316019|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-66316019]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_steady_goal_progress_trend_for_small_change`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-ec8a6861|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-EC8A6861]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_derives_unstable_goal_progress_arc_from_whiplash_history`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-7b649d0d|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-7B649D0D]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_infers_stagnating_goal_execution_state_from_repeated_planning_without_progress`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-6f6df46f|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-6F6DF46F]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_enqueue_persists_durable_task`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-7459e194|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-7459E194]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_enqueue_can_skip_in_process_dispatch`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-d57f2078|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-D57F2078]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_run_pending_once_processes_ready_tasks_without_start_loop`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-2dab61a6|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-2DAB61A6]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_run_pending_once_skips_exhausted_retry_tasks`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-7345e8c0|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-7345E8C0]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_recovers_pending_tasks_on_start`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-696a93ac|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-696A93AC]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_retries_failed_task_after_backoff_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-8cfa1a30|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-8CFA1A30]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_skips_failed_task_before_backoff_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-reflection-worker-py-test-reflection-worker-a68e2596|PYFUNC-BACKEND-TESTS-TEST-REFLECTION-WORKER-PY-TEST-REFLECTION-WORKER-A68E2596]]: `backend/tests/test_reflection_worker.py` contains function `test_reflection_worker_stops_retrying_after_max_attempts`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
