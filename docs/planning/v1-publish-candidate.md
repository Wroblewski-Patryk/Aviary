# V1 Publish Candidate

Last updated: 2026-05-02

## Published Candidate

- Validated candidate commit: `582b146cdd89a488acc6bcebee4c00a7c418d108`
- Remote: `origin/main`
- Push result: local `main` was pushed to `origin/main`
- Push range: `5372d33..582b146`

## Published Scope

The pushed scope includes:

- canonical UI and localization baseline captured in the current web shell
- backend-backed recent activity surface
- v1 audit and execution plan
- current v1 release boundary
- v1 commit-scope audit
- v1 local candidate validation record

## Excluded Scope

- `artifacts/behavior_validation/prj843-report.json`
- generated `.codex/artifacts/...` validation output
- organizer provider credential activation
- multimodal Telegram
- mobile/Expo restart
- external observability stack
- AI red-team scenario implementation

## Validation Before Push

The pushed candidate was validated by PRJ-905:

- backend tests: `1019 passed`
- web production build: passed
- behavior validation: `19 passed, 209 deselected`
- diff hygiene: passed

## Next Gate

PRJ-907 must prove production deployment parity. Until release smoke passes
against production, the release is published to `origin/main` but not
production-green.
