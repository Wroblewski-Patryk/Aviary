# Task

## Header
- ID: PRJ-987
- Title: Extract tools detail-card component cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-986
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 987
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The tools route still rendered current-status and next-step detail-card chrome
inline in `web/src/App.tsx` after the summary and fact-card extractions.

## Goal

Move tools detail-card presentation into the tools component module without
changing status text, next-action summarization, or Telegram linking behavior.

## Scope

- `web/src/App.tsx`
- `web/src/components/tools.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: tools detail cards were still hidden in the app
  monolith.
- Expected product or reliability outcome: tools route presentation ownership
  becomes clearer while tools actions remain stable.
- How success will be observed: build and full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `ToolsDetailCard` to `web/src/components/tools.tsx` and use it for the
current-status and next-step tools cards.

## Constraints
- use existing systems and approved mechanisms
- do not move tools overview API calls or state out of `App()`
- do not alter labels, values, route behavior, or visual classes
- do not move Telegram link-code generation behavior
- do not open a visible browser window

## Implementation Plan
1. Add a small `ToolsDetailCard` component that owns only detail-card chrome.
2. Replace the current-status and next-step detail-card wrappers in `App.tsx`.
3. Keep next-action summarization and Telegram linking at the current call site.
4. Run web build and full route smoke.
5. Update docs and context.

## Acceptance Criteria
- Tools current-status and next-step detail-card wrappers no longer repeat
  inline in `App.tsx`.
- `web/src/components/tools.tsx` owns `ToolsDetailCard`.
- Telegram linking behavior remains in `App.tsx`.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Tools detail-card shell extracted.
- [x] Tools overview state, API, link, and summarization behavior remain in
  `App()`.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - confirmed `/tools` uses `ToolsDetailCard`
- High-risk checks:
  - Telegram link-code generation and next-action summarization were not moved
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
  - route map now records tools detail-card ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing tools detail-card markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Remaining mismatches: tools technical details still live in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: inline `ToolsDetailCard` markup back into `App.tsx`
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

- Task summary: moved tools current-status and next-step detail-card chrome into
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
  - tools technical details still live in `App.tsx`
- Next steps:
  - extract the tools technical-detail panel or continue another route-local
    component slice
- Decisions made:
  - keep Telegram linking behavior in `App()`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: tools detail-card wrappers repeated inline.
- Gaps: tools technical details remain inline.
- Inconsistencies: tools component ownership was still incomplete.
- Architecture constraints: keep tools state/API in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-987 tools detail-card extraction.
- Priority rationale: small presentational cleanup adjacent to PRJ-986.
- Why other candidates were deferred: Telegram link and technical details need
  separate scopes to avoid behavior drift.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/tools.tsx`, docs/context.
- Logic: move only the card wrapper and label.
- Edge cases: next-action summarization stays at the call site.

### 4. Execute Implementation
- Implementation notes: extracted a `children`-based detail-card shell.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave detail cards inline.
- Technical debt introduced: no
- Scalability assessment: tools route presentation now has summary, fact, and
  detail primitives.
- Refinements made: avoided moving Telegram link behavior.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
