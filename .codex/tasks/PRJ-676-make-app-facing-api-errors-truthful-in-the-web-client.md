# Task

## Header
- ID: PRJ-676
- Title: Make app-facing API errors truthful in the web client
- Status: READY
- Owner: Frontend Builder
- Depends on: PRJ-675
- Priority: P0

## Context
The current shared browser API helper parses every non-empty response body as
JSON. When backend routes fail with plain-text `Internal Server Error`, the
first-party web shell surfaces a JSON parser exception instead of the real
route failure, which hides the actual product issue and makes debugging
misleading.

## Goal
Repair the shared web API helper so the browser client reports app-facing
backend failures truthfully across success, error, empty-body, and non-JSON
error responses.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Shared client transport logic no longer throws JSON parser noise for
      plain-text backend failures.
- [ ] Browser-visible error messages preserve truthful route failure detail or
      a stable fallback instead of parser exceptions.
- [ ] Focused client-side regression coverage protects the repaired behavior.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
- Screenshots/logs:
- High-risk checks:

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md;
  docs/architecture/27_codex_instructions.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

## Review Checklist (mandatory)
- [ ] Architecture alignment confirmed.
- [ ] Existing systems were reused where applicable.
- [ ] No workaround paths were introduced.
- [ ] No logic duplication was introduced.
- [ ] Definition of Done evidence is attached.
- [ ] Relevant validations were run.
- [ ] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The repair must stay inside the existing web transport helper instead of
creating route-specific parsing paths.
