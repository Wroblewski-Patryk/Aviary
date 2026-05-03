# Task

## Header
- ID: PRJ-1066
- Title: Audit next frontend cleanup after dashboard signal-column extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1065
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1066
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1065` extracted the dashboard signal-card column. The next frontend slice
should remain a visual-neutral component boundary cleanup.

## Goal
Select the next smallest frontend architecture cleanup after dashboard
signal-column extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/public-shell.tsx`
- `.codex/tasks/PRJ-1066-next-cleanup-after-dashboard-signal-column-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining repeated public and dashboard route maps.
2. Select exactly one small extraction candidate.
3. Confirm the candidate has an existing owner component module.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task avoids broader public hero/footer redesign.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Get-Content web/src/components/public-shell.tsx`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 3558 -First 60`
  - `git diff --check`
- Result: repeated public trust proof pill maps found; diff check passed.

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
- Task summary: selected `PublicTrustPillList` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: public shell inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1067.
- Next steps: add and reuse `PublicTrustPillList` for the two public proof
  pill lists.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: public micro-proof and proof-bridge lists both render
  `publicHomeSurface.trustBand.slice(0, 3)` with `PublicGlyph`.
- Gaps: `web/src/components/public-shell.tsx` owns glyph rendering but not the
  repeated trust-pill list shell.
- Inconsistencies: other repeated list shells now live in owner modules.
- Architecture constraints: do not alter public footer, hero layout, or
  route-owned public copy/data.

### 2. Select One Priority Task
- Selected task: PRJ-1067 extract `PublicTrustPillList`.
- Priority rationale: small repeated public-shell presentation boundary with an
  existing owner module.
- Why other candidates were deferred: public pillars, footer trust cards,
  dashboard figure/flow pieces, settings controls, tools groups, and route data
  helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: public-shell component owner, public route JSX,
  component map, docs/context.
- Logic: render `label/icon` trust items through a class-configurable list.
- Edge cases: preserve list, item, and icon classes for both call sites.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: public shell inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave the two public proof maps inline.
- Technical debt introduced: no
- Scalability assessment: selected wrapper improves ownership while keeping
  footer and hero structure untouched.
- Refinements made: scoped extraction to the two `slice(0, 3)` pill lists only.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
