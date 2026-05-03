# Task

## Header
- ID: PRJ-1067
- Title: Extract public trust-pill list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1066
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1067
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1066` selected repeated public proof pill lists that render the first three
trust-band items with `PublicGlyph`.

## Goal
Add and reuse `PublicTrustPillList` while preserving existing public proof
classes and route-owned public home data.

## Scope
- `web/src/components/public-shell.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1067-public-trust-pill-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PublicTrustPillList` to `web/src/components/public-shell.tsx`.
2. Replace public micro-proof and proof-bridge trust pill maps in `App.tsx`.
3. Keep footer trust-band cards and public home data in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Public micro-proof and proof-bridge lists use `PublicTrustPillList`.
- Existing wrapper, item, and icon classes are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared public trust-pill list component exists and is used by target
  sections.
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
- New shared pattern introduced: `PublicTrustPillList`
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
- Task summary: added `PublicTrustPillList` and reused it for public
  micro-proof and proof-bridge trust pill lists.
- Files changed: public-shell component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: public footer trust-card extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: two public proof lists duplicated the same trust-band glyph pill map.
- Gaps: public-shell component ownership covered glyphs but not trust pill
  lists.
- Inconsistencies: other repeated list shells now live in owner modules.
- Architecture constraints: keep public copy/data in `App()` and avoid footer
  changes.

### 2. Select One Priority Task
- Selected task: PRJ-1067.
- Priority rationale: selected by PRJ-1066 and limited to repeated
  presentation.
- Why other candidates were deferred: public footer cards, pillars, dashboard
  figure/flow pieces, settings controls, tools groups, and route data helpers
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: public-shell component owner, public route JSX,
  docs/context.
- Logic: render class-configured `label/icon` pills with `PublicGlyph`.
- Edge cases: preserve both call-site class sets and the `slice(0, 3)` data
  selection.

### 4. Execute Implementation
- Implementation notes: added `PublicTrustPillList` and replaced two inline
  maps.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract only a pill row and keep wrappers inline.
- Technical debt introduced: no
- Scalability assessment: configurable classes keep both public proof contexts
  stable without adding a new styling system.
- Refinements made: footer trust-band rendering was left untouched.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
