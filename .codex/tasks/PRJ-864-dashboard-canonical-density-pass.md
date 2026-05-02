# Task

## Header
- ID: PRJ-864
- Title: Dashboard Canonical Density Pass
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-863
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 864
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The authenticated shell/sidebar is closer to the canonical direction, but the
Dashboard route still stretches its canonical content across too much vertical
space. The approved dashboard reference shows the hero, guidance rail, cognitive
flow, and lower cards as a dense first-viewport flagship overview.

## Goal
Compress and rebalance the Dashboard route so the first viewport reads closer
to the canonical dashboard reference while preserving the existing data flow and
shared shell/sidebar.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/tasks/PRJ-864-dashboard-canonical-density-pass.md`

## Implementation Plan
1. Remove the extra desktop toolbar from canonical dashboard framing.
2. Reduce dashboard hero/stage vertical footprint.
3. Rebalance the dashboard guidance rail so cards do not feel cramped.
4. Compress flow and lower cards enough to bring the first viewport closer to
   the approved reference.
5. Run build, whitespace validation, and screenshot comparison.

## Acceptance Criteria
- Dashboard desktop first viewport shows materially more canonical content than
  before: hero, right guidance, flow, and lower cards begin in the viewport.
- The dashboard does not reintroduce a visible browser/mockup shell frame.
- No horizontal overflow on desktop or mobile.
- Chat layout remains unaffected.

## Definition of Done
- [x] Web build passes.
- [x] `git diff --check` passes.
- [x] Desktop and mobile dashboard screenshots are captured.
- [x] Canonical dashboard reference and latest implementation are inspected
      with `view_image`.

## Validation Evidence
- Tests: `Push-Location .\web; npm run build; Pop-Location` passed.
- Manual checks: `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-864-dashboard-canonical-density-pass.md` passed with line-ending warnings only.
- Screenshots/logs:
  - `.codex/artifacts/prj864-dashboard-canonical-pass/dashboard-before-1568x1003.png`
  - `.codex/artifacts/prj864-dashboard-canonical-pass/dashboard-desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj864-dashboard-canonical-pass/dashboard-mobile-390x844-v2.png`
  - `.codex/artifacts/prj864-dashboard-canonical-pass/chat-desktop-smoke-1568x1003-v2.png`

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Fidelity target: structurally_faithful
- Screenshot comparison pass completed: yes
- Remaining mismatches: dashboard still uses the existing figure asset and route-local
  cards rather than a fully unified generated dashboard canvas; mobile remains
  intentionally stacked and scroll-first.

## Result Report
- Task summary: pending
- Files changed: pending
- How tested: pending
- What is incomplete: pending
- Next steps: pending

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard content is too vertically spread out compared with the
  canonical first viewport.
- Gaps: hero, flow, and lower cards do not read together in the initial view.
- Architecture constraints: reuse existing dashboard route, assets, and data.

### 2. Select One Priority Task
- Selected task: dashboard canonical density pass.
- Priority rationale: after shell/sidebar, dashboard is the next flagship
  canonical surface.
- Why other candidates were deferred: chat already received the v5 structural
  pass; personality should wait until dashboard framing is steadier.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard route shell class and dashboard CSS.
- Logic: no runtime/API changes.
- Edge cases: desktop density, mobile overflow, text clipping.

### 4. Execute Implementation
- Implementation notes: moved the dashboard guidance rail out of the hero-stage
  height calculation, introduced a top composition with a primary dashboard
  column and side guidance rail, hid the extra canonical route toolbar on
  dashboard, and reduced hero/flow/card density.

### 5. Verify and Test
- Validation performed: web build, diff whitespace check, desktop dashboard
  screenshot, mobile dashboard screenshot, and chat desktop smoke screenshot.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only reducing padding and font sizes; rejected
  because the right rail still forced the hero-stage to exceed the first
  viewport.
- Technical debt introduced: none known; the change reuses existing route
  sections and CSS classes.
- Refinements made: moved rail structure before further shrinking values so the
  layout aligns structurally with the approved dashboard composition.

### 7. Update Documentation and Knowledge
- Docs updated: task evidence only; no new canonical pattern was approved.
- Context updated: `.codex/context/TASK_BOARD.md` and
  `.codex/context/PROJECT_STATE.md`.
- Learning journal updated: not needed; no recurring pitfall confirmed.
