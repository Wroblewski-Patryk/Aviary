# Task

## Header
- ID: PRJ-1324
- Title: Mystic clean UI orchestration wave 1
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1323
- Priority: P1
- Requirement Rows: REQ-UX-1324
- Quality Scenario Rows: QA-UX-1324
- Risk Rows: RISK-UI-1324
- Iteration: 1324
- Operation Mode: BUILDER
- Mission ID: PRJ-1324-mystic-clean-ui-orchestration-wave-1
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: lift authenticated shell visual quality to a cleaner mystical premium baseline without changing feature behavior.
- Release objective advanced: flagship web UX polish and trust perception.
- Included slices: shell chrome and chat surface visual simplification, hierarchy cleanup, and calmer material treatment.
- Explicit exclusions: route logic, backend/API, data contracts, copy semantics, auth flow behavior, and deployment scripts.
- Checkpoint cadence: one scoped CSS checkpoint per cycle with proof.
- Stop conditions: any required JSX redesign or behavior change beyond CSS-only polish.
- Handoff expectation: verified first wave with evidence and next wave recommendation.

## Context
The user requested coordinated UI improvement toward a mystical, clean, beautiful experience. Current UI is functional and evidence-backed, but still contains visual weight and local clutter in authenticated shell/chrome areas.

## Goal
Deliver the first visible quality jump in shell and chat chrome while preserving information architecture and interaction behavior.

## Scope
- `web/src/index.css`
- route surfaces: authenticated shell, route switcher, sidebar nav, chat topbar/transcript cards

## Implementation Plan
1. Refine shell/chrome materials to be calmer and less noisy.
2. Improve route-switcher and sidebar visual hierarchy while keeping controls intact.
3. Polish chat topbar/transcript message surfaces for readability and visual rhythm.
4. Run build and route smoke validation.
5. Record mission/state updates and define the next UI checkpoint.

## Acceptance Criteria
- Authenticated shell reads cleaner and more premium without losing navigation clarity.
- Chat surface is calmer and easier to scan.
- No route behavior or backend data path changes.
- Frontend build and route smoke remain green.

## Definition of Done
- [x] CSS-only UI checkpoint implemented.
- [x] `npm run build` passes.
- [x] `npm run smoke:routes` passes.
- [x] State/task artifacts updated with proof.

## Validation Evidence
- Tests: `npm run build`; `npm run smoke:routes`.
- Manual checks: route smoke confirms no overlay, no horizontal overflow, no unnamed interactive controls across 14 routes.
- Screenshots/logs: route smoke JSON output in terminal (`status: ok`, `route_count: 14`).
- High-risk checks: no API/backend/data/route behavior changes; CSS-only patch.
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/visual-direction-brief.md`, `docs/ux/anti-patterns.md`
- Canonical visual target: calmer authenticated shell and chat chrome
- Fidelity target: style_inspired
- Existing shared pattern reused: yes (`aion-*` shell and chat classes)
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Responsive checks: desktop | tablet | mobile (via route smoke guards)

## Result Report
- Task summary: first wave polish reduced visual heaviness in shell navigation and chat surfaces, improving calmness and hierarchy without behavior drift.
- Files changed: `web/src/index.css`, `.codex/tasks/PRJ-1324-mystic-clean-ui-orchestration-wave-1.md`, `.agents/state/active-mission.md`, `.codex/context/TASK_BOARD.md`.
- What is incomplete: this is wave 1; deeper route-level parity passes (dashboard/personality/chat micro-composition) remain for next checkpoints.
- Next steps: run wave 2 focused on Dashboard + Personality decorative discipline and spacing consistency.

## Notes
- Design direction source: `docs/ux/visual-direction-brief.md`, `docs/ux/anti-patterns.md`, `docs/ux/experience-quality-bar.md`.
- This is wave 1 of a larger coordinated UX cleanup program.
