# Task

## Header
- ID: PRJ-1279
- Title: Profile Settings Chain Refresh
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1278
- Priority: P1
- Coverage Ledger Rows: CHAIN-PROFILE-SETTINGS
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-SEMANTIC-CURATION
- Iteration: 1279
- Operation Mode: BUILDER
- Mission ID: PRJ-1279-profile-settings-chain-refresh
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] `.agents/core/mission-control.md` was reviewed for long-running work.
- [x] Missing or template-like state tables were bootstrapped from repository
      sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: promote the stale partial profile/settings execution chain
  into fresh verified graph evidence.
- Release objective advanced: architecture graph semantic curation for a real
  UI/API/model/test/docs chain.
- Included slices: Settings page route, web app shell, `/app/me` API,
  profile model, preferences/API tests, docs/evidence graph rows.
- Explicit exclusions: deeper interactive browser form journey and production
  account data smoke.
- Checkpoint cadence: one focused verification slice.
- Stop conditions: stop if profile API tests, web build, route smoke, or graph
  validation fails.
- Handoff expectation: future agents can treat `CHAIN-PROFILE-SETTINGS` as
  verified local evidence while still seeing the excluded deeper UX journey.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `.agents/state/next-steps.md` | Mission integration and state updates | Verified chain closure | Parent validation gate | DONE |
| Product/Requirements | Active chat | `docs/architecture/registry/chains.csv` | Profile settings chain scope | Bounded chain objective | Evidence row | DONE |
| Architecture | Active chat | `docs/architecture/graph-system.md` | Registry graph semantics | Chain marked verified | Graph generator tests | DONE |
| Backend/API | Active chat | `backend/tests/test_api_routes.py` | `/app/me` settings API | Focused route proof | pytest focused selection | DONE |
| Frontend/UX | Active chat | `web/scripts/route-smoke.mjs` | `/settings` route rendering | Route marker proof | route smoke | DONE |
| Data/Migrations | Active chat | `MODEL-AION-PROFILE` registry row | Profile model linkage | Existing model link retained | backend tests | DONE |
| QA/Test | Active chat | `backend/tests/test_architecture_graph_generator.py` | Graph status pin | Regression pin | graph pytest | DONE |
| Security/Ops/Docs | Active chat | `.agents/state/*` | Evidence and state docs | Source-of-truth refresh | `git diff --check` | DONE |

### Lane Checks

- [x] `.agents/state/active-mission.md` was created or refreshed for broad work.
- [x] `.agents/workflows/responsibility-lanes.md` was reviewed.
- [x] Every important responsibility has an owner or explicit omission.
- [x] No delegated write lanes overlap.
- [x] Each delegated lane has expected output and proof.
- [x] Missing ownership/evidence/context gaps will be recorded in
      `.agents/state/responsibility-learning.md` if discovered.
- [x] Process eval will be recorded in `.agents/state/agent-evals.md` if this
      is broad, repeated, partial, or subagent-heavy work.

## Context

`CHAIN-PROFILE-SETTINGS` was still `partial` even though its feature, API,
model, tests, and page nodes were already verified. The graph system needed
one stale functional chain promoted with current proof after PRJ-1278 closed
the graph workflow mechanics.

## Goal

Refresh profile/settings proof across UI route, backend API, profile model,
tests, and docs links, then mark the chain verified.

## Success Signal
- User or operator problem: agents can inspect profile/settings as a complete
  execution chain instead of finding a stale partial row.
- Expected product or reliability outcome: profile/settings has current local
  proof across route rendering and backend settings contract tests.
- How success will be observed: chain row, evidence row, generated graph, and
  graph pytest all agree.
- Post-launch learning needed: no

## Deliverable For This Stage

Verified graph registry update plus generated artifacts and state updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `CHAIN-PROFILE-SETTINGS` is verified in `chains.csv`.
- [x] A fresh evidence row records profile/settings proof.
- [x] Graph generator tests pin the chain and evidence.
- [x] Generated graph artifacts are refreshed.
- [x] State files record proof and residual risk.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_preferences.py tests/test_api_routes.py -k "app_me or patch_settings or preference"; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `10 passed, 127 deselected in 3.32s`
  - `Push-Location .\web; npm run build; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
  - `Push-Location .\web; npm run smoke:routes; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `route_count=14`, `status=ok`, `/settings` marker `aion-settings-canvas` passed
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `auto_nodes=5229`, `auto_relations=3931`, merged `nodes=5286`, `relations=3979`, `chains=7`, `evidence=16`, `research_sources=21`, `theory_claims=9`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `8 passed, 1 deselected in 3.69s`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m py_compile .\scripts\generate_architecture_inventory.py .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Manual checks: registry chain row reviewed against existing relation and node rows.
- Screenshots/logs: route smoke JSON output reviewed in terminal.
- High-risk checks: no runtime implementation changed.
- Coverage ledger updated: yes
- Coverage rows closed or changed: `CHAIN-PROFILE-SETTINGS`
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: `AVIARY-ARCH-GRAPH-001`
- Requirements matrix updated: yes
- Requirement rows closed or changed: `REQ-ARCH-1268`
- Quality scenarios updated: yes
- Quality scenario rows closed or changed: `QA-MAINT-ARCH-GRAPH-1268`
- Risk register updated: yes
- Risk rows closed or changed: `RISK-ARCH-GRAPH-SEMANTIC-CURATION`

## Result Report

`CHAIN-PROFILE-SETTINGS` is now verified with fresh backend settings API,
preference utility, web build, and `/settings` route smoke evidence. The graph
test suite pins both the chain status and new evidence row so the map fails if
the registry drifts.
