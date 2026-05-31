# Task

## Header
- ID: LUC-991
- Title: [Aviary] LUC-976-L2 Product and capability roadmap audit
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Product Docs Agent
- Depends on: LUC-976
- Priority: P1
- Mission ID: LUC-976-takeover-baseline-refresh
- Mission Status: CHECKPOINTED

## Context
`LUC-991` is the Product Docs lane under the active takeover-preparation mission (`LUC-976`). The role scope is preparation-only: audit and map product/capability roadmap truth, then leave bounded follow-up signals without implementation work.

## Goal
Produce one evidence-backed product and capability roadmap audit that clarifies what is already implemented, what remains planned, and what should be treated as deferred or blocked for takeover readiness.

## Constraints
- preparation-only lane; no broad implementation
- no deploy, push, production mutation, or credential mutation
- unknowns must stay explicit
- output must be durable in repo source-of-truth files

## Deliverable For This Stage
- capability roadmap audit matrix linked to canonical product/planning docs
- mismatch/gap register with explicit statuses
- bounded follow-up recommendations for remaining `LUC-976` lanes

## Acceptance Criteria
- roadmap rows use evidence-backed status wording
- implemented-vs-planned boundaries are explicit for product capabilities
- deferred/blocked areas are separated from release-critical prep rows
- source-of-truth context is synced in the same heartbeat

## Product And Capability Roadmap Audit (2026-05-31)

| Capability area | Current status | Evidence | Roadmap posture |
| --- | --- | --- | --- |
| Backend-first AION runtime and app-facing API baseline | implemented and verified | `docs/overview.md`; `backend/app/api/routes.py`; `backend/tests/` | stable baseline; keep verification-first follow-ups |
| Web product shell and critical routes | implemented and verified | `.codex/context/PROJECT_STATE.md` (`LUC-944`); `web/scripts/route-smoke.mjs` | maintain via smoke gates; no broad redesign in this lane |
| Mobile surface | present in code, behavior partially verified | `.agents/state/delivery-map.md` (`AVIARY-DM-004`, `AVIARY-VIS-*`) | intentionally deferred; native proof still blocked by missing local Android tooling |
| External provider activation (ClickUp/Calendar/Drive/Telegram advanced flows) | implemented but not fully verified end-to-end | `docs/overview.md`; `.agents/state/delivery-map.md` (`AVIARY-DM-002`, `AVIARY-DM-027`) | keep as bounded follow-up slices; do not treat as takeover-prep blocker unless scope is reactivated |
| Architecture graph evidence system | implemented and verified | `.agents/state/delivery-map.md` (`AVIARY-DM-005..026`); `docs/graphs/*` | active and healthy; maintain incremental closure model |
| Product planning decision memory | implemented and verified with large backlog history | `docs/planning/open-decisions.md`; `docs/planning/next-iteration-plan.md` | needs prioritization hygiene for takeover readability, not feature changes |

## Gap Register

| Gap ID | Severity | Gap | Status | Next owner | Proof required |
| --- | --- | --- | --- | --- | --- |
| LUC991-G1 | P1 | `next-iteration-plan` carries historical queue volume that obscures near-term takeover readiness view | present in code, behavior unknown | Product Docs lane follow-up | narrowed takeover-focused roadmap appendix |
| LUC991-G2 | P1 | Delivery map includes active and archival trajectories together; current takeover slice is readable but not concise | implemented but not verified | Product Docs + Docs Memory lanes | compact active-release capability subset table |
| LUC991-G3 | P2 | Mobile readiness remains blocked by environment tooling (`adb`/`emulator`) but appears alongside active product signals | blocked by error | QA/Test + Ops/Release lanes | explicit deferred marker with unblock owner/action in release posture docs |

## Validation Evidence
- Manual evidence scan:
  - `docs/overview.md`
  - `docs/README.md`
  - `docs/planning/open-decisions.md`
  - `docs/planning/next-iteration-plan.md`
  - `.agents/state/delivery-map.md`
  - `.agents/state/next-steps.md`
- Runtime tests: not run (docs/state-only audit lane).
- Reality status: verified (for documented audit scope).

## Heartbeat Closure Note (2026-05-31)
- Acknowledged latest board comment (`local-board`): janitor status sync only; no new product/deploy mutation requested.
- Paperclip API closure attempt from this run was blocked by active ownership lock:
  - `POST /api/issues/{id}/comments` -> `Issue run ownership conflict`
  - `POST /api/issues/{id}/checkout` -> `Issue checkout conflict`
  - Active run observed via `GET /api/issues/{id}/active-run`: `runId=51f33417-fd21-4824-8f52-5190b028fe92`, `status=running`.
- Disposition intent for this lane remains `done` with evidence packet and source-of-truth sync already present.
- Unblock owner/action: active issue run owner should submit final `PATCH /api/issues/{id}` with `status=done` and closure comment referencing this packet.

## Lane Governance Addendum (2026-05-31)
- New board comment acknowledged: `softwarehouse-wip-dedupe:block-on-active-owner-lane:v1`.
- Operational effect:
  - this issue lane is blocked behind active `LUC-990` ownership and should be moved to `todo` plus re-woken only after `LUC-990` closes.
- Scope note:
  - this addendum changes run-governance disposition only; it does not invalidate the completed roadmap-audit evidence in this packet.

## Result Report
- Completed:
  - established a dedicated `LUC-991` product/capability roadmap audit packet
  - mapped capability areas to evidence-backed statuses (`implemented`, `planned`, `deferred`, `blocked`)
  - captured three bounded roadmap hygiene gaps with explicit next owners and proof expectations
- Remaining:
  - execute remaining sibling lanes (`LUC-990`, `LUC-992`, `LUC-993`, `LUC-994`) and integrate into parent `LUC-976` closure
  - optionally open a narrow Product Docs follow-up for roadmap readability compaction if board prioritizes it
