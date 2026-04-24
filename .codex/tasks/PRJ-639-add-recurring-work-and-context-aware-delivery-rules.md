# Task

## Header
- ID: PRJ-639
- Title: Add recurring work and context-aware delivery rules
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-638
- Priority: P1

## Context
The planned-work model should support routines and recurring follow-ups without
becoming a second scheduler or a simplistic reminder engine.

## Goal
Add recurring planned-work semantics plus context-aware delivery rules such as
quiet hours, not-before windows, and skip-versus-delay posture.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Recurring planned work is represented as bounded data plus reevaluation rules.
- [ ] Delivery can be delayed, skipped, or handed off based on context and policy.
- [ ] The system remains explainable through explicit state and policy surfaces.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted scheduler/planning/runtime coverage
- Manual checks: verify recurring work does not create a parallel scheduler
- Screenshots/logs:
- High-risk checks: avoid hidden autonomous delivery loops

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
The goal is time-aware reasoning, not a generic calendar product.
