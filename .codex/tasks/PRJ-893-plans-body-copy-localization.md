# Task

## Header
- ID: PRJ-893
- Title: Plans Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-892
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 893
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-890 found `/plans` still renders route-owned English body copy in Polish UI
mode. PRJ-892 completed the preceding Memory slice.

## Goal
Move static Plans route body copy into the existing `UI_COPY.plans` structure.

## Scope
- Route:
  - `/plans`
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-893-plans-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - localizing shared Dashboard guidance cards
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: Polish Plans view still contains English
  route-owned body copy.
- Expected product or reliability outcome: static Plans route copy is owned by
  the existing localization structure.
- How success will be observed: build passes and a Polish Plans smoke no longer
  finds targeted English hardcoded phrases from PRJ-890.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused localization refactor for static Plans route copy.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend `UI_COPY.plans` for route-owned body strings and count units.
2. Replace hardcoded Plans route copy with `copy.plans` fields.
3. Use Plans-local context cards to avoid broad shared Dashboard changes.
4. Run frontend build.
5. Run a Polish Plans smoke for targeted English phrase absence.
6. Update task board and project state.

## Acceptance Criteria
- Static Plans stat details, path labels, flow rows, next-step cards, and
  context rows use `copy.plans`.
- English behavior remains unchanged for the Plans route.
- Polish smoke confirms targeted Plans English phrases are absent.
- `npm run build` passes.

## Definition of Done
- [x] Plans static body copy uses `UI_COPY.plans`.
- [x] Build passes.
- [x] Polish Plans smoke passes.
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
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-893-plans-body-copy-localization.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP Polish Plans copy smoke
  - result: passed
  - checked route-owned Polish strings, targeted English phrase absence,
    route path, and horizontal overflow
- Screenshots/logs:
  - `.codex/artifacts/prj893-plans-body-copy-localization/pl-plans-copy-smoke.json`
  - `.codex/artifacts/prj893-plans-body-copy-localization/pl-plans-mobile.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This slice only localizes Plans route-owned static copy.

## Result Report
- Task summary:
  - moved Plans route-owned static copy into `UI_COPY.plans`
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-893-plans-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - frontend build
  - Chrome CDP Polish Plans copy smoke with screenshot evidence
  - diff whitespace check
- What is incomplete:
  - `/goals` and shared recent/guidance copy still need separate slices
- Next steps:
  - localize `/goals` route-owned body copy
- Decisions made:
  - use Plans-local context cards instead of expanding a shared Dashboard
    guidance refactor

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - PRJ-890 found Plans route-owned English body copy in Polish UI mode.
- Gaps:
  - lower Plans sections were not fully backed by `UI_COPY`.
- Inconsistencies:
  - hero labels localized while path, flow rows, suggestions, and context
    cards stayed English.
- Architecture constraints:
  - reuse `UI_COPY`; avoid a broad shared Dashboard guidance refactor.

### 2. Select One Priority Task
- Selected task:
  - localize Plans route-owned body copy.
- Priority rationale:
  - next visible route-owned copy gap after Memory.
- Why other candidates were deferred:
  - Goals and shared copy need separate focused slices.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - task and context docs
- Logic:
  - add Plans copy fields and build Plans route arrays from them.
- Edge cases:
  - singular/plural units should avoid obvious Polish grammar issues.

### 4. Execute Implementation
- Implementation notes:
  - localized Plans stat details, planning path labels, flow rows, next-step
    cards, and context cards
  - added localized count units for goals and tasks

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Chrome CDP Polish Plans copy smoke
  - screenshot review
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leaving shared Dashboard guidance cards was rejected for the Plans side
    panel because it would keep route-owned English in the localized view.
- Technical debt introduced: no
- Scalability assessment:
  - follows the route-specific `UI_COPY` pattern established by recent slices.
- Refinements made:
  - replaced shared guidance rows with Plans-local context rows.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-893-plans-body-copy-localization.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
