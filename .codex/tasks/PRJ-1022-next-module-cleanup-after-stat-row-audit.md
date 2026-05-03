# Task

## Header
- ID: PRJ-1022
- Title: Audit next module route cleanup target after stat row extraction
- Task Type: documentation
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1021
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1022
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Module overview bars and stat-row wrappers now have shared route-keyed
ownership. Remaining module-route duplication includes recent activity lists
and more route-specific decorative inner panels.

## Goal

Choose the next repeated module route cleanup target while preserving
route-specific visual composition.

## Scope

- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated recent-activity list markup remains inline
  for module routes.
- Expected product or reliability outcome: next slice removes repeated list-row
  chrome while keeping data and route panels explicit.
- How success will be observed: PRJ-1023 is queued for `ModuleActivityList`.
- Post-launch learning needed: no

## Deliverable For This Stage

Record `ModuleActivityList` as the next implementation target.

## Constraints
- do not change runtime code in this task
- do not touch decorative main panels yet
- keep activity data ownership in `App()`
- preserve route-specific classes through route-key props

## Implementation Plan
1. Inspect remaining repeated module route list patterns.
2. Select the smallest repeated wrapper/list target.
3. Update route audit, roadmap, and context.
4. Run `git diff --check`.

## Acceptance Criteria
- Next target is selected with rationale.
- PRJ-1023 is queued.
- Deferred decorative panels are named.
- `git diff --check` passes.

## Definition of Done
- [x] Boundary recorded.
- [x] Roadmap and context updated.
- [x] Diff validation completed.

## Validation Evidence
- Tests:
  - `git diff --check`
  - result: passed
- Manual checks:
  - inspected memory/reflections recent activity rows and decorative panels
- High-risk checks:
  - route-specific decorative panels deferred
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Result Report

- Task summary: selected shared module activity list extraction.
- Files changed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-1022-next-module-cleanup-after-stat-row-audit.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is queued as PRJ-1023
- Next steps:
  - extract `ModuleActivityList`
- Decisions made:
  - recent activity list is lower risk than decorative main-panel extraction

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - recent activity rows repeat between memory and reflections
- Gaps:
  - decorative main panels remain route-local
- Inconsistencies:
  - PRJ-1022 needed a post-stat-row target
- Architecture constraints:
  - route data ownership remains in `App()`

### 2. Select One Priority Task
- Selected task: PRJ-1022
- Priority rationale: it is the next queued module route cleanup audit
- Why other candidates were deferred:
  - decorative panels are more route-specific and visual-sensitive

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - queue a route-keyed activity list component
- Edge cases:
  - preserve row dot and text classes by route key

### 4. Execute Implementation
- Implementation notes:
  - queued PRJ-1023 for `ModuleActivityList`

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - jump to decorative panel extraction; deferred due visual specificity
- Technical debt introduced: no
- Scalability assessment:
  - adequate for small repeated-list cleanup
- Refinements made:
  - limited target to memory/reflections activity rows

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
