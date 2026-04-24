# Task

## Header
- ID: PRJ-625
- Title: Sync docs/context for the durable capability-record baseline
- Status: BACKLOG
- Owner: Product Docs Agent
- Depends on: PRJ-624
- Priority: P1

## Context
After role/skill/tool-authorization catalog truth is live, canonical docs and repository context must describe the same growth model and authorization boundary.

## Goal
Synchronize docs and context for durable capability records.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Architecture/runtime/testing/ops docs describe the same durable capability-record baseline.
- [ ] Planning docs and repository context reflect the same lane completion state.
- [ ] No older wording remains that suggests self-modifying executable skill learning.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: doc-and-context sync
- Manual checks: cross-review against runtime/evidence contract
- Screenshots/logs:
- High-risk checks: keep the truthful boundary between metadata, selection, authorization, and execution

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/03_identity_roles_skills.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: contracts/runtime reality/testing/ops/planning/context

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
This slice should make future UI/admin work easier by removing ambiguity from the docs.
