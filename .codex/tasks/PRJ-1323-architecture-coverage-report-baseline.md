# Task

## Header
- ID: PRJ-1323
- Title: Architecture coverage report baseline for full-function mapping
- Task Type: analysis
- Current Stage: verification
- Status: DONE
- Owner: Planning + QA/Test
- Depends on: PRJ-1322
- Priority: P1
- Mission ID: PRJ-1323-architecture-coverage-report-baseline
- Mission Status: VERIFIED

## Goal
Provide a deterministic coverage report that quantifies how far the project is from "every function fully described with chain/evidence".

## Definition of Done
- [x] add a coverage-report script over generated architecture graph data
- [x] generate JSON and Markdown baseline reports
- [x] publish the baseline counts for curated scope vs full (curated + auto) scope
- [x] generate a prioritized curation queue for function/class/API/component/test nodes

## Validation Evidence
- script:
  - `backend/scripts/report_architecture_coverage.py`
- command:
  - `Push-Location backend; ..\.venv\Scripts\python scripts/report_architecture_coverage.py; Pop-Location`
- output:
  - `json_report=docs/status/architecture-coverage-report.json`
  - `markdown_report=docs/status/architecture-coverage-report.md`
  - `curated_gap_nodes=0`
  - `all_gap_nodes=5300`
- prioritized queue:
  - `docs/status/architecture-gaps-all-full.json` (full gap export)
  - `docs/status/architecture-curation-queue-priority.csv` (`queue_rows=3265`)
  - `docs/status/architecture-curation-batch-1-template.csv` (`batch_rows=120`)
- operational coverage mode:
  - `backend/scripts/query_architecture_graph.py` supports `--gap-mode strict|operational`
  - query regression pack PASS: `26 passed`
  - operational full-scope report:
    - `docs/status/architecture-coverage-report-operational.json`
    - `docs/status/architecture-coverage-report-operational.md`
    - `curated_gap_nodes=0`, `all_gap_nodes=1121` (initial operational baseline)
    - `curated_gap_nodes=0`, `all_gap_nodes=0` (after relation coverage refinement + graph regeneration)
  - canonical gate:
    - `run_architecture_graph_local_release_gate.py` -> `overall_status=PASSED`

## Result
The system is fully closed for curated proof scope, while full auto-discovered scope still requires iterative curation/evidence promotion.
