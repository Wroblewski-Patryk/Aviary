# Task

## Header
- ID: PRJ-629
- Title: Sync docs/context for organizer daily-use activation
- Status: BACKLOG
- Owner: Product Docs Agent
- Depends on: PRJ-628
- Priority: P1

## Context
Once organizer tools are framed as daily-use helpers rather than just provider-ready connectors, the same truth must be reflected across docs and context.

## Goal
Synchronize docs/context for organizer daily-use activation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Runtime reality/testing/ops docs describe the daily-use organizer baseline.
- [ ] Planning/context reflects the same lane completion state.
- [ ] Older wording that treats the stack as only abstract provider readiness is removed or updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: doc-and-context sync
- Manual checks: cross-review against workflow evidence
- Screenshots/logs:
- High-risk checks: keep the boundary between internal planning state and external tools explicit

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/10_future_vision.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality/testing/runbook/planning/context

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
This is the close-out slice for the organizer daily-use lane.
