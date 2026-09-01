"""Small parsers for canon Markdown owned by the Diyse repository."""
from __future__ import annotations
import re

from .repo import SourceGapError


def _clean(cell: str) -> str:
    return re.sub(r"[*_`]", "", cell).strip()


def extract_markdown_table(text: str, heading: str) -> list[dict[str, str]]:
    """Return the first Markdown table after an exact/contained heading string."""
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if heading in line)
    except StopIteration as exc:
        raise SourceGapError(f"Missing section/table heading: {heading}") from exc

    header_index = None
    for i in range(start + 1, min(len(lines), start + 20)):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and "---" in lines[i + 1]:
            header_index = i
            break
    if header_index is None:
        raise SourceGapError(f"Missing Markdown table after: {heading}")

    headers = [_clean(x) for x in lines[header_index].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2 :]:
        if not line.lstrip().startswith("|"):
            break
        cells = [_clean(x) for x in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    if not rows:
        raise SourceGapError(f"Empty Markdown table after: {heading}")
    return rows


def find_line_value(text: str, label: str, *, pattern: str = r"(-?\d+(?:\.\d+)?)") -> str:
    for line in text.splitlines():
        if label in line:
            match = re.search(pattern, line)
            if match:
                return match.group(1)
    raise SourceGapError(f"Missing value for: {label}")


def parse_int(value: str) -> int:
    match = re.search(r"-?\d+", value.replace(",", ""))
    if not match:
        raise SourceGapError(f"Expected integer value, got: {value!r}")
    return int(match.group(0))


def parse_float(value: str) -> float:
    match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
    if not match:
        raise SourceGapError(f"Expected numeric value, got: {value!r}")
    return float(match.group(0))
