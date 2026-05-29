from __future__ import annotations

import ast
import csv
import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


NODE_COLUMNS = [
    "id",
    "name",
    "type",
    "status",
    "layer",
    "module",
    "feature",
    "description",
    "file_path",
    "related_files",
    "parent_id",
    "child_ids",
    "depends_on",
    "used_by",
    "ui_related",
    "api_related",
    "database_related",
    "tests_related",
    "docs_related",
    "agent_related",
    "risk_level",
    "completion_percent",
    "last_verified_at",
    "verification_status",
    "notes",
    "tags",
]

RELATION_COLUMNS = [
    "id",
    "source_id",
    "relation_type",
    "target_id",
    "status",
    "description",
    "evidence",
    "notes",
    "tags",
]

EXCLUDED_DIRS = {
    ".git",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "Aviary - docs",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".expo",
    ".expo-web-export",
    "artifacts",
}

EXCLUDED_PREFIXES = {
    ".codex/artifacts/",
    ".codex/tmp/",
    "docs/architecture/nodes/",
    "docs/architecture/graphs/",
}

SCANNED_EXTENSIONS = {
    ".py",
    ".ps1",
    ".sh",
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".mjs",
    ".css",
    ".json",
    ".toml",
    ".yml",
    ".yaml",
    ".md",
    ".csv",
    ".html",
}


@dataclass(frozen=True)
class Inventory:
    nodes: list[dict[str, str]]
    relations: list[dict[str, str]]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2].resolve()


def norm(path: Path) -> str:
    return Path(path).as_posix().replace("//", "/")


def slug(value: str, max_length: int = 72) -> str:
    raw = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").upper()
    if not raw:
        raw = "NODE"
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8].upper()
    trimmed = raw[: max_length - 9].strip("-")
    return f"{trimmed}-{digest}"


def file_id(relative_path: str) -> str:
    return "FILE-" + slug(relative_path)


def symbol_id(relative_path: str, symbol_type: str, name: str) -> str:
    return f"{symbol_type.upper()}-" + slug(f"{relative_path}:{name}")


def relation_id(source: str, relation_type: str, target: str) -> str:
    return "AUTO-REL-" + slug(f"{source}:{relation_type}:{target}", 86)


def row(
    node_id: str,
    name: str,
    node_type: str,
    layer: str,
    module: str,
    feature: str,
    description: str,
    file_path: str,
    parent_id: str = "",
    verification_status: str = "missing_evidence",
    tags: str = "",
) -> dict[str, str]:
    status = "implemented" if node_type not in {"documentation", "test"} else "verified"
    if verification_status == "missing_evidence":
        status = "implemented"
    return {
        "id": node_id,
        "name": name,
        "type": node_type,
        "status": status,
        "layer": layer,
        "module": module,
        "feature": feature,
        "description": description,
        "file_path": file_path,
        "related_files": "",
        "parent_id": parent_id,
        "child_ids": "",
        "depends_on": "",
        "used_by": "",
        "ui_related": "",
        "api_related": "",
        "database_related": "",
        "tests_related": "",
        "docs_related": "",
        "agent_related": "",
        "risk_level": "medium" if layer in {"backend", "api", "database", "runtime"} else "low",
        "completion_percent": "50" if verification_status == "missing_evidence" else "70",
        "last_verified_at": date.today().isoformat(),
        "verification_status": verification_status,
        "notes": "Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.",
        "tags": tags,
    }


def relation(
    source: str,
    relation_type: str,
    target: str,
    description: str,
    evidence: str,
    tags: str,
) -> dict[str, str]:
    return {
        "id": relation_id(source, relation_type, target),
        "source_id": source,
        "relation_type": relation_type,
        "target_id": target,
        "status": "implemented",
        "description": description,
        "evidence": evidence,
        "notes": "Auto-discovered relation; verify before using as release-critical proof.",
        "tags": tags,
    }


def should_scan(path: Path, root: Path) -> bool:
    try:
        relative = norm(path.relative_to(root))
    except ValueError:
        return False
    if any(relative.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
        return False
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    if path.suffix.lower() not in SCANNED_EXTENSIONS:
        return False
    if path.name in {"package-lock.json"}:
        return False
    return True


def classify_file(relative_path: str) -> tuple[str, str, str, str, str]:
    path = Path(relative_path)
    top = path.parts[0] if path.parts else "root"
    ext = path.suffix.lower()
    if relative_path.startswith("backend/app/api/"):
        return "api_file", "api", "backend", "api_contracts", "#auto #api"
    if relative_path.startswith("backend/app/memory/") or relative_path.startswith("backend/migrations/"):
        return "data_file", "database", "backend", "data_model", "#auto #data"
    if relative_path.startswith("backend/app/"):
        return "backend_file", "backend", "backend", top, "#auto #backend"
    if relative_path.startswith("backend/tests/"):
        return "test", "test", "backend", "test_coverage", "#auto #test"
    if relative_path.startswith("web/src/components/"):
        return "component_file", "frontend", "web", "component_inventory", "#auto #frontend #component"
    if relative_path.startswith("web/src/"):
        return "frontend_file", "frontend", "web", "web_shell", "#auto #frontend"
    if relative_path.startswith("mobile/"):
        return "mobile_file", "frontend", "mobile", "mobile_shell", "#auto #mobile"
    if relative_path.startswith("docs/") or ext == ".md":
        return "documentation", "docs", "docs", "documentation", "#auto #docs"
    if relative_path.startswith(".agents/") or relative_path.startswith("agents/"):
        return "agent_file", "docs", "agents", "agent_workflow", "#auto #agent"
    if relative_path.startswith(".codex/") or relative_path.startswith("tasks/"):
        return "task_file", "docs", "tasks", "task_state", "#auto #task"
    if ext in {".json", ".toml", ".yml", ".yaml"}:
        return "config", "config", top, "configuration", "#auto #config"
    return "file", top, top, "inventory", "#auto"


def package_for_python(relative_path: str) -> str:
    without_suffix = relative_path.removesuffix(".py")
    return without_suffix.replace("/", ".").replace("\\", ".")


def build_python_index(files: list[str]) -> dict[str, str]:
    index: dict[str, str] = {}
    for relative_path in files:
        if not relative_path.endswith(".py"):
            continue
        package = package_for_python(relative_path)
        index[package] = file_id(relative_path)
        if package.endswith(".__init__"):
            index[package.removesuffix(".__init__")] = file_id(relative_path)
    return index


def parse_python_symbols(root: Path, relative_path: str, parent_file_id: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    nodes: list[dict[str, str]] = []
    relations: list[dict[str, str]] = []
    path = root / relative_path
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="ignore"))
    except SyntaxError:
        return nodes, relations

    for item in tree.body:
        if isinstance(item, ast.ClassDef):
            node_id = symbol_id(relative_path, "PYCLASS", item.name)
            nodes.append(
                row(
                    node_id,
                    item.name,
                    "class",
                    "backend" if relative_path.startswith("backend/") else "script",
                    Path(relative_path).parts[0],
                    "symbol_inventory",
                    f"Python class `{item.name}` auto-discovered from `{relative_path}`.",
                    relative_path,
                    parent_file_id,
                    "implementation_evidence",
                    "#auto #python #class",
                )
            )
            relations.append(
                relation(parent_file_id, "parent_of", node_id, f"`{relative_path}` contains class `{item.name}`.", relative_path, "#auto #contains")
            )
        elif isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node_id = symbol_id(relative_path, "PYFUNC", item.name)
            nodes.append(
                row(
                    node_id,
                    item.name,
                    "function",
                    "backend" if relative_path.startswith("backend/") else "script",
                    Path(relative_path).parts[0],
                    "symbol_inventory",
                    f"Python function `{item.name}` auto-discovered from `{relative_path}`.",
                    relative_path,
                    parent_file_id,
                    "implementation_evidence",
                    "#auto #python #function",
                )
            )
            relations.append(
                relation(parent_file_id, "parent_of", node_id, f"`{relative_path}` contains function `{item.name}`.", relative_path, "#auto #contains")
            )
    return nodes, relations


TS_SYMBOL_PATTERN = re.compile(
    r"(?:export\s+)?(?:async\s+)?(?:function|const|let|var|class|interface|type)\s+([A-Za-z_][A-Za-z0-9_]*)"
)
CSS_SELECTOR_PATTERN = re.compile(r"(^|\n)\s*([.#][A-Za-z0-9_-]+)\s*[{,]")
TS_IMPORT_PATTERN = re.compile(r"from\s+['\"]([^'\"]+)['\"]|import\s+['\"]([^'\"]+)['\"]")


def parse_text_symbols(root: Path, relative_path: str, parent_file_id: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    nodes: list[dict[str, str]] = []
    relations: list[dict[str, str]] = []
    text = (root / relative_path).read_text(encoding="utf-8", errors="ignore")
    ext = Path(relative_path).suffix.lower()
    if ext in {".ts", ".tsx", ".js", ".jsx", ".mjs"}:
        seen: set[str] = set()
        for match in TS_SYMBOL_PATTERN.finditer(text):
            name = match.group(1)
            if name in seen:
                continue
            seen.add(name)
            symbol_type = "component" if name[:1].isupper() and ext in {".tsx", ".jsx"} else "function"
            prefix = "TSCOMP" if symbol_type == "component" else "TSFUNC"
            node_id = symbol_id(relative_path, prefix, name)
            nodes.append(
                row(
                    node_id,
                    name,
                    symbol_type,
                    "frontend" if relative_path.startswith(("web/", "mobile/")) else "script",
                    Path(relative_path).parts[0],
                    "symbol_inventory",
                    f"TypeScript/JavaScript symbol `{name}` auto-discovered from `{relative_path}`.",
                    relative_path,
                    parent_file_id,
                    "implementation_evidence",
                    f"#auto #typescript #{symbol_type}",
                )
            )
            relations.append(
                relation(parent_file_id, "parent_of", node_id, f"`{relative_path}` contains symbol `{name}`.", relative_path, "#auto #contains")
            )
    elif ext == ".css":
        seen_selectors: set[str] = set()
        for match in CSS_SELECTOR_PATTERN.finditer(text):
            selector = match.group(2)
            if selector in seen_selectors:
                continue
            seen_selectors.add(selector)
            node_id = symbol_id(relative_path, "CSS", selector)
            nodes.append(
                row(
                    node_id,
                    selector,
                    "ui_element",
                    "frontend",
                    Path(relative_path).parts[0],
                    "style_inventory",
                    f"CSS selector `{selector}` auto-discovered from `{relative_path}`.",
                    relative_path,
                    parent_file_id,
                    "implementation_evidence",
                    "#auto #css #ui",
                )
            )
            relations.append(
                relation(parent_file_id, "parent_of", node_id, f"`{relative_path}` defines selector `{selector}`.", relative_path, "#auto #contains")
            )
    return nodes, relations


def resolve_relative_import(source_path: str, target: str, known_files: set[str]) -> str:
    if not target.startswith("."):
        return ""
    source_dir = Path(source_path).parent
    base = (source_dir / target).as_posix()
    candidates = [
        base,
        base + ".ts",
        base + ".tsx",
        base + ".js",
        base + ".jsx",
        base + ".mjs",
        base + ".py",
        base + "/index.ts",
        base + "/index.tsx",
        base + "/__init__.py",
    ]
    for candidate in candidates:
        normalized = norm(Path(candidate))
        if normalized in known_files:
            return file_id(normalized)
    return ""


def import_relations(root: Path, relative_path: str, parent_file_id: str, known_files: set[str], python_index: dict[str, str]) -> list[dict[str, str]]:
    relations: list[dict[str, str]] = []
    path = root / relative_path
    ext = path.suffix.lower()
    text = path.read_text(encoding="utf-8", errors="ignore")
    if ext == ".py":
        try:
            tree = ast.parse(text)
        except SyntaxError:
            return relations
        modules: set[str] = set()
        for item in ast.walk(tree):
            if isinstance(item, ast.Import):
                modules.update(alias.name for alias in item.names)
            elif isinstance(item, ast.ImportFrom) and item.module:
                modules.add(item.module)
        for module in sorted(modules):
            target = python_index.get(module)
            if target:
                relations.append(
                    relation(parent_file_id, "depends_on", target, f"`{relative_path}` imports `{module}`.", relative_path, "#auto #import")
                )
    elif ext in {".ts", ".tsx", ".js", ".jsx", ".mjs"}:
        for match in TS_IMPORT_PATTERN.finditer(text):
            specifier = match.group(1) or match.group(2)
            target = resolve_relative_import(relative_path, specifier, known_files)
            if target:
                relations.append(
                    relation(parent_file_id, "depends_on", target, f"`{relative_path}` imports `{specifier}`.", relative_path, "#auto #import")
                )
    return relations


def discover(root: Path) -> Inventory:
    files: list[str] = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            dirname
            for dirname in dirnames
            if dirname not in EXCLUDED_DIRS and not dirname.startswith(".vite")
        ]
        current_path = Path(current_root)
        for filename in filenames:
            path = current_path / filename
            if should_scan(path, root):
                files.append(norm(path.relative_to(root)))
    files.sort()
    known_files = set(files)
    python_index = build_python_index(files)
    nodes: list[dict[str, str]] = []
    relations: list[dict[str, str]] = []

    for relative_path in files:
        node_id = file_id(relative_path)
        node_type, layer, module, feature, tags = classify_file(relative_path)
        verification = "documentation_evidence" if node_type == "documentation" else "test_evidence" if node_type == "test" else "implementation_evidence"
        nodes.append(
            row(
                node_id,
                Path(relative_path).name,
                node_type,
                layer,
                module,
                feature,
                f"Repository file `{relative_path}` auto-discovered for architecture graph inventory.",
                relative_path,
                "",
                verification,
                tags,
            )
        )
        if node_type == "test":
            target = infer_test_target(relative_path, known_files)
            if target:
                relations.append(
                    relation(node_id, "verifies", target, f"Test file `{relative_path}` appears to verify `{target}`.", relative_path, "#auto #test")
                )
        elif node_type == "documentation":
            documented = infer_doc_target(relative_path, known_files)
            if documented:
                relations.append(
                    relation(node_id, "documents", documented, f"Doc `{relative_path}` appears to document `{documented}`.", relative_path, "#auto #docs")
                )

        if relative_path.endswith(".py"):
            symbol_nodes, symbol_relations = parse_python_symbols(root, relative_path, node_id)
            nodes.extend(symbol_nodes)
            relations.extend(symbol_relations)
        elif Path(relative_path).suffix.lower() in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".css"}:
            symbol_nodes, symbol_relations = parse_text_symbols(root, relative_path, node_id)
            nodes.extend(symbol_nodes)
            relations.extend(symbol_relations)
        relations.extend(import_relations(root, relative_path, node_id, known_files, python_index))

    return Inventory(nodes=nodes, relations=dedupe_relations(relations))


def infer_test_target(relative_path: str, known_files: set[str]) -> str:
    name = Path(relative_path).stem
    if not name.startswith("test_"):
        return ""
    base = name.removeprefix("test_")
    candidates = [
        f"backend/app/core/{base}.py",
        f"backend/app/api/{base}.py",
        f"backend/app/memory/{base}.py",
        f"backend/app/reflection/{base}.py",
        f"backend/app/workers/{base}.py",
        f"web/src/lib/{base}.ts",
        f"web/scripts/{base}.mjs",
    ]
    for candidate in candidates:
        if candidate in known_files:
            return file_id(candidate)
    return ""


def infer_doc_target(relative_path: str, known_files: set[str]) -> str:
    stem = Path(relative_path).stem.replace("_", "-")
    candidates = [
        f"backend/app/core/{stem.replace('-', '_')}.py",
        f"backend/app/api/{stem.replace('-', '_')}.py",
        f"web/src/components/{stem}.tsx",
        f"web/src/lib/{stem}.ts",
    ]
    for candidate in candidates:
        if candidate in known_files:
            return file_id(candidate)
    return ""


def dedupe_relations(relations: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for item in relations:
        key = item["id"]
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for item in rows:
            writer.writerow(item)


def write_summary(root: Path, inventory: Inventory) -> None:
    path = root / "docs" / "architecture" / "registry" / "auto_inventory_summary.md"
    by_type = {}
    for item in inventory.nodes:
        by_type[item["type"]] = by_type.get(item["type"], 0) + 1
    by_relation = {}
    for item in inventory.relations:
        by_relation[item["relation_type"]] = by_relation.get(item["relation_type"], 0) + 1
    lines = [
        "# Auto Architecture Inventory Summary",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"- auto nodes: `{len(inventory.nodes)}`",
        f"- auto relations: `{len(inventory.relations)}`",
        "",
        "## Node Types",
        "",
        "| Type | Count |",
        "| --- | --- |",
    ]
    for key, value in sorted(by_type.items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## Relation Types", "", "| Type | Count |", "| --- | --- |"])
    for key, value in sorted(by_relation.items()):
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Rows are auto-discovered and should be promoted or refined in curated CSVs when they become release-critical.",
            "- Generated Obsidian graph exports merge these rows with the curated registry.",
            "- Generated output directories are excluded from scanning to avoid recursive graph growth.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    root = repo_root()
    inventory = discover(root)
    registry = root / "docs" / "architecture" / "registry"
    write_csv(registry / "auto_nodes.csv", inventory.nodes, NODE_COLUMNS)
    write_csv(registry / "auto_relations.csv", inventory.relations, RELATION_COLUMNS)
    write_summary(root, inventory)
    print(f"auto_nodes={len(inventory.nodes)}")
    print(f"auto_relations={len(inventory.relations)}")
    print("wrote docs/architecture/registry/auto_nodes.csv")
    print("wrote docs/architecture/registry/auto_relations.csv")
    print("wrote docs/architecture/registry/auto_inventory_summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
