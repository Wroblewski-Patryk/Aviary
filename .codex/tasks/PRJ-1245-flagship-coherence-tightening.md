# Task

## Header
- ID: PRJ-1245
- Title: Flagship secondary chrome coherence tightening
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1244
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1245
- Quality Scenario Rows: QA-UX-1245
- Risk Rows: RISK-UI-1245
- Iteration: 1245
- Operation Mode: TESTER
- Mission ID: PRJ-1245-flagship-coherence-tightening
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
- Mission objective: make flagship UI feel more coherent by flattening secondary route-local micro-surfaces on Chat and Personality while leaving Dashboard untouched.
- Release objective advanced: v1.2 web UI canonical coherence across flagship screens.
- Included slices: Chat cognitive belt material, Chat belt meta/progress treatment, Personality overview status, Personality side-panel/signal-row material.
- Explicit exclusions: no Dashboard edits, no backend/API changes, no new data, no route behavior changes, no new components, no hiding supported controls.
- Checkpoint cadence: baseline screenshots, one CSS patch, three-route screenshot gate, full route smoke, navigation/account proof, state update.
- Stop conditions: contrast loss, Chat top belt becoming unreadable, Personality mobile status collision, route failure, or any horizontal overflow.
- Handoff expectation: next checkpoint should be a content/data decision or one exact screenshot mismatch, not another broad visual pass.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance | Validation gate | IN_PROGRESS |
| UX Parity | Raman subagent | Dashboard/Chat/Personality references | Read-only cross-surface audit | Smallest CSS-only checkpoint | Completed report | DONE |
| QA/Test | Dalton subagent | route-smoke scripts | Validation plan | Commands and responsive risks | Completed report | DONE |
| Frontend/UX | Active chat | screenshots, design memory | `web/src/index.css` | CSS-only secondary chrome pass | Fresh screenshots | IN_PROGRESS |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | PLANNED |

## Context
Dashboard, Chat, and Personality each have verified canonical fidelity slices. Fresh PRJ-1245 baseline screenshots show no route failures, but Chat and Personality still have more route-local status/card chrome than the canonical direction needs.

## Goal
Reduce secondary micro-surface weight so Chat and Personality feel closer to one calm product system while preserving all existing data, labels, controls, responsive behavior, navigation, and account access.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep the implementation CSS-only and route-local

## Definition of Done
- [x] CSS tightening pass is complete.
- [x] Build passes.
- [x] Dashboard/Chat/Personality desktop/tablet/mobile screenshot gate passes.
- [x] Full route smoke, navigation proof, and account proof pass.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- adding or hiding controls, fake data, unsupported cards, or product rename

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1245-flagship-coherence-tightening/screenshots --report .codex/artifacts/prj1245-flagship-coherence-tightening/report.json --screenshot-routes /dashboard,/chat,/personality --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `screenshot_count=9`, `failed_count=0`
  - `node scripts/route-smoke.mjs --report .codex/artifacts/prj1245-flagship-coherence-tightening/route-smoke-report.json` -> PASS, `route_count=14`, `status=ok`
  - `node scripts/route-smoke.mjs --navigation-proof --report .codex/artifacts/prj1245-flagship-coherence-tightening/navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1245-flagship-coherence-tightening/account-proof.json` -> PASS, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warning only
- Manual checks:
  - Compared fresh baseline and post-change desktop/mobile Chat and Personality screenshots.
  - Verified Chat top belt still carries readable context but no longer feels like six heavy mini-cards.
  - Verified Personality status, side panels, and rows are flatter while preserving values and mobile readability.
- Screenshots/logs:
  - `.codex/artifacts/prj1245-flagship-coherence-tightening/baseline/`
  - `.codex/artifacts/prj1245-flagship-coherence-tightening/screenshots/`
  - `.codex/artifacts/prj1245-flagship-coherence-tightening/report.json`
  - `.codex/artifacts/prj1245-flagship-coherence-tightening/route-smoke-report.json`
  - `.codex/artifacts/prj1245-flagship-coherence-tightening/navigation-proof.json`
  - `.codex/artifacts/prj1245-flagship-coherence-tightening/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot_set
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`, `docs/ux/assets/aion-chat-canonical-reference-v5.png`, `docs/ux/assets/aion-personality-canonical-reference-v1.png`
- Canonical visual target: calmer flagship secondary chrome
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Chat cognitive belt, Personality overview status, Personality side panels
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: not full pixel-perfect parity; Dashboard was intentionally not changed in this slice.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: Chat and Personality secondary chrome was flattened through a small CSS-only pass, while Dashboard was left untouched.
- Files changed:
  - `web/src/index.css`
- How tested:
  - build, nine-screenshot flagship gate, full route smoke, navigation proof, account proof, `git diff --check`, screenshot review.
- What is incomplete:
  - exact canonical copy/icon parity and Dashboard content changes remain out of scope.
- Decisions made:
  - do not continue broad visual flattening into Dashboard because its hero/metric composition is already the stronger canonical surface.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Fresh baseline showed the shared shell and flagship routes were stable, while Chat and Personality still had heavier secondary micro-surfaces than the canonical direction needs.

### 2. Select One Priority Mission Objective
- Selected a cross-flagship coherence tightening focused only on secondary chrome in Chat and Personality.

### 3. Plan Implementation
- Used Raman's read-only UX parity lane, Dalton's QA lane, and baseline screenshots. Kept Dashboard out of implementation scope.

### 4. Execute Implementation
- Flattened Chat cognitive belt cards/meta/progress and Personality overview status/side-panel row material.

### 5. Verify and Test
- Validation passed as listed above.

### 6. Self-Review
- No controls were hidden, no data changed, no new components were added, and Dashboard was not touched.

### 7. Update Documentation and Knowledge
- Task, active mission, task board, project state, requirements, quality/risk, module confidence, next steps, agent evals, system health, and design memory were updated.
