# Task

## Header
- ID: PRJ-600
- Title: Freeze the production credential-activation baseline for organizer tools
- Status: DONE
- Owner: Planner
- Depends on: PRJ-599
- Priority: P0

## Context
The first production organizer-tool stack is already behavior-proven and
machine-visible, but production still needs one explicit activation baseline
for provider credentials, opt-ins, and confirmation posture before the stack
can be treated as truly live.

## Goal
Freeze one operator-facing production activation baseline for the ClickUp,
Google Calendar, and Google Drive organizer stack.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] canonical docs record the required provider credentials for the first organizer stack
- [x] docs distinguish read-only activation from mutate-with-confirmation activation
- [x] planning/context truth points to the next activation slice after the frozen baseline

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
  - cross-review of architecture contract, env/config guidance, runbook, and planning/context truth
- Screenshots/logs:
- High-risk checks:
  - ClickUp mutation paths stay confirmation-bound
  - Calendar and Drive remain bounded read-only activation targets

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/26_env_and_config.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice intentionally freezes the operator baseline only. Actual actionable
activation surfaces belong to `PRJ-601`.
