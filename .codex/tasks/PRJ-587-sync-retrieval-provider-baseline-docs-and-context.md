# Task

## Header
- ID: PRJ-587
- Title: Sync docs/context for retrieval-provider baseline
- Status: DONE
- Owner: Product Docs
- Depends on: PRJ-586
- Priority: P1

## Context
`PRJ-584..PRJ-586` froze the production retrieval baseline, aligned runtime to
OpenAI provider-owned embeddings, and made drift release-blocking. Canonical
docs and context needed to describe the same live truth and evidence path.

## Goal
Synchronize docs and repository context around the selected retrieval-provider
baseline, enforcement posture, and release-proof surfaces.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] runtime reality and ops docs describe the aligned OpenAI retrieval baseline
- [x] testing guidance points to the strict release-smoke and incident-evidence proof path
- [x] planning/context truth advances the queue to `PRJ-588`

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `.\scripts\run_release_smoke.ps1 -BaseUrl 'https://personality.luckysparrow.ch'` -> passed
- Manual checks:
  - canonical docs/context review after `PRJ-586`
- Screenshots/logs:
- High-risk checks:
  - docs no longer describe retrieval provider drift as an expected live warning posture

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/17_logging_and_debugging.md`
  - `docs/architecture/29_runtime_behavior_testing.md`
  - `docs/architecture/26_env_and_config.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - included in this task

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
This is a sync-only slice; runtime behavior changes remain owned by
`PRJ-585..PRJ-586`.
