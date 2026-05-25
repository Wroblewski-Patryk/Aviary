from __future__ import annotations

import json
from pathlib import Path

from scripts import build_architecture_graph_hosted_evidence_packet as packet_builder


def _write_artifact(path: Path, *, gap_count: int) -> None:
    items = [{"node": {"id": "X"}, "gaps": ["missing"]}] if gap_count else []
    path.write_text(json.dumps({"include_auto": False, "items": items}), encoding="utf-8")


def test_packet_builder_passes_for_zero_gap_artifacts(tmp_path: Path) -> None:
    fast = tmp_path / "fast.json"
    heavy = tmp_path / "heavy.json"
    out_dir = tmp_path / "packet"
    _write_artifact(fast, gap_count=0)
    _write_artifact(heavy, gap_count=0)

    exit_code = packet_builder.run(
        ["--fast-artifact", str(fast), "--heavy-artifact", str(heavy), "--out-dir", str(out_dir)]
    )

    assert exit_code == 0
    data = json.loads((out_dir / "architecture-graph-hosted-evidence.json").read_text(encoding="utf-8"))
    assert data["status"] == "PASSED"
    assert data["fast_artifact"]["gap_count"] == 0
    assert data["heavy_artifact"]["gap_count"] == 0


def test_packet_builder_fails_for_nonzero_gap_artifacts(tmp_path: Path) -> None:
    fast = tmp_path / "fast.json"
    out_dir = tmp_path / "packet"
    _write_artifact(fast, gap_count=1)

    exit_code = packet_builder.run(["--fast-artifact", str(fast), "--out-dir", str(out_dir)])

    assert exit_code == 1
    data = json.loads((out_dir / "architecture-graph-hosted-evidence.json").read_text(encoding="utf-8"))
    assert data["status"] == "FAILED"
    assert data["fast_artifact"]["gap_count"] == 1
