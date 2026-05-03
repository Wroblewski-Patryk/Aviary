# Task

## Header
- ID: PRJ-1068
- Title: Audit next frontend cleanup after public trust-pill list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1067
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1068
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1067` moved repeated public trust proof pills into
`PublicTrustPillList`. The public route still has a presentational feature
strip map that belongs to the same public-shell owner.

## Goal
Select the next smallest frontend cleanup after public trust-pill list
extraction without changing public copy, data, or layout.

## Scope
- `web/src/App.tsx`
- `web/src/components/public-shell.tsx`
- `.codex/tasks/PRJ-1068-next-cleanup-after-public-trust-pill-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining public route presentation maps after PRJ-1067.
2. Select exactly one small extraction candidate.
3. Confirm the candidate fits `web/src/components/public-shell.tsx`.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task avoids public footer, hero, copy, or data changes.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "publicHomeSurface.pillars|publicHomeSurface.trustBand" -Context 1,5`
  - `Get-Content web/src/components/public-shell.tsx`
  - `git diff --check`
- Result: public feature-strip map found; diff check passed.

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
- Task summary: selected `PublicFeatureCardList` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: public route/component inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1069.
- Next steps: add and reuse `PublicFeatureCardList` for the public feature
  strip.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: public feature-strip card markup remains inline in `App.tsx`.
- Gaps: `web/src/components/public-shell.tsx` owns public glyph/proof helpers
  but not the adjacent feature-card list shell.
- Inconsistencies: other public proof list presentation now lives in
  `public-shell.tsx`.
- Architecture constraints: keep public route data and copy in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1069 extract `PublicFeatureCardList`.
- Priority rationale: smallest public-shell presentation boundary still visible
  after trust-pill extraction.
- Why other candidates were deferred: footer trust cards, dashboard figure/flow
  pieces, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: public-shell component owner, public route JSX,
  component map, docs/context.
- Logic: render `icon/title/body` feature cards through a shared list wrapper.
- Edge cases: preserve `aion-public-feature-*` classes and route-owned data.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: public route/component inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave the feature strip inline until a full public
  shell extraction.
- Technical debt introduced: no
- Scalability assessment: selected wrapper stays inside an existing owner
  module and avoids public layout changes.
- Refinements made: footer trust cards remain deferred because they use a
  different article shape.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
