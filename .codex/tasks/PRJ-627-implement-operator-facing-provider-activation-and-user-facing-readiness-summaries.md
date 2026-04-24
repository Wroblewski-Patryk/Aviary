# Task

## Header
- ID: PRJ-627
- Title: Implement operator-facing provider activation and user-facing readiness summaries
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-626
- Priority: P1

## Context
The current activation snapshot is useful but still mostly operator-oriented. The next step is to expose daily-use readiness more clearly for each provider and workflow.

## Goal
Expose a clearer daily-use readiness summary for organizer providers.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Existing backend surfaces expose clearer provider activation posture for daily use.
- [ ] Missing credentials, opt-in, and confirmation boundaries remain explicit.
- [ ] Regression coverage pins the richer readiness summary.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage
- Manual checks: `/health.connectors.organizer_tool_stack` and inspection/debug checks
- Screenshots/logs:
- High-risk checks: do not blur provider activation with automatic authorization or hidden execution

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/17_logging_and_debugging.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality/testing/ops likely

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
This should help the user quickly understand whether ClickUp/Calendar/Drive are truly ready for daily use.
