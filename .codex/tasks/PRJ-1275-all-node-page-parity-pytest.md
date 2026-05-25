# Task

## Header
- ID: PRJ-1275
- Title: All node page parity pytest
- Task Type: test
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1274
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1275
- Operation Mode: TESTER
- Mission ID: PRJ-1275-all-node-page-parity-pytest
- Mission Status: VERIFIED

## Context

`PRJ-1274` compared key generated graph artifacts, but not every generated
Obsidian node page. A stale, orphaned, or unrefreshed node page could still
survive unnoticed.

## Goal

Add a full node-page parity test that regenerates node pages into a temporary
directory, compares the generated node file set with the repository node file
set, and verifies file content parity for every generated node page.

## Scope

- `backend/tests/test_architecture_graph_generator.py`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Generate node pages into `tmp_path`.
2. Compare generated and committed node page file names.
3. Assert committed node page count matches the loaded registry node count.
4. Compare generated and committed content for every node page.
5. Update evidence and state.

## Acceptance Criteria

- Focused pytest passes.
- Test writes only to a temp directory.
- Orphaned, missing, or stale node pages would fail the test.
- Full graph generation passes after evidence update.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `9 passed in 108.30s`
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5225`
  - `auto_relations=3931`
  - merged graph `nodes=5281`
  - merged graph `relations=3976`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=13`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: added full generated node-page parity coverage.
- Files changed: graph generator test, evidence registry, generated graph
  artifacts, and project state files.
- How tested: focused pytest and full graph generation passed.
- What is incomplete: this is intentionally heavier than the fast checks; use
  it as a strong graph integrity gate.
- Next steps: decide whether this heavy parity check belongs in CI or remains
  a pre-release/manual validation gate.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Key artifact parity existed, but all generated node pages were not checked.

### 2. Select One Priority Mission Objective
- Selected objective: full node-page parity guard.

### 3. Plan Implementation
- Generate node pages to temp output and compare file set plus content.

### 4. Execute Implementation
- Added all-node parity test to `test_architecture_graph_generator.py`.

### 5. Verify and Test
- Focused pytest passed with 9 tests in 108.30 seconds.

### 6. Self-Review
- The test is strong but heavy; CI inclusion should be a conscious policy
  decision.

### 7. Update Documentation and Knowledge
- Evidence registry and state updates are part of this checkpoint.
