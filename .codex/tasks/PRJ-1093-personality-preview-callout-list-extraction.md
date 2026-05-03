# Task

## Header
- ID: PRJ-1093
- Title: Extract personality preview callout list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1092
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1093
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1092` selected the `/personality` hero preview callout map as the next
smallest frontend cleanup. The route data and hero stage layout remain owned by
`App()`.

## Goal
Move personality preview callout article presentation into the existing
personality component owner without changing callout data, classes, or visual
layout.

## Scope
- `web/src/App.tsx`
- `web/src/components/personality.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PersonalityPreviewCalloutList` to
   `web/src/components/personality.tsx`.
2. Replace the inline `personalityPreviewCallouts.map(...)` in `App.tsx`.
3. Keep callout data construction and hero stage layout in `App()`.
4. Sync docs/context.
5. Run frontend build, route smoke, and diff validation.

## Acceptance Criteria
- [x] `App.tsx` no longer maps personality preview callouts inline.
- [x] Existing callout classes and typography are preserved.
- [x] Callout data remains in `App()`.
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
  `route_count=14`, and diff check returned exit code 0.

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
- Screenshot comparison pass completed: no; markup-only extraction covered by
  build and route smoke
- Remaining mismatches: none introduced

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `PersonalityPreviewCalloutList` usage and docs/context
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
- Task summary: added `PersonalityPreviewCalloutList` and reused it for
  personality hero callouts.
- Files changed:
  - `.codex/tasks/PRJ-1093-personality-preview-callout-list-extraction.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/personality.tsx`
- How tested: frontend build, route smoke, and diff check passed.
- What is incomplete: nothing known.
- Next steps: audit the next smallest frontend cleanup.
- Decisions made: keep personality callout data and hero stage layout in
  `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: personality hero callout map was inline in `App.tsx`.
- Gaps: personality component owner lacked a callout-list wrapper.
- Inconsistencies: no runtime inconsistency; only presentation ownership.
- Architecture constraints: keep route data and stage layout in `App()`.

### 2. Select One Priority Task
- Selected task: extract `PersonalityPreviewCalloutList`.
- Priority rationale: smallest presentation-only extraction selected by
  `PRJ-1092`.
- Why other candidates were deferred: tools directory, shell navigation, form
  options, and route projections have broader ownership or behavior concerns.

### 3. Plan Implementation
- Files or surfaces to modify: `personality.tsx`, `App.tsx`, docs/context.
- Logic: render existing callout articles from explicit callout data.
- Edge cases: preserve caller-owned class names.

### 4. Execute Implementation
- Implementation notes: `PersonalityPreviewCalloutList` renders existing
  article typography and receives `personalityPreviewCallouts` from `App()`.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

### 6. Self-Review
- Simpler option considered: leave the callout map inline.
- Technical debt introduced: no
- Scalability assessment: route-specific wrapper avoids a generic decorative
  callout abstraction.
- Refinements made: hero figure wrapper remains in `App()` to avoid changing
  visual composition.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
