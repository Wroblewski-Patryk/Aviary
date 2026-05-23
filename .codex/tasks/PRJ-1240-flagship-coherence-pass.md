# Task

## Header
- ID: PRJ-1240
- Title: Flagship coherence pass for Dashboard, Chat, and Personality
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1239, REQ-UX-1240
- Quality Scenario Rows: QAS-UX-1240
- Risk Rows: RISK-UX-1240
- Iteration: 1240
- Operation Mode: TESTER
- Mission ID: PRJ-1240-flagship-coherence-pass
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
- Mission objective: continue the v1.2 flagship UI convergence loop with the smallest low-risk patch that improves coherence across Dashboard, Chat, and Personality.
- Release objective advanced: web UI canonical fidelity for the future mobile-app foundation.
- Included slices: CSS-only proportions, crop, and visual hierarchy refinements for three flagship surfaces.
- Explicit exclusions: no new components, no fake data, no backend/API changes, no product rename from Aviary to AION/Prometheus.
- Checkpoint cadence: one CSS patch, screenshot gate, visual review, state update.
- Stop conditions: screenshot audit failure, visible regression, route overflow, or product-copy/branding conflict.
- Handoff expectation: next task should continue from evidence-backed screenshot drift, not broad restyling.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Bounded coherence pass | Parent validation gate | DONE |
| Frontend/UX | Coordinator, serial lane | Canonical Dashboard/Chat/Personality refs | `web/src/index.css` | CSS-only polish | Fresh screenshots | DONE |
| QA/Test | Coordinator | route-smoke and navigation/account scripts | Web route proof | Build, smoke, screenshot, nav/account | PASS reports | DONE |
| Documentation/Memory | Coordinator | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

### Lane Checks

- [x] Subagent delegation was considered; no spawn-agent tool was available in this runtime, so the lane model was run serially.
- [x] Every important responsibility has an owner or explicit omission.
- [x] No delegated write lanes overlap.
- [x] Missing ownership/runtime tooling gap recorded in responsibility learning.

## Context
PRJ-1239 removed the largest frame mismatch from Dashboard, Chat, and Personality, but the user correctly asked to keep coordinating until the UI is genuinely beautiful and coherent. The next useful slice was not a rewrite; it was a small shared proportion pass.

## Goal
Improve visual coherence across the three flagship authenticated routes while moving them closer to canonical references and preserving all route, navigation, account, and responsive proof.

## Scope
- `web/src/index.css`
- Routes: `/dashboard`, `/chat`, `/personality`
- Artifacts: `.codex/artifacts/prj1240-flagship-coherence-pass/`

## Implementation Plan
1. Compare PRJ-1239 screenshots against canonical Dashboard, Chat, and Personality assets.
2. Patch only CSS for scene scale, overlay weight, card density, and persona-stage hierarchy.
3. Run build and focused route screenshot gate.
4. Run navigation and account proof.
5. Review rendered screenshots and update durable state.

## Acceptance Criteria
- Dashboard central hero has stronger first-read authority and quieter metric overlays.
- Chat persona-stage overlays are less dominant while preserving the canonical 60/40 conversation/persona split.
- Personality callouts and side panels are calmer without losing the embodied map structure.
- No route failure, framework overlay, unnamed interactive controls, or document-level horizontal overflow.

## Definition of Done
- [x] CSS-only implementation is complete.
- [x] Build passes.
- [x] Focused Dashboard/Chat/Personality desktop/tablet/mobile screenshot gate passes.
- [x] Navigation proof passes.
- [x] Account proof passes.
- [x] Browser/IAB path was attempted and closed; route-smoke remains the authenticated rendered proof.
- [x] Project state and confidence ledgers are updated.

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1240-flagship-coherence-pass/screenshots --report .codex/artifacts/prj1240-flagship-coherence-pass/report.json --screenshot-routes /dashboard,/chat,/personality --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS
  - `npm run audit:ui-navigation` -> PASS
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1240-flagship-coherence-pass/account-proof.json` -> PASS
  - `git diff --check` -> PASS with LF/CRLF warning only
- Screenshots/logs:
  - `.codex/artifacts/prj1240-flagship-coherence-pass/screenshots/`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/report.json`
  - `.codex/artifacts/prj1240-flagship-coherence-pass/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Canonical visual target:
  - `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
  - `docs/ux/assets/aion-chat-canonical-reference-v5.png`
  - `docs/ux/assets/aion-personality-canonical-reference-v1.png`
- Fidelity target: structurally_faithful
- Existing shared pattern reused: flagship scenic surface, soft panel material, persona-stage overlays
- New shared pattern introduced: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact pixel parity is not claimed; future work should continue from screenshot-specific Dashboard density and Chat/Personality asset/copy differences.
- Responsive checks: desktop, tablet, mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Review Checklist
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Relevant validations were run.
- [x] Docs/context were updated.

## Result Report
- Task summary: CSS-only flagship coherence pass completed for Dashboard, Chat, and Personality.
- Files changed:
  - `web/src/index.css`
- How tested:
  - build, focused screenshot gate, navigation proof, account proof, cleanup check.
- What is incomplete:
  - no 95% pixel parity claim; next work should tune specific screenshot mismatches.
- Next steps:
  - continue Dashboard exact card/copy-density parity or Chat transcript/persona asset fidelity as separate narrow slices.
- Decisions made:
  - preserve Aviary branding; canonical AION/Prometheus labels are not treated as rename approval.

## Autonomous Loop Evidence

### 1. Analyze Current State
- PRJ-1239 had removed the extra header, but screenshots still showed visual density drift and overlay-card imbalance.

### 2. Select One Priority Mission Objective
- Selected task: one small flagship coherence CSS pass.

### 3. Plan Implementation
- Modify only existing selectors in `web/src/index.css`; avoid new JSX/components.

### 4. Execute Implementation
- Tuned Dashboard hero height/metric overlay weight, Chat persona overlay scale, and Personality callout/panel density.

### 5. Verify and Test
- Validation passed as listed above.

### 6. Self-Review
- A personality crop attempt made the figure read as a narrow poster, so it was corrected before closure.

### 7. Update Documentation and Knowledge
- Task, active mission, task board, project state, requirements, quality/risk, module confidence, next steps, responsibility learning, and agent eval were updated.
