# Task

## Header
- ID: PRJ-585
- Title: Align production retrieval configuration and execution to the chosen provider baseline
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-584
- Priority: P1

## Context
`PRJ-584` froze `openai_api_embeddings` as the steady-state production retrieval
baseline, with `local_hybrid` as transition-only and deterministic as explicit
compatibility fallback. Live production still reports
`retrieval_lifecycle_pending_gaps=["provider_baseline_not_aligned"]` because
the runtime requests `deterministic` embeddings even though production already
has `OPENAI_API_KEY`.

## Goal
Make repository-driven production request and execute the approved OpenAI
retrieval baseline so `/health.memory_retrieval` stops reporting
`provider_baseline_not_aligned`.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] repository-driven Coolify production defaults request the OpenAI embedding provider baseline
- [x] regression coverage pins the production compose retrieval baseline
- [x] live production `/health.memory_retrieval` no longer reports `provider_baseline_not_aligned`

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\.venv\Scripts\python -m pytest -q tests/test_coolify_compose.py` -> `7 passed`
- Manual checks:
  - `docker compose -f docker-compose.coolify.yml config` -> OK
  - production `GET /health` now reports:
    - `memory_retrieval.semantic_embedding_provider_requested=openai`
    - `memory_retrieval.semantic_embedding_provider_effective=openai`
    - `memory_retrieval.semantic_embedding_model_requested=text-embedding-3-small`
    - `memory_retrieval.semantic_embedding_model_effective=text-embedding-3-small`
    - `memory_retrieval.semantic_embedding_execution_class=provider_owned_openai_api`
    - `memory_retrieval.semantic_embedding_production_baseline_state=aligned_openai_provider_owned`
    - `memory_retrieval.retrieval_lifecycle_provider_drift_state=aligned_target_provider`
    - `memory_retrieval.retrieval_lifecycle_alignment_state=aligned_with_defined_lifecycle_baseline`
    - `memory_retrieval.retrieval_lifecycle_pending_gaps=[]`
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` -> passed
- Screenshots/logs:
- High-risk checks:
  - explicit Coolify env overrides for embedding provider/model were absent, so repo-driven defaults now own the production retrieval baseline

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/26_env_and_config.md`
  - `docs/implementation/runtime-reality.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - docs/context sync completed in `PRJ-587`

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice should stay repo-driven through `docker-compose.coolify.yml` and
must not create a production-only side path outside the existing Coolify
baseline.
