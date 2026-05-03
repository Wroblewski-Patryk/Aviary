# Task

## Header
- ID: PRJ-1113
- Title: Extract shell mobile tabbar
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1112
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1113
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1112` selected a shell-owned mobile tabbar boundary while preserving the
route-owned scroll-centering effect in `App()`.

## Goal
Move the bottom mobile tabbar JSX into `web/src/components/shell.tsx` while
keeping route refs and route-change behavior explicit.

## Success Signal
- User or operator problem: the final live JSX render map leaves `App.tsx`.
- Expected product or reliability outcome: route smoke remains green and the
  mobile tabbar boundary is documented.
- How success will be observed: build, route smoke, map inspection, and diff
  check pass.
- Post-launch learning needed: no

## Scope
- Update `web/src/components/shell.tsx`.
- Update `web/src/App.tsx`.
- Update docs/context.

## Deliverable For This Stage
A verified `ShellMobileTabbar` extraction.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add `ShellMobileTabbar` to `web/src/components/shell.tsx`.
2. Pass `routes`, `activeRoute`, `labelForRoute`, `onRouteChange`,
   `scrollRef`, and `registerRouteRef`.
3. Replace the inline mobile tabbar JSX in `App.tsx`.
4. Keep the `/chat` hidden condition and scroll-centering effect in `App()`.
5. Run build, route smoke, remaining-map inspection, and diff check.

## Acceptance Criteria
- `App.tsx` no longer maps `ROUTES` for the mobile tabbar inline.
- `ShellMobileTabbar` preserves existing mobile tabbar selectors/classes.
- Route button refs remain registered into `App()` state.
- Build and route smoke pass.

## Definition of Done
- [x] `ShellMobileTabbar` implemented.
- [x] Inline mobile tabbar JSX replaced.
- [x] Build and route smoke pass.
- [x] Docs/context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: passed with `status=ok`, `route_count=14`
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - result: remaining maps inspected; live JSX render maps are gone
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
After this task, the remaining `.map(...)` calls in `App.tsx` are data
projections or local transcript state updates, not JSX render maps.

## Result Report

- Task summary:
  - extracted the shell mobile tabbar to `ShellMobileTabbar`.
- Files changed:
  - `.codex/tasks/PRJ-1113-shell-mobile-tabbar-extraction.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/shell.tsx`
- How tested:
  - `npm run build`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - remaining data projections in `App.tsx` still need a final boundary audit.
- Next steps:
  - `PRJ-1114` audit remaining data projections and frontend cleanup closure.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - bottom mobile tabbar JSX map still lived in `App.tsx`.
- Gaps:
  - no shell-owned mobile tabbar boundary existed.
- Inconsistencies:
  - none found.
- Architecture constraints:
  - scroll-centering effect remains in `App()`.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1113` extract shell mobile tabbar.
- Priority rationale:
  - it removes the final live JSX render map from `App.tsx`.
- Why other candidates were deferred:
  - remaining maps are data projections or local state updates.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/components/shell.tsx`
  - `web/src/App.tsx`
  - docs/context/task files
- Logic:
  - move markup to a shell component and pass refs/callbacks explicitly.
- Edge cases:
  - active route styling, route labels, route changes, and scroll ref
    registration.

### 4. Execute Implementation
- Implementation notes:
  - `ShellMobileTabbar` now renders the mobile tabbar and registers route
    button refs through a callback.

### 5. Verify and Test
- Validation performed:
  - `npm run build`
  - `npm run smoke:routes`
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leave refs and map inline.
- Technical debt introduced: no
- Scalability assessment:
  - shell component owns presentation while `App()` owns route effects.
- Refinements made:
  - generic route typing mirrors existing shell route/nav components.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
