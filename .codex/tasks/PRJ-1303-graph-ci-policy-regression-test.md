# Task

## Header
- ID: PRJ-1303
- Title: Graph CI policy regression test
- Task Type: implementation
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1302
- Priority: P1
- Mission ID: PRJ-1303-graph-ci-policy-regression-test
- Mission Status: VERIFIED

## Goal
Prevent silent CI policy drift by testing graph workflow requirements directly.

## Scope
- `backend/tests/test_architecture_graph_ci_policy.py`

## Validation Evidence
- Graph policy test confirms `--fail-on-gaps` is present in workflow
- Graph policy test confirms hosted artifact upload steps are present
- Graph fast suite and local zero-gap audit remain green

## Residual
Hosted run evidence remains optional supplementary evidence under `DEC-005`.
