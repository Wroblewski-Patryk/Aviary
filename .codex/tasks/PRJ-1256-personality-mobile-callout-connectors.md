# Task

## Header
- ID: PRJ-1256
- Title: Personality mobile callout connector visibility
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1255
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1256
- Quality Scenario Rows: QA-UX-1256
- Risk Rows: RISK-UI-1256
- Iteration: 1256
- Operation Mode: BUILDER
- Mission ID: PRJ-1256-personality-mobile-callout-connectors
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] Affected module confidence, requirement, quality, and risk rows were identified.
- [x] The task improves release confidence, not only local appearance.

## Mission Block
- Mission objective: make mobile Personality callout connector lines readable enough that callouts feel attached to the embodied figure.
- Release objective advanced: v1.2 web Personality canonical mobile embodied-map clarity.
- Included slices: CSS-only mobile connector line and endpoint visibility for existing callouts.
- Explicit exclusions: no copy, labels, values, backend data, role card restoration, timeline rail changes, Dashboard, Chat, shared shell, navigation, or asset changes.
- Checkpoint cadence: CSS patch, Personality screenshot gate, navigation/account proof, cleanup, source-of-truth update.
- Stop conditions: connectors overlap face/callout text awkwardly, any callout disappears, timeline rail regresses, document overflow appears, or desktop/tablet Personality regress.
- Handoff expectation: next checkpoint should pick one exact route mismatch or request a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, task board | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Lagrange subagent | canonical references, latest screenshots | Read-only priority report | Checkpoint recommendation | Report integrated | DONE |
| QA/Test | Darwin subagent | route-smoke scripts, cleanup notes | Read-only validation plan | Commands and pitfalls | Report integrated | DONE |
| Frontend/UX | Active chat | canonical screenshot, `docs/ux/design-memory.md` | `web/src/index.css` | CSS-only mobile connector pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
`PRJ-1252` made mobile Personality callouts lighter and `PRJ-1254` made the Mind Layers Timeline compact. Lagrange's UX parity lane identified the next smallest mismatch: mobile connector lines and endpoint dots are too faint, so the callouts do not read as clearly attached to the embodied figure as in the canonical mobile reference.

## Goal
Strengthen mobile Personality callout connectors without changing supported callouts, data, timeline, or artwork.

## Scope
- `web/src/index.css`
- Route/surface: `/personality`
- Selectors: `.aion-personality-callout::before`, `.aion-personality-callout::after`, `.aion-personality-callout-identity`, `.aion-personality-callout-knowledge`, `.aion-personality-callout-planning`, `.aion-personality-callout-skills`

## Implementation Plan
1. Keep Personality component markup and data unchanged.
2. In the mobile breakpoint, increase connector line contrast and endpoint visibility for existing callouts.
3. Preserve compact callout card sizing and the PRJ-1254 timeline rail.
4. Avoid desktop/tablet changes unless screenshot proof requires a reset.
5. Run focused Personality screenshots, build, navigation/account proof, `git diff --check`, and cleanup checks.
6. Update source-of-truth state and design memory before closure.

## Acceptance Criteria
- Mobile callout connector lines and endpoint dots are visible enough to tie callouts to the figure.
- All supported mobile callouts remain visible and readable.
- Mobile timeline rail remains unchanged.
- Personality desktop/tablet/mobile screenshot gate passes.
- Navigation proof, account proof, `git diff --check`, and cleanup checks pass.

## Definition of Done
- [x] CSS-only mobile Personality connector patch is implemented.
- [x] Personality desktop/tablet/mobile screenshot gate passes.
- [x] Build, navigation proof, and account proof pass.
- [x] Cleanup checks are recorded.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing copy, labels, metric values, backend-backed data, fixture content, role card visibility, timeline rail, Dashboard, Chat, shared shell, navigation, account controls, route data, or canonical assets
- hiding supported callouts or values

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS.
  - `node scripts\route-smoke.mjs --screenshots C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1256-personality-mobile-callout-connectors\screenshots --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1256-personality-mobile-callout-connectors\report.json --screenshot-routes /personality --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --navigation-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1256-personality-mobile-callout-connectors\navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --account-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1256-personality-mobile-callout-connectors\account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Mobile Personality screenshot reviewed against `aion-personality-canonical-reference-v1.png`: callout connector lines and endpoint dots are now visible enough to bind callouts to the figure.
  - Desktop and tablet screenshots remained stable.
  - PRJ-1254 compact timeline rail remained intact.
- Screenshots/logs:
  - `.codex/artifacts/prj1256-personality-mobile-callout-connectors/screenshots/mobile-personality.png`
  - `.codex/artifacts/prj1256-personality-mobile-callout-connectors/screenshots/tablet-personality.png`
  - `.codex/artifacts/prj1256-personality-mobile-callout-connectors/screenshots/desktop-personality.png`
  - `.codex/artifacts/prj1256-personality-mobile-callout-connectors/report.json`
  - `.codex/artifacts/prj1256-personality-mobile-callout-connectors/navigation-proof.json`
  - `.codex/artifacts/prj1256-personality-mobile-callout-connectors/account-proof.json`
- Cleanup:
  - No validation-owned node/Vite, route-smoke, Chromium, or headless browser process remained.
  - No listener on ports `5173` or `4173`.
  - Eight fresh route-smoke temp profiles from this checkpoint were removed after iterative screenshot tuning.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-personality-canonical-reference-v1.png`; `.codex/artifacts/prj1254-personality-mobile-timeline-rail/screenshots/mobile-personality.png`
- Canonical visual target: mobile callouts visibly connected to the embodied figure with thin lines and endpoint dots.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-personality-callout`
- New shared pattern introduced: no
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical icon glyphs, richer callout data, and full Personality 95% pixel parity remain separate decisions.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: restored and strengthened mobile Personality callout connector lines/dots so callouts read as attached to the embodied figure.
- Files changed: `web/src/index.css`; project task, state, requirement, quality, risk, design-memory, and coordination ledgers.
- How tested: build, focused Personality desktop/tablet/mobile screenshot gate, navigation proof, account proof, screenshot review, `git diff --check`, and cleanup checks.
- What is incomplete: not a full Personality 95% pixel parity claim; exact canonical icon/data/content parity remains separate.
- Next steps: pick one exact remaining screenshot mismatch on one route, or make a content/data decision before changing canonical copy, icon glyphs, or backend-backed labels.
- Decisions made: pivoted from a broader Dashboard candidate to Lagrange's smaller Personality mobile connector recommendation; restored `display: block` because a broader `max-width: 899px` rule hid connector `::before` lines.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: mobile Personality callout connector lines are too faint to clearly bind callouts to the figure.
- Gaps: no backend/API or component work needed.
- Inconsistencies: canonical mobile reference shows clear thin connector lines and endpoint dots.
- Architecture constraints: preserve existing data and component contracts.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1256 Personality mobile callout connector visibility.
- Priority rationale: Lagrange identified it as the smallest screenshot-backed mismatch after PRJ-1255, and it is safer than another broader layout pass.
- Why other candidates were deferred: Dashboard desktop hero satellites remain a possible future target, but this connector pass is smaller and does not risk desktop composition churn.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only mobile connector visibility tuning.
- Edge cases: connector overlap, text occlusion, too-heavy visual noise, timeline regression, desktop/tablet regression.

### 4. Execute Implementation
- Implementation notes: mobile `.aion-personality-callout::before` now explicitly displays as a thin connector line, and `.aion-personality-callout::after` endpoints are slightly stronger while existing callout cards, values, and timeline rail remain unchanged.

### 5. Verify and Test
- Validation performed: build, focused Personality screenshot gate across desktop/tablet/mobile, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- Result: verified.

### 6. Self-Review
- Simpler option considered: increasing line opacity only; screenshot review showed the line was still hidden because `display: none` from the tablet/mobile guardrail was not reset.
- Technical debt introduced: no
- Scalability assessment: route-local CSS remains bounded to existing callout pseudo-elements.
- Refinements made: restored display before tuning color/endpoint contrast.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`
- Context updated: task board, project state, active mission, current focus, next steps, module confidence ledger, requirements matrix, quality scenarios, risk register, system health, and agent evals.
- Learning journal updated: not applicable
