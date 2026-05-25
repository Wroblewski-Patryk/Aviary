# Task

## Header
- ID: PRJ-1286
- Title: Auth API graph gap closure
- Task Type: documentation
- Current Stage: verification
- Status: DONE
- Owner: Active chat coordinator
- Depends on: PRJ-1285
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-AUTH-001
- Requirement Rows: REQ-ARCH-1286
- Quality Scenario Rows: QA-MAINT-ARCH-GRAPH-1286
- Risk Rows: RISK-ARCH-GRAPH-1286
- Iteration: 1286
- Operation Mode: BUILDER
- Mission ID: PRJ-1286-auth-api-graph-gap-closure
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed through current graph mission state.
- [x] `.agents/core/mission-control.md` was reviewed through active mission contract.
- [x] Missing or template-like state tables were not blocking this narrow graph evidence slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence by aligning verified status with explicit graph proof.

## Mission Block
- Mission objective: remove `API-APP-AUTH` from the curated missing-proof queue by adding explicit relations, chain mapping, and evidence tied to focused auth API tests.
- Release objective advanced: authenticated app access traceability.
- Included slices: focused test proof, chain row, relation rows, evidence row, generated artifacts, state updates.
- Explicit exclusions: auth behavior changes, UI login redesign, production auth smoke, password policy redesign.
- Checkpoint cadence: one implementation and validation checkpoint.
- Stop conditions: focused auth tests fail, graph validation fails, or gap audit still reports `API-APP-AUTH` for missing evidence/chain after regeneration.
- Handoff expectation: future agents can trace auth from app shell to API/session/profile/test/docs.

## Context
The global gap audit reported `API-APP-AUTH` as a high-risk curated node with no evidence rows and no function chains, despite existing auth API pytest coverage.

## Goal
Add graph proof for the auth API boundary without changing application runtime behavior.

## Success Signal
- User or operator problem: verified graph nodes should not be trusted without explicit evidence and chain proof.
- Expected product or reliability outcome: auth API confidence is traceable in the graph.
- How success will be observed: focused auth tests pass, graph generation passes, and `API-APP-AUTH` is absent from the top gap report.
- Post-launch learning needed: no.

## Scope
- `docs/architecture/registry/chains.csv`
- `docs/architecture/registry/relations.csv`
- `docs/architecture/registry/evidence.csv`
- `backend/tests/test_architecture_graph_generator.py`
- generated graph artifacts
- state files touched by mission closure

## Implementation Plan
1. Run focused auth API tests to capture fresh proof.
2. Add auth relation rows for app shell calls, profile model persistence, API tests, and docs.
3. Add `CHAIN-APP-AUTH` mapping app shell -> auth API -> profile model -> tests -> docs.
4. Add auth evidence row.
5. Regenerate inventory and graph artifacts.
6. Run focused auth tests plus fast graph/query validation.
7. Update state files.

## Acceptance Criteria
- Focused auth API tests pass.
- `API-APP-AUTH` has an evidence row.
- `API-APP-AUTH` participates in a verified chain.
- Generated graph artifacts include the new chain/evidence.
- Gap audit no longer lists `API-APP-AUTH` in the top curated gap output.

## Definition of Done
- [x] focused auth API tests pass
- [x] auth chain/evidence/relations added
- [x] graph artifacts regenerated
- [x] fast graph validation passes
- [x] state docs updated

## Forbidden
- changing auth runtime behavior in this documentation/evidence task
- claiming production auth smoke without running it
- treating graph evidence as a substitute for security review

## Validation Evidence
- Tests:
  - focused auth API pytest PASS: `3 passed in 2.77s`
  - focused auth plus graph/query pytest PASS:
    `21 passed, 1 deselected in 71.18s`
- Manual checks:
  - graph generation PASS with `auto_nodes=5275`, `auto_relations=3967`,
    merged `nodes=5336`, `relations=4028`, `chains=8`, `evidence=23`,
    `research_sources=21`, `theory_claims=9`
  - node query for `API-APP-AUTH` reports `Gaps: none`
  - top curated gap audit no longer lists `API-APP-AUTH`
- Reality status: verified

## Result Report

- Task summary: closed the `API-APP-AUTH` graph gap with explicit relations, chain, and evidence.
- Files changed: graph registry CSVs, generated graph artifacts, graph generator test pins, state ledgers.
- How tested: focused auth pytest, graph generation, focused auth plus graph/query pytest, node query, gap audit.
- What is incomplete: production auth smoke and security review are separate scopes.
- Next steps: close the next high-risk curated gap from audit output.
