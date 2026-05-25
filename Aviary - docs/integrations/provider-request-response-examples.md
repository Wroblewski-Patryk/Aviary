# Provider Request/Response Examples

Last updated: 2026-05-03
Task: `PRJ-964`

## Purpose

This document records sanitized request/response shapes for provider-backed
operations that exist in the current codebase. It is not live-smoke evidence and
does not prove credentials are configured in production.

Use this reference to review provider boundaries without exposing secrets,
provider raw payload bodies, or private user data.

## Sanitization Rules

- Tokens are represented as `<REDACTED_TOKEN>`.
- External IDs are synthetic, for example `<CLICKUP_LIST_ID>`.
- User-owned task names, file names, and calendar windows are examples only.
- Raw provider payload bodies are not copied into app-facing examples.
- Failure examples show the app/provider boundary state, not secret values.

## ClickUp Task Creation

Code owner:

- `backend/app/integrations/task_system/clickup_client.py`
- `backend/app/core/action.py`

Operation:

- connector operation: `task_system.create_task`
- action: `clickup_create_task`
- mode: `mutate_with_confirmation`
- confirmation required: yes
- readiness settings: `CLICKUP_API_TOKEN`, `CLICKUP_LIST_ID`

Provider request:

```http
POST https://api.clickup.com/api/v2/list/<CLICKUP_LIST_ID>/task
Authorization: <REDACTED_TOKEN>
Content-Type: application/json

{
  "name": "Prepare v1 release checklist",
  "description": "Sanitized task description written after explicit confirmation."
}
```

Sanitized provider success shape:

```json
{
  "id": "clk_task_123",
  "name": "Prepare v1 release checklist",
  "status": {
    "status": "to do"
  },
  "url": "https://app.clickup.com/t/clk_task_123"
}
```

App/action output shape:

```json
{
  "status": "success",
  "actions": ["clickup_create_task"],
  "notes": "ClickUp task created (clk_task_123) for 'Prepare v1 release checklist'."
}
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["clickup_create_task"],
  "notes": "ClickUp task execution failed: HTTPStatusError: <sanitized provider error>"
}
```

## ClickUp Task Listing

Operation:

- connector operation: `task_system.list_tasks`
- action: `clickup_list_tasks`
- mode: `read_only`
- confirmation required: no
- readiness settings: `CLICKUP_API_TOKEN`, `CLICKUP_LIST_ID`

Provider request:

```http
GET https://api.clickup.com/api/v2/list/<CLICKUP_LIST_ID>/task?page=0
Authorization: <REDACTED_TOKEN>
Content-Type: application/json
```

Sanitized provider success shape:

```json
{
  "tasks": [
    {
      "id": "clk_task_123",
      "name": "Release checklist",
      "status": {
        "status": "in progress"
      }
    },
    {
      "id": "clk_task_456",
      "name": "Docs sync",
      "status": {
        "status": "to do"
      }
    }
  ]
}
```

App/action output shape:

```json
{
  "status": "success",
  "actions": ["clickup_list_tasks"],
  "notes": "ClickUp task read returned: Release checklist, Docs sync."
}
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["clickup_list_tasks"],
  "notes": "ClickUp task read failed: HTTPStatusError: <sanitized provider error>"
}
```

## ClickUp Task Update

Operation:

- connector operation: `task_system.update_task`
- action: `clickup_update_task`
- mode: `mutate_with_confirmation`
- confirmation required: yes
- readiness settings: `CLICKUP_API_TOKEN`, `CLICKUP_LIST_ID`

Provider request:

```http
PUT https://api.clickup.com/api/v2/task/<CLICKUP_TASK_ID>
Authorization: <REDACTED_TOKEN>
Content-Type: application/json

{
  "status": "complete"
}
```

Sanitized provider success shape:

```json
{
  "id": "clk_task_123",
  "name": "Release checklist",
  "status": {
    "status": "complete"
  }
}
```

App/action output shape:

```json
{
  "status": "success",
  "actions": ["clickup_update_task"],
  "notes": "ClickUp task updated (clk_task_123) for 'Release checklist' with status 'complete'."
}
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["clickup_update_task"],
  "notes": "ClickUp task update failed: HTTPStatusError: <sanitized provider error>"
}
```

## Google Calendar Availability

Code owner:

- `backend/app/integrations/calendar/google_calendar_client.py`
- `backend/app/core/action.py`

Operation:

- connector operation: `calendar.read_availability`
- action: `google_calendar_read_availability`
- mode: `read_only`
- confirmation required: no
- readiness settings:
  - `GOOGLE_CALENDAR_ACCESS_TOKEN`
  - `GOOGLE_CALENDAR_CALENDAR_ID`
  - `GOOGLE_CALENDAR_TIMEZONE`

Provider request:

```http
POST https://www.googleapis.com/calendar/v3/freeBusy
Authorization: Bearer <REDACTED_TOKEN>
Content-Type: application/json

{
  "timeMin": "2026-05-04T08:00:00+00:00",
  "timeMax": "2026-05-04T18:00:00+00:00",
  "timeZone": "Europe/Warsaw",
  "items": [
    {
      "id": "<GOOGLE_CALENDAR_ID>"
    }
  ]
}
```

Sanitized provider success shape:

```json
{
  "calendars": {
    "<GOOGLE_CALENDAR_ID>": {
      "busy": [
        {
          "start": "2026-05-04T09:00:00Z",
          "end": "2026-05-04T10:00:00Z"
        }
      ]
    }
  }
}
```

App/action output shape:

```json
{
  "status": "success",
  "actions": ["google_calendar_read_availability"],
  "notes": "Google Calendar availability read returned 1 busy window and 3 candidate free slots."
}
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["google_calendar_read_availability"],
  "notes": "Google Calendar availability read failed: HTTPStatusError: <sanitized provider error>"
}
```

## Google Drive Metadata Listing

Code owner:

- `backend/app/integrations/cloud_drive/google_drive_client.py`
- `backend/app/core/action.py`

Operation:

- connector operation: `cloud_drive.list_files`
- action: `google_drive_list_files`
- mode: `read_only`
- confirmation required: no
- readiness settings:
  - `GOOGLE_DRIVE_ACCESS_TOKEN`
  - `GOOGLE_DRIVE_FOLDER_ID` optional scope limiter

Provider request:

```http
GET https://www.googleapis.com/drive/v3/files?pageSize=5&fields=files(id,name,mimeType,modifiedTime),nextPageToken&orderBy=modifiedTime%20desc&q=trashed%20%3D%20false%20and%20%27<GOOGLE_DRIVE_FOLDER_ID>%27%20in%20parents
Authorization: Bearer <REDACTED_TOKEN>
```

Sanitized provider success shape:

```json
{
  "files": [
    {
      "id": "drive_file_123",
      "name": "Release notes",
      "mimeType": "application/vnd.google-apps.document",
      "modifiedTime": "2026-05-03T09:30:00.000Z"
    }
  ]
}
```

App/action output shape:

```json
{
  "status": "success",
  "actions": ["google_drive_list_files"],
  "notes": "Google Drive metadata read returned: Release notes (application/vnd.google-apps.document, 2026-05-03T09:30:00.000Z)."
}
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["google_drive_list_files"],
  "notes": "Google Drive metadata read failed: HTTPStatusError: <sanitized provider error>"
}
```

## DuckDuckGo Knowledge Search

Code owner:

- `backend/app/integrations/knowledge_search/duckduckgo_client.py`
- `backend/app/core/action.py`

Operation:

- connector operation: `knowledge_search.search_web`
- action: `duckduckgo_search_web`
- mode: `read_only`
- confirmation required: no
- readiness settings: none

Provider request:

```http
GET https://html.duckduckgo.com/html/?q=Aviary%20release%20notes
```

Sanitized provider result shape:

```json
[
  {
    "title": "Aviary release notes",
    "url": "https://example.com/release-notes",
    "snippet": "A bounded search-result snippet.",
    "rank": "1"
  }
]
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["duckduckgo_search_web"],
  "notes": "Web search failed: HTTPStatusError: <sanitized provider error>"
}
```

## Generic HTTP Page Read

Code owner:

- `backend/app/integrations/web_browser/generic_http_client.py`
- `backend/app/core/action.py`

Operation:

- connector operation: `web_browser.read_page`
- action: `generic_http_read_page`
- mode: `read_only`
- confirmation required: no
- readiness settings: none

Provider request:

```http
GET https://example.com/release-notes
```

Sanitized provider result shape:

```json
{
  "url": "https://example.com/release-notes",
  "title": "Release notes",
  "content_type": "text/html",
  "excerpt": "A bounded excerpt extracted from page text.",
  "truncated": "false"
}
```

Failure shape:

```json
{
  "status": "failed",
  "actions": ["generic_http_read_page"],
  "notes": "Browser page read failed: HTTPStatusError: <sanitized provider error>"
}
```

## Credential-Missing Boundary

When required settings are absent, provider-backed operations must not attempt
external calls. They should stay at the action/integration boundary and report a
provider-not-ready posture.

Representative app/action shape:

```json
{
  "status": "skipped",
  "actions": ["provider_not_ready"],
  "notes": "Provider-backed connector execution is not configured for this operation."
}
```

This shape is intentionally generic because provider-specific secrets and raw
provider errors must not be exposed in app surfaces.

## Related Evidence

- [Provider Integration Reference](index.md)
- [Provider Payload Leakage Audit](../security/v1-provider-payload-leakage-audit.md)
- [Organizer Provider Activation Runbook](../operations/organizer-provider-activation-runbook.md)
- `backend/tests/test_action_executor.py`
- `backend/tests/test_runtime_pipeline.py`
- `backend/tests/test_api_routes.py`
