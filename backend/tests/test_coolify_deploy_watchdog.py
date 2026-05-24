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

