"""Parse Class EXP, recruitment CEXP, and campaign CEXP authority."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re

from .markdown import extract_markdown_table, find_markdown_table, parse_int
from .repo import SourceGapError, find_repo_root, read_repo_text

CLASS_EXP_CEXP_PATH = "docs/10_PROGRESSION_AND_EXP/CLASS_EXP_CEXP.md"
CLASS_RECRUITMENT_CEXP_PATH = (
    "docs/10_PROGRESSION_AND_EXP/CLASS_RECRUITMENT_AND_STARTING_CEXP.md"
)
CAMPAIGN_CEXP_BUDGETS_PATH = "docs/10_PROGRESSION_AND_EXP/CAMPAIGN_CEXP_BUDGETS.md"
CLASS_CEXP_CAP = 6_000
CLASS_LEVEL_CAP = 13


@dataclass(frozen=True)
class ClassLevelThresholdSource:
    class_level: int
    cumulative_cexp: int
    cexp_to_next: int | None
    source_path: str = CLASS_EXP_CEXP_PATH


@dataclass(frozen=True)
class CharacterStartingCexpSource:
    character: str
    recruitment_chapter: int
    starting_base_class_level: int
    starting_base_cexp: int
    recruitment_chapter_cexp_after_join: int
    source_path: str = CLASS_RECRUITMENT_CEXP_PATH


@dataclass(frozen=True)
class CampaignCexpBudgetSource:
    chapter: int
    cexp: int
    source_path: str = CAMPAIGN_CEXP_BUDGETS_PATH


@dataclass(frozen=True)
class Chapter13CexpSplitSource:
    pre_last_shelter: int
    post_last_shelter: int
    source_path: str = CAMPAIGN_CEXP_BUDGETS_PATH


def _chapter_number(value: str) -> int:
    match = re.search(r"\bCh(?:apter)?\s*(\d+)\b", value, re.I)
    if not match:
        raise SourceGapError(f"Expected chapter value, got: {value!r}")
    return int(match.group(1))


def _class_level(value: str) -> int:
    match = re.search(r"\bCL\s*(\d+)\b", value, re.I)
    if not match:
        raise SourceGapError(f"Expected Class Level value, got: {value!r}")
    return int(match.group(1))


def _load_thresholds(root_string: str) -> tuple[ClassLevelThresholdSource, ...]:
    root = Path(root_string)
    text = read_repo_text(CLASS_EXP_CEXP_PATH, root=root)
    table = find_markdown_table(text, ("Class Level", "Cumulative CEXP", "CEXP to next"))
    rows: list[ClassLevelThresholdSource] = []
    for row in table:
        level = _class_level(row["Class Level"])
        cumulative = parse_int(row["Cumulative CEXP"])
        next_value = row["CEXP to next"].strip()
        cexp_to_next = None if next_value in {"—", "-", "N/A"} else parse_int(next_value)
        rows.append(
            ClassLevelThresholdSource(
                class_level=level,
                cumulative_cexp=cumulative,
                cexp_to_next=cexp_to_next,
            )
        )

    rows.sort(key=lambda item: item.class_level)
    if [row.class_level for row in rows] != list(range(1, CLASS_LEVEL_CAP + 1)):
        raise SourceGapError(
            f"{CLASS_EXP_CEXP_PATH} must publish contiguous CL1–CL{CLASS_LEVEL_CAP} thresholds"
        )
    if rows[0].cumulative_cexp != 0 or rows[-1].cumulative_cexp != CLASS_CEXP_CAP:
        raise SourceGapError(
            f"{CLASS_EXP_CEXP_PATH} disagrees with expected 0→{CLASS_CEXP_CAP} Class CEXP curve"
        )
    if any(
        later.cumulative_cexp <= earlier.cumulative_cexp
        for earlier, later in zip(rows, rows[1:])
    ):
        raise SourceGapError(f"Non-increasing Class CEXP thresholds in {CLASS_EXP_CEXP_PATH}")
    for index, row in enumerate(rows[:-1]):
        expected = rows[index + 1].cumulative_cexp - row.cumulative_cexp
        if row.cexp_to_next != expected:
            raise SourceGapError(
                f"CL{row.class_level} CEXP-to-next disagrees with cumulative thresholds"
            )
    if rows[-1].cexp_to_next is not None:
        raise SourceGapError("CL13 must not publish CEXP to next")
    return tuple(rows)


def _load_starting_cexp(root_string: str) -> tuple[CharacterStartingCexpSource, ...]:
    root = Path(root_string)
    text = read_repo_text(CLASS_RECRUITMENT_CEXP_PATH, root=root)
    starting_table = find_markdown_table(
        text,
        ("Character", "Recruitment", "Starting Base CL", "Starting Base CEXP"),
    )
    handoff_table = find_markdown_table(
        text,
        (
            "Character",
            "Recruitment chapter CEXP before join",
            "Canonical CEXP remaining after join",
        ),
    )
    handoffs = {
        row["Character"]: parse_int(row["Canonical CEXP remaining after join"])
        for row in handoff_table
    }

    rows: list[CharacterStartingCexpSource] = []
    for row in starting_table:
        character = row["Character"]
        recruitment_chapter = _chapter_number(row["Recruitment"])
        starting_cl = _class_level(row["Starting Base CL"])
        starting_cexp = parse_int(row["Starting Base CEXP"])
        remaining = handoffs.get(character)
        if remaining is None:
            if recruitment_chapter == 0:
                # Ch0 has no campaign CEXP budget; Ch1 is earned normally after recruitment.
                remaining = 0
            else:
                raise SourceGapError(
                    f"Missing recruitment-chapter CEXP handoff for {character}"
                )
        rows.append(
            CharacterStartingCexpSource(
                character=character,
                recruitment_chapter=recruitment_chapter,
                starting_base_class_level=starting_cl,
                starting_base_cexp=starting_cexp,
                recruitment_chapter_cexp_after_join=remaining,
            )
        )

    thresholds = {row.class_level: row.cumulative_cexp for row in _load_thresholds(root_string)}
    for row in rows:
        expected = thresholds.get(row.starting_base_class_level)
        if expected != row.starting_base_cexp:
            raise SourceGapError(
                f"{row.character} starting CL/CEXP disagree: CL{row.starting_base_class_level} "
                f"expects {expected}, source publishes {row.starting_base_cexp}"
            )
    return tuple(rows)


def _budget_rows(text: str, heading: str) -> list[dict[str, str]]:
    return extract_markdown_table(text, heading)


def _load_campaign_budgets(root_string: str) -> tuple[CampaignCexpBudgetSource, ...]:
    root = Path(root_string)
    text = read_repo_text(CAMPAIGN_CEXP_BUDGETS_PATH, root=root)
    rows: list[CampaignCexpBudgetSource] = []
    for heading in ("Pre-Volition", "Post-Volition"):
        for row in _budget_rows(text, heading):
            if "Chapter" not in row or "Campaign CEXP" not in row:
                raise SourceGapError(
                    f"Unexpected CEXP budget table after {heading} in {CAMPAIGN_CEXP_BUDGETS_PATH}"
                )
            rows.append(
                CampaignCexpBudgetSource(
                    chapter=_chapter_number(row["Chapter"]),
                    cexp=parse_int(row["Campaign CEXP"]),
                )
            )
    rows.sort(key=lambda item: item.chapter)
    if [row.chapter for row in rows] != list(range(1, 14)):
        raise SourceGapError(
            f"{CAMPAIGN_CEXP_BUDGETS_PATH} must publish one CEXP budget for Chapters 1–13"
        )
    if sum(row.cexp for row in rows if row.chapter <= 7) != 4_950:
        raise SourceGapError("Pre-Volition CEXP budgets no longer sum to 4,950")
    if sum(row.cexp for row in rows if row.chapter >= 8) != 8_750:
        raise SourceGapError("Post-Volition CEXP budgets no longer sum to 8,750")
    return tuple(rows)


def _load_ch13_split(root_string: str) -> Chapter13CexpSplitSource:
    root = Path(root_string)
    text = read_repo_text(CAMPAIGN_CEXP_BUDGETS_PATH, root=root)
    pre_match = re.search(r"pre[–-]Last Shelter:\s*\*\*([\d,]+) CEXP\*\*", text, re.I)
    post_match = re.search(r"post[–-]Last Shelter:\s*\*\*([\d,]+) CEXP\*\*", text, re.I)
    if not (pre_match and post_match):
        raise SourceGapError(
            f"Missing Chapter 13 Last Shelter CEXP split in {CAMPAIGN_CEXP_BUDGETS_PATH}"
        )
    split = Chapter13CexpSplitSource(
        pre_last_shelter=int(pre_match.group(1).replace(",", "")),
        post_last_shelter=int(post_match.group(1).replace(",", "")),
    )
    ch13 = next(
        row.cexp for row in _load_campaign_budgets(root_string) if row.chapter == 13
    )
    if split.pre_last_shelter + split.post_last_shelter != ch13:
        raise SourceGapError("Chapter 13 CEXP split does not sum to the Chapter 13 budget")
    return split


@lru_cache(maxsize=4)
def _cached_thresholds(root_string: str) -> tuple[ClassLevelThresholdSource, ...]:
    return _load_thresholds(root_string)


@lru_cache(maxsize=4)
def _cached_starting_cexp(root_string: str) -> tuple[CharacterStartingCexpSource, ...]:
    return _load_starting_cexp(root_string)


@lru_cache(maxsize=4)
def _cached_campaign_budgets(root_string: str) -> tuple[CampaignCexpBudgetSource, ...]:
    return _load_campaign_budgets(root_string)


@lru_cache(maxsize=4)
def _cached_ch13_split(root_string: str) -> Chapter13CexpSplitSource:
    return _load_ch13_split(root_string)


def load_class_level_thresholds(
    *, root: Path | None = None
) -> tuple[ClassLevelThresholdSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_thresholds(str(repo))


def load_character_starting_cexp(
    *, root: Path | None = None
) -> tuple[CharacterStartingCexpSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_starting_cexp(str(repo))


def load_campaign_cexp_budgets(
    *, root: Path | None = None
) -> tuple[CampaignCexpBudgetSource, ...]:
    repo = (root or find_repo_root()).resolve()
    return _cached_campaign_budgets(str(repo))


def load_chapter13_cexp_split(*, root: Path | None = None) -> Chapter13CexpSplitSource:
    repo = (root or find_repo_root()).resolve()
    return _cached_ch13_split(str(repo))


__all__ = [
    "CAMPAIGN_CEXP_BUDGETS_PATH",
    "CLASS_CEXP_CAP",
    "CLASS_EXP_CEXP_PATH",
    "CLASS_LEVEL_CAP",
    "CLASS_RECRUITMENT_CEXP_PATH",
    "CampaignCexpBudgetSource",
    "CharacterStartingCexpSource",
    "Chapter13CexpSplitSource",
    "ClassLevelThresholdSource",
    "load_campaign_cexp_budgets",
    "load_character_starting_cexp",
    "load_chapter13_cexp_split",
    "load_class_level_thresholds",
]
