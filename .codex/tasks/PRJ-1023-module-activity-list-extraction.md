# Task

## Header
- ID: PRJ-1023
- Title: Extract shared module activity list
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1022
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1023
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-1022` selected the repeated recent activity row lists in `/memory` and
`/reflections` as the next safe module-route cleanup target.

## Goal

Move repeated recent activity row markup into a route-keyed shared component
while keeping activity data ownership and slicing in `App()`.

## Scope

- `web/src/components/shared.tsx`
- `web/src/App.tsx`
- `docs/frontend/route-component-map.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: memory/reflections recent movement row markup was
  duplicated inline.
- Expected product or reliability outcome: row chrome is shared and route-keyed,
  while activity data remains visible in `App()`.
- How success will be observed: build and route smoke pass with
  `ModuleActivityList`.
- Post-launch learning needed: no

## Deliverable For This Stage

Release-ready activity list extraction with validation and docs/context sync.

## Constraints
- do not move `personalityRecentActivity` data derivation
- preserve route-specific row/dot CSS selectors
- do not touch decorative main panels
- do not touch dashboard/personality flagship surfaces

## Implementation Plan
1. Add `ModuleActivityList` to `web/src/components/shared.tsx`.
2. Replace memory/reflections recent activity rows in `web/src/App.tsx`.
3. Keep data slicing and route panel shells in `App()`.
4. Update docs and context.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Memory and reflections recent activity rows render through `ModuleActivityList`.
- Route-specific selectors are preserved through `routeKey`.
- Activity data ownership stays in `App()`.
- Validation passes.

## Definition of Done
- [x] Component extraction completed.
- [x] Route data ownership preserved in `App()`.
- [x] Docs and context updated.
- [x] Relevant validation completed.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed route-keyed row and dot classes are preserved
- High-risk checks:
  - decorative panels and flagship routes untouched
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Result Report

- Task summary: extracted memory/reflections recent activity row markup into
  `ModuleActivityList`.
- Files changed:
  - `web/src/components/shared.tsx`
  - `web/src/App.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- What is incomplete:
  - decorative module panels remain route-local
- Next steps:
  - PRJ-1024 audit next module route cleanup target
- Decisions made:
  - list accepts already-sliced items so route ownership stays explicit

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - recent activity row markup repeated in memory/reflections
- Gaps:
  - decorative panels still route-local
- Inconsistencies:
  - PRJ-1023 was queued but implementation was not present
- Architecture constraints:
  - route data ownership stays in `App()`

### 2. Select One Priority Task
- Selected task: PRJ-1023
- Priority rationale: it was the next queued implementation slice
- Why other candidates were deferred:
  - decorative panel extraction is more route-specific and visual-sensitive

### 3. Plan Implementation
- Files or surfaces to modify:
  - shared component module, memory/reflections route usage, docs, context
- Logic:
  - route-keyed row/dot classes with explicit items prop
- Edge cases:
  - preserve list spacing and text classes

### 4. Execute Implementation
- Implementation notes:
  - added `ModuleActivityList`

### 5. Verify and Test
- Validation performed:
  - build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leave rows inline; rejected because the duplication is stable and low-risk
- Technical debt introduced: no
- Scalability assessment:
  - adequate for module route cleanup
- Refinements made:
  - kept panel headings route-local

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route/component map
  - app route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
