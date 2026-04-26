# Task

## Header
- ID: PRJ-764
- Title: Plan canonical multi-channel conversation and relational outreach
- Task Type: design
- Current Stage: planning
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-744
- Priority: P0

## Context
The user resolved the previously open decision around cross-channel posture.
The app chat is the canonical conversation surface and linked channels such as
Telegram should mirror that same continuity while proactive outreach remains
adaptive and relation-sensitive.

## Goal
Capture the approved architecture and produce one execution-ready plan for
canonical multi-channel conversation, mirrored delivery, and relational
outreach behavior.

## Deliverable For This Stage
Architecture updates plus one detailed implementation plan broken into task
groups and execution slices.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] architecture reflects canonical app-owned conversation plus linked-channel mirroring
- [x] transport adaptation rule is frozen for segmented Telegram delivery
- [x] the repo contains one execution-ready plan with detailed task groups

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
  - architecture/runtime/code cross-review
- Manual checks:
  - reviewed current channel and delivery code
  - reviewed current architecture and runtime docs
- Screenshots/logs:
  - n/a
- High-risk checks:
  - existing delivery router already supports ordered Telegram segmentation

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/11_event_contact.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/20_action_system.md`
  - `docs/architecture/23_proactive_system.md`
- Fits approved architecture: yes
- Mismatch discovered: yes
- Decision required from user: no
- Approval reference if architecture changed:
  - user answers captured in this conversation
- Follow-up architecture doc updates:
  - completed in the files above

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes:
  - none
- Health-check impact:
  - none
- Smoke steps updated:
  - not required at planning stage
- Rollback note:
  - revert docs and task planning if the product policy changes

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
The execution queue for this lane starts at `PRJ-750`.
