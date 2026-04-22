from __future__ import annotations

from typing import Any


ROLE_SKILL_POLICY_OWNER = "role_skill_boundary_policy"
ROLE_SELECTION_OWNER = "role_selection_policy"
SKILL_SELECTION_OWNER = "skill_registry"
SKILL_EXECUTION_BOUNDARY = "metadata_only_capability_hints"
SKILL_EXECUTION_HINT = "skills_inform_role_and_plan_but_do_not_execute_side_effects"


def role_skill_policy_snapshot(
    *,
    selected_skill_count: int = 0,
    planned_skill_count: int = 0,
) -> dict[str, Any]:
    return {
        "policy_owner": ROLE_SKILL_POLICY_OWNER,
        "role_selection_owner": ROLE_SELECTION_OWNER,
        "skill_selection_owner": SKILL_SELECTION_OWNER,
        "skill_execution_boundary": SKILL_EXECUTION_BOUNDARY,
        "action_skill_execution_allowed": False,
        "planning_carries_selected_skills": True,
        "selected_skill_count": max(0, int(selected_skill_count)),
        "planned_skill_count": max(0, int(planned_skill_count)),
        "production_baseline_state": "metadata_only_boundary_stable",
        "production_baseline_hint": SKILL_EXECUTION_HINT,
    }
