import re

from app.core.action_delivery import action_delivery_envelope_matches_plan
from app.core.contracts import (
    ActionDelivery,
    ActionExecutionObservation,
    ActionLoopSummaryOutput,
    ActionResult,
    CancelPlannedWorkItemDomainIntent,
    CalendarSchedulingIntentDomainIntent,
    CompletePlannedWorkItemDomainIntent,
    ConnectedDriveAccessDomainIntent,
    ConnectorCapabilityDiscoveryDomainIntent,
    ConnectorPermissionGateOutput,
    ContextOutput,
    Event,
    ExternalTaskSyncDomainIntent,
    ExpressionOutput,
    MaintainTaskStatusDomainIntent,
    MemoryRecord,
    MotivationOutput,
    NoopDomainIntent,
    PerceptionOutput,
    PlanOutput,
    PromoteInferredGoalDomainIntent,
    PromoteInferredTaskDomainIntent,
    ReschedulePlannedWorkItemDomainIntent,
    RoleOutput,
    UpsertPlannedWorkItemDomainIntent,
    KnowledgeSearchDomainIntent,
    WebBrowserAccessDomainIntent,
    MaintainRelationDomainIntent,
    UpdateProactiveStateDomainIntent,
    UpdateCollaborationPreferenceDomainIntent,
    UpdateProactivePreferenceDomainIntent,
    UpdateResponseStyleDomainIntent,
    UpdateTaskStatusDomainIntent,
    ToolGroundedLearningCandidate,
    UpsertGoalDomainIntent,
    UpsertTaskDomainIntent,
)
from app.core.connector_policy import (
    connector_guardrail_snapshot,
    connector_intent_policy_violation,
)
from app.core.connector_confirmation import (
    build_connector_confirmation_replay_snapshot,
    build_pending_connector_confirmation_payload,
)
from app.integrations.calendar.google_calendar_client import GoogleCalendarAvailabilityClient
from app.integrations.cloud_drive.google_drive_client import GoogleDriveMetadataClient
from app.integrations.delivery_router import DeliveryRouter
from app.integrations.knowledge_search.duckduckgo_client import DuckDuckGoSearchClient
from app.integrations.task_system.clickup_client import ClickUpTaskClient
from app.integrations.telegram.client import TelegramClient
from app.integrations.telegram.telemetry import TelegramChannelTelemetry
from app.integrations.web_browser.generic_http_client import GenericHttpPageClient
from app.memory.embeddings import (
    materialize_embedding,
    normalize_embedding_refresh_mode,
    normalize_embedding_source_kinds,
    resolve_embedding_posture,
)
from app.memory.episodic import build_episode_summary
from app.memory.openai_embedding_client import OpenAIEmbeddingClient
from app.memory.repository import MemoryRepository
from app.core.tool_grounded_learning import (
    TOOL_GROUNDED_LEARNING_POLICY_OWNER,
    is_tool_grounded_conclusion_kind,
    tool_grounded_conclusion_kind,
)


class ActionExecutor:
    GENERIC_TOPIC_TAGS = {"general"}
    PERSISTABLE_LANGUAGE_SOURCES = {"explicit_request", "diacritic_signal", "keyword_signal"}
    WEBSITE_REVIEW_MAX_STEPS = 2

    def __init__(
        self,
        memory_repository: MemoryRepository,
        telegram_client: TelegramClient,
        *,
        semantic_vector_enabled: bool = True,
        embedding_provider: str = "deterministic",
        embedding_model: str = "deterministic-v1",
        embedding_dimensions: int = 32,
        embedding_source_kinds: tuple[str, ...] | None = None,
        embedding_refresh_mode: str = "on_write",
        openai_api_key: str | None = None,
        openai_embedding_client: OpenAIEmbeddingClient | None = None,
        clickup_task_client: ClickUpTaskClient | None = None,
        google_calendar_client: GoogleCalendarAvailabilityClient | None = None,
        google_drive_client: GoogleDriveMetadataClient | None = None,
        knowledge_search_client: DuckDuckGoSearchClient | None = None,
        web_browser_client: GenericHttpPageClient | None = None,
        telegram_telemetry: TelegramChannelTelemetry | None = None,
    ):
        self.memory_repository = memory_repository
        self.delivery_router = DeliveryRouter(
            telegram_client=telegram_client,
            telegram_telemetry=telegram_telemetry,
        )
        self.semantic_vector_enabled = semantic_vector_enabled
        self.embedding_dimensions = max(1, int(embedding_dimensions))
        self.embedding_refresh_mode = normalize_embedding_refresh_mode(embedding_refresh_mode)
        if embedding_source_kinds is None:
            self.embedding_source_kinds = set(normalize_embedding_source_kinds(None))
        else:
            self.embedding_source_kinds = {str(item).strip().lower() for item in embedding_source_kinds if str(item).strip()}
        self.embedding_posture = resolve_embedding_posture(
            provider=embedding_provider,
            model=embedding_model,
            openai_api_key=openai_api_key,
        )
        self.openai_embedding_client = openai_embedding_client
        if self.openai_embedding_client is None and str(openai_api_key or "").strip():
            self.openai_embedding_client = OpenAIEmbeddingClient(api_key=openai_api_key)
        self.clickup_task_client = clickup_task_client
        self.google_calendar_client = google_calendar_client
        self.google_drive_client = google_drive_client
        self.knowledge_search_client = knowledge_search_client
        self.web_browser_client = web_browser_client

    async def execute(self, plan: PlanOutput, delivery: ActionDelivery) -> ActionResult:
        proactive_delivery_guard = plan.proactive_delivery_guard
        if proactive_delivery_guard is not None and not proactive_delivery_guard.allowed:
            return ActionResult(
                status="noop",
                actions=[],
                notes=f"Proactive delivery deferred: {proactive_delivery_guard.reason}.",
            )
        connector_policy_violations = self._connector_policy_violations(plan)
        if connector_policy_violations:
            return ActionResult(
                status="fail",
                actions=[],
                notes=(
                    "Connector policy guardrail blocked inconsistent intent posture: "
                    + "; ".join(connector_policy_violations)
                ),
            )
        if not action_delivery_envelope_matches_plan(
            envelope=delivery.execution_envelope,
            plan=plan,
        ):
            return ActionResult(
                status="fail",
                actions=[],
                notes="Action delivery envelope drift detected between planning and action.",
            )
        connector_execution_result = await self._execute_provider_backed_connector_intents(plan)
        if connector_execution_result is not None and connector_execution_result.status == "fail":
            return connector_execution_result
        if not plan.needs_response:
            if connector_execution_result is not None:
                return connector_execution_result
            return ActionResult(status="noop", actions=[], notes="No response required.")
        effective_delivery = delivery
        if connector_execution_result is not None:
            enriched_message = self.enrich_delivery_message(
                delivery=delivery,
                action_result=connector_execution_result,
            )
            effective_delivery = delivery.model_copy(update={"message": enriched_message})
        delivery_result = await self.delivery_router.deliver(effective_delivery)
        if connector_execution_result is None:
            return delivery_result
        return self._merge_connector_execution_with_delivery(
            connector_execution_result=connector_execution_result,
            delivery_result=delivery_result,
        )

    async def persist_episode(
        self,
        event: Event,
        perception: PerceptionOutput,
        context: ContextOutput,
        motivation: MotivationOutput,
        role: RoleOutput,
        plan: PlanOutput,
        action_result: ActionResult,
        expression: ExpressionOutput,
    ) -> MemoryRecord:
        memory_kind = self._memory_kind(event, perception)
        memory_topics = self._memory_topics(event, perception)
        intent_updates = await self._apply_domain_intents(event=event, plan=plan)
        preference_update = str(intent_updates["preference_update"])
        collaboration_update = str(intent_updates["collaboration_update"])
        goal_update = str(intent_updates["goal_update"])
        task_update = str(intent_updates["task_update"])
        task_status_update = str(intent_updates["task_status_update"])
        planned_work_update = str(intent_updates["planned_work_update"])
        planned_work_status_update = str(intent_updates["planned_work_status_update"])
        calendar_connector_update = str(intent_updates["calendar_connector_update"])
        task_connector_update = str(intent_updates["task_connector_update"])
        drive_connector_update = str(intent_updates["drive_connector_update"])
        connector_expansion_update = str(intent_updates["connector_expansion_update"])
        relation_update = str(intent_updates["relation_update"])
        proactive_state_update = str(intent_updates["proactive_state_update"])
        proactive_preference_update = str(intent_updates["proactive_preference_update"])
        tool_grounded_learning_update = await self._persist_tool_grounded_learning(
            event=event,
            action_result=action_result,
        )
        calendar_connector_guardrail = str(intent_updates["calendar_connector_guardrail"])
        task_connector_guardrail = str(intent_updates["task_connector_guardrail"])
        drive_connector_guardrail = str(intent_updates["drive_connector_guardrail"])
        connector_expansion_guardrail = str(intent_updates["connector_expansion_guardrail"])
        executed_intents = list(intent_updates["executed_intents"])
        pending_connector_confirmation = build_pending_connector_confirmation_payload(
            event=event,
            plan=plan,
            action_result=action_result,
        )
        connector_confirmation_replay = build_connector_confirmation_replay_snapshot(
            event=event,
            plan=plan,
            action_result=action_result,
            pending_confirmation=pending_connector_confirmation,
        )

        payload = {
            "payload_version": 1,
            "event": str(event.payload.get("text", "")),
            "event_visibility": self._event_transcript_visibility(event=event),
            "chat_id": event.payload.get("chat_id"),
            "memory_kind": memory_kind,
            "memory_topics": memory_topics,
            "domain_intents": executed_intents,
            "response_language": expression.language,
            "affect_label": perception.affective.affect_label,
            "affect_intensity": perception.affective.intensity,
            "affect_needs_support": perception.affective.needs_support,
            "affect_source": perception.affective.source,
            "affect_evidence": perception.affective.evidence[:3],
            "behavior_feedback": [
                item.model_dump(mode="json")
                for item in perception.behavior_feedback
            ],
            "preference_update": preference_update,
            "collaboration_update": collaboration_update,
            "goal_update": goal_update,
            "task_update": task_update,
            "task_status_update": task_status_update,
            "planned_work_update": planned_work_update,
            "planned_work_status_update": planned_work_status_update,
            "calendar_connector_update": calendar_connector_update,
            "task_connector_update": task_connector_update,
            "drive_connector_update": drive_connector_update,
            "connector_expansion_update": connector_expansion_update,
            "relation_update": relation_update,
            "proactive_state_update": proactive_state_update,
            "proactive_preference_update": proactive_preference_update,
            "tool_grounded_learning_update": tool_grounded_learning_update,
            "calendar_connector_guardrail": calendar_connector_guardrail,
            "task_connector_guardrail": task_connector_guardrail,
            "drive_connector_guardrail": drive_connector_guardrail,
            "connector_expansion_guardrail": connector_expansion_guardrail,
            "context": context.summary,
            "motivation": motivation.mode,
            "role": role.selected,
            "plan_goal": plan.goal,
            "plan_steps": plan.steps,
            "action": action_result.status,
            "action_actions": list(action_result.actions),
            "pending_connector_confirmation": pending_connector_confirmation,
            "connector_confirmation_replay": connector_confirmation_replay,
            "assistant_visibility": self._assistant_transcript_visibility(
                event=event,
                action_result=action_result,
                expression=expression,
            ),
            "expression": expression.message,
        }
        summary = build_episode_summary(payload, max_length=1000)

        stored = await self.memory_repository.write_episode(
            event_id=event.event_id,
            trace_id=event.meta.trace_id,
            source=event.source,
            user_id=event.meta.user_id,
            event_timestamp=event.timestamp,
            summary=summary,
            payload=payload,
            importance=motivation.importance,
        )
        if (
            self.semantic_vector_enabled
            and "episodic" in self.embedding_source_kinds
            and hasattr(self.memory_repository, "upsert_semantic_embedding")
        ):
            if self.embedding_refresh_mode == "manual":
                episode_embedding = None
                embedding_status = "pending_manual_refresh"
            else:
                episode_embedding, embedding_status = await materialize_embedding(
                    content=f"{payload['event']} {payload['context']} {payload['expression']}",
                    posture=self.embedding_posture,
                    dimensions=self.embedding_dimensions,
                    refresh_mode=self.embedding_refresh_mode,
                    openai_embedding_client=self.openai_embedding_client,
                )
            await self.memory_repository.upsert_semantic_embedding(
                user_id=event.meta.user_id,
                source_kind="episodic",
                source_id=str(stored["id"]),
                source_event_id=event.event_id,
                scope_type="global",
                scope_key="global",
                content=str(payload["event"]),
                embedding=episode_embedding,
                embedding_model=self.embedding_posture["model_effective"],
                embedding_dimensions=self.embedding_dimensions,
                metadata={
                    "memory_kind": memory_kind,
                    "memory_topics": memory_topics,
                    "response_language": expression.language,
                    "affect_label": perception.affective.affect_label,
                    "affect_needs_support": perception.affective.needs_support,
                    "embedding_provider_requested": self.embedding_posture["provider_requested"],
                    "embedding_provider_effective": self.embedding_posture["provider_effective"],
                    "embedding_provider_hint": self.embedding_posture["provider_hint"],
                    "embedding_model_requested": self.embedding_posture["model_requested"],
                    "embedding_model_effective": self.embedding_posture["model_effective"],
                    "embedding_refresh_mode": self.embedding_refresh_mode,
                    "embedding_status": embedding_status,
                },
            )

        if perception.language_source in self.PERSISTABLE_LANGUAGE_SOURCES:
            await self.memory_repository.upsert_user_profile_language(
                user_id=event.meta.user_id,
                language_code=expression.language,
                confidence=perception.language_confidence,
                source=perception.language_source,
            )

        return MemoryRecord(
            id=stored["id"],
            event_id=stored["event_id"],
            timestamp=stored["timestamp"],
            summary=stored["summary"],
            payload=stored.get("payload", {}),
            importance=stored["importance"],
        )

    def _event_transcript_visibility(self, *, event: Event) -> str:
        if event.source == "scheduler":
            return "internal"
        return "transcript"

    def _assistant_transcript_visibility(
        self,
        *,
        event: Event,
        action_result: ActionResult,
        expression: ExpressionOutput,
    ) -> str:
        if not str(expression.message or "").strip():
            return "internal"
        if event.source == "scheduler":
            if action_result.status == "success" and "send_telegram_message" in action_result.actions:
                return "transcript"
            return "internal"
        if action_result.status not in {"success", "partial"}:
            return "internal"
        return "transcript"

    async def _execute_provider_backed_connector_intents(self, plan: PlanOutput) -> ActionResult | None:
        executed_actions: list[str] = []
        notes: list[str] = []
        learning_candidates: list[ToolGroundedLearningCandidate] = []
        observations: list[ActionExecutionObservation] = []
        latest_search_selected_url = ""
        latest_search_source_reference = ""

        for intent in plan.domain_intents:
            if isinstance(intent, ExternalTaskSyncDomainIntent):
                if intent.provider_hint != "clickup":
                    continue
                if self.clickup_task_client is None or not getattr(self.clickup_task_client, "ready", False):
                    return self._clickup_provider_blocked_result(intent)

                if intent.operation == "create_task":
                    if not self._connector_intent_confirmed(plan=plan, intent=intent):
                        executed_actions.append("clickup_mutation_confirmation_required")
                        task_name = self._connector_task_name(intent.task_hint)
                        notes.append(
                            "ClickUp task creation requires explicit confirmation before mutation."
                        )
                        observations.append(
                            self._action_observation(
                                tool_id="clickup",
                                operation="task_system.clickup_create_task",
                                provider_path="clickup:create_task",
                                source_reference=task_name,
                                bounded_summary=(
                                    "ClickUp task creation was not executed because "
                                    "explicit confirmation is still required."
                                ),
                                confidence=0.0,
                                blocker="confirmation_required",
                                next_step_relevance="needs_confirmation",
                            )
                        )
                        continue
                    task_name = self._connector_task_name(intent.task_hint)
                    try:
                        result = await self.clickup_task_client.create_task(
                            name=task_name,
                            description=f"Created by AION connector execution from intent: {intent.task_hint}",
                        )
                    except Exception as exc:
                        return ActionResult(
                            status="fail",
                            actions=["clickup_create_task"],
                            notes=f"ClickUp task execution failed: {type(exc).__name__}: {exc}",
                        )

                    executed_actions.append("clickup_create_task")
                    task_id = str(result.get("id", "unknown"))
                    notes.append(f"ClickUp task created ({task_id}) for '{task_name}'.")
                    observations.append(
                        self._action_observation(
                            tool_id="clickup",
                            operation="task_system.clickup_create_task",
                            provider_path="clickup:create_task",
                            source_reference=task_id,
                            bounded_summary=f"Created ClickUp task '{task_name}' with id '{task_id}'.",
                            confidence=0.82,
                            next_step_relevance="mutation_evidence_for_final_reply",
                        )
                    )
                    continue

                if intent.operation == "list_tasks":
                    try:
                        tasks = await self.clickup_task_client.list_tasks(limit=5)
                    except Exception as exc:
                        return ActionResult(
                            status="fail",
                            actions=["clickup_list_tasks"],
                            notes=f"ClickUp task read failed: {type(exc).__name__}: {exc}",
                        )

                    executed_actions.append("clickup_list_tasks")
                    task_names = [
                        self._connector_task_name(str(task.get("name", "")))
                        for task in tasks
                        if str(task.get("name", "")).strip()
                    ]
                    if task_names:
                        notes.append(
                            "ClickUp task read returned: " + ", ".join(task_names[:3]) + "."
                        )
                        task_summary = "ClickUp tasks observed: " + ", ".join(task_names[:3])
                        observations.append(
                            self._action_observation(
                                tool_id="clickup",
                                operation="task_system.clickup_list_tasks",
                                provider_path="clickup:list_tasks",
                                source_reference="clickup:list_tasks",
                                bounded_summary=task_summary,
                                confidence=0.78,
                            )
                        )
                        learning_candidates.append(
                            self._tool_learning_candidate(
                                source_family="task_system",
                                source_operation="list_tasks",
                                content=task_summary,
                                source_reference="clickup:list_tasks",
                            )
                        )
                    else:
                        notes.append("ClickUp task read returned no visible tasks.")
                        observations.append(
                            self._action_observation(
                                tool_id="clickup",
                                operation="task_system.clickup_list_tasks",
                                provider_path="clickup:list_tasks",
                                source_reference="clickup:list_tasks",
                                bounded_summary="ClickUp task read returned no visible tasks.",
                                confidence=0.62,
                                blocker="empty_result",
                                next_step_relevance="empty_read_evidence",
                            )
                        )
                    continue

                if intent.operation == "update_task":
                    try:
                        tasks = await self.clickup_task_client.list_tasks(limit=10)
                    except Exception as exc:
                        return ActionResult(
                            status="fail",
                            actions=["clickup_update_task"],
                            notes=f"ClickUp task lookup failed before update: {type(exc).__name__}: {exc}",
                        )

                    matched_task = self._match_clickup_task(intent.task_hint, tasks)
                    matched_task_name = self._connector_task_name(str(matched_task.get("name", ""))) if matched_task else ""
                    if not self._connector_intent_confirmed(plan=plan, intent=intent):
                        executed_actions.append("clickup_list_tasks")
                        if matched_task_name:
                            notes.append(
                                "ClickUp task update requires explicit confirmation before mutation. "
                                f"Matched candidate: {matched_task_name}."
                            )
                            bounded_summary = (
                                "ClickUp update candidate observed before confirmation: "
                                f"{matched_task_name}."
                            )
                            source_reference = str(matched_task.get("id", "clickup:list_tasks") if matched_task else "clickup:list_tasks")
                        else:
                            notes.append(
                                "ClickUp task update requires explicit confirmation before mutation, "
                                "and no bounded task match was found."
                            )
                            bounded_summary = (
                                "ClickUp update was not executed because explicit confirmation is required "
                                "and no bounded task match was found."
                            )
                            source_reference = "clickup:list_tasks"
                        observations.append(
                            self._action_observation(
                                tool_id="clickup",
                                operation="task_system.clickup_list_tasks",
                                provider_path="clickup:list_tasks",
                                source_reference=source_reference,
                                bounded_summary=bounded_summary,
                                confidence=0.66 if matched_task_name else 0.42,
                                blocker="confirmation_required",
                                next_step_relevance="needs_confirmation",
                            )
                        )
                        continue
                    if matched_task is None:
                        return ActionResult(
                            status="fail",
                            actions=["clickup_update_task"],
                            notes="ClickUp task update failed: no bounded task match found for the requested hint.",
                        )
                    task_id = str(matched_task.get("id", "") or "").strip()
                    if not task_id:
                        return ActionResult(
                            status="fail",
                            actions=["clickup_update_task"],
                            notes="ClickUp task update failed: matched task is missing an id.",
                        )
                    status_hint = self._normalize_clickup_status(intent.status_hint)
                    try:
                        updated = await self.clickup_task_client.update_task(
                            task_id=task_id,
                            status=status_hint,
                        )
                    except Exception as exc:
                        return ActionResult(
                            status="fail",
                            actions=["clickup_update_task"],
                            notes=f"ClickUp task update failed: {type(exc).__name__}: {exc}",
                        )

                    executed_actions.append("clickup_update_task")
                    updated_name = self._connector_task_name(str(updated.get("name", matched_task.get("name", ""))))
                    updated_status = str(updated.get("status", status_hint) or status_hint)
                    notes.append(
                        f"ClickUp task updated ({task_id}) for '{updated_name}' with status '{updated_status}'."
                    )
                    observations.append(
                        self._action_observation(
                            tool_id="clickup",
                            operation="task_system.clickup_update_task",
                            provider_path="clickup:update_task",
                            source_reference=task_id,
                            bounded_summary=(
                                f"Updated ClickUp task '{updated_name}' ({task_id}) "
                                f"to status '{updated_status}'."
                            ),
                            confidence=0.82,
                            next_step_relevance="mutation_evidence_for_final_reply",
                        )
                    )
                    continue

                continue

            if isinstance(intent, CalendarSchedulingIntentDomainIntent):
                if (
                    self.google_calendar_client is None
                    or not getattr(self.google_calendar_client, "ready", False)
                    or intent.provider_hint != "google_calendar"
                    or intent.operation != "read_availability"
                ):
                    continue
                try:
                    availability = await self.google_calendar_client.read_availability(
                        time_hint=intent.time_hint,
                        slot_minutes=60,
                        slot_limit=3,
                    )
                except Exception as exc:
                    return ActionResult(
                        status="fail",
                        actions=["google_calendar_read_availability"],
                        notes=f"Google Calendar availability read failed: {type(exc).__name__}: {exc}",
                    )

                executed_actions.append("google_calendar_read_availability")
                free_slot_preview = list(availability.get("free_slot_preview", []))
                if free_slot_preview:
                    normalized_slots = [str(slot) for slot in free_slot_preview[:3]]
                    notes.append(
                        "Google Calendar availability read "
                        f"({availability.get('window_start')} -> {availability.get('window_end')}, "
                        f"{availability.get('time_zone')}) found "
                        f"{availability.get('busy_window_count', 0)} busy windows. "
                        "Top free slots: "
                        + "; ".join(normalized_slots)
                        + "."
                    )
                    calendar_summary = (
                        "Calendar availability observed: "
                        f"{availability.get('window_start')} -> {availability.get('window_end')} "
                        f"{availability.get('time_zone')} busy={availability.get('busy_window_count', 0)} "
                        "top_free_slots="
                        + "; ".join(normalized_slots)
                    )
                    observations.append(
                        self._action_observation(
                            tool_id="google_calendar",
                            operation="calendar.google_calendar_read_availability",
                            provider_path="google_calendar:read_availability",
                            source_reference=str(
                                availability.get("window_start") or intent.time_hint or "calendar:read_availability"
                            ),
                            bounded_summary=calendar_summary,
                            confidence=0.76,
                        )
                    )
                    learning_candidates.append(
                        self._tool_learning_candidate(
                            source_family="calendar",
                            source_operation="read_availability",
                            content=calendar_summary,
                            source_reference=str(availability.get("window_start") or intent.time_hint or "calendar:read_availability"),
                        )
                    )
                else:
                    notes.append(
                        "Google Calendar availability read "
                        f"({availability.get('window_start')} -> {availability.get('window_end')}, "
                        f"{availability.get('time_zone')}) found no bounded free-slot preview."
                    )
                    calendar_summary = (
                        "Calendar availability observed: "
                        f"{availability.get('window_start')} -> {availability.get('window_end')} "
                        f"{availability.get('time_zone')} busy={availability.get('busy_window_count', 0)} "
                        "no_top_free_slots"
                    )
                    observations.append(
                        self._action_observation(
                            tool_id="google_calendar",
                            operation="calendar.google_calendar_read_availability",
                            provider_path="google_calendar:read_availability",
                            source_reference=str(
                                availability.get("window_start") or intent.time_hint or "calendar:read_availability"
                            ),
                            bounded_summary=calendar_summary,
                            confidence=0.7,
                            blocker="no_free_slot_preview",
                            next_step_relevance="availability_blocker_evidence",
                        )
                    )
                    learning_candidates.append(
                        self._tool_learning_candidate(
                            source_family="calendar",
                            source_operation="read_availability",
                            content=calendar_summary,
                            source_reference=str(availability.get("window_start") or intent.time_hint or "calendar:read_availability"),
                        )
                    )
                continue

            if isinstance(intent, ConnectedDriveAccessDomainIntent):
                if (
                    self.google_drive_client is None
                    or not getattr(self.google_drive_client, "ready", False)
                    or intent.provider_hint != "google_drive"
                    or intent.operation != "list_files"
                ):
                    continue
                try:
                    files = await self.google_drive_client.list_files(
                        file_hint=intent.file_hint,
                        limit=5,
                    )
                except Exception as exc:
                    return ActionResult(
                        status="fail",
                        actions=["google_drive_list_files"],
                        notes=f"Google Drive metadata read failed: {type(exc).__name__}: {exc}",
                    )

                executed_actions.append("google_drive_list_files")
                if files:
                    preview = [self._connector_drive_preview(item) for item in files[:3]]
                    notes.append("Google Drive metadata read returned: " + "; ".join(preview) + ".")
                    drive_summary = "Google Drive files observed: " + "; ".join(preview)
                    observations.append(
                        self._action_observation(
                            tool_id="google_drive",
                            operation="cloud_drive.google_drive_list_files",
                            provider_path="google_drive:list_files",
                            source_reference=str(intent.file_hint or "google_drive:list_files"),
                            bounded_summary=drive_summary,
                            confidence=0.76,
                        )
                    )
                    learning_candidates.append(
                        self._tool_learning_candidate(
                            source_family="cloud_drive",
                            source_operation="list_files",
                            content=drive_summary,
                            source_reference=str(intent.file_hint or "google_drive:list_files"),
                        )
                    )
                else:
                    notes.append("Google Drive metadata read returned no visible files.")
                    observations.append(
                        self._action_observation(
                            tool_id="google_drive",
                            operation="cloud_drive.google_drive_list_files",
                            provider_path="google_drive:list_files",
                            source_reference=str(intent.file_hint or "google_drive:list_files"),
                            bounded_summary="Google Drive metadata read returned no visible files.",
                            confidence=0.62,
                            blocker="empty_result",
                            next_step_relevance="empty_read_evidence",
                        )
                    )
                continue

            if isinstance(intent, KnowledgeSearchDomainIntent):
                if (
                    self.knowledge_search_client is None
                    or not getattr(self.knowledge_search_client, "ready", False)
                    or intent.provider_hint != "duckduckgo_html"
                    or intent.operation != "search_web"
                ):
                    continue
                try:
                    results = await self.knowledge_search_client.search_web(
                        query=intent.query_hint,
                        limit=5,
                    )
                except Exception as exc:
                    return ActionResult(
                        status="fail",
                        actions=["duckduckgo_search_web"],
                        notes=f"Web search failed: {type(exc).__name__}: {exc}",
                    )
                executed_actions.append("duckduckgo_search_web")
                if results:
                    preview = [self._search_result_preview(item) for item in results[:3]]
                    latest_search_selected_url = str(results[0].get("url", "") or "").strip()
                    latest_search_source_reference = intent.query_hint
                    notes.append("Web search returned: " + "; ".join(preview) + ".")
                    search_summary = f"Web search for '{intent.query_hint.strip()}': " + "; ".join(preview)
                    observations.append(
                        self._action_observation(
                            tool_id="web_search",
                            operation="knowledge_search.search_web",
                            provider_path="duckduckgo_html:search_web",
                            source_reference=intent.query_hint,
                            bounded_summary=search_summary,
                            confidence=0.72,
                        )
                    )
                    learning_candidates.append(
                        self._tool_learning_candidate(
                            source_family="knowledge_search",
                            source_operation="search_web",
                            content=search_summary,
                            source_reference=intent.query_hint,
                        )
                    )
                else:
                    notes.append("Web search returned no bounded results.")
                    observations.append(
                        self._action_observation(
                            tool_id="web_search",
                            operation="knowledge_search.search_web",
                            provider_path="duckduckgo_html:search_web",
                            source_reference=intent.query_hint,
                            bounded_summary="Web search returned no bounded results.",
                            confidence=0.58,
                            blocker="empty_result",
                            next_step_relevance="empty_read_evidence",
                        )
                    )
                continue

            if isinstance(intent, WebBrowserAccessDomainIntent):
                if (
                    self.web_browser_client is None
                    or not getattr(self.web_browser_client, "ready", False)
                    or intent.provider_hint != "generic_http"
                    or intent.operation != "read_page"
                ):
                    continue
                target_url = self._extract_url(intent.page_hint)
                if not target_url:
                    if self._plan_selects_skill(plan, "website_review"):
                        website_review_result = await self._execute_search_first_website_review(
                            query_hint=intent.page_hint,
                            selected_url=latest_search_selected_url,
                            selected_url_source_reference=latest_search_source_reference,
                        )
                        if website_review_result.status == "fail":
                            return website_review_result
                        executed_actions.extend(website_review_result.actions)
                        notes.append(website_review_result.notes)
                        learning_candidates.extend(website_review_result.tool_learning_candidates)
                        observations.extend(website_review_result.observations)
                        continue
                    return ActionResult(
                        status="fail",
                        actions=["generic_http_read_page"],
                        notes="Browser page read failed: no bounded URL was provided.",
                        observations=[
                            self._action_observation(
                                tool_id="web_browser",
                                operation="web_browser.read_page",
                                provider_path="generic_http:read_page",
                                source_reference=intent.page_hint,
                                bounded_summary="Browser page read failed because no bounded URL was provided.",
                                confidence=0.0,
                                blocker="missing_bounded_url",
                                next_step_relevance="clarification_required",
                            )
                        ],
                    )
                try:
                    page = await self.web_browser_client.read_page(url=target_url, excerpt_length=500)
                except Exception as exc:
                    return ActionResult(
                        status="fail",
                        actions=["generic_http_read_page"],
                        notes=f"Browser page read failed: {type(exc).__name__}: {exc}",
                    )
                executed_actions.append("generic_http_read_page")
                excerpt = " ".join(str(page.get("excerpt", "") or "").split())[:220]
                page_summary = (
                    f"Page read {page.get('title') or 'untitled'} "
                    f"({str(page.get('url', ''))[:120]}): {excerpt}"
                ).strip()
                notes.append(
                    "Browser page read returned: "
                    f"{page.get('title') or 'untitled'} [{page.get('content_type')}] "
                    f"{str(page.get('url', ''))[:120]}. Summary: {excerpt or 'no bounded excerpt available'}."
                )
                observations.append(
                    self._action_observation(
                        tool_id="web_browser",
                        operation="web_browser.read_page",
                        provider_path="generic_http:read_page",
                        source_reference=str(page.get("url", "") or target_url),
                        bounded_summary=page_summary,
                        confidence=0.74,
                    )
                )
                learning_candidates.append(
                    self._tool_learning_candidate(
                        source_family="web_browser",
                        source_operation="read_page",
                        content=page_summary,
                        source_reference=str(page.get("url", "") or target_url),
                    )
                )
                continue

        if not executed_actions:
            return None

        return ActionResult(
            status="success",
            actions=executed_actions,
            notes=" ".join(notes),
            tool_learning_candidates=learning_candidates,
            observations=observations,
            action_loop=self._action_loop_summary(
                plan=plan,
                status="success",
                actions=executed_actions,
                observations=observations,
            ),
        )

    async def _execute_search_first_website_review(
        self,
        *,
        query_hint: str,
        selected_url: str = "",
        selected_url_source_reference: str = "",
    ) -> ActionResult:
        if self.web_browser_client is None or not getattr(self.web_browser_client, "ready", False):
            return ActionResult(
                status="fail",
                actions=["generic_http_read_page"],
                notes="Website review failed: web browser client is not ready.",
                observations=[
                    self._action_observation(
                        tool_id="web_browser",
                        operation="web_browser.read_page",
                        provider_path="generic_http:read_page",
                        source_reference=query_hint,
                        bounded_summary="Website review could not read a page because the web browser client is not ready.",
                        confidence=0.0,
                        blocker="web_browser_client_not_ready",
                        next_step_relevance="provider_blocker",
                    )
                ],
            )

        executed_actions: list[str] = []
        notes: list[str] = []
        learning_candidates: list[ToolGroundedLearningCandidate] = []
        observations: list[ActionExecutionObservation] = []
        target_url = self._extract_url(selected_url)

        if not target_url:
            if self.knowledge_search_client is None or not getattr(self.knowledge_search_client, "ready", False):
                return ActionResult(
                    status="fail",
                    actions=["duckduckgo_search_web"],
                    notes="Website review failed: no bounded URL was provided and search is not ready.",
                    observations=[
                        self._action_observation(
                            tool_id="web_search",
                            operation="knowledge_search.search_web",
                            provider_path="duckduckgo_html:search_web",
                            source_reference=query_hint,
                            bounded_summary="Website review could not find a target page because search is not ready.",
                            confidence=0.0,
                            blocker="search_client_not_ready",
                            next_step_relevance="provider_blocker",
                        )
                    ],
                )
            try:
                results = await self.knowledge_search_client.search_web(query=query_hint, limit=3)
            except Exception as exc:
                return ActionResult(
                    status="fail",
                    actions=["duckduckgo_search_web"],
                    notes=f"Website review search failed: {type(exc).__name__}: {exc}",
                )

            executed_actions.append("duckduckgo_search_web")
            if not results:
                notes.append("Website review search returned no bounded target page.")
                observations.append(
                    self._action_observation(
                        tool_id="web_search",
                        operation="knowledge_search.search_web",
                        provider_path="duckduckgo_html:search_web",
                        source_reference=query_hint,
                        bounded_summary="Website review search returned no bounded target page.",
                        confidence=0.52,
                        blocker="empty_result",
                        next_step_relevance="clarification_required",
                    )
                )
                return ActionResult(status="success", actions=executed_actions, notes=" ".join(notes), observations=observations)

            preview = [self._search_result_preview(item) for item in results[:3]]
            selected = results[0]
            target_url = self._extract_url(str(selected.get("url", "") or ""))
            notes.append("Website review search selected: " + preview[0] + ".")
            search_summary = f"Website review search for '{query_hint.strip()}': " + "; ".join(preview)
            observations.append(
                self._action_observation(
                    tool_id="web_search",
                    operation="knowledge_search.search_web",
                    provider_path="duckduckgo_html:search_web",
                    source_reference=query_hint,
                    bounded_summary=search_summary,
                    confidence=0.7,
                    next_step_relevance="selected_first_result_for_page_review",
                )
            )
            learning_candidates.append(
                self._tool_learning_candidate(
                    source_family="knowledge_search",
                    source_operation="search_web",
                    content=search_summary,
                    source_reference=query_hint,
                )
            )
        elif selected_url_source_reference:
            notes.append(f"Website review reused search-selected target: {target_url}.")

        if not target_url:
            return ActionResult(
                status="fail",
                actions=executed_actions or ["generic_http_read_page"],
                notes="Website review failed: selected search result did not include a bounded URL.",
                observations=[
                    *observations,
                    self._action_observation(
                        tool_id="web_browser",
                        operation="web_browser.read_page",
                        provider_path="generic_http:read_page",
                        source_reference=query_hint,
                        bounded_summary="Website review could not read a page because the selected result had no bounded URL.",
                        confidence=0.0,
                        blocker="selected_result_missing_url",
                        next_step_relevance="clarification_required",
                    ),
                ],
            )

        try:
            page = await self.web_browser_client.read_page(url=target_url, excerpt_length=500)
        except Exception as exc:
            return ActionResult(
                status="fail",
                actions=[*executed_actions, "generic_http_read_page"],
                notes=f"Website review page read failed: {type(exc).__name__}: {exc}",
            )

        executed_actions.append("generic_http_read_page")
        excerpt = " ".join(str(page.get("excerpt", "") or "").split())[:220]
        page_summary = (
            f"Website review page read {page.get('title') or 'untitled'} "
            f"({str(page.get('url', ''))[:120]}): {excerpt}"
        ).strip()
        notes.append(
            "Website review page read returned: "
            f"{page.get('title') or 'untitled'} [{page.get('content_type')}] "
            f"{str(page.get('url', ''))[:120]}. Summary: {excerpt or 'no bounded excerpt available'}."
        )
        observations.append(
            self._action_observation(
                tool_id="web_browser",
                operation="web_browser.read_page",
                provider_path="generic_http:read_page",
                source_reference=str(page.get("url", "") or target_url),
                bounded_summary=page_summary,
                confidence=0.74,
                next_step_relevance="website_review_satisfied",
            )
        )
        learning_candidates.append(
            self._tool_learning_candidate(
                source_family="web_browser",
                source_operation="read_page",
                content=page_summary,
                source_reference=str(page.get("url", "") or target_url),
            )
        )
        notes.append(f"Website review loop completed within {self.WEBSITE_REVIEW_MAX_STEPS} steps.")
        return ActionResult(
            status="success",
            actions=executed_actions,
            notes=" ".join(notes),
            tool_learning_candidates=learning_candidates,
            observations=observations,
            action_loop=self._action_loop_summary(
                plan=None,
                status="success",
                actions=executed_actions,
                observations=observations,
            ),
        )

    def _merge_connector_execution_with_delivery(
        self,
        *,
        connector_execution_result: ActionResult,
        delivery_result: ActionResult,
    ) -> ActionResult:
        status = delivery_result.status
        if connector_execution_result.status == "success" and delivery_result.status == "fail":
            status = "partial"
        notes = f"{connector_execution_result.notes} {delivery_result.notes}".strip()
        return ActionResult(
            status=status,
            actions=[*connector_execution_result.actions, *delivery_result.actions],
            notes=notes,
            tool_learning_candidates=[
                *connector_execution_result.tool_learning_candidates,
                *delivery_result.tool_learning_candidates,
            ],
            observations=[
                *connector_execution_result.observations,
                *delivery_result.observations,
            ],
            action_loop=connector_execution_result.action_loop,
        )

    async def _persist_tool_grounded_learning(
        self,
        *,
        event: Event,
        action_result: ActionResult,
    ) -> str:
        if not hasattr(self.memory_repository, "upsert_conclusion"):
            return ""

        persisted_kinds: list[str] = []
        for candidate in action_result.tool_learning_candidates:
            if not is_tool_grounded_conclusion_kind(candidate.conclusion_kind):
                continue
            await self.memory_repository.upsert_conclusion(
                user_id=event.meta.user_id,
                kind=candidate.conclusion_kind,
                content=candidate.content,
                confidence=float(candidate.confidence),
                source=f"{TOOL_GROUNDED_LEARNING_POLICY_OWNER}:{candidate.source_family}.{candidate.source_operation}",
                supporting_event_id=event.event_id,
            )
            persisted_kinds.append(candidate.conclusion_kind)
        return ",".join(persisted_kinds)

    def _tool_learning_candidate(
        self,
        *,
        source_family: str,
        source_operation: str,
        content: str,
        source_reference: str,
    ) -> ToolGroundedLearningCandidate:
        return ToolGroundedLearningCandidate(
            source_family=source_family,
            source_operation=source_operation,
            conclusion_kind=tool_grounded_conclusion_kind(
                source_family=source_family,
                source_operation=source_operation,
            ),
            content=" ".join(str(content).split())[:500],
            source_reference=" ".join(str(source_reference).split())[:200],
        )

    def _action_observation(
        self,
        *,
        tool_id: str,
        operation: str,
        provider_path: str,
        bounded_summary: str,
        source_reference: str = "",
        confidence: float = 0.0,
        blocker: str | None = None,
        next_step_relevance: str = "available_for_expression_and_memory",
    ) -> ActionExecutionObservation:
        return ActionExecutionObservation(
            tool_id=" ".join(str(tool_id).split())[:80],
            operation=" ".join(str(operation).split())[:120],
            provider_path=" ".join(str(provider_path).split())[:120],
            source_reference=" ".join(str(source_reference).split())[:200],
            bounded_summary=" ".join(str(bounded_summary).split())[:500],
            confidence=max(0.0, min(1.0, float(confidence))),
            blocker=(" ".join(str(blocker).split())[:120] if blocker else None),
            next_step_relevance=" ".join(str(next_step_relevance).split())[:160],
            raw_payload_included=False,
        )

    def _action_loop_summary(
        self,
        *,
        plan: PlanOutput | None,
        status: str,
        actions: list[str],
        observations: list[ActionExecutionObservation],
    ) -> ActionLoopSummaryOutput:
        blockers: list[str] = []
        for observation in observations:
            if observation.blocker and observation.blocker not in blockers:
                blockers.append(observation.blocker)

        relevance_values = {observation.next_step_relevance for observation in observations}
        if "confirmation_required" in blockers or "needs_confirmation" in relevance_values:
            completion_state = "needs_confirmation"
        elif "clarification_required" in relevance_values:
            completion_state = "needs_clarification"
        elif "step_limit" in blockers:
            completion_state = "step_limit"
        elif status != "success" or blockers:
            completion_state = "blocked"
        else:
            completion_state = "satisfied"

        selected_skill_ids: list[str] = []
        if plan is not None:
            for skill in plan.selected_skills:
                if skill.skill_id not in selected_skill_ids:
                    selected_skill_ids.append(skill.skill_id)

        used_tools: list[str] = []
        for observation in observations:
            if observation.tool_id not in used_tools:
                used_tools.append(observation.tool_id)
        if not used_tools:
            for action in actions:
                if action not in used_tools:
                    used_tools.append(action)

        return ActionLoopSummaryOutput(
            step_count=len(observations),
            selected_skill_ids=selected_skill_ids,
            used_tools=used_tools,
            completion_state=completion_state,
            blockers=blockers,
            raw_payload_included=False,
        )

    def _clickup_provider_blocked_result(self, intent: ExternalTaskSyncDomainIntent) -> ActionResult:
        observations = [
            self._action_observation(
                tool_id="clickup",
                operation=f"task_system.clickup_{intent.operation}",
                provider_path=f"clickup:{intent.operation}",
                source_reference=intent.task_hint,
                bounded_summary="ClickUp provider client is not ready for the requested operation.",
                confidence=0.0,
                blocker="clickup_client_not_ready",
                next_step_relevance="provider_blocker",
            )
        ]
        return ActionResult(
            status="success",
            actions=["clickup_provider_blocked"],
            notes="ClickUp execution blocked: provider client is not ready.",
            observations=observations,
            action_loop=self._action_loop_summary(
                plan=None,
                status="success",
                actions=["clickup_provider_blocked"],
                observations=observations,
            ),
        )

    def _connector_intent_confirmed(
        self,
        *,
        plan: PlanOutput,
        intent: ExternalTaskSyncDomainIntent,
    ) -> bool:
        gate = self._matching_task_connector_gate(plan=plan, intent=intent)
        return bool(gate is not None and gate.requires_confirmation and gate.allowed)

    def _matching_task_connector_gate(
        self,
        *,
        plan: PlanOutput,
        intent: ExternalTaskSyncDomainIntent,
    ) -> ConnectorPermissionGateOutput | None:
        for gate in plan.connector_permission_gates:
            if gate.connector_kind != "task_system":
                continue
            if str(gate.provider_hint or "") != str(intent.provider_hint or ""):
                continue
            if gate.operation != intent.operation:
                continue
            return gate
        return None

    def _connector_task_name(self, task_hint: str) -> str:
        normalized = " ".join(str(task_hint or "").split())
        if not normalized:
            return "AION follow-up"
        return normalized[:120]

    def _connector_drive_preview(self, item: dict[str, str]) -> str:
        name = " ".join(str(item.get("name", "") or "").split())[:80] or "unnamed"
        mime_type = str(item.get("mime_type", "") or "").strip() or "unknown"
        item_id = str(item.get("id", "") or "").strip() or "unknown"
        return f"{name} [{mime_type}] ({item_id})"

    def _search_result_preview(self, item: dict[str, str]) -> str:
        title = " ".join(str(item.get("title", "") or "").split())[:80] or "untitled"
        url = str(item.get("url", "") or "").strip()[:120] or "unknown"
        return f"{title} ({url})"

    def enrich_delivery_message(self, *, delivery: ActionDelivery, action_result: ActionResult) -> str:
        supplements: list[str] = []
        notes = str(action_result.notes or "")
        markers = (
            ("Web search returned:", "Web lookup"),
            ("Browser page read returned:", "Page review"),
        )
        positions = [
            (notes.find(marker), marker, label)
            for marker, label in markers
            if notes.find(marker) != -1
        ]
        positions.sort(key=lambda item: item[0])
        for index, (start, marker, label) in enumerate(positions):
            if start == -1:
                continue
            next_start = len(notes)
            if index + 1 < len(positions):
                next_start = positions[index + 1][0]
            start = notes.find(marker)
            segment = notes[start:next_start].strip()
            if not segment:
                continue
            segment = segment.rstrip()
            if segment.endswith("Execution envelope:"):
                segment = segment.removesuffix("Execution envelope:").rstrip()
            normalized = segment.removeprefix(marker).strip()
            normalized = normalized.rstrip(". ")
            if normalized:
                supplements.append(f"{label}: {normalized}")
        if not supplements:
            return delivery.message
        return f"{delivery.message}\n\n" + "\n".join(supplements)

    def _extract_url(self, value: str) -> str:
        for token in str(value or "").split():
            token = token.strip("()[]<>,.;'\"")
            if token.startswith(("http://", "https://")):
                return token[:500]
            if re.fullmatch(r"(?:[a-z0-9-]+\.)+[a-z]{2,}", token, re.IGNORECASE):
                return f"https://{token[:492]}"
        return ""

    def _match_clickup_task(self, task_hint: str, tasks: list[dict]) -> dict | None:
        hint_tokens = self._text_tokens(task_hint)
        best_task: dict | None = None
        best_score = 0
        for task in tasks:
            task_tokens = self._text_tokens(str(task.get("name", "")) + " " + str(task.get("description", "")))
            overlap = len(hint_tokens.intersection(task_tokens))
            if overlap > best_score:
                best_score = overlap
                best_task = task
        return best_task if best_score > 0 else None

    def _normalize_clickup_status(self, status_hint: str) -> str:
        lowered = str(status_hint or "").strip().lower()
        if lowered in {"done", "complete", "closed"}:
            return "complete"
        if lowered in {"in_progress", "progress", "doing"}:
            return "in progress"
        return "to do"

    async def _apply_domain_intents(self, *, event: Event, plan: PlanOutput) -> dict[str, object]:
        preference_update = ""
        collaboration_update = ""
        goal_update = ""
        task_update = ""
        task_status_update = ""
        planned_work_update = ""
        planned_work_status_update = ""
        calendar_connector_update = ""
        task_connector_update = ""
        drive_connector_update = ""
        connector_expansion_update = ""
        relation_update = ""
        proactive_state_update = ""
        proactive_preference_update = ""
        calendar_connector_guardrail = ""
        task_connector_guardrail = ""
        drive_connector_guardrail = ""
        connector_expansion_guardrail = ""
        executed_intents: list[str] = []
        active_goals_cache: list[dict] | None = None
        active_tasks_cache: list[dict] | None = None
        active_planned_work_cache: list[dict] | None = None

        for intent in plan.domain_intents:
            executed_intents.append(intent.intent_type)

            if isinstance(intent, NoopDomainIntent):
                continue

            if isinstance(intent, UpdateResponseStyleDomainIntent):
                preference_update = f"response_style:{intent.style}"
                continue

            if isinstance(intent, UpdateCollaborationPreferenceDomainIntent):
                collaboration_update = intent.preference
                continue

            if isinstance(intent, UpdateProactivePreferenceDomainIntent):
                proactive_preference_update = f"proactive_opt_in:{str(intent.opt_in).lower()}"
                if hasattr(self.memory_repository, "upsert_conclusion"):
                    await self.memory_repository.upsert_conclusion(
                        user_id=event.meta.user_id,
                        kind="proactive_opt_in",
                        content="true" if intent.opt_in else "false",
                        confidence=0.95,
                        source=intent.source,
                        supporting_event_id=event.event_id,
                    )
                continue

            if isinstance(intent, UpsertGoalDomainIntent):
                stored_goal = await self.memory_repository.upsert_active_goal(
                    user_id=event.meta.user_id,
                    name=intent.name,
                    description=intent.description,
                    priority=intent.priority,
                    goal_type=intent.goal_type,
                )
                goal_update = str(stored_goal["name"])
                if active_goals_cache is None:
                    active_goals_cache = [stored_goal]
                else:
                    active_goals_cache.append(stored_goal)
                continue

            if isinstance(intent, PromoteInferredGoalDomainIntent):
                stored_goal = await self.memory_repository.upsert_active_goal(
                    user_id=event.meta.user_id,
                    name=intent.name,
                    description=intent.description,
                    priority=intent.priority,
                    goal_type=intent.goal_type,
                )
                goal_update = str(stored_goal["name"])
                if active_goals_cache is None:
                    active_goals_cache = [stored_goal]
                else:
                    active_goals_cache.append(stored_goal)
                continue

            if isinstance(intent, UpsertTaskDomainIntent):
                if active_goals_cache is None:
                    active_goals_cache = await self.memory_repository.get_active_goals(
                        user_id=event.meta.user_id,
                        limit=5,
                    )
                linked_goal_id = self._match_goal_for_task(intent.name, active_goals_cache)
                stored_task = await self.memory_repository.upsert_active_task(
                    user_id=event.meta.user_id,
                    name=intent.name,
                    description=intent.description,
                    priority=intent.priority,
                    goal_id=linked_goal_id,
                    status=intent.status,
                )
                task_update = str(stored_task["name"])
                if active_tasks_cache is None:
                    active_tasks_cache = [stored_task]
                else:
                    active_tasks_cache.append(stored_task)
                continue

            if isinstance(intent, PromoteInferredTaskDomainIntent):
                if active_goals_cache is None:
                    active_goals_cache = await self.memory_repository.get_active_goals(
                        user_id=event.meta.user_id,
                        limit=5,
                    )
                linked_goal_id = self._match_goal_for_task(intent.name, active_goals_cache)
                stored_task = await self.memory_repository.upsert_active_task(
                    user_id=event.meta.user_id,
                    name=intent.name,
                    description=intent.description,
                    priority=intent.priority,
                    goal_id=linked_goal_id,
                    status=intent.status,
                )
                task_update = str(stored_task["name"])
                if active_tasks_cache is None:
                    active_tasks_cache = [stored_task]
                else:
                    active_tasks_cache.append(stored_task)
                continue

            if isinstance(intent, UpdateTaskStatusDomainIntent):
                if active_tasks_cache is None:
                    active_tasks_cache = await self.memory_repository.get_active_tasks(
                        user_id=event.meta.user_id,
                        limit=8,
                    )
                matched_task = self._match_task_for_status(intent.task_hint, active_tasks_cache)
                if matched_task is None:
                    continue
                updated_task = await self.memory_repository.update_task_status(
                    task_id=int(matched_task["id"]),
                    status=intent.status,
                )
                if updated_task is not None:
                    task_status_update = f"{updated_task['name']}:{updated_task['status']}"
                continue

            if isinstance(intent, UpsertPlannedWorkItemDomainIntent):
                if active_goals_cache is None:
                    active_goals_cache = await self.memory_repository.get_active_goals(
                        user_id=event.meta.user_id,
                        limit=5,
                    )
                if active_tasks_cache is None:
                    goal_ids = [int(goal["id"]) for goal in active_goals_cache if goal.get("id") is not None]
                    active_tasks_cache = await self.memory_repository.get_active_tasks(
                        user_id=event.meta.user_id,
                        goal_ids=goal_ids,
                        limit=8,
                    )
                linked_goal_id = intent.goal_id
                linked_task_id = intent.task_id
                if linked_goal_id is None:
                    linked_goal_id = self._match_goal_for_task(intent.summary, active_goals_cache)
                if linked_task_id is None:
                    matched_task = self._match_task_for_status(intent.summary, active_tasks_cache)
                    linked_task_id = int(matched_task["id"]) if matched_task is not None and matched_task.get("id") is not None else None
                stored_planned_work = await self.memory_repository.upsert_planned_work_item(
                    user_id=event.meta.user_id,
                    kind=intent.work_kind,
                    summary=intent.summary,
                    goal_id=linked_goal_id,
                    task_id=linked_task_id,
                    not_before=intent.not_before,
                    preferred_at=intent.preferred_at,
                    expires_at=intent.expires_at,
                    recurrence_mode=intent.recurrence_mode,
                    recurrence_rule=intent.recurrence_rule,
                    delivery_channel=intent.channel_hint,
                    requires_foreground_execution=bool(intent.requires_foreground_execution),
                    quiet_hours_policy=intent.quiet_hours_policy,
                    provenance=intent.provenance,
                    source_event_id=event.event_id,
                )
                planned_work_update = (
                    f"{stored_planned_work['kind']}:"
                    f"{stored_planned_work['summary']}:"
                    f"{stored_planned_work['status']}"
                )
                if active_planned_work_cache is None:
                    active_planned_work_cache = [stored_planned_work]
                else:
                    active_planned_work_cache.append(stored_planned_work)
                continue

            if isinstance(intent, ReschedulePlannedWorkItemDomainIntent):
                updated_planned_work = await self.memory_repository.reschedule_planned_work_item(
                    work_id=int(intent.work_id),
                    not_before=intent.not_before,
                    preferred_at=intent.preferred_at,
                    expires_at=intent.expires_at,
                )
                if updated_planned_work is not None:
                    planned_work_status_update = (
                        f"{updated_planned_work['summary']}:"
                        f"{updated_planned_work['status']}:"
                        "rescheduled"
                    )
                continue

            if isinstance(intent, CancelPlannedWorkItemDomainIntent):
                updated_planned_work = await self.memory_repository.cancel_planned_work_item(
                    work_id=int(intent.work_id),
                )
                if updated_planned_work is not None:
                    planned_work_status_update = (
                        f"{updated_planned_work['summary']}:"
                        f"{updated_planned_work['status']}:"
                        "cancelled"
                    )
                continue

            if isinstance(intent, CompletePlannedWorkItemDomainIntent):
                updated_planned_work = await self.memory_repository.complete_planned_work_item(
                    work_id=int(intent.work_id),
                )
                if updated_planned_work is not None:
                    planned_work_status_update = (
                        f"{updated_planned_work['summary']}:"
                        f"{updated_planned_work['status']}:"
                        "completed"
                    )
                continue

            if isinstance(intent, MaintainTaskStatusDomainIntent):
                if active_tasks_cache is None:
                    active_tasks_cache = await self.memory_repository.get_active_tasks(
                        user_id=event.meta.user_id,
                        limit=8,
                    )
                matched_task = self._match_task_for_status(intent.task_hint, active_tasks_cache)
                if matched_task is None:
                    continue
                updated_task = await self.memory_repository.update_task_status(
                    task_id=int(matched_task["id"]),
                    status=intent.status,
                )
                if updated_task is not None:
                    task_status_update = f"{updated_task['name']}:{updated_task['status']}"
                continue

            if isinstance(intent, CalendarSchedulingIntentDomainIntent):
                calendar_connector_update = (
                    f"{intent.operation}:{intent.mode}:{intent.provider_hint or 'generic'}"
                )
                calendar_connector_guardrail = connector_guardrail_snapshot(intent)
                continue

            if isinstance(intent, ExternalTaskSyncDomainIntent):
                task_connector_update = (
                    f"{intent.operation}:{intent.mode}:{intent.provider_hint}"
                )
                task_connector_guardrail = connector_guardrail_snapshot(intent)
                continue

            if isinstance(intent, ConnectedDriveAccessDomainIntent):
                drive_connector_update = (
                    f"{intent.operation}:{intent.mode}:{intent.provider_hint}"
                )
                drive_connector_guardrail = connector_guardrail_snapshot(intent)
                continue

            if isinstance(intent, ConnectorCapabilityDiscoveryDomainIntent):
                connector_expansion_update = (
                    f"{intent.connector_kind}:{intent.provider_hint}:{intent.requested_capability}"
                )
                connector_expansion_guardrail = connector_guardrail_snapshot(intent)
                continue

            if isinstance(intent, MaintainRelationDomainIntent):
                if hasattr(self.memory_repository, "upsert_relation"):
                    stored_relation = await self.memory_repository.upsert_relation(
                        user_id=event.meta.user_id,
                        relation_type=intent.relation_type,
                        relation_value=intent.relation_value,
                        confidence=float(intent.confidence),
                        source=intent.source,
                        supporting_event_id=event.event_id,
                        scope_type=intent.scope_type,
                        scope_key=intent.scope_key,
                        evidence_count=int(intent.evidence_count),
                        decay_rate=float(intent.decay_rate),
                    )
                    relation_update = (
                        f"{stored_relation['relation_type']}:"
                        f"{stored_relation['relation_value']}:"
                        f"{stored_relation['scope_type']}:"
                        f"{stored_relation['scope_key']}"
                    )
                continue

            if isinstance(intent, UpdateProactiveStateDomainIntent):
                proactive_state_update = f"{intent.state}:{intent.trigger}:{intent.reason}"
                if hasattr(self.memory_repository, "upsert_conclusion"):
                    await self.memory_repository.upsert_conclusion(
                        user_id=event.meta.user_id,
                        kind="proactive_outreach_state",
                        content=intent.state,
                        confidence=0.9,
                        source=intent.source,
                        supporting_event_id=event.event_id,
                    )
                    await self.memory_repository.upsert_conclusion(
                        user_id=event.meta.user_id,
                        kind="proactive_outreach_trigger",
                        content=intent.trigger,
                        confidence=0.9,
                        source=intent.source,
                        supporting_event_id=event.event_id,
                    )
                continue

        return {
            "preference_update": preference_update,
            "collaboration_update": collaboration_update,
            "goal_update": goal_update,
            "task_update": task_update,
            "task_status_update": task_status_update,
            "planned_work_update": planned_work_update,
            "planned_work_status_update": planned_work_status_update,
            "calendar_connector_update": calendar_connector_update,
            "task_connector_update": task_connector_update,
            "drive_connector_update": drive_connector_update,
            "connector_expansion_update": connector_expansion_update,
            "relation_update": relation_update,
            "proactive_state_update": proactive_state_update,
            "proactive_preference_update": proactive_preference_update,
            "calendar_connector_guardrail": calendar_connector_guardrail,
            "task_connector_guardrail": task_connector_guardrail,
            "drive_connector_guardrail": drive_connector_guardrail,
            "connector_expansion_guardrail": connector_expansion_guardrail,
            "executed_intents": executed_intents,
        }

    def _connector_policy_violations(self, plan: PlanOutput) -> list[str]:
        violations: list[str] = []
        for intent in plan.domain_intents:
            if isinstance(
                intent,
                (
                    CalendarSchedulingIntentDomainIntent,
                    ExternalTaskSyncDomainIntent,
                    ConnectedDriveAccessDomainIntent,
                    ConnectorCapabilityDiscoveryDomainIntent,
                    KnowledgeSearchDomainIntent,
                    WebBrowserAccessDomainIntent,
                ),
            ):
                violation = connector_intent_policy_violation(intent)
                if violation is not None:
                    violations.append(violation)
        return violations

    def _plan_selects_skill(self, plan: PlanOutput, skill_id: str) -> bool:
        expected = str(skill_id or "").strip().lower()
        return any(str(skill.skill_id or "").strip().lower() == expected for skill in plan.selected_skills)

    def _match_goal_for_task(self, task_name: str, active_goals: list[dict]) -> int | None:
        task_tokens = self._text_tokens(task_name)
        best_goal_id: int | None = None
        best_score = 0
        for goal in active_goals:
            goal_id = goal.get("id")
            if goal_id is None:
                continue
            goal_tokens = self._text_tokens(str(goal.get("name", "")) + " " + str(goal.get("description", "")))
            overlap = len(task_tokens.intersection(goal_tokens))
            if overlap > best_score:
                best_score = overlap
                best_goal_id = int(goal_id)
        return best_goal_id

    def _match_task_for_status(self, task_hint: str, active_tasks: list[dict]) -> dict | None:
        hint_tokens = self._text_tokens(task_hint)
        best_task: dict | None = None
        best_score = 0
        for task in active_tasks:
            task_id = task.get("id")
            if task_id is None:
                continue
            task_tokens = self._text_tokens(str(task.get("name", "")) + " " + str(task.get("description", "")))
            overlap = len(hint_tokens.intersection(task_tokens))
            if overlap > best_score:
                best_score = overlap
                best_task = task
        return best_task if best_score > 0 else None

    def _memory_kind(self, event: Event, perception: PerceptionOutput) -> str:
        specific_topics = [
            topic
            for topic in self._memory_topics(event, perception)
            if topic not in self.GENERIC_TOPIC_TAGS
        ]
        return "semantic" if len(specific_topics) >= 2 else "continuity"

    def _memory_topics(self, event: Event, perception: PerceptionOutput) -> list[str]:
        text = str(event.payload.get("text", "")).strip().lower()
        canonical = "".join(char if char.isalnum() or char.isspace() else " " for char in text)
        stopwords = {
            "a",
            "an",
            "and",
            "are",
            "do",
            "for",
            "how",
            "i",
            "in",
            "is",
            "it",
            "me",
            "my",
            "now",
            "or",
            "please",
            "the",
            "this",
            "to",
            "we",
            "what",
            "with",
            "you",
            "czy",
            "co",
            "jak",
            "mi",
            "mnie",
            "na",
            "po",
            "prosze",
            "sie",
            "teraz",
            "to",
            "w",
            "z",
        }
        topics: list[str] = []
        seen: set[str] = set()
        for tag in perception.topic_tags:
            cleaned = tag.strip().lower()
            if not cleaned or cleaned in seen:
                continue
            seen.add(cleaned)
            topics.append(cleaned)
            if len(topics) >= 4:
                return topics

        for token in canonical.split():
            if len(token) < 3 or token in stopwords or token in seen:
                continue
            seen.add(token)
            topics.append(token)
            if len(topics) >= 4:
                break
        return topics

    def _text_tokens(self, value: str) -> set[str]:
        canonical = "".join(char if char.isalnum() or char.isspace() else " " for char in value.strip().lower())
        return {token for token in canonical.split() if len(token) >= 3}
