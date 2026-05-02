# V1 Commit Scope Audit

Last updated: 2026-05-02

## Purpose

This document records the current release-candidate commit scope after the
`v1` boundary was frozen in `docs/planning/current-v1-release-boundary.md`.

## Candidate Base

- Base remote: `origin/main`
- Base commit: `5372d33a4fd132bc6280bb781642eb3ce55fbfdc`
- Candidate head: `350250fa7ee737863f72cdeb6c876d7fc39e17e1`
- Local branch posture: `main` is ahead of `origin/main` by 2 commits.

## Candidate Commits

1. `2c5cf8b chore: capture canonical ui and v1 audit baseline`
   - captures the canonical UI/localization task records
   - includes the backend-backed recent activity surface
   - records the fresh v1 audit and execution plan
   - includes prior validation evidence from PRJ-901 and PRJ-902
2. `350250f docs: freeze current v1 release boundary`
   - freezes the current `v1` scope
   - separates core blockers, included web checks, extension gates, and
     hardening gates

## Included Scope

- backend additive `/app/personality/overview.recent_activity` projection
- backend test coverage for authenticated user-scoped recent activity
- canonical web shell and route polish captured in the current UI baseline
- localized module/copy task records and evidence notes
- v1 audit and release-boundary planning sources
- task board, project state, and learning journal updates required by the
  repository workflow

## Excluded Scope

- local `artifacts/behavior_validation/prj843-report.json`
- generated `.codex/artifacts/...` evidence files that are intentionally not
  committed by default
- organizer provider credential activation
- multimodal Telegram
- mobile/Expo restart
- new external observability stack
- AI red-team scenario implementation

## Dirty Tree Result

The candidate tracked tree is clean after the PRJ-903 commit. The only
remaining untracked path is local artifact output:

- `artifacts/behavior_validation/prj843-report.json`

That path is excluded from the release candidate. It should either stay local
or be handled by a separate artifact-retention decision; it must not be swept
into the candidate commit.

## Validation Evidence Available Before PRJ-905

- `PRJ-901` full backend gate: `1019 passed`
- `PRJ-901` web build: passed
- `PRJ-902` behavior validation: `19 passed, 209 deselected`
- `PRJ-903` commit diff check: passed after amend

This evidence is useful but not enough for the next release step because the
candidate head is now `350250fa7ee737863f72cdeb6c876d7fc39e17e1`. PRJ-905 must
run the current candidate validation gate against this head.

## Next Gate

`PRJ-905` must run and record:

1. full backend pytest gate
2. web production build
3. behavior validation with an artifact path under `.codex/artifacts/prj905-*`
4. `git diff --check`
5. final candidate status, including whether untracked local artifacts remain
   excluded
