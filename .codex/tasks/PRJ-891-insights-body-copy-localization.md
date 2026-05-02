# Task

## Header
- ID: PRJ-891
- Title: Insights Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-890
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 891
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-890 ranked `/insights` as the remaining module route with the highest
observed route-owned English body-copy debt in Polish UI mode.

## Goal
Move static Insights route body copy into the existing `UI_COPY.insights`
structure so Polish localized views no longer show the targeted English
route-owned insight copy.

## Scope
- Route:
  - `/insights`
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-891-insights-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - localizing shared Dashboard, Goals, Plans, or Memory route copy
  - translating backend/provider payload values
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: Polish Insights view still contains English
  route-owned body copy.
- Expected product or reliability outcome: static Insights route copy is owned
  by the existing localization structure.
- How success will be observed: build passes and a Polish Insights smoke no
  longer finds the targeted English hardcoded phrases from PRJ-890.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused localization refactor for static Insights route copy.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend `UI_COPY.insights` for route-owned body strings.
2. Replace hardcoded Insights route copy with `copy.insights` fields.
3. Use Insights-local guidance cards to avoid broad shared Dashboard changes.
4. Run frontend build.
5. Run a Polish Insights smoke for targeted English phrase absence.
6. Update task board and project state.

## Acceptance Criteria
- Static Insights stat details, map labels, signal rows, clarity notes, and
  guidance candidates use `copy.insights`.
- English behavior remains unchanged for the Insights route.
- Polish smoke confirms targeted Insights English phrases are absent.
- `npm run build` passes.

## Definition of Done
- [x] Insights static body copy uses `UI_COPY.insights`.
- [x] Build passes.
- [x] Polish Insights smoke passes.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new localization system
- broad shared Dashboard guidance refactor
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-891-insights-body-copy-localization.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP Polish Insights copy smoke
  - result: passed
  - checked route-owned Polish strings, targeted English phrase absence,
    corrected `1 cel`, route path, and horizontal overflow
- Screenshots/logs:
  - `.codex/artifacts/prj891-insights-body-copy-localization/pl-insights-copy-smoke-v2.json`
  - `.codex/artifacts/prj891-insights-body-copy-localization/pl-insights-mobile-v2.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This slice intentionally keeps shared Dashboard guidance copy outside scope.

## Result Report
- Task summary:
  - moved Insights route-owned static copy into `UI_COPY.insights`
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-891-insights-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - frontend build
  - Chrome CDP Polish Insights copy smoke with screenshot evidence
  - diff whitespace check
- What is incomplete:
  - shared Dashboard guidance used by other routes remains out of scope
- Next steps:
  - localize `/memory`, `/plans`, and `/goals` route-owned body copy
- Decisions made:
  - Insights uses local guidance cards so this slice does not refactor shared
    Dashboard guidance data

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - PRJ-890 found `/insights` had the most targeted English body-copy signals.
- Gaps:
  - lower Insights sections were not fully backed by `UI_COPY`.
- Inconsistencies:
  - hero labels localized while map, signal rows, notes, and guidance remained
    English.
- Architecture constraints:
  - reuse `UI_COPY`; avoid a broad shared guidance refactor in this slice.

### 2. Select One Priority Task
- Selected task:
  - localize Insights route-owned body copy.
- Priority rationale:
  - highest-impact route from PRJ-890 audit.
- Why other candidates were deferred:
  - Memory, Plans, Goals, and Tools need separate focused slices.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - task and context docs
- Logic:
  - add Insights copy fields and build Insights route arrays from them.
- Edge cases:
  - singular/plural units should avoid obvious Polish grammar issues.

### 4. Execute Implementation
- Implementation notes:
  - localized Insights stat details, map labels, signal rows, clarity notes,
    and guidance candidates
  - added localized singular/plural unit handling for visible insight counts

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Chrome CDP Polish Insights copy smoke
  - screenshot review
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - reusing shared Dashboard guidance cards was rejected for this slice because
    it would keep English copy in Insights or expand scope across routes.
- Technical debt introduced: no
- Scalability assessment:
  - follows the route-specific `UI_COPY` pattern established by PRJ-888 and
    PRJ-889.
- Refinements made:
  - fixed the visible `1 cele` issue to render `1 cel`.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-891-insights-body-copy-localization.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
