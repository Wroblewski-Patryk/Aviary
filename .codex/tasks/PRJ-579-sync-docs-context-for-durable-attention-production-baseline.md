# Task

## Header
- ID: PRJ-579
- Title: Sync docs/context for durable-attention production baseline
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-578
- Priority: P1

## Context
Production durable attention is already live after `PRJ-577`, and `PRJ-578`
added release-smoke, incident-evidence, and behavior-validation proof for that
baseline. Canonical docs and repository context must now describe the same
production truth instead of leaving durable attention split between older
rollout wording and the new evidence surfaces.

## Goal
Synchronize architecture, runtime reality, testing guidance, ops notes, and
context truth around the live durable-attention production baseline and its
proof path.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] Canonical docs describe durable attention as the live production owner baseline.
- [x] Docs record the same proof path across `/health`, exported incident evidence, release smoke, and behavior validation.
- [x] Task board and project state both move `PRJ-579` to `DONE` and advance the next `READY` task.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'`
- Manual checks: doc/runtime/ops cross-review against live production `/health`
- Screenshots/logs: n/a
- High-risk checks: ensure docs point to the existing live proof surfaces and do not invent stricter public-health fields than production currently exposes

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/17_logging_and_debugging.md`, `docs/architecture/29_runtime_behavior_testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: n/a
- Follow-up architecture doc updates: durable-attention live production baseline and proof surfaces synced across architecture/runtime/ops/testing docs

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
This slice is docs/context only. No learning-journal update was needed because
the durable-attention proof path itself was already established in `PRJ-578`.
