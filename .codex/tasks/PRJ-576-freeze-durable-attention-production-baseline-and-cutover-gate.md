# Task

## Header
- ID: PRJ-576
- Title: Freeze the durable-attention production baseline and cutover gate
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-575
- Priority: P0

## Context
Post-v1 production now runs deferred reflection and externalized scheduler
cadence, but live `/health.attention` still reports
`coordination_mode=in_process` and `contract_store_mode=in_process_only`.
Repository-backed durable attention is already implemented and health says
deployment readiness is green, so the next small slice is to freeze one
explicit production cutover gate before switching production defaults.

## Goal
Record one explicit durable-attention production baseline that defines the
selected target owner, cutover proof surfaces, and rollback posture.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] one explicit decision records durable inbox as the target production
      attention owner
- [x] cutover proof surfaces and required green signals are frozen in planning,
      context, and ops truth
- [x] rollback posture is explicit before the production switch task begins

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - none; planning and contract-freezing slice
- Manual checks:
  - reviewed `docs/architecture/16_agent_contracts.md`
  - reviewed `docs/implementation/runtime-reality.md`
  - reviewed `docs/operations/runtime-ops-runbook.md`
  - reviewed live `GET https://personality.luckysparrow.ch/health`
- Screenshots/logs:
  - live `/health.attention` shows:
    - `coordination_mode=in_process`
    - `deployment_readiness.ready=true`
    - `blocking_signals=[]`
    - `contract_store_mode=in_process_only`
- High-risk checks:
  - confirmed reflection and cadence are already externalized before seeding the
    durable-attention production switch
  - confirmed Telegram round-trip remains healthy while attention is still in
    `in_process`

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - durable-attention production switch gate is now explicit in planning and ops
    truth before `PRJ-577`

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
Frozen durable-attention production gate:

- target owner:
  - `ATTENTION_COORDINATION_MODE=durable_inbox`
- cutover proof surfaces:
  - `GET /health.attention`
  - `GET /health.runtime_topology.attention_switch`
  - `GET /health.conversation_channels.telegram`
  - release smoke
- required green signals before and after the switch:
  - `attention.deployment_readiness.ready=true`
  - `attention.deployment_readiness.blocking_signals=[]`
  - `attention.contract_store_mode=repository_backed_durable_inbox`
  - `attention.deployment_readiness.contract_store_state=repository_backed_durable_inbox`
  - Telegram round-trip remains `provider_backed_ready`
  - no duplicate-reply or burst-assembly regressions are observed in the smoke
    path
- rollback posture:
  - return production to `ATTENTION_COORDINATION_MODE=in_process`
  - treat `in_process` as the safe rollback baseline until burst claim, cleanup,
    or reply-order semantics are stable again
