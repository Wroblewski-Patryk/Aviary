# Task

## Header
- ID: PRJ-680
- Title: Sync web stabilization docs, context, and ops truth after the repairs
- Status: READY
- Owner: Product Docs Agent
- Depends on: PRJ-679
- Priority: P1

## Context
The next lane is product-facing stabilization work. Once the broken routes,
client truthfulness, and proof surfaces are repaired, repo truth must be
updated in the same cycle so later work starts from a stable documented
baseline instead of rediscovering the same issues.

## Goal
Synchronize planning, context, testing, and ops truth with the repaired web
production baseline.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Task board and project state reflect the repaired stabilization lane.
- [ ] Testing and ops docs describe the current smoke and acceptance evidence.
- [ ] Learning journal captures any confirmed recurring pitfall discovered
      during the repair wave.

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
- Architecture source reviewed: docs/architecture/17_logging_and_debugging.md;
  docs/engineering/testing.md; docs/operations/runtime-ops-runbook.md
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
This task closes the lane only after repaired product truth is documented.
