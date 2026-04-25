# Task

## Header
- ID: PRJ-677
- Title: Fix Tools and Personality route loading lifecycle in the web shell
- Status: READY
- Owner: Frontend Builder
- Depends on: PRJ-676
- Priority: P0

## Context
Production validation shows that `/app/tools/overview` and
`/app/personality/overview` return `200`, but the corresponding `Tools` and
`Personality` routes remain on loading and never render their payload. Current
client analysis shows the route lifecycle cancels its own request path before
the successful payload is committed.

## Goal
Make both routes load, finish, and render backend truth reliably when entered
through the normal browser navigation flow.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] `Tools` renders grouped backend payload instead of remaining on a
      spinner when `/app/tools/overview` succeeds.
- [ ] `Personality` renders overview sections instead of remaining on a
      spinner when `/app/personality/overview` succeeds.
- [ ] Loading, cancellation, and re-entry behavior are covered by focused web
      regressions.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
- Screenshots/logs:
- High-risk checks:

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md;
  docs/architecture/29_runtime_behavior_testing.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

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
The fix should preserve the current thin-client posture over backend-owned
contracts.
