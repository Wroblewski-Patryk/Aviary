# Task

## Header
- ID: PRJ-1036
- Title: Audit next live frontend cleanup after provider row extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1035
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1036
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1035 extracted integrations provider rows into shared value-row
presentation. Remaining live route-local candidates include memory signal cards,
dashboard progress rows, goal horizon rows, route data helpers, and decorative
panels.

## Goal
Select the next live frontend cleanup target after integrations provider row
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: route-local card presentation still hides simple
  module behavior in `App()`.
- Expected product or reliability outcome: the next frontend cleanup stays
  small and avoids visual-sensitive progress panels.
- How success will be observed: docs select one next implementation task.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting the next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep route data and copy construction in `App()`

## Implementation Plan
1. Inspect remaining memory signal, dashboard progress, and goal horizon row
   candidates.
2. Compare simple meta cards with progress-row and decorative candidates.
3. Select one next implementation slice.
4. Update frontend docs, roadmap, task board, and project state.
5. Run `git diff --check`.

## Acceptance Criteria
- Exactly one next task is selected.
- Deferred candidates and reasons are documented.
- The selected task preserves existing CSS selectors and route data ownership.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - reviewed `memorySignalCards`, `dashboardGoalRows`, and `goalHorizonRows`
    usages in `web/src/App.tsx`
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
  - add PRJ-1037 as memory signal meta-card list extraction

## Notes
Selected next task:
- PRJ-1037: extract memory signal cards into a route-keyed meta-card list.

This is currently a single-route usage, but the card shape is simple and the
existing route-keyed shared component pattern can preserve
`aion-memory-signal-*` selectors while keeping `memorySignalCards` in `App()`.

Deferred:
- dashboard progress rows because they use progress width sizing.
- goal horizon rows because they include token, detail, progress, and value.
- route data-helper extraction because it moves more semantics than the next
  presentation-only slice.
- decorative panels because they require visual audits.

## Result Report

- Task summary: selected memory signal meta-card list extraction as the next
  live frontend cleanup.
- Files changed:
  - `.codex/tasks/PRJ-1036-next-live-cleanup-after-provider-row-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is deferred to PRJ-1037
- Next steps:
  - implement `ModuleMetaCardList` for memory signal cards
- Decisions made:
  - defer progress-row extraction

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - memory signal cards remain inline in `App()`
- Gaps:
  - no shared meta-card list owns `meta/title/body` card presentation
- Inconsistencies:
  - other simple module card/list shapes have shared components
- Architecture constraints:
  - route data and copy construction remain in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1036 audit next live cleanup target
- Priority rationale:
  - memory signal cards are lower risk than progress/decorative panels
- Why other candidates were deferred:
  - progress rows and visual panels are more layout-sensitive

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - select next implementation task
- Edge cases:
  - avoid overgeneralizing progress rows

### 4. Execute Implementation
- Implementation notes:
  - selected PRJ-1037

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - start route data-helper extraction, but it is broader
- Technical debt introduced: no
- Scalability assessment:
  - route-keyed meta-card list follows existing shared component pattern
- Refinements made:
  - progress row candidates were explicitly deferred

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
