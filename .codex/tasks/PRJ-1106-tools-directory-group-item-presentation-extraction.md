# Task

## Header
- ID: PRJ-1106
- Title: Extract tools directory group and item presentation
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1105
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1106
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1105` added a focused `/tools` behavior characterization, making it safe
to extract the tools directory group/item JSX without losing toggle or Telegram
link behavior.

## Goal
Move the `/tools` group and item presentation behind a tools component while
keeping route-owned data, state, API calls, and side-effect handlers in
`App()`.

## Success Signal
- User or operator problem: `App.tsx` gets smaller without changing tools
  behavior.
- Expected product or reliability outcome: tools directory rendering is owned by
  `web/src/components/tools.tsx` and the characterization remains green.
- How success will be observed: build, tools characterization, route smoke, and
  diff check pass.
- Post-launch learning needed: no

## Scope
- Update `web/src/components/tools.tsx`.
- Update `web/src/App.tsx`.
- Update frontend docs, v1 roadmap, task board, and project state.

## Deliverable For This Stage
A verified component extraction for tools directory group/item presentation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add `ToolsDirectoryGroupList` and explicit label props to
   `web/src/components/tools.tsx`.
2. Reuse existing `ToolsFactCard`, `ToolsDetailCard`,
   `ToolsTechnicalDetailPanel`, `ToolsTelegramLinkPanel`, and tool formatting
   helpers inside the tools owner module.
3. Replace the inline `toolsOverview?.groups.map(...)` block in `App.tsx` with
   `ToolsDirectoryGroupList`.
4. Keep `toolsOverview`, `savingToolId`, `telegramLinkStart`,
   `telegramLinkBusy`, `handleToolToggle`, and `handleStartTelegramLink` in
   `App()`.
5. Run build, tools characterization, route smoke, and diff check.

## Acceptance Criteria
- `App.tsx` no longer maps `toolsOverview?.groups` inline.
- `ToolsDirectoryGroupList` preserves `aion-tools-group`,
  `aion-tools-item-grid`, and `aion-tools-item-card` selectors.
- Toggle callbacks still reach `handleToolToggle`.
- Telegram link callbacks still reach `handleStartTelegramLink`.
- `npm run test:tools-directory` passes.

## Definition of Done
- [x] Component extraction implemented.
- [x] Behavior characterization passes.
- [x] Route smoke passes.
- [x] Docs/context updated.

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
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location`
  - result: passed with `status=ok`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: passed with `status=ok`, `route_count=14`
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - result: remaining maps inspected after extraction
- Screenshots/logs: command output recorded in session.
- High-risk checks:
  - `git diff --check`
  - result: passed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: current `/tools` implementation
- Canonical visual target: current v1 tools directory
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable for presentation extraction
- Visual-direction brief reviewed: not applicable for presentation extraction
- Existing shared pattern reused: tools owner module component extraction
- New shared pattern introduced: no
- Design-memory entry reused: frontend route/component map
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: not assessed
- State checks: loading, empty, error, success via tools characterization
- Feedback locality checked: yes
- Raw technical errors hidden from end users: yes
- Responsive checks: route smoke only
- Input-mode checks: pointer/click through tools characterization
- Accessibility checks: no markup role changes introduced
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `ToolsDirectoryGroupList` usage if needed
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes
The component receives label objects explicitly so route copy ownership remains
in `App()`. The tools owner module owns only the repeated presentation and
local rendering conditions for each item.

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

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future maintainers of the `/tools` route
- Existing workaround or pain: behaviorful tools JSX lived inline in `App.tsx`.
- Smallest useful slice: move only group/item presentation after
  characterization exists.
- Success metric or signal: build and tools characterization pass.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: tools directory toggle and Telegram linking start
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke:
  - `npm run test:tools-directory`
  - `npm run smoke:routes`
- Rollback or disable path: revert the component extraction

- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: unchanged frontend client path
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: yes
- Error state verified: yes
- Refresh/restart behavior verified: built-dist route load
- Regression check performed:
  - `npm run build`
  - `npm run test:tools-directory`
  - `npm run smoke:routes`

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no new data handled
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: error state remains characterized
- Residual risk: no real provider credentials are exercised by this frontend
  extraction

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary:
  - extracted tools directory group/item presentation to
    `ToolsDirectoryGroupList`.
- Files changed:
  - `.codex/tasks/PRJ-1106-tools-directory-group-item-presentation-extraction.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/tools.tsx`
- How tested:
  - `npm run build`
  - `npm run test:tools-directory`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - remaining `App.tsx` maps are data projections or ref-sensitive route maps.
- Next steps:
  - `PRJ-1107` audit remaining frontend map boundaries after tools directory
    extraction.
- Decisions made:
  - keep route-owned API/state/effect handlers in `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - `/tools` repeated group/item JSX lived inline in `App.tsx`.
- Gaps:
  - none after `PRJ-1105`; behavior characterization exists.
- Inconsistencies:
  - none found.
- Architecture constraints:
  - route state and side effects stay in `App()`.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1106` extract tools directory group/item presentation.
- Priority rationale:
  - it is the next smallest implementation after tools behavior proof.
- Why other candidates were deferred:
  - chat transcript and mobile tabbar maps remain ref-sensitive.
  - pure route data projections are not presentation extraction targets.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/components/tools.tsx`
  - `web/src/App.tsx`
  - docs/context/task files
- Logic:
  - move repeated group/item rendering to a component and pass labels/callbacks.
- Edge cases:
  - saving toggle state, Telegram link busy state, link code display, and empty
    group list.

### 4. Execute Implementation
- Implementation notes:
  - `ToolsDirectoryGroupList` now renders the group and item cards.
  - `App()` passes route copy, common labels, busy state, link state, and
    callbacks explicitly.

### 5. Verify and Test
- Validation performed:
  - `npm run build`
  - `npm run test:tools-directory`
  - `npm run smoke:routes`
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - move only group wrapper and leave item cards in `App()`.
- Technical debt introduced: no
- Scalability assessment:
  - the component is route-owned, typed, and uses existing tools helpers.
- Refinements made:
  - removed stale tool-formatting imports from `App.tsx`.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
