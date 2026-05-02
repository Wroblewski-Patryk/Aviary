# Task

## Header
- ID: PRJ-872
- Title: Chat 99 Canonical Evidence Pass
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-871
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 872
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The renewed 99% canonical UI lane has closed shared layout, public home, dashboard, and personality. Chat already has a v5 canonical implementation but needs a fresh evidence pass on top of the current shell/sidebar and route changes before a clean commit candidate can be prepared.

## Goal
Tighten `/chat` toward the approved v5 canonical chat reference while preserving the two-column chat/persona model, real route data flow, composer behavior, and shared authenticated shell.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-872-chat-99-canonical-evidence-pass.md`
- Screenshot evidence under `.codex/artifacts/prj872-chat-99-canonical-evidence-pass/`

## Implementation Plan
1. Compare the current `/chat` render against `docs/ux/assets/aion-chat-canonical-reference-v5.png`.
2. Capture desktop and mobile screenshots with stable mocked API responses.
3. Apply only focused layout/density fixes required by visible drift.
4. Rebuild and capture after screenshots.
5. Update task/context evidence so the repo can move closer to a commit-ready state.

## Acceptance Criteria
- Desktop `/chat` keeps the canonical two-column 60/40 conversation/persona composition.
- The cognitive belt, transcript, composer, and persona card read as one calm surface without extra route chrome.
- Mobile remains readable without horizontal overflow and without clipped primary controls.
- Existing API calls and local chat state behavior remain unchanged.
- Screenshot comparison evidence is recorded.

## Success Signal
- User or operator problem: The canonical UI lane needs more polish before a trustworthy commit/push candidate.
- Expected product or reliability outcome: Chat aligns with the refreshed canonical shell and adjacent flagship routes.
- How success will be observed: browser screenshots compared against the v5 canonical chat reference.
- Post-launch learning needed: no

## Deliverable For This Stage
Focused implementation and verification evidence for the chat canonical pass.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `/chat` screenshot evidence is captured before and after the pass.
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
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-872-chat-99-canonical-evidence-pass.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP render at `1568x1003` and `390x844`
  - no visible desktop route toolbar
  - no horizontal mobile overflow
  - portrait notes hide on mobile as intended
- Screenshots/logs:
  - `.codex/artifacts/prj872-chat-99-canonical-evidence-pass/chat-desktop-before-1568x1003.png`
  - `.codex/artifacts/prj872-chat-99-canonical-evidence-pass/chat-mobile-before-390x844.png`
  - `.codex/artifacts/prj872-chat-99-canonical-evidence-pass/chat-desktop-after-1568x1003-v1.png`
  - `.codex/artifacts/prj872-chat-99-canonical-evidence-pass/chat-mobile-after-390x844-v1.png`
- High-risk checks:
  - frontend-only chat visual refinement; no backend, DB, auth, or runtime contract changed
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
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v5.png`
- Canonical visual target: `/chat` authenticated route
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: previously established in canonical lane
- Existing shared pattern reused: canonical authenticated shell/sidebar, chat v5 two-column model, chat persona raster asset, cognitive belt
- New shared pattern introduced: no
- Design-memory entry reused: existing canonical chat direction
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: preserve existing raster chat persona stage asset and code-native chat UI
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: The live UI keeps the AION shared sidebar and code-native chat controls rather than shipping the generated v5 reference as a static image. The top belt remains text-first rather than icon-heavy to preserve current component patterns.
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: semantic controls preserved
- Parity evidence: screenshot comparison against `docs/ux/assets/aion-chat-canonical-reference-v5.png` and latest Chrome CDP renders listed above

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
- User or operator affected: AION web user using the flagship chat route
- Existing workaround or pain: The route needs fresh parity proof after adjacent shell and route passes.
- Smallest useful slice: one focused `/chat` canonical evidence pass
- Success metric or signal: improved screenshot parity against the approved v5 chat reference
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: visual review after deploy

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: read and send a chat message
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
- Data classification: existing authenticated chat UI data only
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

- Task summary: added canonical v5-style portrait support notes for memory continuity, expression, and channel context while preserving the existing two-column chat and composer behavior.
- Files changed: `web/src/App.tsx`, `web/src/index.css`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/tasks/PRJ-872-chat-99-canonical-evidence-pass.md`
- How tested: web build, diff hygiene, Chrome CDP desktop/mobile screenshot comparison.
- What is incomplete: final deploy-side visual review can still tune exact note placement after product inspection.
- Next steps: prepare a clean commit candidate or continue with lower-priority route polish if requested.
- Decisions made: preserve mobile simplicity by hiding portrait notes below desktop.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Chat has a v5 canonical implementation but no fresh 99% evidence after recent shell/home/dashboard/personality changes.
- Gaps: current screenshot comparison for the renewed 99% lane is not yet captured.
- Inconsistencies: pending screenshot audit.
- Architecture constraints: preserve existing shell, chat API flow, composer behavior, and v5 persona asset.

### 2. Select One Priority Task
- Selected task: PRJ-872 Chat 99 Canonical Evidence Pass.
- Priority rationale: Chat is the remaining central flagship route before preparing a clean commit candidate.
- Why other candidates were deferred: Tools/settings are less directly tied to the flagship canonical trio.

### 3. Plan Implementation
- Files or surfaces to modify: `/chat` JSX/CSS and context docs only.
- Logic: preserve route data consumption and interactions.
- Edge cases: empty transcript preview, long transcript, mobile fixed navigation, composer wrapping.

### 4. Execute Implementation
- Implementation notes: added three code-native portrait notes and repositioned note anchors to match the canonical right-side persona annotation rhythm.

### 5. Verify and Test
- Validation performed: `npm run build`, `git diff --check`, Chrome CDP screenshots at desktop and mobile sizes.
- Result: passed.

### 6. Self-Review
- Simpler option considered: CSS-only density pass if screenshot audit shows JSX is structurally correct.
- Technical debt introduced: no
- Scalability assessment: changes should remain route-scoped.
- Refinements made: kept notes desktop-only so mobile does not become cluttered.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-872-chat-99-canonical-evidence-pass.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
