# V1 Candidate Validation Gate

Last updated: 2026-05-02

## Candidate

- Candidate head: `463ad04bc147c1284d0f1e12b4d5ff0cabec6fa1`
- Branch posture before this validation record commit: `main` ahead of
  `origin/main` by 3 commits
- Release boundary:
  `docs/planning/current-v1-release-boundary.md`
- Commit-scope audit:
  `docs/planning/v1-commit-scope-audit.md`

## Validation Results

| Gate | Command | Result |
| --- | --- | --- |
| Full backend tests | `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location` | Passed, `1019 passed` |
| Web production build | `Push-Location .\web; npm run build; Pop-Location` | Passed |
| Behavior validation | `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_behavior_validation.py --gate-mode operator --artifact-path ..\.codex\artifacts\prj905-v1-candidate-validation\behavior-validation-report.json; Pop-Location` | Passed, `19 passed, 209 deselected` |
| Diff hygiene | `git diff --check` | Passed |

Behavior validation artifact:

- `.codex/artifacts/prj905-v1-candidate-validation/behavior-validation-report.json`

## Candidate Status

The current candidate passed the local validation gate and is ready for
publishing in PRJ-906.

Remaining local-only output:

- `artifacts/behavior_validation/prj843-report.json`

That artifact remains excluded from the candidate. It should not be committed
as part of PRJ-906 unless a separate artifact-retention decision changes the
release evidence policy.

## Release Implication

This gate proves the candidate locally. It does not prove live production.
PRJ-906 must publish the candidate, and PRJ-907 must run production release
smoke with deployed revision parity before `v1` can be called production-green.
