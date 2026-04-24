# Task

## Header
- ID: PRJ-618
- Title: Freeze the first live website-reading workflow baseline
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-617
- Priority: P0

## Context
Search and browser tool families already exist, but the user-facing daily-use workflow "check this website and tell me what is on it" is not yet frozen as an explicit production behavior contract.

## Goal
Define the bounded first-class website-reading workflow for no-UI `v1`.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] One explicit bounded website-reading workflow is documented.
- [x] The workflow names input, output, safety, and memory-capture boundaries.
- [x] Planning docs and context agree on the same baseline.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: not run; docs-and-contract-only slice
- Manual checks: architecture/product/runtime cross-review
- Screenshots/logs:
- High-risk checks: keep website reading inside existing search/browser -> action -> memory boundary

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/16_agent_contracts.md`, `docs/architecture/10_future_vision.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: likely contracts/runtime reality if wording is widened

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The baseline should cover "read a page and summarize it" and optionally "search first, then inspect the chosen page".

Completion notes:

- canonical workflow baseline is now frozen in `docs/architecture/10_future_vision.md`
  and `docs/architecture/16_agent_contracts.md`
- the workflow stays inside the existing `knowledge_search -> web_browser ->
  action -> tool_grounded_learning` boundary
- direct URL review and search-first review are both allowed, but output stays
  bounded to summary-level page evidence and source notes
- next slice `PRJ-619` should expose this same workflow as one operator-visible
  readiness and guardrail surface through existing backend truth
