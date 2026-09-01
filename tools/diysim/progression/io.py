"""JSON loading for progression-route planning inputs."""
from __future__ import annotations

import json
from pathlib import Path

from .player_exp import cumulative_exp
from .routes import ProgressionSegment


def load_progression_route(path: str | Path) -> tuple[int, tuple[ProgressionSegment, ...]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "start_exp" in data:
        start_exp = int(data["start_exp"])
    else:
        start_level = int(data.get("start_level", 1))
        start_exp = cumulative_exp(start_level)

    segments = tuple(
        ProgressionSegment(
            name=segment["name"],
            count=int(segment.get("count", 1)),
            exp_each=int(segment.get("exp_each", 0)),
            flat_exp=int(segment.get("flat_exp", 0)),
            completion_rate=float(segment.get("completion_rate", 1.0)),
        )
        for segment in data.get("segments", [])
    )
    return start_exp, segments
