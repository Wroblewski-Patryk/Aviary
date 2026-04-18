# LEARNING_JOURNAL

Purpose: keep a compact memory of recurring execution pitfalls and verified
fixes for this repository.

## Update Rules

- Add or update an entry when a failure pattern is reproducible or documented.
- Prefer updating an existing entry over creating duplicates.
- Keep entries in English and free of secrets.
- Apply the new guardrail in the same task where the learning is captured.

## Entry Template

```markdown
### YYYY-MM-DD - Short Title
- Context:
- Symptom:
- Root cause:
- Guardrail:
- Preferred pattern:
- Avoid:
- Evidence:
```

## Entries

### 2026-04-18 - Schema work must validate both migration and startup paths
- Context: database and runtime tasks while the repository still carries both
  Alembic baseline ownership and a compatibility `create_tables()` startup path.
- Symptom: a schema change can appear correct in one path while still drifting
  in the other, which creates false confidence and hidden startup regressions.
- Root cause: schema ownership is temporarily split between formal migrations
  and MVP bootstrap convenience behavior.
- Guardrail: until migration-first ownership fully replaces startup bootstrap,
  every schema-affecting task must validate both the migration path and the
  current runtime startup assumptions, then sync docs and project state.
- Preferred pattern:
  - update Alembic or schema files
  - run targeted schema or runtime tests
  - verify startup assumptions still hold
  - record the dual-path impact in docs or project state
- Avoid:
  - treating Alembic success alone as sufficient proof that the runtime startup
    path is still safe
- Evidence:
  - migration-first default and compatibility-path decision trail recorded in
    `.codex/context/PROJECT_STATE.md` and `docs/planning/open-decisions.md`

### 2026-04-18 - Validation commands must match real test inventory
- Context: task-board validation commands during stage-boundary and contract-test
  slices.
- Symptom: a validation command can fail immediately with "file not found" even
  when code changes are correct.
- Root cause: task metadata drifted to a stale test path
  (`tests/test_telegram_webhook.py`) that no longer exists in the repository.
- Guardrail: before running or recording a task validation command, verify each
  referenced test path exists in `tests/`.
- Preferred pattern:
  - check planned test files against repository inventory
  - update task-board and planning validation commands when paths changed
  - run the corrected command and record the exact passing output scope
- Avoid:
  - copying historical validation snippets without path existence checks
- Evidence:
  - `PRJ-018` validation command corrected to existing tests in
    `.codex/context/TASK_BOARD.md`
  - full regression remained green after the correction
