# Task

## Header
- ID: PRJ-880
- Title: Goals Canonical Route
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-879
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 880
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Plans is now a canonical authenticated module route. The next disabled sidebar
module is Goals, which should focus on goal posture and progress without
becoming another planning board or introducing action side effects.

## Goal
Promote Goals from a disabled sidebar entry into a canonical authenticated route
using existing planning summary and dashboard goal data.

## Scope
- Route:
  - `/goals`
- Files:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-880-goals-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - backend endpoints
  - database or runtime goal logic
  - goal editing or action side effects
  - Insights, Automations, or Integrations routes

## Success Signal
- User or operator problem: Goals appears in the canonical sidebar but cannot
  be opened as a first-class view.
- Expected product or reliability outcome: Goals becomes a polished route-level
  surface showing goal posture, active counts, and progress context.
- How success will be observed: route can be navigated, screenshots show a
  canonical layout, and build passes.
- Post-launch learning needed: no

## Deliverable For This Stage
One implemented Goals route with canonical styling, screenshot evidence, and
context updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- use available real display data from `/app/personality/overview` when present

## Implementation Plan
1. Add `/goals` to the route type, route list, normalization, and route copy.
2. Enable the sidebar and mobile navigation item for Goals.
3. Build a Goals route using existing `planningSummary`, dashboard goal rows,
   and recent activity/guidance data.
4. Add route-scoped CSS matching the canonical shell language.
5. Capture desktop/mobile screenshots and run frontend validation.
6. Update task board and project state.

## Acceptance Criteria
- `/goals` is a first-class route.
- Sidebar and mobile tabbar can navigate to Goals.
- Goals route uses existing data from current overview where available.
- The layout follows the canonical shell without adding a new visual system.
- `npm run build` passes.
- Screenshot evidence exists for desktop and mobile.

## Definition of Done
- [x] Goals route is implemented.
- [x] Sidebar and mobile navigation include Goals as an active route.
- [x] Build passes.
- [x] Screenshot evidence is captured.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping
- backend, DB, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-880-goals-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - `/goals` renders as a first-class authenticated route
  - Goals sidebar item is active and navigable
  - Goals mobile tabbar item is active and navigable
  - overview-backed active goal count renders from `/app/personality/overview`
  - dashboard goal progress rows render without mobile overflow
- Screenshots/logs:
  - `.codex/artifacts/prj880-goals-canonical-route/goals-desktop-1568x1003-v1.png`
  - `.codex/artifacts/prj880-goals-canonical-route/goals-mobile-390x844-v1.png`
- High-risk checks:
  - no backend, DB, auth, env, action-layer, or goals runtime contract changes
  - no `aion-cdp-goals-*` Chrome processes remained after screenshots
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/architecture-source-of-truth.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: canonical authenticated sidebar and PRJ-875 route
  evidence
- Canonical visual target: Goals as an authenticated canonical module route
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: canonical sidebar, route overview bar,
  restrained panels, route-scoped CSS
- New shared pattern introduced: no
- Design-memory entry reused: Timeline-backed metadata, surface-first flagship
  closure, canonical authenticated sidebar spine
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: code-native, no new raster asset
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches:
  - Goal rows use seeded dashboard progress labels until a dedicated goals API
    exists; this is visible context data already used elsewhere, not a new fake
    backend path.
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: route headings and navigation focus remain semantic
- Parity evidence: pending

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert the eventual Goals route commit if a visual regression
  is found
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
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

## Notes
This task intentionally implements only Goals. Insights, Automations, and
Integrations should follow as separate slices.

## Result Report

- Task summary: Promoted Goals from a disabled sidebar entry to a canonical
  authenticated route backed by existing planning and dashboard goal summaries.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-880-goals-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-880-goals-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - Chrome CDP desktop and mobile screenshots
- What is incomplete:
  - no dedicated goals endpoint or goal editing behavior was added
- Next steps:
  - implement Insights as the next separate canonical module slice.
- Decisions made:
  - keep Goals as a direction/progress surface and keep planning/action
    concerns out of the route.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Goals exists in the sidebar as a disabled module entry.
- Gaps: no `/goals` route is registered.
- Inconsistencies: sidebar suggests a module that is not yet navigable.
- Architecture constraints: no backend or runtime changes; use existing
  overview and dashboard data.

### 2. Select One Priority Task
- Selected task: PRJ-880 Goals Canonical Route.
- Priority rationale: Goals is the next disabled module after Plans in the
  canonical sidebar.
- Why other candidates were deferred: Insights and integration modules should
  follow as separate slices.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, `web/src/index.css`, task and
  context docs.
- Logic: route registration, navigation enablement, and code-native Goals UI.
- Edge cases: empty goal summary still renders a calm empty-success posture.
- Validation path: build, diff hygiene, desktop/mobile screenshots.

### 4. Execute Implementation
- Implementation notes:
  - added `/goals` to route typing, route normalization, and navigation
  - enabled Goals in the sidebar and mobile tabbar
  - extended overview loading to include Goals
  - added a route-scoped Goals canvas, overview bar, stat cards, goal horizon,
    progress list, signal cards, and guidance list

### 5. Verify and Test
- Validation performed:
  - frontend build
  - diff hygiene
  - Chrome CDP screenshots
- Result: passed

### 6. Self-Review
- Simpler option considered: keep Goals disabled until a dedicated goals
  endpoint exists.
- Technical debt introduced: no
- Scalability assessment: the route is isolated and can later swap to a
  dedicated goals endpoint without changing shell routing.
- Refinements made: validated in TESTER mode that Goals reads differently from
  Plans and that mobile progress rows do not overflow.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-880-goals-canonical-route.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
