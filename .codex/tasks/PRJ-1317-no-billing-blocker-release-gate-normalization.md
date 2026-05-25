# Task

## Header
- ID: PRJ-1317
- Title: No-billing-blocker release gate normalization
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1316
- Priority: P0
- Mission ID: PRJ-1317-no-billing-blocker-release-gate-normalization
- Mission Status: VERIFIED

## Goal
Ensure GitHub Actions billing state cannot block release readiness for this project.

## Definition of Done
- [x] hosted proof checklist explicitly marked optional
- [x] next steps prioritize local/Coolify required gates
- [x] decision register records no-billing-blocker policy as durable decision

## Validation Evidence
- updated:
  - `docs/operations/architecture-graph-hosted-proof-checklist.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/decision-register.md` (`DEC-005`)
  - `.agents/state/active-mission.md`
