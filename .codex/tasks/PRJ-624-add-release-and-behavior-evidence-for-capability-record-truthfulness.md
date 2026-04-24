# Task

## Header
- ID: PRJ-624
- Title: Add release and behavior evidence for capability-record truthfulness
- Status: BACKLOG
- Owner: QA/Test
- Depends on: PRJ-623
- Priority: P1

## Context
Once capability records are visible, evidence must prove that the backend truthfully distinguishes described guidance from executable/authorized behavior.

## Goal
Pin the capability-record truthfulness contract through regression and release evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Regression coverage proves catalog truthfulness semantics.
- [ ] Release or incident evidence consumes the same contract.
- [ ] Behavior-level proof exists for at least one described-versus-authorized distinction.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage
- Manual checks: release-smoke or incident-evidence checks
- Screenshots/logs:
- High-risk checks: avoid evidence that only checks shape while ignoring truthfulness semantics

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
The catalog must not imply that a durable skill description equals live tool authority.
