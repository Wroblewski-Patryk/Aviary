# Documentation Drift Report

Last updated: 2026-05-03

This report records documentation drift found during PRJ-937. It is intended to
make missing links visible, not to claim full closure.

## Confirmed Drift Or Cleanup

| Finding | Evidence | Impact | Status |
| --- | --- | --- | --- |
| Missing engineering entrypoint requested by user | `docs/index.md` did not exist before PRJ-937 | New agents had to infer entry order from `docs/README.md` and AGENTS rules | Fixed by PRJ-937 |
| No documentation inventory | No `docs/analysis/documentation-inventory.md` existed | Existing docs could not be audited as a system | Fixed by PRJ-937 foundation |
| No codebase map | No `docs/architecture/codebase-map.md` existed | Module/route/model ownership was scattered across code and docs | Fixed by PRJ-937 foundation |
| No traceability matrix | No `docs/architecture/traceability-matrix.md` existed | Feature-to-code/test/docs paths were implicit | Fixed by PRJ-937 foundation |
| No pipeline registry | No `docs/pipelines/index.md` existed | Runtime and product flows lacked one registry | Fixed by PRJ-937 foundation |
| No module registry | No `docs/modules/index.md` existed | Module responsibilities and dependencies were implicit | Fixed by PRJ-937 foundation |
| No docs contribution rules | No `docs/CONTRIBUTING-DOCS.md` existed | Future feature/module/route/model changes could skip map updates | Fixed by PRJ-937 foundation |
| Repeated heading noise in docs README | `docs/README.md` contained repeated `Governance Addendum` headings | Low readability issue at documentation entrypoint | Fixed by PRJ-937 |
| Missing dedicated API reference | No `docs/api/index.md` existed before PRJ-938 | Endpoint purpose, auth posture, schemas, side effects, callers, and tests were scattered | Fixed by PRJ-938 foundation |
| Missing dedicated data/model reference | No `docs/data/index.md` existed before PRJ-939 | Persistent-state ownership across models, migrations, repository methods, features, and tests was scattered | Fixed by PRJ-939 foundation |
| Foreground runtime only existed as registry entry | `docs/pipelines/index.md` summarized the central runtime pipeline, but no dedicated pipeline doc existed | Stage order, data dependencies, side effects, failure points, and tests were too compressed | Fixed by PRJ-940 foundation |
| App chat only existed as registry entry | The browser chat flow had no dedicated doc for optimistic UI, backend runtime handoff, durable transcript projection, and reconciliation | Product-critical chat behavior could drift between frontend local state and backend transcript truth | Fixed by PRJ-941 foundation |
| Deferred reflection only existed as registry entry | The background queue/signal writer path lacked a dedicated doc | Durable conclusions, relations, proposals, theta, progress, and milestones could drift without one queue/data/test map | Fixed by PRJ-942 foundation |
| Scheduler/proactive only existed as registry entry | Cadence ownership, due planned work, observer admission, proactive ticks, and evidence writes lacked one dedicated doc | Background wakeup behavior could drift across scheduler, proactive, planned-work, health, and ops paths | Fixed by PRJ-943 foundation |
| Tools/connectors only existed as registry entry | Tool readiness, preference writes, Telegram link-code start, connector execution baseline, and permission gates lacked one dedicated doc | Provider readiness, user preference, and backend-owned authorization boundaries could drift | Fixed by PRJ-944 foundation |
| Missing generated OpenAPI artifact | No generated schema was checked in before PRJ-946 | API route/schema drift could not be compared against FastAPI output | Fixed by PRJ-946 foundation |
| Missing ERD and column model reference | Data docs listed tables but had no generated ERD or column-by-column reference before PRJ-947 | Persistent state shape required manual inspection of ORM models | Fixed by PRJ-947 foundation |
| Tests lacked stable feature/pipeline ownership IDs | Traceability mapped tests by filename and inspected responsibility only | Coverage could not be checked mechanically against feature/pipeline ownership | Fixed at file level by PRJ-948 foundation |
| Frontend route/component ownership was too coarse | Codebase map only said most frontend ownership lived in `web/src/App.tsx` | Route data dependencies and fallback/static surfaces were hard to trace | Fixed at route/helper level by PRJ-949 foundation |
| Provider-specific integration docs were incomplete | Tools docs named connector readiness but did not map providers, settings, live operations, policy-only operations, tests, and gaps in one place | Provider readiness could be confused with connector authorization capability | Fixed by PRJ-950 foundation |

## Code Without Dedicated Documentation

| Code Area | Current Coverage | Gap |
| --- | --- | --- |
| `backend/app/api/routes.py` | Codebase map, traceability matrix, API reference, and generated OpenAPI artifact | Per-route examples are still missing |
| `backend/app/api/schemas.py` | API reference lists schemas and fields; OpenAPI exports generated schema shapes | Deep schema examples and generated client sync are still missing |
| `backend/app/memory/models.py` | Codebase map, data reference, generated column reference, and Mermaid ERD | Exhaustive repository-method reference is still missing |
| `backend/app/core/*_policy.py` | Module registry groups policies | Dedicated policy registry is missing |
| `backend/app/core/runtime_graph.py` | Pipeline registry covers foreground runtime | Per-node graph state input/output documentation is missing |
| `backend/app/reflection/*.py` | Pipeline and module registry cover reflection | Per-signal extraction docs are missing |
| `backend/app/integrations/**` | Traceability, tools pipeline, and provider integration reference cover major integrations, readiness, permission boundaries, tests, and gaps | Provider-specific request/response examples and live smoke evidence remain incomplete |
| `web/src/App.tsx` | Codebase map and frontend route/component map cover route shell, state owners, API calls, helper clusters, and gaps | Component extraction ownership remains mostly monolithic |
| `web/src/lib/api.ts` | Codebase map covers app API client | OpenAPI/type-generation sync is missing |

## Documentation That May Describe Historical State

| Docs | Reason | Handling Rule |
| --- | --- | --- |
| Many `docs/planning/*.md` files | They are task plans and evidence across many completed iterations | Treat as historical unless referenced by current task board, project state, or docs index |
| Older numbered architecture docs | The repository explicitly states `02`, `15`, and `16` are canonical when conflicts appear | Compare before relying on older claims |
| Operator command examples | Script ownership moved to `backend/scripts` in prior work | Prefer current ops/testing docs and verify script paths before copying |

## Endpoint Documentation Gaps

The first-pass endpoint reference now lives in `docs/api/index.md`.

Remaining API gaps:

- flexible response schemas with `extra="allow"` need deeper shape docs
- generic event/debug payload contracts need a dedicated event contract
  reference
- route tests are not tagged with machine-readable endpoint IDs

## Database Documentation Gaps

The first-pass data/model reference now lives in `docs/data/index.md`.

Remaining data documentation gaps:

- migration-to-column mapping is filename-level, not exhaustive
- repository methods are grouped by responsibility, not documented one by one

## Tests Without Explicit Feature Metadata

The backend test suite is now mapped at file level in
[Test Ownership Ledger](../engineering/test-ownership-ledger.md). Remaining
gap: ownership is not yet test-function-level and no inline pytest marker
convention has been adopted.

## Features With Documentation But No Dedicated Tests Found In This Pass

- Frontend route rendering has build and screenshot task evidence, but no
  dedicated frontend unit/e2e suite was found during PRJ-937.
- UX parity docs are extensive, but automated screenshot comparison ownership
  appears task-evidence-driven rather than a stable test command.

## Next Repair Loops

The ordered repair lane is tracked in
[Documentation System Gap Repair Plan](../planning/documentation-system-gap-repair-plan.md).

No documentation-system repair loops from PRJ-945 remain open. New loops should
come from fresh drift findings or implementation changes.
