# Task

## Header
- ID: PRJ-1071
- Title: Extract public footer trust band
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1070
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1071
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1070` selected the public footer trust-band map as a distinct public-shell
component extraction.

## Goal
Add and reuse `PublicTrustBand` while preserving footer semantics, public trust
classes, glyph rendering, and route-owned public home data.

## Scope
- `web/src/components/public-shell.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1071-public-trust-band-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PublicTrustBand` to `web/src/components/public-shell.tsx`.
2. Replace the public footer trust-band map in `App.tsx`.
3. Keep public home copy/data in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Public footer uses `PublicTrustBand`.
- Existing footer element, `aion-public-trust-*` classes, and `PublicGlyph`
  rendering are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared public trust-band component exists and is used by the target
  section.
- [x] Frontend build passes.
- [x] Full route smoke passes.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Manual checks:
  - `git diff --check`
- Result: passed; route smoke reported `status=ok`, `route_count=14`.

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
- New shared pattern introduced: `PublicTrustBand`
- Screenshot comparison pass completed: no; no intentional visual change

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
- Task summary: added `PublicTrustBand` and reused it for the public footer
  trust-band.
- Files changed: public-shell component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: dashboard figure/flow extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: public footer trust-band article markup was still inline in `App.tsx`.
- Gaps: public-shell owner had proof and feature helpers but not the footer
  trust-band shell.
- Inconsistencies: public route presentation ownership was still split.
- Architecture constraints: keep public copy/data in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1071.
- Priority rationale: selected by PRJ-1070 and limited to public presentation.
- Why other candidates were deferred: dashboard figure/flow pieces, settings
  controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: public-shell component owner, public route JSX,
  docs/context.
- Logic: render `label/icon` footer articles through `PublicGlyph`.
- Edge cases: preserve footer semantics and existing CSS classes.

### 4. Execute Implementation
- Implementation notes: added `PublicTrustBand` and replaced the inline footer
  trust-band map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: reuse `PublicTrustPillList`.
- Technical debt introduced: no
- Scalability assessment: dedicated component preserves footer semantics and
  keeps public-shell ownership cohesive.
- Refinements made: kept public home data in `App()`.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
