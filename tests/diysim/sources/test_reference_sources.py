from __future__ import annotations

from tools.diysim.sources.references import resolve_enabled_action_references
from tools.diysim.sources.repo import find_repo_root, read_repo_text


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.index(marker) + len(marker)
    next_heading = text.find("\n## ", start)
    if next_heading == -1:
        next_heading = len(text)
    return text[start:next_heading]


def test_zevraya_sustenance_summary_resolves_unique_complete_action_owners() -> None:
    repo = find_repo_root()
    text = read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS/ZEVRAYA_LIFE_FORCE_RESERVOIRS.md")
    result = resolve_enabled_action_references(
        _section(text, "Sustenance"),
        repo_root=repo,
        current_path=repo / "docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS/ZEVRAYA_LIFE_FORCE_RESERVOIRS.md",
    )

    assert result.complete
    assert result.names == ("Sustenance Draw", "Perfected Siphon")
    assert {match.path for match in result.matches} == {
        "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/MATRON_ZEVRAYA.md"
    }


def test_zevraya_conduction_summary_resolves_unique_complete_action_owners() -> None:
    repo = find_repo_root()
    text = read_repo_text("docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS/ZEVRAYA_LIFE_FORCE_RESERVOIRS.md")
    result = resolve_enabled_action_references(
        _section(text, "Conduction"),
        repo_root=repo,
        current_path=repo / "docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS/ZEVRAYA_LIFE_FORCE_RESERVOIRS.md",
    )

    assert result.complete
    assert result.names == ("Weather Conduction", "Perfected Conduction")
