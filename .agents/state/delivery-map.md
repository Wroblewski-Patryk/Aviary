# Delivery Map

Last updated: 2026-05-11

## Project Alias

The product name is Aviary. The repository folder is `Personality`.

## Current Product Target

- Product: Aviary
- Current release or milestone: architecture evidence hardening with external blocker
- Primary user: Aviary operator/user
- Primary outcome: Runtime, memory, reflection, scheduler, connector, API, web, and ops journeys work with proof.
- Top blockers: `ARCH-CONNECTORS-001` provider credential activation smoke is externally blocked.
- Next mission: Convert project-status-dashboard and architecture implementation map rows into module/journey delivery rows.

## Source Inputs

| ID | Type | Source | What it defines | Status |
| --- | --- | --- | --- | --- |
| SRC-001 | dashboard | `docs/operations/project-status-dashboard.md` | Current readiness radar | active |
| SRC-002 | architecture map | `docs/operations/architecture-implementation-map-2026-05-10.csv` | Architecture implementation/evidence rows | active |
| SRC-003 | architecture | `docs/architecture/` | Runtime, memory, action, logging, behavior contracts | active |

## Module / Journey Map

| ID | Module | Journey or screen | Layers needed | Current state | Evidence | Next mission |
| --- | --- | --- | --- | --- | --- | --- |
| AVIARY-DM-001 | Project status radar | Generated dashboard and architecture map | scripts, docs, evidence | partial | `project-status-dashboard.md`, `module-confidence-ledger.md` | Mirror dashboard rows into delivery/module confidence rows. |
| AVIARY-DM-002 | External providers | Provider activation smoke | integrations, secrets, ops, tests | blocked | `ARCH-CONNECTORS-001` | Run smoke when credentials are available. |

## Visual Slice Map

| ID | Reference | Screen / zone | Components | States | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| AVIARY-VIS-001 | TBD | Web shell/dashboard/chat | TBD | loading, empty, error, success, blocked | planned | none |
