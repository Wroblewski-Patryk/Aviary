# Task

## Header
- ID: PRJ-1270
- Title: Affect motivation and role research claims
- Task Type: documentation
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1269
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1270
- Operation Mode: ARCHITECT
- Mission ID: PRJ-1270-affect-motivation-role-research-claims
- Mission Status: VERIFIED

## Context

`PRJ-1269` expanded research support for perception, planning, and
memory/reflection. The next source-review target was motivation, affective
state, and role selection. These were present in code and architecture docs but
not represented as curated graph nodes.

## Goal

Promote affective assessment, motivation, and role selection into curated
architecture graph nodes and attach scoped research-backed theory claims.

## Scope

- `docs/architecture/registry/nodes.csv`
- `docs/architecture/registry/relations.csv`
- `docs/architecture/registry/research_sources.csv`
- `docs/architecture/registry/theory_claims.csv`
- `docs/architecture/registry/evidence.csv`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Add curated nodes for affective assessment, motivation, and role selection.
2. Link those nodes to the runtime orchestrator through relation rows.
3. Add reviewed affective neuroscience, motivation/reward, and social
   cognition sources.
4. Add theory claims with at least 3 sources and explicit limitations.
5. Regenerate the architecture inventory and graph outputs.
6. Update project state and ledgers.

## Acceptance Criteria

- New nodes validate against the canonical node schema.
- New relations reference existing node IDs.
- New reviewed/mapped theory claims cite at least 3 sources.
- Generated research map includes affective, motivation, and role claims.
- Graph generation passes.
- Claims do not imply machine emotion, biological motivation, or social
  cognition.

## Validation Evidence

- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5205`
  - `auto_relations=3917`
  - merged graph `nodes=5261`
  - merged graph `relations=3962`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=12`
  - research sources `research_sources=18`
  - theory claims `theory_claims=8`

## Result Report

- Task summary: promoted affective assessment, motivation, and role selection
  into curated graph nodes with research-backed theory claims.
- Files changed: registry CSVs, generated graph artifacts, and project state
  files.
- How tested: full inventory plus graph generation passed.
- What is incomplete: UX-specific neuroscience claims remain future work and
  need separate source review.
- Next steps: add UX/cognitive-load/user-attention theory claims only if a
  concrete UI node and source set are selected.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Motivation, affective assessment, and role selection existed in code but not
  as curated graph nodes.

### 2. Select One Priority Mission Objective
- Selected objective: curated runtime-stage nodes plus research-backed claims.

### 3. Plan Implementation
- Add nodes, relations, source rows, theory claims, run generator, update state.

### 4. Execute Implementation
- Added canonical CSV rows for the selected runtime stages and claims.

### 5. Verify and Test
- Full inventory plus graph generation passed with 18 research sources and 8
  theory claims.

### 6. Self-Review
- Claims are scoped as software analogies and do not replace runtime tests.

### 7. Update Documentation and Knowledge
- Source-of-truth updates are part of this checkpoint.
