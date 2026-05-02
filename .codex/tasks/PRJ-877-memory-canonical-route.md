# Task

## Header
- ID: PRJ-877
- Title: Memory Canonical Route
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-875, PRJ-876
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 877
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The canonical route package currently covers public home, dashboard, chat,
personality, settings, and tools. The authenticated sidebar still contains
disabled module entries for memory, reflections, plans, goals, insights,
automations, and integrations. The first dependent surface in that order is
Memory.

## Goal
Promote Memory from a disabled sidebar entry into a canonical authenticated
route that reuses existing overview data and shell patterns.

## Scope
- Route:
  - `/memory`
- Files:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-877-memory-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - backend endpoints
  - database or runtime memory logic
  - new decorative image assets
  - other disabled sidebar module routes

## Success Signal
- User or operator problem: Memory appears in the canonical sidebar but cannot
  be opened as a first-class view.
- Expected product or reliability outcome: Memory becomes a polished,
  route-level surface using real available overview data where possible.
- How success will be observed: route can be navigated, screenshots show a
  canonical layout, and build passes.
- Post-launch learning needed: no

## Deliverable For This Stage
One implemented Memory route, with canonical styling, screenshot evidence, and
documentation updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- use available real display data from `/app/personality/overview` when present

## Implementation Plan
1. Add `/memory` to the route type, route list, normalization, and route copy.
2. Enable the sidebar and mobile navigation item for Memory.
3. Build a Memory route using existing `knowledgeSummary`, `preferenceSummary`,
   `chatRelatedMemory`, and personality recent activity data.
4. Add route-scoped CSS matching the canonical shell language.
5. Capture desktop/mobile screenshots and run frontend validation.
6. Update task board and project state.

## Acceptance Criteria
- `/memory` is a first-class route.
- Sidebar and mobile tabbar can navigate to Memory.
- Memory route uses existing data from the current overview where available.
- The layout follows the canonical shell without adding a new visual system.
- `npm run build` passes.
- Screenshot evidence exists for desktop and mobile.

## Definition of Done
- [x] Memory route is implemented.
- [x] Sidebar and mobile navigation include Memory as an active route.
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
- backend or DB changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-877-memory-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - `/memory` renders as a first-class authenticated route
  - Memory sidebar item is active and navigable
  - Memory mobile tabbar item is active and navigable
  - overview-backed memory counts render from `/app/personality/overview`
- Screenshots/logs:
  - `.codex/artifacts/prj877-memory-canonical-route/memory-desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj877-memory-canonical-route/memory-mobile-390x844-v2.png`
- High-risk checks:
  - no backend, DB, auth, env, or runtime memory contract changes
  - no `aion-cdp-memory-*` Chrome processes remained after screenshots
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
- Design source reference: canonical authenticated sidebar and current PRJ-875
  route evidence
- Canonical visual target: Memory as an authenticated canonical module route
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: canonical sidebar, route overview bar,
  restrained panels, route-scoped CSS
- New shared pattern introduced: no
- Design-memory entry reused: Canonical authenticated sidebar spine,
  timeline-backed metadata, route-specific persona adaptation
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: code-native, no new raster asset
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches:
  - Memory currently uses code-native orbit art rather than a route-specific
    generated raster motif; acceptable for this slice because no approved
    Memory-specific image reference exists yet.
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
- Rollback note: revert the eventual Memory route commit if a visual regression
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
This task intentionally implements only Memory. The remaining disabled module
entries should follow as separate narrow slices.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY` or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB -> validation -> error handling -> test. Partial implementations, mock-only paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: AION web app reviewer
- Existing workaround or pain: Memory appears in the sidebar but is disabled.
- Smallest useful slice: enable and implement the Memory route only.
- Success metric or signal: route opens and build/screenshot evidence passes.
- Feature flag, staged rollout, or disable path: revert the UI route commit
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: open Memory from authenticated shell navigation
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: frontend build
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Chrome CDP screenshots
- Rollback or disable path: revert the UI route commit

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: existing `/app/personality/overview` display data
- Endpoint and client contract match: no new endpoint
- DB schema and migrations verified: not applicable
- Loading state verified: inherited existing overview loading path
- Error state verified: inherited existing overview error path
- Refresh/restart behavior verified: Chrome CDP route reload completed
- Regression check performed: build, diff hygiene, screenshots

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: authenticated UI display data
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged existing `/app/me` bootstrap
- Abuse cases: not applicable
- Secret handling: unchanged
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: route exposes only already-fetched overview summaries

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Promoted Memory from a disabled sidebar entry to a canonical
  authenticated route backed by existing overview summaries.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-877-memory-canonical-route.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-877-memory-canonical-route.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - Chrome CDP desktop and mobile screenshots
- What is incomplete:
  - Memory-specific backend detail data is not added; the route intentionally
    uses existing overview summaries.
- Next steps:
  - implement the next disabled module route as a separate slice, likely
    Reflections.
- Decisions made:
  - use existing `/app/personality/overview` data instead of adding a new API
    or fake local data.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Memory exists in the sidebar as a disabled module entry.
- Gaps: no `/memory` route is registered.
- Inconsistencies: sidebar suggests a module that is not yet navigable.
- Architecture constraints: no backend or runtime changes; use existing
  overview data.

### 2. Select One Priority Task
- Selected task: PRJ-877 Memory Canonical Route.
- Priority rationale: Memory is the first disabled module in the canonical
  sidebar and is foundational for other deeper module views.
- Why other candidates were deferred: Reflections, Plans, Goals, Insights,
  Automations, and Integrations should follow after Memory as separate slices.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx`, `web/src/index.css`, task and
  context docs.
- Logic: route registration, navigation enablement, and code-native Memory UI.
- Edge cases: empty overview summaries must still render a calm, non-error
  state.
- Validation path: build, diff hygiene, desktop/mobile screenshots.

### 4. Execute Implementation
- Implementation notes:
  - added `/memory` to route typing, route normalization, and navigation
  - enabled Memory in the sidebar and mobile tabbar
  - extended overview loading to include Memory
  - added a route-scoped Memory canvas, overview bar, stat cards, continuity
    map, signal cards, and recent movement list

### 5. Verify and Test
- Validation performed:
  - frontend build
  - diff hygiene
  - Chrome CDP screenshots
- Result: passed

### 6. Self-Review
- Simpler option considered: keep Memory disabled until backend-specific data
  exists.
- Technical debt introduced: no
- Scalability assessment: the route is isolated and can later swap to a
  dedicated memory endpoint without changing shell routing.
- Refinements made: overview fetch condition was expanded after screenshot QA
  showed the first Memory render was not yet receiving real summary data.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-877-memory-canonical-route.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
