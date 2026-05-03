# Task

## Header
- ID: PRJ-1100
- Title: Audit next frontend cleanup after shell nav button extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1099
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1100
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1099` moved the desktop sidebar nav map into the shell owner. Remaining
maps include mobile/tablet route switchers, settings form options, tools
directory behavior, chat transcript mapping, and route data projections.

## Goal
Select the next smallest cleanup that can reuse the same shell-owned route-nav
boundary without moving route state, refs, or side effects out of `App()`.

## Scope
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining route/control maps.
2. Select a route-switcher target without refs or side-effectful logic.
3. Defer lower mobile tabbar, settings options, tools directory, chat transcript,
   and data projections.
4. Sync docs/context.
5. Run diff validation.

## Acceptance Criteria
- [x] Exactly one next implementation target is selected.
- [x] Ref-owning, behaviorful, and data-projection maps are deferred.
- [x] Source-of-truth files record the selected follow-up task.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Audit result is recorded.
- [x] Validation evidence is attached.

## Validation Evidence
- Tests: not applicable; audit-only slice.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,5`
  - `Select-String -Path web/src/App.tsx -Pattern "shellNavItems|aion-sidebar-nav|ShellNavButton|ROUTES.map|UI_LANGUAGE_OPTIONS.map|UTC_OFFSET_OPTIONS.map|toolsOverview\\?\\.groups" -Context 2,6`
  - `git diff --check`
- Result: `ShellRouteSwitcher` was selected for `PRJ-1101`; diff check passed.

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
- Design source reference: existing route switcher inside mobile route header
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
- Task summary: selected shell route switcher extraction for the route header.
- Files changed:
  - `.codex/tasks/PRJ-1100-next-cleanup-after-shell-nav-button-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1101`.
- Next steps: implement `ShellRouteSwitcher`.
- Decisions made: defer the bottom mobile tabbar because it owns refs.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: tablet route switcher still maps `ROUTES` inline in `App.tsx`.
- Gaps: shell owner lacks a simple route-switcher wrapper separate from the
  ref-owning bottom mobile tabbar.
- Inconsistencies: no behavior issue; only shell presentation ownership.
- Architecture constraints: keep route state, route labels, and route changes
  in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1101` extract shell route switcher.
- Priority rationale: small route-control wrapper with no refs and clear route
  smoke coverage.
- Why other candidates were deferred: bottom mobile tabbar owns refs, settings
  options are form-control details, tools directory includes side effects, chat
  transcript owns message refs/rendering, and route projections are data shaping.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/shell.tsx`,
  docs/context.
- Logic: render the existing border wrapper, scroll row, and route buttons from
  explicit route labels.
- Edge cases: preserve active button classes and route callback.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave route switcher inline.
- Technical debt introduced: no
- Scalability assessment: shell-specific route switcher avoids moving route
  constants or labels into shell.
- Refinements made: selected the non-ref switcher, not the lower tabbar.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
