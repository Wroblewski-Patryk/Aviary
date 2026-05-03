# Task

## Header
- ID: PRJ-1027
- Title: Extract shared module dot-row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1026
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1027
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1026 selected plans context rows and goals guidance rows as the next shared
module cleanup target. Both lists use the same wrapper, row, dot, title, and
body structure with route-specific selectors.

## Goal
Move repeated dot-row module list presentation into a shared component while
preserving route-specific CSS selectors and keeping data construction in
`App()`.

## Scope
- `web/src/components/shared.tsx`
- `web/src/App.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated dot-row JSX remains in module route side
  panels.
- Expected product or reliability outcome: route rendering is easier to trace
  without changing frontend behavior.
- How success will be observed: build and 14-route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage
A verified `ModuleDotRowList` extraction with docs and context synced.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep route state and route data ownership in `App()`

## Implementation Plan
1. Add `ModuleDotRowList` to `web/src/components/shared.tsx`.
2. Preserve existing row/dot class names through explicit `routeKey` and
   `rowKey` props.
3. Replace plans context rows and goals guidance rows in `web/src/App.tsx`.
4. Update frontend docs, roadmap, task board, and project state.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Existing `aion-plans-context-*` and `aion-goals-guidance-*` selectors remain
  unchanged.
- `plansContextCards` and `goalGuidanceCards` remain in `App()`.
- `npm run build`, `npm run smoke:routes`, and `git diff --check` pass.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a frontend refactor slice.
- [x] Shared component added.
- [x] Repeated JSX replaced for the selected routes.
- [x] Relevant docs and context updated.
- [x] Validation evidence recorded.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed route/row keys preserve existing CSS selectors
- Screenshots/logs: route smoke output
- High-risk checks:
  - no API, state, persistence, auth, or deployment code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - audit the next module cleanup target after `ModuleDotRowList`

## Notes
This is presentation-only. It intentionally does not touch memory signal cards
or the goal horizon because those shapes include additional content and visual
behavior.

## Result Report

- Task summary: added `ModuleDotRowList` and used it for plans context rows and
  goals guidance rows.
- Files changed:
  - `web/src/components/shared.tsx`
  - `web/src/App.tsx`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `npm run build`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - memory signal cards and decorative module panels remain future audited
    slices
- Next steps:
  - audit whether the single-route memory signal card is worth extracting or
    whether to shift to a route data/helper slice
- Decisions made:
  - keep data arrays in `App()` and preserve CSS via `routeKey`/`rowKey`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - repeated dot-row JSX remained in `/plans` and `/goals`
- Gaps:
  - no shared dot-row list existed for these module side panels
- Inconsistencies:
  - same visual row shape was implemented inline twice
- Architecture constraints:
  - keep route data derivation in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1027 extract shared module dot-row list
- Priority rationale:
  - low-risk follow-up from PRJ-1026
- Why other candidates were deferred:
  - memory signals and decorative panels have different shapes

### 3. Plan Implementation
- Files or surfaces to modify:
  - shared component module, route JSX, frontend docs, context
- Logic:
  - route/row key class-name composition only
- Edge cases:
  - no empty-state or API behavior changes

### 4. Execute Implementation
- Implementation notes:
  - added `ModuleDotRowList`
  - replaced two inline map blocks

### 5. Verify and Test
- Validation performed:
  - frontend build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leave the rows inline, but the same structure now appears in two module
    routes and has an obvious shared boundary
- Technical debt introduced: no
- Scalability assessment:
  - the component can cover future route-keyed dot rows with matching shape
- Refinements made:
  - excluded memory signal and horizon rows from this scope

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, route component map, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
