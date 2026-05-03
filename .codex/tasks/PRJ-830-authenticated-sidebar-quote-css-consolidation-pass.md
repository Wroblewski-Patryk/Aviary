# Task

## Header
- ID: PRJ-830
- Title: Authenticated sidebar quote CSS consolidation pass
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-829
- Priority: P1

## Context
The authenticated sidebar has already received multiple exactness slices. The
quote closure still contains an older overridden CSS block with mojibake-era
values above the final canonical overrides.

## Goal
Consolidate the sidebar quote styles into one canonical block so the rail stays
easier to maintain and safer for final parity tuning.

## Success Signal
- User or operator problem:
  - the quote closure still carries duplicated CSS with stale encoded literals
- Expected product or reliability outcome:
  - cleaner and more trustworthy sidebar implementation before proof
- How success will be observed:
  - quote styles live in one stable block without contradictory earlier values
- Post-launch learning needed: no

## Deliverable For This Stage
A bounded sidebar-only CSS consolidation pass plus synced task/context notes.

## Scope
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Remove the stale earlier quote-card CSS block.
2. Keep only the canonical final quote styles.
3. Run focused validation and sync context.

## Acceptance Criteria
- sidebar quote styles are defined once
- no stale mojibake-era content literals remain in the live quote block
- focused validation passes

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] Quote CSS is consolidated into one live block.
- [x] Context is synced.
- [x] Focused validation evidence is attached.

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
  - verified that the sidebar quote closure now has one canonical CSS block
    instead of an older overridden duplicate
- Screenshots/logs:
  - deploy-side sidebar proof still pending
- High-risk checks:
  - `git diff --check -- web/src/index.css .codex/tasks/PRJ-830-authenticated-sidebar-quote-css-consolidation-pass.md`

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/planning/sidebar-layout-canonical-convergence-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aviary-sidebar-layout-canonical-reference-v1.png`
- Canonical visual target: authenticated desktop sidebar quote closure
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: authenticated sidebar quote closure
- New shared pattern introduced: no
- Design-memory entry reused: sidebar canonical rail contract
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: existing shell assets only
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop
- Input-mode checks: pointer
- Accessibility checks: not in this bounded slice
- Parity evidence:

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert bounded CSS consolidation slice
- Observability or alerting impact: none
- Staged rollout or feature flag: no

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
- [x] Learning journal update was not required; no new recurring pitfall was
  confirmed in this closure sync.

## Notes
This slice is implementation cleanup within the active sidebar surface, not a
new visual direction.

## Closure Sync - 2026-05-03

- Current release status:
  - DONE as a historical authenticated-sidebar quote CSS consolidation slice.
- Current source truth:
  - `web/src/App.tsx` keeps the sidebar quote card on
    `aion-sidebar-quote-*` hooks.
  - `web/src/index.css` keeps one canonical live quote block with stable
    punctuation content and final spacing values.
- Superseding proof owners:
  - `PRJ-868` canonical layout foundation.
  - `PRJ-875` canonical UI final route sweep.
  - `docs/ux/flagship-baseline-transfer.md`.
- Closure evidence:
  - reviewed this task history, current sidebar quote source, design memory,
    flagship baseline transfer, and later project/board proof.
  - no runtime files were changed by this closure sync.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. Partial implementations, mock-only
paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: authenticated desktop users
- Existing workaround or pain: duplicated quote CSS risks future drift
- Smallest useful slice: quote-closure CSS consolidation
- Success metric or signal: one stable live quote block remains
- Feature flag, staged rollout, or disable path: no
- Post-launch feedback or metric check: deploy-side sidebar proof

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated shell opening
- SLI: visual parity only
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: `npm run build`
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: sidebar CSS diff
- Rollback or disable path: revert slice

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused shell/sidebar diff

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: not applicable
- Trust boundaries: not applicable
- Permission or ownership checks: not applicable
- Abuse cases: not applicable
- Secret handling: none
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: low

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios:
- Multi-step context scenarios:
- Adversarial or role-break scenarios:
- Prompt injection checks:
- Data leakage and unauthorized access checks:
- Result:

## Result Report

- Task summary:
  - consolidated the sidebar quote closure CSS into one live canonical block
- Files changed:
  - `web/src/index.css`
  - `.codex/tasks/PRJ-830-authenticated-sidebar-quote-css-consolidation-pass.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/index.css .codex/tasks/PRJ-830-authenticated-sidebar-quote-css-consolidation-pass.md`
- What is incomplete:
  - deploy-side sidebar proof still decides whether the sidebar lane is ready
    to close
- Next steps:
  - compare deployed sidebar against the canonical rail
  - if parity clears, move to the `dashboard` surface group
- Decisions made:
  - kept this slice as implementation cleanup within the active sidebar lane
