# Task

## Header
- ID: PRJ-1273
- Title: Generated graph freshness pytest
- Task Type: test
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1272
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1273
- Operation Mode: BUILDER
- Mission ID: PRJ-1273-generated-graph-freshness-pytest
- Mission Status: VERIFIED

## Context

The graph generator tests validated synthetic rows and the live CSV registry,
but they did not yet detect stale generated outputs. A future agent could edit
CSV files and forget to regenerate `architecture-graph.json` or rollups.

## Goal

Add pytest coverage that checks generated graph outputs are aligned with the
current loaded registry and include the latest evidence/research rollup rows.

## Scope

- `backend/tests/test_architecture_graph_generator.py`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Load the current registry and generated `architecture-graph.json`.
2. Compare generated counts for nodes, relations, chains, evidence, research
   sources, and theory claims against the live registry.
3. Assert generated evidence and research rollups include recent critical
   entries.
4. Update evidence registry summary.
5. Regenerate graph outputs and update state.

## Acceptance Criteria

- Focused pytest passes.
- Generated graph JSON count mismatches would fail the test.
- Generated rollup omissions for latest research/evidence rows would fail the
  test.
- Full graph generation passes after evidence update.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `7 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5221`
  - `auto_relations=3929`
  - merged graph `nodes=5277`
  - merged graph `relations=3974`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=13`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: added generated-output freshness checks to the architecture
  graph pytest suite.
- Files changed: graph generator test, evidence registry, generated graph
  artifacts, and project state files.
- How tested: focused pytest and full graph generation passed.
- What is incomplete: the test checks counts and critical rows, not byte-for-
  byte no-diff generation.
- Next steps: add a strict no-diff CI gate only if generated docs become a
  required CI artifact.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Live registry tests existed, but generated outputs could still go stale.

### 2. Select One Priority Mission Objective
- Selected objective: generated graph freshness pytest.

### 3. Plan Implementation
- Compare generated graph JSON counts with live registry counts and inspect
  generated rollups for critical rows.

### 4. Execute Implementation
- Added generated-output assertions to `test_architecture_graph_generator.py`.

### 5. Verify and Test
- Focused pytest passed with 7 tests.

### 6. Self-Review
- Test avoids rewriting generated docs and provides a practical stale-output
  guard.

### 7. Update Documentation and Knowledge
- Evidence registry and state updates are part of this checkpoint.
