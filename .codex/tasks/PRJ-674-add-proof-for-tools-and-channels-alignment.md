# Task

## Header
- ID: PRJ-674
- Title: Add proof that tools and channels UI stays aligned with backend truth
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-670, PRJ-671, PRJ-672, PRJ-673
- Priority: P1

## Context
The tools screen must remain truthful over time. Existing repo standards
already require release smoke, tests, and context synchronization for new
product-facing boundaries.

## Goal
Add validation, test coverage, and documentation so tools and channels state
remain aligned across backend API, web UI, and deployment truth.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- reuse existing release and regression patterns where possible

## Definition of Done
- [x] Focused backend and web validations cover the tools overview flow.
- [x] Release or smoke guidance includes the tools and channels truth checks
  when relevant to deploy scope.
- [x] Canonical docs describe the new app-facing tools boundary and its limits.
- [x] Context files are synchronized with the delivered baseline.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "tools_overview or tools_preferences or telegram_link"; Pop-Location`
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py; Pop-Location`
  - `Push-Location web; npm run build; Pop-Location`
- Manual checks:
  - docs now direct operators to verify `/app/tools/overview`,
    `/app/tools/preferences`, and `/app/tools/telegram/link/start` as the
    backend-owned product boundary when a release touches tools/channels
- Screenshots/logs:
- High-risk checks: ensure no UI state claims provider readiness or linkage
  that backend does not confirm

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md; docs/architecture/26_env_and_config.md; docs/engineering/testing.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing and product-shell docs

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This task should explicitly guard against the web client becoming a second
source of truth for connector availability.
