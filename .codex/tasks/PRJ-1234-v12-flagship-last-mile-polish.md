# Task

## Header
- ID: PRJ-1234
- Title: v1.2 flagship last-mile UX/UI polish
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1233
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: `WEB-APP`, `WEB-UI-FLAGSHIP`
- Requirement Rows: `REQ-UX-V12-FLAGSHIP-PARITY`
- Quality Scenario Rows: `QA-UX-RESPONSIVE`, `QA-UX-A11Y`
- Risk Rows: `RISK-UX-CANONICAL-DRIFT`
- Iteration: 1234
- Operation Mode: BUILDER
- Mission ID: PRJ-1234-v12-flagship-last-mile-polish
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed in the active mission context.
- [x] `.agents/core/mission-control.md` was reviewed in the active mission context.
- [x] Missing or template-like state tables were confirmed not needed for this CSS/UI slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: close the final documented flagship-detail checklist for Dashboard, Chat, Personality, and shared shell so the v1.2 web app becomes a stronger mobile-app foundation.
- Release objective advanced: local v1.2 web UX release-candidate confidence.
- Included slices: CSS last-mile rhythm/crop/hierarchy polish; low-risk accessibility semantics; screenshot-contract proof; docs/state updates.
- Explicit exclusions: backend/API/runtime/database/native implementation and production release promotion.
- Checkpoint cadence: one implementation checkpoint followed by the full PRJ-1234 local UX gate.
- Stop conditions: canonical references conflict with user notes, screenshot gate fails with structural overflow, or a change requires backend/product behavior.
- Handoff expectation: green validation evidence, screenshot artifact path, residual visual mismatches, and next release-candidate decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `AGENTS.md`, active mission, task board | Integration, final decision, docs/state | Mission closure and truthful pass/fail | Parent validation gate | DONE |
| UX Gap Audit | Subagent Pauli | canonical refs, PRJ-1233 screenshots | Dashboard, Chat, Personality visual deltas | Ranked visual gaps | Read-only lane report | DONE |
| Design-System Audit | Subagent Banach plus previous Bohr | web CSS/components | Low-risk UI/accessibility improvements | Safe patch recommendations | Read-only lane report | DONE |
| QA/Test | Subagent Wegener | route smoke scripts, testing docs | Local UX proof gate | Gate contract | Read-only lane report | DONE |
| Frontend/UX | Active chat | final flagship checklist | `web/src/index.css`, shell/accessibility where safe | Last-mile polish patch | Build and screenshots | DONE |
| Backend/API | Explicit omission | Excluded by scope | none | No backend changes | Diff audit | OMITTED |
| Security/Ops/Docs | Active chat | state docs | docs/state updates | Evidence and release boundary | Updated state | DONE |

### Lane Checks

- [x] `.agents/state/active-mission.md` was refreshed for broad work.
- [x] `.agents/workflows/responsibility-lanes.md` was reviewed in mission context.
- [x] Every important responsibility has an owner or explicit omission.
- [x] No delegated write lanes overlap.
- [x] Each delegated lane has expected output and proof.
- [x] Missing ownership/evidence/context gaps will be recorded if found.
- [x] Process eval will be recorded if coordination issues appear.

## Context
PRJ-1233 produced a green 42-screenshot v1.2 web polish checkpoint. The remaining documented work is a last-mile flagship checklist for Dashboard, Chat, Personality, and shared shell.

## Goal
Make the authenticated flagship web surfaces feel calmer, simpler, and closer to the canonical references across desktop, tablet, and mobile, while preserving the already-green route contract.

## Scope
- `web/src/index.css`
- `web/src/components/shell.tsx` if accessibility-only semantics are added
- `web/src/App.tsx` if accessibility-only semantics are added
- `web/scripts/route-smoke.mjs` only if screenshot contract drift is corrected
- `.codex/tasks/PRJ-1234-v12-flagship-last-mile-polish.md`
- state/context docs required for mission closure

## Implementation Plan
1. Gather lane audits and compare current screenshots against canonical references.
2. Apply the smallest useful visual polish for Dashboard, Chat, Personality, and shared shell hierarchy.
3. Apply low-risk accessibility semantics that do not alter product behavior.
4. Run the PRJ-1234 local UX gate.
5. Review screenshots, clean validation processes, update state/docs, and commit.

## Success Signal
- User or operator problem: the web app should feel ready to use as a polished personality companion and credible base for mobile UI.
- Expected product or reliability outcome: flagship surfaces are structurally faithful, responsive, and free of obvious visual clutter or overflow.
- How success will be observed: 42 screenshot gate green plus manual review of touched flagship screenshots.
- Post-launch learning needed: yes

## Deliverable For This Stage
Integrated implementation patch plus validation artifacts for the local UX pass.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within web UX/UI and accessibility scope
- do not claim production v1.2 release without a separate deployment mission

## Acceptance Criteria
- Dashboard guidance, recent activity, intention, and lower grid read as one calm flagship surface.
- Chat transcript/composer is the dominant conversation instrument; context belt/support column stay quiet.
- Personality side stack hierarchy is clearer; mobile compression remains ceremonial and legible.
- Shared shell keeps premium/inset feel across flagship routes.
- Full local UX proof gate passes.

## Definition of Done
- [x] CSS/semantics patch is complete and scoped.
- [x] `node --check scripts/route-smoke.mjs` passes.
- [x] `npm run build` passes.
- [x] route smoke reports `route_count=14`, `status=ok`.
- [x] responsive screenshot gate reports `screenshot_count=42`, `failed_count=0`.
- [x] navigation proof and account proof pass.
- [x] Manual screenshot review covers touched flagship surfaces.
- [x] Cleanup check shows no validation-owned browser/server leftovers.
- [x] State docs and module confidence are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- backend/API/runtime/deploy changes
- production release claim without deploy parity proof

## Validation Evidence
- Tests: `node --check scripts/route-smoke.mjs`; `npm run build`; route smoke; full screenshot gate; navigation proof; account proof; `git diff --check`.
- Manual checks: desktop Dashboard/Chat, tablet Dashboard, mobile Chat/Personality screenshot review.
- Screenshots/logs: `.codex/artifacts/prj1234-flagship-last-mile-polish/screenshots/`; route/nav/account reports in the same artifact folder.
- High-risk checks: no framework overlays, no horizontal overflow, no unnamed visible interactive controls, cleanup checks for browser/dev-server leftovers.
- Coverage ledger updated: not applicable
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/architecture/architecture-source-of-truth.md`, active mission context
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: canonical screenshot assets under `docs/ux/assets/`
- Canonical visual target: final flagship checklist for Dashboard, Chat, Personality
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: Aviary vellum shell, route-smoke screenshot gate
- New shared pattern introduced: no
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: mobile Chat still intentionally favors conversation-first simplicity over showing all six cognitive cards; full production v1.2 parity is not claimed until release promotion.
- State checks: success via route smoke; loading/empty/error not changed
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: pending touch/pointer/keyboard smoke
- Accessibility checks: route-smoke unnamed interactive count `0`; route `aria-current`, account popover semantics, disclosure focus-visible improvements.
- Parity evidence: `screenshot_count=42`, `failed_count=0`, touched flagship screenshots manually reviewed.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert PRJ-1234 commit
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
PRJ-1234 is verified for the local v1.2 flagship last-mile UX checkpoint.

Implemented:
- lighter desktop utility bar rhythm and display-token alias
- calmer Chat stage/portrait-panel spacing
- Dashboard guidance hierarchy and wide-screen right-column pacing refinements
- compact mobile Personality learned-knowledge callout restoration
- clearer Personality side-stack hierarchy
- route/account/disclosure accessibility semantics

Validation:
- `node --check scripts/route-smoke.mjs` -> PASS
- `npm run build` -> PASS
- route smoke -> `route_count=14`, `status=ok`
- full screenshot gate -> `viewport_count=3`, `screenshot_count=42`, `failed_count=0`
- navigation proof -> `step_count=4`, `failed_count=0`
- account proof -> `step_count=1`, `failed_count=0`, `panel_visible=true`
- `git diff --check` -> PASS with LF/CRLF warnings only
- cleanup -> no validation-owned browser, route-smoke, dev-server, or `5173`/`4173` listener leftovers

Residual risk:
- This is not a production v1.2 release.
- Mobile Chat full six-card canonical context remains a product taste decision
  because PRJ-1233 intentionally favored faster conversation-first entry.
