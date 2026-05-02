# Column Model Reference

Generated from `backend/app/memory/models.py` via `Base.metadata`.
Do not edit table details by hand; regenerate this file after model changes.

Regeneration command:

```powershell
Push-Location .\backend
..\.venv\Scripts\python .\scripts\export_data_model_reference.py --columns-output ..\docs\data\columns.md --erd-output ..\docs\data\erd.mmd
Pop-Location
```

## `aion_attention_turn`

- ORM model: `AionAttentionTurn`
- Primary key: `id`
- Unique constraints: uq_aion_attention_turn_user_conversation(user_id, conversation_key)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `conversation_key` | `VARCHAR(96)` | no | yes | none |
| `turn_id` | `VARCHAR(64)` | no | yes | none |
| `status` | `VARCHAR(24)` | no | yes | pending |
| `source_count` | `INTEGER` | no | no | 1 |
| `assembled_text` | `TEXT` | yes | no | none |
| `owner_mode` | `VARCHAR(24)` | no | no | durable_inbox |
| `messages_json` | `JSON` | yes | no | none |
| `event_ids_json` | `JSON` | yes | no | none |
| `update_keys_json` | `JSON` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_auth_session`

- ORM model: `AionAuthSession`
- Primary key: `id`
- Unique constraints: uq_aion_auth_session_token_hash(session_token_hash)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `VARCHAR(64)` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `session_token_hash` | `VARCHAR(128)` | no | yes | none |
| `expires_at` | `DATETIME` | no | yes | none |
| `revoked_at` | `DATETIME` | yes | yes | none |
| `last_seen_at` | `DATETIME` | yes | no | none |
| `user_agent` | `VARCHAR(256)` | yes | no | none |
| `ip_address` | `VARCHAR(64)` | yes | no | none |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_auth_user`

- ORM model: `AionAuthUser`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `VARCHAR(64)` | no | no | none |
| `email` | `VARCHAR(320)` | no | yes | none |
| `password_hash` | `TEXT` | no | no | none |
| `display_name` | `VARCHAR(120)` | yes | no | none |
| `is_active` | `INTEGER` | no | no | 1 |
| `last_login_at` | `DATETIME` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_conclusion`

- ORM model: `AionConclusion`
- Primary key: `id`
- Unique constraints: uq_aion_conclusion_user_kind_scope(user_id, kind, scope_type, scope_key)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `kind` | `VARCHAR(32)` | no | yes | none |
| `scope_type` | `VARCHAR(16)` | no | yes | global |
| `scope_key` | `VARCHAR(64)` | no | yes | global |
| `content` | `VARCHAR(128)` | no | no | none |
| `confidence` | `FLOAT` | no | no | 0.0 |
| `source` | `VARCHAR(32)` | no | no | system |
| `supporting_event_id` | `VARCHAR(64)` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_goal`

- ORM model: `AionGoal`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `name` | `VARCHAR(160)` | no | no | none |
| `description` | `TEXT` | no | no | none |
| `priority` | `VARCHAR(16)` | no | yes | medium |
| `status` | `VARCHAR(24)` | no | yes | active |
| `goal_type` | `VARCHAR(24)` | no | no | tactical |
| `created_at` | `DATETIME` | no | no | callable |
| `updated_at` | `DATETIME` | no | no | callable |

## `aion_goal_milestone`

- ORM model: `AionGoalMilestone`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `goal_id` | `INTEGER` | no | yes | none |
| `name` | `VARCHAR(160)` | no | no | none |
| `phase` | `VARCHAR(32)` | no | yes | none |
| `status` | `VARCHAR(24)` | no | yes | active |
| `source_event_id` | `VARCHAR(64)` | yes | no | none |
| `created_at` | `DATETIME` | no | no | callable |
| `updated_at` | `DATETIME` | no | no | callable |

## `aion_goal_milestone_history`

- ORM model: `AionGoalMilestoneHistory`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `goal_id` | `INTEGER` | no | yes | none |
| `milestone_name` | `VARCHAR(160)` | no | no | none |
| `phase` | `VARCHAR(32)` | no | yes | none |
| `risk_level` | `VARCHAR(32)` | yes | yes | none |
| `completion_criteria` | `VARCHAR(64)` | yes | no | none |
| `source_event_id` | `VARCHAR(64)` | yes | no | none |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_goal_progress`

- ORM model: `AionGoalProgress`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `goal_id` | `INTEGER` | no | yes | none |
| `score` | `FLOAT` | no | no | 0.0 |
| `execution_state` | `VARCHAR(32)` | yes | no | none |
| `progress_trend` | `VARCHAR(32)` | yes | no | none |
| `source_event_id` | `VARCHAR(64)` | yes | no | none |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_memory`

- ORM model: `AionMemory`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `event_id` | `VARCHAR(64)` | no | yes | none |
| `trace_id` | `VARCHAR(64)` | no | yes | none |
| `source` | `VARCHAR(32)` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `event_timestamp` | `DATETIME` | no | no | none |
| `summary` | `TEXT` | no | no | none |
| `payload` | `JSON` | yes | no | none |
| `importance` | `FLOAT` | no | no | 0.0 |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_planned_work_item`

- ORM model: `AionPlannedWorkItem`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `goal_id` | `INTEGER` | yes | yes | none |
| `task_id` | `INTEGER` | yes | yes | none |
| `kind` | `VARCHAR(24)` | no | yes | none |
| `summary` | `VARCHAR(220)` | no | no | none |
| `status` | `VARCHAR(24)` | no | yes | pending |
| `not_before` | `DATETIME` | yes | yes | none |
| `preferred_at` | `DATETIME` | yes | yes | none |
| `expires_at` | `DATETIME` | yes | yes | none |
| `recurrence_mode` | `VARCHAR(16)` | no | no | none |
| `recurrence_rule` | `VARCHAR(120)` | no | no | none |
| `delivery_channel` | `VARCHAR(16)` | no | no | none |
| `requires_foreground_execution` | `INTEGER` | no | no | 1 |
| `quiet_hours_policy` | `VARCHAR(32)` | no | no | respect_user_context |
| `provenance` | `VARCHAR(32)` | no | no | explicit_user_request |
| `source_event_id` | `VARCHAR(64)` | yes | yes | none |
| `last_evaluated_at` | `DATETIME` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_profile`

- ORM model: `AionProfile`
- Primary key: `user_id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `user_id` | `VARCHAR(64)` | no | no | none |
| `preferred_language` | `VARCHAR(8)` | no | no | none |
| `ui_language` | `VARCHAR(16)` | no | no | system |
| `utc_offset` | `VARCHAR(16)` | no | no | UTC+00:00 |
| `language_confidence` | `FLOAT` | no | no | 0.0 |
| `language_source` | `VARCHAR(32)` | no | no | default |
| `telegram_chat_id` | `VARCHAR(64)` | yes | no | none |
| `telegram_user_id` | `VARCHAR(64)` | yes | no | none |
| `telegram_link_code` | `VARCHAR(32)` | yes | yes | none |
| `telegram_link_code_issued_at` | `DATETIME` | yes | no | none |
| `telegram_linked_at` | `DATETIME` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_reflection_task`

- ORM model: `AionReflectionTask`
- Primary key: `id`
- Unique constraints: uq_aion_reflection_task_event_id(event_id)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `event_id` | `VARCHAR(64)` | no | yes | none |
| `status` | `VARCHAR(24)` | no | yes | pending |
| `attempts` | `INTEGER` | no | no | 0 |
| `last_error` | `TEXT` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_relation`

- ORM model: `AionRelation`
- Primary key: `id`
- Unique constraints: uq_aion_relation_user_type_scope(user_id, relation_type, scope_type, scope_key)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `relation_type` | `VARCHAR(32)` | no | yes | none |
| `relation_value` | `VARCHAR(128)` | no | no | none |
| `confidence` | `FLOAT` | no | no | 0.0 |
| `source` | `VARCHAR(32)` | no | no | background_reflection |
| `scope_type` | `VARCHAR(16)` | no | yes | global |
| `scope_key` | `VARCHAR(64)` | no | yes | global |
| `supporting_event_id` | `VARCHAR(64)` | yes | no | none |
| `evidence_count` | `INTEGER` | no | no | 1 |
| `decay_rate` | `FLOAT` | no | no | 0.02 |
| `last_observed_at` | `DATETIME` | no | no | callable |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_scheduler_cadence_evidence`

- ORM model: `AionSchedulerCadenceEvidence`
- Primary key: `id`
- Unique constraints: uq_aion_scheduler_cadence_evidence_kind(cadence_kind)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `cadence_kind` | `VARCHAR(24)` | no | yes | none |
| `execution_owner` | `VARCHAR(32)` | no | no | none |
| `execution_mode` | `VARCHAR(24)` | no | no | none |
| `summary_json` | `JSON` | yes | no | none |
| `last_run_at` | `DATETIME` | no | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_semantic_embedding`

- ORM model: `AionSemanticEmbedding`
- Primary key: `id`
- Unique constraints: uq_aion_semantic_embedding_source(user_id, source_kind, source_id)

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `source_kind` | `VARCHAR(24)` | no | yes | none |
| `source_id` | `VARCHAR(96)` | no | yes | none |
| `source_event_id` | `VARCHAR(64)` | yes | yes | none |
| `scope_type` | `VARCHAR(16)` | no | yes | global |
| `scope_key` | `VARCHAR(64)` | no | yes | global |
| `content` | `TEXT` | no | no | none |
| `embedding` | `JSON` | yes | no | none |
| `embedding_model` | `VARCHAR(64)` | no | no | deterministic-v1 |
| `embedding_dimensions` | `INTEGER` | no | no | 32 |
| `metadata_json` | `JSON` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_subconscious_proposal`

- ORM model: `AionSubconsciousProposal`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `proposal_type` | `VARCHAR(32)` | no | yes | none |
| `summary` | `TEXT` | no | no | none |
| `payload` | `JSON` | yes | no | none |
| `confidence` | `FLOAT` | no | no | 0.0 |
| `source_event_id` | `VARCHAR(64)` | yes | yes | none |
| `status` | `VARCHAR(24)` | no | yes | pending |
| `decision_reason` | `TEXT` | yes | no | none |
| `research_policy` | `VARCHAR(16)` | no | no | read_only |
| `allowed_tools_json` | `JSON` | yes | no | none |
| `decided_at` | `DATETIME` | yes | no | none |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |

## `aion_task`

- ORM model: `AionTask`
- Primary key: `id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `id` | `INTEGER` | no | no | none |
| `user_id` | `VARCHAR(64)` | no | yes | none |
| `goal_id` | `INTEGER` | yes | yes | none |
| `name` | `VARCHAR(160)` | no | no | none |
| `description` | `TEXT` | no | no | none |
| `priority` | `VARCHAR(16)` | no | yes | medium |
| `status` | `VARCHAR(24)` | no | yes | todo |
| `created_at` | `DATETIME` | no | no | callable |
| `updated_at` | `DATETIME` | no | no | callable |

## `aion_theta`

- ORM model: `AionTheta`
- Primary key: `user_id`
- Unique constraints: none

| Column | Type | Nullable | Indexed | Default |
| --- | --- | --- | --- | --- |
| `user_id` | `VARCHAR(64)` | no | no | none |
| `support_bias` | `FLOAT` | no | no | 0.0 |
| `analysis_bias` | `FLOAT` | no | no | 0.0 |
| `execution_bias` | `FLOAT` | no | no | 0.0 |
| `updated_at` | `DATETIME` | no | no | callable |
| `created_at` | `DATETIME` | no | no | callable |
