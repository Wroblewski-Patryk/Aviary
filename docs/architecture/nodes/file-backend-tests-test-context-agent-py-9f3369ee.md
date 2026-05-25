---
id: "FILE-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-9F3369EE"
name: "test_context_agent.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_context_agent.py"
related_files: []
tags: ["auto", "test"]
---

# test_context_agent.py

ID: `FILE-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-9F3369EE`

## Summary

Repository file `backend/tests/test_context_agent.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-event-503e6726|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-EVENT-503E6726]]: `backend/tests/test_context_agent.py` contains function `_event`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-perception-fde0e070|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-PERCEPTION-FDE0E070]]: `backend/tests/test_context_agent.py` contains function `_perception`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-identity-4564bb67|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-IDENTITY-4564BB67]]: `backend/tests/test_context_agent.py` contains function `_identity`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-stays-db9763da|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-STAYS-DB9763DA]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_stays_simple_without_recent_memory`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-26ad55f6|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-26AD55F6]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_stable_user_preferences_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-3015a01b|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-3015A01B]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_long_term_memory_topic_summary_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-b79111b6|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-B79111B6]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_affective_support_pattern_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-99d68c38|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-99D68C38]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_relation_cues_when_confident_relations_exist`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-can-in-3744bc1e|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-CAN-IN-3744BC1E]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_can_include_identity_stance`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-a3569d09|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-A3569D09]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_foreground_awareness_name_memory_and_tools`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-01b24770|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-01B24770]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_recent_turn_gap_when_memory_has_timestamp`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-5159dc9d|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-5159DC9D]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_relevant_active_goals_and_tasks`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-prefers-affect-c1c56d73|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-PREFERS-AFFECT-C1C56D73]]: `backend/tests/test_context_agent.py` contains function `test_context_prefers_affective_relevant_memory_order_when_support_is_needed`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-088da4a9|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-088DA4A9]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_active_goal_milestones`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-format-ec0481fe|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-FORMAT-EC0481FE]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_formats_active_goal_milestone_with_risk_and_criteria`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-format-5089bc9e|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-FORMAT-5089BC9E]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_formats_active_goal_milestone_with_arc`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-format-b42e6e81|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-FORMAT-B42E6E81]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_formats_active_goal_milestone_with_pressure`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-format-39ff4ff7|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-FORMAT-39FF4FF7]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_formats_active_goal_milestone_with_dependency_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-format-d78539ac|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-FORMAT-D78539AC]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_formats_active_goal_milestone_with_due_state`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-format-3a845cc9|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-FORMAT-3A845CC9]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_formats_active_goal_milestone_with_due_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-c7724866|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-C7724866]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_collaboration_preference_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-ff154212|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-FF154212]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_execution_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-f7e00543|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-F7E00543]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_stagnating_goal_execution_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-c217c376|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-C217C376]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_recovering_goal_execution_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-96deda2f|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-96DEDA2F]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_advancing_goal_execution_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-12a357cd|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-12A357CD]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_progress_score_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-7ddf7c6f|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-7DDF7C6F]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_progress_trend_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-ebc093df|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-EBC093DF]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_progress_arc_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-baf3ce30|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-BAF3CE30]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_transition_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-5b24bf44|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-5B24BF44]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-78b110d8|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-78B110D8]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_arc_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-762722b6|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-762722B6]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_pressure_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-56af9fe8|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-56AF9FE8]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_dependency_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-f5fb7d3a|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-F5FB7D3A]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_due_state_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-97729129|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-97729129]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_due_window_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-30355242|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-30355242]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_goal_milestone_risk_and_completion_criteria_from_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-27587118|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-27587118]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_recent_goal_progress_history`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-4dba62c1|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-4DBA62C1]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_recent_goal_milestone_history`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-ignores-low-co-60e1d82a|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-IGNORES-LOW-CO-60E1D82A]]: `backend/tests/test_context_agent.py` contains function `test_context_ignores_low_confidence_conclusions`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-related-tags-a-df340b66|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-RELATED-TAGS-A-DF340B66]]: `backend/tests/test_context_agent.py` contains function `test_context_related_tags_are_deduplicated_preserving_order`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-includ-7d5656d4|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-INCLUD-7D5656D4]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_includes_recent_memory_signal`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-keeps-dc0a8c75|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-KEEPS-DC0A8C75]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_keeps_vector_retrieved_memory_without_lexical_overlap`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-clip-text-prefers-comp-bbb5d9f2|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CLIP-TEXT-PREFERS-COMP-BBB5D9F2]]: `backend/tests/test_context_agent.py` contains function `test_clip_text_prefers_completed_sentence_when_it_fits`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-clip-text-falls-back-t-0fa9310d|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CLIP-TEXT-FALLS-BACK-T-0FA9310D]]: `backend/tests/test_context_agent.py` contains function `test_clip_text_falls_back_to_word_boundary_with_ellipsis`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-summary-clips-ebe16ed6|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SUMMARY-CLIPS-EBE16ED6]]: `backend/tests/test_context_agent.py` contains function `test_context_summary_clips_long_memory_cleanly`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-prefers-same-l-7467bdac|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-PREFERS-SAME-L-7467BDAC]]: `backend/tests/test_context_agent.py` contains function `test_context_prefers_same_language_memory_over_mismatched_recent_entries`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-falls-back-to-a50d76c5|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-FALLS-BACK-TO-A50D76C5]]: `backend/tests/test_context_agent.py` contains function `test_context_falls_back_to_unknown_language_memory_when_no_match_exists`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-deduplicates-s-85a19959|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-DEDUPLICATES-S-85A19959]]: `backend/tests/test_context_agent.py` contains function `test_context_deduplicates_same_memory_summary`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-deduplicates-n-b9ebd9be|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-DEDUPLICATES-N-B9EBD9BE]]: `backend/tests/test_context_agent.py` contains function `test_context_deduplicates_near_duplicate_event_memory`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-prefers-more-t-2b9bc9ac|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-PREFERS-MORE-T-2B9BC9AC]]: `backend/tests/test_context_agent.py` contains function `test_context_prefers_more_topically_relevant_memory_over_higher_importance`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-uses-importanc-d63e87ce|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-USES-IMPORTANC-D63E87CE]]: `backend/tests/test_context_agent.py` contains function `test_context_uses_importance_when_relevance_is_tied`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-skips-irreleva-4e24fd88|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-SKIPS-IRRELEVA-4E24FD88]]: `backend/tests/test_context_agent.py` contains function `test_context_skips_irrelevant_memory_for_specific_request`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-keeps-memory-f-29416332|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-KEEPS-MEMORY-F-29416332]]: `backend/tests/test_context_agent.py` contains function `test_context_keeps_memory_for_ambiguous_short_follow_up`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-uses-perceptio-9c2fab3d|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-USES-PERCEPTIO-9C2FAB3D]]: `backend/tests/test_context_agent.py` contains function `test_context_uses_perception_topic_tags_for_memory_matching`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-prefers-semant-c57b30dc|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-PREFERS-SEMANT-C57B30DC]]: `backend/tests/test_context_agent.py` contains function `test_context_prefers_semantic_memory_for_specific_request_over_continuity`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-prefers-contin-4832c451|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-PREFERS-CONTIN-4832C451]]: `backend/tests/test_context_agent.py` contains function `test_context_prefers_continuity_memory_for_short_follow_up`.
- `parent_of` -> [[pyfunc-backend-tests-test-context-agent-py-test-context-reads-structur-8a0b7077|PYFUNC-BACKEND-TESTS-TEST-CONTEXT-AGENT-PY-TEST-CONTEXT-READS-STRUCTUR-8A0B7077]]: `backend/tests/test_context_agent.py` contains function `test_context_reads_structured_memory_payload_before_legacy_summary`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
