# Task

## Header
- ID: PRJ-1103
- Title: Extract settings select option list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1102
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1103
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1102` selected settings select option-list extraction. Settings state,
normalization, and `onChange` handlers remain owned by `App()`.

## Goal
Move repeated settings `<option>` rendering into the existing settings component
owner without changing select state, labels, or normalization behavior.

## Scope
- `web/src/App.tsx`
- `web/src/components/settings.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `SettingsSelectOptionList` to `web/src/components/settings.tsx`.
2. Replace UI language option map in `App.tsx`.
3. Replace UTC offset option map in `App.tsx`.
4. Keep select values, normalization, language-aware labels, and handlers in
   `App()`.
5. Sync docs/context.
6. Run frontend build, route smoke, and diff validation sequentially.

## Acceptance Criteria
- [x] `App.tsx` no longer maps UI language and UTC offset options inline.
- [x] Existing option values and labels are preserved.
- [x] Select state and handlers remain in `App()`.
- [x] Frontend validation passes.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Implementation is tiny, testable, and reversible.
- [x] No temporary solutions, mocks, bypasses, or duplicated logic were added.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Manual checks:
  - `git diff --check`
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14` after rerunning with a longer timeout, and diff check
  returned exit code 0.

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
- Design source reference: existing settings select options
- Fidelity target: structurally_faithful
- Existing shared pattern reused: settings component owner
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; markup-only extraction covered by
  build and route smoke
- Remaining mismatches: none introduced

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `SettingsSelectOptionList` usage and docs/context
  updates

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
- Task summary: added `SettingsSelectOptionList` and reused it for UI language
  and UTC offset selects.
- Files changed:
  - `.codex/tasks/PRJ-1103-settings-select-option-list-extraction.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/settings.tsx`
- How tested: frontend build, route smoke, and diff check passed.
- What is incomplete: nothing known.
- Next steps: audit the next smallest frontend cleanup.
- Decisions made: keep select values, normalization, and handlers in `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: settings select option maps were inline in `App.tsx`.
- Gaps: settings component owner lacked an option-list renderer.
- Inconsistencies: no behavior inconsistency; only option presentation.
- Architecture constraints: keep select state and normalization in `App()`.

### 2. Select One Priority Task
- Selected task: extract `SettingsSelectOptionList`.
- Priority rationale: smallest remaining settings-owned presentation map
  selected by `PRJ-1102`.
- Why other candidates were deferred: mobile tabbar owns refs, tools directory
  owns side effects, chat transcript owns message refs/rendering, and data
  projections are not presentation work.

### 3. Plan Implementation
- Files or surfaces to modify: `settings.tsx`, `App.tsx`, docs/context.
- Logic: render options from `{ value }` items and a caller label function.
- Edge cases: preserve language-aware option labels.

### 4. Execute Implementation
- Implementation notes: `SettingsSelectOptionList` is generic over
  `{ value: string }` and leaves label ownership at the call site.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14` after rerunning with a longer timeout, and diff check
  returned exit code 0.

### 6. Self-Review
- Simpler option considered: leave two option maps inline.
- Technical debt introduced: no
- Scalability assessment: bounded settings renderer avoids moving form state
  into the component.
- Refinements made: one renderer handles both language and UTC offset options.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
