# Documentation Overview

Updated: 2026-05-29

This file is the docs-parity baseline entry for the Personality (Aviary)
repository. It provides one stable index for current documentation ownership,
scope, and residual gaps during the `LUC-260` takeover preparation mission.

## Project Scope And Status

- Project alias: `Aviary` (repository folder name remains `Personality`)
- Current takeover parent: `LUC-260` (`IN_PROGRESS`, blocked by child lanes)
- This file closes docs parity artifact gap `LUC260-G2` only for the
  `docs/documentation-overview.md` requirement.

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

- `LUC-446`, `LUC-447`, and `LUC-448` baseline lanes are now closed and their
  artifacts are present.
- `LUC-580` baseline refresh is closed with known-state evidence.
- `LUC-694` synchronized docs-memory ledgers to keep baseline references
  aligned across `.codex/context/*` and `.agents/state/*`.
