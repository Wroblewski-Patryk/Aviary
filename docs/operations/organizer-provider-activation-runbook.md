# Organizer Provider Activation Runbook

Last updated: 2026-05-03

## Purpose

This runbook turns the organizer provider credential gap into an explicit
operator checklist for ClickUp, Google Calendar, and Google Drive.

Organizer provider activation is an extension gate. It does not block the core
no-UI v1 declaration, but it must be complete before claiming daily-use
organizer readiness.

## Current Production Snapshot

Checked on 2026-05-03 through `GET https://aviary.luckysparrow.ch/health`.

- `/health.connectors.organizer_tool_stack.readiness_state`:
  `provider_credentials_missing`
- `/health.connectors.organizer_tool_stack.provider_ready_operation_count`:
  `0`
- `/health.connectors.organizer_tool_stack.provider_total_operation_count`:
  `5`
- `/health.connectors.organizer_tool_stack.daily_use_state`:
  `daily_use_workflows_blocked_by_provider_activation`
- `/health.connectors.organizer_tool_stack.daily_use_ready_workflow_count`:
  `0`
- `/health.connectors.organizer_tool_stack.daily_use_total_workflow_count`:
  `3`

Blocked workflows:

- `clickup_task_review_and_mutation`
- `google_calendar_availability_inspection`
- `google_drive_file_space_inspection`

## Activation Boundaries

- Raw provider secrets belong in deployment environment configuration only.
- Browser and mobile UI must not become a provider-secret entry surface.
- User opt-in remains required for organizer operations even after provider
  credentials are configured.
- ClickUp mutations remain confirmation-gated:
  - `task_system.clickup_create_task`
  - `task_system.clickup_update_task`
- Google Calendar remains read-only availability evidence:
  - `calendar.google_calendar_read_availability`
- Google Drive remains metadata-only file-space evidence:
  - `cloud_drive.google_drive_list_files`
- Calendar management, Drive document body ingestion, and Drive mutations are
  out of scope unless architecture explicitly changes.

## Required Provider Settings

### ClickUp

Required environment settings:

- `CLICKUP_API_TOKEN`
- `CLICKUP_LIST_ID`

Operations unlocked when configured and user-enabled:

- `task_system.clickup_create_task`
- `task_system.clickup_list_tasks`
- `task_system.clickup_update_task`

Expected health transition:

- `provider_requirements.clickup.ready=true`
- `provider_readiness.task_system.clickup_list_tasks.ready=true`
- `clickup_task_review_and_mutation.daily_use_ready=true`

### Google Calendar

Required environment settings:

- `GOOGLE_CALENDAR_ACCESS_TOKEN`
- `GOOGLE_CALENDAR_CALENDAR_ID`
- `GOOGLE_CALENDAR_TIMEZONE`

Operations unlocked when configured and user-enabled:

- `calendar.google_calendar_read_availability`

Expected health transition:

- `provider_requirements.google_calendar.ready=true`
- `provider_readiness.calendar.google_calendar_read_availability.ready=true`
- `google_calendar_availability_inspection.daily_use_ready=true`

### Google Drive

Required environment settings:

- `GOOGLE_DRIVE_ACCESS_TOKEN`
- `GOOGLE_DRIVE_FOLDER_ID`

Operations unlocked when configured and user-enabled:

- `cloud_drive.google_drive_list_files`

Expected health transition:

- `provider_requirements.google_drive.ready=true`
- `provider_readiness.cloud_drive.google_drive_list_files.ready=true`
- `google_drive_file_space_inspection.daily_use_ready=true`

## Operator Checklist

1. Confirm the intended production environment.
2. Add or update the required provider settings in Coolify or the active
   deployment environment.
3. Redeploy the service.
4. Run `GET /health` and inspect:
   - `connectors.organizer_tool_stack.activation_snapshot`
   - `connectors.organizer_tool_stack.provider_requirements`
   - `connectors.organizer_tool_stack.provider_readiness`
   - `v1_readiness.organizer_daily_use_state`
5. Confirm `provider_activation_ready=3`.
6. Confirm `provider_ready_operation_count=5`.
7. Confirm `daily_use_ready_workflow_count=3`.
8. Confirm user opt-in is enabled through the app settings route or API
   settings update path for the account being smoked.
9. Run `PRJ-918` provider activation smoke.
10. Attach production health and smoke evidence to the release record.

## Smoke Expectations

After activation, `PRJ-918` should prove:

- ClickUp read-only task listing works.
- ClickUp create/update remains confirmation-gated and bounded.
- Google Calendar availability read works with the configured calendar and
  timezone.
- Google Drive metadata listing works for the configured folder.
- Raw provider payloads do not leak through:
  - durable memory
  - `/health`
  - `/app/personality/overview`
  - web routes
- `organizer_daily_use_state` reflects actual provider readiness.

## Rollback

If a provider activation causes runtime instability or incorrect readiness:

1. Remove or correct the affected provider environment settings.
2. Redeploy.
3. Confirm `/health.release_readiness.ready=true`.
4. Confirm the affected provider returns to `credentials_missing` or the
   corrected ready state.
5. Do not mark organizer daily use ready until `PRJ-918` passes again.
