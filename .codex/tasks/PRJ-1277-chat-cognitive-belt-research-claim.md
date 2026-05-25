# Task

## Header
- ID: PRJ-1277
- Title: Chat cognitive belt research claim
- Task Type: documentation
- Current Stage: verification
- Status: DONE
- Owner: Active chat / Coordinator
- Depends on: PRJ-1276
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-001
- Requirement Rows: REQ-ARCH-1268
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1268
- Risk Rows: RISK-ARCH-GRAPH-1268
- Iteration: 1277
- Operation Mode: BUILDER
- Mission ID: PRJ-1277-chat-cognitive-belt-research-claim
- Mission Status: VERIFIED

## Context

The graph system had research-backed runtime, memory, affect, motivation, and
role claims. The next checkpoint was to prove the workflow on one concrete
UX/UI node rather than adding broad abstract research claims.

## Goal

Promote the Chat cognitive belt into a curated graph node and attach a scoped
3-source neuroscience/cognitive-science theory claim about compact context,
working memory, visual working memory, and attentional load.

## Scope

- `docs/architecture/registry/nodes.csv`
- `docs/architecture/registry/ui_elements.csv`
- `docs/architecture/registry/relations.csv`
- `docs/architecture/registry/research_sources.csv`
- `docs/architecture/registry/theory_claims.csv`
- `docs/architecture/registry/evidence.csv`
- `backend/tests/test_architecture_graph_generator.py`
- generated graph artifacts and source-of-truth state updates

## Implementation Plan

1. Add a curated `UI-CHAT-COGNITIVE-BELT` node.
2. Link the node to app chat, the web shell, and route-smoke evidence.
3. Add three reviewed sources for working memory, visual working memory, and
   attentional load.
4. Add a scoped UX theory claim with explicit limitations.
5. Add evidence and tests so the claim appears in registry validation,
   evidence rollup, and research rollup.
6. Regenerate graph artifacts and update source-of-truth state.

## Acceptance Criteria

- The Chat cognitive belt has a stable graph node.
- The theory claim cites at least 3 reviewed sources.
- The claim limitations state that research support is not behavior proof.
- Generated node pages, graph JSON, evidence map, and research map include the
  new node/claim.
- Fast graph validation passes.

## Validation Evidence

- Source review:
  - Cowan 2001, Behavioral and Brain Sciences,
    `10.1017/S0140525X01003922`
  - Luck and Vogel 1997, Nature, `10.1038/36846`
  - Lavie 2005, Trends in Cognitive Sciences,
    `10.1016/j.tics.2004.12.004`
- `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Result:
  - `auto_nodes=5227`
  - `auto_relations=3931`
  - merged graph `nodes=5284`
  - merged graph `relations=3979`
  - curated function chains `chains=7`
  - curated evidence rows `evidence=14`
  - research sources `research_sources=21`
  - theory claims `theory_claims=9`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `8 passed, 1 deselected in 45.36s`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS, `9 passed in 255.06s`
- `Push-Location .\backend; ..\.venv\Scripts\python -m py_compile .\scripts\generate_architecture_inventory.py .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS

## Result Report

- Task summary: created the first concrete UX/UI research-backed graph claim
  for the Chat cognitive belt.
- Files changed: curated graph CSVs, typed UI view, generator pytest, generated
  graph artifacts, task/state files.
- How tested: source review, full graph generation, fast graph pytest, heavy
  graph pytest, and generator compile passed.
- What is incomplete: this is not a usability proof; screenshot and behavior
  evidence remain the proof layer for UI quality.
- Next steps: promote another critical auto-discovered feature chain into
  curated evidence, or add a UX claim only when a concrete node and sources are
  selected.

## Autonomous Loop Evidence

### 1. Analyze Current State
- `PRJ-1276` made graph validation practical; the next recommended checkpoint
  was a concrete UX/UI research claim.

### 2. Select One Priority Mission Objective
- Selected objective: map one real UI element to scoped research support.

### 3. Plan Implementation
- Add node, relations, sources, claim, evidence, tests, and generated outputs.

### 4. Execute Implementation
- Added `UI-CHAT-COGNITIVE-BELT`, 3 source rows, 1 theory claim, 3 relation
  rows, and 1 evidence row.

### 5. Verify and Test
- Fast graph pytest, generator compile, and full graph generation passed.

### 6. Self-Review
- The limitations explicitly prevent treating research support as runtime,
  accessibility, or usability proof.

### 7. Update Documentation and Knowledge
- Generated Obsidian node pages, graph JSON/Mermaid, evidence map, research
  map, task board, project state, and agent state files were updated.
