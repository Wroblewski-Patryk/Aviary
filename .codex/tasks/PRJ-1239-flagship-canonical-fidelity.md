# Task

## Header
- ID: PRJ-1239
- Title: Flagship canonical fidelity pass
- Task Type: design
- Current Stage: verification
- Status: REVIEW
- Owner: Frontend Builder
- Depends on: PRJ-1238
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: web.flagship.chat, web.flagship.personality, web.flagship.dashboard
- Requirement Rows: REQ-UI-FLAGSHIP-CANONICAL-FIDELITY
- Quality Scenario Rows: QA-UX-FLAGSHIP-PARITY
- Risk Rows: RISK-UI-CANONICAL-DRIFT
- Iteration: 1239
- Operation Mode: ARCHITECT
- Mission ID: PRJ-1239-flagship-canonical-fidelity
- Mission Status: VERIFIED_CHECKPOINT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed in prior v1.2 startup and canonical docs were refreshed for this checkpoint.
- [x] `.agents/core/mission-control.md` was reviewed in prior v1.2 startup and active mission is being refreshed.
- [x] Missing or template-like state tables were not blocking this UI slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: make Dashboard, Chat, and Personality converge toward their canonical visual references instead of remaining style-inspired variants.
- Release objective advanced: v1.2 web UI canonical fidelity.
- Included slices: compare canonical/current screenshots, close Chat first as the clearest full-screen target, then use evidence to choose Personality and Dashboard follow-up patches.
- Explicit exclusions: global product rename from Aviary to AION/Prometheus, backend/API changes, fake data or non-backed controls.
- Checkpoint cadence: one flagship surface per checkpoint with screenshots and validation.
- Stop conditions: stop if canonical reference conflicts with product branding, if route behavior regresses, or if screenshot proof cannot be captured.
- Handoff expectation: leave a gap table, implementation evidence, screenshot paths, and next surface target.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS.md, canonical UX docs | Integration, task closure, state updates | Parent decision and final acceptance | Build, route smoke, screenshots | REVIEW |
| UX Parity Audit | Subagent Confucius | `docs/ux/canonical-web-screen-reference-set.md` | Dashboard, Chat, Personality references | Gap table and priority order | Read-only report | DONE |
| Implementation Mapping | Subagent Aquinas | web source and CSS | Route layout ownership map | Smallest safe patch recommendation | Read-only report | DONE |
| Frontend/UX | Active chat | canonical screenshot set | `web/src/App.tsx`, `web/src/index.css`, route components as needed | Flagship frame/proportion patch | Screenshot comparison | DONE |
| QA/Test | Active chat | route smoke scripts | web validation | Responsive proof | Build and screenshot gate | DONE |
| Docs/State | Active chat | task/state docs | `.agents/state/*`, `.codex/context/*`, `docs/ux/design-memory.md` | Durable checkpoint memory | Updated files | DONE |

### Lane Checks

- [x] `.agents/state/active-mission.md` was created or refreshed for broad work.
- [x] `.agents/workflows/responsibility-lanes.md` was reviewed in the v1.2 coordinator flow.
- [x] Every important responsibility has an owner or explicit omission.
- [x] No delegated write lanes overlap.
- [x] Each delegated lane has expected output and proof.
- [x] Missing ownership/evidence/context gaps will be recorded if found.
- [x] Process eval will be recorded because this is broad and subagent-heavy work.

## Context
The user reported that Dashboard, Chat, and Personality still look like different views with similar styling rather than convergent canonical implementations. The approved canonical references live in `docs/ux/assets/` and `docs/ux/canonical-web-screen-reference-set.md`.

## Goal
Close the largest fidelity gaps by making each flagship route follow its canonical layout hierarchy, starting with Chat because it has the clearest full-screen target and the smallest safe route-local patch.

## Success Signal
- User or operator problem: flagship views do not match the planned visual language closely enough to serve as web and mobile app foundations.
- Expected product or reliability outcome: Chat, then Personality and Dashboard, become screenshot-comparable to canonical references with fewer unrelated cards and duplicate headers.
- How success will be observed: fresh desktop/tablet/mobile screenshots and route smoke show the route is structurally closer to the canonical target.
- Post-launch learning needed: yes

## Deliverable For This Stage
Implement and verify the first flagship frame/proportion correction across Chat, Personality, and Dashboard. Record remaining exact-parity gaps as next checkpoints.

## Constraints
- use existing systems and approved mechanisms
- do not introduce fake browser chrome, fake controls, or unsupported backend data
- do not change product branding from Aviary without explicit decision
- close one surface at a time

## Definition of Done
- [x] Chat desktop no longer has extra desktop utility chrome above the canonical conversation stage.
- [x] Chat body preserves the canonical top belt plus 60/40 transcript/persona split.
- [x] Dashboard and Personality no longer carry the extra desktop utility header above the route scene.
- [x] Route smoke/build/screenshot validation passes.
- [x] State and design memory record the evidence and remaining mismatches.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests: `npm run build`; focused route-smoke screenshot gate for `/dashboard`, `/chat`, `/personality`; `npm run audit:ui-navigation`; route-smoke account proof.
- Manual checks: desktop Dashboard, Chat, and Personality screenshots compared against canonical references after implementation.
- Screenshots/logs: `.codex/artifacts/prj1239-flagship-canonical-fidelity/screenshots/`; `.codex/artifacts/prj1239-flagship-canonical-fidelity/report.json`; `.codex/artifacts/prj1239-flagship-canonical-fidelity/account-proof.json`.
- Reality status: partially verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v5.png`, `docs/ux/assets/aion-personality-canonical-reference-v1.png`, `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target: Chat first, then Personality and Dashboard
- Fidelity target: structurally_faithful
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: authenticated shell and route components
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact 95% parity still needs card-proportion and copy-density tuning; branding remains Aviary pending product decision.
- Responsive checks: desktop | tablet | mobile

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
