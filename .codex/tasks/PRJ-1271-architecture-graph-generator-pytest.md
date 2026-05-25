# Task

## Header
- ID: PRJ-1271
- Title: Architecture graph generator pytest coverage
- Task Type: test
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1268, PRJ-1269, PRJ-1270
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1271
- Operation Mode: BUILDER
- Mission ID: PRJ-1271-architecture-graph-generator-pytest
- Mission Status: VERIFIED

## Context

The architecture graph generator had command-level proof, but no dedicated
pytest for the research-evidence validation rules. Since the graph is becoming
a project nervous system, generator validation needs automated test coverage.

## Goal

Add focused pytest coverage for the research claim validation contract and
graph research payload export.

## Scope

- `backend/tests/test_architecture_graph_generator.py`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Import the graph generator script through `importlib`.
2. Build minimal in-memory registry rows.
3. Verify reviewed theory claims with fewer than 3 sources fail validation.
4. Verify reviewed theory claims with 3 existing sources pass validation.
5. Verify graph JSON exports include research sources and theory claims.
6. Register the pytest as evidence.

## Acceptance Criteria

- Focused pytest passes.
- Test does not mutate repository docs.
- Evidence registry links the pytest to `TEST-ARCH-GRAPH-GENERATOR`.
- Full graph generation still passes after evidence update.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `3 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5215`
  - `auto_relations=3925`
  - merged graph `nodes=5271`
  - merged graph `relations=3970`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=13`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: added focused pytest coverage for graph generator research
  validation and export behavior.
- Files changed: new test file, evidence registry, generated graph artifacts,
  and project state files.
- How tested: focused pytest and full graph generation passed.
- What is incomplete: broader end-to-end fixture tests for full registry
  generation can be added later if graph schema changes again.
- Next steps: add a CI or task-board gate that includes this focused pytest
  before claiming research-evidence changes verified.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Generator had command proof but no pytest for research-evidence rules.

### 2. Select One Priority Mission Objective
- Selected objective: focused generator contract test.

### 3. Plan Implementation
- Test validation rules and JSON export directly through the generator module.

### 4. Execute Implementation
- Added `backend/tests/test_architecture_graph_generator.py`.

### 5. Verify and Test
- Focused pytest passed with 3 tests.

### 6. Self-Review
- Test uses temp output for graph export and does not mutate repository docs.

### 7. Update Documentation and Knowledge
- Evidence registry and state updates are part of this checkpoint.
