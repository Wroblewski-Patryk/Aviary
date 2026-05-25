from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = PROJECT_ROOT / ".github" / "workflows" / "architecture-graph.yml"


def test_architecture_graph_workflow_enforces_fail_on_gaps() -> None:
    text = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert "--gaps --format json --fail-on-gaps" in text


def test_architecture_graph_workflow_uploads_gap_artifacts() -> None:
    text = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert "name: architecture-gaps-fast" in text
    assert "name: architecture-gaps-heavy" in text
    assert "name: architecture-hosted-evidence-fast" in text
    assert "name: architecture-hosted-evidence-heavy" in text
    assert "uses: actions/upload-artifact@v4" in text
