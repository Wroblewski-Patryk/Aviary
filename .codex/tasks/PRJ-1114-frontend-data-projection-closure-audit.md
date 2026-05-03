# Task

## Header
- ID: PRJ-1114
- Title: Audit remaining data projections and frontend cleanup closure
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1113
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1114
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1113` moved the bottom mobile tabbar out of `App.tsx`. The remaining
`.map(...)` call sites need a closure audit to determine whether the frontend
presentation extraction lane should continue.

## Goal
Confirm whether any live JSX render maps remain in `App.tsx` and select the
next v1 priority.

## Success Signal
- User or operator problem: the frontend cleanup lane does not continue past
  its useful boundary.
- Expected product or reliability outcome: remaining maps are classified as
  data projections or state updates, and v1 work returns to release-reality
  priorities.
- How success will be observed: docs/context record the closure and next
  priority.
- Post-launch learning needed: no

## Scope
- Inspect remaining `web/src/App.tsx` `.map(...)` call sites.
- Inspect current v1 roadmap blockers.
- Update docs/context.

## Deliverable For This Stage
A closure audit for the frontend presentation extraction lane.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect remaining `.map(...)` call sites.
2. Classify them as data projections or state updates.
3. Confirm no live JSX render maps remain.
4. Check v1 roadmap for next highest priority.
5. Update docs/context and run `git diff --check`.

## Acceptance Criteria
- Remaining maps are classified.
- Frontend presentation extraction lane closure is recorded.
- Next v1 priority is selected.
- `git diff --check` passes.

## Definition of Done
- [x] Current state analyzed.
- [x] Closure decision recorded.
- [x] Docs/context updated.
- [x] Validation evidence recorded.

## Validation Evidence
- Tests: not applicable for audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - result: remaining maps inspected
  - `Select-String -Path docs/planning/v1-reality-audit-and-roadmap.md -Pattern "PRJ-952|PRJ-953|PRJ-1114|BLOCKED_EXTERNAL|READY_AFTER" -Context 0,2`
  - result: v1 roadmap blockers inspected
  - `git status --short`
  - result: current modified/untracked scope inspected
- High-risk checks:
  - `git diff --check`
  - result: passed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## Notes
Remaining `App.tsx` maps:

- `primary_goal_names` and `primary_task_names` string normalization
- recent channel label derivation
- goal horizon row data projection
- integration provider row data projection
- chat motivation metric text joining
- local transcript state updates after send success/failure

These are not live JSX render maps. Further movement would be helper/data-model
work and should be justified separately, not treated as presentation cleanup.

Next v1 priority is release reality. `PRJ-952` remains `BLOCKED_EXTERNAL`
pending Coolify/operator action, with `PRJ-953..PRJ-955` still gated behind
deploy parity. If external deploy inputs are unavailable, the next local task
should be a release-readiness evidence refresh rather than more frontend
component extraction.

## Result Report

- Task summary:
  - closed the current frontend presentation extraction lane.
- Files changed:
  - `.codex/tasks/PRJ-1114-frontend-data-projection-closure-audit.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - production deploy parity remains externally blocked.
- Next steps:
  - return to v1 release reality: resolve `PRJ-952` externally or run a local
    release-readiness evidence refresh if deploy inputs are still unavailable.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - no live JSX render maps remain in `App.tsx`.
- Gaps:
  - v1 deploy parity remains blocked externally.
- Inconsistencies:
  - none found.
- Architecture constraints:
  - remaining maps are route data/state derivations.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1114` audit remaining data projections and frontend cleanup closure.
- Priority rationale:
  - closure avoids inventing more frontend extraction work after the useful
    presentation boundary is complete.
- Why other candidates were deferred:
  - release tasks are next, but `PRJ-952` requires external deploy/operator
    input.

### 3. Plan Implementation
- Files or surfaces to modify:
  - task file, task board, project state, frontend audit docs, v1 roadmap.
- Logic:
  - classify remaining maps and update source-of-truth closure state.
- Edge cases:
  - avoid converting local transcript state updates into unnecessary helper
    work.

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
  - keep extracting data projections into helpers.
- Technical debt introduced: no
- Scalability assessment:
  - frontend presentation ownership is now substantially clearer; helper work
    can be planned separately if it has a concrete payoff.
- Refinements made:
  - next priority was reconnected to v1 release blockers.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
