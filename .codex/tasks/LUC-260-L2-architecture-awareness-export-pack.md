# Task

## Header
- ID: LUC-260-L2
- Title: [Personality] Architecture awareness export parity pack
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: CTO Architect
- Depends on: LUC-260
- Priority: P1
- Mission ID: LUC-260-takeover-baseline
- Mission Status: PLANNED

## Context
`LUC-260` flagged missing architecture-awareness export artifacts expected by the shared operating model.

## Goal
Restore architecture-awareness export parity for Personality takeover baseline.

## Constraints
- no broad architecture rewrites; baseline export parity only
- no runtime behavior changes
- consistency with canonical docs in `docs/architecture/`

## Deliverable For This Stage
- generate/restore:
  - `docs/graphs/architecture-awareness.json`
  - `docs/graphs/architecture-awareness.csv`
  - `docs/graphs/architecture-graph.md`
  - `docs/graphs/architecture-graph.mmd`
  - `docs/graphs/function-journey-index.json`
  - `docs/graphs/user-action-index.json`
  - `docs/status/architecture-awareness-report.md`

## Definition of Done
- [x] Export pack exists and is internally consistent.
- [x] Report includes coverage gaps/unknowns explicitly.
- [x] `LUC-260` packet receives source-linked parity evidence.

## Forbidden
- runtime/app feature implementation
- unrelated refactors
- paper-only claims without generated artifacts

## Result Report
- Task summary:
  - Restored the architecture-awareness export parity pack by generating all required `docs/graphs/*` artifacts from the canonical registry graph (`docs/architecture/graphs/architecture-graph.json`) and writing a status report with explicit missing-link unknowns.
- Files changed:
  - `backend/scripts/build_architecture_awareness_pack.py`
  - `docs/graphs/architecture-awareness.json`
  - `docs/graphs/architecture-awareness.csv`
  - `docs/graphs/architecture-graph.md`
  - `docs/graphs/architecture-graph.mmd`
  - `docs/graphs/function-journey-index.json`
  - `docs/graphs/user-action-index.json`
  - `docs/status/architecture-awareness-report.md`
- How tested:
  - `Push-Location backend; ..\.venv\Scripts\python scripts/build_architecture_awareness_pack.py; Pop-Location` -> PASS
  - Verified generated file presence and non-empty content for all required pack artifacts.
- What is incomplete:
  - `LUC-447` takeover proof-gate shortlist remains pending outside this lane.
- Next steps:
  - Fold this closure evidence into parent `LUC-260` and continue with `LUC-447`.
- Decisions made:
  - Used the canonical architecture graph as the single source for parity exports to avoid architecture drift between `docs/architecture/graphs` and compatibility exports under `docs/graphs`.
