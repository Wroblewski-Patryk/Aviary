# Task

## Header
- ID: LUC-976
- Title: [Aviary] Full takeover audit and operating baseline
- Task Type: research
- Current Stage: verification
- Status: IN_PROGRESS
- Owner: Planner
- Depends on: none
- Priority: P0
- Mission ID: LUC-976-takeover-baseline-refresh
- Mission Status: CHECKPOINTED

## Context
Issue `LUC-976` was assigned as the active critical heartbeat scope. Role constraints for Aviary Project Manager allow preparation-only execution: scan, baseline, gap map, and handoff planning.

## Goal
Refresh the takeover operating baseline so the board has one current, evidence-backed view of Aviary readiness and the next delegated lanes.

## Constraints
- preparation-only lane; no broad implementation
- no deploy, push, production mutation, or credential mutation
- unknowns must stay explicit
- state must be durable in repo source-of-truth files

## Deliverable For This Stage
- refreshed known-state snapshot
- refreshed takeover gap register
- explicit next delegated lanes and proof contracts

## Acceptance Criteria
- baseline includes product/docs/runtime/tests/ops-readiness signals with source paths
- each major area has evidence-backed status wording
- unresolved gaps are translated into bounded next lanes (owner + proof)
- source-of-truth sync is completed in the same heartbeat

## Known-State Snapshot (2026-05-31)

| Area | Status | Evidence |
| --- | --- | --- |
| Canonical context files (`PROJECT_STATE`, `TASK_BOARD`, `LEARNING_JOURNAL`) | implemented and verified | `.codex/context/PROJECT_STATE.md`, `.codex/context/TASK_BOARD.md`, `.codex/context/LEARNING_JOURNAL.md` |
| Active mission router | implemented and verified | `.agents/state/active-mission.md` |
| Next-steps backlog router | implemented and verified | `.agents/state/next-steps.md` |
| Backend API route baseline | implemented and verified | `backend/app/api/routes.py` route decorators count `19` |
| Backend test inventory baseline | implemented and verified | `backend/tests/` file count `123` |
| Architecture awareness export pack presence | implemented and verified | `docs/graphs/architecture-awareness.json`, `docs/graphs/architecture-awareness.csv`, `docs/graphs/architecture-graph.md`, `docs/graphs/architecture-graph.mmd`, `docs/graphs/function-journey-index.json`, `docs/graphs/user-action-index.json` |

## Takeover Gap Register

| Gap ID | Severity | Gap | Status | Next owner | Proof required |
| --- | --- | --- | --- | --- | --- |
| LUC976-G1 | P0 | No dedicated `LUC-976` takeover packet existed in repo memory | implemented and verified | Aviary PM | task packet + context sync |
| LUC976-G2 | P1 | Legacy `LUC-260` takeover baseline is stale against latest issue lineage | implemented but not verified | Aviary PM | explicit supersession note + state links |
| LUC976-G3 | P1 | Deferred specialist prep lanes still not activated as fresh child issues under `LUC-976` | present in code, behavior unknown | 11 Innovations Director / Delivery | child issues with owner/scope/proof |
| LUC976-G4 | P1 | Ops readiness doc parity includes template-like residuals in archival docs area | present in code, behavior unknown | Ops/Release lane | bounded docs parity closure note |

## Specialist Lanes For Activation

| Lane | Scope | Expected output |
| --- | --- | --- |
| Product Docs | refresh canonical docs parity baseline for current issue lineage | one docs parity packet linked to `LUC-976` |
| Architecture | re-verify architecture-awareness exports and drift classification | fresh architecture parity note and drift posture |
| QA/Test | re-state minimal takeover proof gate for current baseline | replayable command shortlist and evidence contract |
| Ops/Release | confirm readiness/rollback/smoke entrypoints for preparation mode | concise ops baseline note and residual risk list |

## Delegated Child Issues (2026-05-31)

- `LUC-990` - `[Aviary] LUC-976-L1 Architecture graph and traceability audit`
- `LUC-991` - `[Aviary] LUC-976-L2 Product and capability roadmap audit`
- `LUC-992` - `[Aviary] LUC-976-L3 Runtime smoke and regression evidence baseline`
- `LUC-993` - `[Aviary] LUC-976-L4 Ops and release readiness baseline`
- `LUC-994` - `[Aviary] LUC-976-L5 Documentation status and root-index refresh`

## Validation Evidence
- Command evidence:
  - `(Get-ChildItem backend\\tests -File -Recurse).Count` -> `123`
  - `(Get-Content backend\\app\\api\\routes.py | Select-String -Pattern "@router\\.(get|post|put|delete|patch)\\(").Count` -> `19`
- Runtime tests: not run (docs/state-only checkpoint).
- Reality status: partially verified.

## Result Report
- Completed:
  - created `LUC-976` takeover task contract and evidence snapshot
  - synced takeover checkpoint into source-of-truth context files
  - clarified next delegated specialist lanes for activation phase
  - created delegated child issues `LUC-990` to `LUC-994` as bounded one-owner lanes
- Remaining:
  - run and close child lanes `LUC-990` to `LUC-994`, then integrate evidence into parent closure packet
  - reconcile/supersede `LUC-260` references where they are still the active pointer
