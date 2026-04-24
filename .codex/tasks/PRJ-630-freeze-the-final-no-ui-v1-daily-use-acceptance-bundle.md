# Task

## Header
- ID: PRJ-630
- Title: Freeze the final no-UI V1 daily-use acceptance bundle
- Status: BACKLOG
- Owner: Planning Agent
- Depends on: PRJ-629
- Priority: P0

## Context
After deploy truth, website-reading, capability records, and organizer daily-use lanes are settled, the repo needs one explicit final acceptance contract for no-UI `v1`.

## Goal
Define the final daily-use acceptance bundle for no-UI `v1`.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] One explicit acceptance bundle records all final no-UI `v1` gates.
- [ ] The bundle names the exact runtime, evidence, and scenario surfaces.
- [ ] Planning docs and context agree on the same closure contract.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks: product/runtime/ops cross-review
- Screenshots/logs:
- High-risk checks: do not redefine `v1`; express closure using existing approved backend truth and evidence systems

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/10_future_vision.md`, `docs/architecture/17_logging_and_debugging.md`, `docs/architecture/29_runtime_behavior_testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: planning/context and possibly product docs

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
This should be the contract that finally lets us say "`v1` is real for daily use".
