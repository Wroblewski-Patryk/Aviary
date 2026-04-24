# Task

## Header
- ID: PRJ-626
- Title: Freeze the daily-use organizer workflow baseline
- Status: BACKLOG
- Owner: Planning Agent
- Depends on: PRJ-625
- Priority: P1

## Context
Organizer-tool stack is already frozen technically, but the product still needs one explicit daily-use baseline that feels real to the user.

## Goal
Define the first daily-use organizer workflows for ClickUp, Calendar, and Drive.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] One explicit daily-use organizer workflow set is documented.
- [ ] The workflow set names provider boundaries, opt-ins, and confirmation posture.
- [ ] Planning docs and context agree on the same baseline.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks: architecture/product/ops cross-review
- Screenshots/logs:
- High-risk checks: keep internal planning state primary and external tools action-owned

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/10_future_vision.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: likely contracts/runtime reality if wording is tightened

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
Examples should include task review/update, availability inspection, and file listing as bounded daily-use helpers.
