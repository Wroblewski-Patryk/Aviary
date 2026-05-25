# Task

## Header
- ID: PRJ-1272
- Title: Current registry validation pytest
- Task Type: test
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1271
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1272
- Operation Mode: BUILDER
- Mission ID: PRJ-1272-current-registry-validation-pytest
- Mission Status: VERIFIED

## Context

`PRJ-1271` added focused in-memory tests for research claim validation and
graph JSON export. The next hardening step was to test the actual current
repository registry, not only synthetic rows.

## Goal

Ensure the current canonical CSV registry validates under pytest and the
research rollup can be generated into a temporary directory without mutating
repository docs.

## Scope

- `backend/tests/test_architecture_graph_generator.py`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Add a pytest that loads the current repository registry.
2. Assert `validate_registry` returns no errors.
3. Assert the current research layer contains expected minimum source and
   claim coverage.
4. Assert every current theory claim has at least three source IDs.
5. Generate the current research rollup into a temp directory and inspect key
   claim IDs.
6. Regenerate graph outputs and update state.

## Acceptance Criteria

- Focused pytest passes.
- Test reads current CSV registry and does not write to repository docs.
- Evidence registry summary reflects the broader pytest coverage.
- Full graph generation passes after the evidence update.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `5 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5218`
  - `auto_relations=3927`
  - merged graph `nodes=5274`
  - merged graph `relations=3972`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=13`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: extended graph generator pytest coverage to the live canonical
  registry and temp research rollup generation.
- Files changed: graph generator test, evidence registry, generated graph
  artifacts, and project state files.
- How tested: focused pytest and full graph generation passed.
- What is incomplete: this does not yet compare generated repo files for drift;
  that can be a later CI-style checksum or no-diff gate.
- Next steps: add a stale-generated-output detection gate if CI begins
  enforcing docs generation.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Existing pytest covered synthetic rows, but not the live registry.

### 2. Select One Priority Mission Objective
- Selected objective: validate the current canonical CSV registry under pytest.

### 3. Plan Implementation
- Load registry, validate, check research coverage, write temp rollup.

### 4. Execute Implementation
- Added live-registry tests to `test_architecture_graph_generator.py`.

### 5. Verify and Test
- Focused pytest passed with 5 tests.

### 6. Self-Review
- Tests write only to `tmp_path` and do not mutate repository docs.

### 7. Update Documentation and Knowledge
- Evidence registry and state updates are part of this checkpoint.
