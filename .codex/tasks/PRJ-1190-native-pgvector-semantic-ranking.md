# PRJ-1190 Native pgvector Semantic Ranking

## Header
- ID: PRJ-1190
- Title: Native pgvector semantic ranking for long-term memory retrieval
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-1189
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-MEMORY-001
- Requirement Rows: REQ-AI-001
- Quality Scenario Rows: QA-AI-001
- Risk Rows: RISK-AI-001
- Iteration: 1190
- Operation Mode: BUILDER
- Mission ID: PRJ-1190-native-pgvector-semantic-ranking
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] `.agents/core/mission-control.md` was reviewed through active repository instructions.
- [x] Missing or template-like state tables were bootstrapped from repository sources, or confirmed not needed.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task or mission improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: remove the small recent-candidate ceiling from semantic vector ranking so long-term memories can be retrieved by similarity at scale.
- Release objective advanced: AION memory continuity remains useful as stored memory grows.
- Included slices: repository ranking path, SQLite fallback hardening, regression tests, docs/state updates.
- Explicit exclusions: adding a new pgvector HNSW/IVFFLAT index migration.
- Checkpoint cadence: implement, targeted tests, full backend, production deploy proof.
- Stop conditions: failing memory retrieval tests, SQL syntax failure on production, or architecture mismatch.
- Handoff expectation: report ranking mode, tests, production status, and remaining indexing work.

## Context
PRJ-1189 proved that semantically matched episodic memories can enter runtime context. The remaining scale risk was that repository fallback ranking fetched a small latest-first candidate set before cosine scoring. On PostgreSQL/pgvector production, ranking should be delegated to the database operator across the filtered vector set.

## Goal
Use native PostgreSQL pgvector distance ranking for semantic similarity queries while preserving local SQLite/JSON fallback behavior.

## Scope
- `backend/app/memory/repository.py`
- `backend/tests/test_memory_repository.py`
- `docs/architecture/15_runtime_flow.md`
- `docs/implementation/runtime-reality.md`
- project state ledgers

## Implementation Plan
1. Add a PostgreSQL-specific semantic similarity path using `embedding <=> CAST(:query_embedding AS vector)`.
2. Keep the existing Python cosine fallback for SQLite/local dev, but widen its candidate pool enough to avoid the previous small-window failure.
3. Add regression coverage for old relevant vectors behind newer unrelated records.
4. Run targeted and full backend validation.
5. Deploy and run a production semantic recall proof after Coolify builds the commit.

## Acceptance Criteria
- PostgreSQL semantic queries are ordered by pgvector distance in SQL.
- SQLite/local fallback still returns the most similar older vector behind newer noise.
- Full backend test suite passes.
- Production `/health` stays green after deploy.

## Definition of Done
- [x] Existing memory systems are reused.
- [x] No alternate memory subsystem is introduced.
- [x] Regression tests cover the fixed candidate-window behavior.
- [x] Full backend validation passes.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_memory_repository.py -k "semantic_embeddings or expanded_candidates or postgres_vector_literal or vector_matched_episodic"; ...` -> `3 passed, 68 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "memory or hybrid or semantic or preference or pet or recent"; ...` -> `17 passed, 95 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; ...` -> `1082 passed`
- Manual checks: repository SQL and fallback paths reviewed.
- High-risk checks: vector literal rejects non-finite values before SQL execution.
- Module confidence ledger updated: yes
- Module confidence rows closed or changed: AVIARY-MEMORY-001
- Requirements matrix updated: yes
- Requirement rows closed or changed: REQ-AI-001
- Quality scenarios updated: yes
- Quality scenario rows closed or changed: QA-AI-001
- Risk register updated: yes
- Risk rows closed or changed: RISK-AI-001
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/architecture/15_runtime_flow.md`, `docs/architecture/26_env_and_config.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: `docs/architecture/15_runtime_flow.md`, `docs/implementation/runtime-reality.md`

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: production smoke should confirm semantic recall and `/health.memory_retrieval` OpenAI/pgvector posture.
- Rollback note: revert PRJ-1190 if production pgvector SQL fails; PRJ-1189 behavior remains the previous working retrieval path.
- Observability or alerting impact: existing runtime `memory_flow` remains the behavioral proof surface.
- Staged rollout or feature flag: existing `SEMANTIC_VECTOR_ENABLED`.

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
- [x] Docs or context were updated because repository truth changed.
- [x] Learning journal was not updated because no recurring pitfall was confirmed.

## Result Report
- Task summary: PostgreSQL semantic similarity now ranks with native pgvector distance; local fallback is widened and regression-tested.
- Files changed: memory repository, memory repository tests, runtime memory docs, project ledgers.
- How tested: targeted repository/runtime tests and full backend pytest.
- What is incomplete: index migration for ANN acceleration remains future hardening when memory volume requires it.
- Next steps: deploy and production-smoke the native pgvector ranking path.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: semantic ranking could miss old memories if they were not inside the latest-first candidate pool.
- Gaps: native pgvector operator path was not used by repository retrieval.
- Architecture constraints: keep existing memory tables and runtime context flow.

### 1a. Bootstrap Missing Project Knowledge
- Bootstrap needed: no
- Sources scanned: repository, tests, architecture docs, task board, ledgers.
- Rows created or corrected: PRJ-1190 task and memory evidence updates.
- Blocking unknowns: production SQL syntax must be verified after deploy.
- Why it was safe to continue: the change preserves fallback behavior and only switches PostgreSQL ranking to the database-native vector operator.

### 2. Select One Priority Mission Objective
- Selected task: native pgvector semantic ranking.
- Priority rationale: long-term digital-being memory must not become biased toward newest vectors only.
- Why other candidates were deferred: ANN index migration is a scale optimization after the query path is verified.

### 3. Plan Implementation
- Files or surfaces to modify: repository similarity query, tests, docs/state.
- Logic: detect PostgreSQL dialect and use `<=>`; otherwise use widened Python cosine candidate pool.
- Edge cases: empty embeddings, non-finite vector values, scope filters, source-kind filters.

### 4. Execute Implementation
- Implementation notes: added `_query_semantic_similarity_postgres` and `_postgres_vector_literal`.

### 5. Verify and Test
- Validation performed: targeted memory tests, runtime tests, full backend.
- Result: all local checks passed.

### 6. Self-Review
- Simpler option considered: only widen local candidate pool.
- Technical debt introduced: no
- Scalability assessment: database-side ranking is the right query path; ANN index remains future scale hardening.
- Refinements made: non-finite vector values fail closed to no vector query.

### 7. Update Documentation and Knowledge
- Docs updated: runtime flow and runtime reality.
- Context updated: task board, project state, ledgers.
- Learning journal updated: not applicable.
