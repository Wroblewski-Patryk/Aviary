# Task

## Header
- ID: PRJ-638
- Title: Implement foreground delivery for due planned work
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-637
- Priority: P0

## Context
Once due work reaches attention, foreground runtime should treat it as a normal
planning and action problem instead of special-casing reminder delivery.

## Goal
Implement canonical foreground handling for due planned work through planning,
expression, and action.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Due planned work can result in a Telegram or API follow-up through the existing foreground path.
- [ ] Completion, snooze, and cancellation semantics remain explicit state transitions.
- [ ] No direct delivery path exists outside planning -> expression -> action.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted runtime pipeline and action coverage
- Manual checks: verify due work produces normal foreground turn artifacts
- Screenshots/logs:
- High-risk checks: do not let planned work bypass the action boundary

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/15_runtime_flow.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing and ops notes

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
This is still internal-first planning state; organizer sync remains a later extension.
