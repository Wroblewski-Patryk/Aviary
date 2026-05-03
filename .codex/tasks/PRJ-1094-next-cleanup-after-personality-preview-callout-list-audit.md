# Task

## Header
- ID: PRJ-1094
- Title: Audit next frontend cleanup after personality preview callout extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1093
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1094
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1093` moved personality hero callouts into the personality component
owner. Remaining maps in `App.tsx` include route data projections, shell nav,
form options, behaviorful tools directory cards, and a small public-home nav
link list.

## Goal
Select the next smallest presentation-only cleanup that improves component
ownership without changing route behavior.

## Scope
- `web/src/App.tsx`
- `web/src/components/public-shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining `App.tsx` maps.
2. Compare candidates against existing component owners.
3. Select one display-only target.
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
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - `Get-Content web/src/components/public-shell.tsx`
  - `git diff --check`
- Result: `PublicNavLinkList` was selected for `PRJ-1095`; diff check passed.

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
- Design source reference: existing public-home nav link implementation
- Fidelity target: structurally_faithful
- Existing shared pattern reused: public-shell component owner
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
- Task summary: selected public home nav link-list extraction.
- Files changed:
  - `.codex/tasks/PRJ-1094-next-cleanup-after-personality-preview-callout-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1095`.
- Next steps: implement `PublicNavLinkList`.
- Decisions made: defer tools directory, shell account facts, form option maps,
  shell route navigation, and route data projections.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: public-home nav links remain inline in `App.tsx`.
- Gaps: public-shell owner lacks a nav-link list wrapper.
- Inconsistencies: no runtime inconsistency; only presentation ownership.
- Architecture constraints: keep public copy/data in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1095` extract public nav link list.
- Priority rationale: display-only list with existing public-shell owner.
- Why other candidates were deferred: remaining candidates are behaviorful,
  control-specific, shell-wide, or data projections.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/public-shell.tsx`,
  docs/context.
- Logic: render existing nav wrapper and anchors from string labels.
- Edge cases: preserve current `href="#aviary-home"` behavior.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave nav links inline.
- Technical debt introduced: no
- Scalability assessment: public-specific wrapper avoids generic navigation
  abstraction.
- Refinements made: selected a small route-local target over shell-wide maps.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
