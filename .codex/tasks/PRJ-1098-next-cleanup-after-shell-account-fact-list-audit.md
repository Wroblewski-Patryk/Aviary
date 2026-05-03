# Task

## Header
- ID: PRJ-1098
- Title: Audit next frontend cleanup after shell account fact extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1097
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1098
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1097` moved shell account facts into `web/src/components/shell.tsx`.
Remaining maps include desktop sidebar nav, mobile route controls, settings
select options, tools directory behavior, and route data projections.

## Goal
Select the next smallest shell cleanup that keeps route state and navigation
effects in `App()` while moving repeated shell presentation into the shell owner.

## Scope
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining shell and control maps in `App.tsx`.
2. Select the lowest-risk shell-owned target.
3. Defer mobile route controls, settings option maps, tools directory, and data
   projections.
4. Sync docs/context.
5. Run diff validation.

## Acceptance Criteria
- [x] Exactly one next implementation target is selected.
- [x] Behaviorful/control/data-projection maps are deferred.
- [x] Source-of-truth files record the selected follow-up task.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Audit result is recorded.
- [x] Validation evidence is attached.

## Validation Evidence
- Tests: not applicable; audit-only slice.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "shellNavItems|aion-sidebar-nav|ShellNavButton|ROUTES.map|UI_LANGUAGE_OPTIONS.map|UTC_OFFSET_OPTIONS.map|toolsOverview\\?\\.groups" -Context 2,6`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 3770 -First 25`
  - `git diff --check`
- Result: `ShellNavButtonList` was selected for `PRJ-1099`; diff check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing desktop sidebar nav
- Fidelity target: structurally_faithful
- Existing shared pattern reused: authenticated shell component owner
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; audit-only
- Remaining mismatches: none introduced

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert documentation/context updates for this audit

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
- Task summary: selected desktop sidebar nav button-list extraction.
- Files changed:
  - `.codex/tasks/PRJ-1098-next-cleanup-after-shell-account-fact-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1099`.
- Next steps: implement `ShellNavButtonList`.
- Decisions made: keep `changeRoute`, active route state, and route item data in
  `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: desktop sidebar nav still maps `shellNavItems` inline in `App.tsx`.
- Gaps: shell owner has individual nav buttons but not the list wrapper.
- Inconsistencies: no behavior issue; only shell presentation ownership.
- Architecture constraints: keep route state and `changeRoute` in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1099` extract shell nav button list.
- Priority rationale: shell-owned wrapper around existing `ShellNavButton`
  with route callback passed from `App()`.
- Why other candidates were deferred: mobile route nav has refs/scroll state,
  settings option maps are form-control details, tools directory is
  side-effectful, and data projections are not presentation work.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/shell.tsx`,
  docs/context.
- Logic: render existing sidebar nav wrapper and buttons from route items.
- Edge cases: preserve disabled behavior and avoid calling navigation when
  `item.route` is missing.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave sidebar nav inline.
- Technical debt introduced: no
- Scalability assessment: shell-specific list keeps route-control ownership in
  `App()` while reducing inline presentation.
- Refinements made: mobile tabbar was deferred because it owns refs.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
