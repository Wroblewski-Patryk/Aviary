# Task

## Header
- ID: PRJ-1276
- Title: Fast and heavy graph validation modes
- Task Type: test
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1275
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1276
- Operation Mode: BUILDER
- Mission ID: PRJ-1276-fast-heavy-graph-validation-modes
- Mission Status: VERIFIED

## Context

`PRJ-1275` added a strong all-node parity test, but that made the focused
architecture graph pytest suite take around two minutes. The system needed a
clear fast gate for everyday work and a heavy gate for pre-release or
high-confidence graph validation.

## Goal

Mark the all-node parity test as `slow`, register the marker, and document
fast versus heavy graph validation commands.

## Scope

- `backend/tests/test_architecture_graph_generator.py`
- `backend/pyproject.toml`
- `docs/architecture/graph-system.md`
- `docs/architecture/registry/README.md`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Add a registered `slow` pytest marker.
2. Mark the all-node parity test as slow.
3. Document the fast graph gate using `-m "not slow"`.
4. Document the heavy graph gate that includes all-node parity.
5. Verify both gates.
6. Regenerate graph artifacts and update state.

## Acceptance Criteria

- Fast gate passes and deselects the slow parity test.
- Heavy gate passes and includes the slow parity test.
- Documentation names both commands.
- Evidence registry summary reflects validation-mode coverage.
- Full graph generation passes after docs/evidence updates.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `8 passed, 1 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `9 passed in 99.70s`
- `Push-Location .\backend; ..\.venv\Scripts\python -m py_compile .\scripts\generate_architecture_graph.py .\scripts\generate_architecture_inventory.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- final rerun of the fast gate after source-of-truth updates -> PASS,
  `8 passed, 1 deselected in 4.18s`
- `git diff --check` -> PASS with CRLF normalization warnings only
- Result:
  - `auto_nodes=5226`
  - `auto_relations=3931`
  - merged graph `nodes=5282`
  - merged graph `relations=3976`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=13`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: split architecture graph validation into documented fast and
  heavy modes.
- Files changed: pytest marker config, graph generator test, graph docs,
  registry docs, evidence registry, generated graph artifacts, and state files.
- How tested: fast gate, heavy gate, py_compile, full graph generation, and
  `git diff --check` passed.
- What is incomplete: CI policy still needs a future decision on whether the
  heavy gate runs always, pre-release only, or manually.
- Next steps: choose one concrete UX/UI graph node for a scoped research claim.

## Autonomous Loop Evidence

### 1. Analyze Current State
- All-node parity was correct but heavy.

### 2. Select One Priority Mission Objective
- Selected objective: make graph validation both strong and practical.

### 3. Plan Implementation
- Add marker, document fast/heavy commands, validate both paths.

### 4. Execute Implementation
- Added `slow` marker and fast/heavy validation documentation.

### 5. Verify and Test
- Fast and heavy graph pytest gates passed.

### 6. Self-Review
- Everyday agents can now run a fast gate while retaining a strong heavy gate
  for release-level confidence.

### 7. Update Documentation and Knowledge
- Evidence registry and state updates are part of this checkpoint.
