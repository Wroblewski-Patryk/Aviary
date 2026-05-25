---
id: "FILE-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-A85ACAEC"
name: "test_memory_repository.py"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "test_coverage"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "test_evidence"
file_path: "backend/tests/test_memory_repository.py"
related_files: []
tags: ["auto", "test"]
---

# test_memory_repository.py

ID: `FILE-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-A85ACAEC`

## Summary

Repository file `backend/tests/test_memory_repository.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-tests-test-memory-repository-py-fakeopenaiembeddingclie-50f743c9|PYCLASS-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-FAKEOPENAIEMBEDDINGCLIE-50F743C9]]: `backend/tests/test_memory_repository.py` contains class `FakeOpenAIEmbeddingClient`.
- `parent_of` -> [[pyclass-backend-tests-test-memory-repository-py-boolhostilevector-7e056b25|PYCLASS-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-BOOLHOSTILEVECTOR-7E056B25]]: `backend/tests/test_memory_repository.py` contains class `BoolHostileVector`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-5340f552|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-5340F552]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_serializes_pgvector_array_without_truthiness_check`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-599ba855|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-599BA855]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_persists_structured_episode_payload`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-5378c949|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-5378C949]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_loads_episode_by_user_and_event_id`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-4ef0122f|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-4EF0122F]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_memory_layer_vocabulary_and_conclusion_mapping`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-2d44ff9b|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-2D44FF9B]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_keeps_topic_scoped_memory_summaries_visible_with_goal_scope`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-ab4a9ae6|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-AB4A9AE6]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_persists_attention_turn_contract_store_and_cleans_up_answered_rows`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-3ff1323f|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-3FF1323F]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_resolves_user_profile_by_linked_telegram_identity`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-87c58c32|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-87C58C32]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_reassigns_telegram_link_ownership_to_latest_user`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-65ccc457|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-65CCC457]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_merges_legacy_telegram_state_into_linked_auth_user`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-8ff9409c|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-8FF9409C]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_persists_scheduler_cadence_evidence_contract_store`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-4383e2d8|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-4383E2D8]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_persists_passive_active_scheduler_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-3602b81b|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-3602B81B]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upserts_and_queries_semantic_embeddings`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-56b1fec5|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-56B1FEC5]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_similarity_fallback_scores_beyond_small_recent_candidate_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-71b02307|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-71B02307]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_formats_postgres_vector_literal_for_native_ranking`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-3f1bf07d|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-3F1BF07D]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_conclusion_materializes_affective_embedding_on_write`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-b57f5662|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-B57F5662]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_conclusion_materializes_semantic_embedding_on_write`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-11f694b2|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-11F694B2]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_conclusion_uses_effective_embedding_posture_when_provider_is_not_implemented`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-aece2ae8|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-AECE2AE8]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_conclusion_keeps_semantic_embedding_pending_in_manual_refresh_mode`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-50040345|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-50040345]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_materializes_local_hybrid_embedding_provider_when_selected`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-cf6ec406|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-CF6EC406]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_materializes_openai_embedding_provider_when_selected_and_configured`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-f761deeb|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-F761DEEB]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_builds_query_embedding_with_configured_openai_provider`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-43e60239|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-43E60239]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_conclusion_keeps_affective_embedding_pending_in_manual_refresh_mode`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-fb8940b6|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-FB8940B6]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_conclusion_skips_embedding_shell_when_source_kind_is_disabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-8e3b98db|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-8E3B98DB]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_builds_hybrid_memory_bundle_with_vector_and_lexical_diagnostics`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-64d61582|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-64D61582]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_includes_vector_matched_episodic_memory_outside_recent_window`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-d8988c65|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-D8988C65]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_keeps_relation_embeddings_out_of_default_foreground_retrieval_baseline`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-c99ab32e|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-C99AB32E]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_includes_vector_matched_relation_when_relation_source_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-b76c9821|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-B76C9821]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upserts_and_reads_scoped_relations`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-ad1b3c2f|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-AD1B3C2F]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_relation_materializes_embedding_when_relation_source_is_enabled`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-7f8693a2|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-7F8693A2]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upsert_relation_keeps_embedding_pending_in_manual_refresh_mode`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-449f5235|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-449F5235]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_refreshes_relation_with_repeated_quality_evidence`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-8b967deb|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-8B967DEB]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_resets_relation_lifecycle_when_relation_value_changes`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-a8328bd9|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-A8328BD9]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_revalidates_relation_confidence_and_expires_stale_rows`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-2d3c9f78|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-2D3C9F78]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_persists_and_resolves_subconscious_proposals`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-630662da|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-630662DA]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_reenters_deferred_subconscious_proposals_in_pending_query`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-7c5dacd1|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-7C5DACD1]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_can_read_conclusions_by_memory_layer`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-7bb16701|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-7BB16701]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_reports_reflection_task_stats`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-58fb64b5|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-58FB64B5]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upserts_and_loads_active_goals_and_tasks`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-5a6cd178|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-5A6CD178]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_updates_task_status_and_removes_done_from_active_list`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-30507775|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-30507775]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_syncs_and_loads_active_goal_milestones`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-a8612ee4|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-A8612EE4]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_appends_and_reads_goal_milestone_history`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-6e2c9939|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-6E2C9939]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_execution_state_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-daad6e01|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-DAAD6E01]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_affective_reflection_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-e9306886|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-E9306886]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_allows_dynamic_goal_execution_state_transition`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-46662cfe|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-46662CFE]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_supports_scoped_goal_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-c156a507|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-C156A507]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_get_user_conclusions_can_filter_by_scope`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-18470193|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-18470193]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_canonicalizes_global_reflection_conclusions_to_global_scope`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-d56a6eb5|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-D56A6EB5]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_progress_score_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-26488277|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-26488277]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_proactive_opt_in_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-53ddf680|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-53DDF680]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_progress_trend_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-39922b32|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-39922B32]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_transition_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-37158d56|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-37158D56]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_allows_dynamic_goal_milestone_transition_updates`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-a31b7504|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-A31B7504]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_state_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-dc970df4|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-DC970DF4]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_risk_and_completion_criteria_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-e8af6884|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-E8AF6884]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_arc_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-17864798|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-17864798]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_pressure_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-f1ea4d0e|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-F1EA4D0E]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_dependency_state_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-a33ff4b8|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-A33FF4B8]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_due_state_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-24ec8674|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-24EC8674]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_milestone_due_window_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-8a209ee8|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-8A209EE8]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_exposes_goal_progress_arc_in_runtime_preferences`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-3b09fa7b|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-3B09FA7B]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_runtime_preferences_can_hold_more_than_six_kinds`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-b945b51f|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-B945B51F]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_appends_and_reads_goal_progress_history`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-3d90e686|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-3D90E686]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_can_persist_ui_language_separately_from_preferred_language`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-17464568|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-17464568]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_upserts_and_updates_planned_work_items`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-98259412|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-98259412]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_returns_due_planned_work_and_marks_it_due`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-15e01109|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-15E01109]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_snoozes_and_advances_recurring_planned_work`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-186f6698|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-186F6698]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_resets_single_user_runtime_data_and_preserves_managed_settings`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-7999a090|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-7999A090]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_projects_recent_chat_transcript_in_chronological_order`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-0d830ccb|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-0D830CCB]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_hides_scheduler_internal_prompt_but_keeps_delivered_scheduler_reply`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-329aaead|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-329AAEAD]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_ignores_internal_rows_when_counting_unanswered_proactive_and_recent_activity`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-71053e48|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-71053E48]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_blocks_scheduler_candidate_when_contact_cadence_is_on_demand`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-82059d64|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-82059D64]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_backfills_communication_boundary_relations_from_existing_episodes`.
- `parent_of` -> [[pyfunc-backend-tests-test-memory-repository-py-test-memory-repository-197a6e75|PYFUNC-BACKEND-TESTS-TEST-MEMORY-REPOSITORY-PY-TEST-MEMORY-REPOSITORY-197A6E75]]: `backend/tests/test_memory_repository.py` contains function `test_memory_repository_cleans_runtime_data_for_all_users_while_preserving_auth_and_profiles`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
