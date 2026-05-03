# Task

## Header
- ID: PRJ-1112
- Title: Audit mobile tabbar ref extraction readiness
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1111
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1112
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
After `PRJ-1111`, the bottom mobile tabbar is the last live JSX render map in
`App.tsx`. It owns scroll container refs and per-route button refs used by an
existing route-change centering effect.

## Goal
Determine the safe extraction boundary for the mobile tabbar.

## Success Signal
- User or operator problem: the final live JSX map can be extracted without
  breaking active-route scroll centering.
- Expected product or reliability outcome: extraction keeps the route-change
  scroll effect in `App()` and moves only tabbar presentation to the shell
  owner.
- How success will be observed: the next task is recorded with explicit ref
  ownership.
- Post-launch learning needed: no

## Scope
- Inspect mobile tabbar markup and refs in `web/src/App.tsx`.
- Inspect shell component ownership in `web/src/components/shell.tsx`.
- Update docs/context.

## Deliverable For This Stage
An audit result selecting the mobile tabbar extraction boundary.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect `mobileNavScrollRef`, `mobileNavRefs`, and the scroll-centering
   effect.
2. Inspect existing shell navigation components.
3. Define extraction props for a shell-owned mobile tabbar.
4. Update docs/context and run `git diff --check`.

## Acceptance Criteria
- Scroll ref ownership is documented.
- Route button ref registration is documented.
- One next task is selected.
- `git diff --check` passes.

## Definition of Done
- [x] Current state analyzed.
- [x] Safe extraction boundary selected.
- [x] Docs/context updated.
- [x] Validation evidence recorded.

## Validation Evidence
- Tests: not applicable for audit-only task.
- Manual checks:
  - `Get-Content web/src/App.tsx | Select-Object -Skip 4888 -First 45`
  - `Select-String -Path web/src/App.tsx -Pattern "mobileNavScrollRef|mobileNavRefs|aion-mobile-tabbar|changeRoute\(|routeLabel\(" -Context 2,5`
  - `Get-Content web/src/components/shell.tsx`
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
- Follow-up architecture doc updates:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`

## Notes
Safe extraction boundary:

- Add a shell-owned `ShellMobileTabbar`.
- Pass `routes`, `activeRoute`, `labelForRoute`, and `onRouteChange`.
- Pass `scrollRef` and `registerRouteRef` from `App()` so the existing
  centering effect remains route-owned.
- Keep the `/chat` hide condition in `App()` for this slice.

The next task is `PRJ-1113`: extract `ShellMobileTabbar`.

## Result Report

- Task summary:
  - audited the final live JSX render map and selected a safe shell extraction
    boundary.
- Files changed:
  - `.codex/tasks/PRJ-1112-mobile-tabbar-ref-extraction-readiness-audit.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - mobile tabbar extraction is pending.
- Next steps:
  - `PRJ-1113` extract `ShellMobileTabbar`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - bottom mobile tabbar render map still lives in `App.tsx`.
- Gaps:
  - no component boundary yet for mobile tabbar refs.
- Inconsistencies:
  - none found.
- Architecture constraints:
  - route scroll-centering effect should stay in `App()` for this slice.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1112` audit mobile tabbar ref extraction readiness.
- Priority rationale:
  - it is the last live JSX map after chat transcript extraction.
- Why other candidates were deferred:
  - remaining non-mobile maps are route data projections or local state updates.

### 3. Plan Implementation
- Files or surfaces to modify:
  - task file, task board, project state, frontend audit docs, v1 roadmap.
- Logic:
  - define ref-preserving shell component boundary.
- Edge cases:
  - active route scroll centering, `/chat` hidden state, and route label
    localization.

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
  - move scroll effect into the component.
- Technical debt introduced: no
- Scalability assessment:
  - keeping the effect in `App()` avoids changing route behavior while still
    removing the render map in the next slice.
- Refinements made:
  - extraction props were defined explicitly.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
