# Task

## Header
- ID: PRJ-1274
- Title: Generated artifact parity pytest
- Task Type: test
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1273
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1274
- Operation Mode: BUILDER
- Mission ID: PRJ-1274-generated-artifact-parity-pytest
- Mission Status: VERIFIED

## Context

`PRJ-1273` checked generated graph JSON counts and critical rollup rows. The
remaining practical stale-output gap was whether key generated artifacts in the
repository exactly match a fresh generator run.

## Goal

Add a no-mutation pytest that regenerates graph artifacts into a temporary
directory and compares key generated outputs with the repository versions.

## Scope

- `backend/tests/test_architecture_graph_generator.py`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Load the live registry.
2. Write generated node pages, relation index, chain index, graph exports,
   status rollup, evidence rollup, and research rollup to `tmp_path`.
3. Compare key generated files with the repository versions.
4. Include critical node pages for research-expanded runtime stages and the
   graph generator test node.
5. Update evidence and project state.

## Acceptance Criteria

- Focused pytest passes.
- Test writes only to a temp directory.
- Key generated artifacts match current generator output exactly.
- Full graph generation passes after evidence update.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `8 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5223`
  - `auto_relations=3930`
  - merged graph `nodes=5279`
  - merged graph `relations=3975`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=13`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: added key generated artifact parity checks to the graph
  generator pytest suite.
- Files changed: graph generator test, evidence registry, generated graph
  artifacts, and project state files.
- How tested: focused pytest and full graph generation passed.
- What is incomplete: the test compares key artifacts and selected node pages,
  not every generated node page.
- Next steps: expand parity to all generated node pages only if runtime cost is
  acceptable in CI.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Stale-output guard existed for counts and key rows but not exact artifact
  parity.

### 2. Select One Priority Mission Objective
- Selected objective: key generated artifact parity guard.

### 3. Plan Implementation
- Generate into `tmp_path` and compare key outputs with repository files.

### 4. Execute Implementation
- Added artifact parity test to `test_architecture_graph_generator.py`.

### 5. Verify and Test
- Focused pytest passed with 8 tests.

### 6. Self-Review
- The test avoids mutating repository docs and gives path-specific failures.

### 7. Update Documentation and Knowledge
- Evidence registry and state updates are part of this checkpoint.
