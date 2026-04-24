# Task

## Header
- ID: PRJ-620
- Title: Add behavior and release proof for live web-knowledge workflows
- Status: READY
- Owner: QA/Test
- Depends on: PRJ-619
- Priority: P0

## Context
Once website-reading readiness is live, release and behavior proof must show that the personality can actually use bounded web knowledge in the intended way.

## Goal
Prove the bounded website-reading workflow through tests and release evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Behavior validation covers at least one bounded website-reading scenario.
- [ ] Release smoke proves the same website-reading contract from runtime truth.
- [ ] Regression coverage pins the key workflow surfaces.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage
- Manual checks: behavior-validation and release-smoke evidence
- Screenshots/logs:
- High-risk checks: prove the workflow without widening provider payload exposure or bypassing planning/action

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
The target scenario should feel like a real user request, not only a provider-unit test.
