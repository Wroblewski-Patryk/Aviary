# Task

## Header
- ID: LUC-1205
- Title: [Aviary] [Known State Refresh] Evidence delta and next repair lanes
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Aviary Project Manager
- Depends on: LUC-1183
- Priority: P1
- Mission ID: LUC-1205-known-state-refresh-delta
- Mission Status: VERIFIED

## Context
Wake payload assigned `LUC-1205` and required concrete heartbeat action. Aviary remains in preparation mode, so this checkpoint must refresh known-state evidence and route next repair lanes without implementation work.

## Goal
Capture fresh evidence delta versus the previous known-state checkpoint and restate the next owner-scoped repair lanes.

## Constraints
- preparation-only scope for Aviary
- docs/state and read-only evidence collection only
- no implementation, deploy, restart, protected smoke, push, or production mutation

## Definition of Done
- [x] Fresh evidence snapshot collected.
- [x] Delta vs previous known-state checkpoint recorded.
- [x] Repair lanes restated with owners and proof expectations.
- [x] Source-of-truth routers synchronized.

## Forbidden
- broad implementation work
- deploy/push/restart/protected smoke/production mutation
- secret disclosure

## Validation Evidence
- `(Get-ChildItem backend/tests -Recurse -File | Measure-Object).Count` -> `125`
- `(Get-Content backend/app/api/routes.py | Select-String -Pattern "@router\.(get|post|put|delete|patch)\(").Count` -> `19`
- `(Get-ChildItem backend/migrations/versions -File | Measure-Object).Count` -> `12`
- `docs/graphs/architecture-health.json`:
  - `generated_at=2026-05-31T22:41:51.998Z`
  - `counts.entities=18649`
  - `counts.relations=30166`
  - `signals.implementation_without_tests.count=6528`
- `docs/graphs/architecture-proof-register.csv`:
  - line count `18650` (header + `18649` entities)
  - last write `2026-06-01 00:53:05`
- `docs/status/task-synchronization-report.md`:
  - tasks without architecture links `0`
  - implementation entities without task links `701`
  - verified entities without proof evidence `0`

## Result Report
- Task summary:
  - Refreshed the known-state evidence delta for `LUC-1205` and confirmed preparation posture remains unchanged.
  - No runtime/deploy mutation was performed.
  - Final issue disposition for this parent lane: `done` (follow-up specialist lanes `LUC-1205-A..D` remain separate delegated work).
- Files changed:
  - `.codex/tasks/LUC-1205-known-state-refresh-evidence-delta-and-next-repair-lanes.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/active-mission.md`
  - `.agents/state/next-steps.md`
- How tested:
  - Read-only evidence commands listed above.
- What is incomplete:
  - Specialist execution of repair lanes remains pending director routing/assignment.
- Next steps:
  - Route `LUC-1205-A..D` to owning specialists with the existing proof contracts.

## Evidence Delta vs LUC-1183

- Wake follow-up (2026-06-01):
  - `node scripts/build-architecture-awareness-index.mjs --project Aviary --root C:\Personal\Projekty\Aplikacje\Aviary`
    from `C:\Personal\Projekty\Aplikacje\Paperclip_Softwarehouse` hit timeout again after `1204s`.
  - Exporter reproducibility remains an active blocker for lane `LUC-1205-A`.
- Core local baseline remains stable:
  - backend tests `125`
  - route decorators `19`
  - migrations `12`
- Architecture artifact window remains fresh (same generated window on 2026-05-31, last writes on 2026-06-01).
- Open gap posture remains unchanged:
  - implementation entities without task links `701`
  - implementation/test proof-link clusters still concentrated around auth, chat/personality, and tools/integrations APIs.

## Next Repair Lanes

1. `LUC-1205-A` - Architecture exporter reproducibility guard
- Owner: Architecture Specialist
- Scope: reproduce exporter path with bounded runtime and deterministic invocation path for Aviary.
- Proof: successful exporter run, runtime evidence, fresh `docs/graphs/*` + `docs/status/*` timestamps.

2. `LUC-1205-B` - Auth and identity proof-link closure
- Owner: Backend Builder + QA/Test
- Scope: close proof-link/task-link cluster for `/app/auth/*`, `/app/me`, `/app/me/settings`.
- Proof: focused endpoint tests and reduced missing-link set for those endpoints.

3. `LUC-1205-C` - Chat and personality proof-link closure
- Owner: Backend Builder + QA/Test
- Scope: close proof-link/task-link cluster for `/app/chat/history`, `/app/chat/message`, `/app/personality/overview`.
- Proof: focused endpoint tests and reduced missing-link set for those endpoints.

4. `LUC-1205-D` - Tools and integrations proof-link closure
- Owner: Backend Builder + QA/Test
- Scope: close proof-link/task-link cluster for `/app/tools/overview`, `/app/tools/preferences`, `/app/tools/telegram/link/start`, `/app/connectors/confirm`.
- Proof: focused endpoint tests and reduced missing-link set for those endpoints.

## Heartbeat Recovery Checkpoint (2026-06-01)

- Wake reason handled: `source_scoped_recovery_action` for `LUC-1205`.
- Coordinator disposition sync: this parent lane remains `DONE`; no reopen.
- Why no reopen:
  - parent scope (known-state delta + delegated next lanes) is already completed and recorded
  - executable continuation exists only in delegated specialist lanes `LUC-1205-A..D`
- This heartbeat action:
  - revalidated local source-of-truth alignment (`TASK_BOARD`, `PROJECT_STATE`, `active-mission`, task packet)
  - preserved preparation-only boundary and no implementation/deploy mutation
- Final disposition for this heartbeat: `done`
