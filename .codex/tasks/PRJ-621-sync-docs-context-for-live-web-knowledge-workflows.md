# Task

## Header
- ID: PRJ-621
- Title: Sync docs/context for live web-knowledge workflows
- Status: BACKLOG
- Owner: Product Docs Agent
- Depends on: PRJ-620
- Priority: P1

## Context
After website-reading becomes a named production workflow with evidence, docs and context must describe the same user-facing truth.

## Goal
Synchronize runtime reality, testing, ops, and planning/context for the live web-knowledge workflow.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Canonical docs reflect the website-reading workflow baseline.
- [ ] Runtime reality/testing/ops reflect the same proof path.
- [ ] Repository context reflects the same lane completion state.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: doc-and-context sync
- Manual checks: cross-review against runtime truth and behavior/release evidence
- Screenshots/logs:
- High-risk checks: avoid mixing website-reading baseline with future unrestricted browsing claims

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
This slice should make it obvious to a later UI/admin layer what "website reading" actually means in `v1`.
