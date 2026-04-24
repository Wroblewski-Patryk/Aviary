# Task

## Header
- ID: PRJ-622
- Title: Freeze the durable capability-record baseline
- Status: BACKLOG
- Owner: Planning Agent
- Depends on: PRJ-621
- Priority: P1

## Context
Architecture now allows durable role presets, durable skill descriptions, and per-user tool authorization records. The runtime still needs one explicit baseline for how these records exist truthfully without widening execution authority.

## Goal
Freeze one bounded capability-record contract for roles, skills, and tool authorization.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] One explicit bounded capability-record contract is documented.
- [ ] The contract distinguishes description, selection, and authorization.
- [ ] Planning docs and context agree on that boundary.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks: architecture/product cross-review
- Screenshots/logs:
- High-risk checks: do not imply self-modifying executable skill learning or hidden tool authorization

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/03_identity_roles_skills.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: contracts/planning/context if wording is refined

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
This task sets the truthful growth model for "what the personality has learned" versus "what it can actually execute".
