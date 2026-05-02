# Task

## Header
- ID: PRJ-873
- Title: Settings Canonical Shell Polish
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-872
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 873
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The primary canonical routes now use the refreshed AION shell and material system. `/settings` remains more generic and card-heavy, so it can visually undermine the product quality even though it is a utility route.

## Goal
Bring `/settings` into the same canonical AION shell language with a calmer overview, compact controls, clearer profile/preferences/data-safety grouping, and evidence-backed desktop/mobile behavior.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-873-settings-canonical-shell-polish.md`
- Screenshot evidence under `.codex/artifacts/prj873-settings-canonical-shell-polish/`

## Implementation Plan
1. Capture current `/settings` desktop and mobile screenshots.
2. Audit visible drift against the established AION shell, sidebar, dashboard, chat, and personality material language.
3. Replace the generic route hero/card grid with a route-scoped settings canvas and canonical overview/control panels.
4. Preserve existing form controls, save/reset handlers, and API contracts.
5. Run build, diff hygiene, screenshot checks, and update source-of-truth context.

## Acceptance Criteria
- `/settings` no longer reads as a generic form grid detached from the canonical shell.
- Profile, interface, conversation/proactive, save, and reset areas are grouped clearly.
- Desktop has a controlled two-column settings layout with a compact overview bar.
- Mobile remains readable without horizontal overflow or clipped controls.
- Existing settings save/reset behavior and API calls remain unchanged.

## Success Signal
- User or operator problem: Utility screens should feel as polished as flagship routes.
- Expected product or reliability outcome: Settings feels like part of the same premium AION interface.
- How success will be observed: screenshot review across desktop and mobile.
- Post-launch learning needed: no

## Deliverable For This Stage
Focused implementation and verification evidence for the settings canonical shell polish.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] `/settings` screenshot evidence is captured before and after the pass.
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
  - `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-873-settings-canonical-shell-polish.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP render at `1568x1003` and `390x844`
  - no visible desktop route toolbar
  - no horizontal mobile overflow
  - save/reset controls remain visible and guarded
- Screenshots/logs:
  - `.codex/artifacts/prj873-settings-canonical-shell-polish/settings-desktop-before-1568x1003.png`
  - `.codex/artifacts/prj873-settings-canonical-shell-polish/settings-mobile-before-390x844.png`
  - `.codex/artifacts/prj873-settings-canonical-shell-polish/settings-desktop-after-1568x1003-v2.png`
  - `.codex/artifacts/prj873-settings-canonical-shell-polish/settings-mobile-after-390x844-v2.png`
- High-risk checks:
  - reset behavior remains behind the existing exact confirmation phrase
  - frontend-only layout change; no backend, DB, auth, or runtime contract changed
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
- Design source reference: established AION canonical shell/sidebar and flagship route references
- Canonical visual target: `/settings` authenticated route
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: previously established in canonical lane
- Existing shared pattern reused: canonical authenticated shell/sidebar, overview bar, soft panels, material cards
- New shared pattern introduced: no
- Design-memory entry reused: existing AION canonical shell direction
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: code-native panels only; no new raster assets
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: No dedicated settings canonical screenshot exists; this pass is structurally faithful to the approved AION shell and route material language rather than pixel-close to a settings-specific mockup.
- State checks: loading | empty | error | success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: unchanged
- Responsive checks: desktop | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: semantic controls preserved
- Parity evidence: screenshot comparison against established AION canonical shell/route material and latest Chrome CDP renders listed above

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
No backend, DB, auth, runtime, or destructive data behavior change is in scope. Reset remains guarded by the existing confirmation phrase.

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
- User or operator affected: AION web user changing account and interface preferences
- Existing workaround or pain: Settings reads less canonical than the flagship routes.
- Smallest useful slice: one route-local `/settings` shell polish pass
- Success metric or signal: cleaner desktop/mobile screenshots with preserved controls
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: visual review after deploy

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: change and save settings
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: browser screenshot render and build
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
- Data classification: existing authenticated settings data only
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: accidental reset remains guarded by existing confirmation phrase
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

- Task summary: replaced the generic settings hero/form grid with a canonical settings canvas, compact overview bar, preference panel, side save/proactive stack, and calmer danger panel while preserving all controls and handlers.
- Files changed: `web/src/App.tsx`, `web/src/index.css`, `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`, `.codex/tasks/PRJ-873-settings-canonical-shell-polish.md`
- How tested: web build, diff hygiene, Chrome CDP desktop/mobile screenshot comparison.
- What is incomplete: no settings-specific canonical screenshot exists, so this remains structurally faithful rather than pixel-close.
- Next steps: prepare a commit candidate or continue lower-priority route polish.
- Decisions made: keep reset visible but less dominant and preserve exact confirmation guard.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/settings` still uses a generic route hero and form-card grid compared with canonicalized flagship routes.
- Gaps: no dedicated settings canonical screenshot exists, so this must reuse approved shell/route patterns.
- Inconsistencies: pending screenshot audit.
- Architecture constraints: preserve existing settings handlers and contracts.

### 2. Select One Priority Task
- Selected task: PRJ-873 Settings Canonical Shell Polish.
- Priority rationale: Utility route quality is now the next visible interface gap after flagship route passes.
- Why other candidates were deferred: Additional dashboard/chat/personality micro-polish can wait until utility shell consistency is improved.

### 3. Plan Implementation
- Files or surfaces to modify: `/settings` JSX/CSS and context docs only.
- Logic: preserve save/reset behavior and form state.
- Edge cases: mobile form wrapping, reset danger panel, keyboard/accessibility controls.

### 4. Execute Implementation
- Implementation notes: introduced route-scoped settings canvas classes, grouped profile/interface/time/conversation into one preference panel, moved proactive/save/reset into a supporting side stack, and compressed the mobile settings header.

### 5. Verify and Test
- Validation performed: `npm run build`, `git diff --check`, Chrome CDP screenshots at desktop and mobile sizes.
- Result: passed.

### 6. Self-Review
- Simpler option considered: CSS-only retune, but route structure may need grouping changes for visual clarity.
- Technical debt introduced: no
- Scalability assessment: changes should remain route-scoped.
- Refinements made: route-specific mobile header compression and danger-panel visual quieting.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-873-settings-canonical-shell-polish.md`
- Context updated: `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
