# Task

## Header
- ID: PRJ-1070
- Title: Audit next frontend cleanup after public feature-card list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1069
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1070
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1069` moved the public feature strip into `PublicFeatureCardList`. The
remaining public footer trust-band list is a separate article shape with the
same public-shell owner.

## Goal
Select the next smallest frontend cleanup after public feature-card list
extraction without changing public footer content or layout.

## Scope
- `web/src/App.tsx`
- `web/src/components/public-shell.tsx`
- `.codex/tasks/PRJ-1070-next-cleanup-after-public-feature-card-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect the remaining public footer trust-band map.
2. Select exactly one small extraction candidate.
3. Confirm the candidate fits `web/src/components/public-shell.tsx`.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task avoids public copy/data changes.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Get-Content web/src/App.tsx | Select-Object -Skip 3604 -First 25`
  - `Select-String -Path web/src/App.tsx -Pattern "publicHomeSurface.trustBand|aion-public-trust" -Context 1,5`
  - `git diff --check`
- Result: public footer trust-band map found; diff check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: `PublicGlyph`
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; audit-only task

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report
- Task summary: selected `PublicTrustBand` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: public footer inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1071.
- Next steps: add and reuse `PublicTrustBand` for the public footer trust-band
  list.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: public footer trust-band card markup remains inline in `App.tsx`.
- Gaps: public-shell owner now has feature and proof list helpers but not the
  footer trust-band shell.
- Inconsistencies: public route presentation is partially extracted.
- Architecture constraints: keep public route copy/data in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1071 extract `PublicTrustBand`.
- Priority rationale: small public-shell presentation cleanup with a clear owner
  and no data changes.
- Why other candidates were deferred: dashboard figure/flow pieces, settings
  controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: public-shell component owner, public route JSX,
  component map, docs/context.
- Logic: render `label/icon` footer trust articles through `PublicGlyph`.
- Edge cases: preserve footer, item, icon, and label markup/classes.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: public footer inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: reuse `PublicTrustPillList`.
- Technical debt introduced: no
- Scalability assessment: a dedicated footer component avoids overloading the
  pill-list semantics.
- Refinements made: selected a distinct component because footer cards use an
  article structure.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
