# Task

## Header
- ID: PRJ-1285
- Title: Architecture graph gap audit mode
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Active chat coordinator
- Depends on: PRJ-1284
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-GAP-AUDIT-001
- Requirement Rows: REQ-ARCH-1285
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1285
- Risk Rows: RISK-ARCH-GRAPH-1285
- Iteration: 1285
- Operation Mode: TESTER
- Mission ID: PRJ-1285-architecture-graph-gap-audit-mode
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed through current graph mission state.
- [x] `.agents/core/mission-control.md` was reviewed through active mission contract.
- [x] Missing or template-like state tables were not blocking this narrow graph-system slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence by making missing graph proof discoverable.

## Mission Block
- Mission objective: extend the graph query CLI with a global gap audit report for missing proof and incomplete chain signals.
- Release objective advanced: architecture graph operational auditing and agent systemic planning.
- Included slices: CLI mode, focused tests, evidence/docs, generated artifacts, state updates.
- Explicit exclusions: fixing every reported gap, hosted CI proof, interactive graph UI, new research claims.
- Checkpoint cadence: one implementation and validation checkpoint.
- Stop conditions: graph validation fails, generated artifacts drift, or audit mode overclaims auto-inventory rows as curated release defects.
- Handoff expectation: future agents can run `--gaps` to select the next missing-proof target.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `.agents/state/active-mission.md` | Integration, task closure, memory updates | Bounded mission | Final validation gate | DONE |
| Backend/Ops | Active chat | `backend/scripts/query_architecture_graph.py` | CLI behavior | `--gaps` mode | Focused pytest and smoke | DONE |
| QA/Test | Active chat | existing query tests | `backend/tests/test_architecture_graph_query.py` | gap report tests | pytest PASS | DONE |
| Architecture/Docs | Active chat | `docs/architecture/graph-system.md` | docs/evidence/generated artifacts | audit workflow mapped | generator validation | DONE |

## Context
`PRJ-1284` added a single-node graph query CLI. Agents now need a whole-graph missing-proof report to avoid guessing the next evidence target.

## Goal
Add `--gaps` mode that reports nodes with missing evidence, tests, docs, incomplete chains, or unresolved research support, excluding auto-inventory rows by default.

## Success Signal
- User or operator problem: agents need a system-level queue of graph gaps.
- Expected product or reliability outcome: missing proof becomes discoverable before feature-confidence work starts.
- How success will be observed: tests and CLI smoke show a gap report from generated graph JSON.
- Post-launch learning needed: no.

## Scope
- `backend/scripts/query_architecture_graph.py`
- `backend/tests/test_architecture_graph_query.py`
- `docs/architecture/registry/evidence.csv`
- `docs/architecture/graph-system.md`
- generated graph/node/status/testing artifacts
- state files touched by mission closure

## Implementation Plan
1. Add a mutually exclusive `--gaps` CLI mode.
2. Build a gap report from existing `query_node` and `detect_gaps` helpers.
3. Exclude `#auto` nodes by default; add `--include-auto` for broad inventory inspection.
4. Render markdown and JSON gap reports.
5. Add focused tests and smoke commands.
6. Regenerate graph artifacts and update state.

## Acceptance Criteria
- `--gaps` returns non-empty markdown/json reports from a graph with missing proof.
- Default gap report excludes auto-inventory rows.
- `--include-auto` can include auto rows.
- Existing `--node` and `--search` behavior remains green.
- Evidence/docs/generated artifacts are refreshed.

## Definition of Done
- [x] gap audit mode implemented
- [x] focused tests pass
- [x] graph artifacts regenerated
- [x] fast graph validation passes
- [x] source-of-truth state updated

## Forbidden
- treating auto-inventory rows as release-critical defects by default
- replacing CSV as source of truth
- creating an unrelated graph UI
- fixing unrelated feature gaps in this audit-mode task

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
  - PASS: `18 passed, 1 deselected in 3.39s`
- Manual checks:
  - graph generation PASS with `auto_nodes=5274`, `auto_relations=3967`,
    merged `nodes=5335`, `relations=4024`, `chains=7`, `evidence=22`,
    `research_sources=21`, `theory_claims=9`
  - CLI gap JSON smoke PASS with `--gaps --limit 5 --format json`
  - generated evidence map/node page/graph JSON include
    `EVID-ARCH-GRAPH-GAP-AUDIT`
- Reality status: verified

## Result Report

- Task summary: added a global curated missing-proof audit mode to the graph query CLI.
- Files changed: `backend/scripts/query_architecture_graph.py`, `backend/tests/test_architecture_graph_query.py`, `docs/architecture/registry/evidence.csv`, `docs/architecture/graph-system.md`, generated graph artifacts, and state ledgers.
- How tested: focused query plus fast graph pytest PASS; graph generation PASS; CLI gap JSON smoke PASS.
- What is incomplete: fixing the reported gaps and building an interactive graph UI remain separate tasks.
- Next steps: choose the next high-risk curated gap from audit output and close it with evidence/chain work.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: single-node query exists, but whole-graph missing-proof queue does not.
- Gaps: agents still need to manually choose suspected nodes before seeing gaps.
- Architecture constraints: CSV remains canonical; generated JSON is a read model.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1285 graph gap audit mode.
- Priority rationale: closes the next operational gap after query CLI.

### 3. Plan Implementation
- Files or surfaces to modify: listed in Scope.
- Logic: reuse existing query/gap helpers, add report rendering and CLI mode.
- Edge cases: auto inventory exclusion, empty reports, limit handling.

### 4. Execute Implementation
- Implementation notes: reused query/gap helpers, added report rendering, `--gaps`, `--include-auto`, and default auto-row exclusion.

### 5. Verify and Test
- Validation performed: focused pytest, graph generation, fast graph pytest, CLI gap JSON smoke, generated evidence inclusion check.
- Result: verified.

### 6. Self-Review
- Technical debt introduced: no
- Refinements made: gap audit sorts high-risk curated gaps ahead of lower-risk items and leaves auto rows opt-in.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/architecture/graph-system.md` and generated graph docs.
- Context updated: active mission, task board, project state, next steps, system health, module confidence, requirement matrix, quality scenarios, risk register, project memory index.
