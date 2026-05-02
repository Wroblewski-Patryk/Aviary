# Task

## Header
- ID: PRJ-867
- Title: Tools Canonical Shell Consistency Pass
- Task Type: design
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-866
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 867
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The frozen canonical surfaces have received focused passes. `Tools` is not yet
frozen by a dedicated canonical screenshot, but the canonical reference set says
it may borrow the current visual language. The current Tools route repeats the
same title across multiple large panels and still shows the extra desktop route
toolbar, making it feel less aligned with Chat, Dashboard, and Personality.

## Goal
Bring `/tools` into the canonical shell language by removing duplicate heading
layers, hiding the extra route toolbar, and introducing one compact operational
overview before the detailed tool catalog.

## Success Signal
- User or operator problem: Tools feels less canonical and more generic than
  the recently polished routes.
- Expected product or reliability outcome: Tools reads as one coherent shell
  surface with summary first and catalog second.
- How success will be observed: desktop/mobile screenshots and no overflow.
- Post-launch learning needed: no

## Deliverable For This Stage
Implement a focused `/tools` UI composition pass and verify it with build and
screenshots.

## Constraints
- use existing systems and approved mechanisms
- do not change tools API contracts or data semantics
- do not introduce a new frozen canonical asset for Tools
- preserve loading and empty state behavior

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/tasks/PRJ-867-tools-canonical-shell-consistency-pass.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Hide the extra desktop route toolbar for Tools.
2. Replace duplicate route hero and summary panels with one compact Tools
   overview bar.
3. Retune catalog spacing and panels using existing AION material tokens.
4. Preserve tool groups, item controls, Telegram linking, loading, and empty
   state behavior.
5. Run build, diff check, and desktop/mobile screenshots.

## Acceptance Criteria
- Tools first viewport no longer repeats the same large heading three times.
- Tools uses one canonical overview surface plus the detailed catalog.
- No horizontal overflow on desktop or mobile.
- Existing tool toggles/details/Telegram linking remain present.

## Definition of Done
- [x] Web build passes.
- [x] `git diff --check` passes.
- [x] Desktop and mobile Tools screenshots are captured.
- [x] Latest implementation screenshot is inspected with `view_image`.

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
- Tests: `Push-Location .\web; npm run build; Pop-Location` passed.
- Manual checks: `git diff --check -- web/src/App.tsx web/src/index.css .codex/tasks/PRJ-867-tools-canonical-shell-consistency-pass.md` passed with line-ending warnings only.
- Screenshots/logs:
  - `.codex/artifacts/prj867-tools-canonical-shell-pass/desktop-before-1568x1003.png`
  - `.codex/artifacts/prj867-tools-canonical-shell-pass/mobile-before-390x844.png`
  - `.codex/artifacts/prj867-tools-canonical-shell-pass/desktop-1568x1003-v2.png`
  - `.codex/artifacts/prj867-tools-canonical-shell-pass/mobile-390x844-v2.png`
  - `.codex/artifacts/prj867-tools-canonical-shell-pass/settings-smoke-1568x1003.png`
- High-risk checks: no runtime/data-contract changes in scope
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence
- Architecture source reviewed: `docs/ux/canonical-web-screen-reference-set.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: canonical shell routes and route translation rules
- Canonical visual target: borrowed canonical shell language for non-frozen Tools
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: compact overview bars and canonical shell
- New shared pattern introduced: no
- Design-memory entry reused: route translation rules
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no new assets
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: Tools is not frozen by a dedicated canonical reference,
  so this pass aligns it structurally with the canonical shell rather than
  claiming pixel parity.
- State checks: success; loading/empty preserved by code path
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop | mobile
- Input-mode checks: pointer
- Accessibility checks: existing buttons/inputs retained
- Parity evidence:
  - implementation inspected:
    `.codex/artifacts/prj867-tools-canonical-shell-pass/desktop-1568x1003-v2.png`
  - mobile inspected:
    `.codex/artifacts/prj867-tools-canonical-shell-pass/mobile-390x844-v2.png`

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not applicable
- Rollback note: revert Tools JSX/CSS changes
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist
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

## Result Report
- Task summary: removed duplicated Tools hero/summary structure, hid the extra
  route toolbar, and introduced one compact operational overview above the
  existing tool catalog.
- Files changed: `web/src/App.tsx`, `web/src/index.css`,
  `.codex/tasks/PRJ-867-tools-canonical-shell-consistency-pass.md`,
  `.codex/context/TASK_BOARD.md`, `.codex/context/PROJECT_STATE.md`.
- How tested: web build, diff whitespace check, desktop/mobile Tools
  screenshots, Settings smoke screenshot.
- What is incomplete: Tools still has no dedicated canonical screenshot; this
  is shell-language alignment only.
- Next steps: polish Settings under the same canonical material language or
  pause to sort local commits before pushing.
- Decisions made: preserved existing tool data, controls, details, and Telegram
  linking behavior.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: Tools repeats the route title in three large panels and keeps the
  extra desktop toolbar.
- Gaps: first viewport feels less canonical than Chat, Dashboard, and
  Personality.
- Inconsistencies: duplicated summary structure and generic nested cards.
- Architecture constraints: preserve existing API-driven tool catalog.

### 2. Select One Priority Task
- Selected task: Tools canonical shell consistency pass.
- Priority rationale: after frozen canonical routes, Tools is the next visible
  shell route and is explicitly allowed to borrow canonical structure.
- Why other candidates were deferred: Settings is already acceptable under the
  current approved direction and should be handled after Tools.

### 3. Plan Implementation
- Files or surfaces to modify: Tools JSX and CSS.
- Logic: no API or runtime behavior changes.
- Edge cases: loading/empty states, Telegram linking action, mobile overflow.

### 4. Execute Implementation
- Implementation notes: added `aion-tools-overview-bar`, condensed summary
  cards, hid the desktop route toolbar for Tools, and renamed the detailed
  section to Tool directory.

### 5. Verify and Test
- Validation performed: web build, diff whitespace check, desktop/mobile
  screenshots, Settings smoke screenshot.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only hiding the toolbar; rejected because repeated
  title panels would still make the route feel non-canonical.
- Technical debt introduced: none known; existing data paths and controls were
  preserved.
- Refinements made: kept the catalog intact while removing only the duplicated
  framing layers.

### 7. Update Documentation and Knowledge
- Docs updated: task evidence only; no new canonical pattern introduced.
- Context updated: `.codex/context/TASK_BOARD.md` and
  `.codex/context/PROJECT_STATE.md`.
- Learning journal updated: not needed; no recurring pitfall confirmed.
