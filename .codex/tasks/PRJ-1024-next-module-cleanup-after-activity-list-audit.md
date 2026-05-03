# Task

## Header
- ID: PRJ-1024
- Title: Audit next module route cleanup target after activity list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1023
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1024
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The browser shell is being reduced in small v1 architecture slices so
`web/src/App.tsx` keeps route state and backend contracts while repeated
presentation chrome moves into shared components. PRJ-1023 extracted the shared
recent activity list used by `/memory` and `/reflections`.

## Goal
Select the next smallest module-route cleanup target that improves component
ownership without changing route behavior, API calls, data projections, or
canonical visual intent.

## Scope
- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: module route ownership remains hard to trace while
  repeated JSX stays embedded in `App()`.
- Expected product or reliability outcome: the next implementation slice is
  explicit, low risk, and traceable.
- How success will be observed: docs name the next target, deferred targets, and
  validation expectations.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit note selecting the next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect remaining module-route card/list clusters in `web/src/App.tsx`.
2. Compare candidates by risk, visual specificity, and reuse potential.
3. Select one implementation task.
4. Update the route cluster audit, v1 roadmap, and context files.
5. Run whitespace/diff validation.

## Acceptance Criteria
- The selected next task is one small implementation slice.
- Deferred candidates are documented with the reason they are deferred.
- The next task preserves existing route data ownership and behavior.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - reviewed remaining module route card/list clusters in `web/src/App.tsx`
- Screenshots/logs: not applicable
- High-risk checks:
  - no runtime code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - add PRJ-1025 as the next shared module text-card list extraction

## Notes
The safest next target is a shared route-keyed text-card list for module cards
whose markup is currently just `title` plus `body`. This can cover reflection
prompt cards, planning suggestion cards, and goal signal cards while preserving
their current CSS class names through explicit route/card keys.

Deferred:
- memory signal cards because they include `meta`
- plans/goals context rows because they include dot-row chrome
- decorative goal horizon panel because it is visually richer and should be
  split only after another focused audit

## Result Report

- Task summary: selected shared module text-card list extraction as the next
  module cleanup slice.
- Files changed:
  - `.codex/tasks/PRJ-1024-next-module-cleanup-after-activity-list-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is intentionally deferred to PRJ-1025
- Next steps:
  - implement `ModuleTextCardList` for reflection prompt cards, planning step
    cards, and goal signal cards
- Decisions made:
  - defer memory signal cards, dot-row context lists, and decorative goal
    horizon panels

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - repeated title/body card JSX remains in module route branches
- Gaps:
  - no shared text-card list wrapper exists for route-keyed module cards
- Inconsistencies:
  - similar reflection, plan, and goal card presentation is owned directly by
    `App()`
- Architecture constraints:
  - keep state, API, copy, and data derivation in `App()` for this slice

### 2. Select One Priority Task
- Selected task:
  - PRJ-1024 audit next module cleanup target
- Priority rationale:
  - planning prevents accidental visual or behavior drift before another
    component extraction
- Why other candidates were deferred:
  - richer panels and provider/helper clusters are higher risk

### 3. Plan Implementation
- Files or surfaces to modify:
  - frontend architecture docs and context files
- Logic:
  - docs-only selection
- Edge cases:
  - avoid claiming implementation completion

### 4. Execute Implementation
- Implementation notes:
  - selected a route-keyed shared text-card list as PRJ-1025

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - defer all route work, but that would leave an obvious repeated JSX cluster
    unmapped
- Technical debt introduced: no
- Scalability assessment:
  - next task keeps route-specific CSS names through explicit keys
- Refinements made:
  - memory signal cards were excluded because their `meta` field makes them a
    different shape

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
