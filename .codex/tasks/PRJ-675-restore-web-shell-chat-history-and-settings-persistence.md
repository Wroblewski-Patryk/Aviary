# Task

## Header
- ID: PRJ-675
- Title: Restore web-shell chat history and settings persistence through the app-facing backend contract
- Status: READY
- Owner: Backend Builder
- Depends on:
- Priority: P0

## Context
Fresh production validation of `https://personality.luckysparrow.ch/` proved
that register, login, logout, and live chat replies work, but the first-party
web shell still has two backend-owned product blockers. `GET /app/chat/history`
returns `500`, leaving the continuity panel empty, and
`PATCH /app/me/settings` returns `500`, so the settings screen cannot persist
user-owned changes through the intended app-facing flow.

## Goal
Restore both app-facing backend paths so the current web shell can truthfully
read recent conversation state and persist user settings without changing the
approved `/app/*` boundary.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] `GET /app/chat/history` returns `200` for an authenticated user and the
      payload matches the existing contract.
- [ ] `PATCH /app/me/settings` persists values and returns the expected
      settings payload without introducing a parallel settings path.
- [ ] Targeted backend regression coverage protects both routes and their
      current production failure mode.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
- Screenshots/logs:
- High-risk checks:

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md;
  docs/architecture/26_env_and_config.md; docs/architecture/29_runtime_behavior_testing.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## Review Checklist (mandatory)
- [ ] Architecture alignment confirmed.
- [ ] Existing systems were reused where applicable.
- [ ] No workaround paths were introduced.
- [ ] No logic duplication was introduced.
- [ ] Definition of Done evidence is attached.
- [ ] Relevant validations were run.
- [ ] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Production evidence is captured in
`.codex/artifacts/ui-prod-test-2026-04-25/result.json`.
