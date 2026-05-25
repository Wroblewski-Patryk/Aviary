---
id: "FILE-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-5EF4EDBE"
name: "generate_architecture_graph.py"
type: "file"
status: "implemented"
layer: "backend"
module: "backend"
feature: "inventory"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/scripts/generate_architecture_graph.py"
related_files: []
tags: ["auto"]
---

# generate_architecture_graph.py

ID: `FILE-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-5EF4EDBE`

## Summary

Repository file `backend/scripts/generate_architecture_graph.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-scripts-generate-architecture-graph-py-registry-09199661|PYCLASS-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-REGISTRY-09199661]]: `backend/scripts/generate_architecture_graph.py` contains class `Registry`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-repo-root-77bb6952|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-REPO-ROOT-77BB6952]]: `backend/scripts/generate_architecture_graph.py` contains function `repo_root`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-read-csv-58d342b9|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-READ-CSV-58D342B9]]: `backend/scripts/generate_architecture_graph.py` contains function `read_csv`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-split-refs-0450a75b|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-SPLIT-REFS-0450A75B]]: `backend/scripts/generate_architecture_graph.py` contains function `split_refs`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-slug-8db32925|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-SLUG-8DB32925]]: `backend/scripts/generate_architecture_graph.py` contains function `slug`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-md-link-45afa3dc|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-MD-LINK-45AFA3DC]]: `backend/scripts/generate_architecture_graph.py` contains function `md_link`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-yaml-list-b2d4b72c|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-YAML-LIST-B2D4B72C]]: `backend/scripts/generate_architecture_graph.py` contains function `yaml_list`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-validate-registr-5f2a992d|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-VALIDATE-REGISTR-5F2A992D]]: `backend/scripts/generate_architecture_graph.py` contains function `validate_registry`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-load-registry-e1837ae4|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-LOAD-REGISTRY-E1837AE4]]: `backend/scripts/generate_architecture_graph.py` contains function `load_registry`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-relation-maps-06f93cf1|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-RELATION-MAPS-06F93CF1]]: `backend/scripts/generate_architecture_graph.py` contains function `relation_maps`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-evidence-map-1beb832e|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-EVIDENCE-MAP-1BEB832E]]: `backend/scripts/generate_architecture_graph.py` contains function `evidence_map`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-chain-map-90ef9bf9|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-CHAIN-MAP-90EF9BF9]]: `backend/scripts/generate_architecture_graph.py` contains function `chain_map`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-theory-claim-map-dcf79164|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-THEORY-CLAIM-MAP-DCF79164]]: `backend/scripts/generate_architecture_graph.py` contains function `theory_claim_map`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-node-pages-37d44e31|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-NODE-PAGES-37D44E31]]: `backend/scripts/generate_architecture_graph.py` contains function `write_node_pages`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-relations-d953aad6|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-RELATIONS-D953AAD6]]: `backend/scripts/generate_architecture_graph.py` contains function `write_relations_index`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-chains-ind-dedf0319|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-CHAINS-IND-DEDF0319]]: `backend/scripts/generate_architecture_graph.py` contains function `write_chains_index`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-graph-expo-d2fb13de|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-GRAPH-EXPO-D2FB13DE]]: `backend/scripts/generate_architecture_graph.py` contains function `write_graph_exports`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-status-rol-40abefc8|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-STATUS-ROL-40ABEFC8]]: `backend/scripts/generate_architecture_graph.py` contains function `write_status_rollup`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-evidence-r-1922062c|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-EVIDENCE-R-1922062C]]: `backend/scripts/generate_architecture_graph.py` contains function `write_evidence_rollup`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-write-research-r-8812b61b|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-WRITE-RESEARCH-R-8812B61B]]: `backend/scripts/generate_architecture_graph.py` contains function `write_research_rollup`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-graph-py-main-7791c53b|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-GRAPH-PY-MAIN-7791C53B]]: `backend/scripts/generate_architecture_graph.py` contains function `main`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
