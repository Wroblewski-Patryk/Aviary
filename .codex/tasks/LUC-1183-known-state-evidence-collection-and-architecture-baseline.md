# Task

## Header
- ID: LUC-1183
- Title: [Aviary] [Known State] Evidence collection and architecture baseline
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Planning Agent
- Depends on: LUC-1170
- Priority: P1
- Mission ID: LUC-1183-known-state-baseline-refresh
- Mission Status: VERIFIED

## Context
Board wake `softwarehouse-known-state-wakeup:v1` requested immediate local evidence collection and conversion into concrete next repair lanes, with strict preparation-mode boundaries.

## Goal
Refresh the local known-state evidence snapshot and produce owner-scoped repair lanes without implementation, deploy, restart, protected smoke, production mutation, or secret disclosure.

## Constraints
- preparation-only scope for Aviary
- docs/state and local evidence only
- no deploy/push/restart/protected smoke/production mutation

## Definition of Done
- [x] Fresh local evidence snapshot captured.
- [x] Current architecture baseline status captured from generated artifacts.
- [x] Findings converted into concrete owner-scoped repair lanes.
- [x] Source-of-truth routers synchronized.

## Forbidden
- implementation work outside PM preparation scope
- deploy, push, restart, protected smoke, production mutation
- secret disclosure

## Validation Evidence
- Local evidence refresh:
  - `(Get-ChildItem backend/tests -Recurse -File | Measure-Object).Count` -> `125`
  - `(Get-Content backend/app/api/routes.py | Select-String -Pattern "@router\.(get|post|put|delete|patch)\(").Count` -> `19`
  - `(Get-ChildItem backend/migrations/versions -File | Measure-Object).Count` -> `12`
- Architecture artifact freshness:
  - `docs/graphs/architecture-awareness.json` last write: `2026-05-31 23:51:24`
  - `docs/status/architecture-awareness-report.md` last write: `2026-05-31 23:53:55`
- Architecture report health snapshot (`docs/status/architecture-awareness-report.md`):
  - implementation entities without inferred tests: `200`
  - implementation entities without inferred docs: `200`
  - disconnected entities: `0`
  - owner attribution missing: `0`
- Reality status: verified

## Result Report
- Task summary:
  - Completed the requested local known-state evidence refresh and converted findings into concrete next repair lanes.
  - Preserved preparation-mode boundary: no runtime/deploy mutation.
- Files changed:
  - `.codex/tasks/LUC-1183-known-state-evidence-collection-and-architecture-baseline.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/active-mission.md`
- How tested:
  - local command evidence and architecture artifact timestamp/report inspection.
- What is incomplete:
  - specialist execution of repair lanes remains pending assignment.
- Next steps:
  - route `LUC-1183-A..D` to owning specialists for execution.

## LUC-1183 Repair Lanes

1. `LUC-1183-A` - Architecture exporter reproducibility guard
- Owner: Architecture Specialist
- Scope: reproduce and harden architecture export runtime so it completes reliably with bounded runtime evidence.
- Proof: successful exporter run, runtime evidence, fresh `docs/graphs/*` and `docs/status/*` timestamps.

2. `LUC-1183-B` - Auth and identity proof-link closure
- Owner: Backend Builder + QA/Test
- Scope: close missing proof-link cluster for `/app/auth/*`, `/app/me`, `/app/me/settings`.
- Proof: focused endpoint tests and architecture report delta for those endpoints.

3. `LUC-1183-C` - Chat and personality proof-link closure
- Owner: Backend Builder + QA/Test
- Scope: close proof-link cluster for `/app/chat/history`, `/app/chat/message`, `/app/personality/overview`.
- Proof: focused endpoint tests and architecture report delta for those endpoints.

4. `LUC-1183-D` - Tools and integrations proof-link closure
- Owner: Backend Builder + QA/Test
- Scope: close proof-link cluster for `/app/tools/overview`, `/app/tools/preferences`, `/app/tools/telegram/link/start`, `/app/connectors/confirm`.
- Proof: focused endpoint tests and architecture report delta for those endpoints.

## Heartbeat Checkpoint (2026-06-01)

- Wake comment triage:
  - Latest board comment (`0f644a8b-558b-462f-bbe4-96fb996ac305`) is bookkeeping-only (`in_progress` janitor sync) and does not change scope.
- Required exporter refresh:
  - Attempted from Aviary root: `node scripts/build-architecture-awareness-index.mjs --project Aviary --root C:\Personal\Projekty\Aplikacje\Aviary` -> failed (`MODULE_NOT_FOUND`, script absent in Aviary repo).
  - Attempted from Softwarehouse repo path:
    - `node scripts/build-architecture-awareness-index.mjs --project Aviary --root C:\Personal\Projekty\Aplikacje\Aviary`
    - run exceeded local heartbeat timeout twice (184s and 604s), so exporter reproducibility remains an open lane (`LUC-1183-A` / `LUC-1170-A` family).
- Fresh baseline evidence present in generated artifacts:
  - `docs/graphs/architecture-health.json`:
    - `generated_at: 2026-05-31T22:38:38.314Z`
    - `entities: 18649`
    - `relations: 30166`
    - `implementation_without_tests: 6528`
    - `missing_documentation: 0`
    - `missing_owner_attribution: 0`
    - `disconnected_entities: 0`
  - `docs/graphs/architecture-proof-register.csv`:
    - rows: `18649`
    - last write: `2026-06-01T00:47:42`
  - `docs/status/architecture-dependency-report.md`:
    - dependency relations: `26`
    - entities with dependencies: `6`
  - `docs/status/task-synchronization-report.md`:
    - tasks without architecture links: `0`
    - implementation entities without task links: `701`
    - verified entities without proof evidence: `0`
