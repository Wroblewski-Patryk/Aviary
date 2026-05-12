# Task

## Header
- ID: PRJ-818
- Title: Harden frontend Chrome characterization launch
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-817
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 818
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Rendered frontend evidence remains blocked. `npm run smoke:routes` now fails
locally because headless Chrome exits with `GPU process isn't usable` despite
the existing `--disable-gpu` flag.

## Goal
Make existing frontend Chrome-based characterization/smoke harnesses more
robust in the current Windows desktop environment without changing product
runtime behavior.

## Scope
- `web/scripts/route-smoke.mjs`
- `web/scripts/chat-transcript-characterization.mjs`
- `web/scripts/tools-directory-characterization.mjs`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`

## Success Signal
- User or operator problem: rendered frontend smoke evidence is blocked by
  local Chrome GPU startup failure or CDP hangs.
- Expected product or reliability outcome: route smoke and existing
  characterization scripts launch Chrome with safer headless flags.
- How success will be observed: route smoke passes, or the remaining blocker is
  narrower and recorded with evidence.
- Post-launch learning needed: yes

## Deliverable For This Stage
Verified Chrome/CDP harness hardening with bounded failure evidence for the
current local blocker.

## Constraints
- use existing scripts and approved mechanisms
- do not add a new browser framework
- do not change product runtime behavior
- do not claim visual proof unless rendered commands actually pass
- keep changes small and reversible

## Implementation Plan
1. Identify the Chrome startup failure mode from existing smoke output.
2. Add conservative headless stability flags to existing Chrome launch arrays.
3. Re-run route smoke and targeted characterization scripts.
4. Record exact pass/fail evidence and update context.

## Acceptance Criteria
- Chrome launch flags are consistent across frontend smoke/characterization
  scripts.
- `npm run smoke:routes` is retried after hardening.
- At least one existing rendered frontend harness passes, or the blocker is
  documented as still outside the code-level harness.
- Source-of-truth files record the outcome honestly.

## Definition of Done
- [x] launch hardening is implemented
- [x] relevant frontend harnesses are run
- [x] source-of-truth files are updated

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
    -> failed fast with `Chrome timed out while dumping DOM`
  - `Push-Location .\web; npm run test:chat-transcript; Pop-Location`
    -> failed fast with `Timed out waiting for CDP response to Page.enable`
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location`
    -> failed fast with `Timed out waiting for CDP response to Page.enable`
  - `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
    -> passed
  - `git diff --check` -> passed with LF/CRLF warnings only
- Manual checks:
  - confirmed stale Node test processes were stopped after timeout experiments
- Screenshots/logs:
  - no screenshot proof; rendered paths remain blocked
- High-risk checks:
  - product runtime code was not changed

## Result Report
- Task summary: added bounded Chrome/CDP launch and command failure behavior to
  existing frontend rendered harnesses.
- Files changed:
  - `web/scripts/route-smoke.mjs`
  - `web/scripts/chat-transcript-characterization.mjs`
  - `web/scripts/tools-directory-characterization.mjs`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
  - `docs/planning/next-iteration-plan.md`
- How tested:
  - `npm run smoke:routes`
  - `npm run test:chat-transcript`
  - `npm run test:tools-directory`
  - `npm run test:connector-confirmation`
  - `git diff --check`
- What is incomplete: local rendered proof still does not pass because Chrome
  dump-dom and CDP are not responding normally in this host.
- Next steps: use an alternate rendered validation path or run the harnesses on
  a host where headless Chrome works normally.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: local rendered harnesses fail before useful DOM/screenshot evidence.
- Gaps: Chrome launch flags are not robust enough for current Windows desktop
  headless behavior.
- Inconsistencies: source-contract characterization passes, but rendered route
  smoke does not.
- Architecture constraints: no runtime/product behavior changes.

### 2. Select One Priority Task
- Selected task: `PRJ-818` harden frontend Chrome characterization launch.
- Priority rationale: it directly targets the rendered-evidence blocker.
- Why other candidates were deferred: broader UI parity should wait for a
  stable rendered evidence path.

### 3. Plan Implementation
- Files or surfaces to modify: existing Chrome launch arrays in web scripts.
- Logic: add conservative headless flags and retry existing scripts.
- Edge cases: Chrome may still be blocked by OS permissions; record honestly.

### 4. Execute Implementation
- Implementation notes:
  - added conservative headless GPU-disable flags to existing Chrome launches
  - added a 30-second route-smoke DOM dump timeout
  - added bounded DevTools discovery fetches, Blob-safe WebSocket parsing, and
    10-second CDP command timeouts to CDP characterization scripts

### 5. Verify and Test
- Validation performed:
  - route smoke, chat transcript characterization, tools directory
    characterization, connector confirmation characterization, and
    `git diff --check`
- Result:
  - connector confirmation source-contract characterization passed
  - rendered Chrome/CDP harnesses now fail fast with actionable environment
    blockers rather than hanging

### 6. Self-Review
- Simpler option considered: leave only source-contract proof; rejected because
  route smoke exposes a concrete harness startup failure.
- Technical debt introduced: no product debt; harnesses still need a host that
  can run headless Chrome normally for rendered proof.
- Refinements made: removed the `--single-process` experiment because it caused
  long hangs in this host.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/next-iteration-plan.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.agents/state/current-focus.md`
  - `.agents/state/next-steps.md`
  - `.agents/state/system-health.md`
