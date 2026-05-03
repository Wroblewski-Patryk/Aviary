# Task

## Header
- ID: PRJ-1107
- Title: Audit remaining frontend map boundaries after tools directory extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1106
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1107
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1106` removed the largest remaining behaviorful tools directory map from
`App.tsx`. The remaining maps need classification before another implementation
target is selected.

## Goal
Classify the remaining `App.tsx` maps and select the next smallest safe
frontend cleanup that does not cross behavior or ref ownership boundaries.

## Success Signal
- User or operator problem: frontend cleanup continues without risky chat or
  mobile navigation ref movement.
- Expected product or reliability outcome: the next task removes a small data
  projection without changing route behavior.
- How success will be observed: remaining maps are classified and one next task
  is recorded.
- Post-launch learning needed: no

## Scope
- Inspect remaining `web/src/App.tsx` `.map(...)` call sites.
- Update frontend audit docs, roadmap, task board, and project state.

## Deliverable For This Stage
An audit result selecting the next safe implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect remaining `.map(...)` call sites.
2. Separate pure data projections from behaviorful/ref-sensitive rendering.
3. Select one small implementation target.
4. Update docs/context.
5. Run `git diff --check`.

## Acceptance Criteria
- Remaining maps are classified.
- Chat transcript and mobile tabbar maps are explicitly deferred.
- One next small task is selected.
- `git diff --check` passes.

## Definition of Done
- [x] Current state analyzed.
- [x] One next priority task selected.
- [x] Docs/context updated.
- [x] Validation evidence recorded.

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
- Tests: not applicable for audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - result: remaining maps inspected
- Screenshots/logs: not applicable.
- High-risk checks:
  - `git diff --check`
  - result: passed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: current browser shell implementation
- Canonical visual target: current v1 browser shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable for audit-only task
- Visual-direction brief reviewed: not applicable for audit-only task
- Existing shared pattern reused: route/component ownership audit pattern
- New shared pattern introduced: no
- Design-memory entry reused: frontend route/component map
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: not assessed
- State checks: not applicable
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: docs-only audit; revert task/context/doc changes if needed
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes
Remaining map categories:

- pure data projections: planning names, recent channels, goal horizon rows,
  integration provider rows, and chat motivation text
- local state updates: optimistic transcript reconciliation
- public hero highlight projection: `publicHomeSurface.heroCards.map(...)`
  adapts `{ title, body }` to `MotifFigurePanel`'s `{ label, value }`
- chat transcript rendering: owns message refs, delivery labels, timestamps,
  and markdown rendering
- bottom mobile tabbar: owns scroll refs and route button registration

The next smallest safe task is `PRJ-1108`: align the public hero card data
shape with `MotifFigurePanel` highlights so the JSX no longer performs a
one-off projection.

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

This task is audit-only and does not deliver runtime behavior.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future frontend maintainers
- Existing workaround or pain: remaining maps need correct ownership decisions
  before more extraction.
- Smallest useful slice: align public hero data shape.
- Success metric or signal: next task selected with risky maps deferred.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: public landing hero
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: `git diff --check`
- Rollback or disable path: revert docs/context/task changes

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: `git diff --check`

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no data touched
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: none for audit-only change

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary:
  - classified remaining `App.tsx` maps after tools directory extraction.
- Files changed:
  - `.codex/tasks/PRJ-1107-remaining-frontend-map-boundary-audit.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - public hero data-shape alignment is not yet implemented.
- Next steps:
  - `PRJ-1108` align public hero card data shape with motif highlights.
- Decisions made:
  - defer chat transcript and mobile tabbar extraction until separate
    ref/behavior audits.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - remaining maps mix pure data projections and ref-sensitive rendering.
- Gaps:
  - no immediate safe chat/mobile extraction target was selected.
- Inconsistencies:
  - public hero data uses `{ title, body }` but `MotifFigurePanel` consumes
    `{ label, value }`.
- Architecture constraints:
  - refs and message rendering behavior stay route-owned until separately
    audited.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1107` audit remaining frontend map boundaries.
- Priority rationale:
  - ARCHITECT iteration should prevent risky extraction after the last large map
    moved.
- Why other candidates were deferred:
  - chat transcript owns refs/delivery/timestamp/markdown behavior.
  - bottom mobile tabbar owns scroll refs.
  - route data projections are not presentation maps.

### 3. Plan Implementation
- Files or surfaces to modify:
  - task file, task board, project state, frontend audit docs, v1 roadmap.
- Logic:
  - classify maps and select the smallest safe implementation follow-up.
- Edge cases:
  - avoid turning ref-sensitive maps into generic components prematurely.

### 4. Execute Implementation
- Implementation notes:
  - audit-only docs/context updates were made; runtime code was not changed.

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - proceed directly to chat transcript extraction.
- Technical debt introduced: no
- Scalability assessment:
  - data-shape alignment is reversible and lower risk than ref movement.
- Refinements made:
  - risky maps were explicitly deferred.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
