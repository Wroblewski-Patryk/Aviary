from __future__ import annotations

import json
from pathlib import Path

from scripts import run_architecture_graph_hosted_proof_intake as intake


def _write_artifact(path: Path, *, gap_count: int) -> None:
    items = [{"node": {"id": "X"}, "gaps": ["missing"]}] if gap_count else []
    path.write_text(json.dumps({"include_auto": False, "items": items}), encoding="utf-8")


def test_intake_passes_for_fast_and_heavy_zero_gap(tmp_path: Path) -> None:
    fast = tmp_path / "fast.json"
    heavy = tmp_path / "heavy.json"
    out_dir = tmp_path / "packet"
    _write_artifact(fast, gap_count=0)
    _write_artifact(heavy, gap_count=0)

    exit_code = intake.run(
        ["--fast-artifact", str(fast), "--heavy-artifact", str(heavy), "--out-dir", str(out_dir)]
    )

    assert exit_code == 0
    packet = json.loads((out_dir / "architecture-graph-hosted-evidence.json").read_text(encoding="utf-8"))
    assert packet["status"] == "PASSED"


def test_intake_fails_when_fast_artifact_has_gaps(tmp_path: Path) -> None:
    fast = tmp_path / "fast.json"
    out_dir = tmp_path / "packet"
    _write_artifact(fast, gap_count=1)

    exit_code = intake.run(["--fast-artifact", str(fast), "--out-dir", str(out_dir)])

    assert exit_code == 1
