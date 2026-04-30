# Task

## Header
- ID: PRJ-817
- Title: Fix web copy encoding regression across the flagship shell
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-816
- Priority: P1

## Context
The user reported visible mojibake and broken Polish diacritics across the web
shell. The regression is currently concentrated in `web/src/App.tsx`, where
flagship-route copy, sidebar labels, and public-shell text drifted through a
mix of malformed UTF-8 and ASCII fallback strings.

## Goal
Restore clean localized copy in the web shell so the flagship surfaces no
longer render broken Polish text.

## Success Signal
- User or operator problem:
  - sidebar and other flagship UI surfaces show broken Polish characters
- Expected product or reliability outcome:
  - localized copy renders with correct Polish diacritics and without visible
    mojibake in the active web shell
- How success will be observed:
  - focused source audit finds no remaining Polish mojibake or ASCII fallback
    drift in `web/src/App.tsx`, and the frontend build passes
- Post-launch learning needed: yes

## Deliverable For This Stage
One bounded implementation slice that repairs the affected source strings,
records the pitfall, and validates the web build.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-817-fix-web-copy-encoding-regression.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`

## Implementation Plan
1. Audit `web/src/App.tsx` for mojibake and plain-ASCII fallback strings in the
   localized flagship copy.
2. Repair the affected Polish strings and any immediately adjacent encoding
   drift that would still leave the shell visibly broken.
3. Record the regression and detection guardrail in project context.
4. Run the frontend build and focused diff checks.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Acceptance Criteria
- Polish flagship-shell strings no longer contain visible mojibake
- no plain-ASCII fallback remains where correct Polish diacritics are expected
- build and focused diff checks pass

## Definition of Done
- [x] Affected source strings are repaired.
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
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-817-fix-web-copy-encoding-regression.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/context/LEARNING_JOURNAL.md`
- Manual checks:
  - re-audited the localized shell copy blocks in `web/src/App.tsx` after the
    repair and confirmed the broken Polish strings were restored
- Screenshots/logs:
  - Vite production build completed successfully
- High-risk checks:
  - kept the fix bounded to source copy and project context only

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
  - active flagship shell routes using localized UI copy
- Canonical visual target:
  - render the approved copy without encoding drift
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - existing flagship shell copy blocks in `web/src/App.tsx`
- New shared pattern introduced: no
- Design-memory entry reused:
  - not applicable
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - visual proof should happen naturally on the next deploy compare
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks:
  - copy-only repair preserves existing semantics
- Parity evidence:
  - source audit in `web/src/App.tsx`

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note:
  - revert the copy-only source patch if a language block regresses
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
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
- The initial shell output overstated the scope because PowerShell console
  rendering made already-correct UTF-8 lines look suspicious; raw file
  inspection remains the final source of truth.

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
  - re-audit the localized shell copy after the fix

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected:
  - flagship web users reading Polish UI copy
- Existing workaround or pain:
  - broken diacritics make the product look unfinished
- Smallest useful slice:
  - repair the affected source strings in `web/src/App.tsx`
- Success metric or signal:
  - no visible Polish mojibake remains in the flagship shell source
- Feature flag, staged rollout, or disable path: no
- Post-launch feedback or metric check:
  - next deploy-side UI check

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey:
  - reading flagship shell navigation and public-entry copy
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
  - revert this copy-only patch

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
  - public/localized UI copy only
- Trust boundaries:
  - frontend shell text
- Permission or ownership checks:
  - not applicable
- Abuse cases:
  - not applicable
- Secret handling:
  - none
- Security tests or scans:
  - not applicable
- Fail-closed behavior:
  - not applicable
- Residual risk:
  - adjacent non-Polish language strings may still need a later cleanup pass

## Result Report

- Task summary:
  - repaired the broken Polish flagship-shell copy in `web/src/App.tsx` and
    recorded the encoding-audit guardrail in project context
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-817-fix-web-copy-encoding-regression.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-817-fix-web-copy-encoding-regression.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md .codex/context/LEARNING_JOURNAL.md`
- What is incomplete:
  - deploy-side visual confirmation of the repaired shell copy
  - adjacent non-Polish language cleanup remains outside this bounded fix
- Next steps:
  - verify the deployed shell no longer shows broken Polish characters
  - then return to the active flagship route parity lane
- Decisions made:
  - treated the user-reported Polish copy regression as the bounded repair
    scope
  - recorded console-rendering ambiguity as a recurring audit pitfall
