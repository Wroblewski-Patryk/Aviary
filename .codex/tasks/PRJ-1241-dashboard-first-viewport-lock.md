# Task

## Header
- ID: PRJ-1241
- Title: Dashboard first viewport canonical lock
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1240
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1241
- Quality Scenario Rows: QA-UX-1241
- Risk Rows: RISK-UI-1241
- Iteration: 1241
- Operation Mode: BUILDER
- Mission ID: PRJ-1241-dashboard-first-viewport-lock
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
- Mission objective: lock the Dashboard first viewport closer to the canonical reference without adding controls, cards, fake data, or new product behavior.
- Release objective advanced: v1.2 web UI canonical fidelity for the future mobile-app foundation.
- Included slices: Dashboard desktop first-viewport hierarchy, hero/guidance/flow density, responsive proof.
- Explicit exclusions: no backend/API changes, no new routes, no product rename, no new dashboard data, no new shared shell work.
- Checkpoint cadence: one Dashboard patch, screenshot gate, visual review, state update.
- Stop conditions: horizontal overflow, clipped first-viewport text, route failure, shell regression, or any change that makes Dashboard noisier.
- Handoff expectation: next checkpoint should continue from screenshot-specific drift, not broad restyling.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Parfit subagent | Dashboard canonical reference | Read-only Dashboard parity audit | Top drift list | Completed report | DONE |
| Frontend/UX | Active chat | UX audit, design memory | `web/src/index.css`, Dashboard route | Minimal visual patch | Fresh screenshots | DONE |
| QA/Test | Aristotle subagent | route-smoke scripts | Validation plan | Commands and regression risks | Completed report | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

### Lane Checks

- [x] `.agents/state/active-mission.md` was refreshed for broad work.
- [x] Every important responsibility has an owner or explicit omission.
- [x] Delegated lanes are read-only and do not overlap write scope.
- [x] Each delegated lane has expected output and proof.

## Context
PRJ-1240 made Dashboard, Chat, and Personality more coherent, but Dashboard still reads more like a card dashboard than the canonical first viewport. The next user nudge asked the coordinator team to continue until the UX/UI is beautiful and coherent.

## Goal
Make the Dashboard first viewport calmer, more canonical, and more visually led by the central embodied hero while preserving real backend-backed data and existing navigation behavior.

## Success Signal
- User or operator problem: Dashboard still has too much card/control noise.
- Expected product or reliability outcome: Dashboard first viewport reads as one coherent Aviary cockpit rather than competing modules.
- How success will be observed: rendered desktop/tablet/mobile screenshots and route/navigation/account proof.
- Post-launch learning needed: yes

## Deliverable For This Stage
Implementation patch plus validation evidence for the Dashboard route.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep Dashboard as the only edited route surface

## Definition of Done
- [x] Dashboard first viewport patch is complete.
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
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1241-dashboard-first-viewport/screenshots --report .codex/artifacts/prj1241-dashboard-first-viewport/report.json --screenshot-routes /dashboard --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `screenshot_count=3`, `failed_count=0`
  - `node scripts/route-smoke.mjs --report .codex/artifacts/prj1241-dashboard-first-viewport/route-smoke-report.json` -> PASS, `route_count=14`, `status=ok`
  - `npm run audit:ui-navigation` -> PASS, `step_count=4`, `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1241-dashboard-first-viewport/account-proof.json` -> PASS, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warning only
- Manual checks:
  - Compared `docs/ux/assets/aion-dashboard-canonical-reference-v2.png` with the latest desktop Dashboard screenshot.
  - Verified the central hero reads stronger than the lower card band, the right guidance rail is quieter, cognitive flow is lighter, and the lower Reflection card no longer shows a clipped row.
- Screenshots/logs:
  - `.codex/artifacts/prj1241-dashboard-first-viewport/screenshots/`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/report.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/route-smoke-report.json`
  - `.codex/artifacts/prj1241-dashboard-first-viewport/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target: Dashboard first viewport
- Fidelity target: structurally_faithful
- Existing shared pattern reused: flagship scenic surface, soft panel material, cognitive flow bridge
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: this is a verified first-viewport lock, not a full pixel-perfect 95% claim; the remaining drift is exact portrait/metric connector geometry versus the static canonical image.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: Dashboard first viewport was tuned toward the canonical reference with a route-local CSS patch.
- Files changed:
  - `web/src/index.css`
- How tested:
  - build, Dashboard screenshot gate, full route smoke, navigation proof, account proof, `git diff --check`, screenshot review.
- What is incomplete:
  - exact pixel parity is not claimed; remaining work should focus on hero connector geometry or continue to Chat/Personality only as separate checkpoint slices.
- Decisions made:
  - keep Aviary branding and existing backend-backed data; do not add new Dashboard cards or controls.

## Autonomous Loop Evidence

### 1. Analyze Current State
- PRJ-1240 improved flagship coherence, but Dashboard still read too much like a card grid and less like the canonical embodied cockpit.

### 2. Select One Priority Mission Objective
- Selected Dashboard first viewport lock as the only surface for this checkpoint.

### 3. Plan Implementation
- Use subagent read-only UX and QA lanes, then make a route-local CSS patch.

### 4. Execute Implementation
- Strengthened the desktop hero, narrowed/softened metric overlays, made the guidance rail lighter, softened the cognitive flow bridge, and prevented a clipped Reflection row.

### 5. Verify and Test
- Validation passed as listed above.

### 6. Self-Review
- No new components, fake data, global shell changes, or backend behavior were introduced.

### 7. Update Documentation and Knowledge
- Task, active mission, task board, project state, requirements, quality/risk, module confidence, next steps, and design memory were updated.
