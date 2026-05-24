from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "backend" / "scripts" / "run_coolify_deploy_watchdog.py"

SPEC = importlib.util.spec_from_file_location("run_coolify_deploy_watchdog_script", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_decide_next_action_done_when_parity_true() -> None:
    assert (
        MODULE.decide_next_action(
            parity=True,
            trigger_enabled=True,
            already_triggered=False,
            webhook_ready=True,
        )
        == "done"
    )


def test_decide_next_action_requests_webhook_trigger_once() -> None:
    assert (
        MODULE.decide_next_action(
            parity=False,
            trigger_enabled=True,
            already_triggered=False,
            webhook_ready=True,
        )
        == "trigger_webhook"
    )


def test_decide_next_action_requires_manual_deploy_when_no_webhook() -> None:
    assert (
        MODULE.decide_next_action(
            parity=False,
            trigger_enabled=True,
            already_triggered=False,
            webhook_ready=False,
        )
        == "needs_manual_coolify_deploy"
    )


def test_fetch_health_with_fallback_uses_urllib_when_requests_fails(monkeypatch) -> None:
    class _ReqErr(Exception):
        pass

    def _fail_requests(_base_url: str):
        raise MODULE.requests.RequestException("blocked")

    def _ok_urllib(_base_url: str):
        return {"status": "ok", "deployment": {"runtime_build_revision": "abc"}}

    monkeypatch.setattr(MODULE, "fetch_health_requests", _fail_requests)
    monkeypatch.setattr(MODULE, "fetch_health_urllib", _ok_urllib)

    health, method = MODULE.fetch_health_with_fallback("https://example.com")
    assert method == "urllib"
    assert health["status"] == "ok"
