# Task

## Header
- ID: PRJ-913
- Title: Web V1 Route Smoke After Release Candidate
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-912, PRJ-909
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 913
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Core no-UI v1 is accepted, production privacy/debug posture is documented, and
the live Telegram smoke is blocked by operator-owned preconditions. The next
locally actionable product gate is a fresh web route smoke after the release
candidate and recent docs commits.

## Goal
Verify the authenticated web shell routes against a local real backend path and
fix any concrete responsive route defect found by the smoke.

## Scope
- `web/src/index.css`
- authenticated web routes:
  - `/dashboard`
  - `/chat`
  - `/personality`
  - `/settings`
  - `/tools`
  - `/memory`
  - `/reflections`
  - `/plans`
  - `/goals`
  - `/insights`
  - `/automations`
  - `/integrations`
- unauthenticated `/login`
- `.codex/tasks/PRJ-913-web-v1-route-smoke-after-release-candidate.md`
- `docs/planning/v1-web-route-smoke-after-release-candidate.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: web-v1 should not claim product readiness while
  primary routes are blank, broken, overflowing, or leaking raw technical
  errors.
- Expected product or reliability outcome: primary routes render through the
  existing shell on desktop and mobile against real local `/app/*` endpoints.
- How success will be observed: build passes, route smoke passes, screenshot
  evidence exists, and the found `/tools` mobile overflow is fixed.
- Post-launch learning needed: no

## Deliverable For This Stage
Route-smoke evidence and a narrow responsive CSS fix for the concrete mobile
overflow found during verification.

## Constraints
- use the existing app shell and API contracts
- do not introduce mocked app data as product truth
- do not commit generated screenshots, local databases, or temporary scripts
- do not mutate production data
- keep the browser-plugin fallback documented if used

## Implementation Plan
1. Run `npm run build`.
2. Start a local backend against a temporary SQLite database under `.codex/tmp`
   with `STARTUP_SCHEMA_MODE=create_tables`.
3. Use Vite on `127.0.0.1:5173` and register a local test user through the
   real `/app/auth/register` endpoint.
4. Smoke `/login` plus the authenticated route set on desktop and mobile.
5. Fix any concrete route overflow found by the smoke.
6. Rerun build and route smoke.
7. Record evidence and context.

## Acceptance Criteria
- `/login` renders for unauthenticated state.
- All selected authenticated routes render nonblank after local registration.
- Desktop and mobile checks have no route failures.
- Mobile route checks do not expose content-level horizontal overflow.
- No unexpected console errors remain.
- Screenshot evidence is captured locally.

## Definition of Done
- [x] `npm run build` passed.
- [x] Local backend health was green during the smoke.
- [x] Route smoke passed for 24 authenticated route/viewport checks.
- [x] `/tools` mobile overflow was fixed.
- [x] Screenshot evidence was captured locally.
- [x] Context and planning docs were updated.
- [x] `git diff --check` passed.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated route rendering logic
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - bundled Node + Playwright route smoke
  - result: passed:
    - `routeChecks=24`
    - `failures=0`
    - `unexpectedConsoleIssueCount=0`
    - `benignConsoleIssueCount=2`
    - `screenshots=8`
  - `git diff --check`
  - result: passed
- Manual checks:
  - local backend `/health` returned `status=ok`
  - smoke used a local registered user and real `/app/*` endpoints through
    Vite proxy
  - `/tools` mobile overflow changed from failing to passing
- Screenshots/logs:
  - `.codex/artifacts/prj913-web-v1-route-smoke/route-smoke-results.json`
  - `.codex/artifacts/prj913-web-v1-route-smoke/login-desktop.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/dashboard-desktop.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/chat-desktop.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/personality-desktop.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/dashboard-mobile.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/chat-mobile.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/tools-mobile.png`
  - `.codex/artifacts/prj913-web-v1-route-smoke/integrations-mobile.png`
- High-risk checks:
  - production was not mutated
  - temporary local backend was stopped
  - generated `.codex/tmp` and screenshot artifacts remain uncommitted
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/ux/screen-quality-checklist.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `docs/engineering/local-development.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: active canonical web shell direction in
  `docs/ux/visual-direction-brief.md`
- Canonical visual target: authenticated product shell routes
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: current authenticated shell and Tools route
  classes
- New shared pattern introduced: no
- Design-memory entry reused: responsive route smoke and no-overflow rule
- Design-memory update required: no
- Visual gap audit completed: yes, smoke found `/tools` mobile overflow
- Background or decorative asset strategy: no asset change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: route-smoke screenshot proof captured
- Remaining mismatches: visual parity polish remains in PRJ-914/PRJ-915 lanes
- State checks: loading, empty, error, success covered through route rendering
  and local empty account posture where practical
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop, mobile
- Input-mode checks: pointer through route navigation and page load; keyboard
  not expanded in this smoke
- Accessibility checks: route labels and buttons remained available; no full
  a11y audit in this slice
- Parity evidence: local screenshots listed above

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert the small CSS changes in `web/src/index.css`
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

- Task summary: verified web-v1 routes and fixed concrete `/tools` mobile
  overflow.
- Files changed:
  - `web/src/index.css`
  - `docs/planning/v1-web-route-smoke-after-release-candidate.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-913-web-v1-route-smoke-after-release-candidate.md`
- How tested: web build, local backend health, bundled Node Playwright smoke,
  screenshot evidence, `git diff --check`.
- What is incomplete: production web route smoke still requires a deployed
  post-commit SHA; PRJ-914/PRJ-915 remain product-honesty improvements.
- Next steps: start `PRJ-914` Replace Remaining Static Personality Metrics.
- Decisions made: browser plugin was unavailable because the local Node used by
  `node_repl` is below the plugin minimum; bundled Node + Playwright was used
  as the documented fallback.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: web route proof was stale after recent release-hardening commits.
- Gaps: no current desktop/mobile smoke evidence for all primary authenticated
  routes.
- Inconsistencies: browser plugin bootstrap blocked on local Node version.
- Architecture constraints: use real API path where possible; do not mock
  product truth.

### 2. Select One Priority Task
- Selected task: PRJ-913 Web V1 Route Smoke After Release Candidate.
- Priority rationale: next locally actionable P1 after PRJ-909 was blocked by
  operator preconditions.
- Why other candidates were deferred: PRJ-914/915 are implementation polish and
  should follow a current route health baseline.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css` only if smoke finds a
  concrete defect; task/context/planning docs for evidence.
- Logic: build, local backend, local registration, route loop, overflow check.
- Edge cases: Polish UI labels after system locale; intentional unauthenticated
  `/login` 401 probe; mobile tabbar scroll.

### 4. Execute Implementation
- Browser plugin setup failed due Node version requirement.
- Started local backend on temporary SQLite and used existing Vite dev server.
- Registered local smoke account.
- Ran route smoke, found `/tools` mobile overflow.
- Fixed grid minimum sizing, technical detail badge wrapping, and root
  horizontal clipping.

### 5. Verify and Test
- Web build passed after the fix.
- Route smoke passed with 24 checks and zero unexpected console issues.
- Temporary backend was stopped.

### 6. Self-Review
- Simpler option considered: record the overflow as a follow-up only; rejected
  because it was a small, localized CSS defect found by the smoke.
- Technical debt introduced: no
- Scalability assessment: fix improves shared mobile containment for current
  Tools content and mobile tabbar behavior.
- Refinements made: route smoke expectations were adjusted to Polish UI labels
  rather than forcing English labels.

### 7. Update Documentation And Knowledge
- Docs updated: yes
- Context updated: yes
- Learning journal updated: not applicable.
