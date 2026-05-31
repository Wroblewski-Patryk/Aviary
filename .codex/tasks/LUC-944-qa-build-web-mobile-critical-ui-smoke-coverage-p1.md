# Task

## Header
- ID: LUC-944
- Title: [Aviary][QA] Build web/mobile critical UI smoke coverage (P1)
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: none
- Priority: P1
- Iteration: 1
- Operation Mode: BUILDER
- Mission ID: LUC-944-web-mobile-critical-ui-smoke
- Mission Status: VERIFIED

## Context
`LUC-944` was assigned without a local task packet. The repository already has a broad route smoke harness, but this issue needs an explicit P1 critical-path UI smoke pack for both web and mobile breakpoints with repeatable evidence.

## Goal
Define and execute a bounded QA smoke contract for critical UI routes and interactions, then leave replayable artifacts and state updates.

## Scope
- `web/scripts/route-smoke.mjs` execution and report artifacts
- Critical routes: `/`, `/login`, `/dashboard`, `/chat`, `/personality`, `/tools`, `/integrations`, `/settings`
- Viewports: `desktop`, `mobile`
- Source-of-truth sync after proof

## Implementation Plan
1. Run `npm run build` in `web/`.
2. Run route smoke with screenshot/report output for the critical route set.
3. Verify report fields: `status=ok`, `failed_count=0`, expected route and screenshot counts.
4. Update `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, and `.agents/state/module-confidence-ledger.md` with command/result evidence.

## Acceptance Criteria
- Critical route smoke completes with `status=ok`.
- Screenshot gate has `failed_count=0` for desktop and mobile.
- Evidence artifacts are stored under `.codex/artifacts/luc944-web-mobile-critical-ui-smoke/`.
- State files are updated with exact commands and outcomes.

## Constraints
- Use existing smoke harness only; no replacement framework.
- No backend/API or product behavior changes in this lane.
- Keep to QA verification scope; escalate failures as defects instead of patching unrelated layers.

## Definition of Done
- [x] Critical UI smoke command(s) executed with saved report.
- [x] Evidence captured in task file and source-of-truth state files.
- [x] Final state is one of: `DONE` (all pass) or `BLOCKED` with concrete failing proof and next owner.

## Forbidden
- Broad UI redesign
- Temporary bypasses in smoke checks
- Mixing implementation fixes with verification-only lane without explicit handoff

## Validation Evidence
- Executed commands:
  - `Push-Location web; npm run build; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
  - first smoke attempt in parallel with build -> FAIL (`ENOENT ... web/dist/index.html`)
  - `Push-Location web; node scripts/route-smoke.mjs --report ../.codex/artifacts/luc944-web-mobile-critical-ui-smoke/report.json --screenshots ../.codex/artifacts/luc944-web-mobile-critical-ui-smoke/screenshots --screenshot-routes /,/login,/dashboard,/chat,/personality,/tools,/integrations,/settings --viewports desktop,mobile --fail-on-ui-findings; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Report highlights:
  - `status=ok`
  - `route_count=14`
  - `ui_audit.viewport_count=2`
  - `ui_audit.screenshot_count=16`
  - `ui_audit.failed_count=0`
- Artifact:
  - `.codex/artifacts/luc944-web-mobile-critical-ui-smoke/report.json`
  - `.codex/artifacts/luc944-web-mobile-critical-ui-smoke/screenshots/*.png`
- Reality status: verified

## Result Report
- Task summary: Critical web/mobile UI smoke coverage executed and verified for the bounded P1 route set.
- Files changed: this task packet plus source-of-truth state files.
- How tested: web build plus route-smoke screenshot gate for desktop/mobile across 8 critical routes.
- What is incomplete: none in this lane scope.
- Next steps: optional expansion only if a new route or interaction becomes release-critical.
