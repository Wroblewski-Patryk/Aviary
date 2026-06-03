# Task

## Header
- ID: LUC-1170-D
- Title: [Aviary] Tools and integrations proof-link closure
- Task Type: verification
- Current Stage: planning
- Status: READY
- Owner: Backend Builder
- Depends on: LUC-1170
- Priority: P1
- Mission ID: LUC-1170-known-state-refresh-closure
- Mission Status: CHECKPOINTED

## Context
Architecture-awareness report shows proof-link gaps for tools/integrations endpoints that are user-facing and release-relevant.

## Goal
Close proof-link coverage for tools/integrations endpoint contracts and test visibility.

## Scope
- `/app/tools/overview`, `/app/tools/preferences`
- `/app/tools/telegram/link/start`, `/app/connectors/confirm`
- `backend/tests/*` focused tests
- architecture report and graph outputs

## Implementation Plan
1. Verify current missing-link rows for targeted endpoints.
2. Add/refresh focused tests for tools/integrations endpoints.
3. Refresh architecture-awareness export.
4. Capture missing-link delta and residual exceptions.
5. Sync task/state evidence.

## Acceptance Criteria
- Focused tools/integrations endpoint tests pass.
- Reported missing-link footprint for scoped endpoints is reduced or justified.
- Evidence and residual risks are documented.

## Definition of Done
- [ ] Focused test evidence exists for scoped endpoints.
- [ ] Architecture report delta is captured.
- [ ] Residual gap owner/action is explicit.

## Validation Evidence
- Tests: focused route pack for tools/integrations
- Manual checks: architecture report delta review
- Screenshots/logs: command outputs and report excerpts
- Reality status: implemented, not verified

## Result Report
- Task summary: pending specialist execution
- Files changed: none in this packet
- How tested: none yet
- What is incomplete: implementation and verification
- Next steps: backend + QA execution lane
