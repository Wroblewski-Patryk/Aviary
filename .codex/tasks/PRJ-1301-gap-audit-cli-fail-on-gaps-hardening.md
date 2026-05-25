# Task

## Header
- ID: PRJ-1301
- Title: Gap audit CLI fail-on-gaps hardening
- Task Type: implementation
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1300
- Priority: P1
- Mission ID: PRJ-1301-gap-audit-cli-fail-on-gaps-hardening
- Mission Status: VERIFIED

## Goal
Add native `--fail-on-gaps` support to graph query CLI and use it directly in CI.

## Scope
- `backend/scripts/query_architecture_graph.py`
- `backend/tests/test_architecture_graph_query.py`
- `.github/workflows/architecture-graph.yml`
- `docs/architecture/graph-system.md`
- `docs/engineering/testing.md`

## Validation Evidence
- Graph query/generator fast suite PASS (`33 passed, 1 deselected`)
- `query_architecture_graph.py --gaps --format json --fail-on-gaps` PASS on current zero-gap graph
- CI workflow now uses native CLI exit behavior instead of inline JSON parsing

## Residual
Hosted Actions proof remains pending next push/PR run.
