# Task

## Header
- ID: PRJ-1252
- Title: Personality mobile embodied-map callout compression
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1251
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1252
- Quality Scenario Rows: QA-UX-1252
- Risk Rows: RISK-UI-1252
- Iteration: 1252
- Operation Mode: BUILDER
- Mission ID: PRJ-1252-personality-mobile-callout-map-quieting
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` and active mission state were reviewed through the current mission packet.
- [x] Affected module confidence, requirement, quality, and risk rows were identified.
- [x] The task improves release confidence, not only local appearance.

## Mission Block
- Mission objective: make mobile Personality hero callouts feel like compact embodied-map annotations instead of chunky cards covering the figure.
- Release objective advanced: v1.2 web Personality canonical mobile first-read quality.
- Included slices: CSS-only mobile callout size, material, typography, and placement tuning.
- Explicit exclusions: no callout copy/labels/counts/data changes, no backend/runtime changes, no route behavior changes, no shared shell, Dashboard, or Chat changes, no hiding supported callouts.
- Checkpoint cadence: CSS patch, Personality screenshot gate, build, route smoke, navigation/account proof, cleanup, source-of-truth update.
- Stop conditions: any supported callout becomes undiscoverable, the figure is obscured more than before, document overflow appears, or desktop/tablet Personality regresses.
- Handoff expectation: next checkpoint should pick one exact remaining route mismatch or request a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, task board | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Bacon subagent | canonical Personality asset, recent screenshots | Read-only priority report | Single checkpoint recommendation | Report integrated | DONE |
| QA/Test | Nash subagent | route-smoke scripts, recent cleanup notes | Read-only validation plan | Commands and pitfalls | Report integrated | DONE |
| Frontend/UX | Active chat | `docs/ux/design-memory.md`, screenshots | `web/src/index.css` | CSS-only mobile Personality callout pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
After PRJ-1251, Dashboard mobile first-read is calmer. Fresh Personality screenshots and the UX parity lane show that mobile Personality is structurally close to the canonical embodied map, but hero callouts still read like oversized metric cards over the figure.

## Goal
Compress and quiet mobile Personality callouts while keeping every supported callout visible and preserving backend-backed values.

## Scope
- `web/src/index.css`
- Route/surface: `/personality`
- Selectors: `.aion-personality-callout`, `.aion-personality-callout-identity`, `.aion-personality-callout-knowledge`, `.aion-personality-callout-planning`, `.aion-personality-callout-skills`, `.aion-personality-role-card`

## Implementation Plan
1. Tune mobile callout width, padding, radius, material, and shadow.
2. Reduce title/body typography inside callouts on mobile.
3. Adjust mobile placement so lower callouts cover less of the figure.
4. Preserve all callouts and values.
5. Run focused Personality screenshots and full web route proof.
6. Update source-of-truth state and design memory before closure.

## Acceptance Criteria
- Mobile Personality callouts read as compact map annotations, not heavy cards.
- All supported callouts remain visible.
- The figure/embodied map is less obstructed than before.
- Personality desktop/tablet/mobile screenshot gate passes.
- Full route smoke, navigation proof, account proof, and cleanup checks pass.

## Definition of Done
- [x] CSS-only mobile Personality callout patch is implemented.
- [x] Personality desktop/tablet/mobile screenshot gate passes.
- [x] Build, route smoke, navigation proof, and account proof pass.
- [x] Cleanup checks are recorded.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing callout copy, labels, counts, backend-backed values, personality data, route behavior, shared shell, Dashboard, Chat, or canonical assets
- hiding supported callouts

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS.
  - `node scripts\route-smoke.mjs --screenshots C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1252-personality-mobile-callout-map\screenshots --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1252-personality-mobile-callout-map\report.json --screenshot-routes /personality --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --navigation-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1252-personality-mobile-callout-map\navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --account-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1252-personality-mobile-callout-map\account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Mobile Personality screenshot reviewed after the second pass: callouts are smaller and quieter; `Planning` no longer wraps; all supported callouts remain visible; the portrait/embodied map breathes better.
  - Desktop and tablet Personality screenshots stayed structurally stable.
- Screenshots/logs:
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/screenshots/mobile-personality.png`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/screenshots/tablet-personality.png`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/screenshots/desktop-personality.png`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/report.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/navigation-proof.json`
  - `.codex/artifacts/prj1252-personality-mobile-callout-map/account-proof.json`
- Cleanup:
  - No active `chrome-headless-shell` process found.
  - No listener on ports `5173` or `4173`.
  - No active Personality `route-smoke.mjs` or Vite process found.
  - Four fresh route-smoke temp profiles from this checkpoint were removed; older historical temp profiles were left untouched.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-personality-canonical-reference-v1.png`; `.codex/artifacts/prj1250-next-ui-audit/screenshots/mobile-personality.png`
- Canonical visual target: Personality mobile hero as an embodied map with compact annotations
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-personality-callout`
- New shared pattern introduced: no
- Design-memory entry reused: Personality canonical fidelity
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical icon/content/copy parity remains a separate content/data decision; this slice is a verified mobile callout hierarchy pass.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: compressed and quieted mobile Personality callouts so they read more like compact embodied-map annotations instead of chunky metric cards over the figure.
- Files changed: `web/src/index.css`; project state, task, requirement, quality, risk, design-memory, and coordination ledgers.
- How tested: build, focused Personality desktop/tablet/mobile screenshot gate, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- What is incomplete: not a full 95% pixel parity claim; exact canonical iconography, copy density, and backend content alignment remain separate product/data decisions.
- Next steps: choose one exact remaining screenshot mismatch on one route, or make a content/data decision before changing canonical labels, icons, or route fixture content.
- Decisions made: keep all supported Personality callouts visible; reduce only mobile annotation material, typography, and placement; do not restore the hidden mobile role card without a product decision.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: mobile Personality hero callouts are still too card-heavy and obscure the figure.
- Gaps: no backend/API work needed; this is CSS hierarchy and placement.
- Inconsistencies: canonical reference uses compact annotations, while current mobile callouts read as metric cards.
- Architecture constraints: preserve existing data and route/component contracts.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1252 Personality mobile callout quieting.
- Priority rationale: UX parity lane identified it as the next smallest high-impact mismatch after Dashboard and Chat were verified.
- Why other candidates were deferred: exact content/icon parity requires separate content decisions; Dashboard and Chat latest slices are verified.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only mobile callout density and placement.
- Edge cases: hidden callouts, increased portrait occlusion, desktop/tablet regression, mobile overflow.

### 4. Execute Implementation
- Implementation notes: reduced mobile callout width, padding, typography, radius, material weight, and lower callout placement; widened the Planning callout enough to keep `0 active goals` on one line.

### 5. Verify and Test
- Validation performed: build, focused Personality screenshot gate across desktop/tablet/mobile, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- Result: PASS; `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`; navigation `failed_count=0`; account `panel_visible=true`.

### 6. Self-Review
- Simpler option considered: hiding or removing callouts would have reduced clutter faster, but it would have hidden supported backend-backed data and violated the mission.
- Technical debt introduced: no
- Scalability assessment: CSS-only mobile route-local adjustment stays inside the existing Personality pattern and does not add a new component family.
- Refinements made: reduced value typography after screenshot review showed the first Planning pass wrapped awkwardly.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`
- Context updated: `.codex/context/PROJECT_STATE.md`, `.codex/context/TASK_BOARD.md`, `.agents/state/active-mission.md`, `.agents/state/current-focus.md`, `.agents/state/next-steps.md`, `.agents/state/module-confidence-ledger.md`, `.agents/state/requirements-verification-matrix.md`, `.agents/state/quality-attribute-scenarios.md`, `.agents/state/risk-register.md`, `.agents/state/system-health.md`, `.agents/state/agent-evals.md`
- Learning journal updated: not applicable
