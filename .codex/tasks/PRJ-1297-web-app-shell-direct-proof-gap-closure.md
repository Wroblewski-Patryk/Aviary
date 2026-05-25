# Task

## Header
- ID: PRJ-1297
- Title: Web app shell direct proof gap closure
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1296
- Priority: P1
- Mission ID: PRJ-1297-web-app-shell-direct-proof-gap-closure
- Mission Status: VERIFIED

## Goal
Add direct graph evidence for `COMP-WEB-APP` so the shell component no longer appears in curated proof gaps.

## Scope
- `docs/architecture/registry/evidence.csv`
- `backend/tests/test_architecture_graph_generator.py`
- `backend/tests/test_architecture_graph_query.py`
- generated graph artifacts under `docs/architecture/`

## Validation Evidence
- `npm run build` in `web` PASS
- `npm run smoke:routes` in `web` PASS (`route_count=14`, `status=ok`)
- inventory + graph generation PASS (`auto_nodes=5295`, `auto_relations=3977`, merged `nodes=5356`, `relations=4041`, `chains=9`, `evidence=53`)
- `pytest -q tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"` PASS (`28 passed, 1 deselected`)
- `query_architecture_graph.py --node COMP-WEB-APP --show-gaps` => `Gaps: none`

## Residual
Route/build proof is local and does not replace screenshot parity or production smoke.
