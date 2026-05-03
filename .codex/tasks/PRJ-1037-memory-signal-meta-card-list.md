# Task

## Header
- ID: PRJ-1037
- Title: Extract shared module meta-card list for memory signals
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1036
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1037
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1036 selected the memory signal cards because they are a small
presentation-only `meta/title/body` shape. Progress rows and decorative panels
remain intentionally deferred.

## Goal
Move memory signal card presentation behind a shared route-keyed meta-card list
without changing memory data or copy construction.

## Scope
- `web/src/components/shared.tsx`
- `web/src/App.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: memory signal card presentation remains inline in
  `App()`.
- Expected product or reliability outcome: another simple module card shape is
  traceable through shared presentation.
- How success will be observed: build and 14-route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage
A verified `ModuleMetaCardList` extraction with docs and context synced.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep `memorySignalCards` data and copy construction in `App()`

## Implementation Plan
1. Add `ModuleMetaCardList` to `web/src/components/shared.tsx`.
2. Preserve `aion-memory-signal-*` selectors through `routeKey` and `cardKey`.
3. Replace inline memory signal card JSX in `/memory`.
4. Update docs, roadmap, task board, and project state.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Existing memory signal CSS selectors remain unchanged.
- `memorySignalCards` remains in `App()`.
- `npm run build`, `npm run smoke:routes`, and `git diff --check` pass.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a frontend refactor slice.
- [x] Shared meta-card list component added.
- [x] Memory signal card JSX replaced.
- [x] Relevant docs and context updated.
- [x] Validation evidence recorded.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed `routeKey="memory"` and `cardKey="signal"` preserve existing CSS
    class names
- High-risk checks:
  - no API, memory, auth, persistence, or deployment code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - audit progress-row or route data-helper cleanup separately

## Notes
This is presentation-only. It does not change memory summary projections,
recent-channel labels, learned-state summaries, or route behavior.

## Result Report

- Task summary: added `ModuleMetaCardList` and used it for memory signal cards.
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
  - progress rows and visual panels remain future audited slices
- Next steps:
  - audit whether progress row presentation or route data helpers should move
    next
- Decisions made:
  - keep `memorySignalCards` in `App()`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - memory signal card JSX was inline
- Gaps:
  - no shared meta-card list existed
- Inconsistencies:
  - other simple module card/list shapes had shared components
- Architecture constraints:
  - memory data remains route-owned in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1037 extract shared module meta-card list
- Priority rationale:
  - direct follow-up from PRJ-1036
- Why other candidates were deferred:
  - progress rows are more layout-sensitive

### 3. Plan Implementation
- Files or surfaces to modify:
  - shared components, `App.tsx`, frontend docs, context
- Logic:
  - route-keyed class-name composition only
- Edge cases:
  - preserve meta/title/body order

### 4. Execute Implementation
- Implementation notes:
  - added `ModuleMetaCardList`
  - replaced memory signal map

### 5. Verify and Test
- Validation performed:
  - frontend build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leave single-route card inline, but the shape fits the existing shared
    route-keyed pattern
- Technical debt introduced: no
- Scalability assessment:
  - meta-card list can support future matching module cards
- Refinements made:
  - progress rows remain out of scope

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, route component map, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
