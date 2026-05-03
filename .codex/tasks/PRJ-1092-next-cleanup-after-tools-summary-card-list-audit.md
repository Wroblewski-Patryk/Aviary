# Task

## Header
- ID: PRJ-1092
- Title: Audit next frontend cleanup after tools summary card extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1091
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1092
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1091` moved the tools summary card list into the tools component owner.
The remaining inline maps in `App.tsx` now include state/data projections,
navigation, form options, behaviorful tools directory cards, and a few
presentation-only visual clusters.

## Goal
Select the next smallest frontend cleanup that improves presentation ownership
without changing route state, side effects, or canonical visuals.

## Scope
- `web/src/App.tsx`
- `web/src/components/personality.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: `App.tsx` still owns small visual maps that obscure
  route behavior.
- Expected product or reliability outcome: one next presentation-only target is
  ready for implementation.
- How success will be observed: a concrete follow-up task is selected and
  larger/behaviorful maps are deferred.
- Post-launch learning needed: no

## Deliverable For This Stage
An audit result selecting exactly one implementation target for the next slice.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect remaining `App.tsx` maps after tools summary extraction.
2. Inspect the personality component owner and current hero callout markup.
3. Select one presentation-only target.
4. Sync source-of-truth planning and context.
5. Run diff validation.

## Acceptance Criteria
- [x] Exactly one next implementation target is selected.
- [x] Behaviorful maps are explicitly deferred.
- [x] Source-of-truth files record the selected follow-up task.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Audit result is recorded in source-of-truth files.
- [x] Validation evidence is attached.

## Validation Evidence
- Tests: not applicable; audit-only slice.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\\.map\\(" -Context 1,4`
  - `Get-Content web/src/components/personality.tsx`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 4990 -First 70`
  - `git diff --check`
- Result: `PersonalityPreviewCalloutList` was selected for `PRJ-1093`; diff
  check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing `/personality` hero callout implementation
- Canonical visual target: preserve current callout articles and classes
- Fidelity target: structurally_faithful
- Existing shared pattern reused: personality route component owner
- New shared pattern introduced: no
- Design-memory update required: no
- Screenshot comparison pass completed: no; audit-only
- Remaining mismatches: none introduced
- State checks: success
- Accessibility checks: no interactive markup change
- Parity evidence: target preserves existing class names and text structure

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
- Task summary: selected personality hero preview callout list extraction.
- Files changed:
  - `.codex/tasks/PRJ-1092-next-cleanup-after-tools-summary-card-list-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested: inspected candidate code and ran `git diff --check`.
- What is incomplete: implementation is intentionally deferred to `PRJ-1093`.
- Next steps: implement `PersonalityPreviewCalloutList`.
- Decisions made: defer behaviorful tools directory, shell navigation, form
  option maps, and route data projections.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: personality hero callout map remains inline in `App.tsx`.
- Gaps: personality component owner lacks a callout-list wrapper.
- Inconsistencies: no runtime inconsistency; only presentation ownership.
- Architecture constraints: keep callout data in `App()`, move markup only.

### 2. Select One Priority Task
- Selected task: `PRJ-1093` extract personality preview callout list.
- Priority rationale: display-only and owned by an existing route module.
- Why other candidates were deferred: tools directory contains actions;
  navigation/form maps are shell or control-specific; data projections are not
  presentation extraction targets.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/personality.tsx`,
  docs/context.
- Logic: render existing callout articles from explicit callout data.
- Edge cases: preserve caller-owned `className` values.

### 4. Execute Implementation
- Implementation notes: audit only; no runtime code changed.

### 5. Verify and Test
- Validation performed: code inspection and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave hero callouts inline.
- Technical debt introduced: no
- Scalability assessment: route-specific wrapper avoids a premature generic
  visual callout abstraction.
- Refinements made: selected an architecture-mode target that respects flagship
  visual ownership.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
