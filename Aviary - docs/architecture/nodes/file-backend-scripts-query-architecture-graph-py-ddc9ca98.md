---
id: "FILE-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-DDC9CA98"
name: "query_architecture_graph.py"
type: "file"
status: "implemented"
layer: "backend"
module: "backend"
feature: "inventory"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/scripts/query_architecture_graph.py"
related_files: []
tags: ["auto"]
---

# query_architecture_graph.py

ID: `FILE-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-DDC9CA98`

## Summary

Repository file `backend/scripts/query_architecture_graph.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-scripts-query-architecture-graph-py-graphindexes-32d86fd7|PYCLASS-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-GRAPHINDEXES-32D86FD7]]: `backend/scripts/query_architecture_graph.py` contains class `GraphIndexes`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-repo-root-fb757c23|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-REPO-ROOT-FB757C23]]: `backend/scripts/query_architecture_graph.py` contains function `repo_root`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-default-graph-path-31f59955|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-DEFAULT-GRAPH-PATH-31F59955]]: `backend/scripts/query_architecture_graph.py` contains function `default_graph_path`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-split-refs-3591d287|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-SPLIT-REFS-3591D287]]: `backend/scripts/query_architecture_graph.py` contains function `split_refs`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-split-chain-nodes-83aa7e08|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-SPLIT-CHAIN-NODES-83AA7E08]]: `backend/scripts/query_architecture_graph.py` contains function `split_chain_nodes`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-load-graph-2abf19ea|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-LOAD-GRAPH-2ABF19EA]]: `backend/scripts/query_architecture_graph.py` contains function `load_graph`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-build-indexes-6b44fbb8|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-BUILD-INDEXES-6B44FBB8]]: `backend/scripts/query_architecture_graph.py` contains function `build_indexes`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-search-nodes-0c28bc19|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-SEARCH-NODES-0C28BC19]]: `backend/scripts/query_architecture_graph.py` contains function `search_nodes`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-suggest-nodes-c7b78941|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-SUGGEST-NODES-C7B78941]]: `backend/scripts/query_architecture_graph.py` contains function `suggest_nodes`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-find-node-5b3f411f|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-FIND-NODE-5B3F411F]]: `backend/scripts/query_architecture_graph.py` contains function `find_node`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-detect-gaps-026988be|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-DETECT-GAPS-026988BE]]: `backend/scripts/query_architecture_graph.py` contains function `detect_gaps`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-query-node-560cd0e9|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-QUERY-NODE-560CD0E9]]: `backend/scripts/query_architecture_graph.py` contains function `query_node`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-gap-report-fc3ddbca|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-GAP-REPORT-FC3DDBCA]]: `backend/scripts/query_architecture_graph.py` contains function `gap_report`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-relation-line-c0bbb104|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-RELATION-LINE-C0BBB104]]: `backend/scripts/query_architecture_graph.py` contains function `relation_line`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-render-search-markd-bb9890e5|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-RENDER-SEARCH-MARKD-BB9890E5]]: `backend/scripts/query_architecture_graph.py` contains function `render_search_markdown`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-render-gap-report-m-c26bda72|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-RENDER-GAP-REPORT-M-C26BDA72]]: `backend/scripts/query_architecture_graph.py` contains function `render_gap_report_markdown`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-render-node-markdow-a73df9d4|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-RENDER-NODE-MARKDOW-A73DF9D4]]: `backend/scripts/query_architecture_graph.py` contains function `render_node_markdown`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-parse-args-2fd23549|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-PARSE-ARGS-2FD23549]]: `backend/scripts/query_architecture_graph.py` contains function `parse_args`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-run-1f620bf1|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-RUN-1F620BF1]]: `backend/scripts/query_architecture_graph.py` contains function `run`.
- `parent_of` -> [[pyfunc-backend-scripts-query-architecture-graph-py-main-00cad7c8|PYFUNC-BACKEND-SCRIPTS-QUERY-ARCHITECTURE-GRAPH-PY-MAIN-00CAD7C8]]: `backend/scripts/query_architecture_graph.py` contains function `main`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
