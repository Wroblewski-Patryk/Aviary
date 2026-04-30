# Task

## Header
- ID: PRJ-821
- Title: Freeze Canonical 100 Slice Closure Map
- Task Type: design
- Current Stage: implementation
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-820
- Priority: P1

## Context
The project now has multiple flagship parity lanes and enough history that
random polishing risks reopening already-visited surfaces. A single execution
map is needed so future visual work stays bounded and ordered.

## Goal
Freeze a single 100-slice flagship closure map that preserves the approved
surface order and parity gates.

## Success Signal
- User or operator problem:
  - visual work can drift across too many surfaces without one clear closure
    backlog
- Expected product or reliability outcome:
  - every future flagship UX/UI slice can be mapped to one numbered closure
    step
- How success will be observed:
  - repo contains one explicit 100-slice execution map and context points to it
- Post-launch learning needed: no

## Deliverable For This Stage
One planning document plus context synchronization.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Scope
- `docs/planning/canonical-100-slice-closure-map.md`
- `.codex/tasks/PRJ-821-freeze-canonical-100-slice-closure-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Freeze a numbered 100-slice execution map covering `home`, shared shell,
   sidebar, `dashboard`, `chat`, `personality`, and final cross-surface proof.
2. Keep slice ordering aligned with the approved one-surface-at-a-time parity
   workflow.
3. Record the map in task board and project state.
4. Run focused diff validation.

## Acceptance Criteria
- 100 slices are numbered and grouped by surface
- closure order is explicit
- context points to the new plan
- focused diff validation passes

## Definition of Done
- [x] planning document created
- [x] task board updated
- [x] project state updated
- [x] focused validation recorded

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
  - `git diff --check -- docs/planning/canonical-100-slice-closure-map.md .codex/tasks/PRJ-821-freeze-canonical-100-slice-closure-map.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- Manual checks:
  - reviewed closure order against `docs/ux/canonical-visual-implementation-workflow.md`
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - no implementation scope mixed into the planning-only slice

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/ux/canonical-visual-implementation-workflow.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: canonical web screen-set in `docs/ux/`
- Canonical visual target: flagship web surfaces
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: one-surface-at-a-time closure workflow
- New shared pattern introduced: no
- Design-memory entry reused: yes
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: not applicable in planning-only slice
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: implementation still required
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence:

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: delete planning doc if superseded
- Observability or alerting impact: none
- Staged rollout or feature flag: no

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
The map is a closure device, not a promise that every surface will necessarily
consume all provisional slices before meeting its parity gate.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. Partial implementations, mock-only
paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: UX/UI implementation workflow
- Existing workaround or pain: too many micro-passes can fragment closure
- Smallest useful slice: one numbered closure map
- Success metric or signal: one plan can guide the next flagship slice without re-auditing from zero
- Feature flag, staged rollout, or disable path: no
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: not applicable
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: not applicable
- Rollback or disable path: remove or supersede the planning document

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused diff validation

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: none
- Trust boundaries: unchanged
- Permission or ownership checks: not applicable
- Abuse cases: not applicable
- Secret handling: none
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: low

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios:
- Multi-step context scenarios:
- Adversarial or role-break scenarios:
- Prompt injection checks:
- Data leakage and unauthorized access checks:
- Result:

## Result Report

- Task summary:
  - created a numbered 100-slice flagship closure map covering the remaining
    canonical UX/UI convergence lane
- Files changed:
  - `docs/planning/canonical-100-slice-closure-map.md`
  - `.codex/tasks/PRJ-821-freeze-canonical-100-slice-closure-map.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check -- docs/planning/canonical-100-slice-closure-map.md .codex/tasks/PRJ-821-freeze-canonical-100-slice-closure-map.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - all implementation slices remain to be executed progressively
- Next steps:
  - keep `home` as the active surface until its deploy-side parity gate is confirmed
- Decisions made:
  - preserved the current closure order instead of reopening multiple route lanes in parallel
