---
id: "FILE-BACKEND-MIGRATIONS-ENV-PY-6383787F"
name: "env.py"
type: "data_file"
status: "implemented"
layer: "database"
module: "backend"
feature: "data_model"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/migrations/env.py"
related_files: []
tags: ["auto", "data"]
---

# env.py

ID: `FILE-BACKEND-MIGRATIONS-ENV-PY-6383787F`

## Summary

Repository file `backend/migrations/env.py` auto-discovered for architecture graph inventory.

## Links

- parent: none
- children: none
- depends_on: none
- used_by: none
- ui_related: none
- api_related: none
- database_related: none
- tests_related: none
- docs_related: none
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[pyfunc-backend-migrations-env-py-resolve-database-url-a240a877|PYFUNC-BACKEND-MIGRATIONS-ENV-PY-RESOLVE-DATABASE-URL-A240A877]]: `backend/migrations/env.py` contains function `_resolve_database_url`.
- `parent_of` -> [[pyfunc-backend-migrations-env-py-run-migrations-offline-f1ac05cb|PYFUNC-BACKEND-MIGRATIONS-ENV-PY-RUN-MIGRATIONS-OFFLINE-F1AC05CB]]: `backend/migrations/env.py` contains function `run_migrations_offline`.
- `parent_of` -> [[pyfunc-backend-migrations-env-py-run-sync-migrations-8ea7404e|PYFUNC-BACKEND-MIGRATIONS-ENV-PY-RUN-SYNC-MIGRATIONS-8EA7404E]]: `backend/migrations/env.py` contains function `_run_sync_migrations`.
- `parent_of` -> [[pyfunc-backend-migrations-env-py-run-migrations-online-764c88f9|PYFUNC-BACKEND-MIGRATIONS-ENV-PY-RUN-MIGRATIONS-ONLINE-764C88F9]]: `backend/migrations/env.py` contains function `run_migrations_online`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
