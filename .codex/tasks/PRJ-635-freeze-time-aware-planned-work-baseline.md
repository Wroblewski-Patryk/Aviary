# Task

## Header
- ID: PRJ-635
- Title: Freeze the time-aware planned-work baseline for core no-UI V1
- Status: READY
- Owner: Planning Agent
- Depends on: PRJ-631
- Priority: P0

## Context
The approved architecture change replaces a standalone reminder mindset with one
shared future-work model driven by planning, scheduler reevaluation, and the
existing action boundary.

## Goal
Freeze one canonical architecture baseline where planned future work is part of
core no-UI `v1`, while organizer-tool activation remains a later extension.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Canonical architecture docs define planned future work as an extension of internal planning state.
- [ ] Core no-UI `v1` closure no longer depends on organizer-tool credentials.
- [ ] Planning/context truth seeds the next implementation queue from this revised baseline.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: architecture and planning cross-review
- Manual checks: compare revised v1 definition across architecture and planning docs
- Screenshots/logs:
- High-risk checks: do not keep organizer tooling as a hidden blocker for core `v1` after this revision

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/10_future_vision.md`, `docs/architecture/15_runtime_flow.md`, `docs/architecture/16_agent_contracts.md`, `docs/architecture/12_data_model.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: user-approved revision on 2026-04-24 for time-aware planned work as part of core `v1`
- Follow-up architecture doc updates: planning/context truth and later runtime/testing/ops docs

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
This slice is architectural and planning-first by design.
