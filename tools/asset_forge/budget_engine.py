from __future__ import annotations

from collections import Counter


def patch_count(width: int, height: int, tile: int = 768, overlap: int = 96) -> int:
    if tile <= 0:
        raise ValueError("tile must be > 0")
    if overlap < 0 or overlap >= tile:
        raise ValueError("overlap must satisfy 0 <= overlap < tile")

    def axis_count(length: int) -> int:
        if length <= tile:
            return 1
        step = tile - overlap
        starts = list(range(0, max(1, length - tile + 1), step))
        last = length - tile
        if starts[-1] != last:
            starts.append(last)
        return len(set(starts))

    return axis_count(width) * axis_count(height)


def estimate_generation_calls(
    queue: list[dict],
    *,
    atlas_tile: int = 768,
    atlas_overlap: int = 96,
) -> dict:
    """Estimate image-generation calls before a batch is submitted.

    Direct edits cost one call. Atlas processing costs one call per coordinate patch.
    Propagated animation frames cost zero additional image-generation calls.
    """
    calls = 0
    by_category: Counter[str] = Counter()
    by_action: Counter[str] = Counter()

    for row in queue:
        action = row.get("action")
        category = row.get("category", "unknown")
        count = 0
        if action == "ai_style_edit":
            count = 1
        elif action == "structure_preserving_pass":
            count = patch_count(
                int(row["width"]),
                int(row["height"]),
                atlas_tile,
                atlas_overlap,
            )
        elif action == "propagate_from_anchor":
            count = 0

        calls += count
        by_category[category] += count
        by_action[action or "unknown"] += count

    return {
        "estimated_image_generation_calls": calls,
        "by_category": dict(sorted(by_category.items())),
        "by_action": dict(sorted(by_action.items())),
        "atlas_tile": atlas_tile,
        "atlas_overlap": atlas_overlap,
    }
