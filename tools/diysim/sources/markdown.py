"""Small parsers for canon Markdown owned by the Diyse repository."""
from __future__ import annotations
import re
from collections.abc import Iterable

from .repo import SourceGapError


def _clean(cell: str) -> str:
    return re.sub(r"[*_`]", "", cell).strip()


def _table_at(lines: list[str], header_index: int) -> list[dict[str, str]]:
    headers = [_clean(x) for x in lines[header_index].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2 :]:
        if not line.lstrip().startswith("|"):
            break
        cells = [_clean(x) for x in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def extract_markdown_tables(text: str) -> list[list[dict[str, str]]]:
    """Return every ordinary pipe-delimited Markdown table in document order."""
    lines = text.splitlines()
    tables: list[list[dict[str, str]]] = []
    for index, line in enumerate(lines[:-1]):
        if not line.lstrip().startswith("|"):
            continue
        if not lines[index + 1].lstrip().startswith("|") or "---" not in lines[index + 1]:
            continue
        rows = _table_at(lines, index)
        if rows:
            tables.append(rows)
    return tables


def find_markdown_table(text: str, required_columns: Iterable[str]) -> list[dict[str, str]]:
    """Find the first Markdown table whose headers contain all required columns."""
    required = set(required_columns)
    for rows in extract_markdown_tables(text):
        if rows and required.issubset(rows[0]):
            return rows
    columns = ", ".join(sorted(required))
    raise SourceGapError(f"Missing Markdown table with columns: {columns}")


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

    rows = _table_at(lines, header_index)
    if not rows:
        raise SourceGapError(f"Empty Markdown table after: {heading}")
    return rows


def extract_heading_block(text: str, heading: str) -> str:
    """Return a Markdown heading and its body until the next same/higher-level heading."""
    lines = text.splitlines()
    start = None
    level = None
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if match and heading in match.group(2):
            start = index
            level = len(match.group(1))
            break
    if start is None or level is None:
        raise SourceGapError(f"Missing heading block: {heading}")

    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = re.match(r"^(#{1,6})\s+", lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "\n".join(lines[start:end]).strip()


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
