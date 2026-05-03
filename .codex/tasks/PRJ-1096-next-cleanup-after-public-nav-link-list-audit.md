# Task

## Header
- ID: PRJ-1096
- Title: Audit next frontend cleanup after public nav link extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1095
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1096
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1095` moved public nav links into the public-shell owner. Remaining inline
maps include shell account facts, route navigation controls, settings select
options, tools directory behavior, and route data projections.

## Goal
Select the next smallest cleanup that moves repeated presentation without
changing route state, account data, navigation behavior, or form behavior.

## Scope
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining maps after public nav extraction.
2. Compare shell account facts against existing shell component ownership.
3. Select one display-only target and defer behaviorful/control maps.
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
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,5`
  - `Get-Content web/src/components/shell.tsx`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 3835 -First 115`
  - `git diff --check`
- Result: `ShellAccountFactList` was selected for `PRJ-1097`; diff check
  passed.

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
- Design source reference: existing desktop popover and mobile account fact
  renderings
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
- Task summary: selected shell account fact-list extraction.
- Files changed:
  - `.codex/tasks/PRJ-1096-next-cleanup-after-public-nav-link-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1097`.
- Next steps: implement `ShellAccountFactList`.
- Decisions made: defer route navigation controls, settings option maps, tools
  directory behavior, and route data projections.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `accountSummaryItems` is mapped inline in both desktop and mobile
  account panels.
- Gaps: shell owner lacks a small fact-list wrapper with desktop/mobile variants.
- Inconsistencies: no behavior issue; only repeated presentation.
- Architecture constraints: keep account data and account panel state in
  `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1097` extract shell account fact list.
- Priority rationale: repeated display-only account facts with an existing
  shell owner.
- Why other candidates were deferred: route nav maps are behaviorful, form
  option maps are control-specific, tools directory includes side-effect hooks,
  and data projections are not presentation extraction targets.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/shell.tsx`,
  docs/context.
- Logic: render account fact items with existing desktop and mobile classes.
- Edge cases: preserve both current wrappers and the sign-out/settings actions
  outside the new component.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave both maps inline.
- Technical debt introduced: no
- Scalability assessment: shell-specific variant avoids a generic fact-list
  abstraction.
- Refinements made: selected the repeated display list rather than shell nav
  controls.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
