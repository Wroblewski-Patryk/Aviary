# Task

## Header
- ID: PRJ-636
- Title: Add the durable planned-work contract and storage shape
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-635
- Priority: P0

## Context
Core no-UI `v1` now requires time-aware planned future work. The runtime needs
one explicit durable model for future work items before scheduler reevaluation
or user-visible delivery can stay architecture-aligned.

## Goal
Add the planned-work contract and durable storage shape without creating a
parallel reminder subsystem.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] A durable planned-work entity exists in the runtime contract and storage model.
- [ ] Planning can express create, reschedule, cancel, and complete intents for planned work.
- [ ] The new model remains explicitly internal-first and action-owned for durable writes.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted repository/model/contract coverage
- Manual checks: verify no second reminder subsystem was introduced
- Screenshots/logs:
- High-risk checks: avoid hidden side-effect ownership outside action

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/12_data_model.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality, testing, ops notes

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
This task should extend existing goal/task/proactive ownership rather than fork it.
