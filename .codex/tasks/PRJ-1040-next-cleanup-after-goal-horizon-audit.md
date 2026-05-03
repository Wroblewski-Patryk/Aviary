# Task

## Header
- ID: PRJ-1040
- Title: Audit next frontend cleanup after goal horizon extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1039
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1040
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1039 extracted `/goals` horizon progress rows. Remaining visible frontend
cleanup candidates include dashboard progress rows, route data-helper
extraction, and visual panel extraction.

## Goal
Select the next frontend cleanup target after goal horizon extraction without
breaking the dashboard visual direction.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: dashboard progress row presentation remains inline
  in `App()`.
- Expected product or reliability outcome: dashboard presentation moves into
  dashboard-owned components instead of generic shared UI.
- How success will be observed: docs select one next implementation task.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting the next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep dashboard data and sizing calculations in `App()`

## Implementation Plan
1. Inspect the remaining dashboard progress row block.
2. Compare dashboard-specific component extraction with route data-helper and
   visual panel extraction.
3. Select one next implementation slice.
4. Update frontend docs, roadmap, task board, and project state.
5. Run `git diff --check`.

## Acceptance Criteria
- Exactly one next task is selected.
- Dashboard visual sensitivity is documented.
- The selected task preserves existing CSS selectors and data ownership.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - reviewed `dashboardGoalRows` render block and `web/src/components/dashboard.tsx`
- High-risk checks:
  - no runtime code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - add PRJ-1041 as dashboard progress list extraction

## Notes
Selected next task:
- PRJ-1041: extract `DashboardProgressList` into `web/src/components/dashboard.tsx`.

This keeps dashboard-specific presentation in the dashboard component module
instead of widening the generic shared component surface. `dashboardGoalRows`
and `scaledMetricSize(...)` stay in `App()`.

Deferred:
- route data-helper extraction because it moves broader runtime projections.
- visual panel extraction because it needs a dedicated visual/screenshot audit.
- broad dashboard layout extraction because the dashboard is a flagship surface.

## Result Report

- Task summary: selected dashboard-specific progress list extraction as the
  next frontend cleanup.
- Files changed:
  - `.codex/tasks/PRJ-1040-next-cleanup-after-goal-horizon-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is deferred to PRJ-1041
- Next steps:
  - implement `DashboardProgressList`
- Decisions made:
  - use a dashboard-specific component instead of generic shared component

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - dashboard progress rows remain inline
- Gaps:
  - dashboard component module owns signal cards but not progress rows
- Inconsistencies:
  - dashboard presentational pieces are split between `App()` and dashboard components
- Architecture constraints:
  - do not broadly refactor flagship dashboard layout without visual evidence

### 2. Select One Priority Task
- Selected task:
  - PRJ-1040 audit next cleanup target
- Priority rationale:
  - dashboard progress list is narrow and dashboard-owned
- Why other candidates were deferred:
  - route data-helper and visual panel work are broader

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - select next implementation task
- Edge cases:
  - preserve dashboard selectors

### 4. Execute Implementation
- Implementation notes:
  - selected PRJ-1041

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - generic shared progress list, but dashboard has a different visual role
- Technical debt introduced: no
- Scalability assessment:
  - dashboard-specific ownership keeps visual risk bounded
- Refinements made:
  - broad dashboard layout extraction remains deferred

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
