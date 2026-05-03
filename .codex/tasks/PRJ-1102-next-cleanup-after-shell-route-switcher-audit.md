# Task

## Header
- ID: PRJ-1102
- Title: Audit next frontend cleanup after shell route switcher extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1101
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1102
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1101` moved the non-ref route-header switcher into the shell owner. The
remaining maps in `App.tsx` are now mostly data projections, chat transcript
mapping, tools directory behavior, the ref-owning mobile tabbar, and settings
select option maps.

## Goal
Select the next smallest cleanup that moves presentation-only markup while
keeping form state, normalization, and side effects in `App()`.

## Scope
- `web/src/App.tsx`
- `web/src/components/settings.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining maps after route switcher extraction.
2. Inspect settings select option maps.
3. Select a small settings-owned option renderer and defer behaviorful maps.
4. Sync docs/context.
5. Run diff validation.

## Acceptance Criteria
- [x] Exactly one next implementation target is selected.
- [x] Behaviorful/ref-owning/data-projection maps are deferred.
- [x] Source-of-truth files record the selected follow-up task.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Audit result is recorded.
- [x] Validation evidence is attached.

## Validation Evidence
- Tests: not applicable; audit-only slice.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,5`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 4640 -First 75`
  - `Get-Content web/src/components/settings.tsx`
  - `git diff --check`
- Result: `SettingsSelectOptionList` was selected for `PRJ-1103`; diff check
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
- Design source reference: existing settings select option rendering
- Fidelity target: structurally_faithful
- Existing shared pattern reused: settings component owner
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
- Task summary: selected settings select option-list extraction.
- Files changed:
  - `.codex/tasks/PRJ-1102-next-cleanup-after-shell-route-switcher-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1103`.
- Next steps: implement `SettingsSelectOptionList`.
- Decisions made: keep select state, normalization, and `onChange` handlers in
  `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: settings select option maps remain inline in `App.tsx`.
- Gaps: settings owner lacks a tiny option-list renderer.
- Inconsistencies: no behavior inconsistency; only form option presentation.
- Architecture constraints: keep state, normalization, and handlers in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1103` extract settings select option list.
- Priority rationale: smallest remaining presentation-only map with existing
  settings owner.
- Why other candidates were deferred: mobile tabbar owns refs, tools directory
  owns side effects, chat transcript owns message refs/rendering, and route
  projections are data shaping.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/settings.tsx`,
  docs/context.
- Logic: render option elements from `{ value }` items and a label callback.
- Edge cases: preserve current labels for UI language and UTC offset.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave option maps inline.
- Technical debt introduced: no
- Scalability assessment: settings-specific option renderer is bounded and does
  not move form control ownership.
- Refinements made: one option renderer covers both language and UTC options.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
