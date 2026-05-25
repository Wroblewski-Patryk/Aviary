# Task

## Header
- ID: PRJ-1268
- Title: Research evidence mapping layer
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1266, PRJ-1267
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1268
- Operation Mode: BUILDER
- Mission ID: PRJ-1268-research-evidence-mapping-layer
- Mission Status: VERIFIED

## Context

The user asked for the feature-management agent to connect neuroscience-backed
project theories to scientific sources where possible. The existing graph
system already had implementation, test, behavior, connection, and
documentation evidence, but not a separate research-evidence layer.

## Goal

Add a CSV-backed research evidence layer so neuroscience-inspired or
cognitive-science claims expressed in code/docs can be linked to reviewed
scientific sources, applicability scope, limitations, and generated graph
outputs.

## Scope

- `docs/architecture/registry/research_sources.csv`
- `docs/architecture/registry/theory_claims.csv`
- `backend/scripts/generate_architecture_graph.py`
- `docs/testing/architecture-research-map.md`
- generated node pages and graph JSON
- graph-system documentation and source-of-truth state updates

## Implementation Plan

1. Add research source and theory claim CSV contracts.
2. Require reviewed/mapped theory claims to cite at least 3 source IDs.
3. Keep scientific support separate from runtime/test evidence.
4. Generate node-page theory claim sections and a research rollup.
5. Seed initial neuroscience sources and claims for runtime and memory flow.
6. Regenerate the auto inventory and architecture graph.

## Acceptance Criteria

- Research sources and theory claims are canonical CSV inputs.
- Reviewed/mapped claims fail validation if fewer than 3 sources are linked.
- Generated graph JSON includes research sources and theory claims.
- Obsidian node pages show theory claims for affected nodes.
- `docs/testing/architecture-research-map.md` is generated.
- Validation passes without starting local servers or browsers.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python -m py_compile .\scripts\generate_architecture_graph.py .\scripts\generate_architecture_inventory.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5203`
  - `auto_relations=3917`
  - merged graph `nodes=5256`
  - merged graph `relations=3959`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=10`
  - research sources `research_sources=4`
  - theory claims `theory_claims=2`

## Result Report

- Task summary: added a research evidence layer to the architecture graph.
- Files changed: graph generator, research CSVs, graph docs, generated graph
  artifacts, and project state files.
- How tested: Python compile plus full inventory and graph generation passed.
- What is incomplete: the seed source set covers the first two claims only;
  future neuroscience-inspired features need claim-by-claim review and source
  promotion.
- Next steps: when a feature expresses a cognitive/neuroscience theory, add a
  theory claim with 3 sources or mark it `needs_sources`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Existing evidence registry covered implementation/test/docs but not
  scientific support for cognitive theories.

### 2. Select One Priority Mission Objective
- Selected objective: add research evidence as a bounded extension to the graph
  system.

### 3. Plan Implementation
- Add CSV contracts, validation, generated outputs, seed rows, and state
  updates.

### 4. Execute Implementation
- Added research source and theory claim registries and graph generator
  support.

### 5. Verify and Test
- Compile and full inventory plus graph generation passed.

### 6. Self-Review
- Scientific evidence is explicitly scoped as theory support, not runtime
  proof or consciousness proof.

### 7. Update Documentation and Knowledge
- Updated graph-system docs and source-of-truth state files.
