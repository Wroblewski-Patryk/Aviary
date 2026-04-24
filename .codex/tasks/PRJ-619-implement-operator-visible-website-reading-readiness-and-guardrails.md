# Task

## Header
- ID: PRJ-619
- Title: Implement operator-visible website-reading readiness and guardrails
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-618
- Priority: P0

## Context
The workflow needs runtime truth: what provider path is selected, what bounded page-read semantics are allowed, and what blocks live website reading in production.

## Goal
Expose one truthful readiness and guardrail surface for website reading.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Existing health/debug surfaces expose website-reading readiness and blocker posture.
- [ ] The same surfaces encode bounded read semantics and allowed provider path.
- [ ] Regression coverage pins the new guardrail contract.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage for API/runtime/deployment scripts as needed
- Manual checks: `/health.connectors` plus internal inspection/debug checks
- Screenshots/logs:
- High-risk checks: do not add a second browser/search subsystem outside connector/action ownership

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/17_logging_and_debugging.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality/testing/ops if visibility widens

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
The operator should be able to tell whether "read my site" is available, bounded, and safe.
