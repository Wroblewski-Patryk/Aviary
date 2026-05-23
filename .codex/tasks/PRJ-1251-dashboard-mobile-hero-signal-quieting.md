# Task

## Header
- ID: PRJ-1251
- Title: Dashboard mobile hero signal density and numeral clarity pass
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1248, PRJ-1250
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1251
- Quality Scenario Rows: QA-UX-1251
- Risk Rows: RISK-UI-1251
- Iteration: 1251
- Operation Mode: BUILDER
- Mission ID: PRJ-1251-dashboard-mobile-hero-signal-quieting
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
- Mission objective: make mobile Dashboard hero signal cards quieter and make count values read as numerals, while preserving all supported signals and the PRJ-1248 flow rail.
- Release objective advanced: v1.2 web Dashboard canonical mobile first-read quality.
- Included slices: CSS-only Dashboard signal typography, density, decorative wave quieting, and mobile card hierarchy.
- Explicit exclusions: no backend data changes, no fixture/copy/label changes, no route behavior changes, no Chat/Personality/shared shell changes, no hiding supported signals.
- Checkpoint cadence: CSS patch, Dashboard screenshot gate, build, route smoke, navigation/account proof, cleanup, source-of-truth update.
- Stop conditions: any signal becomes undiscoverable, mobile document overflow appears, PRJ-1248 rail/Current Phase regresses, or desktop/tablet Dashboard noticeably worsens.
- Handoff expectation: next checkpoint should pick one exact remaining route mismatch or request a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, task board | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Locke subagent | canonical Dashboard assets, recent screenshots | Read-only priority report | Single checkpoint recommendation | Report integrated | DONE |
| QA/Test | Turing subagent | route-smoke scripts, recent cleanup notes | Read-only validation plan | Commands and pitfalls | Report integrated | DONE |
| Frontend/UX | Active chat | `docs/ux/design-memory.md`, screenshots | `web/src/index.css` | CSS-only Dashboard signal pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
PRJ-1248 made mobile Dashboard's cognitive-flow band compact, and PRJ-1250 completed the latest Chat metadata polish. Fresh screenshots and the UX parity lane show mobile Dashboard still opens with six visually loud hero signal cards. Numeric values such as `1` and `0 / 0` use display styling and read like `I` and `O / O`.

## Goal
Keep all Dashboard hero signals visible while making them quieter support metadata and improving numeral clarity across Dashboard hero signal cards.

## Scope
- `web/src/index.css`
- Route/surface: `/dashboard`
- Selectors: `.aion-dashboard-signal-card`, `.aion-dashboard-signal-value`, `.aion-dashboard-signal-detail`, `.aion-dashboard-signal-note`, `.aion-dashboard-signal-wave`, mobile `.aion-dashboard-hero-grid` signal rules

## Implementation Plan
1. Switch Dashboard signal values from display serif to UI numeric typography with tabular numerals.
2. Reduce signal card material and decorative wave weight on mobile.
3. Preserve every signal card and avoid changing data, labels, or component structure.
4. Run focused Dashboard screenshots and full web route proof.
5. Update source-of-truth state and design memory before closure.

## Acceptance Criteria
- Mobile Dashboard values read as numerals, not ambiguous display glyphs.
- All six supported hero signal cards remain visible.
- Dashboard first viewport feels calmer and less analytics-grid-heavy.
- Desktop/tablet/mobile Dashboard screenshot gate passes.
- Full route smoke, navigation proof, account proof, and cleanup checks pass.

## Definition of Done
- [x] CSS-only Dashboard signal patch is implemented.
- [x] Dashboard desktop/tablet/mobile screenshot gate passes.
- [x] Build, full route smoke, navigation proof, and account proof pass.
- [x] Cleanup checks are recorded.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing source labels, backend data, fixture values, copy, route behavior, icon/content parity, Chat, Personality, shared shell, or navigation
- hiding supported Dashboard signals

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location` -> PASS.
  - `Push-Location .\web; node scripts\route-smoke.mjs --screenshots C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1251-dashboard-mobile-hero-signal-quieting\screenshots --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1251-dashboard-mobile-hero-signal-quieting\report.json --screenshot-routes /dashboard --viewports desktop,tablet,mobile --fail-on-ui-findings; Pop-Location` -> PASS, `screenshot_count=3`, `failed_count=0`, `route_count=14`, `status=ok`.
  - `Push-Location .\web; node scripts\route-smoke.mjs --navigation-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1251-dashboard-mobile-hero-signal-quieting\navigation-proof.json; Pop-Location` -> PASS, `step_count=4`, `failed_count=0`.
  - `Push-Location .\web; node scripts\route-smoke.mjs --account-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1251-dashboard-mobile-hero-signal-quieting\account-proof.json; Pop-Location` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Reviewed mobile Dashboard screenshot after the patch. Hero signal values now read as clear numerals, all six supported signals remain visible, and decorative wave/noise is removed from mobile first-read cards.
  - Reviewed desktop Dashboard screenshot after the patch. Numeric values are clearer and the hero satellite structure remains intact.
  - Dashboard mobile flow rail still reports contained overflowing rail children, matching the intentional PRJ-1248 horizontal rail; document-level `horizontalOverflow=false`.
- Screenshots/logs:
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/screenshots/mobile-dashboard.png`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/screenshots/desktop-dashboard.png`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/report.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/navigation-proof.json`
  - `.codex/artifacts/prj1251-dashboard-mobile-hero-signal-quieting/account-proof.json`
- Cleanup:
  - Cleanup check found no Personality route-smoke, Vite/dev-server, 5173/4173 listener, temp route-smoke profile, temp chat-transcript profile, or headless browser leftovers.
  - Unrelated Vite processes from `C:\Personal\Projekty\Aplikacje\Obiekty` were observed and intentionally not stopped.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`; `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots/mobile-dashboard.png`; `.codex/artifacts/prj1250-next-ui-audit/screenshots/mobile-dashboard.png`
- Canonical visual target: Dashboard hero as a calm scenic overview with signal satellites, not a dense analytics grid
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-dashboard-signal-card`
- New shared pattern introduced: no
- Design-memory entry reused: Dashboard mobile flow rail; Dashboard hero connector geometry
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: this is a verified mobile first-read hierarchy pass, not full pixel-perfect Dashboard parity; exact canonical iconography, copy density, and richer content/data alignment remain separate decisions
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: Dashboard hero signal values now use UI numeric typography, and mobile hero signal cards are quieter by removing decorative waves and third-line note copy from the first-read card treatment.
- Files changed: `web/src/index.css`; `.codex/tasks/PRJ-1251-dashboard-mobile-hero-signal-quieting.md`; state/context/docs files.
- How tested: web build, focused Dashboard desktop/tablet/mobile screenshot gate, full route smoke, navigation proof, account proof, `git diff --check`, screenshot review, cleanup checks.
- What is incomplete: full Dashboard 95% canonical parity and content/icon/copy parity remain outside this CSS-only slice.
- Next steps: choose one exact remaining route mismatch or make a content/data decision before changing labels, icons, or fixture content.
- Decisions made: keep all six Dashboard signals visible; improve numeric typography globally for Dashboard signal values; quiet mobile-only microcopy and decorative wave noise.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: mobile Dashboard hero signal cards are too visually loud and numeric values are ambiguous.
- Gaps: no need for backend/API work; this is a CSS hierarchy and typography slice.
- Inconsistencies: canonical Dashboard wants calm signal satellites, while mobile current state reads like a dense grid.
- Architecture constraints: preserve existing data and route/component contracts.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1251 Dashboard mobile hero signal quieting.
- Priority rationale: both coordinator screenshot review and UX parity lane identified it as the smallest high-impact next UI checkpoint.
- Why other candidates were deferred: Chat source marker is verified; full icon/copy parity requires product/content decisions.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only typography/density changes.
- Edge cases: mobile overflow, desktop/tablet regression, accidental signal hiding.

### 4. Execute Implementation
- Implementation notes: changed `aion-dashboard-signal-value` to UI tabular numerals and tuned mobile `aion-dashboard-signal-card` layout/density; removed mobile decorative wave and note line from first-read cards while preserving card, label, value, and detail.

### 5. Verify and Test
- Validation performed: build, focused Dashboard screenshots, full route smoke, navigation proof, account proof, `git diff --check`, cleanup.
- Result: PASS.

### 6. Self-Review
- Simpler option considered: only changing `font-family`; rejected because mobile cards still looked too dense after the first screenshot.
- Technical debt introduced: no
- Scalability assessment: route-local CSS only; no new components or data contracts.
- Refinements made: after first screenshot, removed mobile decorative wave and note line to reduce hero card noise.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`.
- Context updated: project state, task board, active mission, next steps, module confidence, requirements, quality, risk, system health.
- Learning journal updated: not applicable
