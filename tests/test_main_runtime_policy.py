import logging
from types import SimpleNamespace

from app.main import _log_runtime_policy_warnings


def test_startup_logs_warning_when_production_runs_with_debug_payload_enabled(caplog) -> None:
    logger_name = "aion.app"
    caplog.set_level("WARNING", logger=logger_name)
    logger = logging.getLogger(logger_name)
    settings = SimpleNamespace(
        app_env="production",
        event_debug_enabled=True,
        startup_schema_mode="migrate",
    )

    _log_runtime_policy_warnings(settings=settings, logger=logger)

    messages = [record.getMessage() for record in caplog.records if record.name == logger_name]
    assert any("runtime_policy_warning" in message for message in messages)
    assert any("disable_debug_payload_in_production" in message for message in messages)
    assert any("source=explicit" in message for message in messages)


def test_startup_skips_warning_when_debug_payload_is_disabled(caplog) -> None:
    logger_name = "aion.app"
    caplog.set_level("WARNING", logger=logger_name)
    logger = logging.getLogger(logger_name)
    settings = SimpleNamespace(
        app_env="production",
        event_debug_enabled=False,
        startup_schema_mode="migrate",
    )

    _log_runtime_policy_warnings(settings=settings, logger=logger)

    messages = [record.getMessage() for record in caplog.records if record.name == logger_name]
    assert not any("runtime_policy_warning" in message for message in messages)


def test_startup_skips_debug_warning_when_production_uses_environment_default_disable(caplog) -> None:
    logger_name = "aion.app"
    caplog.set_level("WARNING", logger=logger_name)
    logger = logging.getLogger(logger_name)

    class _Settings:
        app_env = "production"
        event_debug_enabled = None
        startup_schema_mode = "migrate"

        @staticmethod
        def is_event_debug_enabled() -> bool:
            return False

    _log_runtime_policy_warnings(settings=_Settings(), logger=logger)

    messages = [record.getMessage() for record in caplog.records if record.name == logger_name]
    assert not any("disable_debug_payload_in_production" in message for message in messages)


def test_startup_logs_warning_when_production_runs_with_schema_compatibility_mode(caplog) -> None:
    logger_name = "aion.app"
    caplog.set_level("WARNING", logger=logger_name)
    logger = logging.getLogger(logger_name)
    settings = SimpleNamespace(
        app_env="production",
        event_debug_enabled=False,
        startup_schema_mode="create_tables",
    )

    _log_runtime_policy_warnings(settings=settings, logger=logger)

    messages = [record.getMessage() for record in caplog.records if record.name == logger_name]
    assert any("runtime_policy_warning" in message for message in messages)
    assert any("use_migration_first_startup_in_production" in message for message in messages)


def test_startup_skips_schema_compatibility_warning_outside_production(caplog) -> None:
    logger_name = "aion.app"
    caplog.set_level("WARNING", logger=logger_name)
    logger = logging.getLogger(logger_name)
    settings = SimpleNamespace(
        app_env="development",
        event_debug_enabled=False,
        startup_schema_mode="create_tables",
    )

    _log_runtime_policy_warnings(settings=settings, logger=logger)

    messages = [record.getMessage() for record in caplog.records if record.name == logger_name]
    assert not any("use_migration_first_startup_in_production" in message for message in messages)
