# Task

## Header
- ID: PRJ-886
- Title: Sidebar Localized Module Labels
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-885
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 886
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The canonical module routes are now enabled, but their sidebar labels still use
English string literals for several modules even though `UI_COPY.routes` already
contains localized labels.

## Goal
Make the authenticated sidebar and mobile tabbar use existing route localization
for all canonical module route labels.

## Scope
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-886-sidebar-localized-module-labels.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - new translations
  - visual redesign
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: Polish/German shell users see English labels for
  newly enabled canonical modules.
- Expected product or reliability outcome: sidebar and mobile tabbar labels
  remain consistent with the selected UI language.
- How success will be observed: build passes and a Polish smoke confirms module
  labels render from `routeLabel`.
- Post-launch learning needed: no

## Deliverable For This Stage
One small frontend fix replacing hardcoded module labels with existing
`routeLabel` calls.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Replace hardcoded sidebar labels for module routes with `routeLabel`.
2. Run frontend build.
3. Run a focused Polish shell smoke.
4. Update task board and project state.

## Acceptance Criteria
- Memory, Reflections, Plans, Goals, Insights, Automations, and Integrations
  labels use `routeLabel`.
- Existing English behavior remains unchanged.
- Polish route labels render in the authenticated shell.
- `npm run build` passes.

## Definition of Done
- [x] Labels use the existing localization helper.
- [x] Build passes.
- [x] Polish smoke passes.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated route-label logic
- temporary bypasses or hardcoded language branches
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-886-sidebar-localized-module-labels.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Polish authenticated shell smoke passed with expected labels:
    - `Pamięć`
    - `Refleksje`
    - `Plany`
    - `Cele`
    - `Wnioski`
    - `Automatyzacje`
    - `Integracje`
- Screenshots/logs:
  - `.codex/artifacts/prj886-sidebar-localized-module-labels/pl-sidebar-smoke-v2.json`
  - `.codex/artifacts/prj886-sidebar-localized-module-labels/pl-dashboard-sidebar-desktop-v2.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This is a localization consistency fix for the canonical shell.

## Result Report

- Task summary: Replaced hardcoded canonical module sidebar labels with
  existing `routeLabel` calls.
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-886-sidebar-localized-module-labels.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - Chrome CDP Polish sidebar smoke
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-886-sidebar-localized-module-labels.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - no new translations were added
- Next steps:
  - rerun final route smoke only if more shell navigation changes are made
- Decisions made:
  - reuse `UI_COPY.routes` as the single source for route labels.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: newly enabled module labels were hardcoded in English.
- Gaps: localized labels existed but were not used in `shellNavItems`.
- Inconsistencies: first-class routes used `routeLabel`, while module routes did
  not.
- Architecture constraints: use existing localization helper; no new language
  system.

### 2. Select One Priority Task
- Selected task: PRJ-886 Sidebar Localized Module Labels.
- Priority rationale: this is a small canonical shell polish with low risk and
  visible user impact.
- Why other candidates were deferred: larger visual or release work should not
  be mixed into this focused fix.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, task and context docs.
- Logic: replace literals with `routeLabel(route, resolvedUiLanguage)`.
- Edge cases: preserve English labels when English is selected.
- Validation path: build and Polish UI smoke.

### 4. Execute Implementation
- Implementation notes:
  - updated Memory, Reflections, Plans, Goals, Insights, Automations, and
    Integrations labels to use `routeLabel`

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Polish sidebar smoke
  - screenshot evidence
  - diff hygiene
- Result: passed

### 6. Self-Review
- Simpler option considered: leave English labels because routes are functional.
- Technical debt introduced: no.
- Scalability assessment: all canonical route labels now share the same helper.
- Refinements made: reran the Polish smoke with Unicode escapes after an inline
  PowerShell encoding issue in the first test script.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-886-sidebar-localized-module-labels.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
