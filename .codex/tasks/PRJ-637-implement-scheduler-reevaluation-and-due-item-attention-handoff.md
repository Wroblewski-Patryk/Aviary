# Task

## Header
- ID: PRJ-637
- Title: Implement scheduler reevaluation and due-item attention handoff
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-636
- Priority: P0

## Context
Time-aware planned work needs a scheduler-owned reevaluation path that can wake
foreground cognition without sending messages directly.

## Goal
Implement background reevaluation of planned work and convert due items into
attention or proposal handoffs for foreground processing.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] External scheduler cadence reevaluates planned work with current time and context.
- [ ] Due items enter the existing attention or proposal boundary instead of bypassing it.
- [ ] Background ownership remains side-effect-free with respect to user-visible delivery.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted scheduler/runtime attention coverage
- Manual checks: verify due work reaches foreground through the canonical handoff path
- Screenshots/logs:
- High-risk checks: avoid direct Telegram/API delivery from background cadence

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/15_runtime_flow.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality and runbook

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
The important boundary is reevaluate in background, deliver in foreground.
