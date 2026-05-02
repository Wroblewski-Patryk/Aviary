# Task

## Header
- ID: PRJ-876
- Title: Canonical UI Commit Scope Audit
- Task Type: release
- Current Stage: post-release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-875
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 876
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The canonical UI package has passed route-level screenshot and build evidence.
Before creating a commit, the changed file set needs a scope audit so release
work does not accidentally stage unrelated artifacts.

## Goal
Define the clean commit candidate for the canonical UI package and record what
should and should not be staged.

## Scope
- Review:
  - tracked UI and context diffs
  - untracked task files
  - untracked non-task artifacts
- Files changed by this task:
  - `.codex/tasks/PRJ-876-canonical-ui-commit-scope-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Out of scope:
  - creating a commit
  - pushing to origin
  - changing product UI behavior

## Success Signal
- User or operator problem: the canonical UI package is large enough that a
  careless commit could include unrelated files.
- Expected product or reliability outcome: the next commit can be created
  selectively and safely.
- How success will be observed: explicit stage/include/exclude lists plus
  validation evidence.
- Post-launch learning needed: no

## Deliverable For This Stage
A commit-scope audit with exact include and exclude guidance.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect tracked changed files.
2. Inspect untracked files that could be accidentally staged.
3. Define the commit candidate include list.
4. Define the files to leave unstaged unless explicitly requested.
5. Run lightweight validation for repository hygiene.
6. Update context documents.

## Acceptance Criteria
- The task records tracked changed files.
- The task records untracked files relevant to staging decisions.
- The task separates canonical UI package files from unrelated artifacts.
- Build/diff hygiene evidence remains available from PRJ-875 and is referenced.
- Context documents are updated.

## Definition of Done
- [x] Commit candidate include list is documented.
- [x] Exclude list is documented.
- [x] Validation evidence is documented.
- [x] Task board and project state are updated.

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
- committing or pushing without explicit user request in this task

## Validation Evidence
- Tests:
  - `git diff --name-only`
  - result: listed tracked changed files
  - `git ls-files --others --exclude-standard`
  - result: listed untracked task files plus `artifacts/behavior_validation/prj843-report.json`
  - `git diff --stat -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
  - result: canonical UI tracked diff summarized
- Manual checks:
  - `.gitignore` confirms `.codex/artifacts/` screenshot evidence is ignored
    and should not be staged by default
- Screenshots/logs:
  - PRJ-875 screenshot evidence remains in `.codex/artifacts/`
- High-risk checks:
  - no product code changed in this audit task
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `.codex/context/TASK_BOARD.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: PRJ-869 through PRJ-875 evidence
- Canonical visual target: commit-ready canonical UI package
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused: not applicable
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: yes, in PRJ-875
- Background or decorative asset strategy: no change
- Canonical asset extraction required: no
- Screenshot comparison pass completed: yes, in PRJ-875
- Remaining mismatches: no new visual mismatches reviewed in this audit
- State checks: loading | empty | error | success
- Feedback locality checked: yes, via PRJ-875
- Raw technical errors hidden from end users: yes, via PRJ-875
- Responsive checks: desktop | mobile
- Input-mode checks: touch | pointer | keyboard
- Accessibility checks: no new UI
- Parity evidence: PRJ-875 screenshots

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert the eventual canonical UI commit if a visual regression
  is found
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
Recommended commit candidate include list:

- `web/src/App.tsx`
- `web/src/index.css`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-864-dashboard-canonical-density-pass.md`
- `.codex/tasks/PRJ-865-personality-canonical-first-viewport-pass.md`
- `.codex/tasks/PRJ-866-landing-canonical-first-viewport-pass.md`
- `.codex/tasks/PRJ-867-tools-canonical-shell-consistency-pass.md`
- `.codex/tasks/PRJ-868-canonical-99-layout-foundation.md`
- `.codex/tasks/PRJ-869-public-home-landing-99-pass.md`
- `.codex/tasks/PRJ-870-dashboard-99-canonical-evidence-pass.md`
- `.codex/tasks/PRJ-871-personality-99-canonical-pass.md`
- `.codex/tasks/PRJ-872-chat-99-canonical-evidence-pass.md`
- `.codex/tasks/PRJ-873-settings-canonical-shell-polish.md`
- `.codex/tasks/PRJ-874-tools-canonical-directory-polish.md`
- `.codex/tasks/PRJ-875-canonical-ui-final-route-sweep.md`
- `.codex/tasks/PRJ-876-canonical-ui-commit-scope-audit.md`

Recommended exclude list unless the user explicitly requests otherwise:

- `.codex/tasks/PRJ-851-publish-and-smoke-release-smoke-summary.md`
- `.codex/tasks/PRJ-852-chat-canonical-97-parity-closure.md`
- `artifacts/behavior_validation/prj843-report.json`
- `.codex/artifacts/` screenshot evidence because it is intentionally ignored
  by `.gitignore`

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
- User or operator affected: release operator
- Existing workaround or pain: untracked task files and an unrelated artifact
  make broad staging risky
- Smallest useful slice: document the commit scope
- Success metric or signal: clear include/exclude lists
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: create a clean canonical UI commit
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: PRJ-875 frontend build
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: PRJ-875 route screenshots
- Rollback or disable path: revert the eventual commit

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: PRJ-875
- Error state verified: PRJ-875
- Refresh/restart behavior verified: PRJ-875
- Regression check performed: PRJ-875 build and screenshots

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: repository metadata and frontend UI
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: accidental staging of unrelated artifacts
- Secret handling: unchanged
- Security tests or scans: not applicable
- Fail-closed behavior: selective staging recommended
- Residual risk: operator must still execute staging carefully

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: Documented the canonical UI commit candidate and staging
  exclusions.
- Files changed:
  - `.codex/tasks/PRJ-876-canonical-ui-commit-scope-audit.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --name-only`
  - `git ls-files --others --exclude-standard`
  - `git diff --stat -- web/src/App.tsx web/src/index.css .codex/context/TASK_BOARD.md .codex/context/PROJECT_STATE.md`
- What is incomplete:
  - commit and push are not performed by this task
- Next steps:
  - create the selective commit when requested
- Decisions made:
  - leave unrelated PRJ-851/PRJ-852 and `artifacts/behavior_validation/prj843-report.json`
    out of the recommended canonical UI commit

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: repository has a large canonical UI diff plus multiple untracked task
  files and one untracked behavior validation artifact.
- Gaps: the exact commit candidate was not recorded.
- Inconsistencies: `.codex/artifacts/` is ignored, while `artifacts/` is not
  ignored and should not be staged accidentally.
- Architecture constraints: keep release scope explicit and avoid unrelated
  artifact churn.

### 2. Select One Priority Task
- Selected task: PRJ-876 Canonical UI Commit Scope Audit.
- Priority rationale: the project is commit-ready visually, but staging risk
  remains before release.
- Why other candidates were deferred: new UI polish should wait until the
  current package is safely committed.

### 3. Plan Implementation
- Files or surfaces to modify: task and context docs only.
- Logic: no app logic changes.
- Edge cases: accidental broad `git add .` could include unrelated artifacts.
- Validation path: git file-list commands and context updates.

### 4. Execute Implementation
- Implementation notes: inspected tracked and untracked file sets and recorded
  commit candidate boundaries.

### 5. Verify and Test
- Validation performed: git diff and untracked-file inspection.
- Result: passed

### 6. Self-Review
- Simpler option considered: just tell the user to commit everything.
- Technical debt introduced: no
- Scalability assessment: the documented include/exclude list is enough for the
  current release slice and avoids inventing new release tooling.
- Refinements made: separated canonical UI task files from unrelated task and
  behavior artifacts.

### 7. Update Documentation and Knowledge
- Docs updated: `.codex/tasks/PRJ-876-canonical-ui-commit-scope-audit.md`
- Context updated: `.codex/context/TASK_BOARD.md`,
  `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
