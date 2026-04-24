# Task

## Header
- ID: PRJ-601
- Title: Expose one actionable onboarding surface for organizer-tool activation
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-600
- Priority: P1

## Context
The organizer-tool stack already exposes provider readiness, but operators
still need to infer missing credentials and activation steps across multiple
per-provider fields.

## Goal
Expose one operator-facing activation snapshot for the frozen organizer-tool
stack through the existing health surface.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] `/health.connectors.organizer_tool_stack` includes one actionable activation snapshot
- [ ] activation snapshot records provider-specific credential gaps and next actions
- [ ] regression coverage pins the new activation snapshot contract

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_api_routes.py` -> `87 passed`
- Manual checks:
- Screenshots/logs:
- High-risk checks:
  - activation snapshot stays inside `organizer_tool_stack` instead of creating a parallel onboarding endpoint

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice should extend the existing organizer tool stack surface instead of
creating a second activation endpoint.
