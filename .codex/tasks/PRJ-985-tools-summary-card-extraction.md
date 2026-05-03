# Task

## Header
- ID: PRJ-985
- Title: Extract tools summary card component cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-984
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 985
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The tools route still rendered its summary-card markup inline in
`web/src/App.tsx` after tool formatting helpers were extracted.

## Goal

Move tools summary card presentation into a dedicated tools component module
without changing tools overview data or route behavior.

## Scope

- `web/src/App.tsx`
- `web/src/components/tools.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: tools summary presentation was hidden in the app
  monolith.
- Expected product or reliability outcome: tools route component ownership is
  clearer while tools overview data remains in `App()`.
- How success will be observed: build and full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `ToolsSummaryCard` to `web/src/components/tools.tsx`.

## Constraints
- use existing systems and approved mechanisms
- do not move tools overview API calls or state out of `App()`
- do not alter labels, values, route behavior, or visual classes
- do not open a visible browser window

## Implementation Plan
1. Add `web/src/components/tools.tsx`.
2. Move tools summary-card markup into `ToolsSummaryCard`.
3. Keep summary data construction in `App()`.
4. Run web build and full route smoke.
5. Update docs and context.

## Acceptance Criteria
- Tools summary card markup no longer lives inline in `App.tsx`.
- `web/src/components/tools.tsx` owns `ToolsSummaryCard`.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Tools summary card extracted.
- [x] Tools overview state and API behavior remain in `App()`.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - confirmed `/tools` uses `ToolsSummaryCard`
- High-risk checks:
  - tools overview data construction was untouched
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - route map now records tools component ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing tools summary-card markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Remaining mismatches: tools item cards still live in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: inline `ToolsSummaryCard` markup back into `App.tsx`
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

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

- Task summary: moved tools summary-card markup into
  `web/src/components/tools.tsx`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/tools.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - tools item cards still live in `App.tsx`
- Next steps:
  - extract a tools item fact-card component or tools details component cluster
- Decisions made:
  - keep tools summary data construction in `App()`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: tools summary-card markup remained inline.
- Gaps: tools item rendering remains large.
- Inconsistencies: tools component ownership had not started.
- Architecture constraints: keep tools state/API in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-985 tools summary card extraction.
- Priority rationale: small pure tools route component protected by full smoke.
- Why other candidates were deferred: tools item cards include toggle/linking
  state and need a narrower follow-up.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/tools.tsx`, docs/context.
- Logic: move pure summary card markup.
- Edge cases: summary values remain preformatted strings.

### 4. Execute Implementation
- Implementation notes: extracted only stateless markup.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave summary cards inline.
- Technical debt introduced: no
- Scalability assessment: tools component ownership can now grow gradually.
- Refinements made: avoided moving tools API/state.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
