# Task

## Header
- ID: PRJ-892
- Title: Memory Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-891
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 892
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-890 found `/memory` still renders route-owned English body copy in Polish
UI mode after the higher-priority Insights route was fixed by PRJ-891.

## Goal
Move static Memory route body copy into the existing `UI_COPY.memory`
structure so Polish localized views no longer show targeted English
route-owned memory copy.

## Scope
- Route:
  - `/memory`
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-892-memory-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - localizing shared Dashboard or Personality copy
  - translating backend/provider payload values
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: Polish Memory view still contains English
  route-owned body copy.
- Expected product or reliability outcome: static Memory route copy is owned by
  the existing localization structure.
- How success will be observed: build passes and a Polish Memory smoke no
  longer finds targeted English hardcoded phrases from PRJ-890.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused localization refactor for static Memory route copy.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend `UI_COPY.memory` for route-owned body strings and count units.
2. Replace hardcoded Memory route copy with `copy.memory` fields.
3. Run frontend build.
4. Run a Polish Memory smoke for targeted English phrase absence.
5. Update task board and project state.

## Acceptance Criteria
- Static Memory stat details, map labels, continuity rows, and signal cards use
  `copy.memory`.
- English behavior remains unchanged for the Memory route.
- Polish smoke confirms targeted Memory English phrases are absent.
- `npm run build` passes.

## Definition of Done
- [x] Memory static body copy uses `UI_COPY.memory`.
- [x] Build passes.
- [x] Polish Memory smoke passes.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new localization system
- broad shared Dashboard or Personality copy refactor
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-892-memory-body-copy-localization.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP Polish Memory copy smoke
  - result: passed
  - checked route-owned Polish strings, targeted English phrase absence,
    route path, and horizontal overflow
- Screenshots/logs:
  - `.codex/artifacts/prj892-memory-body-copy-localization/pl-memory-copy-smoke-v2.json`
  - `.codex/artifacts/prj892-memory-body-copy-localization/pl-memory-mobile-v2.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This slice only localizes Memory route-owned static copy.

## Result Report
- Task summary:
  - moved Memory route-owned static copy into `UI_COPY.memory`
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-892-memory-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - frontend build
  - Chrome CDP Polish Memory copy smoke with screenshot evidence
  - diff whitespace check
- What is incomplete:
  - shared recent-activity entries remain English and need a separate shared
    localization slice
- Next steps:
  - localize `/plans` and `/goals` route-owned body copy
- Decisions made:
  - keep shared recent-activity localization out of this route-owned slice

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - PRJ-890 found Memory route-owned English body copy in Polish UI mode.
- Gaps:
  - lower Memory sections were not fully backed by `UI_COPY`.
- Inconsistencies:
  - hero labels localized while map, continuity rows, and signal cards stayed
    partly English.
- Architecture constraints:
  - reuse `UI_COPY`; do not add a second localization system.

### 2. Select One Priority Task
- Selected task:
  - localize Memory route-owned body copy.
- Priority rationale:
  - next visible route-owned copy gap after Insights.
- Why other candidates were deferred:
  - Plans, Goals, and shared recent activity need separate focused slices.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - task and context docs
- Logic:
  - add Memory copy fields and build Memory route arrays from them.
- Edge cases:
  - singular/plural units should avoid obvious Polish grammar issues.

### 4. Execute Implementation
- Implementation notes:
  - localized Memory stat details, map labels, continuity rows, and signal
    cards
  - added localized count units for patterns, insights, and cues

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Chrome CDP Polish Memory copy smoke
  - screenshot review
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - inline Polish copy was rejected because it preserves the localization drift.
- Technical debt introduced: no
- Scalability assessment:
  - follows the route-specific `UI_COPY` pattern established by PRJ-888 through
    PRJ-891.
- Refinements made:
  - adjusted Polish wording for a calmer canonical tone.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-892-memory-body-copy-localization.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
