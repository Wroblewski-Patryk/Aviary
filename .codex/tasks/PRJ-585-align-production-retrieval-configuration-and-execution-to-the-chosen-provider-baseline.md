# Task

## Header
- ID: PRJ-585
- Title: Align production retrieval configuration and execution to the chosen provider baseline
- Status: IN_PROGRESS
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
- [ ] repository-driven Coolify production defaults request the OpenAI embedding provider baseline
- [ ] regression coverage pins the production compose retrieval baseline
- [ ] live production `/health.memory_retrieval` no longer reports `provider_baseline_not_aligned`

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
- Screenshots/logs:
- High-risk checks:

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
- Fits approved architecture: yes | no
- Mismatch discovered: yes | no
- Decision required from user: yes | no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## Review Checklist (mandatory)
- [ ] Architecture alignment confirmed.
- [ ] Existing systems were reused where applicable.
- [ ] No workaround paths were introduced.
- [ ] No logic duplication was introduced.
- [ ] Definition of Done evidence is attached.
- [ ] Relevant validations were run.
- [ ] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice should stay repo-driven through `docker-compose.coolify.yml` and
must not create a production-only side path outside the existing Coolify
baseline.
