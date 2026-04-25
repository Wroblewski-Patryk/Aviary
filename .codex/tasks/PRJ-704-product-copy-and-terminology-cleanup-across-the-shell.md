# Task

## Header
- ID: PRJ-704
- Title: Clean product-facing copy and remove system-language leakage
- Status: BACKLOG
- Owner: Frontend Builder
- Depends on: PRJ-703
- Priority: P0

## Context
Current UI copy still contains architecture-oriented terms such as `backend
truth`, `live contract`, endpoint references, and other internal framing that
belongs in docs or inspect mode rather than primary product surfaces.

## Goal
Replace system wording with user-facing product language across login, shell,
settings, tools, and personality surfaces while preserving truthful behavior.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Primary shell copy no longer references backend contracts or raw endpoints as user-facing value.
- [ ] Shared terminology across routes reads consistently as product copy.
- [ ] Any remaining technical detail is explicitly secondary or inspect-only.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `npm run build` in `web/`
- Manual checks: copy review across `/login`, `/chat`, `/settings`, `/tools`, and `/personality`
- Screenshots/logs: browser text proof in the refreshed audit artifact set
- High-risk checks: confirm product wording stays truthful and does not promise unsupported capability

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: n/a
- Follow-up architecture doc updates: none expected

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
The user-facing shell should describe outcomes, actions, and states rather than
internal implementation posture.
