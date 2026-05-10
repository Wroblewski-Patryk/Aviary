# Module Confidence Ledger

Last updated: 2026-05-11

## Project Alias

The product name is Aviary. The repository folder is `Personality`.

## Purpose

This ledger is the quick reality map for Aviary. It tracks whether each
important runtime, memory, reflection, scheduler, action, integration, API, web,
mobile, and operations journey is implemented, verified, broken, blocked, or
unknown. Keep it honest. Do not turn uncertainty into optimism.

## Status Vocabulary

- `NOT_STARTED`: no meaningful implementation exists.
- `IN_PROGRESS`: implementation is actively changing.
- `IMPLEMENTED_NOT_VERIFIED`: code exists, but current proof is missing.
- `PARTIAL`: some scenarios pass, but important scenarios are missing or stale.
- `VERIFIED`: current evidence proves the journey for the target scope.
- `BROKEN`: a reproducible defect exists.
- `BLOCKED`: verification or implementation is blocked by access, decision,
  environment, dependency, or missing input.
- `DEFERRED`: explicitly out of the current release scope.

## Confidence Rules

- `High`: fresh reproducible evidence exists for the real journey.
- `Medium`: good local proof exists, but target, edge-case, or freshness is
  incomplete.
- `Low`: evidence is missing, stale, inferred, or chat-only.

## Ledger

| ID | Module | Journey / function | Priority | Status | Confidence | Evidence | Missing proof or defect | Next smallest action | Owner | Last verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AVIARY-STATUS-001 | Project status radar | Generated project status dashboard and architecture implementation map | P0 | PARTIAL | Medium | `docs/operations/project-status-dashboard.md`, `docs/operations/project-status-dashboard.json`, `docs/operations/architecture-implementation-map-2026-05-10.csv`, and `PROJECT_STATE.md` entries from 2026-05-10/2026-05-11. | Dashboard exists, but module confidence rows are not yet mirrored here by runtime journey. | Convert current dashboard/audit rows into module-confidence rows for runtime, connectors, web UX, deploy automation, test evidence, and mobile scope. | Planning + QA/Test | 2026-05-11 |
| AVIARY-BLOCKER-001 | External providers | Provider credential activation smoke for connector readiness | P0 | BLOCKED | Medium | `PROJECT_STATE.md` identifies `ARCH-CONNECTORS-001` as top blocker. | External credentials/input needed for target provider activation proof. | Keep blocked state explicit; when credentials exist, run provider activation smoke and update dashboard plus this ledger. | Ops/Release + QA/Test | 2026-05-11 |

## Maintenance Rules

- Update this file when a feature ships, a bug is fixed, a regression appears,
  architecture changes, validation proves a journey, or a module is deferred.
- Prefer verification missions before fix missions when the only problem is
  missing evidence.
- Mark a journey `VERIFIED` only when evidence is current and reproducible.
- Mark a journey `BROKEN` when a real user journey fails, even if related tests
  pass.
- Link evidence to test names, commands, screenshots, smoke notes, commits, or
  task IDs. Chat-only evidence is not enough.
