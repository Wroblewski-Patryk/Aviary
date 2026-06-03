# Task

## Header
- ID: LUC-1170-C
- Title: [Aviary] Chat and personality flow proof-link closure
- Task Type: verification
- Current Stage: planning
- Status: READY
- Owner: Backend Builder
- Depends on: LUC-1170
- Priority: P1
- Mission ID: LUC-1170-known-state-refresh-closure
- Mission Status: CHECKPOINTED

## Context
Known-state report still marks chat/personality endpoints as missing link coverage even with prior partial verification evidence.

## Goal
Close proof-link gaps for core chat and personality overview endpoints with focused regression evidence.

## Scope
- `/app/chat/history`, `/app/chat/message`, `/app/personality/overview`
- `backend/tests/*` focused route-level verification
- `docs/status/architecture-awareness-report.md` and graph exports

## Implementation Plan
1. Confirm current missing-link rows for chat/personality endpoints.
2. Add/refresh focused tests for chat and personality routes.
3. Rebuild architecture-awareness outputs.
4. Capture before/after delta and classify any remaining gap.
5. Sync task/state routers.

## Acceptance Criteria
- Focused chat/personality test pack passes.
- Missing-link delta is reduced or explicitly justified.
- Evidence is durable in task and context files.

## Definition of Done
- [ ] Endpoint test evidence is attached.
- [ ] Report delta for missing links is attached.
- [ ] Follow-up risk/owner is explicit for unresolved items.

## Validation Evidence
- Tests: focused route pack for chat + personality
- Manual checks: architecture report delta review
- Screenshots/logs: command outputs and report excerpts
- Reality status: implemented, not verified

## Result Report
- Task summary: pending specialist execution
- Files changed: none in this packet
- How tested: none yet
- What is incomplete: implementation and verification
- Next steps: backend + QA execution lane
