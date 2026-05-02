# Task

## Header
- ID: PRJ-882
- Title: Automations Canonical Route
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-881
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 882
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Insights is now a canonical authenticated module route. The next disabled
sidebar module is Automations, which should expose proactive and scheduler
posture without introducing a new automation system or hidden side effects.

## Goal
Promote Automations from a disabled sidebar entry into a canonical authenticated
route using existing account settings and backend health data.

## Scope
- Route:
  - `/automations`
- Files:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-882-automations-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - new scheduler APIs
  - creating, editing, or deleting automations
  - database or runtime automation logic
  - action side effects
  - Integrations route

## Success Signal
- User or operator problem: Automations appears in the canonical sidebar but
  cannot be opened as a first-class view.
- Expected product or reliability outcome: Automations becomes a polished
  route-level surface showing proactive preference, attention queue, scheduler
  posture, and action boundary.
- How success will be observed: route can be navigated, screenshots show a
  canonical layout, and build passes.
- Post-launch learning needed: no

## Deliverable For This Stage
One implemented Automations route with canonical styling, screenshot evidence,
and context updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- use available real display data from `/app/me` and `/health` when present

## Implementation Plan
1. Add `/automations` to the route type, route list, normalization, and route copy.
2. Enable the sidebar and mobile navigation item for Automations.
3. Build an Automations route using `me.settings.proactive_opt_in` and
   `healthSnapshot` attention/proactive fields.
4. Add route-scoped CSS matching the canonical shell language.
5. Capture desktop/mobile screenshots and run frontend validation.
6. Update task board and project state.

## Acceptance Criteria
- `/automations` is a first-class route.
- Sidebar and mobile tabbar can navigate to Automations.
- Automations route uses existing account and health data where available.
- The layout follows the canonical shell without adding a new visual system.
- `npm run build` passes.
- Screenshot evidence exists for desktop and mobile.

## Definition of Done
- [x] Automations route is implemented.
- [x] Sidebar and mobile navigation include Automations as an active route.
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
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-882-automations-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - `/automations` renders as a first-class authenticated route
  - Automations sidebar item is active and navigable
  - Automations mobile tabbar item is active and navigable
  - proactive setting renders from `/app/me`
  - attention queue and scheduler posture render from `/health`
- Screenshots/logs:
  - `.codex/artifacts/prj882-automations-canonical-route/automations-desktop-1568x1003-v1.png`
  - `.codex/artifacts/prj882-automations-canonical-route/automations-mobile-390x844-v1.png`
- High-risk checks:
  - no backend, DB, auth, env, scheduler, or action-layer changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This task intentionally implements only Automations. Integrations should follow
as a separate slice.

## Result Report

- Task summary: Promoted Automations from a disabled sidebar entry to a
  canonical authenticated route backed by existing account settings and health
  data.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-882-automations-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-882-automations-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - Chrome CDP desktop and mobile screenshots
- What is incomplete:
  - no scheduler API, automation editor, or action behavior was added
- Next steps:
  - implement Integrations as the next separate canonical module slice.
- Decisions made:
  - keep Automations as read-only operational posture and leave the proactive
    setting switch in Settings.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Automations exists in the sidebar as a disabled module entry.
- Gaps: no `/automations` route is registered.
- Inconsistencies: sidebar suggests a module that is not yet navigable.
- Architecture constraints: no backend, scheduler, or action-layer changes; use
  existing `/app/me` and `/health` data.

### 2. Select One Priority Task
- Selected task: PRJ-882 Automations Canonical Route.
- Priority rationale: Automations is the next disabled module after Insights in
  the canonical sidebar.
- Why other candidates were deferred: Integrations should follow as a separate
  slice.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, `web/src/index.css`, task and
  context docs.
- Logic: route registration, navigation enablement, health fetch inclusion, and
  code-native Automations UI.
- Edge cases: unavailable health renders conservatively as unknown while
  preserving settings-backed proactive state.
- Validation path: build, diff hygiene, desktop/mobile screenshots.

### 4. Execute Implementation
- Implementation notes:
  - added `/automations` to route typing, route normalization, and navigation
  - enabled Automations in the sidebar and mobile tabbar
  - extended health loading to include Automations
  - added a route-scoped Automations canvas, overview bar, stat cards,
    switchboard, flow rows, guardrails, and health details

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Chrome CDP screenshots
  - diff hygiene
- Result: passed

### 6. Self-Review
- Simpler option considered: keep Automations disabled until a full automation
  management API exists.
- Technical debt introduced: no
- Scalability assessment: the route is isolated and can later add real
  automation management without changing shell routing.
- Refinements made: preserved action boundary by keeping the route read-only.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-882-automations-canonical-route.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
