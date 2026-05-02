# Task

## Header
- ID: PRJ-883
- Title: Integrations Canonical Route
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-882
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 883
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Automations is now a canonical authenticated module route. The remaining
disabled sidebar module is Integrations, which should expose provider readiness
from the existing tools overview without adding provider calls or link flows.

## Goal
Promote Integrations from a disabled sidebar entry into a canonical
authenticated route using existing tools overview data.

## Scope
- Route:
  - `/integrations`
- Files:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-883-integrations-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - new integration APIs
  - provider calls
  - link flow changes
  - tool preference changes
  - backend or DB changes

## Success Signal
- User or operator problem: Integrations appears in the canonical sidebar but
  cannot be opened as a first-class view.
- Expected product or reliability outcome: Integrations becomes a polished
  route-level surface showing provider readiness, link needs, and boundaries.
- How success will be observed: route can be navigated, screenshots show a
  canonical layout, and build passes.
- Post-launch learning needed: no

## Deliverable For This Stage
One implemented Integrations route with canonical styling, screenshot evidence,
and context updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- use available real display data from `/app/tools/overview` when present

## Implementation Plan
1. Add `/integrations` to the route type, route list, normalization, and route copy.
2. Enable the sidebar and mobile navigation item for Integrations.
3. Build an Integrations route using `toolsOverview` provider readiness and
   link state.
4. Add route-scoped CSS matching the canonical shell language.
5. Capture desktop/mobile screenshots and run frontend validation.
6. Update task board and project state.

## Acceptance Criteria
- `/integrations` is a first-class route.
- Sidebar and mobile tabbar can navigate to Integrations.
- Integrations route uses existing tools overview data where available.
- The layout follows the canonical shell without adding a new visual system.
- `npm run build` passes.
- Screenshot evidence exists for desktop and mobile.

## Definition of Done
- [x] Integrations route is implemented.
- [x] Sidebar and mobile navigation include Integrations as an active route.
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
- backend, DB, provider, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-883-integrations-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - `/integrations` renders as a first-class authenticated route
  - Integrations sidebar item is active and navigable
  - Integrations mobile tabbar item is active and navigable
  - provider readiness and link state render from `/app/tools/overview`
  - link-required providers show `Link` before `Ready`
- Screenshots/logs:
  - `.codex/artifacts/prj883-integrations-canonical-route/integrations-desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj883-integrations-canonical-route/integrations-mobile-390x844-v2.png`
- High-risk checks:
  - no backend, DB, auth, env, provider, link-flow, or action-layer changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This task intentionally implements only Integrations.

## Result Report

- Task summary: Promoted Integrations from a disabled sidebar entry to a
  canonical authenticated route backed by existing tools overview data.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-883-integrations-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-883-integrations-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - Chrome CDP desktop and mobile screenshots
- What is incomplete:
  - no provider calls, link flow changes, or tool preference changes were added
- Next steps:
  - run a final route sweep and prepare the canonical UI commit scope.
- Decisions made:
  - keep Integrations as read-only provider posture and leave toggles/link
    flows in Tools.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Integrations exists in the sidebar as a disabled module entry.
- Gaps: no `/integrations` route is registered.
- Inconsistencies: sidebar suggests a module that is not yet navigable.
- Architecture constraints: no backend, provider, link-flow, or action-layer
  changes; use existing tools overview data.

### 2. Select One Priority Task
- Selected task: PRJ-883 Integrations Canonical Route.
- Priority rationale: Integrations is the remaining disabled canonical sidebar
  module.
- Why other candidates were deferred: final sweep and commit prep should follow
  after this slice.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, `web/src/index.css`, task and
  context docs.
- Logic: route registration, navigation enablement, tools overview fetch
  inclusion, and code-native Integrations UI.
- Edge cases: empty tools overview renders a quiet provider row instead of
  inventing provider state.
- Validation path: build, diff hygiene, desktop/mobile screenshots.

### 4. Execute Implementation
- Implementation notes:
  - added `/integrations` to route typing, route normalization, and navigation
  - enabled Integrations in the sidebar and mobile tabbar
  - extended tools overview loading to include Integrations
  - added a route-scoped Integrations canvas, overview bar, stat cards,
    provider map, provider rows, boundary notes, and readiness details

### 5. Verify and Test
- Validation performed:
  - frontend build
  - Chrome CDP screenshots
  - diff hygiene
- Result: passed

### 6. Self-Review
- Simpler option considered: keep Integrations disabled until richer provider
  management exists.
- Technical debt introduced: no
- Scalability assessment: the route can later add deeper provider detail while
  preserving current shell routing.
- Refinements made: link-required providers now display `Link` before `Ready`.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-883-integrations-canonical-route.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
