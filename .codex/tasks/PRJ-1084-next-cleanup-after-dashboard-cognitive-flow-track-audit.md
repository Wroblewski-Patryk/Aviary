# Task

## Header
- ID: PRJ-1084
- Title: Audit next frontend cleanup after dashboard cognitive flow-track extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1083
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1084
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1083` extracted the dashboard cognitive flow track. The dashboard hero
figure still maps a small set of figure notes inline while halo, image, and
badge remain separate shell elements.

## Goal
Select the next smallest frontend cleanup after dashboard cognitive flow-track
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `.codex/tasks/PRJ-1084-next-cleanup-after-dashboard-cognitive-flow-track-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect the dashboard hero figure note map.
2. Select exactly one small extraction candidate.
3. Confirm the candidate does not move the full hero figure stage.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task preserves existing note classes and leaves image/badge
  layout untouched.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "dashboardFigureNotes|aion-dashboard-figure-note" -Context 1,5`
  - `git diff --check`
- Result: dashboard figure note map found; diff check passed.

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
- Task summary: selected `DashboardFigureNoteList` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: dashboard figure note inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1085.
- Next steps: add and reuse `DashboardFigureNoteList`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard figure notes remain inline in `App.tsx`.
- Gaps: dashboard component owner does not cover the figure note list.
- Inconsistencies: other dashboard repeated presentation maps now have wrappers.
- Architecture constraints: do not move the full hero figure stage, image,
  halo, or badge in this slice.

### 2. Select One Priority Task
- Selected task: PRJ-1085 extract `DashboardFigureNoteList`.
- Priority rationale: small note-list extraction with no layout or data changes.
- Why other candidates were deferred: full hero figure stage, current phase
  panel, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  component map, docs/context.
- Logic: render `className/eyebrow/title/body` notes through a shared list.
- Edge cases: preserve caller-owned note class names.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: dashboard figure note inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: move the full figure stage.
- Technical debt introduced: no
- Scalability assessment: note-only extraction keeps flagship hero layout
  stable.
- Refinements made: halo, image, and badge remain inline.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
