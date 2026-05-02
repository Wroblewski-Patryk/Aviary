# Task

## Header
- ID: PRJ-900
- Title: Memory Zero Count Polish Forms
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-899
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 900
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-899 final reaudit found one remaining route-owned Polish grammar defect: `/memory` renders `0 wnioski`.

## Goal
Fix zero-count Polish unit forms in the Memory route while preserving the existing `UI_COPY.memory` pattern.

## Success Signal
- User or operator problem: Polish Memory route shows rough zero-count grammar.
- Expected product or reliability outcome: Memory count labels read naturally for zero, one, and plural cases.
- How success will be observed: build passes and the final module-copy reaudit no longer finds `0 wnioski`.
- Post-launch learning needed: no

## Deliverable For This Stage
Implementation, verification, and context updates for the Memory zero-count grammar fix.

## Scope
- `web/src/App.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-900-memory-zero-count-polish-forms.md`

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add zero-count unit suffixes to `UI_COPY.memory` for English, Polish, and German.
2. Use zero-aware unit selection for Memory pattern, insight, and cue counts.
3. Run the web build.
4. Rerun the final localized module-copy reaudit.
5. Update task and context evidence.

## Acceptance Criteria
- `/memory` renders `0 wniosków` instead of `0 wnioski` in Polish.
- Existing singular/plural behavior remains intact.
- Build and reaudit evidence are recorded.

## Definition of Done
- [x] Memory zero-count unit forms are localized through `UI_COPY.memory`.
- [x] `Push-Location .\web; npm run build; Pop-Location` passes.
- [x] PRJ-899 final reaudit passes after the fix.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests: `Push-Location .\web; npm run build; Pop-Location` passed.
- Manual checks: PRJ-899 final localized module-copy reaudit passed after this fix.
- Screenshots/logs: `.codex/artifacts/prj899-localized-module-copy-final-reaudit/localized-module-copy-final-reaudit.json`
- High-risk checks: frontend copy only
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Result Report
- Task summary: Added zero-count Memory unit suffixes and zero-aware count selection.
- Files changed: `web/src/App.tsx`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/context/LEARNING_JOURNAL.md`, `.codex/tasks/PRJ-900-memory-zero-count-polish-forms.md`
- How tested: web production build and final localized module-copy reaudit.
- What is incomplete: nothing for this slice.
- Next steps: move to the next product-usability slice after localization closure.
- Decisions made: mirrored the Reflections zero-count pattern in Memory.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/memory` shows `0 wnioski`.
- Gaps: Memory lacks zero-count copy keys unlike Reflections.
- Inconsistencies: Reflections has zero-aware Polish count copy; Memory does not.
- Architecture constraints: reuse `UI_COPY.memory`.

### 2. Select One Priority Task
- Selected task: PRJ-900 Memory Zero Count Polish Forms.
- Priority rationale: PRJ-899 found it as the only targeted remaining route-owned defect.
- Why other candidates were deferred: final audit completion depends on this fix.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, task/context docs.
- Logic: add zero suffixes and zero-aware unit selection.
- Edge cases: keep English and German behavior unchanged in meaning.

### 4. Execute Implementation
- Implementation notes: Added zero-count suffixes for Memory pattern, insight, and cue units in English, Polish, and German; updated Memory unit selection to use zero-aware labels.

### 5. Verify and Test
- Validation performed: `Push-Location .\web; npm run build; Pop-Location`; PRJ-899 final localized module-copy reaudit.
- Result: passed.

### 6. Self-Review
- Simpler option considered: special-casing only Polish in JSX, but adding copy keys keeps the localization contract consistent.
- Technical debt introduced: no
- Scalability assessment: consistent with Reflections zero-count handling.
- Refinements made: none after successful reaudit.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-900-memory-zero-count-polish-forms.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: yes; Chrome CDP cleanup pitfall recorded during the final reaudit cycle.
