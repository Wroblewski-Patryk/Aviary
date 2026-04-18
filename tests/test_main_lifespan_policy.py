from fastapi import FastAPI
import pytest

import app.main as app_main


class _StrictDebugMismatchSettings:
    app_env = "production"
    log_level = "INFO"
    event_debug_enabled = True
    startup_schema_mode = "migrate"
    production_policy_enforcement = "strict"

    @staticmethod
    def validate_required() -> None:
        return None

    @staticmethod
    def is_event_debug_enabled() -> bool:
        return True


async def test_lifespan_blocks_startup_before_database_init_when_strict_policy_detects_debug_mismatch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    database_initialized = False

    class _DatabaseGuard:
        def __init__(self, *_args, **_kwargs):
            nonlocal database_initialized
            database_initialized = True
            raise AssertionError("Database initialization should not run when strict policy blocks startup.")

    monkeypatch.setattr(app_main, "get_settings", lambda: _StrictDebugMismatchSettings())
    monkeypatch.setattr(app_main, "Database", _DatabaseGuard)

    with pytest.raises(RuntimeError, match="event_debug_enabled=true"):
        async with app_main.lifespan(FastAPI()):
            pass

    assert database_initialized is False
