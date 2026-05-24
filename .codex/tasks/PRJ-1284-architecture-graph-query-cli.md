# Task

## Header
- ID: PRJ-1284
- Title: Architecture graph query CLI
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Active chat coordinator
- Depends on: PRJ-1282, PRJ-1283
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-QUERY-001
- Requirement Rows: REQ-ARCH-1284
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1284
- Risk Rows: RISK-ARCH-GRAPH-1284
- Iteration: 1284
- Operation Mode: BUILDER
- Mission ID: PRJ-1284-architecture-graph-query-cli
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
- [x] The task improves release confidence by making graph evidence queryable by agents.

## Mission Block
- Mission objective: add a local CLI over `architecture-graph.json` that lets an agent query a node or search term and see impact, chains, evidence, research claims, and proof gaps.
- Release objective advanced: architecture graph operational usability and systemic agent analysis.
- Included slices: query script, focused tests, graph registry rows, generated artifacts, state updates.
- Explicit exclusions: hosted CI execution proof, interactive graph UI, new neuroscience claims, production runtime smoke.
- Checkpoint cadence: one implementation and validation checkpoint.
- Stop conditions: graph validation fails, generated artifacts drift, or registry references become invalid.
- Handoff expectation: future agents can run the query CLI before answering "does this function work".

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `.agents/state/active-mission.md` | Integration, task closure, memory updates | Mission remains bounded | Final validation gate | DONE |
| Architecture | Active chat | `docs/architecture/graph-system.md` | Graph-system docs and registry rows | Query workflow mapped into graph contract | Generator validation | DONE |
| Backend/Ops | Active chat | existing scripts | `backend/scripts/query_architecture_graph.py` | Importable CLI over generated graph JSON | Focused pytest and CLI smoke | DONE |
| QA/Test | Active chat | graph pytest pattern | `backend/tests/test_architecture_graph_query.py` | Query behavior tests | pytest PASS | DONE |
| Security/Ops/Docs | Active chat | graph docs/state | state docs and evidence rows | No secrets/runtime side effects | diff/check evidence | DONE |

### Lane Checks

- [x] `.agents/state/active-mission.md` was refreshed.
- [x] `.agents/workflows/responsibility-lanes.md` ownership model was followed from AGENTS.md.
- [x] Every important responsibility has an owner or explicit omission.
- [x] No delegated write lanes overlap.
- [x] Subagents were not used because the slice is tightly coupled and small.
- [x] Missing ownership/evidence/context gaps will be recorded if discovered.

## Context
The architecture graph foundation, inventory generation, CI policy, and PR checklist exist. Agents still need a direct local way to query a node and see the systemic context required by the graph-system analysis rule.

## Goal
Create a query tool that reads the generated architecture graph export and reports node details, incoming/outgoing relations, chains, evidence, research claims, and missing proof gaps.

## Success Signal
- User or operator problem: agents need fast systemic graph lookup instead of local file-only reasoning.
- Expected product or reliability outcome: graph evidence becomes easier to use during feature checks and impact analysis.
- How success will be observed: focused tests and a CLI smoke command produce systemic graph output for a known node.
- Post-launch learning needed: no.

## Deliverable For This Stage
Implementation plus validation for the query CLI and graph registry integration.

## Scope
- `backend/scripts/query_architecture_graph.py`
- `backend/tests/test_architecture_graph_query.py`
- `backend/tests/test_architecture_graph_generator.py`
- `docs/architecture/registry/nodes.csv`
- `docs/architecture/registry/tests.csv`
- `docs/architecture/registry/relations.csv`
- `docs/architecture/registry/evidence.csv`
- `docs/architecture/graph-system.md`
- generated graph/node/status/testing artifacts
- state files touched by mission closure

## Implementation Plan
1. Add importable query helpers and CLI options for `--node`, `--search`, `--show-gaps`, and `--format markdown|json`.
2. Add tests for exact node lookup, search, relation impact, chains, evidence, theory claims, and gap detection.
3. Add graph nodes, relations, test view row, and evidence row for the new query utility.
4. Regenerate inventory and graph artifacts.
5. Run focused query tests and fast graph validation.
6. Update architecture docs and state ledgers with verified results.

## Acceptance Criteria
- CLI returns markdown and JSON for a known node.
- CLI search finds relevant nodes.
- Query result includes incoming/outgoing relations, chains, evidence, theory claims, and gaps.
- Missing node requests fail with suggestions.
- New script/test/evidence are represented in the architecture graph.
- Fast graph pytest gate passes.

## Constraints
- use existing graph export and registry structures
- do not create a parallel source of truth
- do not introduce runtime side effects
- do not overstate research evidence as runtime proof

## Definition of Done
- [x] query CLI implemented and importable
- [x] focused query tests pass
- [x] graph registry and generated artifacts include the CLI/test/evidence
- [x] fast graph validation passes
- [x] source-of-truth state files updated

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated graph source of truth
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_query.py tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
  - PASS: `14 passed, 1 deselected in 2.94s`
- Manual checks:
  - graph generation PASS with `auto_nodes=5267`, `auto_relations=3961`,
    merged `nodes=5328`, `relations=4018`, `chains=7`, `evidence=21`,
    `research_sources=21`, `theory_claims=9`
  - CLI node smoke PASS for `WORKFLOW-ARCH-GRAPH --show-gaps`
  - CLI search smoke PASS for `query --limit 5 --format json`
  - generated graph JSON, evidence map, and node page include query CLI rows
- Screenshots/logs: not applicable
- High-risk checks: no runtime side effects or secrets involved
- Coverage ledger updated: not applicable
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: `AVIARY-ARCH-GRAPH-QUERY-001`
- Requirements matrix updated: yes
- Requirement rows closed or changed: `REQ-ARCH-1284`
- Quality scenarios updated: yes
- Quality scenario rows closed or changed: `QA-MAINT-ARCH-GRAPH-1284`
- Risk register updated: yes
- Risk rows closed or changed: `RISK-ARCH-GRAPH-1284`
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/architecture/graph-system.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: user requested continued implementation of graph/evidence system
- Follow-up architecture doc updates: query workflow section

## UX/UI Evidence
- Design source type: not applicable
- Screenshot comparison pass completed: not applicable

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: local CLI smoke only
- Rollback note: remove CLI/test/registry rows and regenerate graph artifacts
- Observability or alerting impact: none

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Assumption: `architecture-graph.json` remains the generated read model for query use; CSV remains canonical source of truth.

## Result Report

- Task summary: added a read-only graph query CLI for node/search impact, chains, evidence, theory claims, and gap detection.
- Files changed: `backend/scripts/query_architecture_graph.py`, `backend/tests/test_architecture_graph_query.py`, graph registry CSVs, generated graph artifacts, graph-system docs, and state ledgers.
- How tested: focused query plus fast graph pytest PASS with `14 passed, 1 deselected in 2.94s`; graph generation PASS; CLI node/search smokes PASS; `git diff --check` PASS with LF/CRLF warnings only.
- What is incomplete: hosted CI first-run proof and an interactive graph UI remain separate future slices.
- Next steps: use the CLI before future mapped feature checks; hosted graph CI proof is optional supplementary evidence under `DEC-005` when available.
- Decisions made: use generated `architecture-graph.json` as the read model while keeping CSV as canonical source of truth.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: graph is generated and validated but not directly queryable from CLI.
- Gaps: agent workflow still relies on manual CSV/JSON inspection for impact analysis.
- Inconsistencies: none found.
- Architecture constraints: CSV remains source of truth; generated JSON is a read model.

### 1a. Bootstrap Missing Project Knowledge
- Bootstrap needed: no
- Sources scanned: active mission, task board, graph-system doc, registry snippets, generator tests.
- Assumptions recorded: query utility reads generated graph export only.
- Blocking unknowns: none.
- Why it was safe to continue: user asked to keep implementing the graph/evidence system, and this is a narrow approved extension.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1284 architecture graph query CLI.
- Priority rationale: turns the graph into an operational agent tool after CI and PR checklist foundations.
- Why other candidates were deferred: hosted Actions proof requires push; new chains need a concrete release-critical module selection.

### 3. Plan Implementation
- Files or surfaces to modify: listed in Scope.
- Logic: load graph JSON, build indices, query node/search, compute impact and gaps, render markdown/json.
- Edge cases: missing graph file, missing node, empty evidence, empty tests/docs links, unknown search term.

### 4. Execute Implementation
- Implementation notes: implemented importable query helpers, markdown/json CLI rendering, curated-first search ranking, missing-node suggestions, and proof-gap detection.

### 5. Verify and Test
- Validation performed: graph generation, focused pytest, CLI node/search smoke, generated artifact inclusion checks, and `git diff --check`.
- Result: verified.

### 6. Self-Review
- Simpler option considered: manual JSON grep, rejected because it does not satisfy systemic agent workflow.
- Technical debt introduced: no
- Scalability assessment: local read-only query scales with generated JSON; future UI can reuse the same export.
- Refinements made: search ranking now prioritizes curated registry rows before auto-inventory rows.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/architecture/graph-system.md` and generated graph docs.
- Context updated: active mission, task board, project state, next steps, system health, delivery map, module confidence, requirement matrix, quality scenarios, risk register, project memory index.
- Learning journal updated: not applicable
