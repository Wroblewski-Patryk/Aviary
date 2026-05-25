# Task

## Header
- ID: PRJ-1325
- Title: Mystic clean UI orchestration wave 2
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1324
- Priority: P1
- Requirement Rows: REQ-UX-1325
- Quality Scenario Rows: QA-UX-1325
- Risk Rows: RISK-UI-1325
- Iteration: 1325
- Operation Mode: TESTER
- Mission ID: PRJ-1324-mystic-clean-ui-orchestration-wave-1
- Mission Status: CHECKPOINTED

## Context
Wave 1 improved shell/chat chrome. Next user-facing polish slice targets Dashboard and Personality visual hierarchy, keeping behavior and data flow unchanged.

## Goal
Make Dashboard + Personality feel cleaner, calmer, and more premium with restrained decorative treatment.

## Scope
- `web/src/index.css`
- surfaces: dashboard stage/hero cards and personality hero/callouts/timeline wrapper

## Definition of Done
- [x] CSS-only visual pass landed.
- [x] `npm run build` passes.
- [x] `npm run smoke:routes` passes.
- [x] Task/state updated with verification evidence.

## Validation Evidence
- Tests: `npm run build`; `npm run smoke:routes`.
- Manual checks: route smoke confirms marker presence, no framework overlay, no horizontal overflow, and unnamed interactive count `0` for all routes.
- Reality status: verified

## Result Report
- Task summary: dashboard/personality visual hierarchy is cleaner with reduced ornamental weight, calmer shadows, tighter card rhythm, and softer connector emphasis.
- Files changed: `web/src/index.css`, `.codex/tasks/PRJ-1325-mystic-clean-ui-orchestration-wave-2.md`.
- What is incomplete: Wave 3 remains for fine typography rhythm and mobile polish in flagship surfaces.
