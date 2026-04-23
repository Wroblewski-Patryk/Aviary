# Task

## Header
- ID: PRJ-583
- Title: Sync docs/context for proactive production baseline
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-582
- Priority: P1

## Context
After the production proactive cutover and new evidence gates, canonical docs
and repository truth needed one final sync so operators and future execution
lanes see the same baseline.

## Goal
Align runtime reality, testing guidance, ops notes, planning surfaces, and
context truth around the live bounded proactive production baseline.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] runtime reality describes the live proactive production baseline and proof surfaces
- [x] testing guidance lists the proactive regression and evidence commands
- [x] task board, project state, and planning truth move the queue to `PRJ-584`

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` -> passed
- Manual checks:
  - production `/health.proactive.enabled=true`
  - production `/health.proactive.production_baseline_state=external_scheduler_target_owner`
- Screenshots/logs:
  - live health snapshot from 2026-04-23 after Coolify redeploy
- High-risk checks:
  - docs no longer describe proactive as disabled-by-policy in production

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/17_logging_and_debugging.md`
  - `docs/architecture/29_runtime_behavior_testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - runtime/ops/testing/planning sync only

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This sync also records the recurring deployment pitfall where a Coolify env
override can silently mask the repo-driven proactive baseline.
