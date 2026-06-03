# Task

## Header
- ID: LUC-1170-A
- Title: [Aviary] Architecture exporter timeout triage and reproducibility guard
- Task Type: fix
- Current Stage: planning
- Status: READY
- Owner: Architecture Specialist
- Depends on: LUC-1170
- Priority: P1
- Mission ID: LUC-1170-known-state-refresh-closure
- Mission Status: CHECKPOINTED

## Context
Known-state refresh found repeated timeout when running architecture-awareness indexing from the Paperclip toolchain context.

## Goal
Restore bounded, reproducible completion of `build-architecture-awareness-index` for Aviary and refresh timestamped graph outputs.

## Scope
- `C:/Personal/Projekty/Aplikacje/Paperclip_Softwarehouse/scripts/build-architecture-awareness-index.mjs`
- `docs/graphs/*`
- `docs/status/architecture-awareness-report.md`

## Implementation Plan
1. Reproduce timeout with bounded execution and capture timing/log evidence.
2. Identify the slow/non-terminating stage in script flow.
3. Apply minimal fix or guard (timeout handling, scope pruning, or scanner-bound correction).
4. Re-run export and capture runtime/exit-code proof.
5. Record before/after evidence and update state routers.

## Acceptance Criteria
- Architecture index command exits `0` within a bounded timeout window.
- Fresh graph/report artifacts are generated with current timestamps.
- Any residual risk is explicit with owner/action.

## Definition of Done
- [ ] Timeout root cause is documented with evidence.
- [ ] Reproducibility guard or fix is implemented.
- [ ] Export/report rerun is proven and linked in task/state files.

## Validation Evidence
- Tests: bounded command rerun
- Manual checks: artifact timestamp and report diff review
- Screenshots/logs: command output with duration and exit code
- Reality status: blocked

## Result Report
- Task summary: pending specialist execution
- Files changed: none in this packet
- How tested: none yet
- What is incomplete: full lane execution
- Next steps: specialist implements and verifies
