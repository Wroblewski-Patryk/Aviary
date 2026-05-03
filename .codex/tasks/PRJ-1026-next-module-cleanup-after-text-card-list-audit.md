# Task

## Header
- ID: PRJ-1026
- Title: Audit next module cleanup target after text card list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1025
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1026
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1025 extracted shared route-keyed title/body cards for three module route
side panels. Remaining module-local repeated clusters include memory signal
cards, plans/goals dot-row lists, and more decorative goal horizon structures.

## Goal
Select the next smallest module cleanup target after `ModuleTextCardList`
without changing route behavior or touching decorative visual panels.

## Scope
- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated route-local row JSX remains after the text
  card extraction.
- Expected product or reliability outcome: the next implementation slice is
  selected by evidence instead of broad route refactoring.
- How success will be observed: docs and task board point to one concrete next
  slice.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting the next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep route state and route data ownership in `App()`

## Implementation Plan
1. Inspect remaining repeated module row/card clusters in `web/src/App.tsx`.
2. Compare memory signal cards, dot-row lists, and decorative panels by shape
   and risk.
3. Select one next implementation slice.
4. Update frontend architecture docs, roadmap, and context files.
5. Run `git diff --check`.

## Acceptance Criteria
- Exactly one next task is selected.
- Deferred targets and reasons are documented.
- The selected task can preserve existing CSS selectors and route data
  ownership.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - reviewed remaining module route row/card clusters in `web/src/App.tsx`
- Screenshots/logs: not applicable
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
  - add PRJ-1027 as the next shared module dot-row list extraction

## Notes
The next safest implementation target is a shared route-keyed dot-row list for:

- `/plans` context rows
- `/goals` guidance rows

This has the same row structure: wrapper grid, article row, decorative dot,
title, and body. The component can preserve current class names through
`routeKey` and `rowKey`.

Deferred:
- memory signal cards because only `/memory` currently uses the `meta` shape
- goal horizon rows because they include progress bars and richer visual
  composition
- decorative board/ring panels because they are route-specific visual assets

## Result Report

- Task summary: selected shared module dot-row list extraction as the next
  module cleanup slice.
- Files changed:
  - `.codex/tasks/PRJ-1026-next-module-cleanup-after-text-card-list-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is intentionally deferred to PRJ-1027
- Next steps:
  - implement `ModuleDotRowList` for `/plans` context and `/goals` guidance
    rows
- Decisions made:
  - defer memory signal cards and decorative panels

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - dot-row card markup remains repeated in module route branches
- Gaps:
  - no shared component owns the route-keyed dot-row shape for these routes
- Inconsistencies:
  - plans context and goals guidance rows use the same structure directly in
    `App()`
- Architecture constraints:
  - keep route data arrays in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1026 audit next module cleanup target
- Priority rationale:
  - the implementation candidate is small and lower risk than decorative panels
- Why other candidates were deferred:
  - memory signals and horizon visuals are less reusable

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - select next component extraction
- Edge cases:
  - avoid grouping visually different card shapes

### 4. Execute Implementation
- Implementation notes:
  - selected route-keyed dot-row list extraction as PRJ-1027

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - extract memory signal card first, but it currently has only one route
    consumer
- Technical debt introduced: no
- Scalability assessment:
  - the chosen row shape can be reused by similar route-keyed row lists
- Refinements made:
  - decorative goal horizon was explicitly excluded

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
