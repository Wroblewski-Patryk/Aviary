# Task

## Header
- ID: LUC-260-L4
- Title: [Personality] Ops/release takeover readiness baseline
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: LUC-260
- Priority: P1
- Mission ID: LUC-260-takeover-baseline
- Mission Status: PLANNED

## Context
`LUC-260` requires an explicit operator-level release baseline note before closure.

## Goal
Confirm deploy/readiness/rollback posture for takeover packet without triggering live deployment.

## Constraints
- no live deploy trigger unless explicitly requested
- static/runbook consistency first
- risks must be explicit

## Deliverable For This Stage
- ops/release addendum in `LUC-260` packet covering:
  - canonical deploy entrypoint(s)
  - required smoke proof path
  - rollback reference path
  - current risk posture

## Definition of Done
- [x] Runbook and state files are cross-checked and consistent.
- [x] Readiness note names residual blockers/risk.
- [x] Parent `LUC-260` includes this lane evidence.

## Forbidden
- production mutations
- secret exposure
- broad infra redesign

## Result Report
- Task summary:
  - Built takeover-safe Ops/Release baseline note from canonical runbooks and gate docs, without triggering deployment.
  - Confirmed canonical deploy/readiness entrypoints:
    - release gate policy: `DEPLOYMENT_GATE.md`
    - operator runbook: `Aviary - docs/operations/runtime-ops-runbook.md`
    - release proof scripts:
      - `backend/scripts/run_unified_release_readiness_gate.ps1`
      - `backend/scripts/run_production_release_proof_cycle.ps1`
      - `backend/scripts/run_release_smoke.ps1`
  - Confirmed rollback and recovery reference path:
    - `Aviary - docs/operations/rollback-and-recovery.md`
    - Coolify incident fallback section in runtime ops runbook (`Coolify 503 Recovery Notes`).
  - Established current risk posture:
    - `implemented but not verified`: static environment matrix is still template-like in `Aviary - docs/operations/environment-matrix.md` (`Last updated: YYYY-MM-DD` and empty local/stage/production rows).
    - `present in code, behavior unknown`: stage-specific readiness evidence is not explicitly materialized for this takeover packet.
    - `implemented and verified`: production host baseline and same-origin deployment model are explicitly documented in runbook (`https://aviary.luckysparrow.ch`, `/app`, `/health`, `/event`).
- Files changed:
  - `.codex/tasks/LUC-260-L4-ops-release-baseline-readiness-note.md`
- How tested:
  - Documentation cross-check only (no runtime mutation):
    - `Get-Content -Raw DEPLOYMENT_GATE.md`
    - `Get-Content -Raw "Aviary - docs/operations/runtime-ops-runbook.md"`
    - `Get-Content -Raw "Aviary - docs/operations/environment-matrix.md"`
  - No deploy, restart, migration, or secret operations were performed.
- What is incomplete:
  - Environment matrix is not yet populated with concrete stage/prod owner and evidence rows.
  - This lane does not include fresh live smoke evidence capture; it defines the canonical proof path only.
- Next steps:
  - Product Docs/Architecture lanes should close file-parity blockers (`LUC-445`, `LUC-446`).
  - QA lane should attach minimum takeover proof execution contract (`LUC-447`) using the above ops baseline entrypoints.
- Decisions made:
  - No production mutation is allowed in this lane; ops baseline remains documentation-first.
  - Rollback and smoke authority is anchored to existing runbook + gate artifacts, not ad-hoc commands.
