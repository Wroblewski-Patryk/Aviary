# Task

## Header
- ID: PRJ-1257
- Title: Dashboard desktop hero signal satellite quieting
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1256
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1257
- Quality Scenario Rows: QA-UX-1257
- Risk Rows: RISK-UI-1257
- Iteration: 1257
- Operation Mode: BUILDER
- Mission ID: PRJ-1257-dashboard-desktop-hero-satellite-quieting
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
- Mission objective: make desktop Dashboard hero signal cards read more like quiet canonical satellites connected to the central figure.
- Release objective advanced: v1.2 web Dashboard canonical desktop first-viewport composition.
- Included slices: CSS-only desktop hero signal material, connector, typography, and column proportion tuning.
- Explicit exclusions: no Dashboard data/copy changes, no mobile signal rail changes, no cognitive flow changes, no backend/API changes, no Chat or Personality changes.
- Checkpoint cadence: CSS patch, Dashboard screenshot gate, navigation/account proof, cleanup, source-of-truth update.
- Stop conditions: any hero signal disappears, connector lines collide with text/figure, desktop figure loses visual primacy, tablet/mobile regress, or document overflow appears.
- Handoff expectation: next checkpoint should pick one exact route mismatch or request a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, task board | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Copernicus subagent | canonical references, latest screenshots | Read-only priority report | Checkpoint recommendation | Report integrated | DONE |
| QA/Test | Carver subagent | route-smoke scripts, cleanup notes | Read-only validation plan | Commands and pitfalls | Report integrated | DONE |
| Frontend/UX | Active chat | canonical screenshot, `docs/ux/design-memory.md` | `web/src/index.css` | CSS-only Dashboard hero signal pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
After `PRJ-1256`, Personality mobile callout connectors are verified. The next visible flagship mismatch from coordinator screenshot review is Dashboard desktop: hero-side signals still read as chunky text cards, while the canonical Dashboard reference treats them as lighter satellites connected to the central embodied scene.

## Goal
Quiet Dashboard desktop hero signal cards into lighter satellite annotations while preserving all supported signals and responsive behavior.

## Scope
- `web/src/index.css`
- Route/surface: `/dashboard`
- Selectors: `.aion-dashboard-hero-grid`, `.aion-dashboard-signal-column`, `.aion-dashboard-signal-card`, `.aion-dashboard-signal-card::after`, `.aion-dashboard-signal-*`

## Implementation Plan
1. Keep Dashboard component markup and backend-backed data unchanged.
2. On large desktop, slightly narrow the side signal columns so the central figure stage remains primary.
3. Reduce hero signal material weight through smaller padding, lighter background, lighter border, and softer shadow.
4. Keep connector lines visible and aligned, but less card-heavy.
5. Preserve tablet/mobile overrides unless screenshot proof requires adjustment.
6. Run focused Dashboard screenshots, build, navigation/account proof, `git diff --check`, and cleanup checks.

## Acceptance Criteria
- Desktop Dashboard hero signals read as quiet satellites around the central figure.
- All six hero signals remain visible and readable.
- Central figure stage remains visually primary.
- Tablet and mobile Dashboard remain stable.
- Dashboard desktop/tablet/mobile screenshot gate passes.

## Definition of Done
- [x] CSS-only Dashboard hero signal patch is implemented.
- [x] Dashboard desktop/tablet/mobile screenshot gate passes.
- [x] Build, navigation proof, and account proof pass.
- [x] Cleanup checks are recorded.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing Dashboard data, labels, route behavior, cognitive flow, mobile flow rail, backend/API behavior, Chat, Personality, or canonical assets
- hiding supported hero signals or values

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS.
  - `node scripts\route-smoke.mjs --screenshots C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1257-dashboard-desktop-hero-satellite-quieting\screenshots --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1257-dashboard-desktop-hero-satellite-quieting\report.json --screenshot-routes /dashboard --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --navigation-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1257-dashboard-desktop-hero-satellite-quieting\navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --account-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1257-dashboard-desktop-hero-satellite-quieting\account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Desktop Dashboard screenshot reviewed against `aion-dashboard-canonical-reference-v2.png`: hero signals are lighter and read more like connected satellites while all six values remain visible.
  - Tablet and mobile screenshots remained stable.
- Screenshots/logs:
  - `.codex/artifacts/prj1257-dashboard-desktop-hero-satellite-quieting/screenshots/desktop-dashboard.png`
  - `.codex/artifacts/prj1257-dashboard-desktop-hero-satellite-quieting/screenshots/tablet-dashboard.png`
  - `.codex/artifacts/prj1257-dashboard-desktop-hero-satellite-quieting/screenshots/mobile-dashboard.png`
  - `.codex/artifacts/prj1257-dashboard-desktop-hero-satellite-quieting/report.json`
  - `.codex/artifacts/prj1257-dashboard-desktop-hero-satellite-quieting/navigation-proof.json`
  - `.codex/artifacts/prj1257-dashboard-desktop-hero-satellite-quieting/account-proof.json`
- Cleanup:
  - No validation-owned node/Vite, route-smoke, Chromium, or headless browser process remained.
  - No listener on ports `5173` or `4173`.
  - Three fresh route-smoke temp profiles from this checkpoint were removed.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`; `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/screenshots/desktop-dashboard.png`
- Canonical visual target: desktop hero signals as quiet connected satellites around the central embodied figure.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-dashboard-signal-card`
- New shared pattern introduced: no
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical icon glyphs, richer metric content, and full Dashboard 95% pixel parity remain separate decisions.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: quieted desktop Dashboard hero signal cards so they read more like connected satellites around the central figure.
- Files changed: `web/src/index.css`; project task, state, requirement, quality, risk, design-memory, and coordination ledgers.
- How tested: build, focused Dashboard desktop/tablet/mobile screenshot gate, navigation proof, account proof, screenshot review, `git diff --check`, and cleanup checks.
- What is incomplete: not a full Dashboard 95% pixel parity claim; exact canonical icons/content/data parity remains separate.
- Next steps: pick one exact remaining screenshot mismatch on one route, or make a content/data decision before changing canonical copy, icon glyphs, or backend-backed labels.
- Decisions made: kept all Dashboard signals/data/labels and route behavior unchanged; scoped the visual change to large-desktop hero signal CSS.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: desktop Dashboard hero signals still read as heavy text cards instead of canonical satellites.
- Gaps: no backend/API or component work needed.
- Inconsistencies: canonical Dashboard reference gives the central figure more primacy and uses lighter connected side metrics.
- Architecture constraints: preserve existing data and route contracts.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1257 Dashboard desktop hero signal satellite quieting.
- Priority rationale: it is the largest remaining screenshot-backed flagship mismatch after Chat and Personality micro-slices.
- Why other candidates were deferred: exact icon/content/data parity requires product decisions; recent Chat and Personality slices are verified.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only desktop material/proportion tuning for Dashboard hero signals.
- Edge cases: hidden values, weak contrast, connector collision, tablet/mobile regression, overflow.

### 4. Execute Implementation
- Implementation notes: narrowed large-desktop side signal columns, reduced card material, softened shadows/borders, slightly tightened text, and extended connector lines.

### 5. Verify and Test
- Validation performed: build, focused Dashboard screenshot gate across desktop/tablet/mobile, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- Result: verified.

### 6. Self-Review
- Simpler option considered: only lowering opacity; screenshot review favored a combined material/proportion adjustment so the central hero regained primacy.
- Technical debt introduced: no
- Scalability assessment: CSS remains route-local and large-desktop scoped.
- Refinements made: preserved tablet/mobile override behavior.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`
- Context updated: task board, project state, active mission, current focus, next steps, module confidence ledger, requirements matrix, quality scenarios, risk register, system health, and agent evals.
- Learning journal updated: not applicable
