# Task

## Header
- ID: PRJ-1225
- Title: Mobile account trigger polish
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1224
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-001
- Quality Scenario Rows: QA-UX-001
- Risk Rows: not applicable
- Iteration: 1225
- Operation Mode: TESTER
- Mission ID: UXUI-POLISH-2026-05-14
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] `.agents/core/mission-control.md` was reviewed for long-running work.
- [x] Missing or template-like state tables were bootstrapped from repository sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified or marked not applicable.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: Replace the raw-looking mobile/tablet account trigger with a shared shell-styled trigger while preserving account panel behavior.
- Release objective advanced: Continue repeated web layout polish after shared navigation work.
- Included slices: mobile/tablet account trigger styling, accessibility state, responsive proof, source-of-truth updates.
- Explicit exclusions: account panel content, auth behavior, sign-out behavior, desktop utility account trigger, route definitions, backend, deployment.
- Checkpoint cadence: one implementation checkpoint after screenshot review.
- Stop conditions: build failure, route-smoke failure, navigation proof failure, screenshot regression.
- Handoff expectation: commit and push after validation passes.

## Context
Current mobile and tablet authenticated route headers use a generic `btn btn-outline` account trigger. In screenshots it reads like a browser-default control with a heavy black border, while the rest of the Aviary shell uses soft material tokens.

## Goal
Make the repeated mobile/tablet account trigger feel native to the Aviary shell without changing account panel behavior.

## Success Signal
- User or operator problem: mobile/tablet header chrome feels inconsistent because the account control is visually heavier than the shell.
- Expected product or reliability outcome: repeated route headers look calmer and more intentional across mobile and tablet.
- How success will be observed: refreshed mobile/tablet screenshots show a soft account trigger that matches the shell and still opens the account panel.
- Post-launch learning needed: no

## Deliverable For This Stage
Shared mobile/tablet account trigger polish plus responsive/navigation validation evidence.

## Constraints
- do not change auth, logout, account data, or panel contents
- preserve existing account panel toggle behavior
- preserve desktop utility account trigger
- avoid route-local header overrides

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- source-of-truth state/docs touched by this UI mission

## Implementation Plan
1. Add a dedicated mobile/tablet account trigger class and active state.
2. Add `aria-expanded` to expose the account panel state.
3. Style the trigger with Aviary shell material tokens, stable dimensions, and responsive text handling.
4. Run web build and UI audits sequentially.
5. Review refreshed mobile/tablet screenshots across representative routes.
6. Update source-of-truth files.
7. Commit and push after checks pass.

## Acceptance Criteria
- Mobile/tablet account trigger no longer looks like a raw outline button.
- Account panel toggle behavior remains unchanged.
- Button text stays inside the control on mobile and tablet.
- `npm run build`, `npm run audit:ui-responsive`, and `npm run audit:ui-navigation` pass.
- Source-of-truth files record the result and evidence.

## Definition of Done
- [x] Build passes.
- [x] Responsive and navigation audits pass.
- [x] Account trigger interaction proof passes.
- [x] Representative desktop/tablet/mobile shell screenshots are reviewed.
- [x] Project state, module confidence, requirements, quality, and next steps are updated.
- [x] Changes are committed and pushed.

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
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - `npm run audit:ui-responsive` in `web/` -> PASS with `route_count=14`,
    `viewport_count=3`, `screenshot_count=18`, `failed_count=0`
  - `npm run audit:ui-navigation` in `web/` -> PASS with `step_count=4`,
    `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json`
    in `web/` -> PASS with `account_proof.status=ok`, `step_count=1`,
    `failed_count=0`, `panel_visible=true`
- Manual checks: reviewed refreshed mobile Dashboard, mobile Settings, and
  tablet Dashboard screenshots from
  `.codex/artifacts/prj1150-v11-ui-responsive-audit`
- Screenshots/logs:
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/mobile-dashboard.png`
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/mobile-settings.png`
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/tablet-dashboard.png`
  - `.codex/artifacts/prj1225-account-proof/report.json`
- High-risk checks: cleanup found no active validation-owned
  `chrome-headless-shell`, no route-smoke/Vite/5173 Node process, and no
  listener on `5173`
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: AVIARY-WEB-RESP-001
- Requirements matrix updated: yes
- Requirement rows closed or changed: REQ-UX-001
- Quality scenarios updated: yes
- Quality scenario rows closed or changed: QA-UX-001
- Risk register updated: not applicable
- Risk rows closed or changed: none
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: existing authenticated shell account panel contract
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: audit_screenshot
- Design source reference: `.codex/artifacts/prj1150-v11-ui-responsive-audit/mobile-dashboard.png`
- Canonical visual target: authenticated shared shell header
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: authenticated route header and account panel
- New shared pattern introduced: mobile/tablet account trigger styling plus
  account-trigger route-smoke proof
- Design-memory entry reused: Shared shell navigation layout checkpoint
- Design-memory update required: yes
- Visual gap audit completed: yes
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: none for this focused slice
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop, tablet, mobile passed
- Input-mode checks: pointer/touch account trigger interaction passed through
  account proof
- Accessibility checks: `aria-expanded` now reflects mobile account panel state
- Parity evidence: mobile/tablet account trigger now matches the soft shell
  material language and still opens the account panel

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert this frontend-only commit
- Observability or alerting impact: none
- Staged rollout or feature flag: none

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was selected in this iteration.
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
- [x] Learning journal was updated if a recurring pitfall was confirmed or confirmed not needed.

## Notes
Safe assumption: the account trigger should remain text-visible in mobile/tablet headers, but its visual treatment should match the Aviary shell rather than generic DaisyUI outline styling.

## Result Report
- Result: mobile/tablet account trigger now uses a dedicated Aviary shell
  material style instead of generic outline button styling, and it exposes
  `aria-expanded` for account panel state.
- Files changed in product code: `web/src/App.tsx`, `web/src/index.css`.
- Files changed in validation: `web/scripts/route-smoke.mjs`.
- Architecture impact: none; existing account panel, auth, logout, and
  desktop utility account trigger behavior were preserved.
- Deployment impact: none; frontend-only shared shell polish and route-smoke
  proof expansion.
- Residual risk: deeper account panel layout/content polish remains a separate
  future slice if screenshots show it needs more hierarchy work.
