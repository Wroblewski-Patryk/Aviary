# Task

## Header
- ID: PRJ-628
- Title: Add end-to-end proof for organizer daily-use workflows
- Status: BACKLOG
- Owner: QA/Test
- Depends on: PRJ-627
- Priority: P1

## Context
Organizer-tool posture should be proven as practical daily-use behavior, not only as provider readiness or connector unit behavior.

## Goal
Prove the first daily-use organizer workflows end to end.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Behavior validation covers the selected organizer daily-use workflows.
- [ ] Release smoke or incident evidence proves the same acceptance posture.
- [ ] Regression coverage pins the relevant workflow surfaces.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage
- Manual checks: behavior-validation and release-smoke evidence
- Screenshots/logs:
- High-risk checks: prove realistic workflow posture without widening write authority beyond approved boundaries

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/29_runtime_behavior_testing.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing guidance and ops notes likely

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
The resulting evidence should answer "can the personality really help organize my life/work yet?".
