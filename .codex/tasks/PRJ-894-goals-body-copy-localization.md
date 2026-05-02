# Task

## Header
- ID: PRJ-894
- Title: Goals Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-893
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 894
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-890 found `/goals` still renders route-owned English body copy in Polish UI
mode. PRJ-893 completed the preceding Plans slice.

## Goal
Move static Goals route body copy into the existing `UI_COPY.goals` structure.

## Scope
- Route:
  - `/goals`
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-894-goals-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - broad shared Dashboard goal/guidance refactor
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: Polish Goals view still contains English
  route-owned body copy.
- Expected product or reliability outcome: static Goals route copy is owned by
  the existing localization structure.
- How success will be observed: build passes and a Polish Goals smoke no longer
  finds targeted English hardcoded phrases from PRJ-890.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused localization refactor for static Goals route copy.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend `UI_COPY.goals` for route-owned body strings and count units.
2. Replace hardcoded Goals route copy with `copy.goals` fields.
3. Use Goals-local rows/cards to avoid broad shared Dashboard changes.
4. Run frontend build.
5. Run a Polish Goals smoke for targeted English phrase absence.
6. Update task board and project state.

## Acceptance Criteria
- Static Goals stat details, horizon labels, goal rows, signal cards, and
  guidance rows use `copy.goals`.
- English behavior remains unchanged for the Goals route.
- Polish smoke confirms targeted Goals English phrases are absent.
- `npm run build` passes.

## Definition of Done
- [x] Goals static body copy uses `UI_COPY.goals`.
- [x] Build passes.
- [x] Polish Goals smoke passes.
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
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-894-goals-body-copy-localization.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP Polish Goals copy smoke
  - result: passed
  - checked route-owned Polish strings, targeted English phrase absence,
    route path, and horizontal overflow
- Screenshots/logs:
  - `.codex/artifacts/prj894-goals-body-copy-localization/pl-goals-copy-smoke.json`
  - `.codex/artifacts/prj894-goals-body-copy-localization/pl-goals-mobile.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This slice only localizes Goals route-owned static copy.

## Result Report
- Task summary:
  - moved Goals route-owned static copy into `UI_COPY.goals`
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-894-goals-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - frontend build
  - Chrome CDP Polish Goals copy smoke with screenshot evidence
  - diff whitespace check
- What is incomplete:
  - shared recent/guidance copy outside Goals remains a separate localization
    lane
- Next steps:
  - localize `/reflections` route-owned body copy or run a fresh localized
    route audit to confirm the next highest remaining gap
- Decisions made:
  - use Goals-local rows/cards instead of expanding a shared Dashboard guidance
    refactor

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - PRJ-890 found Goals route-owned English body copy in Polish UI mode.
- Gaps:
  - lower Goals sections were not fully backed by `UI_COPY`.
- Inconsistencies:
  - hero labels localized while horizon, signal cards, and related guidance
    stayed English.
- Architecture constraints:
  - reuse `UI_COPY`; avoid a broad shared Dashboard guidance refactor.

### 2. Select One Priority Task
- Selected task:
  - localize Goals route-owned body copy.
- Priority rationale:
  - next visible route-owned copy gap after Plans.
- Why other candidates were deferred:
  - shared recent/guidance copy needs separate ownership work.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - task and context docs
- Logic:
  - add Goals copy fields and build Goals route arrays from them.
- Edge cases:
  - singular/plural units should avoid obvious Polish grammar issues.

### 4. Execute Implementation
- Implementation notes:
  - localized Goals stat details, horizon labels, goal rows, signal cards, and
    guidance rows
  - added localized count units and singular/plural direction text

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Chrome CDP Polish Goals copy smoke
  - screenshot review
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leaving shared Dashboard rows was rejected for Goals route because it would
    keep route-owned English in the localized view.
- Technical debt introduced: no
- Scalability assessment:
  - follows the route-specific `UI_COPY` pattern established by recent slices.
- Refinements made:
  - singular/plural direction text handles `1 cel` correctly.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-894-goals-body-copy-localization.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
