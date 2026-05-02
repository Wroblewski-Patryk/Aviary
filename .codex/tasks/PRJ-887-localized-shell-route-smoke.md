# Task

## Header
- ID: PRJ-887
- Title: Localized Shell Route Smoke
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-886
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 887
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-886 changed authenticated navigation labels to use the existing localization
helper. A focused localized route smoke should verify that Polish shell labels,
routing, and responsive posture remain healthy after that navigation change.

## Goal
Verify localized authenticated shell navigation after the route-label fix.

## Scope
- Locale:
  - Polish UI (`ui_language: pl`)
- Routes:
  - `/dashboard`
  - `/chat`
  - `/integrations`
- Files:
  - `.codex/tasks/PRJ-887-localized-shell-route-smoke.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - production code changes unless the smoke finds a concrete defect
  - new translations
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: navigation localization can regress between
  desktop sidebar and mobile tabbar.
- Expected product or reliability outcome: Polish shell labels are visible and
  the representative localized routes remain nonblank and non-overflowing.
- How success will be observed: build passes, CDP smoke passes, and screenshot
  evidence exists.
- Post-launch learning needed: no

## Deliverable For This Stage
Verification evidence for localized shell routing after PRJ-886.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Run frontend build.
2. Run Chrome CDP smoke using Polish `/app/me` settings.
3. Verify expected localized module labels are present.
4. Capture desktop and mobile screenshots.
5. Update task board and project state.

## Acceptance Criteria
- `npm run build` passes.
- Polish labels for enabled module routes are present in the shell DOM.
- Representative localized routes render nonblank.
- Representative localized routes do not report horizontal overflow.
- Screenshot evidence exists.

## Definition of Done
- [x] Build passes.
- [x] Localized route smoke passes.
- [x] Screenshot evidence is captured.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated route-label logic
- temporary bypasses or hardcoded language branches
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - Chrome CDP localized shell smoke
  - result: passed, 6 checks
  - `git diff --check -- .codex/tasks/PRJ-887-localized-shell-route-smoke.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: pending final run
- Manual checks:
  - desktop dashboard rendered localized sidebar labels
  - mobile integrations rendered localized header and tabbar labels
  - mobile chat was treated as the intentional exception because the mobile
    tabbar is not rendered for `/chat`
  - no checked route was blank, horizontally overflowing, or throwing a
    JavaScript exception
- Screenshots/logs:
  - `.codex/artifacts/prj887-localized-shell-route-smoke/localized-shell-smoke-results-v2.json`
  - `.codex/artifacts/prj887-localized-shell-route-smoke/dashboard-desktop-v2.png`
  - `.codex/artifacts/prj887-localized-shell-route-smoke/chat-mobile-v2.png`
  - `.codex/artifacts/prj887-localized-shell-route-smoke/integrations-mobile-v2.png`
- High-risk checks:
  - no production code changes planned unless verification finds a defect
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Notes
This task is verification-only unless a concrete localized navigation defect is
found.

## Result Report

- Task summary: Verified representative Polish shell routing after localized
  sidebar labels were introduced.
- Files changed:
  - `.codex/tasks/PRJ-887-localized-shell-route-smoke.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - Chrome CDP localized smoke for `/dashboard`, `/chat`, and `/integrations`
    across desktop and mobile
  - screenshot review for mobile integrations
- What is incomplete:
  - some module body copy remains English in localized views; this is a future
    copy-localization slice, not a shell label regression
- Next steps:
  - localize newly added module body copy where it is still English
- Decisions made:
  - mobile `/chat` is excluded from mobile tabbar label assertion because the
    current UI intentionally does not render the mobile tabbar for chat.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: PRJ-886 changed shell navigation labels.
- Gaps: localized shell needed a post-change smoke.
- Inconsistencies: mobile `/chat` intentionally omits the mobile tabbar.
- Architecture constraints: verification-only unless a concrete defect is found.

### 2. Select One Priority Task
- Selected task: PRJ-887 Localized Shell Route Smoke.
- Priority rationale: navigation localization touched shared shell behavior.
- Why other candidates were deferred: body-copy localization should be a
  separate task.

### 3. Plan Implementation
- Files or surfaces to modify: task and context docs only.
- Logic: build, run localized CDP smoke, capture screenshots, record evidence.
- Edge cases: mobile `/chat` omits mobile tabbar by design.
- Validation path: build, localized smoke, screenshot review, diff hygiene.

### 4. Execute Implementation
- Implementation notes:
  - ran build
  - ran Polish shell smoke for representative routes and viewports
  - reran smoke with corrected expectations after confirming mobile `/chat`
    intentionally does not render the mobile tabbar

### 5. Verify and Test
- Validation performed:
  - frontend build
  - localized CDP smoke
  - screenshot review
  - diff hygiene pending final context update
- Result: passed so far

### 6. Self-Review
- Simpler option considered: rely on PRJ-886 single screenshot only.
- Technical debt introduced: no.
- Scalability assessment: smoke evidence is local and did not add repo code.
- Refinements made: clarified the mobile chat tabbar exception.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-887-localized-shell-route-smoke.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
