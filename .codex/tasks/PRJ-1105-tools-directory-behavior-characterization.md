# Task

## Header
- ID: PRJ-1105
- Title: Add focused tools-directory behavior characterization
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1104
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1105
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1104` found that the remaining `/tools` group/item map is behaviorful. It
includes provider readiness, user preference toggles, technical details, and
Telegram link-code actions, so it needs characterization before extraction.

## Goal
Add a focused frontend behavior characterization for the `/tools` directory so
future component extraction can preserve the current v1 behavior.

## Success Signal
- User or operator problem: behaviorful tools UI can be refactored without
  silently breaking toggles or linking flow.
- Expected product or reliability outcome: a repeatable script proves tools
  loading, empty, error, full, toggle, and Telegram-link behavior.
- How success will be observed: `npm run test:tools-directory` passes after
  `npm run build`.
- Post-launch learning needed: no

## Scope
- Add `web/scripts/tools-directory-characterization.mjs`.
- Add `npm run test:tools-directory`.
- Update frontend docs, v1 roadmap, task board, project state, and learning
  journal.

## Deliverable For This Stage
A passing tools-directory characterization harness plus synchronized docs and
context evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Reuse the built `web/dist` browser-smoke style already used by route smoke.
2. Serve mocked app-facing API endpoints matching the typed web client.
3. Launch headless Chrome through CDP.
4. Check full tools rendering, loading, empty overview, error state, ClickUp
   toggle request, and Telegram link-start request.
5. Add the npm script.
6. Run build, the new characterization, route smoke, and diff check.

## Acceptance Criteria
- `npm run test:tools-directory` fails if `web/dist/index.html` is missing.
- The full tools state proves group/item counts, toggles, Telegram link panel,
  and technical details.
- The toggle path proves `PATCH /app/tools/preferences` receives
  `clickup_enabled=true`.
- The Telegram path proves `POST /app/tools/telegram/link/start` runs once and
  renders the returned link code.
- Loading, empty overview, and API error states are characterized.
- Existing route smoke still passes.

## Definition of Done
- [x] Characterization harness added.
- [x] npm script added.
- [x] Build and frontend smokes pass.
- [x] Docs/context updated.

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

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location`
  - result: passed with `status=ok`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: passed with `status=ok`, `route_count=14`
- Manual checks:
  - inspected `web/src/lib/api.ts`, `web/src/App.tsx`, `web/package.json`,
    and the existing route smoke harness.
- Screenshots/logs: command output recorded in session.
- High-risk checks:
  - `git diff --check`
  - result: passed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/workflows/general.md`
  - `docs/governance/autonomous-engineering-loop.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: current v1 tools route implementation
- Canonical visual target: current `/tools` browser shell behavior
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable for behavior characterization
- Visual-direction brief reviewed: not applicable for behavior characterization
- Existing shared pattern reused: built-dist headless browser smoke
- New shared pattern introduced: no
- Design-memory entry reused: frontend route/component map
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: not assessed
- State checks: loading, empty, error, success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: not applicable for this script
- Input-mode checks: pointer/click through CDP
- Accessibility checks: not changed
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: frontend docs now list the tools characterization
- Rollback note: remove the script and npm entry if it blocks local frontend
  validation unexpectedly
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes
The harness intentionally uses mocked app-facing API responses, like
`route-smoke.mjs`, because it is a frontend behavior characterization for
browser rendering and client action wiring. Backend endpoint contracts remain
covered by backend tests and the typed API client.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future maintainers of the `/tools` route
- Existing workaround or pain: behaviorful route maps were risky to extract
  without focused proof.
- Smallest useful slice: add characterization before component extraction.
- Success metric or signal: tools characterization and route smoke pass.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: tools directory toggle and Telegram linking start
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke:
  - `npm run test:tools-directory`
  - `npm run smoke:routes`
- Rollback or disable path: remove the test script and npm entry

- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: mocked app-facing API path for frontend
  characterization; backend contract tests remain separate
- Endpoint and client contract match: yes, script uses typed web client paths
- DB schema and migrations verified: not applicable
- Loading state verified: yes
- Error state verified: yes
- Refresh/restart behavior verified: route navigation and built-dist reload
- Regression check performed:
  - `npm run build`
  - `npm run test:tools-directory`
  - `npm run smoke:routes`

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: synthetic frontend test data only
- Trust boundaries: browser client to app-facing API mock
- Permission or ownership checks: no auth/permission behavior changed
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: error state characterized
- Residual risk: no real provider credentials are exercised by this frontend
  characterization

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary:
  - added a built-dist CDP characterization for the `/tools` directory.
- Files changed:
  - `.codex/tasks/PRJ-1105-tools-directory-behavior-characterization.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/package.json`
  - `web/scripts/tools-directory-characterization.mjs`
- How tested:
  - `npm run build`
  - `npm run test:tools-directory`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - tools directory component extraction is still pending
- Next steps:
  - `PRJ-1106` extract the tools directory group/item presentation behind a
    component while preserving route-owned state and handlers.
- Decisions made:
  - the test remains frontend-scoped with synthetic API responses, matching the
    existing route-smoke pattern.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - `/tools` group/item rendering combines display with toggle/link callbacks.
- Gaps:
  - no focused frontend characterization existed for tools toggle/link behavior.
- Inconsistencies:
  - none found.
- Architecture constraints:
  - API calls, state, and side effects stay in `App()` during extraction.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1105` add focused tools-directory behavior characterization.
- Priority rationale:
  - TESTER iteration should pin behavior before a behaviorful component move.
- Why other candidates were deferred:
  - component extraction waits until behavior proof is present.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/package.json`
  - `web/scripts/tools-directory-characterization.mjs`
  - docs/context/task files
- Logic:
  - serve built `dist`, mock app-facing API paths, drive Chrome with CDP, and
    assert route behavior.
- Edge cases:
  - delayed overview loading, empty overview, API error, toggle request, and
    Telegram link-start request.

### 4. Execute Implementation
- Implementation notes:
  - added CDP harness with profile cleanup that stops Chrome child processes
    associated with the specific `--user-data-dir`.

### 5. Verify and Test
- Validation performed:
  - `npm run build`
  - `npm run test:tools-directory`
  - `npm run smoke:routes`
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - only assert DOM via `--dump-dom`.
- Technical debt introduced: no
- Scalability assessment:
  - CDP gives enough interaction coverage without adding a new test framework.
- Refinements made:
  - added Windows Chrome process-tree/profile cleanup after an `EBUSY` cleanup
    failure.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: yes.
