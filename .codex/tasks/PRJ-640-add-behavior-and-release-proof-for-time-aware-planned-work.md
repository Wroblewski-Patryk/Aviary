# Task

## Header
- ID: PRJ-640
- Title: Add behavior and release proof for time-aware planned work
- Status: BACKLOG
- Owner: QA/Test
- Depends on: PRJ-639
- Priority: P0

## Context
Core no-UI `v1` cannot claim time-aware planning honestly unless due work,
follow-up delivery, and recurring reevaluation are proven through behavior and
release evidence.

## Goal
Add behavior-validation, health, and release-smoke proof for time-aware planned
work.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Behavior scenarios prove due-item delivery through foreground execution.
- [ ] Health or incident-evidence surfaces expose planned-work posture.
- [ ] Release smoke validates the same planned-work contract.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest, behavior validation, release smoke
- Manual checks: production or local smoke review as appropriate
- Screenshots/logs:
- High-risk checks: do not close core `v1` on repo-only proof if release evidence drifts

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/17_logging_and_debugging.md`, `docs/architecture/29_runtime_behavior_testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing, ops, planning/context

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
This is the acceptance lane for time-aware planned work as a core `v1` capability.
