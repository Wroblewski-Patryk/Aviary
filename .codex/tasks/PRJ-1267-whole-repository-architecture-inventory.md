# Task

## Header
- ID: PRJ-1267
- Title: Whole-repository architecture inventory layer
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1266
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1267
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1267
- Risk Rows: RISK-ARCH-GRAPH-1267
- Iteration: 1267
- Operation Mode: BUILDER
- Mission ID: PRJ-1267-whole-repository-architecture-inventory
- Mission Status: VERIFIED

## Context

`PRJ-1266` created the curated CSV-first graph foundation. The user then asked
to execute everything. The next safe slice was to add a whole-repository
auto-inventory layer so the graph covers the full code/docs/config/test tree
without pretending every auto-discovered row is manually verified release
truth.

## Goal

Generate broad architecture graph coverage across the repository: files,
Python classes/functions, TypeScript/JavaScript symbols, CSS selectors, import
relations, contains relations, test-to-target heuristics, and doc-to-target
heuristics.

## Scope

- `backend/scripts/generate_architecture_inventory.py`
- `backend/scripts/generate_architecture_graph.py`
- `docs/architecture/registry/auto_nodes.csv`
- `docs/architecture/registry/auto_relations.csv`
- `docs/architecture/registry/auto_inventory_summary.md`
- generated graph artifacts under `docs/architecture/nodes/`,
  `docs/architecture/relations/`, `docs/architecture/graphs/`,
  `docs/status/`, and `docs/testing/`
- source-of-truth state updates for this checkpoint

## Implementation Plan

1. Add a repository scanner that prunes generated/heavy directories before
   traversal.
2. Generate file nodes for source, docs, tests, config, migrations, scripts,
   and task/state artifacts.
3. Generate symbol nodes for Python classes/functions, TS/JS symbols, and CSS
   selectors.
4. Generate `parent_of`, import `depends_on`, `verifies`, and `documents`
   relations where discoverable.
5. Merge auto CSV inputs into the graph generator.
6. Regenerate graph outputs.
7. Keep human status rollup concise by summarizing auto-discovered rows.

## Acceptance Criteria

- Auto inventory CSVs are generated and included in the graph.
- Graph generation merges curated and auto-discovered rows.
- Generated output excludes recursive generated graph directories.
- Status rollup distinguishes curated gaps from auto-discovered broad coverage.
- Validation passes without starting local servers or browser processes.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5197`
  - `auto_relations=3915`
  - merged graph `nodes=5249`
  - merged graph `relations=3954`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=9`

## Result Report

- Task summary: added the full-repository auto-inventory layer and merged it
  into the architecture graph.
- Files changed: inventory script, graph generator, registry generated CSVs,
  generated graph artifacts, and project state files.
- How tested: inventory plus graph generation command passed.
- What is incomplete: auto-discovered rows are not release-critical proof by
  themselves; curated chains/evidence still need module-by-module promotion.
- Next steps: promote critical auto rows into curated feature chains for API,
  runtime, memory, frontend routes, and tests.

## Autonomous Loop Evidence

### 1. Analyze Current State
- PRJ-1266 had curated graph foundation but not whole-repository breadth.

### 2. Select One Priority Mission Objective
- Selected objective: whole-repository inventory layer.

### 3. Plan Implementation
- Build scanner, generate CSV, merge into graph, verify.

### 4. Execute Implementation
- Added `generate_architecture_inventory.py` and updated graph generator.

### 5. Verify and Test
- Combined inventory and graph generation passed.

### 6. Self-Review
- Initial `rglob` scan timed out. It was replaced with pruned `os.walk`.
- Status rollup was adjusted to summarize auto inventory instead of dumping
  thousands of rows as human action items.

### 7. Update Documentation and Knowledge
- Updated graph docs and state files.
