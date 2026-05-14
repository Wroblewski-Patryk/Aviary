# Task

## Header
- ID: PRJ-1229
- Title: Authenticated desktop utility bar parity
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1228
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-001
- Quality Scenario Rows: QAS-UX-RESPONSIVE
- Risk Rows: not applicable
- Iteration: 1229
- Operation Mode: BUILDER
- Mission ID: UXUI-1TO1-SHELL-1229
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed in the active UI mission.
- [x] `.agents/core/mission-control.md` was reviewed in the active UI mission.
- [x] Missing or template-like state tables were bootstrapped from repository sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified or marked not applicable.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: move the authenticated desktop shell closer to the canonical references by restoring the shared top utility/search/account band already present in the code.
- Release objective advanced: 1:1 UX/UI convergence for the web authenticated layout.
- Included slices: desktop `ShellUtilityBar` visibility, icon/copy cleanup, shell spacing validation.
- Explicit exclusions: no mobile/tablet header rewrite, no fake browser chrome, no route-local dashboard data redesign, no backend or API changes.
- Checkpoint cadence: implement one shared shell slice, run build and UI audits, compare screenshots, update source-of-truth files.
- Stop conditions: build failure, navigation regression, responsive audit failure, or visual evidence that the utility band harms tablet/mobile.
- Handoff expectation: verified task with screenshots and next mismatch listed.

## Context
The canonical authenticated Dashboard and Chat references show a calm top utility band above route content. `docs/ux/design-memory.md` already records this as an approved flagship shell pattern. The current implementation renders `ShellUtilityBar`, but `.aion-shell-toolbar-chat-canonical { display: none !important; }` suppresses it on desktop, leaving Dashboard and Chat structurally lower-fidelity.

## Goal
Restore the existing shared utility bar on desktop authenticated routes and make its visible controls read as intentional Aviary shell chrome.

## Success Signal
- User or operator problem: the authenticated layout lacks the canonical top utility/search/account framing.
- Expected product or reliability outcome: desktop Dashboard and Chat look structurally closer to the approved references while responsive audits stay green.
- How success will be observed: refreshed desktop screenshots show the utility bar above route content; build, responsive audit, navigation audit, and account proof pass.
- Post-launch learning needed: no

## Deliverable For This Stage
Code changes that reuse the existing `ShellUtilityBar` and CSS pattern, plus validation evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Scope
- `web/src/components/shell.tsx`
- `web/src/index.css`
- UX/source-of-truth notes for the verified slice

## Implementation Plan
1. Replace mojibake/glyph text in `ShellUtilityBar` with clean inline SVG icons and ASCII shortcut text.
2. Remove the desktop utility toolbar suppression while keeping it hidden below `xl`.
3. Tune utility bar spacing/density so it behaves like one calm canonical band.
4. Run build, responsive audit, navigation audit, account proof, screenshot review, and cleanup checks.
5. Update context, task board, design memory, and confidence ledgers.

## Acceptance Criteria
- Desktop authenticated routes show one top utility/search/account band.
- Mobile and tablet route headers remain unchanged.
- No fake browser-window controls are introduced.
- Utility bar text and icons contain no mojibake.
- Required UI validations pass.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for the touched UI scope.
- [x] `npm run build` passes in `web/`.
- [x] `npm run audit:ui-responsive` passes.
- [x] `npm run audit:ui-navigation` passes.
- [x] `--account-proof` route smoke passes.
- [x] Desktop Dashboard and Chat screenshots reviewed against canonical references.
- [x] Source-of-truth files updated.
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
  - `npm run build` in `web/` -> PASS.
  - `npm run audit:ui-responsive` -> PASS, `route_count=14`, `viewport_count=3`, `screenshot_count=18`, `failed_count=0`.
  - `npm run audit:ui-navigation` -> PASS, `step_count=4`, `failed_count=0`.
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1225-account-proof/report.json` -> PASS, `account_proof.status=ok`, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warnings only.
- Manual checks:
  - Reviewed refreshed desktop Dashboard and desktop Chat screenshots against canonical references.
  - Reviewed tablet Dashboard and mobile Dashboard screenshots to confirm the utility bar stayed desktop-only.
- Screenshots/logs:
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/desktop-dashboard.png`
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/desktop-chat.png`
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/tablet-dashboard.png`
  - `.codex/artifacts/prj1150-v11-ui-responsive-audit/mobile-dashboard.png`
- High-risk checks:
  - No document-level horizontal overflow on authenticated desktop routes.
  - No unnamed interactive controls.
  - Cleanup checks found no active `chrome-headless-shell`, no AION validation Node processes, and no listener on `5173`.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: AVIARY-WEB-RESP-001
- Requirements matrix updated: yes
- Requirement rows closed or changed: REQ-UX-001
- Quality scenarios updated: yes
- Quality scenario rows closed or changed: QAS-UX-RESPONSIVE
- Risk register updated: not applicable
- Risk rows closed or changed: not applicable
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/ux/canonical-web-screen-reference-set.md`, `docs/ux/design-memory.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: design memory only if pattern details change

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`, `docs/ux/assets/aion-chat-canonical-reference-v5.png`
- Canonical visual target: authenticated flagship shell top utility band
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: `ShellUtilityBar`, `aion-utility-*`
- New shared pattern introduced: no
- Design-memory entry reused: Flagship utility bar
- Design-memory update required: yes
- Visual gap audit completed: yes
- Background or decorative asset strategy: no asset change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: full 1:1 parity still needs the Dashboard lower-card proportions, exact data/copy density, and further route-local flagship surface comparison.
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: pointer | keyboard
- Accessibility checks: route-smoke unnamed interactive controls remained `0`; account proof stayed green.
- Parity evidence: desktop Dashboard and Chat now show the authenticated utility/search/action/account band above route content; tablet and mobile retain their existing route headers.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert this CSS/component slice.
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

## Notes
- Safe assumption: the browser-like chrome in the Dashboard reference remains presentation context and should not be implemented; only the product utility/search/action band is restored.

## Production-Grade Required Contract
- Goal: restore the authenticated desktop utility bar pattern.
- Scope: `web/src/components/shell.tsx`, `web/src/index.css`, related docs/state.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: `ShellUtilityBar` is visible again on desktop authenticated routes through the existing shared shell path. The bar now presents route context, search, focus mode, quick capture, notification count, and account posture in one calm top band. Mobile/tablet headers stayed unchanged. Validation passed and screenshots were reviewed.

## Integration Evidence
No API, backend, database, runtime, deployment, or integration behavior changed.

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: user requesting 1:1 UX/UI convergence
- Existing workaround or pain: hidden utility bar causes structural mismatch with canonical authenticated references
