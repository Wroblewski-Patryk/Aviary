# Test Ownership Ledger

Last updated: 2026-05-03

This ledger gives backend tests stable feature and pipeline ownership IDs
without changing pytest behavior. It is the current machine-checkable bridge
between the traceability matrix and `backend/tests/`.

## Ownership IDs

| ID | Type | Name |
| --- | --- | --- |
| `FEAT-AUTH` | Feature | App auth and session |
| `FEAT-PROFILE` | Feature | Profile/settings |
| `FEAT-RESET` | Feature | User data reset |
| `FEAT-CHAT` | Feature | App chat |
| `FEAT-EVENT` | Feature | General event ingress |
| `FEAT-DEBUG` | Feature | Debug and incident evidence |
| `FEAT-LEARNED-STATE` | Feature | Personality/learned state overview |
| `FEAT-TOOLS` | Feature | Tools overview and preferences |
| `FEAT-TELEGRAM` | Feature | Telegram linking and delivery |
| `FEAT-RETRIEVAL` | Feature | Retrieval and embeddings |
| `FEAT-DEPLOYMENT` | Feature | Deployment/release smoke |
| `FEAT-WEB-SHELL` | Feature | Web shell routes and localization |
| `PIPE-APP-AUTH` | Pipeline | App auth session |
| `PIPE-APP-CHAT` | Pipeline | App chat turn |
| `PIPE-EVENT-INGRESS` | Pipeline | External event ingress |
| `PIPE-FOREGROUND-RUNTIME` | Pipeline | Foreground runtime |
| `PIPE-DEFERRED-REFLECTION` | Pipeline | Deferred reflection |
| `PIPE-SCHEDULER-PROACTIVE` | Pipeline | Scheduler/proactive/planned work |
| `PIPE-TOOLS` | Pipeline | Tools overview and connector readiness |
| `PIPE-TELEGRAM` | Pipeline | Telegram linking and transport |
| `PIPE-RETRIEVAL` | Pipeline | Retrieval and memory context |
| `PIPE-DEBUG-INCIDENT` | Pipeline | Debug and incident evidence |
| `PIPE-RELEASE-SMOKE` | Pipeline | Release and deployment smoke |
| `PIPE-WEB-SHELL` | Pipeline | Web shell route rendering |
| `DATA-MEMORY` | Data | Memory repository and data model |
| `DATA-SCHEMA` | Data | Schema baseline and migrations |
| `RUNTIME-STAGE` | Runtime | Individual runtime stage contracts |
| `POLICY-GOVERNANCE` | Policy | Runtime, connector, observability, and governance policies |

## Test File Ownership

| Test File | Primary IDs | Secondary IDs | Notes |
| --- | --- | --- | --- |
| `backend/tests/conftest.py` | `SUPPORT-TEST-INFRA` | none | Shared pytest fixtures; not a product feature. |
| `backend/tests/empathy_fixtures.py` | `SUPPORT-TEST-INFRA` | `RUNTIME-STAGE` | Shared empathy/language fixtures. |
| `backend/tests/test_action_executor.py` | `PIPE-TOOLS` | `PIPE-FOREGROUND-RUNTIME`, `POLICY-GOVERNANCE` | Action boundary and tool execution posture. |
| `backend/tests/test_adaptive_policy.py` | `POLICY-GOVERNANCE` | `FEAT-LEARNED-STATE` | Adaptive governance/readiness policy. |
| `backend/tests/test_affective_assessor.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Affective assessment logic. |
| `backend/tests/test_affective_contract.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Affective stage contract. |
| `backend/tests/test_api_routes.py` | `FEAT-AUTH`, `FEAT-PROFILE`, `FEAT-RESET`, `FEAT-CHAT`, `FEAT-EVENT`, `FEAT-DEBUG`, `FEAT-LEARNED-STATE`, `FEAT-TOOLS`, `FEAT-TELEGRAM` | `PIPE-APP-AUTH`, `PIPE-APP-CHAT`, `PIPE-EVENT-INGRESS`, `PIPE-TOOLS`, `PIPE-TELEGRAM`, `PIPE-DEBUG-INCIDENT` | Main route contract suite. |
| `backend/tests/test_behavior_validation_script.py` | `PIPE-RELEASE-SMOKE` | `PIPE-DEBUG-INCIDENT` | Behavior validation gate/script behavior. |
| `backend/tests/test_communication_boundary.py` | `FEAT-TELEGRAM` | `PIPE-FOREGROUND-RUNTIME`, `PIPE-DEFERRED-REFLECTION` | Communication boundary learning and relation evidence. |
| `backend/tests/test_config.py` | `FEAT-AUTH` | `POLICY-GOVERNANCE` | App/runtime configuration behavior. |
| `backend/tests/test_connector_policy.py` | `FEAT-TOOLS` | `PIPE-TOOLS`, `POLICY-GOVERNANCE` | Connector operation and permission policy. |
| `backend/tests/test_context_agent.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME`, `PIPE-RETRIEVAL` | Context-stage behavior. |
| `backend/tests/test_coolify_compose.py` | `FEAT-DEPLOYMENT` | `PIPE-RELEASE-SMOKE` | Compose/deployment configuration checks. |
| `backend/tests/test_debug_compat_telemetry.py` | `FEAT-DEBUG` | `PIPE-DEBUG-INCIDENT` | Debug compatibility telemetry. |
| `backend/tests/test_delivery_router.py` | `FEAT-CHAT`, `FEAT-TELEGRAM` | `PIPE-APP-CHAT`, `PIPE-TELEGRAM` | Reply delivery routing and transport boundaries. |
| `backend/tests/test_deployment_trigger_scripts.py` | `FEAT-DEPLOYMENT` | `PIPE-RELEASE-SMOKE`, `PIPE-DEBUG-INCIDENT` | Deployment trigger and release-smoke scripts. |
| `backend/tests/test_embedding_strategy.py` | `FEAT-RETRIEVAL` | `PIPE-RETRIEVAL` | Embedding strategy and provider/fallback posture. |
| `backend/tests/test_event_normalization.py` | `FEAT-EVENT` | `PIPE-EVENT-INGRESS`, `PIPE-TELEGRAM` | Event normalization and transport payload handling. |
| `backend/tests/test_expression_agent.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME`, `PIPE-APP-CHAT` | Expression-stage behavior. |
| `backend/tests/test_goal_task_signals.py` | `RUNTIME-STAGE` | `PIPE-DEFERRED-REFLECTION`, `DATA-MEMORY` | Goal/task signal extraction and persistence posture. |
| `backend/tests/test_graph_stage_adapters.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Graph adapter contracts. |
| `backend/tests/test_graph_state_contract.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Graph state contract. |
| `backend/tests/test_identity_service.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Identity continuity/service behavior. |
| `backend/tests/test_incident_evidence_bundle_script.py` | `FEAT-DEBUG` | `PIPE-DEBUG-INCIDENT`, `PIPE-RELEASE-SMOKE` | Incident evidence export. |
| `backend/tests/test_language_runtime.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME`, `FEAT-PROFILE` | Runtime language behavior. |
| `backend/tests/test_logging.py` | `POLICY-GOVERNANCE` | `PIPE-DEBUG-INCIDENT` | Logging setup and posture. |
| `backend/tests/test_main_lifespan_policy.py` | `POLICY-GOVERNANCE` | `PIPE-RELEASE-SMOKE` | Lifespan/runtime startup policy. |
| `backend/tests/test_main_runtime_policy.py` | `POLICY-GOVERNANCE` | `PIPE-RELEASE-SMOKE`, `PIPE-DEBUG-INCIDENT` | Runtime policy and production posture. |
| `backend/tests/test_memory_repository.py` | `DATA-MEMORY` | `FEAT-CHAT`, `FEAT-LEARNED-STATE`, `PIPE-DEFERRED-REFLECTION`, `PIPE-SCHEDULER-PROACTIVE`, `PIPE-RETRIEVAL` | Broad repository behavior. |
| `backend/tests/test_motivation_engine.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Motivation-stage behavior. |
| `backend/tests/test_observability_policy.py` | `FEAT-DEBUG` | `PIPE-DEBUG-INCIDENT`, `POLICY-GOVERNANCE` | Observability/export policy. |
| `backend/tests/test_openai_client.py` | `POLICY-GOVERNANCE` | `RUNTIME-STAGE` | OpenAI client boundary and fallback behavior. |
| `backend/tests/test_openai_prompting.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Prompting contract. |
| `backend/tests/test_planned_action_observer.py` | `PIPE-SCHEDULER-PROACTIVE` | `POLICY-GOVERNANCE` | Planned-action observer. |
| `backend/tests/test_planning_agent.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Planning-stage behavior. |
| `backend/tests/test_preferences.py` | `FEAT-PROFILE` | `PIPE-APP-AUTH` | Preference parsing and persistence posture. |
| `backend/tests/test_reflection_supervision_policy.py` | `PIPE-DEFERRED-REFLECTION` | `POLICY-GOVERNANCE` | Reflection supervision policy. |
| `backend/tests/test_reflection_worker.py` | `PIPE-DEFERRED-REFLECTION` | `DATA-MEMORY`, `FEAT-LEARNED-STATE` | Reflection queue and durable outputs. |
| `backend/tests/test_role_agent.py` | `RUNTIME-STAGE` | `PIPE-FOREGROUND-RUNTIME` | Role-stage behavior. |
| `backend/tests/test_runtime_pipeline.py` | `PIPE-FOREGROUND-RUNTIME` | `PIPE-APP-CHAT`, `PIPE-DEFERRED-REFLECTION`, `PIPE-SCHEDULER-PROACTIVE`, `PIPE-TOOLS` | End-to-end runtime composition with fakes. |
| `backend/tests/test_runtime_policy.py` | `POLICY-GOVERNANCE` | `PIPE-DEBUG-INCIDENT`, `PIPE-RELEASE-SMOKE` | Runtime/debug policy. |
| `backend/tests/test_scheduler_contracts.py` | `PIPE-SCHEDULER-PROACTIVE` | `POLICY-GOVERNANCE` | Scheduler domain contracts. |
| `backend/tests/test_scheduler_worker.py` | `PIPE-SCHEDULER-PROACTIVE` | `DATA-MEMORY` | Scheduler/proactive worker behavior. |
| `backend/tests/test_schema_baseline.py` | `DATA-SCHEMA` | `DATA-MEMORY` | Schema/table/constraint baseline. |
| `backend/tests/test_semantic_contracts.py` | `RUNTIME-STAGE` | `PIPE-RETRIEVAL` | Semantic runtime contracts. |
| `backend/tests/test_telegram_client.py` | `FEAT-TELEGRAM` | `PIPE-TELEGRAM` | Telegram client/provider boundary. |
| `backend/tests/test_web_routes.py` | `FEAT-WEB-SHELL` | `PIPE-WEB-SHELL` | Browser shell route fallback behavior. |

## Traceability Row Ownership

| Traceability Feature | Ownership IDs | Primary Test Files |
| --- | --- | --- |
| App auth and session | `FEAT-AUTH`, `PIPE-APP-AUTH` | `test_api_routes.py`, `test_config.py` |
| Profile/settings | `FEAT-PROFILE`, `PIPE-APP-AUTH` | `test_api_routes.py`, `test_preferences.py` |
| User data reset | `FEAT-RESET` | `test_api_routes.py`, `test_memory_repository.py` |
| App chat | `FEAT-CHAT`, `PIPE-APP-CHAT` | `test_api_routes.py`, `test_runtime_pipeline.py`, `test_expression_agent.py`, `test_delivery_router.py` |
| General event ingress | `FEAT-EVENT`, `PIPE-EVENT-INGRESS` | `test_event_normalization.py`, `test_api_routes.py`, `test_runtime_pipeline.py` |
| Debug/incident evidence | `FEAT-DEBUG`, `PIPE-DEBUG-INCIDENT` | `test_api_routes.py`, `test_runtime_policy.py`, `test_observability_policy.py`, `test_incident_evidence_bundle_script.py` |
| Personality/learned state overview | `FEAT-LEARNED-STATE` | `test_api_routes.py`, `test_memory_repository.py` |
| Tools overview and preferences | `FEAT-TOOLS`, `PIPE-TOOLS` | `test_api_routes.py`, `test_connector_policy.py`, `test_action_executor.py` |
| Telegram linking and delivery | `FEAT-TELEGRAM`, `PIPE-TELEGRAM` | `test_api_routes.py`, `test_telegram_client.py`, `test_delivery_router.py` |
| Runtime foreground pipeline | `PIPE-FOREGROUND-RUNTIME`, `RUNTIME-STAGE` | `test_runtime_pipeline.py`, `test_graph_stage_adapters.py`, `test_graph_state_contract.py` |
| Deferred reflection | `PIPE-DEFERRED-REFLECTION` | `test_reflection_worker.py`, `test_reflection_supervision_policy.py`, `test_memory_repository.py` |
| Scheduler/proactive/planned work | `PIPE-SCHEDULER-PROACTIVE` | `test_scheduler_worker.py`, `test_planned_action_observer.py`, `test_runtime_pipeline.py` |
| Retrieval and embeddings | `FEAT-RETRIEVAL`, `PIPE-RETRIEVAL` | `test_embedding_strategy.py`, `test_memory_repository.py`, `test_runtime_pipeline.py` |
| Deployment/release smoke | `FEAT-DEPLOYMENT`, `PIPE-RELEASE-SMOKE` | `test_deployment_trigger_scripts.py`, `test_main_runtime_policy.py` |
| Web shell routes and localization | `FEAT-WEB-SHELL`, `PIPE-WEB-SHELL` | `test_web_routes.py` |

## Known Gaps

- The ledger is file-level, not test-function-level.
- Frontend build evidence is listed in task records, but no dedicated frontend
  unit/e2e suite is owned here yet.
- Inline pytest markers are not introduced in this slice. Add them only after
  the file-level convention proves useful.
