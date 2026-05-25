# Task

## Header
- ID: PRJ-1327
- Title: Mystic clean UI orchestration wave 4
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1326
- Priority: P1
- Requirement Rows: REQ-UX-1327
- Quality Scenario Rows: QA-UX-1327
- Risk Rows: RISK-UI-1327
- Iteration: 1327
- Operation Mode: BUILDER
- Mission ID: PRJ-1324-mystic-clean-ui-orchestration-wave-1
- Mission Status: CHECKPOINTED

## Context
The previous waves improved shell, chat, dashboard, and personality. Remaining refinement is focused on dashboard decorative weight and component calmness.

## Goal
Finalize a cleaner premium finish by softening remaining heavy dashboard accents without changing behavior.

## Scope
- `web/src/index.css`
- surfaces: dashboard cards, flow panel, focus orb, action controls

## Definition of Done
- [x] CSS-only visual pass landed.
- [x] `npm run build` passes.
- [x] `npm run smoke:routes` passes.
- [x] Task/state updated with evidence.

## Validation Evidence
- Tests: `npm run build`; `npm run smoke:routes`.
- Manual checks: route markers present on all 14 routes, no framework overlay, no horizontal overflow, no unnamed interactive controls.
- Reality status: verified

## Result Report
- Task summary: softened remaining heavy dashboard accents (flow panels/cards/orb/actions) and improved interaction polish while preserving behavior.
- Files changed: `web/src/index.css`, `.codex/tasks/PRJ-1327-mystic-clean-ui-orchestration-wave-4.md`.
- What is incomplete: one final wave remains for high-fidelity screenshot parity capture and sign-off.
