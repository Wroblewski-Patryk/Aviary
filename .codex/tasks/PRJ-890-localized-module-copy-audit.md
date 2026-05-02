# Task

## Header
- ID: PRJ-890
- Title: Localized Module Copy Audit
- Task Type: research
- Current Stage: post-release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-889
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 890
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-888 and PRJ-889 fixed route-owned localized copy drift in Integrations and
Automations. Iteration 890 is a TESTER iteration, so the smallest useful next
step is to audit remaining localized module routes before choosing the next
implementation slice.

## Goal
Identify which remaining Polish module routes still contain route-owned English
body copy so the next implementation task can target the highest-impact route.

## Scope
- Routes:
  - `/memory`
  - `/reflections`
  - `/plans`
  - `/goals`
  - `/insights`
  - `/tools`
- Files:
  - `.codex/tasks/PRJ-890-localized-module-copy-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - code changes
  - translating provider or backend payload values
  - visual restyling

## Success Signal
- User or operator problem: the next localized-copy task is unclear after
  fixing Automations and Integrations.
- Expected product or reliability outcome: remaining route-owned English copy
  debt is ranked by observed route impact.
- How success will be observed: CDP audit artifact lists route excerpts,
  targeted English signals, and overflow status.
- Post-launch learning needed: no

## Deliverable For This Stage
One focused audit artifact and source-of-truth update identifying the next
smallest route-localization task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Run a Polish authenticated shell CDP audit for remaining module routes.
2. Mock only existing API responses needed to render those routes.
3. Record targeted English body-copy signals and overflow status.
4. Update task board and project state with the ranked next task.

## Acceptance Criteria
- Audit covers the declared remaining module routes.
- Evidence records route, excerpt, targeted English signals, and overflow flag.
- Next smallest implementation task is identified.

## Definition of Done
- [x] Polish route audit passes without browser/runtime failure.
- [x] Audit evidence is saved under `.codex/artifacts`.
- [x] Task board and project state are updated.
- [x] No code changes are made for this audit task.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new localization system
- code changes
- translating backend/provider-supplied dynamic strings in this audit

## Validation Evidence
- Tests:
  - Chrome CDP Polish module copy audit
  - result: passed
  - `git diff --check -- .codex/tasks/PRJ-890-localized-module-copy-audit.md .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: passed with line-ending warnings only
- Manual checks:
  - route excerpts reviewed from audit output
- Screenshots/logs:
  - `.codex/artifacts/prj890-localized-module-copy-audit/localized-module-copy-audit.json`
- High-risk checks:
  - no code, runtime, API, provider, scheduler, or data contract changes
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - existing `UI_COPY` route localization structure
  - `docs/governance/autonomous-engineering-loop.md`
  - `.codex/context/LEARNING_JOURNAL.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: canonical shell route surfaces PRJ-864 through
  PRJ-889
- Canonical visual target: localized authenticated shell modules
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: previously established for canonical shell
- Existing shared pattern reused: `UI_COPY` localization audit pattern
- New shared pattern introduced: no
- Design-memory entry reused: canonical shell localization pattern
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: no asset change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not applicable
- Remaining mismatches:
  - `/insights` has the highest route-owned English body-copy debt
  - `/memory`, `/plans`, and `/goals` also need copy-localization slices
  - `/tools` has English visible in details, but some values are data-owned
- State checks: success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: mobile
- Input-mode checks: touch
- Accessibility checks: route text remains readable; overflow false for all
  checked routes
- Parity evidence:
  - `.codex/artifacts/prj890-localized-module-copy-audit/localized-module-copy-audit.json`

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
The audit intentionally distinguishes route-owned strings from backend or
provider payload values. The next implementation slice should start with
`/insights`.

## Result Report
- Task summary:
  - audited remaining localized module routes for route-owned English copy.
- Files changed:
  - `.codex/tasks/PRJ-890-localized-module-copy-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - Chrome CDP Polish module copy audit.
- What is incomplete:
  - no copy fixes were made in this TESTER iteration.
- Next steps:
  - localize `/insights` route-owned body copy.
- Decisions made:
  - rank `/insights` first because it has the broadest targeted English signal
    set among checked routes.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - several remaining module routes still contain English body copy in Polish
    UI mode.
- Gaps:
  - no ranked list existed after PRJ-889.
- Inconsistencies:
  - localized labels and hero text can coexist with English lower-section copy.
- Architecture constraints:
  - route-owned strings should move into `UI_COPY`; data-owned strings require
    separate contract decisions.

### 2. Select One Priority Task
- Selected task:
  - audit remaining localized module copy.
- Priority rationale:
  - iteration 890 is a TESTER iteration and should strengthen evidence before
    another implementation slice.
- Why other candidates were deferred:
  - implementing another route without ranking could miss the highest-impact
    localized-copy gap.

### 3. Plan Implementation
- Files or surfaces to modify:
  - task and context docs only.
- Logic:
  - use CDP to render routes in Polish and record targeted English phrases.
- Edge cases:
  - provider/backend payload values may remain English and are noted separately.

### 4. Execute Implementation
- Implementation notes:
  - no code changes; audit used existing routes with mocked API responses.

### 5. Verify and Test
- Validation performed:
  - Chrome CDP audit across six module routes.
- Result:
  - passed; all checked routes avoided horizontal overflow.

### 6. Self-Review
- Simpler option considered:
  - static source search was insufficient because it cannot distinguish rendered
    route copy from dead or data-owned strings.
- Technical debt introduced: no
- Scalability assessment:
  - the audit pattern can be repeated after each localization slice.
- Refinements made:
  - ranked `/insights` as the next task based on observed rendered signals.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `.codex/tasks/PRJ-890-localized-module-copy-audit.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: already updated by PRJ-889 for this recurring
  pitfall.
