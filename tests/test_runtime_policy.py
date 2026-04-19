from types import SimpleNamespace

from app.core.runtime_policy import runtime_policy_snapshot


def test_runtime_policy_snapshot_defaults_to_no_production_mismatches_outside_production() -> None:
    settings = SimpleNamespace(
        app_env="development",
        event_debug_enabled=True,
        startup_schema_mode="migrate",
        production_policy_enforcement="warn",
    )

    snapshot = runtime_policy_snapshot(settings)

    assert snapshot == {
        "startup_schema_mode": "migrate",
        "event_debug_enabled": True,
        "event_debug_source": "explicit",
        "production_policy_enforcement": "warn",
        "production_policy_mismatches": [],
    }


def test_runtime_policy_snapshot_includes_all_production_mismatches() -> None:
    settings = SimpleNamespace(
        app_env="production",
        event_debug_enabled=True,
        startup_schema_mode="create_tables",
        production_policy_enforcement="strict",
    )

    snapshot = runtime_policy_snapshot(settings)

    assert snapshot["production_policy_mismatches"] == [
        "event_debug_enabled=true",
        "startup_schema_mode=create_tables",
    ]
    assert snapshot["production_policy_enforcement"] == "strict"


def test_runtime_policy_snapshot_marks_event_debug_source_as_environment_default_when_unset() -> None:
    class _Settings:
        app_env = "production"
        event_debug_enabled = None
        startup_schema_mode = "migrate"
        production_policy_enforcement = "warn"

        @staticmethod
        def is_event_debug_enabled() -> bool:
            return False

    snapshot = runtime_policy_snapshot(_Settings())

    assert snapshot["event_debug_enabled"] is False
    assert snapshot["event_debug_source"] == "environment_default"
    assert snapshot["production_policy_mismatches"] == []
