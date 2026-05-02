# Task

## Header
- ID: PRJ-875
- Title: Canonical UI Final Route Sweep
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-869, PRJ-870, PRJ-871, PRJ-872, PRJ-873, PRJ-874
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 875
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The canonical UI refresh has completed separate slices for the public home,
dashboard, chat, personality, settings, and tools routes. Before the work can be
treated as a clean commit candidate, the primary routes need one shared
verification pass to catch layout regressions across the canonical shell.

## Goal
Verify the refreshed canonical route set as one coherent UI package and record
evidence that it is ready for release review or commit.

## Scope
- Routes:
  - `/`
  - `/dashboard`
  - `/chat`
  - `/personality`
  - `/settings`
  - `/tools`
- Files:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md`
- Out of scope:
  - new route designs
  - backend, database, runtime, or deployment behavior
  - new API contracts or data model changes

## Success Signal
- User or operator problem: the refreshed UI needs confidence as a coherent,
  committable package rather than isolated screen passes.
- Expected product or reliability outcome: the main public/private route set is
  visually consistent and build-valid after the canonical changes.
- How success will be observed: screenshot evidence, successful build, diff
  hygiene, and documented residual risks.
- Post-launch learning needed: no

## Deliverable For This Stage
A final route sweep with screenshot evidence, validation commands, self-review,
and context updates. Tiny corrective CSS changes were allowed only if the sweep
found an obvious route-level regression.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- preserve existing route data, API calls, and interaction handlers

## Implementation Plan
1. Capture current screenshots for the primary route set on desktop and mobile.
2. Inspect screenshots for shell, sidebar, route header, and responsive layout
   regressions.
3. Apply only narrow route-scoped fixes if a blocking visual issue is found.
4. Run the frontend build and diff hygiene checks.
5. Update task, project state, and task board with the final evidence.

## Acceptance Criteria
- Desktop screenshot evidence exists for the primary route set.
- Mobile screenshot evidence exists for the primary route set or a documented
  reason explains any route omitted.
- `npm run build` passes from `web`.
- `git diff --check` passes for the touched files, allowing line-ending warnings.
- No backend, DB, env, auth, or runtime behavior changes are introduced.

## Definition of Done
- [x] The primary route set has screenshot evidence after the latest UI changes.
- [x] Automated frontend build passes.
- [x] Diff hygiene check passes.
- [x] Task board and project state are updated.
- [x] Residual risks are recorded.

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
- broad new polish beyond the verification sweep

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - desktop screenshots reviewed for `/`, `/dashboard`, `/chat`,
    `/personality`, `/settings`, and `/tools`
  - mobile screenshots reviewed for `/`, `/dashboard`, `/chat`,
    `/personality`, `/settings`, and `/tools`
  - mobile chat composer regression found and corrected with route-scoped CSS
- Screenshots/logs:
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/public-home-unauth-desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/public-home-unauth-mobile-390x844-v2.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/dashboard-desktop-1568x1003.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/dashboard-mobile-390x844.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/chat-desktop-1568x1003.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/chat-mobile-full-390x844-v3.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/personality-desktop-1568x1003.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/personality-mobile-390x844.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/settings-desktop-1568x1003.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/settings-mobile-390x844.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/tools-desktop-1568x1003.png`
  - `.codex/artifacts/prj875-canonical-ui-final-route-sweep/tools-mobile-390x844.png`
- High-risk checks:
  - no backend, DB, env, auth, or runtime contract changes
  - headless Chrome processes launched for the sweep were checked and no
    `aion-cdp-*` processes remained
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
- Design source reference: active canonical AION shell references and completed
  PRJ-869 through PRJ-874 route evidence
- Canonical visual target: coherent AION public/private shell across the main
  route set
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: canonical shell, route overview bars,
  restrained glass panels, compressed mobile route headers
- New shared pattern introduced: no
- Design-memory entry reused: current canonical shell notes
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: reuse existing code-native and
  committed route assets
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches:
  - full-page mobile screenshots show the fixed mobile route nav overlay in the
    captured long image; viewport behavior remains expected
  - public home and dashboard both reuse the large canonical figure motif, as
    intended by the current shell direction
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: visual hierarchy, reachable route controls, no obvious
  overlap or clipped primary labels
- Parity evidence: pending screenshots

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert the frontend UI commit if a visual regression is found
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
The task intentionally focuses on verification and commit readiness. Any
larger route redesign discovered during the sweep should become a follow-up task
instead of being folded into this testers' pass.

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
- Existing workaround or pain: route-level screenshots exist per slice, but not
  yet as one final commit-readiness sweep
- Smallest useful slice: verify the primary route set together
- Success metric or signal: screenshots plus build and diff hygiene pass
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: navigate the primary public and private UI routes
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: frontend build
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: Chrome CDP screenshots and `npm run build`
- Rollback or disable path: revert the frontend UI commit

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: no
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: visually retained from existing route components
- Error state verified: visually retained from existing route components
- Refresh/restart behavior verified: Chrome CDP route reloads completed
- Regression check performed: frontend build and screenshot sweep

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: public UI and authenticated UI shell only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: unchanged
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: none identified for this frontend-only verification task

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Completed a final route sweep for the canonical public/private
  route set and fixed the mobile chat composer layout found during review.
- Files changed:
  - `web/src/index.css`
  - `.codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - Chrome CDP screenshot sweep for primary routes
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - no commit has been created in this task
  - `.codex/artifacts` screenshot evidence remains ignored by git
- Next steps:
  - prepare a selective commit candidate for the canonical UI package
- Decisions made:
  - keep the final sweep as a verification task and limit implementation to a
    narrow mobile chat composer fix

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: main canonical route slices are complete, but final shared route
  evidence has not yet been captured after PRJ-874.
- Gaps: commit-readiness needs one cross-route sweep.
- Inconsistencies: none known at task start.
- Architecture constraints: frontend-only verification must preserve existing
  API and runtime contracts.

### 2. Select One Priority Task
- Selected task: PRJ-875 Canonical UI Final Route Sweep.
- Priority rationale: this is the smallest useful next task after multiple
  UI implementation slices and before release or commit.
- Why other candidates were deferred: new route polish is lower priority until
  the current package is verified.

### 3. Plan Implementation
- Files or surfaces to modify: route screenshots, this task file, project
  state, task board, and possibly narrow CSS only if a regression is found.
- Logic: no product logic changes planned.
- Edge cases: private route mocks must be limited to screenshot capture; mobile
  must avoid clipping route controls.
- Validation path: Chrome CDP screenshots, frontend build, diff hygiene.

### 4. Execute Implementation
- Implementation notes:
  - captured route screenshots for public home and the primary authenticated
    routes
  - corrected mobile chat composer CSS so the text input spans a full row and
    controls move to a separate compact row

### 5. Verify and Test
- Validation performed:
  - Chrome CDP screenshots
  - frontend production build
  - diff hygiene
  - headless Chrome process cleanup check
- Result: passed

### 6. Self-Review
- Simpler option considered: rely on per-route slice evidence only.
- Technical debt introduced: no
- Scalability assessment: the CSS change is route-scoped and improves mobile
  resilience without changing component contracts.
- Refinements made: mobile chat composer now avoids the cramped input layout
  observed during the sweep.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
