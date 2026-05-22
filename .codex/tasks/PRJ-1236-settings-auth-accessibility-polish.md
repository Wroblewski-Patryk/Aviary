# Task

## Header
- ID: PRJ-1236
- Title: Settings and auth accessibility polish
- Task Type: fix
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1235
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: `AVIARY-WEB-RESP-001`
- Requirement Rows: `REQ-UX-1236`
- Quality Scenario Rows: `QA-UX-1236`
- Risk Rows: `RISK-UI-1236`
- Iteration: 1236
- Operation Mode: BUILDER
- Mission ID: PRJ-1236-settings-auth-accessibility-polish
- Mission Status: COMPLETED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed in active mission context.
- [x] `.agents/core/mission-control.md` was reviewed for continuation work.
- [x] Missing or template-like state tables were confirmed not needed for this bounded frontend slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: close the next small accessibility/interaction gap after PRJ-1235 by aligning auth modal mode controls and Settings form controls with their real behavior and names.
- Release objective advanced: local v1.2 web release-candidate confidence.
- Included slices: auth modal segmented-control semantics, modal focus management, Settings control accessible names, Settings copy clarity, diagnostics status de-inerting, mobile auth backdrop focus, full route/screenshot/navigation/account proof, state updates.
- Explicit exclusions: backend/API/runtime, native app implementation, production release, visual redesign.
- Checkpoint cadence: one implementation patch, then full local UX gate.
- Stop conditions: route smoke regression, auth modal becomes harder to operate, Settings controls lose visible labels, or validation reveals a wider interaction model change.
- Handoff expectation: green proof and durable state update.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `AGENTS.md`, mission-control, task board | Integration, state, final decision | Mission closure | Parent validation gate | DONE |
| A11y Audit | Subagent Planck | web shell/app/settings/auth code | Read-only residual report | Ranked findings | Lane report | DONE |
| UX Residual Audit | Subagent Nietzsche | PRJ-1235 screenshots, UX docs | Read-only visual residual report | Ranked findings | Lane report | DONE |
| Frontend/UX | Active chat | `web/src/App.tsx`, `web/src/index.css` | Auth/Settings semantics and copy | Patch | Build + route proof | DONE |
| QA/Test | Active chat | route-smoke, screenshots | Local UX gate | Proof reports | 42 screenshots + nav/account | DONE |
| Docs/State | Active chat | state docs | Durable evidence | Updated ledgers | State diff | DONE |

## Context
PRJ-1235 made the shared mobile shell more compact and removed inert utility buttons. The remaining highest-value non-visual polish from the prior code/a11y audit is form and modal semantics: auth mode buttons currently look like tabs but do not implement a full tab pattern, and Settings controls need explicit accessible names.

## Goal
Make the auth modal and Settings controls more honest, keyboard-friendly, and assistive-technology-friendly without changing product behavior or adding new UI chrome.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/tasks/PRJ-1236-settings-auth-accessibility-polish.md`
- required state/context docs

## Implementation Plan
1. Convert auth modal mode controls from an incomplete `tablist` pattern to a segmented button group with `aria-pressed`.
2. Add explicit accessible names to Settings editable controls: display name, UI language, UTC offset, proactive follow-ups, and reset confirmation.
3. Run syntax/build, route smoke, full screenshot gate, navigation proof, account proof, and focused screenshot review.
4. Update task/state docs and commit if green.

## Acceptance Criteria
- Auth modal no longer exposes an incomplete tab pattern.
- Login/register mode buttons expose selected state through `aria-pressed`.
- Settings controls have explicit accessible names.
- No visible layout regression across desktop/tablet/mobile.
- Full local UX proof remains green.

## Definition of Done
- [x] Implementation patch is scoped to auth/Settings semantics, Settings copy, and auth backdrop focus.
- [x] `node --check scripts/route-smoke.mjs` passes.
- [x] `npm run build` passes.
- [x] route smoke reports `route_count=14`, `status=ok`.
- [x] responsive screenshot gate reports `screenshot_count=42`, `failed_count=0`.
- [x] navigation proof and account proof pass.
- [x] Manual screenshot review covers Login/Auth and Settings.
- [x] Cleanup check shows no PRJ-1236 validation-owned leftovers.
- [x] State docs are updated.

## Forbidden
- new auth flow
- new Settings information architecture
- backend/API/runtime changes
- temporary bypasses
- production release claim

## Validation Evidence
- Tests:
  - `Push-Location .\web; node --check scripts/route-smoke.mjs; npm run build; Pop-Location` -> PASS.
  - route smoke -> `route_count=14`, `status=ok`.
  - full responsive screenshot gate -> `viewport_count=3`, `screenshot_count=42`, `failed_count=0`.
  - navigation proof -> `step_count=4`, `failed_count=0`.
  - account proof -> `step_count=1`, `failed_count=0`, `panel_visible=true`.
- Manual checks:
  - Reviewed `mobile-login.png`, `mobile-settings.png`, `desktop-settings.png`, and `desktop-dashboard.png`.
  - Auth modal no longer exposes an incomplete tablist; login/register are segmented buttons with `aria-pressed`.
  - Auth modal focuses the email field on open, traps Tab/Shift+Tab within the dialog, closes on Escape, and attempts focus restore to the opener.
  - Settings editable controls have explicit accessible names.
  - Desktop diagnostics support text is non-interactive status copy.
  - Settings copy is calmer and less implementation-oriented.
- Screenshots/logs:
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/screenshots/`
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/screenshot-gate-report.json`
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/navigation-proof-report.json`
  - `.codex/artifacts/prj1236-settings-auth-accessibility-polish/account-proof-report.json`
- High-risk checks:
  - In-app Browser proof was attempted for `/login`, but the Browser plugin reported no active Codex browser pane. This is recorded as a Browser-path blocker; route-smoke screenshot and static self-review remain the current proof.
  - Cleanup stopped validation-owned Vite preview process trees and found no PRJ-1236 `chrome-headless-shell`, route-smoke/dev-server processes, or `4173`/`4174` listeners. An unrelated `Obiekty` dev server on `5173` was observed and left untouched.
- Reality status: verified local web UX checkpoint

## Result Report
PRJ-1236 is complete as a local v1.2 web accessibility/interaction polish checkpoint. Auth modal semantics and focus behavior are more honest, Settings controls are explicitly named, Settings copy is less implementation-oriented, diagnostics status no longer behaves like an inert button, and the full route/screenshot/navigation/account gate remains green.
