# Task

## Header
- ID: LUC-992
- Title: [Aviary] LUC-976-L3 Runtime smoke and regression evidence baseline
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: LUC-976
- Priority: P0
- Mission ID: LUC-976-takeover-baseline-refresh
- Mission Status: VERIFIED

## Context
Child lane `LUC-992` under `LUC-976` required a fresh, replayable runtime smoke and regression evidence baseline refresh for takeover preparation.

## Goal
Reconfirm core runtime baseline health with the smallest meaningful command set and leave durable evidence for parent-lane integration.

## Constraints
- Preparation-only lane (no runtime/code changes)
- No deploy, push, production mutation, or credential mutation
- Prefer existing canonical smoke/regression commands
- Unknowns must stay explicit

## Deliverable For This Stage
- one backend runtime regression proof
- one frontend runtime smoke proof
- explicit status classification and residual risk

## Acceptance Criteria
- backend release-smoke subset passes with replayable command evidence
- frontend route smoke passes across canonical route manifest
- results are written into a durable task packet
- residual risks are explicit and bounded

## Validation Evidence
- Backend release-smoke subset:
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py -k "release_smoke"; $code=$LASTEXITCODE; Pop-Location; exit $code`
  - Result: `41 passed, 23 deselected in 244.95s (0:04:04)`
- Backend full primary regression gate (assignment-recovery heartbeat):
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
  - Result: `1156 passed in 367.45s (0:06:07)`
- Frontend build + route smoke screenshot gate:
  - `Push-Location web; npm run build; $code=$LASTEXITCODE; Pop-Location; exit $code`
  - Result: PASS
  - `Push-Location web; node scripts/route-smoke.mjs --report ../.codex/artifacts/luc992-runtime-smoke-regression-baseline/report.json --screenshots ../.codex/artifacts/luc992-runtime-smoke-regression-baseline/screenshots --screenshot-routes /,/login,/dashboard,/chat,/personality,/tools,/integrations,/settings --viewports desktop,mobile --fail-on-ui-findings; $code=$LASTEXITCODE; Pop-Location; exit $code`
  - Result: `route_count=14`, `status=ok`, `viewport_count=2`, `screenshot_count=16`, `failed_count=0`

## Baseline Classification

| Surface | Status | Evidence |
| --- | --- | --- |
| Backend release-smoke trigger paths | implemented and verified | `tests/test_deployment_trigger_scripts.py -k release_smoke` (`41 passed`) |
| Backend full primary regression gate | implemented and verified | `python -m pytest -q` (`1156 passed`) |
| Frontend route mount smoke with screenshot parity gate | implemented and verified | `.codex/artifacts/luc992-runtime-smoke-regression-baseline/report.json` (`route_count=14`, `status=ok`, `screenshot_count=16`, `failed_count=0`) |

## Result Report
- Completed:
  - executed the minimal runtime smoke/regression baseline command set for `LUC-992`
  - recovered assignment heartbeat with full backend primary regression rerun and PASS evidence
  - captured replayable evidence with command strings and exact outcomes
  - stored screenshot-capable route-smoke artifact pack under `.codex/artifacts/luc992-runtime-smoke-regression-baseline/`
- Remaining:
  - close sibling `LUC-994` and integrate `LUC-990..LUC-994` into parent `LUC-976` closure
