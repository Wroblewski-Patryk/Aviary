from __future__ import annotations

from typing import Any


LEARNED_STATE_POLICY_OWNER = "learned_state_inspection_policy"
LEARNED_STATE_INTERNAL_PATH = "/internal/state/inspect"


def learned_state_policy_snapshot() -> dict[str, Any]:
    return {
        "policy_owner": LEARNED_STATE_POLICY_OWNER,
        "internal_inspection_path": LEARNED_STATE_INTERNAL_PATH,
        "inspection_boundary": "internal_admin_debug_access_only",
        "identity_state_scope": "profile_language_plus_conclusion_preferences",
        "learned_knowledge_scope": "semantic_affective_relations_and_reflection_outputs",
        "skill_learning_posture": "selected_skill_metadata_only",
        "planning_state_scope": "active_goals_tasks_milestones_and_pending_proposals",
        "current_turn_selection_surface": "system_debug",
        "future_ui_posture": "backend_owned_surfaces_before_ui",
    }
