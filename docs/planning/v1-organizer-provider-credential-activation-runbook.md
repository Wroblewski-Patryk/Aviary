# V1 Organizer Provider Credential Activation Runbook

Last updated: 2026-05-03

## Status

`PRJ-917` is DONE.

The organizer provider credential gap is now a documented operator checklist.

## Evidence

Production health reviewed on 2026-05-03:

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

Validation:

- `git diff --check`
  - passed

## Runbook

New operator runbook:

- `docs/operations/organizer-provider-activation-runbook.md`

It documents:

- required ClickUp settings:
  - `CLICKUP_API_TOKEN`
  - `CLICKUP_LIST_ID`
- required Google Calendar settings:
  - `GOOGLE_CALENDAR_ACCESS_TOKEN`
  - `GOOGLE_CALENDAR_CALENDAR_ID`
  - `GOOGLE_CALENDAR_TIMEZONE`
- required Google Drive settings:
  - `GOOGLE_DRIVE_ACCESS_TOKEN`
  - `GOOGLE_DRIVE_FOLDER_ID`
- expected health transitions
- user opt-in requirements
- ClickUp mutation confirmation boundaries
- `PRJ-918` provider activation smoke expectations
- rollback

## Notes

No provider settings were changed in this task. `PRJ-918` remains blocked until
the operator configures credentials in the active deployment environment.
