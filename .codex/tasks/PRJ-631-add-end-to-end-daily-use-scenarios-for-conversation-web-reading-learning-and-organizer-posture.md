# Task

## Header
- ID: PRJ-631
- Title: Add end-to-end daily-use scenarios for conversation, web reading, learning, and organizer posture
- Status: BACKLOG
- Owner: QA/Test
- Depends on: PRJ-630
- Priority: P0

## Context
The final acceptance bundle needs scenario-level proof that the personality behaves like a usable daily assistant, not just a healthy runtime with many separate proofs.

## Goal
Add final end-to-end no-UI `v1` daily-use scenarios.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Behavior validation covers final daily-use `v1` scenarios.
- [ ] The scenarios include conversation, website reading, bounded learning reuse, and organizer help.
- [ ] Evidence is suitable for final no-UI `v1` acceptance.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage
- Manual checks: behavior-validation evidence
- Screenshots/logs:
- High-risk checks: keep scenarios within approved provider/tool boundaries and truthful learning semantics

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/29_runtime_behavior_testing.md`, `docs/architecture/10_future_vision.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing guidance and possibly product docs

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
The target is a believable "this personality can help me today" scenario set.
