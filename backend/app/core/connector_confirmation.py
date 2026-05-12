from typing import Any

from app.core.contracts import (
    ActionResult,
    CalendarSchedulingIntentDomainIntent,
    ConnectedDriveAccessDomainIntent,
    ConnectorCapabilityDiscoveryDomainIntent,
    Event,
    ExternalTaskSyncDomainIntent,
    PlanOutput,
)


def build_pending_connector_confirmation_payload(
    *,
    event: Event,
    plan: PlanOutput,
    action_result: ActionResult,
) -> dict[str, Any] | None:
    observation = next(
        (
            item
            for item in action_result.observations
            if item.blocker == "confirmation_required"
            and item.next_step_relevance == "needs_confirmation"
            and item.raw_payload_included is False
        ),
        None,
    )
    if observation is None:
        return None

    gate = next(
        (
            item
            for item in plan.connector_permission_gates
            if item.requires_confirmation and item.allowed is False
        ),
        None,
    )
    if gate is None:
        return None

    return {
        "status": "pending_confirmation",
        "source_event_id": event.event_id,
        "trace_id": event.meta.trace_id,
        "connector_kind": gate.connector_kind,
        "provider_hint": gate.provider_hint,
        "operation": gate.operation,
        "mode": gate.mode,
        "candidate_summary": " ".join(str(observation.bounded_summary).split())[:500],
        "source_reference": " ".join(str(observation.source_reference).split())[:200],
        "reason": gate.reason,
    }


def build_connector_confirmation_replay_snapshot(
    *,
    event: Event,
    plan: PlanOutput,
    action_result: ActionResult,
    pending_confirmation: dict[str, Any] | None,
) -> dict[str, Any] | None:
    if not isinstance(pending_confirmation, dict):
        return None

    observation = next(
        (
            item
            for item in action_result.observations
            if item.blocker == "confirmation_required"
            and item.next_step_relevance == "needs_confirmation"
            and item.raw_payload_included is False
        ),
        None,
    )
    if observation is None:
        return None

    connector_kind = str(pending_confirmation.get("connector_kind", "") or "")
    provider_hint = str(pending_confirmation.get("provider_hint", "") or "")
    operation = str(pending_confirmation.get("operation", "") or "")
    mode = str(pending_confirmation.get("mode", "") or "")

    gate = next(
        (
            item
            for item in plan.connector_permission_gates
            if item.connector_kind == connector_kind
            and str(item.provider_hint or "") == provider_hint
            and item.operation == operation
            and item.mode == mode
            and item.requires_confirmation
            and item.allowed is False
        ),
        None,
    )
    if gate is None:
        return None

    intent = next(
        (
            item
            for item in plan.domain_intents
            if _connector_intent_matches_pending(
                intent=item,
                connector_kind=connector_kind,
                provider_hint=provider_hint,
                operation=operation,
                mode=mode,
            )
        ),
        None,
    )
    if intent is None:
        return None

    return {
        "status": "replay_snapshot_ready",
        "source_event_id": event.event_id,
        "trace_id": event.meta.trace_id,
        "replay_owner": "action",
        "execution_allowed": False,
        "intent": intent.model_dump(mode="json"),
        "connector_permission_gate": gate.model_dump(mode="json"),
        "observation": {
            "tool_id": observation.tool_id,
            "operation": observation.operation,
            "provider_path": observation.provider_path,
            "source_reference": " ".join(str(observation.source_reference).split())[:200],
            "bounded_summary": " ".join(str(observation.bounded_summary).split())[:500],
            "confidence": observation.confidence,
            "blocker": observation.blocker,
            "next_step_relevance": observation.next_step_relevance,
            "raw_payload_included": observation.raw_payload_included,
        },
    }


def _connector_intent_matches_pending(
    *,
    intent: object,
    connector_kind: str,
    provider_hint: str,
    operation: str,
    mode: str,
) -> bool:
    if isinstance(intent, CalendarSchedulingIntentDomainIntent):
        return (
            connector_kind == "calendar"
            and str(intent.provider_hint or "") == provider_hint
            and intent.operation == operation
            and intent.mode == mode
        )
    if isinstance(intent, ExternalTaskSyncDomainIntent):
        return (
            connector_kind == "task_system"
            and str(intent.provider_hint or "") == provider_hint
            and intent.operation == operation
            and intent.mode == mode
        )
    if isinstance(intent, ConnectedDriveAccessDomainIntent):
        return (
            connector_kind == "cloud_drive"
            and str(intent.provider_hint or "") == provider_hint
            and intent.operation == operation
            and intent.mode == mode
        )
    if isinstance(intent, ConnectorCapabilityDiscoveryDomainIntent):
        return (
            connector_kind == intent.connector_kind
            and str(intent.provider_hint or "") == provider_hint
            and operation == f"discover_{intent.requested_capability}"
            and intent.mode == mode
        )
    return False
