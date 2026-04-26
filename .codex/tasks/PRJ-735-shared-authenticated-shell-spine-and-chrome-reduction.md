# Task

## Header
- ID: PRJ-735
- Title: Shared Authenticated Shell Spine And Chrome Reduction
- Task Type: design
- Current Stage: implementation
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-734
- Priority: P1

## Context
The canonical shell-convergence plan identified the parent authenticated shell
as too heavy and too dashboard-like for the approved `chat` route. The next
smallest useful implementation slice was to reduce shell chrome and rebalance
the `chat` route toward a calmer conversation-first composition before
attempting final parity proof.

## Goal
Implement the first convergence slice that reduces shell weight and moves the
`chat` route closer to the canonical premium conversation posture.

## Deliverable For This Stage
- shared authenticated shell styling updated in `web/src/`
- `chat` route composition updated so transcript remains primary while the
  right side becomes a calmer support column
- source-of-truth sync describing what now matches the canonical direction and
  what still remains for the next slices

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] The left authenticated shell rail is visually lighter and less dominant.
- [x] The `chat` route no longer foregrounds a large process rail beside the transcript.
- [x] The composer and support column are closer to the canonical calm editorial posture.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
- Manual checks:
  - reviewed the updated `chat` structure against
    `docs/ux/assets/aion-chat-canonical-reference-v2.png`
  - confirmed the slice reduced shell chrome and replaced the large
    `cognitive flow` module with a calmer support-column summary
- Screenshots/logs:
  - no new authenticated screenshot capture in this slice
  - parity screenshot capture remains explicitly queued in `PRJ-740` and `PRJ-741`
- High-risk checks:
  - ensured the route stayed backend-contract-driven and reused the existing web shell systems

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - none required

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-chat-canonical-reference-v2.png`
  - `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - embodied cognition motif
  - timeline-backed metadata
  - chat background artwork
- New shared pattern introduced: no
- Design-memory entry reused:
  - `docs/ux/design-memory.md`
- Design-memory update required: no
- State checks: success
- Responsive checks: desktop
- Input-mode checks: pointer | keyboard
- Accessibility checks:
  - no new regressions surfaced during implementation
  - full accessibility review remains queued in `PRJ-740`
- Parity evidence:
  - this slice materially improves:
    - lighter left shell framing
    - calmer right support column
    - more integrated composer zone
  - remaining drift:
    - chat controls are still a little busier than the canonical target
    - transcript cards are still more modular than the final reference
    - the route still needs final responsive and screenshot parity proof

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes:
  - none
- Health-check impact:
  - none
- Smoke steps updated:
  - none
- Rollback note:
  - revert `web/src/App.tsx` and `web/src/index.css`

## Review Checklist (mandatory)
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice intentionally stops before final parity claims. The remaining work
belongs to the next planned convergence slices rather than another ad hoc
styling pass.
