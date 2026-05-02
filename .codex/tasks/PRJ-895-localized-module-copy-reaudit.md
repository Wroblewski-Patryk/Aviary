# Task

## Header
- ID: PRJ-895
- Title: Localized Module Copy Reaudit
- Task Type: research
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-894
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 895
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-891 through PRJ-894 localized Insights, Memory, Plans, and Goals
route-owned body copy. Iteration 895 is a TESTER iteration, so the next
smallest useful task is a fresh rendered audit.

## Goal
Re-audit localized module routes in Polish UI mode and identify the next
highest-impact remaining route-owned copy gap.

## Scope
- Routes:
  - `/memory`
  - `/reflections`
  - `/plans`
  - `/goals`
  - `/insights`
  - `/automations`
  - `/integrations`
  - `/tools`
- Files:
  - `.codex/tasks/PRJ-895-localized-module-copy-reaudit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - code changes
  - translating backend/provider payload values
  - visual restyling

## Success Signal
- User or operator problem: remaining localized-copy work is unclear after
  several route fixes.
- Expected product or reliability outcome: the next implementation task is
  ranked from rendered evidence.
- How success will be observed: CDP audit artifact lists route excerpts,
  targeted English signals, and overflow status.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused audit artifact and source-of-truth update identifying the next
smallest route-localization task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Run a Polish authenticated shell CDP audit for module routes.
2. Mock only existing API responses needed to render those routes.
3. Record targeted English body-copy signals and overflow status.
4. Update task board and project state with the ranked next task.

## Acceptance Criteria
- Audit covers the declared module routes.
- Evidence records route, excerpt, targeted English signals, and overflow flag.
- Next smallest implementation task is identified.

## Definition of Done
- [x] Polish route audit passes without browser/runtime failure.
- [x] Audit evidence is saved under `.codex/artifacts`.
- [x] Task board and project state are updated.
- [x] No code changes are made for this audit task.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new localization system
- code changes
- translating backend/provider-supplied dynamic strings in this audit

## Validation Evidence
- Tests:
  - Chrome CDP Polish module copy reaudit
  - result: passed
  - `git diff --check -- .codex/tasks/PRJ-895-localized-module-copy-reaudit.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - route excerpts reviewed from audit output
- Screenshots/logs:
  - `.codex/artifacts/prj895-localized-module-copy-reaudit/localized-module-copy-reaudit.json`
- High-risk checks:
  - no code, runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
The next implementation slice should start with `/reflections`. Shared recent
activity and Tools provider/data-owned copy need separate ownership decisions.

## Result Report
- Task summary:
  - re-audited localized module routes after Goals, Plans, Memory, and
    Insights localization fixes.
- Files changed:
  - `.codex/tasks/PRJ-895-localized-module-copy-reaudit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - Chrome CDP Polish module copy reaudit.
- What is incomplete:
  - no copy fixes were made in this TESTER iteration.
- Next steps:
  - localize `/reflections` route-owned body copy.
- Decisions made:
  - rank `/reflections` first because it has the broadest remaining
    route-owned English signal set.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - `/reflections` still contains route-owned English copy across stat details,
    flow rows, prompts, and recent movement labels.
- Gaps:
  - shared recent activity remains English in `/memory`.
  - `/tools` still contains English mixed between route-owned labels and
    provider/data-owned values.
- Inconsistencies:
  - several routes are now clean for targeted signals, while Reflections still
    follows the older hardcoded-copy pattern.
- Architecture constraints:
  - route-owned strings should move into `UI_COPY`; data-owned strings require
    separate contract decisions.

### 2. Select One Priority Task
- Selected task:
  - audit remaining localized module copy.
- Priority rationale:
  - iteration 895 is a TESTER iteration and should strengthen evidence before
    another implementation slice.
- Why other candidates were deferred:
  - implementing Reflections without this confirmation would miss the updated
    post-Goals state.

### 3. Plan Implementation
- Files or surfaces to modify:
  - task and context docs only.
- Logic:
  - use CDP to render routes in Polish and record targeted English phrases.
- Edge cases:
  - provider/backend payload values may remain English and are noted separately.

### 4. Execute Implementation
- Implementation notes:
  - no code changes; audit used existing routes with mocked API responses.

### 5. Verify and Test
- Validation performed:
  - Chrome CDP audit across eight module routes.
- Result:
  - passed; all checked routes avoided horizontal overflow.

### 6. Self-Review
- Simpler option considered:
  - static source search was insufficient because rendered ownership matters.
- Technical debt introduced: no
- Scalability assessment:
  - the audit pattern can be repeated after each localization slice.
- Refinements made:
  - separated route-owned Reflections debt from shared activity and Tools
    ownership questions.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-895-localized-module-copy-reaudit.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
