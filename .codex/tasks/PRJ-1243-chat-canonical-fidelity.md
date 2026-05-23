# Task

## Header
- ID: PRJ-1243
- Title: Chat canonical fidelity pass
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1240, PRJ-1242
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1243
- Quality Scenario Rows: QA-UX-1243
- Risk Rows: RISK-UI-1243
- Iteration: 1243
- Operation Mode: BUILDER
- Mission ID: PRJ-1243-chat-canonical-fidelity
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
- Mission objective: move Chat closer to `aion-chat-canonical-reference-v5.png` by reducing visible control noise and making the conversation/persona split feel calmer and more canonical.
- Release objective advanced: v1.2 web UI canonical fidelity for Chat.
- Included slices: Chat-only CSS for route-posture suppression, desktop split proportions, transcript/composer calm, assistant ordered-list treatment, solo quick-action suppression, and desktop portrait-overlay cleanup.
- Explicit exclusions: no global shell work, no Dashboard/Personality work, no backend/API changes, no new data, no branding rename, no new component family.
- Checkpoint cadence: one focused patch, Chat desktop/tablet/mobile screenshot gate, full route smoke, navigation/account proof, state update.
- Stop conditions: overflow, clipped transcript/composer, route failure, account/navigation regression, or adding unsupported controls.
- Handoff expectation: next checkpoint should remain a single-surface slice, likely Personality canonical fidelity or a Chat content/icon decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | User-supplied read-only lane brief | Chat canonical reference v5, PRJ-1240 screenshot | Read-only drift list | Top visual differences and safe selectors | Integrated into implementation scope | DONE |
| Frontend/UX | Active chat | UX audit, design memory | `web/src/index.css` | Chat-only CSS fidelity patch | Fresh screenshots | DONE |
| QA/Test | Active chat | route-smoke scripts | Validation gate | Build, smoke, screenshots, nav/account | PASS reports | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
PRJ-1240 made Chat more coherent, while PRJ-1241 and PRJ-1242 closed Dashboard-specific drift. The next best single-surface slice is Chat canonical fidelity because the current render still had extra route-status pills, a heavy solo quick-action chip, a card-like ordered list, and a desktop portrait label stack that competed with the persona image.

## Goal
Make Chat v5 feel simpler and more faithful to the canonical conversation/persona composition while preserving real data-backed content, responsive behavior, navigation, and account access.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep the implementation Chat-only and presentation-focused

## Definition of Done
- [x] Chat removes nonessential visible status/control noise from the first read.
- [x] Desktop Chat split is closer to the canonical conversation/persona balance.
- [x] Transcript and composer rhythm is calmer and less visually chunky.
- [x] Assistant ordered lists render as one calm plan surface instead of stacked heavy cards.
- [x] Build passes.
- [x] Chat desktop/tablet/mobile screenshot gate passes.
- [x] Full route smoke, navigation proof, and account proof pass.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- adding unsupported controls, cards, badges, fake data, or a product rename

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1243-chat-canonical-fidelity/screenshots --report .codex/artifacts/prj1243-chat-canonical-fidelity/report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `screenshot_count=3`, `failed_count=0`
  - `node scripts/route-smoke.mjs --report .codex/artifacts/prj1243-chat-canonical-fidelity/route-smoke-report.json` -> PASS, `route_count=14`, `status=ok`
  - `node scripts/route-smoke.mjs --navigation-proof --report .codex/artifacts/prj1243-chat-canonical-fidelity/navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1243-chat-canonical-fidelity/account-proof.json` -> PASS, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warning only
- Manual checks:
  - Compared `docs/ux/assets/aion-chat-canonical-reference-v5.png` with the latest desktop, tablet, and mobile Chat screenshots.
  - Verified route-status pills and the solo quick-action chip no longer add first-read noise, transcript/composer spacing is calmer, the assistant plan reads as one continuous surface, and the desktop portrait panel no longer has the extra embodied-cognition chip competing with the planning overlay.
- Screenshots/logs:
  - `.codex/artifacts/prj1243-chat-canonical-fidelity/screenshots/`
  - `.codex/artifacts/prj1243-chat-canonical-fidelity/report.json`
  - `.codex/artifacts/prj1243-chat-canonical-fidelity/route-smoke-report.json`
  - `.codex/artifacts/prj1243-chat-canonical-fidelity/navigation-proof.json`
  - `.codex/artifacts/prj1243-chat-canonical-fidelity/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v5.png`
- Canonical visual target: Chat conversation/persona first viewport
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Chat workspace, cognitive belt, transcript shell, composer shell, persona stage overlay notes
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: not full pixel-perfect parity; the route-smoke proof still uses a long test transcript, and exact canonical icon glyph/content parity would require a separate content decision.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: Chat was simplified and aligned closer to canonical v5 through a small CSS-only pass that also calms the transcript and composer.
- Files changed:
  - `web/src/index.css`
- How tested:
  - build, Chat screenshot gate, full route smoke, navigation proof, account proof, `git diff --check`, screenshot review.
- What is incomplete:
  - exact pixel parity and replacement of backend-backed/test transcript content were intentionally not included.
- Decisions made:
  - keep this route-local and presentation-only; hide nonessential route-status pills and solo quick-action chrome because they add noise without changing backend-supported behavior.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Current Chat was structurally close but had visible first-read noise: route-status pills, solo quick action, heavy plan-card list, and an extra portrait chip competing with persona overlays.

### 2. Select One Priority Mission Objective
- Selected Chat canonical fidelity only; deferred Personality and additional Dashboard/content work.

### 3. Plan Implementation
- Use the user-supplied read-only UX parity brief, inspect canonical/current screenshots, and patch only existing Chat CSS.

### 4. Execute Implementation
- Suppressed route-posture pills, widened the desktop persona side, reduced transcript/composer visual weight, converted assistant ordered lists into a single calm plan surface, hid solo quick-action chips, and removed the desktop portrait copy/chip from the canonical Chat composition.

### 5. Verify and Test
- Validation passed as listed above.

### 6. Self-Review
- No new components, fake data, global shell changes, route changes, or backend behavior were introduced.

### 7. Update Documentation and Knowledge
- Task, active mission, task board, project state, requirements, quality/risk, module confidence, next steps, and design memory were updated.
