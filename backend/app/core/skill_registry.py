from __future__ import annotations

from typing import Any

from app.core.contracts import SkillCapabilityOutput


SKILL_REGISTRY_OWNER = "skill_registry"
SKILL_REGISTRY_CATALOG: tuple[dict[str, Any], ...] = (
    {
        "skill_id": "emotional_support",
        "label": "Emotional support",
        "capability_family": "support",
        "allowed_tools": [],
        "limitations": ["does_not_execute_tools"],
        "execution_owner": "not_applicable",
        "authorization_boundary": "not_applicable",
    },
    {
        "skill_id": "structured_reasoning",
        "label": "Structured reasoning",
        "capability_family": "analysis",
        "allowed_tools": [],
        "limitations": ["does_not_execute_tools"],
        "execution_owner": "not_applicable",
        "authorization_boundary": "not_applicable",
    },
    {
        "skill_id": "execution_planning",
        "label": "Execution planning",
        "capability_family": "execution",
        "allowed_tools": [],
        "limitations": ["does_not_execute_tools"],
        "execution_owner": "not_applicable",
        "authorization_boundary": "not_applicable",
    },
    {
        "skill_id": "memory_recall",
        "label": "Memory recall",
        "capability_family": "memory",
        "allowed_tools": [],
        "limitations": ["does_not_execute_tools"],
        "execution_owner": "not_applicable",
        "authorization_boundary": "not_applicable",
    },
    {
        "skill_id": "connector_boundary_review",
        "label": "Connector boundary review",
        "capability_family": "connector_boundary",
        "allowed_tools": [
            "task_system",
            "calendar",
            "cloud_drive",
            "knowledge_search",
            "web_browser",
        ],
        "limitations": ["reviews_connector_posture_only", "does_not_execute_tools"],
        "execution_owner": "action",
        "authorization_boundary": "connector_permission_gates",
    },
    {
        "skill_id": "website_review",
        "label": "Website review",
        "capability_family": "analysis",
        "allowed_tools": ["knowledge_search.search_web", "web_browser.read_page"],
        "limitations": [
            "read_only",
            "no_javascript_execution",
            "no_form_submission",
            "no_login_flow",
            "bounded_source_summary_only",
        ],
        "execution_owner": "action",
        "authorization_boundary": "connector_permission_gates",
    },
    {
        "skill_id": "web_research",
        "label": "Web research",
        "capability_family": "analysis",
        "allowed_tools": ["knowledge_search.search_web", "web_browser.read_page"],
        "limitations": [
            "read_only",
            "source_backed_summary_only",
            "bounded_page_review_optional",
        ],
        "execution_owner": "action",
        "authorization_boundary": "connector_permission_gates",
    },
    {
        "skill_id": "clickup_task_management",
        "label": "ClickUp task management",
        "capability_family": "connector_boundary",
        "allowed_tools": [
            "task_system.clickup_list_tasks",
            "task_system.clickup_create_task",
            "task_system.clickup_update_task",
        ],
        "limitations": [
            "list_tasks_read_only_when_enabled_and_configured",
            "create_update_require_explicit_confirmation",
            "no_provider_payload_persistence",
        ],
        "execution_owner": "action",
        "authorization_boundary": "connector_permission_gates",
    },
    {
        "skill_id": "work_partner_task_management",
        "label": "Work partner task management",
        "capability_family": "connector_boundary",
        "allowed_tools": [
            "task_system.clickup_list_tasks",
            "task_system.clickup_create_task",
            "task_system.clickup_update_task",
        ],
        "limitations": [
            "work_partner_strategy_metadata_only",
            "create_update_require_explicit_confirmation",
            "no_provider_payload_persistence",
        ],
        "execution_owner": "action",
        "authorization_boundary": "connector_permission_gates",
    },
)


def skills_for_role_and_topic(*, role_name: str, topic: str, event_text: str) -> list[SkillCapabilityOutput]:
    normalized_role = str(role_name or "").strip().lower()
    normalized_topic = str(topic or "").strip().lower()
    normalized_text = str(event_text or "").strip().lower()
    skills: list[SkillCapabilityOutput] = []

    if normalized_role == "friend":
        skills.append(_skill_output("emotional_support", reason="friend_role_selected"))
    if normalized_role == "work_partner":
        skills.append(_skill_output("structured_reasoning", reason="work_partner_role_selected"))
        skills.append(_skill_output("execution_planning", reason="work_partner_role_selected"))
        skills.append(_skill_output("connector_boundary_review", reason="work_partner_role_selected"))
    if normalized_role in {"analyst", "mentor"} or normalized_topic == "planning":
        skills.append(_skill_output("structured_reasoning", reason="analysis_or_planning_posture"))
    if normalized_role == "executor":
        skills.append(_skill_output("execution_planning", reason="executor_role_selected"))
    if any(keyword in normalized_text for keyword in {"remember", "recall", "memory", "pamiet", "przypomnij"}):
        skills.append(_skill_output("memory_recall", reason="memory_recall_request_detected"))
    if any(keyword in normalized_text for keyword in {"calendar", "clickup", "drive", "connector", "integrat"}):
        skills.append(_skill_output("connector_boundary_review", reason="connector_related_request_detected"))
    if any(keyword in normalized_text for keyword in {"http://", "https://", "website", "webpage", "page review"}):
        skills.append(_skill_output("website_review", reason="website_review_request_detected"))
    if any(keyword in normalized_text for keyword in {"search", "research", "look up", "latest", "web"}):
        skills.append(_skill_output("web_research", reason="web_research_request_detected"))
    if "clickup" in normalized_text:
        skills.append(_skill_output("clickup_task_management", reason="clickup_task_request_detected"))
        if normalized_role == "work_partner":
            skills.append(_skill_output("work_partner_task_management", reason="work_partner_clickup_request_detected"))

    deduped: list[SkillCapabilityOutput] = []
    seen: set[str] = set()
    for skill in skills:
        if skill.skill_id in seen:
            continue
        seen.add(skill.skill_id)
        deduped.append(skill)
    return deduped


def skill_registry_snapshot() -> dict[str, Any]:
    return {
        "policy_owner": SKILL_REGISTRY_OWNER,
        "catalog": [
            {
                **item,
                "side_effect_posture": "metadata_only",
                "tool_execution_allowed": False,
            }
            for item in SKILL_REGISTRY_CATALOG
        ],
        "catalog_count": len(SKILL_REGISTRY_CATALOG),
        "learning_posture": "registry_metadata_only",
        "learning_hint": "selected_skill_metadata_is_inspectable_but_not_self_modifying_code",
    }


def _skill_output(skill_id: str, *, reason: str) -> SkillCapabilityOutput:
    for item in SKILL_REGISTRY_CATALOG:
        if item["skill_id"] == skill_id:
            return SkillCapabilityOutput(
                skill_id=item["skill_id"],
                label=item["label"],
                capability_family=item["capability_family"],  # type: ignore[arg-type]
                reason=reason,
            )
    raise ValueError(f"Unknown skill registry id: {skill_id}")
