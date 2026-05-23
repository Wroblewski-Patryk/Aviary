# Task

## Header
- ID: PRJ-1237
- Title: Canonical UI layout index and simplification mission
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1236
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: `AVIARY-WEB-RESP-001`
- Requirement Rows: `REQ-UX-1237`
- Quality Scenario Rows: `QA-UX-1237`
- Risk Rows: `RISK-UI-1237`
- Iteration: 1237
- Operation Mode: ARCHITECT
- Mission ID: PRJ-1237-canonical-ui-layout-index
- Mission Status: COMPLETED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed in active mission context.
- [x] `.agents/core/mission-control.md` was reviewed for continuation work.
- [x] Missing or template-like state tables were confirmed not needed for this planning slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: turn the user's simplification direction into a canonical UI layout index that maps visible groups to backend-supported functions and removes permission for unnecessary cards, badges, chips, and inert controls.
- Release objective advanced: v1.2 web UI simplification and future native UI generation readiness.
- Included slices: canonical UI index doc, route group IDs, backend data-source mapping, simplification order, state updates.
- Explicit exclusions: broad implementation rewrite, backend/API changes, native app generation, production release.
- Checkpoint cadence: planning artifact first, then route-local implementation passes.
- Stop conditions: architecture/data mapping is unclear, canonical references conflict with user direction, or a route requires backend data not currently available.
- Handoff expectation: a durable spec that future passes can implement and validate route by route.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `AGENTS.md`, mission-control, UX docs | Integration, state, final decision | Mission closure | Parent validation gate | COMPLETED |
| Architecture/Data | Subagent James | architecture docs, API contracts, web routes | Read-only backend-data mapping | Route data/function report | Lane report | TIMED_OUT |
| UX/Reference | Subagent Newton | canonical refs, screenshots, design memory | Read-only simplification taxonomy | UX simplification report | Lane report | COMPLETED |
| Product Docs | Active chat | `docs/ux/*`, route manifest | `docs/ux/canonical-ui-layout-index.md` | Canonical index | Doc diff | COMPLETED |
| QA/Test | Active chat | docs and current green proof | Planning validation | Source alignment | Inspection | COMPLETED |
| Docs/State | Active chat | state docs | Durable evidence | Updated ledgers | State diff | COMPLETED |

## Context
After many v1.2 polish passes, the web UI is visually richer but the user has identified a deeper product problem: too many controls, cards, badges, and equal-weight groups create chaos. The next step is not to add more polish but to define a stable, canonical UI index before simplifying implementation.

## Goal
Create a source-of-truth UI layout index that says which visible groups exist, what backend-backed function or data they represent, which routes may use them, and which noisy patterns must be removed or demoted.

## Scope
- `docs/ux/canonical-ui-layout-index.md`
- `.codex/tasks/PRJ-1237-canonical-ui-layout-index.md`
- `.agents/state/active-mission.md`
- required state/context docs

## Implementation Plan
1. Read canonical UX, architecture, API contract, route manifest, and current mission state.
2. Delegate read-only architecture/data and UX/reference lanes.
3. Draft the canonical UI layout index with shell zones, component budget, data-source IDs, route group IDs, and simplification order.
4. Integrate lane findings when available.
5. Update state docs and commit the planning artifact if coherent.

## Acceptance Criteria
- Global shell zones are defined once.
- Route groups are indexed with stable IDs.
- Every route maps to backend/client data authority.
- Noise patterns are explicitly removable or demotable.
- Future implementation order is route-local and evidence-based.

## Definition of Done
- [x] `docs/ux/canonical-ui-layout-index.md` exists.
- [x] The index maps global shell, data authority, route groups, component budgets, and simplification order.
- [x] Subagent lane reports are integrated or recorded as pending if still running.
- [x] State docs are updated.
- [x] No implementation rewrite is started before the planning artifact is stable.

## Forbidden
- broad UI rewrite without the canonical index
- new backend contracts
- new visual language that conflicts with canonical references
- keeping inert controls as primary UI
- production release claim

## Validation Evidence
- Tests: not applicable for planning artifact
- Manual checks:
  - reviewed canonical UX source set, current design memory, route data/API contract inventory, and recent PRJ-1234/1235/1236 proof paths
  - integrated UX/reference lane report into noise taxonomy, first-read hierarchy, route hierarchy rules, and pass order
  - architecture/data subagent timed out and was closed; the document explicitly limits authority to known app API contracts until new backend contracts exist
- Screenshots/logs: not applicable
- High-risk checks:
  - no production code rewrite started before the planning artifact
  - no new backend contract invented
  - no production release claimed
- Reality status: verified as planning/source-of-truth artifact

## Result Report
`PRJ-1237` creates the durable UI simplification index for v1.2. The new
source-of-truth document defines global shell zones, backend/client data
authority IDs, route group IDs, component budgets, first-read hierarchy, noise
taxonomy, pass order, ownership map, and acceptance gates. It is now the
foundation for route-local implementation passes that remove unnecessary cards,
badges, chips, fake chrome, and inert controls while preserving canonical
visual direction and backend-backed function.
