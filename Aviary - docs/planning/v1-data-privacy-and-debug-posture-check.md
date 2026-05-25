# V1 Data Privacy And Debug Posture Check

Last updated: 2026-05-02

## Status

V1 data privacy and debug posture is acceptable for core no-UI v1, with
follow-up security hardening still queued for a broader public launch claim.

## Production Snapshot

- production URL:
  - `https://aviary.luckysparrow.ch`
- evaluated production revision:
  - `0535080786acaba9d3fe934a8b97f883ba37d406`
- local health snapshot evidence:
  - `.codex/artifacts/prj912-health-snapshot.json`

The health snapshot is generated evidence and is not committed.

## Debug Posture

Production `/health.runtime_policy` reports:

- `event_debug_enabled=false`
- `event_debug_admin_posture_state=debug_disabled_admin_route_primary_by_default`
- `event_debug_shared_ingress_posture=shared_route_break_glass_only`
- `event_debug_query_compat_enabled=false`
- `debug_token_policy_hint` remains policy-only and does not expose token
  values

Internal debug and inspection surfaces remain gated:

- `/internal/event/debug`
- `/internal/state/inspect`

Relevant regression evidence:

- disabled debug payload returns `403`
- invalid debug token returns `403`
- internal state inspection returns `403` when debug payload access is disabled

## Auth And Reset Boundaries

Regression coverage confirms:

- `/app/me` requires an authenticated session
- `/app/me/reset-data` requires authentication
- reset requires exact confirmation text: `RESET MY DATA`
- reset scope is `single_user_runtime_reset`
- reset revokes active app sessions
- reset preserves app settings required for the account shell

Chat and identity boundaries:

- authenticated app chat history uses the authenticated user
- linked Telegram turns may appear in the authenticated transcript only after
  explicit linking
- unlinked Telegram turns are excluded from authenticated app chat history
- personality overview uses the authenticated app user
- tools overview and tools preference mutations require authentication

## Payload Exposure Boundaries

Production health and incident-evidence posture expose policy and readiness
metadata, not raw provider payloads.

Observed safe fields:

- provider credential setting names may appear as missing-setting hints
- provider secret values do not appear
- `raw_payload_storage_allowed=false`
- planned/proactive raw payload exposure is counts-only
- website reading memory capture boundary is
  `tool_grounded_summary_only_via_action_then_memory`

Code inspection notes:

- settings values such as OpenAI and Telegram tokens are used for runtime
  clients and boolean readiness checks
- health surfaces expose configured/missing posture, not raw secret values
- `system_debug` payload is only included by debug routes after debug access
  enforcement
- strict-mode incident bundle export uses `/health` policy surfaces and does
  not include full `debug` or `system_debug`

## Validation

Commands:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "debug_payload or internal_state_inspection or app_reset_data or app_me_requires_authenticated_session or app_chat_history_excludes_unlinked_telegram_turns or app_personality_overview_uses_authenticated_user or app_tools_overview_requires_authenticated_session"; Pop-Location`
  - result: `23 passed, 96 deselected`
- production `/health` snapshot captured to:
  - `.codex/artifacts/prj912-health-snapshot.json`
- secret-value scan over the production health snapshot found setting names,
  policy hints, `system_debug` surface references, and raw-payload policy
  markers, but no secret values.

## Result

- Core no-UI v1 privacy/debug posture: GO
- Full public-launch security hardening: HOLD until:
  - `PRJ-931` V1 AI Red-Team Scenario Pack
  - `PRJ-932` Cross-User And Session Isolation Audit
  - `PRJ-933` Provider Payload Leakage Audit

## Next Step

Run production Telegram mode smoke (`PRJ-909`) if Telegram is the primary
launch channel, then continue with the AI/security hardening queue.
