# Task

## Header
- ID: PRJ-1248
- Title: Dashboard mobile cognitive-flow rail compression
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1246
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1248
- Quality Scenario Rows: QA-UX-1248
- Risk Rows: RISK-UI-1248
- Iteration: 1248
- Operation Mode: BUILDER
- Mission ID: PRJ-1248-dashboard-mobile-flow-rail
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
- Mission objective: make mobile Dashboard's cognitive-flow band read as a compact bridge instead of a tall stack of flow cards.
- Release objective advanced: v1.2 web mobile Dashboard canonical usability.
- Included slices: mobile-only Dashboard cognitive-flow track and current-phase density.
- Explicit exclusions: no desktop/tablet changes, no backend/API changes, no copy/data/icon changes, no route behavior changes, no shared shell changes, no Chat/Personality changes.
- Checkpoint cadence: one CSS patch, Dashboard screenshot gate, full route smoke, navigation/account proof, state update.
- Stop conditions: document-level horizontal overflow, clipped flow labels, hidden supported flow steps, Dashboard hero regression, route failure, or account/navigation regression.
- Handoff expectation: next checkpoint should be another single route/screenshot mismatch or a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance integrated | Validation gate passed | DONE |
| UX Parity | Erdos subagent | Dashboard mobile screenshot/reference | Read-only mobile Dashboard audit | Scope and risks | Report integrated | DONE |
| QA/Test | James subagent | route-smoke scripts | Validation plan | Commands and risks | Report integrated | DONE |
| Frontend/UX | Active chat | screenshots, design memory | `web/src/index.css` | CSS-only mobile Dashboard pass | Fresh screenshots passed | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
PRJ-1246 fixed mobile Chat's first-read compression. Fresh mobile Dashboard screenshots show the cognitive-flow band still stacks six steps vertically before the lower dashboard data, making the route feel report-like rather than like the canonical diagrammatic bridge.

## Goal
Preserve all flow steps while showing them as a compact horizontal rail on narrow screens, so Active Goals and the lower dashboard data appear sooner.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep the implementation CSS-only and mobile Dashboard-specific

## Definition of Done
- [x] Mobile Dashboard cognitive-flow steps are compressed without hiding supported steps.
- [x] Build passes.
- [x] Dashboard desktop/tablet/mobile screenshot gate passes.
- [x] Full route smoke, navigation proof, and account proof pass.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- adding or hiding controls, fake data, unsupported steps, or product rename

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots --report .codex/artifacts/prj1248-dashboard-mobile-flow-rail/report.json --screenshot-routes /dashboard --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `screenshot_count=3`, `failed_count=0`
  - `node scripts/route-smoke.mjs --report .codex/artifacts/prj1248-dashboard-mobile-flow-rail/route-smoke-report.json` -> PASS, `route_count=14`, `status=ok`
  - `node scripts/route-smoke.mjs --navigation-proof --report .codex/artifacts/prj1248-dashboard-mobile-flow-rail/navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1248-dashboard-mobile-flow-rail/account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warning only
- Manual checks:
  - Reviewed mobile Dashboard screenshot and confirmed the cognitive-flow band now reads as a compact horizontal rail with a next-step peek and lower dashboard data appearing sooner.
  - Cleanup checks found no validation-owned route-smoke, headless browser, or 5173/4173 listener leftovers.
- Screenshots/logs:
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots/mobile-dashboard.png`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots/tablet-dashboard.png`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/screenshots/desktop-dashboard.png`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/report.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/route-smoke-report.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/navigation-proof.json`
  - `.codex/artifacts/prj1248-dashboard-mobile-flow-rail/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Canonical visual target: mobile Dashboard cognitive flow as compact diagrammatic bridge
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Dashboard cognitive flow, flow steps, current phase
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical copy/icon/content parity remains a separate content/data decision
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof
