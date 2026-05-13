# Task

## Header
- ID: PRJ-1187
- Title: Production OpenAI vector dimension alignment
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-1186
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-MEMORY-001
- Requirement Rows: REQ-AI-001
- Quality Scenario Rows: QA-AI-001
- Risk Rows: RISK-AI-001
- Iteration: 1187
- Operation Mode: BUILDER
- Mission ID: MIS-1187-production-vector-alignment
- Mission Status: VERIFIED

## Context
Production Aviary runs on Coolify/VPS with PostgreSQL pgvector and
`OPENAI_API_KEY` configured. A controlled production event proved that the API
can answer and write `aion_memory`, but OpenAI embedding persistence initially
failed because runtime requested 32-dimensional embeddings while the database
column is `vector(1536)`. After dimension alignment, production wrote 1536
dimensional vectors, but serialization of pgvector-returned array values still
used a truthiness check and marked the memory write as failed.

## Goal
Align the Coolify production embedding dimensions with the deployed pgvector
schema and serialize pgvector-returned arrays without boolean evaluation so
OpenAI provider-owned embeddings can be written, reported as successful, and
later retrieved.

## Constraints
- Touch only Aviary/Coolify resources, not other VPS applications.
- Preserve the existing pgvector `vector(1536)` schema.
- Keep local deterministic development defaults available.
- Validate locally and on production after deploy.

## Definition of Done
- [x] Coolify compose defaults `EMBEDDING_DIMENSIONS` to `1536`.
- [x] Tests cover the Coolify production default.
- [x] Repository serialization handles pgvector array values without
      truthiness checks.
- [x] Production deployment is updated.
- [x] Production event writes both `aion_memory` and `aion_semantic_embedding`.
- [x] Production health reports OpenAI embeddings with 1536 dimensions.

## Forbidden
- Do not reset or drop unrelated production data.
- Do not touch non-Aviary containers or Coolify projects.
- Do not disable semantic vector retrieval as a workaround.

## Result Report
- Summary:
  - deployed runtime memory-flow closure to Coolify production
  - aligned production OpenAI embeddings to `1536` dimensions
  - fixed pgvector array serialization so persisted OpenAI vectors do not mark
    memory writes as failed
- Production revisions:
  - first deploy: `978ce1c0ac73fb7e82f6c49e0087887393c371b2`
  - final fix deploy: `9252c9193219a374fd513287a022123fd0176715`
- Production proof:
  - `GET https://aviary.luckysparrow.ch/health` reported
    `semantic_embedding_dimensions=1536` and retrieval depth `6/5`
  - final write event trace:
    `prod-memory-flow-final-write-20260513`
  - final recall event trace:
    `prod-memory-flow-final-read-20260513`
  - reply to `Jak ma na imię mój pies?` contained `Roki`
  - DB proof for `prod-memory-flow-final-20260513`:
    `aion_memory=2`, `aion_semantic_embedding=2`, embedded rows `2`,
    dimensions `1536..1536`, model `text-embedding-3-small`
  - runtime log proof:
    `memory_write_status=stored`, `retrieved_recent_count=1`,
    `retrieved_memory_ids=['1099']`, `context_token_estimate=146`
- Local validation:
  - Coolify/config/API memory policy pack -> `13 passed`
  - pgvector serialization pack -> `3 passed`
  - full backend after first deploy commit -> `1077 passed`
  - full backend after serialization fix -> first run hit one transient local
    HTTP test connection abort, solo rerun passed, second full run -> `1078 passed`
- Residual:
  - production PostgreSQL still reports a database collation version mismatch;
    it did not block memory proof, but should be handled as a separate
    database maintenance task.
