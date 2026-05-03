# Task

## Header
- ID: PRJ-822
- Title: Home Header And Proof Iconography Pass
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-820
- Priority: P1

## Context
The public `home` hero is structurally close, but the top header actions and
micro-proof row still read slightly too placeholder-like compared with the
canonical flagship feel.

## Goal
Make the first viewport calmer and richer by replacing dot-only proof markers
with real iconography and by softening the header action posture.

## Success Signal
- User or operator problem:
  - the top of `home` still carries a bit too much generic-web rhythm
- Expected product or reliability outcome:
  - first viewport feels more premium and more obviously intentional
- How success will be observed:
  - micro-proof row and header controls read closer to the canonical home
    reference after the slice
- Post-launch learning needed: no

## Deliverable For This Stage
A bounded `home`-only UI slice touching the public hero overlay and related
styles.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Replace the micro-proof dot treatment with real semantic icons from the
   existing public glyph system.
2. Slightly soften the public header link and button rhythm.
3. Tighten hero body and CTA spacing to keep the first viewport calmer.
4. Run focused validation and sync context.

## Acceptance Criteria
- micro-proof items use iconography, not only dots
- header controls feel calmer and less generic
- no scope leaks into dashboard/chat/personality
- focused validation passes

## Definition of Done
- [x] micro-proof row is upgraded
- [x] header and hero rhythm are refined
- [x] task board and project state are synced
- [x] focused validation evidence is attached

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
  - reviewed the landing hero overlay and micro-proof anatomy against the
    current canonical home interpretation
- Screenshots/logs:
  - production proof still pending after deploy
- High-risk checks:
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-822-home-header-and-proof-iconography-pass.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/ux/canonical-visual-implementation-workflow.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-landing-canonical-reference-v1.png`
- Canonical visual target: `home`
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: public glyph set and full-bleed landing shell
- New shared pattern introduced: no
- Design-memory entry reused: yes
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: reuse current landing art
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: deploy-side proof still needed
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
- Rollback note: revert bounded home-only style slice
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
This slice stays on the first viewport only.

## Closure Sync - 2026-05-03

- Current release status:
  - DONE as a historical public-home first-viewport iconography and header
    rhythm slice.
- Current source truth:
  - `web/src/App.tsx` renders the public micro-proof row with
    `aion-public-micro-proof-icon` and `PublicGlyph`.
  - `web/src/index.css` keeps the route-local public nav, micro-proof, hero
    body, and CTA rhythm refinements from this slice.
- Superseding proof owners:
  - `PRJ-869` public home landing `99%` canonical pass.
  - `PRJ-875` canonical UI final route sweep.
  - `PRJ-782` shell-frame decision resolution.
- Browser/mockup note:
  - canonical screenshot browser frames are presentation context only.
  - product UI must not simulate browser controls, title bars, or fake window
    chrome.
- Closure evidence:
  - reviewed this task history, current public landing source, design memory,
    user clarification, and later project/board proof.
  - `Select-String -Path web\src\App.tsx,web\src\index.css -Pattern
    "aion-public-browser|WindowChrome|aion-window-chrome"` returned no
    matches in the current source.
  - no runtime files were changed by this closure sync.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
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
- User or operator affected: public visitors
- Existing workaround or pain: micro-proof row still reads too placeholder-like
- Smallest useful slice: iconography and header posture pass
- Success metric or signal: calmer and richer first viewport read
- Feature flag, staged rollout, or disable path: no
- Post-launch feedback or metric check: visual deploy check

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: landing first impression
- SLI: visual parity only
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: `Push-Location .\web; npm run build; Pop-Location`
- Rollback or disable path: revert the bounded slice

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused build and diff validation

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: none
- Trust boundaries: unchanged
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
  - upgraded the `home` first viewport by replacing dot-only proof markers
    with semantic icon chips and calming the header/action rhythm
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `.codex/tasks/PRJ-822-home-header-and-proof-iconography-pass.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-822-home-header-and-proof-iconography-pass.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - deploy-side screenshot proof still needs to confirm whether `home` is now
    beyond the parity gate
- Next steps:
  - compare the deployed `home`
  - if needed, perform one final bounded first-viewport polish slice only
- Decisions made:
  - reused the existing public glyph system instead of introducing new custom
    icon assets for this micro-proof row
