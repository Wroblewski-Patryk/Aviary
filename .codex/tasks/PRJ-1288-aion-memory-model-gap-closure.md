# Task

## Header
- ID: PRJ-1288
- Title: AionMemory model graph gap closure
- Task Type: documentation
- Current Stage: verification
- Status: DONE
- Owner: Active chat coordinator
- Depends on: PRJ-1287
- Priority: P1
- Module Confidence Rows: AVIARY-ARCH-GRAPH-MEMORY-MODEL-001
- Requirement Rows: REQ-ARCH-1288
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1288
- Risk Rows: RISK-ARCH-GRAPH-1288
- Iteration: 1288
- Operation Mode: BUILDER
- Mission ID: PRJ-1288-aion-memory-model-gap-closure
- Mission Status: VERIFIED

## Mission Block
- Mission objective: remove `MODEL-AION-MEMORY` from the curated missing-proof queue by adding explicit model evidence and improving gap attribution for model nodes.
- Included slices: focused memory tests, evidence row, relation row, query-gap attribution refinement, generated artifacts, state updates.
- Explicit exclusions: memory behavior changes, schema changes, production memory smoke.

## Goal
Add graph proof for the AionMemory model and prevent unrelated feature-level missing links from making model nodes look unreliable.

## Acceptance Criteria
- Focused memory/model tests pass.
- `MODEL-AION-MEMORY` has an evidence row.
- Query for `MODEL-AION-MEMORY` reports `Gaps: none`.
- Fast graph validation passes.

## Validation Evidence
- Tests:
  - focused memory/model pytest PASS: `3 passed in 13.37s`
  - inventory plus graph generation PASS with `auto_nodes=5278`, `auto_relations=3968`, merged `nodes=5339`, `relations=4031`, `chains=9`, `evidence=25`, `research_sources=21`, `theory_claims=9`
  - memory/schema plus graph/query pytest PASS: `22 passed, 1 deselected in 20.58s`
- Manual checks:
  - `query_architecture_graph.py --node MODEL-AION-MEMORY --show-gaps` reports `EVID-AION-MEMORY-MODEL-PROOF` and `Gaps: none`
  - top curated gap audit no longer lists `MODEL-AION-MEMORY`
- Reality status: verified

## Result Report
- Task summary: Added explicit model proof for `MODEL-AION-MEMORY`, linked `TEST-MEMORY-REPOSITORY` through `REL-MEMORY-001`, and refined query gap attribution so feature-level future scope does not make model nodes look unreliable.
- Files changed: `backend/scripts/query_architecture_graph.py`; `backend/tests/test_architecture_graph_query.py`; `backend/tests/test_architecture_graph_generator.py`; `docs/architecture/registry/relations.csv`; `docs/architecture/registry/evidence.csv`; generated graph artifacts and state ledgers.
- How tested: focused memory/model pytest, full graph regeneration, focused graph/query pytest, node query smoke, global gap audit smoke.
- What is incomplete: production memory smoke remains a separate runtime/release proof scope.
- Next steps: close the next curated gap, likely `API-EVENT-INGRESS` or docs evidence nodes, before adding unrelated graph machinery.
