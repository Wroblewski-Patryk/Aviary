# Task

## Header
- ID: PRJ-1187
- Title: Production OpenAI vector dimension alignment
- Task Type: fix
- Current Stage: implementation
- Status: IN_PROGRESS
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
- Mission Status: IN_PROGRESS

## Context
Production Aviary runs on Coolify/VPS with PostgreSQL pgvector and
`OPENAI_API_KEY` configured. A controlled production event proved that the API
can answer and write `aion_memory`, but OpenAI embedding persistence failed
because runtime requested 32-dimensional embeddings while the database column is
`vector(1536)`.

## Goal
Align the Coolify production embedding dimensions with the deployed pgvector
schema so OpenAI provider-owned embeddings can be written and later retrieved.

## Constraints
- Touch only Aviary/Coolify resources, not other VPS applications.
- Preserve the existing pgvector `vector(1536)` schema.
- Keep local deterministic development defaults available.
- Validate locally and on production after deploy.

## Definition of Done
- [ ] Coolify compose defaults `EMBEDDING_DIMENSIONS` to `1536`.
- [ ] Tests cover the Coolify production default.
- [ ] Production deployment is updated.
- [ ] Production event writes both `aion_memory` and `aion_semantic_embedding`.
- [ ] Production health reports OpenAI embeddings with 1536 dimensions.

## Forbidden
- Do not reset or drop unrelated production data.
- Do not touch non-Aviary containers or Coolify projects.
- Do not disable semantic vector retrieval as a workaround.

## Result Report
- Pending.
