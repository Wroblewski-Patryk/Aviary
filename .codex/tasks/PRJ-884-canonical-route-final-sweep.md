# Task

## Header
- ID: PRJ-884
- Title: Canonical Route Final Sweep
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-883
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 884
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Memory, Reflections, Plans, Goals, Insights, Automations, and Integrations have
been promoted from disabled sidebar entries into canonical authenticated routes.
The next smallest useful task is a final route sweep before any commit scope is
prepared.

## Goal
Verify the canonical authenticated route set after the module rollout and record
evidence for build, route rendering, responsive posture, and commit-scope risks.

## Scope
- Routes:
  - `/dashboard`
  - `/chat`
  - `/personality`
  - `/memory`
  - `/reflections`
  - `/plans`
  - `/goals`
  - `/insights`
  - `/automations`
  - `/integrations`
  - `/tools`
  - `/settings`
- Files:
  - `.codex/tasks/PRJ-884-canonical-route-final-sweep.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - new route features
  - backend, DB, auth, provider, scheduler, or action-layer changes
  - commit or push

## Success Signal
- User or operator problem: after many route slices, regressions can hide in
  shell routing, mobile tabbar behavior, or authenticated data loading.
- Expected product or reliability outcome: final route set is proven buildable,
  navigable, nonblank, and ready for commit-scope preparation.
- How success will be observed: build passes, route smoke passes, screenshots
  are captured, and docs/context are updated.
- Post-launch learning needed: no

## Deliverable For This Stage
Verification evidence for the complete canonical authenticated route set.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Run frontend build.
2. Run a Chrome CDP route smoke across the authenticated route set.
3. Capture desktop and mobile screenshot evidence for the final route set.
4. Record any visual or routing defects found.
5. Update task board and project state.

## Acceptance Criteria
- `npm run build` passes.
- Every scoped route renders an authenticated shell surface.
- No scoped route is blank.
- Mobile and desktop route smoke complete without horizontal overflow flags.
- Screenshot evidence exists for the final sweep.

## Definition of Done
- [x] Build passes.
- [x] Route smoke passes.
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
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - Chrome CDP final route smoke
  - result: passed, 24 route/viewport checks
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-884-canonical-route-final-sweep.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - desktop dashboard screenshot reviewed
  - mobile chat screenshot reviewed
  - mobile integrations screenshot reviewed
  - no blank route, horizontal overflow, or JavaScript exception found in the
    automated route smoke
- Screenshots/logs:
  - `.codex/artifacts/prj884-canonical-route-final-sweep/route-smoke-results.json`
  - `.codex/artifacts/prj884-canonical-route-final-sweep/dashboard-desktop.png`
  - `.codex/artifacts/prj884-canonical-route-final-sweep/chat-mobile.png`
  - `.codex/artifacts/prj884-canonical-route-final-sweep/integrations-mobile.png`
- High-risk checks:
  - no production code changes planned unless verification finds a defect
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
If this sweep finds a concrete defect, fix only that defect within this task and
rerun the affected validation.

## Result Report

- Task summary: Verified the complete canonical authenticated route set after
  the module rollout.
- Files changed:
  - `.codex/tasks/PRJ-884-canonical-route-final-sweep.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - Chrome CDP route smoke for 12 routes across desktop and mobile
  - screenshot review for representative dashboard, chat, and integrations
    captures
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-884-canonical-route-final-sweep.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - commit scope preparation is still a separate follow-up task
- Next steps:
  - prepare a commit scope audit for the canonical UI package
- Decisions made:
  - no production code changes were required during the sweep.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: many canonical route slices landed in one working tree.
- Gaps: the complete authenticated route set needed one final smoke pass.
- Inconsistencies: none confirmed before verification.
- Architecture constraints: verification-only unless a concrete defect is found.

### 2. Select One Priority Task
- Selected task: PRJ-884 Canonical Route Final Sweep.
- Priority rationale: a final sweep reduces release risk before commit scope
  preparation.
- Why other candidates were deferred: commit and push remain separate explicit
  release actions.

### 3. Plan Implementation
- Files or surfaces to modify: task and context docs only unless a defect is
  found.
- Logic: build, route smoke, screenshot capture, evidence update.
- Edge cases: authenticated redirects, blank views, JavaScript exceptions, and
  mobile horizontal overflow.
- Validation path: build, Chrome CDP smoke, screenshots, diff hygiene.

### 4. Execute Implementation
- Implementation notes:
  - ran build
  - captured desktop/mobile screenshots for all scoped authenticated routes
  - wrote route smoke JSON evidence

### 5. Verify and Test
- Validation performed:
  - frontend build
  - 24 route/viewport Chrome CDP checks
  - representative screenshot review
  - diff hygiene
- Result: passed

### 6. Self-Review
- Simpler option considered: rely only on per-route screenshots from earlier
  slices.
- Technical debt introduced: no
- Scalability assessment: route smoke script remains local evidence only and
  did not add repo code.
- Refinements made: none needed.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-884-canonical-route-final-sweep.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
