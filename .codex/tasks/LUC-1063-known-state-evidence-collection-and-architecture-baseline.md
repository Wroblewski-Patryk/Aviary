# Task

## Header
- ID: LUC-1063
- Title: [Aviary] [Known State] Evidence collection and architecture baseline
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Coordinator
- Priority: P1
- Mission ID: LUC-1063-known-state-baseline
- Mission Status: VERIFIED

## Context
Issue `LUC-1063` was assigned as a high-priority known-state and architecture-baseline heartbeat for Aviary preparation mode.

## Goal
Capture a fresh evidence-backed known-state snapshot so takeover and delegation lanes use current repository truth.

## Constraints
- preparation-only checkpoint; no runtime behavior changes
- no deploy/push/production mutation
- evidence must be reproducible from repository state

## Deliverable For This Stage
- refreshed known-state inventory for canonical docs/state and architecture exports
- minimal runtime surface counts (routes/tests/migrations)
- synchronized source-of-truth pointers

## Known-State Baseline (2026-05-31)

| Area | Status | Evidence |
| --- | --- | --- |
| Canonical state files | implemented and verified | `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.agents/state/active-mission.md`, `.agents/state/next-steps.md` |
| Prior baseline lineage | implemented and verified | `.codex/tasks/LUC-580-known-state-architecture-baseline.md`, `.codex/tasks/LUC-692-architecture-awareness-baseline-proof-and-drift-check.md`, `.codex/tasks/LUC-976-full-takeover-audit-and-operating-baseline.md` |
| Architecture export pack | implemented and verified | `docs/graphs/architecture-awareness.json`, `docs/graphs/architecture-awareness.csv`, `docs/graphs/architecture-graph.md`, `docs/graphs/architecture-graph.mmd`, `docs/graphs/function-journey-index.json`, `docs/graphs/user-action-index.json` |
| Backend route surface | implemented and verified | `backend/app/api/routes.py` (`19` route decorators) |
| Backend test surface | implemented and verified | `backend/tests` (`125` files) |
| Migration chain | implemented and verified | `backend/migrations/versions` (`12` files) |

## Evidence Collection Commands (This Heartbeat)

- `(Get-ChildItem backend/tests -Recurse -File | Measure-Object).Count` -> `125`
- `(Get-Content backend/app/api/routes.py | Select-String -Pattern "@router\.(get|post|put|delete|patch)\(").Count` -> `19`
- `(Get-ChildItem backend/migrations/versions -File | Measure-Object).Count` -> `12`
- `Get-ChildItem docs/graphs -File | Select-Object -ExpandProperty Name` -> canonical six-file architecture export pack present

## Validation Evidence
- Manual checks:
  - canonical state files are present and readable
  - architecture export pack is present in `docs/graphs`
  - route/test/migration surface counts were captured from repository state
- Tests: not applicable (verification-only documentation/state checkpoint)
- Reality status: verified

## Result Report
- Task summary:
  - completed `LUC-1063` known-state and architecture baseline checkpoint with refreshed evidence
  - captured baseline drift signal: backend test-file count is now `125` (previous known-state rows used `123`)
  - processed wake follow-up (`softwarehouse-known-state-wakeup:v1`) by converting refreshed evidence into child-lane-ready repair scope
- Files changed:
  - `.codex/tasks/LUC-1063-known-state-evidence-collection-and-architecture-baseline.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/active-mission.md`
  - `.agents/state/next-steps.md`
- What is incomplete:
  - no runtime/deploy smoke was run because this lane is preparation-mode known-state verification only

## Wake Follow-Up: Concrete Repair Lanes (2026-05-31)

### Additional evidence refresh

- `node scripts/build-architecture-awareness-index.mjs --project Aviary --root C:\Personal\Projekty\Aplikacje\Aviary` (run from `Paperclip_Softwarehouse`) -> regenerated `docs/graphs/*` and `docs/status/*` architecture outputs.
- `docs/status/architecture-awareness-report.md` regenerated at `2026-05-31T10:24:35.780Z`.
- Current architecture baseline signals:
  - entities: `18645`
  - relations: `30158`
  - implementation entities without inferred tests: `200` (top-list report signal)
  - implementation entities without inferred docs: `200` (top-list report signal)
  - ownerless entities: `0`
  - disconnected entities: `0`
- docs-tree footprint signal:
  - `docs/`: `5947` files
  - `Aviary - docs/`: `5644` files

### Child-lane-ready repair map

1. Lane A: docs-tree canonicalization and scanner override curation
   - owner: CTO Architect + Docs Memory Lead
   - scope: reduce architecture-noise from duplicate/low-signal document nodes
   - input: `docs/graphs/architecture-awareness.json`, `docs/status/architecture-awareness-report.md`, `docs/architecture/scanner-overrides.json`, `docs/`, `Aviary - docs/`
   - proof: regenerated report with explicit curation notes and reduced docs-noise signal

2. Lane B: backend endpoint verification closure for missing-link API surface
   - owner: Backend API Specialist + QA Automation Engineer
   - scope: highest-risk endpoints in `/app/auth/*`, `/app/me*`, `/app/chat/*`, `/health`, `/event*`, `/internal/state/inspect`
   - input: `backend/app/api/routes.py`, targeted tests under `backend/tests`
   - proof: targeted test command outputs + updated architecture-awareness linkage

3. Lane C: web/mobile component behavior verification closure
   - owner: Frontend Specialist + QA Automation Engineer
   - scope: core components listed in missing-link sets (`web/src/components/*`, `web/src/App.tsx`, `mobile/src/ui/*`)
   - input: current web/mobile UI components and existing smoke scripts
   - proof: focused behavior checks with artifact links + linkage reduction in architecture report

4. Lane D: architecture export reproducibility guard
   - owner: Architecture Specialist
   - scope: prove repeatability of architecture exports under active repo churn
   - input: architecture build script and generated outputs in `docs/graphs` and `docs/status`
   - proof: fresh rerun timestamp + drift note if counts/status differ

### Disposition

- This issue's preparation-scope deliverable is complete with updated known-state evidence and concrete delegated repair lanes.
- Final disposition for `LUC-1063`: `done`.
