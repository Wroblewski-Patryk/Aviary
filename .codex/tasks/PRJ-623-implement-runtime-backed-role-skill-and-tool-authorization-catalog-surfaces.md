# Task

## Header
- ID: PRJ-623
- Title: Implement runtime-backed role, skill, and tool-authorization catalog surfaces
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-622
- Priority: P1

## Context
Future UI/admin and operator work need a truthful backend catalog of role presets, skill descriptions, and per-user tool authorization posture.

## Goal
Expose one runtime-backed catalog for durable capability records.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Existing health/inspection surfaces expose the capability-record catalog.
- [ ] The catalog distinguishes described, selectable, and authorized posture.
- [ ] Regression coverage pins the surfaced contract.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage
- Manual checks: `/health` and internal inspection checks
- Screenshots/logs:
- High-risk checks: keep execution authority in planning/action; do not create a parallel auth system

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
The desired outcome is a truthful backend catalog, not a new orchestrator.
