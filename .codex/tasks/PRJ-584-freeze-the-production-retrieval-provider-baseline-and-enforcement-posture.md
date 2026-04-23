# Task

## Header
- ID: PRJ-584
- Title: Freeze the production retrieval-provider baseline and enforcement posture
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-583
- Priority: P1

## Context
Production `/health.memory_retrieval` still reports
`retrieval_lifecycle_pending_gaps=["provider_baseline_not_aligned"]` while the
repo already exposes multiple provider postures:
`openai_api_embeddings` as the intended target,
`local_hybrid` as a transition owner, and deterministic execution as the
compatibility fallback. Before runtime alignment work proceeds, the repo needs
one explicit production answer about which provider baseline is final and how
strict provider or model or source-rollout enforcement should behave during the
alignment phase.

## Goal
Freeze one explicit production retrieval-provider baseline and the enforcement
posture that `PRJ-585..PRJ-586` must implement and then prove.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] one explicit target provider baseline is selected for production retrieval
- [x] transition and compatibility fallback postures are frozen without redefining the steady-state owner
- [x] provider, model, and source-rollout enforcement posture is recorded before runtime alignment work starts

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - architecture/runtime/ops cross-review only for this planning slice
- Manual checks:
  - production `GET /health` on 2026-04-23 shows:
    - `retrieval_lifecycle_target_provider_baseline=openai_api_embeddings`
    - `retrieval_lifecycle_transition_provider_baseline=local_hybrid`
    - `retrieval_lifecycle_pending_gaps=["provider_baseline_not_aligned"]`
    - `semantic_embedding_provider_effective=deterministic`
    - `semantic_embedding_production_baseline_state=deterministic_compatibility_baseline`
- Screenshots/logs:
  - canonical docs already describe `openai_api_embeddings` as the intended steady-state baseline and `local_hybrid` as transition-only posture
- High-risk checks:
  - no architecture change was made; this slice only freezes the existing intended production answer before implementation work continues

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/implementation/runtime-reality.md`
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/open-decisions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - planning/context sync only; runtime alignment remains for `PRJ-585..PRJ-587`

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
Frozen production answer for the next retrieval lane:

- steady-state provider baseline remains `openai_api_embeddings`
- `local_hybrid` remains a bounded transition owner, not the final production
  baseline
- deterministic execution remains the explicit compatibility fallback only
- provider, model, and source-rollout enforcement stays `warn` during
  `PRJ-585` so production can align without a premature hard fail
- `PRJ-586` should then make release and incident evidence strict against drift
  after live runtime alignment is complete
