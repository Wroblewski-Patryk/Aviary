# Task

## Header
- ID: PRJ-1307
- Title: Hosted evidence artifact policy regression guard
- Task Type: implementation
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1306
- Priority: P1
- Mission ID: PRJ-1307-hosted-evidence-artifact-policy-regression-guard
- Mission Status: VERIFIED

## Goal
Protect hosted-evidence artifact publication in CI with explicit regression checks.

## Scope
- `backend/tests/test_architecture_graph_ci_policy.py`

## Validation Evidence
- Graph policy + verifier + packet + query/generator fast suite PASS (`39 passed, 1 deselected`)
- Local curated gap gate remains green (`items=[]`)

## Residual
Hosted artifact publication proof remains optional supplementary evidence under `DEC-005`.
