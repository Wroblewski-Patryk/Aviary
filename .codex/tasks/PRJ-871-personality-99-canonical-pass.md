# Task

## Header
- ID: PRJ-871
- Title: Personality 99 Canonical Pass
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-870
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 871
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The renewed 99% canonical UI lane has closed the shared layout foundation, public home, and dashboard surfaces. The next dependent flagship surface is `/personality`, which already has an approved canonical reference and an existing first-viewport implementation from PRJ-865.

## Goal
Bring `/personality` closer to 99% canonical parity against the approved personality reference while preserving the shared authenticated shell, current data flow, and existing canonical persona figure asset.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-871-personality-99-canonical-pass.md`
- Screenshot evidence under `.codex/artifacts/prj871-personality-99-canonical-pass/`

## Implementation Plan
1. Capture the current `/personality` desktop and mobile render against the canonical reference.
2. Audit visible drift in layout structure, hero-stage balance, side-stack density, timeline continuity, mobile collapse, and typography.
3. Apply the smallest focused JSX/CSS changes needed for the personality surface only.
4. Rebuild the web client and capture after screenshots.
5. Record validation, parity notes, and context updates.

## Acceptance Criteria
- `/personality` uses the existing canonical shell and does not reintroduce a route toolbar or browser-frame wrapper.
- Desktop first viewport presents the personality stage, overview, side content, and timeline with visibly improved canonical density.
- Mobile remains readable with no horizontal overflow or clipped primary controls.
- Existing route data/API calls are preserved; no mock-only runtime path is introduced.
- Screenshot comparison evidence is recorded before closure.

## Success Signal
- User or operator problem: Personality still needs the same 99% polish level as the newly refreshed home and dashboard.
- Expected product or reliability outcome: The flagship personality route reads like part of the same canonical AION product surface.
- How success will be observed: side-by-side screenshot review against `docs/ux/assets/aion-personality-canonical-reference-v1.png`.
- Post-launch learning needed: no

## Deliverable For This Stage
Focused implementation plus verification evidence for the personality canonical pass.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `/personality` screenshot evidence is captured before and after the pass.
- [x] Web build passes.
- [x] Diff hygiene passes for touched files.
- [x] Task board and project state record the completed slice.

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
  - result: passed
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-871-personality-99-canonical-pass.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP render at `1568x1003` and `390x844`
  - no visible desktop route toolbar
  - no horizontal mobile overflow
  - nested `role_skill_state.skill_summary.skill_count` now renders as `28`
- Screenshots/logs:
  - `.codex/artifacts/prj871-personality-99-canonical-pass/personality-desktop-before-1568x1003.png`
  - `.codex/artifacts/prj871-personality-99-canonical-pass/personality-mobile-before-390x844.png`
  - `.codex/artifacts/prj871-personality-99-canonical-pass/personality-desktop-after-1568x1003-v2.png`
  - `.codex/artifacts/prj871-personality-99-canonical-pass/personality-mobile-after-390x844-v3.png`
- High-risk checks:
  - frontend-only route/shell visual change; no backend, DB, auth, or runtime contract changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: AGENTS.md, canonical visual implementation workflow, screen quality checklist
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-personality-canonical-reference-v1.png`
- Canonical visual target: `/personality` authenticated route
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: previously established in canonical lane
- Existing shared pattern reused: canonical authenticated shell, sidebar, personality figure asset, route overview bar, stage panels
- New shared pattern introduced: no
- Design-memory entry reused: existing canonical personality route direction
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: preserve existing raster personality figure and code-native panels
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: Desktop keeps the AION shared sidebar instead of the older Prometheus sidebar in the personality reference; this is intentional because the current canonical shell lane uses the AION sidebar. Mobile still uses the fixed shared tabbar, but the personality scene is now compressed so the stage ends at the tabbar boundary.
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: semantic controls preserved; visual focus not weakened
- Parity evidence: screenshot comparison against `docs/ux/assets/aion-personality-canonical-reference-v1.png` and latest Chrome CDP renders listed above

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert the frontend CSS/JSX changes for this task
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
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
Risk is limited to frontend visual density and responsive presentation. No backend, DB, auth, or runtime pipeline behavior is in scope.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY` or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB -> validation -> error handling -> test. Partial implementations, mock-only paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: AION web user reviewing the flagship personality route
- Existing workaround or pain: The route is close but still below the renewed 99% visual bar.
- Smallest useful slice: one focused `/personality` canonical pass
- Success metric or signal: improved screenshot parity against the approved personality reference
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: visual review after deploy

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: inspect personality identity map
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: browser screenshot render
- Rollback or disable path: revert frontend changes from this task

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: unchanged
- Error state verified: unchanged
- Refresh/restart behavior verified: Chrome CDP hard reload through mocked API responses
- Regression check performed: web production build

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: existing authenticated UI data only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: none
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: low visual regression risk

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: tightened `/personality` toward the canonical reference with a calmer overview bar, denser hero/timeline rhythm, improved side-stack density, route-specific mobile header compression, and correct nested skill-count rendering.
- Files changed: `web/src/App.tsx`, `web/src/index.css`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/tasks/PRJ-871-personality-99-canonical-pass.md`
- How tested: web build, diff hygiene, Chrome CDP desktop/mobile screenshot comparison.
- What is incomplete: no backend or real API data contract changes were needed; deploy-side review can still tune final pixels after visual inspection.
- Next steps: continue the 99% canonical lane with the next smallest surface after personality.
- Decisions made: preserve the AION canonical shell/sidebar rather than reverting personality to the older Prometheus reference shell.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/personality` has a prior first-viewport pass but needs renewed 99% evidence after the dashboard pass.
- Gaps: current screenshot comparison is not yet captured for the 99% lane.
- Inconsistencies: pending screenshot audit.
- Architecture constraints: preserve existing shell, route data, and canonical asset.

### 2. Select One Priority Task
- Selected task: PRJ-871 Personality 99 Canonical Pass.
- Priority rationale: It is the next dependent flagship route after dashboard in the canonical closure order.
- Why other candidates were deferred: Chat and settings refinements wait until this route closes or reveals shared-shell regressions.

### 3. Plan Implementation
- Files or surfaces to modify: `/personality` JSX/CSS and context docs only.
- Logic: preserve route data consumption and interactions.
- Edge cases: mobile overflow, long localized text, empty recent activity.

### 4. Execute Implementation
- Implementation notes: reduced route overview weight, tightened hero/timeline/side-panel density, compressed mobile personality header, kept route data flow intact, and fixed nested skill summary rendering.

### 5. Verify and Test
- Validation performed: `npm run build`, `git diff --check`, Chrome CDP screenshots at desktop and mobile sizes.
- Result: passed.

### 6. Self-Review
- Simpler option considered: CSS-only density pass if screenshot audit shows JSX is already structurally correct.
- Technical debt introduced: no
- Scalability assessment: changes should remain route-scoped.
- Refinements made: corrected an overly aggressive first figure zoom after screenshot review and compacted mobile stage height so the scene ends at the fixed tabbar boundary.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-871-personality-99-canonical-pass.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
