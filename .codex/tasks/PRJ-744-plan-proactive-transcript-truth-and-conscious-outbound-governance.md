# Task

## Header
- ID: PRJ-744
- Title: Plan proactive transcript truth and conscious outbound governance
- Task Type: research
- Current Stage: planning
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-717
- Priority: P0

## Context
Production analysis showed that scheduler-owned proactive ticks currently write
`time check-in follow up` into episodic memory and the app transcript projects
that system-originated event as a `role=user` message. This creates two
problems at once:

- user-visible false history in chat/transcript surfaces
- proactive cadence can appear to "speak first" even when the conscious path
  should decide that no outward message is needed

The approved product direction from the user now clarifies the intended
communication rule:

- user-initiated contact must always receive an outward reply on the same
  source, even if minimal
- subconscious or scheduler wakeups may trigger conscious analysis without any
  required user-visible delivery
- proactive delivery should happen only when conscious evaluation concludes
  there is real value in relation-maintaining outreach
- cross-channel escalation after no answer is desired conceptually, but it has
  non-obvious architecture and UX consequences and therefore remains an
  explicit decision gate before implementation

## Goal
Produce an execution-ready repair plan that restores transcript truth,
stabilizes proactive outbound behavior, and protects the conscious versus
subconscious communication boundary without introducing regressions in planned
work, scheduler cadence, or shared chat continuity.

## Deliverable For This Stage
Produce:

- one planning document in `docs/planning/`
- one synced task-board and project-state update
- one explicit execution queue with implementation, regression, and docs tasks
- one explicit decision gate for multi-channel escalation before implementation

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] A concrete repair plan exists for transcript truth and proactive outbound governance.
- [x] The plan separates guaranteed fixes from unresolved architecture decisions.
- [x] Source-of-truth context files point to the same next execution slice.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - not run; planning-only slice
- Manual checks:
  - runtime/architecture/code-path review for scheduler, proactive, transcript,
    and delivery routing
- Screenshots/logs:
  - user-provided production transcript evidence on 2026-04-26
- High-risk checks:
  - confirmed the literal `time check-in follow up` source in
    `backend/app/memory/repository.py`
  - confirmed transcript projection currently maps scheduler-originated `event`
    payloads to `role=user`
  - confirmed Coolify production defaults proactive cadence to enabled every
    1800 seconds

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: yes
- Decision required from user: yes
- Approval reference if architecture changed:
  - none; planning only
- Follow-up architecture doc updates:
  - clarify user-visible communication rule for user-originated turns versus
    scheduler or subconscious wakeups
  - clarify whether cross-channel proactive escalation becomes approved action
    behavior or remains future scope

## UX/UI Evidence (required for UX tasks)
- Design source type:
  - not applicable
- Design source reference:
  - not applicable
- Stitch used: no
- Experience-quality bar reviewed: no
- Visual-direction brief reviewed: no
- Existing shared pattern reused:
  - existing transcript contract and runtime pipeline
- New shared pattern introduced: no
- Design-memory entry reused:
  - not applicable
- Design-memory update required: no
- State checks:
  - success
- Responsive checks:
  - not applicable
- Input-mode checks:
  - not applicable
- Accessibility checks:
  - not applicable
- Parity evidence:
  - not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes:
  - none in planning stage
- Health-check impact:
  - future work should keep `/health.proactive`, scheduler evidence, and
    transcript behavior aligned
- Smoke steps updated:
  - not yet; execution stage
- Rollback note:
  - not applicable in planning stage

## Review Checklist (mandatory)
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
- Decision gate for implementation:
  - multi-channel escalation after silence has real tradeoffs around user
    trust, duplicated outreach, and channel-preference ownership
  - the execution plan therefore includes explicit options rather than
    assuming one final behavior without confirmation
