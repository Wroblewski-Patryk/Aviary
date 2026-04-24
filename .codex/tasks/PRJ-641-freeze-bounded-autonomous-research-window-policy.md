# Task

## Header
- ID: PRJ-641
- Title: Freeze the bounded autonomous research-window policy
- Status: BACKLOG
- Owner: Planning Agent
- Depends on: PRJ-640
- Priority: P1

## Context
The user wants the personality to eventually use spare scheduler windows for
bounded internet learning. That must stay architecture-aligned and
tool-grounded rather than becoming uncontrolled autonomous browsing.

## Goal
Freeze one bounded policy for research windows on top of planned work.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Research windows are defined as planned-work variants, not a separate autonomy engine.
- [ ] Approved triggers, limits, and safety boundaries are explicit.
- [ ] The policy stays compatible with bounded search/browser tools and tool-grounded learning.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: architecture/product/ops cross-review
- Manual checks: compare policy against action-boundary and tool-grounded-learning rules
- Screenshots/logs:
- High-risk checks: avoid uncontrolled internet exploration claims

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/10_future_vision.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: planning/context and later runtime/testing/ops docs

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
This task is intentionally policy-first and should stay bounded to approved tool families.
