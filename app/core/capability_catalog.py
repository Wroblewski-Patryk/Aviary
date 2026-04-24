from __future__ import annotations

from typing import Any


CAPABILITY_CATALOG_POLICY_OWNER = "backend_capability_catalog_policy"


def capability_catalog_snapshot(
    *,
    api_readiness: dict[str, Any],
    learned_state: dict[str, Any],
    role_skill_policy: dict[str, Any],
    skill_registry: dict[str, Any],
    connectors: dict[str, Any],
    selection_visibility_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    organizer_tool_stack = (
        dict(connectors.get("organizer_tool_stack", {}))
        if isinstance(connectors.get("organizer_tool_stack"), dict)
        else {}
    )
    organizer_activation_snapshot = (
        dict(organizer_tool_stack.get("activation_snapshot", {}))
        if isinstance(organizer_tool_stack.get("activation_snapshot"), dict)
        else {}
    )
    web_knowledge_tools = (
        dict(connectors.get("web_knowledge_tools", {}))
        if isinstance(connectors.get("web_knowledge_tools"), dict)
        else {}
    )
    execution_baseline = (
        dict(connectors.get("execution_baseline", {}))
        if isinstance(connectors.get("execution_baseline"), dict)
        else {}
    )
    selection_summary = dict(selection_visibility_summary or {})

    approved_connector_kinds = organizer_tool_stack.get("approved_connector_kinds", [])
    approved_operations = organizer_tool_stack.get("approved_operations", [])
    ready_operations = organizer_tool_stack.get("ready_operations", [])
    credential_gap_operations = organizer_tool_stack.get("credential_gap_operations", [])
    work_partner_tool_families = role_skill_policy.get("work_partner_tool_families", [])

    return {
        "policy_owner": CAPABILITY_CATALOG_POLICY_OWNER,
        "catalog_posture": "aggregated_backend_truth_surface",
        "aggregation_boundary": "composed_from_existing_health_and_internal_inspection_surfaces",
        "execution_authority": "unchanged_action_boundary",
        "authorization_authority": "unchanged_connector_permission_gates",
        "future_ui_posture": "consume_catalog_without_reconstructing_backend_truth_client_side",
        "source_surfaces": {
            "api_readiness": "/health.api_readiness",
            "learned_state": "/health.learned_state",
            "role_skill": "/health.role_skill",
            "connectors": "/health.connectors",
            "internal_inspection": str(api_readiness.get("internal_inspection_path", "/internal/state/inspect")),
            "current_turn_role": str(api_readiness.get("current_turn_role_surface", "system_debug.role")),
            "current_turn_selected_skills": str(
                api_readiness.get(
                    "current_turn_selected_skills_surface",
                    "system_debug.adaptive_state.selected_skills",
                )
            ),
            "current_turn_plan": str(api_readiness.get("current_turn_plan_surface", "system_debug.plan")),
        },
        "role_posture": {
            "role_selection_owner": role_skill_policy.get("role_selection_owner"),
            "current_role_name": role_skill_policy.get("current_role_name", ""),
            "work_partner_role_available": role_skill_policy.get("work_partner_role_available"),
            "work_partner_role_state": role_skill_policy.get("work_partner_role_state"),
            "work_partner_scope": role_skill_policy.get("work_partner_scope"),
            "work_partner_mutation_boundary": role_skill_policy.get("work_partner_mutation_boundary"),
        },
        "skill_catalog_posture": {
            "skill_selection_owner": role_skill_policy.get("skill_selection_owner"),
            "skill_execution_boundary": role_skill_policy.get("skill_execution_boundary"),
            "action_skill_execution_allowed": role_skill_policy.get("action_skill_execution_allowed"),
            "selection_visibility_summary": selection_summary,
            "catalog_count": skill_registry.get("catalog_count", 0),
            "catalog": skill_registry.get("catalog", []),
            "learning_posture": skill_registry.get("learning_posture"),
            "learning_hint": skill_registry.get("learning_hint"),
        },
        "tool_and_connector_posture": {
            "approved_tool_families": sorted(
                {
                    str(item).strip()
                    for item in list(work_partner_tool_families) + list(approved_connector_kinds)
                    if str(item).strip()
                }
            ),
            "approved_operations": list(approved_operations),
            "ready_operations": list(ready_operations),
            "credential_gap_operations": list(credential_gap_operations),
            "organizer_stack_state": organizer_tool_stack.get("readiness_state"),
            "organizer_stack_hint": organizer_tool_stack.get("readiness_hint"),
            "organizer_activation_state": organizer_activation_snapshot.get("provider_activation_state"),
            "organizer_activation_next_actions": organizer_activation_snapshot.get("next_actions", []),
            "confirmation_required_operations": organizer_tool_stack.get("confirmation_required_operations", []),
            "user_opt_in_required_operations": organizer_tool_stack.get("user_opt_in_required_operations", []),
            "web_knowledge_tools": web_knowledge_tools,
            "execution_baseline_owner": execution_baseline.get("execution_owner"),
            "execution_baseline_boundary": execution_baseline.get("mvp_boundary"),
        },
        "learned_state_linkage": {
            "learned_state_policy_owner": learned_state.get("policy_owner"),
            "tool_grounded_learning_policy_owner": (
                learned_state.get("tool_grounded_learning", {}) or {}
            ).get("policy_owner"),
            "skill_learning_posture": learned_state.get("skill_learning_posture"),
            "internal_inspection_path": learned_state.get("internal_inspection_path"),
        },
    }
