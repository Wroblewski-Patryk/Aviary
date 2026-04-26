# Task

## Header
- ID: PRJ-742
- Title: Add Dashboard Route And Canonical Flagship Shell
- Task Type: design
- Current Stage: verification
- Status: COMPLETE
- Owner: Frontend Builder
- Depends on: PRJ-739
- Priority: P0

## Context
The approved canonical screen set includes one flagship authenticated
`dashboard` route, but the current product shell still enters directly into
`/chat`. The route family is visually stronger than before, yet the app still
lacks the canonical overview surface that should sit before `chat`,
`personality`, `tools`, and `settings`.

## Goal
Add a real `/dashboard` route as the first authenticated screen and push the
shared shell, `dashboard`, `chat`, and `personality` closer to the approved
canonical route references.

## Deliverable For This Stage
- authenticated `/dashboard` route in `web/src/`
- route insertion into shell navigation, default routing, and mobile nav
- dashboard composition built from existing shared motifs and backend-owned
  data already available to the web shell
- source-of-truth sync recording the new flagship route baseline

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `/dashboard` exists as a first-class authenticated route.
- [x] login and shell entry now land on `dashboard` instead of entering
      directly into `chat`.
- [x] `dashboard`, `chat`, and `personality` all move visibly closer to the
      canonical route family.

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
  - reviewed `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
  - verified route contract now defaults authenticated entry to `/dashboard`
- Screenshots/logs:
  - local visual proof still needs a dedicated screenshot pass on live data
- High-risk checks:
  - reused existing overview, tools, transcript, and shell primitives instead
    of creating a parallel dashboard system

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
  - none expected beyond planning and context sync

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
  - `docs/ux/assets/aion-chat-canonical-reference-v2.png`
  - `docs/ux/assets/aion-personality-canonical-reference-v1.png`
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - flagship utility bar
  - embodied cognition motif
  - integrated composer tray
- New shared pattern introduced: yes
- Design-memory entry reused:
  - `docs/ux/design-memory.md`
- Design-memory update required: yes
- State checks: loading | empty | success
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: pointer | keyboard | touch
- Accessibility checks:
  - keep route hierarchy readable without relying on illustration only
- Parity evidence:
  - route convergence still needs a later screenshot-proof slice after local
    implementation

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes:
  - none
- Health-check impact:
  - none
- Smoke steps updated:
  - none
- Rollback note:
  - revert `web/src/` route and shell changes

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
This slice adds the missing flagship route without adding a new backend
contract. The implementation reuses existing web-loaded overview,
history, tools, and account data so the dashboard remains one more shell
surface rather than a new system.
