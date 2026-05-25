---
id: "FILE-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-91086467"
name: "generate_architecture_inventory.py"
type: "file"
status: "implemented"
layer: "backend"
module: "backend"
feature: "inventory"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/scripts/generate_architecture_inventory.py"
related_files: []
tags: ["auto"]
---

# generate_architecture_inventory.py

ID: `FILE-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-91086467`

## Summary

Repository file `backend/scripts/generate_architecture_inventory.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-scripts-generate-architecture-inventory-py-inventory-ec1a0de0|PYCLASS-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-INVENTORY-EC1A0DE0]]: `backend/scripts/generate_architecture_inventory.py` contains class `Inventory`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-repo-root-d4cfdae8|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-REPO-ROOT-D4CFDAE8]]: `backend/scripts/generate_architecture_inventory.py` contains function `repo_root`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-norm-12721b4c|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-NORM-12721B4C]]: `backend/scripts/generate_architecture_inventory.py` contains function `norm`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-slug-0e1ae2ea|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-SLUG-0E1AE2EA]]: `backend/scripts/generate_architecture_inventory.py` contains function `slug`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-file-id-7e11dde8|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-FILE-ID-7E11DDE8]]: `backend/scripts/generate_architecture_inventory.py` contains function `file_id`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-symbol-id-e7107240|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-SYMBOL-ID-E7107240]]: `backend/scripts/generate_architecture_inventory.py` contains function `symbol_id`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-relation-id-f128ab70|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-RELATION-ID-F128AB70]]: `backend/scripts/generate_architecture_inventory.py` contains function `relation_id`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-row-27cfcd5f|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-ROW-27CFCD5F]]: `backend/scripts/generate_architecture_inventory.py` contains function `row`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-relation-978652be|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-RELATION-978652BE]]: `backend/scripts/generate_architecture_inventory.py` contains function `relation`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-should-scan-3e02161a|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-SHOULD-SCAN-3E02161A]]: `backend/scripts/generate_architecture_inventory.py` contains function `should_scan`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-classify-fil-ab7c1bd0|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-CLASSIFY-FIL-AB7C1BD0]]: `backend/scripts/generate_architecture_inventory.py` contains function `classify_file`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-package-for-6b1be157|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-PACKAGE-FOR-6B1BE157]]: `backend/scripts/generate_architecture_inventory.py` contains function `package_for_python`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-build-python-03fc45c4|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-BUILD-PYTHON-03FC45C4]]: `backend/scripts/generate_architecture_inventory.py` contains function `build_python_index`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-parse-python-cd2d0368|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-PARSE-PYTHON-CD2D0368]]: `backend/scripts/generate_architecture_inventory.py` contains function `parse_python_symbols`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-parse-text-s-4a175c52|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-PARSE-TEXT-S-4A175C52]]: `backend/scripts/generate_architecture_inventory.py` contains function `parse_text_symbols`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-resolve-rela-ea62247b|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-RESOLVE-RELA-EA62247B]]: `backend/scripts/generate_architecture_inventory.py` contains function `resolve_relative_import`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-import-relat-adceddcb|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-IMPORT-RELAT-ADCEDDCB]]: `backend/scripts/generate_architecture_inventory.py` contains function `import_relations`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-discover-25346c19|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-DISCOVER-25346C19]]: `backend/scripts/generate_architecture_inventory.py` contains function `discover`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-infer-test-t-23bffc44|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-INFER-TEST-T-23BFFC44]]: `backend/scripts/generate_architecture_inventory.py` contains function `infer_test_target`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-infer-doc-ta-729e90f4|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-INFER-DOC-TA-729E90F4]]: `backend/scripts/generate_architecture_inventory.py` contains function `infer_doc_target`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-dedupe-relat-0e90d287|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-DEDUPE-RELAT-0E90D287]]: `backend/scripts/generate_architecture_inventory.py` contains function `dedupe_relations`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-write-csv-596b2ee5|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-WRITE-CSV-596B2EE5]]: `backend/scripts/generate_architecture_inventory.py` contains function `write_csv`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-write-summar-cfbb9c53|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-WRITE-SUMMAR-CFBB9C53]]: `backend/scripts/generate_architecture_inventory.py` contains function `write_summary`.
- `parent_of` -> [[pyfunc-backend-scripts-generate-architecture-inventory-py-main-73df4292|PYFUNC-BACKEND-SCRIPTS-GENERATE-ARCHITECTURE-INVENTORY-PY-MAIN-73DF4292]]: `backend/scripts/generate_architecture_inventory.py` contains function `main`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
