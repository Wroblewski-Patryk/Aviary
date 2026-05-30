# Architecture Awareness Report

Generated: 2026-05-30T22:14:11.106665+00:00
Project: Personality
Root: C:/Personal/Projekty/Aplikacje/Aviary

## Counts By Type

| Type | Count |
| --- | ---: |
| agent | 6 |
| api_file | 4 |
| api_route | 6 |
| backend_file | 111 |
| class | 241 |
| component | 148 |
| component_file | 9 |
| config | 46 |
| data_file | 20 |
| documentation | 1110 |
| event | 1 |
| feature | 10 |
| file | 65 |
| frontend_file | 14 |
| function | 2862 |
| mobile_file | 23 |
| model | 2 |
| page | 4 |
| prompt | 1 |
| script | 2 |
| service | 3 |
| test | 68 |
| ui_element | 735 |
| workflow | 3 |

## Counts By Status

| Status | Count |
| --- | ---: |
| implemented | 4275 |
| verified | 1219 |

## Health Signals

- Implementation entities without inferred tests: 4275
- Implementation entities without inferred docs: 4275
- Entities without relation links: 1213
- Function journey rows: 11
- User action rows: 893

## Top Missing Test Links

- config: architecture-graph.yml (.github/workflows/architecture-graph.yml)
- config: page-2026-04-15T20-44-25-347Z.yml (.playwright-cli/page-2026-04-15T20-44-25-347Z.yml)
- config: page-2026-04-15T20-44-46-172Z.yml (.playwright-cli/page-2026-04-15T20-44-46-172Z.yml)
- config: page-2026-04-15T20-44-59-639Z.yml (.playwright-cli/page-2026-04-15T20-44-59-639Z.yml)
- config: page-2026-04-15T20-45-28-282Z.yml (.playwright-cli/page-2026-04-15T20-45-28-282Z.yml)
- config: page-2026-04-15T20-45-50-133Z.yml (.playwright-cli/page-2026-04-15T20-45-50-133Z.yml)
- config: page-2026-04-15T20-46-04-677Z.yml (.playwright-cli/page-2026-04-15T20-46-04-677Z.yml)
- config: page-2026-04-15T20-46-21-330Z.yml (.playwright-cli/page-2026-04-15T20-46-21-330Z.yml)
- config: page-2026-04-15T20-46-40-337Z.yml (.playwright-cli/page-2026-04-15T20-46-40-337Z.yml)
- config: page-2026-04-15T20-46-57-571Z.yml (.playwright-cli/page-2026-04-15T20-46-57-571Z.yml)
- config: page-2026-04-15T20-47-15-058Z.yml (.playwright-cli/page-2026-04-15T20-47-15-058Z.yml)
- config: page-2026-04-15T20-47-36-166Z.yml (.playwright-cli/page-2026-04-15T20-47-36-166Z.yml)
- config: page-2026-04-15T20-48-28-321Z.yml (.playwright-cli/page-2026-04-15T20-48-28-321Z.yml)
- config: page-2026-04-15T20-48-42-079Z.yml (.playwright-cli/page-2026-04-15T20-48-42-079Z.yml)
- config: page-2026-04-15T20-53-08-945Z.yml (.playwright-cli/page-2026-04-15T20-53-08-945Z.yml)
- config: page-2026-04-15T20-53-17-733Z.yml (.playwright-cli/page-2026-04-15T20-53-17-733Z.yml)
- config: page-2026-04-15T20-53-32-053Z.yml (.playwright-cli/page-2026-04-15T20-53-32-053Z.yml)
- config: page-2026-04-15T20-53-49-407Z.yml (.playwright-cli/page-2026-04-15T20-53-49-407Z.yml)
- config: page-2026-04-15T20-59-47-745Z.yml (.playwright-cli/page-2026-04-15T20-59-47-745Z.yml)
- config: page-2026-04-15T21-00-13-902Z.yml (.playwright-cli/page-2026-04-15T21-00-13-902Z.yml)
- config: page-2026-04-15T21-00-52-690Z.yml (.playwright-cli/page-2026-04-15T21-00-52-690Z.yml)
- config: page-2026-04-15T21-01-06-365Z.yml (.playwright-cli/page-2026-04-15T21-01-06-365Z.yml)
- config: page-2026-04-15T21-01-17-645Z.yml (.playwright-cli/page-2026-04-15T21-01-17-645Z.yml)
- config: page-2026-04-15T21-01-37-282Z.yml (.playwright-cli/page-2026-04-15T21-01-37-282Z.yml)
- config: page-2026-04-15T21-01-54-855Z.yml (.playwright-cli/page-2026-04-15T21-01-54-855Z.yml)
- config: page-2026-04-15T21-02-10-679Z.yml (.playwright-cli/page-2026-04-15T21-02-10-679Z.yml)
- config: page-2026-04-15T21-02-19-568Z.yml (.playwright-cli/page-2026-04-15T21-02-19-568Z.yml)
- config: page-2026-04-15T21-02-55-893Z.yml (.playwright-cli/page-2026-04-15T21-02-55-893Z.yml)
- config: page-2026-04-15T21-03-38-638Z.yml (.playwright-cli/page-2026-04-15T21-03-38-638Z.yml)
- config: page-2026-04-15T21-06-30-601Z.yml (.playwright-cli/page-2026-04-15T21-06-30-601Z.yml)
- config: page-2026-04-15T21-06-58-044Z.yml (.playwright-cli/page-2026-04-15T21-06-58-044Z.yml)
- config: page-2026-04-15T21-07-13-831Z.yml (.playwright-cli/page-2026-04-15T21-07-13-831Z.yml)
- config: page-2026-04-15T21-07-33-964Z.yml (.playwright-cli/page-2026-04-15T21-07-33-964Z.yml)
- config: page-2026-04-15T21-07-47-990Z.yml (.playwright-cli/page-2026-04-15T21-07-47-990Z.yml)
- config: page-2026-04-15T21-08-01-514Z.yml (.playwright-cli/page-2026-04-15T21-08-01-514Z.yml)
- config: page-2026-04-15T21-08-17-705Z.yml (.playwright-cli/page-2026-04-15T21-08-17-705Z.yml)
- config: page-2026-04-15T21-29-42-720Z.yml (.playwright-cli/page-2026-04-15T21-29-42-720Z.yml)
- config: page-2026-04-15T21-30-17-426Z.yml (.playwright-cli/page-2026-04-15T21-30-17-426Z.yml)
- config: page-2026-04-15T21-30-24-877Z.yml (.playwright-cli/page-2026-04-15T21-30-24-877Z.yml)
- backend_file: __init__.py (backend/app/__init__.py)

## Top Missing Doc Links

- config: architecture-graph.yml (.github/workflows/architecture-graph.yml)
- config: page-2026-04-15T20-44-25-347Z.yml (.playwright-cli/page-2026-04-15T20-44-25-347Z.yml)
- config: page-2026-04-15T20-44-46-172Z.yml (.playwright-cli/page-2026-04-15T20-44-46-172Z.yml)
- config: page-2026-04-15T20-44-59-639Z.yml (.playwright-cli/page-2026-04-15T20-44-59-639Z.yml)
- config: page-2026-04-15T20-45-28-282Z.yml (.playwright-cli/page-2026-04-15T20-45-28-282Z.yml)
- config: page-2026-04-15T20-45-50-133Z.yml (.playwright-cli/page-2026-04-15T20-45-50-133Z.yml)
- config: page-2026-04-15T20-46-04-677Z.yml (.playwright-cli/page-2026-04-15T20-46-04-677Z.yml)
- config: page-2026-04-15T20-46-21-330Z.yml (.playwright-cli/page-2026-04-15T20-46-21-330Z.yml)
- config: page-2026-04-15T20-46-40-337Z.yml (.playwright-cli/page-2026-04-15T20-46-40-337Z.yml)
- config: page-2026-04-15T20-46-57-571Z.yml (.playwright-cli/page-2026-04-15T20-46-57-571Z.yml)
- config: page-2026-04-15T20-47-15-058Z.yml (.playwright-cli/page-2026-04-15T20-47-15-058Z.yml)
- config: page-2026-04-15T20-47-36-166Z.yml (.playwright-cli/page-2026-04-15T20-47-36-166Z.yml)
- config: page-2026-04-15T20-48-28-321Z.yml (.playwright-cli/page-2026-04-15T20-48-28-321Z.yml)
- config: page-2026-04-15T20-48-42-079Z.yml (.playwright-cli/page-2026-04-15T20-48-42-079Z.yml)
- config: page-2026-04-15T20-53-08-945Z.yml (.playwright-cli/page-2026-04-15T20-53-08-945Z.yml)
- config: page-2026-04-15T20-53-17-733Z.yml (.playwright-cli/page-2026-04-15T20-53-17-733Z.yml)
- config: page-2026-04-15T20-53-32-053Z.yml (.playwright-cli/page-2026-04-15T20-53-32-053Z.yml)
- config: page-2026-04-15T20-53-49-407Z.yml (.playwright-cli/page-2026-04-15T20-53-49-407Z.yml)
- config: page-2026-04-15T20-59-47-745Z.yml (.playwright-cli/page-2026-04-15T20-59-47-745Z.yml)
- config: page-2026-04-15T21-00-13-902Z.yml (.playwright-cli/page-2026-04-15T21-00-13-902Z.yml)
- config: page-2026-04-15T21-00-52-690Z.yml (.playwright-cli/page-2026-04-15T21-00-52-690Z.yml)
- config: page-2026-04-15T21-01-06-365Z.yml (.playwright-cli/page-2026-04-15T21-01-06-365Z.yml)
- config: page-2026-04-15T21-01-17-645Z.yml (.playwright-cli/page-2026-04-15T21-01-17-645Z.yml)
- config: page-2026-04-15T21-01-37-282Z.yml (.playwright-cli/page-2026-04-15T21-01-37-282Z.yml)
- config: page-2026-04-15T21-01-54-855Z.yml (.playwright-cli/page-2026-04-15T21-01-54-855Z.yml)
- config: page-2026-04-15T21-02-10-679Z.yml (.playwright-cli/page-2026-04-15T21-02-10-679Z.yml)
- config: page-2026-04-15T21-02-19-568Z.yml (.playwright-cli/page-2026-04-15T21-02-19-568Z.yml)
- config: page-2026-04-15T21-02-55-893Z.yml (.playwright-cli/page-2026-04-15T21-02-55-893Z.yml)
- config: page-2026-04-15T21-03-38-638Z.yml (.playwright-cli/page-2026-04-15T21-03-38-638Z.yml)
- config: page-2026-04-15T21-06-30-601Z.yml (.playwright-cli/page-2026-04-15T21-06-30-601Z.yml)
- config: page-2026-04-15T21-06-58-044Z.yml (.playwright-cli/page-2026-04-15T21-06-58-044Z.yml)
- config: page-2026-04-15T21-07-13-831Z.yml (.playwright-cli/page-2026-04-15T21-07-13-831Z.yml)
- config: page-2026-04-15T21-07-33-964Z.yml (.playwright-cli/page-2026-04-15T21-07-33-964Z.yml)
- config: page-2026-04-15T21-07-47-990Z.yml (.playwright-cli/page-2026-04-15T21-07-47-990Z.yml)
- config: page-2026-04-15T21-08-01-514Z.yml (.playwright-cli/page-2026-04-15T21-08-01-514Z.yml)
- config: page-2026-04-15T21-08-17-705Z.yml (.playwright-cli/page-2026-04-15T21-08-17-705Z.yml)
- config: page-2026-04-15T21-29-42-720Z.yml (.playwright-cli/page-2026-04-15T21-29-42-720Z.yml)
- config: page-2026-04-15T21-30-17-426Z.yml (.playwright-cli/page-2026-04-15T21-30-17-426Z.yml)
- config: page-2026-04-15T21-30-24-877Z.yml (.playwright-cli/page-2026-04-15T21-30-24-877Z.yml)
- backend_file: __init__.py (backend/app/__init__.py)

## Notes

- This is a parity export derived from the canonical registry graph under `docs/architecture/graphs`.
- Missing link rows are explicit unknowns; they are not treated as verified behavior.
- `verified` claims still require fresh runtime/test evidence from task-level gates.
