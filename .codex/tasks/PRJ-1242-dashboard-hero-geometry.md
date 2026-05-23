# Task

## Header
- ID: PRJ-1242
- Title: Dashboard hero connector geometry pass
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1241
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1242
- Quality Scenario Rows: QA-UX-1242
- Risk Rows: RISK-UI-1242
- Iteration: 1242
- Operation Mode: ARCHITECT
- Mission ID: PRJ-1242-dashboard-hero-geometry
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
- Mission objective: make Dashboard desktop hero metric geometry read more like the canonical system map without changing data, shell, or route behavior.
- Release objective advanced: v1.2 web UI canonical fidelity for Dashboard.
- Included slices: desktop Dashboard hero layout, metric connector lines, portrait crop.
- Explicit exclusions: no Chat/Personality work, no guidance/lower-grid work, no backend/API changes, no new controls/cards/data.
- Checkpoint cadence: one CSS patch, Dashboard screenshot gate, full route smoke, state update.
- Stop conditions: overflow, clipped hero cards, mobile/tablet regression, route failure, or a return to noisy dashboard-card hierarchy.
- Handoff expectation: next checkpoint should be a separate single-surface slice.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Pasteur subagent | Dashboard canonical reference | Read-only hero geometry audit | Top drift list | Completed report | DONE |
| Frontend/UX | Active chat | UX audit, design memory | `web/src/index.css` | CSS-only desktop hero geometry patch | Fresh screenshots | DONE |
| QA/Test | McClintock subagent | route-smoke scripts | Validation plan | Commands and regression risks | Completed report | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
PRJ-1241 made Dashboard calmer and more canonical, but the remaining named drift is the hero metric geometry: canonical metrics read as side satellites connected to the figure, while the app still reads more like a wide image with small overlay cards.

## Goal
Move the desktop Dashboard hero closer to a canonical system-map composition while preserving the existing backend-backed metrics and all responsive proof.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep the implementation CSS-only and Dashboard-specific

## Definition of Done
- [x] Dashboard desktop hero metrics are positioned as side satellites with visible connector lines.
- [x] Build passes.
- [x] Dashboard desktop/tablet/mobile screenshot gate passes.
- [x] Full route smoke, navigation proof, and account proof pass.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- adding unsupported controls, cards, badges, or fake data

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1242-dashboard-hero-geometry/screenshots --report .codex/artifacts/prj1242-dashboard-hero-geometry/report.json --screenshot-routes /dashboard --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `screenshot_count=3`, `failed_count=0`
  - `node scripts/route-smoke.mjs --report .codex/artifacts/prj1242-dashboard-hero-geometry/route-smoke-report.json` -> PASS, `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` -> PASS, `step_count=4`, `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1242-dashboard-hero-geometry/account-proof.json` -> PASS, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warning only
- Manual checks:
  - Compared `docs/ux/assets/aion-dashboard-canonical-reference-v2.png` with the latest desktop Dashboard screenshot.
  - Verified desktop metric cards now sit as side satellites around the hero, connector lines are visible, and tablet/mobile remain free of overflow through the screenshot gate.
- Screenshots/logs:
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/screenshots/`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/report.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/route-smoke-report.json`
  - `.codex/artifacts/prj1242-dashboard-hero-geometry/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target: Dashboard hero connector/metric geometry
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Dashboard signal columns, figure stage, metric tiles, connector lines
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: not full pixel-perfect parity; static canonical uses a different portrait asset and richer icon glyphs, which are outside this CSS-only geometry slice.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: Dashboard desktop hero metrics were moved from corner overlays into side satellites with visible connector lines.
- Files changed:
  - `web/src/index.css`
- How tested:
  - build, Dashboard screenshot gate, full route smoke, navigation proof, account proof, `git diff --check`, screenshot review.
- What is incomplete:
  - exact pixel parity and icon/content replacement were intentionally not included.
- Decisions made:
  - keep this desktop-first and CSS-only; preserve tablet/mobile simplification and all existing backend-backed metric values.

## Autonomous Loop Evidence

### 1. Analyze Current State
- PRJ-1241 left hero connector/metric geometry as the named residual.

### 2. Select One Priority Mission Objective
- Selected Dashboard hero geometry only; deferred Chat, Personality, guidance, and lower grid.

### 3. Plan Implementation
- Use read-only UX and QA lanes, then make a minimal desktop CSS patch.

### 4. Execute Implementation
- Restored a three-part hero composition on desktop, made metric tiles side satellites, enabled connector lines, and adjusted the portrait crop.

### 5. Verify and Test
- Validation passed as listed above.

### 6. Self-Review
- No new components, fake data, global shell changes, route changes, or backend behavior were introduced.

### 7. Update Documentation and Knowledge
- Task, active mission, task board, project state, requirements, quality/risk, module confidence, next steps, and design memory were updated.
