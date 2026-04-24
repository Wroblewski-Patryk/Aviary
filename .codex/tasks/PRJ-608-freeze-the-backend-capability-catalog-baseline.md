# Task

## Header
- ID: PRJ-608
- Title: Freeze the backend capability-catalog baseline
- Status: DONE
- Owner: Planner
- Depends on: PRJ-607
- Priority: P1

## Context
Tool-grounded learning, organizer-tool activation, deployment provenance, and
learned-state introspection are now machine-visible, but future UI or admin
work still lacks one explicit backend contract for how capability truth should
be read without reconstructing it client-side from scattered surfaces.

## Goal
Freeze one explicit backend capability-catalog contract for future UI and
admin callers by reusing existing health, internal inspection, role-skill, and
connector surfaces instead of introducing a parallel system.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] canonical architecture defines one bounded backend capability-catalog contract
- [x] the contract records which existing backend surfaces are canonical inputs
- [x] the contract keeps skills metadata-only and tools action-owned
- [x] planning/context truth is synchronized around the frozen baseline

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
  - architecture/product cross-review against `docs/architecture/02_architecture.md`
    and `docs/architecture/16_agent_contracts.md`
  - contract cross-review against existing backend inputs in
    `app/core/api_readiness_policy.py`, `app/core/role_skill_policy.py`, and
    `app/core/skill_registry.py`
- Screenshots/logs:
- High-risk checks:
  - capability catalog remains an aggregation contract over existing backend
    truth and does not become a second authorization or execution system

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/16_agent_contracts.md`
  - `app/core/api_readiness_policy.py`
  - `app/core/role_skill_policy.py`
  - `app/core/skill_registry.py`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - synchronized in this task for contract wording only; backend surface
    implementation remains in `PRJ-609`

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This task freezes only the contract. `PRJ-609` remains the execution slice that
should expose one backend capability-catalog payload by composing existing
backend-owned surfaces.
