# Task

## Header
- ID: PRJ-1019
- Title: Extract shared module overview bar component
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1018
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1019
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-1018` selected the repeated module overview bars for `/memory`,
`/reflections`, `/plans`, and `/goals` as the next low-risk frontend
architecture slice.

## Goal

Move repeated route-keyed overview bar chrome behind a shared component while
preserving route-specific classes, copy, status values, and route data
ownership.

## Scope

- `web/src/components/shared.tsx`
- `web/src/App.tsx`
- `docs/frontend/route-component-map.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated module overview bar markup was inline in
  several route branches.
- Expected product or reliability outcome: shared route chrome is explicit and
  reversible while data stays in `App()`.
- How success will be observed: build and route smoke pass after the four
  overview bars use `ModuleOverviewBar`.
- Post-launch learning needed: no

## Deliverable For This Stage

Release-ready component extraction with validation and docs/context sync.

## Constraints
- do not move route data derivation
- preserve route-specific CSS class names
- preserve route-specific aria labels and copy
- do not touch dashboard/personality flagship surfaces

## Implementation Plan
1. Add `ModuleOverviewBar` to `web/src/components/shared.tsx`.
2. Replace `/memory`, `/reflections`, `/plans`, and `/goals` overview bar JSX in
   `web/src/App.tsx`.
3. Update frontend docs and context.
4. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Four module routes render overview bars through `ModuleOverviewBar`.
- Existing CSS selectors and aria labels are preserved.
- Route data ownership stays in `App()`.
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
  - confirmed route-keyed classes and aria labels are passed explicitly
- High-risk checks:
  - dashboard/personality flagship routes untouched
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - PRJ-1020 queued for the next module route cleanup audit

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report

- Task summary: extracted repeated module overview bars into
  `ModuleOverviewBar`.
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
  - additional module route inner panels remain route-local
- Next steps:
  - PRJ-1020 audit next module route cleanup target
- Decisions made:
  - use `routeKey` to preserve existing route-specific selectors

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - four module routes repeated overview bar chrome
- Gaps:
  - inner module panels still need future cleanup
- Inconsistencies:
  - PRJ-1019 was queued but implementation was not present
- Architecture constraints:
  - data ownership stays in `App()`

### 2. Select One Priority Task
- Selected task: PRJ-1019
- Priority rationale: it was the next queued implementation slice
- Why other candidates were deferred:
  - dashboard/personality require visual-governed work
  - provider/health helper ownership needs separate audit

### 3. Plan Implementation
- Files or surfaces to modify:
  - shared component module, four route usages, docs, context
- Logic:
  - pass route key, copy, status label/value, and aria label explicitly
- Edge cases:
  - route-specific status selectors must stay unchanged

### 4. Execute Implementation
- Implementation notes:
  - added a route-keyed shared component for overview bars

### 5. Verify and Test
- Validation performed:
  - build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leave duplicate bars inline; rejected because the pattern is stable and repeated
- Technical debt introduced: no
- Scalability assessment:
  - adequate for module route chrome cleanup
- Refinements made:
  - status value accepts `ReactNode` so callers keep exact formatting ownership

### 7. Update Documentation and Knowledge
- Docs updated:
  - frontend route/component map
  - app route cluster audit
  - v1 roadmap
- Context updated:
  - task board
  - project state
- Learning journal updated: not applicable
