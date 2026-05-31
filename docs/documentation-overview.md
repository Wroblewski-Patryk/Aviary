# Documentation Overview

Updated: 2026-05-31

This file is the docs-parity baseline entry for the Aviary repository. It
provides one stable index for current documentation ownership,
scope, and residual gaps during the `LUC-976` takeover preparation mission.

## Project Scope And Status

- Canonical project root: `C:/Personal/Projekty/Aplikacje/Aviary`
- Canonical project alias: `Aviary`
- Legacy alias: `Personality` (allowed only when historical evidence requires it)
- Duplicate docs surface: `Aviary - docs/` inside the repo is a non-canonical
  copied vault. Treat it as archival reference only; current-truth updates must
  land under canonical `docs/`.
- Current takeover parent: `LUC-976` (`IN_PROGRESS`, pending parent integration)
- Current docs-memory lane: `LUC-994` (`DONE`)
- This file is the canonical docs-memory snapshot used by the `LUC-976-L5`
  documentation status and root-index refresh lane.

## Canonical Documentation Entrypoints

| Area | Primary source |
| --- | --- |
| Documentation index and route map | `docs/documentation-map.md` |
| Runtime and product reality snapshot | `docs/overview.md` |
| Full docs catalog and layering model | `docs/README.md` |
| Canonical architecture authority | `docs/architecture/` |
| Active planning and open decisions | `docs/planning/` |
| Operations and release runbooks | `docs/operations/` |
| Coordinator state and execution memory | `.codex/context/`, `.agents/state/` |

## Residual Unknowns And Open Parity Gaps

- `LUC-990`, `LUC-991`, `LUC-992`, `LUC-993`, and `LUC-994` child lanes are
  closed with task packets under `.codex/tasks/`.
- parent `LUC-976` remains open until all child-lane outputs are integrated
  into one final closure packet.
