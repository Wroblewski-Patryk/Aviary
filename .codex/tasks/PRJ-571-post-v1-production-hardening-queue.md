# Task

## Header
- ID: PRJ-571
- Title: Seed the next post-v1 production-hardening queue from live runtime gaps
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-570
- Priority: P1

## Context
No seeded execution queue remained after the no-UI `v1` closure lane. The
production repair for `PRJ-570` restored Telegram round-trip behavior, but live
`/health` and startup logs still show the next operational gaps clearly:

- reflection external-driver posture remains `in_process` compatibility
- scheduler cadence ownership remains `in_process`
- both surfaces already exist, so the next queue should reduce production drift
  instead of inventing a new capability lane

## Goal
Seed the next smallest architecture-aligned execution queue from those live
production gaps and make the new priority visible in canonical planning truth.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] canonical planning surfaces describe one explicit post-`v1`
  production-hardening lane
- [x] the next queue is ordered from the live production/runtime gaps revealed
  by `/health` and startup logs
- [x] the first new task is marked as the next `READY` slice in planning truth

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - not applicable; planning/context only
- Manual checks:
  - cross-review of live production `/health`
  - cross-review of production startup logs after `PRJ-570`
- Screenshots/logs:
  - production reported `reflection_external_driver_policy.production_baseline_ready=false`
  - production reported `external_scheduler_policy.production_baseline_ready=false`
- High-risk checks:
  - queue only reuses existing architecture lanes and health surfaces

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - planning-only

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This queue deliberately starts with production externalization rather than new
user-facing capability growth because the live runtime already exposes the
target owner surfaces and the remaining drift is operational, not conceptual.
