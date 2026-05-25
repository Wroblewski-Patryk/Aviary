# Task

## Header
- ID: PRJ-1269
- Title: Research claim expansion for perception planning and reflection
- Task Type: documentation
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1268
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1269
- Operation Mode: BUILDER
- Mission ID: PRJ-1269-research-claim-expansion
- Mission Status: VERIFIED

## Context

`PRJ-1268` created the research evidence layer with seed sources and claims.
The next continuation checkpoint was to promote additional cognitive runtime
theories into claim rows where at least three reviewed sources could be
attached.

## Goal

Expand research support for existing graph nodes covering perception/attention,
planning/executive-control, and memory/reflection consolidation.

## Scope

- `docs/architecture/registry/research_sources.csv`
- `docs/architecture/registry/theory_claims.csv`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts under `docs/architecture/` and `docs/testing/`
- source-of-truth state updates

## Implementation Plan

1. Add reviewed attention, salience, cognitive-control, and memory
   consolidation sources.
2. Add theory claims for `AGENT-PERCEPTION`, `AGENT-PLANNING`, and
   `FEAT-MEMORY-FLOW`.
3. Keep applicability scope and limitations explicit for every claim.
4. Regenerate inventory and graph artifacts.
5. Update project state and mission ledgers.

## Acceptance Criteria

- New reviewed/mapped claims cite at least 3 sources.
- Claims attach to existing graph node IDs.
- Generated research map includes the expanded claims and sources.
- Graph generation passes.
- Research evidence remains separate from runtime behavior proof.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5204`
  - `auto_relations=3917`
  - merged graph `nodes=5257`
  - merged graph `relations=3959`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=11`
  - research sources `research_sources=11`
  - theory claims `theory_claims=5`

## Result Report

- Task summary: expanded the research evidence layer for perception,
  planning, and memory/reflection theory claims.
- Files changed: research sources, theory claims, evidence registry, generated
  graph artifacts, and project state files.
- How tested: full inventory plus graph generation passed.
- What is incomplete: broader motivation/role/UX theory claims remain future
  rows unless claim-specific sources are added.
- Next steps: add motivation/affective and role-selection sources only after
  source review.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Research layer existed but only covered two seed claims.

### 2. Select One Priority Mission Objective
- Selected objective: expand research-backed theory claims for three existing
  runtime nodes.

### 3. Plan Implementation
- Add reviewed sources, add scoped claims, regenerate graph, update state.

### 4. Execute Implementation
- Added sources and claims in canonical CSVs.

### 5. Verify and Test
- Full inventory plus graph generation passed with 11 research sources and 5
  theory claims.

### 6. Self-Review
- Claims are explicitly scoped as theory support and not runtime proof.

### 7. Update Documentation and Knowledge
- Source-of-truth updates are part of the checkpoint.
