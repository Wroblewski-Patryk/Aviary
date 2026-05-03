# Task

## Header
- ID: PRJ-1072
- Title: Audit next frontend cleanup after public footer trust-band extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1071
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1072
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1071` completed the public shell trust-band extraction. The remaining
frontend cleanup should return to a small dashboard presentational list instead
of broad route/data movement.

## Goal
Select the next smallest frontend cleanup after public footer trust-band
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `.codex/tasks/PRJ-1072-next-cleanup-after-public-trust-band-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining dashboard presentational maps.
2. Select exactly one small extraction candidate.
3. Confirm the candidate fits `web/src/components/dashboard.tsx`.
4. Record deferred broader or more visual-sensitive candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task avoids dashboard hero/layout changes and dynamic chart
  behavior.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Get-Content web/src/components/dashboard.tsx`
  - `Get-Content web/src/App.tsx | Select-Object -Skip 4058 -First 45`
  - `git diff --check`
- Result: dashboard reflection-row map found; diff check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: dashboard component owner
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
- Task summary: selected `DashboardReflectionList` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: dashboard route/component inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1073.
- Next steps: add and reuse `DashboardReflectionList`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard reflection highlight rows remain inline in `App.tsx`.
- Gaps: dashboard component owner covers signal and progress lists but not the
  reflection-row list.
- Inconsistencies: adjacent small dashboard presentation has been extracted.
- Architecture constraints: avoid dashboard hero/layout changes and leave
  dynamic memory bars deferred.

### 2. Select One Priority Task
- Selected task: PRJ-1073 extract `DashboardReflectionList`.
- Priority rationale: small, static-shape dashboard list with a clear owner.
- Why other candidates were deferred: memory bars use dynamic inline height;
  guidance rows include CTA behavior; figure/flow pieces and route data helpers
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  component map, docs/context.
- Logic: render `title/tag` rows through a shared dashboard list.
- Edge cases: preserve `aion-dashboard-reflection-*` classes and wrapper
  spacing.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: dashboard route/component inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract memory bars first.
- Technical debt introduced: no
- Scalability assessment: selected list is less visual-sensitive than the bar
  chart and keeps the slice reversible.
- Refinements made: dynamic chart extraction remains deferred.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
