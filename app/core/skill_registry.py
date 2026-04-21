from __future__ import annotations

from app.core.contracts import SkillCapabilityOutput


def skills_for_role_and_topic(*, role_name: str, topic: str, event_text: str) -> list[SkillCapabilityOutput]:
    normalized_role = str(role_name or "").strip().lower()
    normalized_topic = str(topic or "").strip().lower()
    normalized_text = str(event_text or "").strip().lower()
    skills: list[SkillCapabilityOutput] = []

    if normalized_role == "friend":
        skills.append(
            SkillCapabilityOutput(
                skill_id="emotional_support",
                label="Emotional support",
                capability_family="support",
                reason="friend_role_selected",
            )
        )
    if normalized_role in {"analyst", "mentor"} or normalized_topic == "planning":
        skills.append(
            SkillCapabilityOutput(
                skill_id="structured_reasoning",
                label="Structured reasoning",
                capability_family="analysis",
                reason="analysis_or_planning_posture",
            )
        )
    if normalized_role == "executor":
        skills.append(
            SkillCapabilityOutput(
                skill_id="execution_planning",
                label="Execution planning",
                capability_family="execution",
                reason="executor_role_selected",
            )
        )
    if any(keyword in normalized_text for keyword in {"remember", "recall", "memory", "pamiet", "przypomnij"}):
        skills.append(
            SkillCapabilityOutput(
                skill_id="memory_recall",
                label="Memory recall",
                capability_family="memory",
                reason="memory_recall_request_detected",
            )
        )
    if any(keyword in normalized_text for keyword in {"calendar", "clickup", "drive", "connector", "integrat"}):
        skills.append(
            SkillCapabilityOutput(
                skill_id="connector_boundary_review",
                label="Connector boundary review",
                capability_family="connector_boundary",
                reason="connector_related_request_detected",
            )
        )

    deduped: list[SkillCapabilityOutput] = []
    seen: set[str] = set()
    for skill in skills:
        if skill.skill_id in seen:
            continue
        seen.add(skill.skill_id)
        deduped.append(skill)
    return deduped
