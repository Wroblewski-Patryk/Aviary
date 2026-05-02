# Task

## Header
- ID: PRJ-889
- Title: Automations Body Copy Localization
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-888
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 889
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-888 localized static Integrations body copy. The next visible localized
shell gap is the Automations route, where the hero copy uses `UI_COPY`, but
stat details, flow labels, boundary cards, and health detail rows still contain
route-owned English strings.

## Goal
Move static Automations route body copy into the existing
`UI_COPY.automations` structure so Polish localized views no longer show
English shell-owned automation copy.

## Scope
- Route:
  - `/automations`
- Files:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-889-automations-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
- Out of scope:
  - translating backend-supplied health error strings
  - changing proactive settings behavior
  - backend, DB, auth, provider, scheduler, or action-layer changes

## Success Signal
- User or operator problem: Polish Automations view still contains English
  route-owned body copy.
- Expected product or reliability outcome: static Automations body copy is
  owned by the existing localization structure.
- How success will be observed: build passes and a Polish Automations smoke no
  longer finds the targeted English hardcoded phrases.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused localization refactor for static Automations route copy.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend `UI_COPY.automations` for static route body strings.
2. Replace hardcoded Automations route copy with `copy.automations` fields.
3. Run frontend build.
4. Run a Polish Automations smoke for targeted English phrase absence.
5. Update task board and project state.

## Acceptance Criteria
- Static Automations stat details, flow labels, boundary cards, and health
  details use `copy.automations`.
- English behavior remains unchanged.
- Polish smoke confirms targeted hardcoded English phrases are absent.
- `npm run build` passes.

## Definition of Done
- [x] Automations static body copy uses `UI_COPY.automations`.
- [x] Build passes.
- [x] Polish Automations smoke passes.
- [x] Task board and project state are updated.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new localization system
- translating backend-supplied dynamic errors in the frontend
- backend, DB, provider, scheduler, or action-layer changes

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `git diff --check -- web/src/App.tsx .codex/tasks/PRJ-889-automations-body-copy-localization.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - Chrome CDP Polish Automations copy smoke
  - result: passed
  - checked route-owned Polish strings, targeted English phrase absence, route
    path, and horizontal overflow
- Screenshots/logs:
  - `.codex/artifacts/prj889-automations-body-copy-localization/pl-automations-copy-smoke.json`
  - `.codex/artifacts/prj889-automations-body-copy-localization/pl-automations-mobile.png`
- High-risk checks:
  - no runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - existing `UI_COPY` route localization structure in `web/src/App.tsx`
  - `docs/governance/autonomous-engineering-loop.md`
  - `docs/ux/screen-quality-checklist.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: canonical shell direction already implemented in
  PRJ-864 through PRJ-888
- Canonical visual target: localized Automations route inside canonical shell
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: previously established for canonical shell
- Existing shared pattern reused: `UI_COPY` route copy and canonical module shell
- New shared pattern introduced: no
- Design-memory entry reused: canonical shell copy localization pattern from
  PRJ-886 and PRJ-888
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no asset change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes
- Remaining mismatches:
  - backend-supplied health `status` may render in English, for example
    `Ready`; this task only localizes route-owned static copy.
- State checks: success
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: mobile
- Input-mode checks: touch
- Accessibility checks: text remains visible in existing semantic route layout
- Parity evidence: pending

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

## Notes
Backend health error strings remain data-owned and may still be English.

## Result Report
- Task summary:
  - moved Automations route-owned static copy into `UI_COPY.automations`
- Files changed:
  - `web/src/App.tsx`
  - `.codex/tasks/PRJ-889-automations-body-copy-localization.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
- How tested:
  - frontend build
  - Chrome CDP Polish Automations copy smoke with screenshot evidence
  - diff whitespace check
- What is incomplete:
  - backend-supplied health status values are not translated in this slice
- Next steps:
  - localize the next module route with route-owned English body copy
- Decisions made:
  - reuse existing `UI_COPY` structure; no new localization mechanism

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - Automations route still contains route-owned English body copy in stat
    details, flow labels, boundary cards, and health detail rows.
- Gaps:
  - Polish UI language does not fully cover Automations body content.
- Inconsistencies:
  - Automations hero uses `UI_COPY`, while lower sections use hardcoded copy.
- Architecture constraints:
  - reuse existing `UI_COPY` localization structure; do not add a new system.

### 2. Select One Priority Task
- Selected task:
  - localize static Automations route body copy.
- Priority rationale:
  - it is the next small, visible localized shell gap after Integrations.
- Why other candidates were deferred:
  - broader route localization and visual polish would exceed one small slice.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - PRJ-889 task record
  - context files after validation
- Logic:
  - add copy keys under `UI_COPY.automations` and replace hardcoded route text.
- Edge cases:
  - backend health errors remain dynamic and out of scope.

### 4. Execute Implementation
- Implementation notes:
  - added English, Polish, and German copy keys under `UI_COPY.automations`
  - replaced hardcoded stat details, flow headers, flow rows, boundary cards,
    and health detail rows with localized copy

### 5. Verify and Test
- Validation performed:
  - `Push-Location .\web; npm run build; Pop-Location`
  - Chrome CDP Polish Automations copy smoke
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - translating only the Polish strings inline was rejected because it would
    keep the same hardcoded-copy drift.
- Technical debt introduced: no
- Scalability assessment:
  - fits the existing route copy structure and can be repeated for remaining
    modules.
- Refinements made:
  - kept backend health status and errors out of scope to avoid disguising
    data-owned values as route-owned copy.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-889-automations-body-copy-localization.md`
  - `.codex/context/LEARNING_JOURNAL.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: yes.
