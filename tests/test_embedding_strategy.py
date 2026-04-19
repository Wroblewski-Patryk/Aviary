from app.memory.embeddings import embedding_strategy_snapshot, normalize_embedding_source_kinds


def test_embedding_strategy_snapshot_marks_no_warning_when_deterministic_provider_is_ready() -> None:
    snapshot = embedding_strategy_snapshot(
        semantic_vector_enabled=True,
        provider="deterministic",
        model="deterministic-v1",
        dimensions=32,
    )

    assert snapshot["semantic_embedding_provider_ready"] is True
    assert snapshot["semantic_embedding_posture"] == "ready"
    assert snapshot["semantic_embedding_source_coverage_state"] == "full_for_current_retrieval_path"
    assert snapshot["semantic_embedding_source_coverage_hint"] == "semantic_and_affective_sources_enabled"
    assert snapshot["semantic_embedding_warning_state"] == "no_warning"
    assert snapshot["semantic_embedding_warning_hint"] == "embedding_strategy_ready"


def test_embedding_strategy_snapshot_marks_vectors_disabled_warning_state() -> None:
    snapshot = embedding_strategy_snapshot(
        semantic_vector_enabled=False,
        provider="deterministic",
        model="deterministic-v1",
        dimensions=16,
    )

    assert snapshot["semantic_retrieval_mode"] == "lexical_only"
    assert snapshot["semantic_embedding_source_coverage_state"] == "vectors_disabled"
    assert snapshot["semantic_embedding_source_coverage_hint"] == "not_applicable_vectors_disabled"
    assert snapshot["semantic_embedding_warning_state"] == "vectors_disabled"
    assert (
        snapshot["semantic_embedding_warning_hint"]
        == "enable_semantic_vectors_to_activate_embedding_strategy"
    )


def test_embedding_strategy_snapshot_marks_provider_fallback_warning_state() -> None:
    snapshot = embedding_strategy_snapshot(
        semantic_vector_enabled=True,
        provider="openai",
        model="text-embedding-3-small",
        dimensions=1536,
    )

    assert snapshot["semantic_embedding_provider_ready"] is False
    assert snapshot["semantic_embedding_posture"] == "fallback_deterministic"
    assert snapshot["semantic_embedding_provider_effective"] == "deterministic"
    assert snapshot["semantic_embedding_model_effective"] == "deterministic-v1"
    assert snapshot["semantic_embedding_warning_state"] == "provider_fallback_active"
    assert (
        snapshot["semantic_embedding_warning_hint"]
        == "provider_not_implemented_using_deterministic_fallback"
    )


def test_embedding_strategy_snapshot_marks_missing_source_coverage_when_semantic_and_affective_are_disabled() -> None:
    snapshot = embedding_strategy_snapshot(
        semantic_vector_enabled=True,
        provider="deterministic",
        model="deterministic-v1",
        dimensions=32,
        source_kinds=("episodic", "relation"),
    )

    assert snapshot["semantic_embedding_source_kinds"] == ["episodic", "relation"]
    assert snapshot["semantic_embedding_source_coverage_state"] == "missing_for_current_retrieval_path"
    assert (
        snapshot["semantic_embedding_source_coverage_hint"]
        == "enable_semantic_or_affective_source_for_vector_hits"
    )


def test_normalize_embedding_source_kinds_returns_defaults_when_missing() -> None:
    assert normalize_embedding_source_kinds(None) == ("episodic", "semantic", "affective")
    assert normalize_embedding_source_kinds("") == ("episodic", "semantic", "affective")


def test_normalize_embedding_source_kinds_normalizes_order_and_uniqueness() -> None:
    assert normalize_embedding_source_kinds("relation,episodic,episodic") == ("episodic", "relation")
