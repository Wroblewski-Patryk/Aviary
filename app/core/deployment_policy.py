from __future__ import annotations


def deployment_policy_snapshot() -> dict[str, object]:
    return {
        "policy_owner": "deployment_standard_and_release_reliability",
        "deployment_automation_policy_owner": "coolify_repo_deploy_automation",
        "hosting_baseline": "coolify_medium_term_standard",
        "hosting_transition_state": "not_scheduled",
        "canonical_coolify_app": {
            "project_id": "icmgqml9uw3slzch9m9ok23z",
            "environment_id": "qxooi9coxat272krzjx221fv",
            "application_id": "jr1oehwlzl8tcn3h8gh2vvih",
        },
        "deployment_automation_baseline": {
            "primary_trigger_mode": "source_automation",
            "fallback_trigger_modes": [
                "webhook_manual_fallback",
                "ui_manual_fallback",
            ],
            "provenance_evidence_state": "fallback_artifact_supported_primary_history_required",
            "provenance_evidence_hint": "verify_coolify_history_and_attach_fallback_artifact_when_primary_automation_is_not_used",
        },
        "deployment_trigger_slo": {
            "delivery_success_rate_percent": 99.0,
            "manual_redeploy_exception_rate_percent": 5.0,
            "evidence_owner": "coolify_webhook_plus_release_smoke",
        },
        "rollback_posture": "release_smoke_failure_blocks_completion_and_keeps_manual_rollback_available",
    }
