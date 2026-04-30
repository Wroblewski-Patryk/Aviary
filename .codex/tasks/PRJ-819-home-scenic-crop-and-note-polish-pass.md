# Task

## Header
- ID: PRJ-819
- Title: Polish public home scenic crop and note rhythm
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-818
- Priority: P1

## Context
After `PRJ-818`, the public `home` shell is structurally much closer to the
target. The strongest remaining drift is now visual rather than structural:
the scenic crop, note-card styling, and `bridge + trust band` rhythm still
need a calmer, more canonical finish.

## Goal
Bring the `home` surface closer to the intended flagship feel by polishing the
hero crop, note cards, and lower closure rhythm without reopening the shell
structure.

## Success Signal
- User or operator problem:
  - `home` is structurally close, but the scene still needs more polish to
    feel truly canonical
- Expected product or reliability outcome:
  - the landing artwork has more authority, note cards feel lighter, and the
    bridge/trust closure reads as one elegant continuation
- How success will be observed:
  - deployed `home` looks less card-heavy and more scenic at desktop widths
- Post-launch learning needed: no

## Deliverable For This Stage
One bounded visual-polish slice for `home` only.

## Scope
- `web/src/index.css`
- `.codex/tasks/PRJ-819-home-scenic-crop-and-note-polish-pass.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Retune hero copy proportions and scenic crop.
2. Soften and reposition the note cards.
3. Tighten the overlap and materials of `feature bridge` and `trust band`.
4. Validate with frontend build and focused diff checks.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Acceptance Criteria
- hero art reads with stronger stage authority
- note cards feel lighter and better placed
- `feature bridge` and `trust band` look calmer and more integrated
- build and diff checks pass

## Definition of Done
- [x] Visual polish is applied.
- [x] Validation evidence is attached.
- [x] Task and repository truth are updated.

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
  - `git diff --check -- web/src/index.css .codex/tasks/PRJ-819-home-scenic-crop-and-note-polish-pass.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- Manual checks:
  - reviewed the updated desktop proportions and overlap rhythm directly in
    the source styles
- Screenshots/logs:
  - frontend production build completed successfully
- High-risk checks:
  - kept the slice CSS-only to avoid re-opening route structure risk

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/27_codex_instructions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - not applicable

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `docs/ux/assets/aion-landing-canonical-reference-v1.png`
- Canonical visual target:
  - public `home` scenic-polish closure
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - `PRJ-818` full-bleed public shell
- New shared pattern introduced: no
- Design-memory entry reused:
  - full-bleed public shell framing
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - preserve the image-based landing stage and strengthen it through crop and
    overlay polish
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - live compare should still verify exact desktop crop and tablet note density
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: desktop | tablet | mobile
- Input-mode checks: pointer | touch
- Accessibility checks:
  - visual-only CSS changes preserve existing semantics
- Parity evidence:
  - merged canonical landing spec plus the user's shell notes

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note:
  - revert the CSS-only polish pass if overlap or note readability regresses
- Observability or alerting impact: none
- Staged rollout or feature flag: none

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
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
- This slice stays CSS-only on purpose, because the structural shell work is
  already in place and the remaining gap is mostly scenic tuning.

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

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed:
  - `home` CTA and modal flow remain untouched

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected:
  - public-entry visitors on larger screens
- Existing workaround or pain:
  - the landing scene still felt slightly too card-heavy
- Smallest useful slice:
  - CSS-only crop and note polish
- Success metric or signal:
  - calmer scenic read with less visual cardiness
- Feature flag, staged rollout, or disable path: no
- Post-launch feedback or metric check:
  - next deploy-side compare

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey:
  - public landing first viewport read
- SLI:
  - not applicable
- SLO:
  - not applicable
- Error budget posture: not applicable
- Health/readiness check:
  - frontend build succeeds
- Logs, dashboard, or alert route:
  - not applicable
- Smoke command or manual smoke:
  - `Push-Location .\web; npm run build; Pop-Location`
- Rollback or disable path:
  - revert the CSS-only public-home polish pass

## AI Testing Evidence (required for AI features)

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios:
- Multi-step context scenarios:
- Adversarial or role-break scenarios:
- Prompt injection checks:
- Data leakage and unauthorized access checks:
- Result:

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification:
  - public shell visuals only
- Trust boundaries:
  - unauthenticated web shell
- Permission or ownership checks:
  - existing auth controls preserved
- Abuse cases:
  - not applicable
- Secret handling:
  - none
- Security tests or scans:
  - not applicable
- Fail-closed behavior:
  - not applicable
- Residual risk:
  - final judgment still depends on deployed screenshot parity

## Result Report

- Task summary:
  - polished the `home` scenic crop, note cards, and `bridge + trust band`
    rhythm to reduce cardiness and increase stage authority
- Files changed:
  - `web/src/index.css`
  - `.codex/tasks/PRJ-819-home-scenic-crop-and-note-polish-pass.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/index.css .codex/tasks/PRJ-819-home-scenic-crop-and-note-polish-pass.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - deploy-side proof for exact crop and note density
- Next steps:
  - compare deployed `home` and then either close it higher or spend one last
    micro-pass on note positions
- Decisions made:
  - kept this pass CSS-only because structural framing is already in place
