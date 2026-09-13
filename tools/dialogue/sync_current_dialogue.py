#!/usr/bin/env python3
"""Synchronize DIYSE Chapters 0-3 combined dialogue manuscripts and reader.

The standalone Markdown scene files under docs/03_DIALOGUE/PRODUCTION/CHAPTER_##
remain exact wording authority. This tool deliberately derives every combined/readable
output from those atomics so a derived manuscript cannot silently become a competing
source of truth.

Outputs:
- CHAPTER_##_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md for Chapters 0-3
- docs/03_DIALOGUE/PRODUCTION/CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md
- build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx

Use --check to verify the generated Markdown outputs are current without writing them.
The DOCX is a derived reader artifact: spoken dialogue is copied verbatim while
writer-facing production/audit metadata is omitted.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
PROD = ROOT / "docs/03_DIALOGUE/PRODUCTION"
SYNC_MANIFEST = PROD / "CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md"
READER_OUT = ROOT / "build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx"


@dataclass(frozen=True)
class SourceSpec:
    label: str
    pattern: str


@dataclass(frozen=True)
class ChapterSpec:
    chapter: str
    title: str
    sources: tuple[SourceSpec, ...]

    @property
    def directory(self) -> Path:
        return PROD / f"CHAPTER_{self.chapter}"

    @property
    def output(self) -> Path:
        return self.directory / f"CHAPTER_{self.chapter}_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md"

    @property
    def index(self) -> Path:
        return self.directory / f"CHAPTER_{self.chapter}_DIALOGUE_AUTHORITY_INDEX.md"


def beats(start: int, end: int) -> tuple[SourceSpec, ...]:
    return tuple(SourceSpec(f"Beat {n}", f"BEAT_{n:02d}_*.md") for n in range(start, end + 1))


CHAPTERS: tuple[ChapterSpec, ...] = (
    ChapterSpec(
        "00",
        "Chapter 0",
        tuple(SourceSpec(f"P{n:02d}", f"P{n:02d}_*.md") for n in range(1, 8))
        + (SourceSpec("C01 — Six Minutes", "C01_SIX_MINUTES_*.md"),),
    ),
    ChapterSpec(
        "01",
        "Chapter 1",
        beats(1, 15)
        + (
            SourceSpec("C02 — Torren's Version of Dinner", "C03_TORRENS_VERSION_OF_DINNER_*.md"),
            SourceSpec("C03 — What the Map Says", "C04_WHAT_THE_MAP_SAYS_*.md"),
            SourceSpec("C04 — Not Professionally", "C05_NOT_PROFESSIONALLY_*.md"),
        ),
    ),
    ChapterSpec(
        "02",
        "Chapter 2",
        beats(1, 16)
        + (SourceSpec("C05 — Still Burns", "C06_STILL_BURNS_*.md"),),
    ),
    ChapterSpec(
        "03",
        "Chapter 3",
        beats(1, 15)
        + (
            SourceSpec("C06 — Nimera Takes Over a Table", "H01_NIMERA_TAKES_OVER_A_TABLE_*.md"),
            SourceSpec("C07 — Ilyra and Nimera", "H03_ILYRA_AND_NIMERA_*.md"),
        ),
    ),
)


DIALOGUE_RE = re.compile(r"^\*\*([^*\n]+):\*\*\s*(.*)$")
HEADING_RE = re.compile(r"^(#{2,6})\s+(.*)$")

# Reader skips writer-facing / production-only sections. These are deliberately
# broad because the reader is derived, never an authority for implementation prose.
SKIP_SECTION_TERMS = (
    "production note",
    "production notes",
    "audit check",
    "audit note",
    "knowledge check",
    "knowledge checkpoint",
    "world-state checkpoint",
    "continuity note",
    "continuity notes",
    "current production state",
    "conflict order",
    "gameplay handoff",
    "player exit",
    "cleanup window",
    "natural-turn",
    "spoken-dialogue",
)

SKIP_LINE_PREFIXES = (
    "**Status:**",
    "**Story authority:**",
    "**Primary story authority:**",
    "**Method note:**",
    "**Rhythm note:**",
    "**Production note:**",
    "**Hard continuity:**",
    "**Owning cumulative manuscript:**",
    "**Dialogue workflow authority:**",
    "**Character-Life numbering authority:**",
    "**Availability:**",
    "**Participants:**",
    "**Objective:**",
    "Objective:",
    "Transition into:",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def resolve_source(chapter: ChapterSpec, spec: SourceSpec) -> Path:
    matches = [p for p in chapter.directory.glob(spec.pattern) if p.is_file()]
    # Never allow the derived manuscript itself to satisfy a broad pattern.
    matches = [p for p in matches if p != chapter.output and "AUTHORITY_INDEX" not in p.name]
    if len(matches) != 1:
        rels = [str(p.relative_to(ROOT)) for p in matches]
        raise RuntimeError(
            f"{chapter.title} / {spec.label}: pattern {spec.pattern!r} must resolve exactly once; "
            f"found {len(matches)}: {rels}"
        )
    return matches[0]


def resolved_chapter_sources(chapter: ChapterSpec) -> list[tuple[SourceSpec, Path, bytes, str]]:
    out: list[tuple[SourceSpec, Path, bytes, str]] = []
    seen: set[Path] = set()
    for spec in chapter.sources:
        path = resolve_source(chapter, spec)
        if path in seen:
            raise RuntimeError(f"Duplicate source selected: {path}")
        seen.add(path)
        data = path.read_bytes()
        data.decode("utf-8")  # fail loudly on unexpected encoding
        out.append((spec, path, data, sha256_bytes(data)))
    return out


def protected_checks(all_sources: dict[str, list[tuple[SourceSpec, Path, bytes, str]]]) -> None:
    text_by_ch = {
        ch: "\n".join(data.decode("utf-8") for _, _, data, _ in sources)
        for ch, sources in all_sources.items()
    }

    must_exist = {
        "01": [
            "**CYANIS:** Old slut?",
            "**TORREN:** Bitch.",
        ],
        "03": [
            "PREVIOUS ERROR",
            "LAST SENTINEL CONFIRMED",
            "**CYANIS:** I bet you use that cape to sneak up on the goats you fuck.",
            "**TORREN:** You look like a walking dick in armor.",
            "Might. Elements. Grace. Memory. Perception. Ruin.",
        ],
    }
    for chapter, needles in must_exist.items():
        for needle in needles:
            if needle not in text_by_ch[chapter]:
                raise RuntimeError(f"Protected anchor missing in Chapter {int(chapter)}: {needle}")

    stale = "Might. Elements. Grace. Resource. Perception. Ruin."
    if stale in text_by_ch["03"]:
        raise RuntimeError("Stale Chapter-3 Resource Face list is still present; expected Memory.")

    # Nimera is not met until Chapter 3. This catches accidental Character-Life leakage.
    if re.search(r"\bNimera\b", text_by_ch["01"], flags=re.IGNORECASE):
        raise RuntimeError("Chapter 1 still contains a Nimera reference before her Chapter-3 meeting.")


def render_combined(chapter: ChapterSpec, sources: list[tuple[SourceSpec, Path, bytes, str]]) -> str:
    lines: list[str] = [
        f"# DIYSE — {chapter.title} — Synchronized Rehearsal-First Working Dialogue Manuscript",
        "",
        "**Status:** CURRENT DERIVED READ-THROUGH — SYNCHRONIZED AGAINST CURRENT ATOMIC DIALOGUE SOURCES",
        "",
        "**Authority rule:** the standalone atomic scene files remain exact wording authority. This file is generated, not hand-authored. If any atomic source changes, rerun `python tools/dialogue/sync_current_dialogue.py` before treating this manuscript as current.",
        "",
        "## Source manifest",
        "",
        "| Order | Canonical slot | Atomic source | SHA-256 |",
        "|---:|---|---|---|",
    ]
    for i, (spec, path, _data, digest) in enumerate(sources, start=1):
        lines.append(f"| {i} | {spec.label} | `{path.name}` | `{digest}` |")

    lines += ["", "---", ""]

    for spec, path, data, digest in sources:
        text = data.decode("utf-8").rstrip()
        lines += [
            f"## {spec.label}",
            "",
            f"**Atomic source:** `{path.name}`  ",
            f"**Source SHA-256:** `{digest}`",
            "",
            text,
            "",
            "---",
            "",
        ]

    lines += [
        "## Synchronization footer",
        "",
        "This derived manuscript was assembled exclusively from the atomic sources listed above. No dialogue wording was rewritten during assembly.",
        "",
    ]
    return "\n".join(lines)


def render_sync_manifest(
    all_sources: dict[str, list[tuple[SourceSpec, Path, bytes, str]]],
    combined: dict[str, str],
) -> str:
    lines = [
        "# DIYSE — Chapters 0–3 Dialogue Synchronization Manifest",
        "",
        "**Status:** CURRENT — generated from active atomic dialogue sources",
        "",
        "This manifest proves which atomics were used for each combined read-through. The atomics remain wording authority; the combined manuscripts and reader are derived products.",
        "",
        "## Combined manuscripts",
        "",
        "| Chapter | Combined manuscript | Combined SHA-256 | Atomic sources |",
        "|---|---|---|---:|",
    ]
    for chapter in CHAPTERS:
        rendered = combined[chapter.chapter].encode("utf-8")
        lines.append(
            f"| {int(chapter.chapter)} | `{chapter.output.relative_to(ROOT)}` | `{sha256_bytes(rendered)}` | {len(all_sources[chapter.chapter])} |"
        )

    for chapter in CHAPTERS:
        lines += ["", f"## Chapter {int(chapter.chapter)} sources", "", "| Order | Canonical slot | Path | SHA-256 |", "|---:|---|---|---|"]
        for i, (spec, path, _data, digest) in enumerate(all_sources[chapter.chapter], start=1):
            lines.append(f"| {i} | {spec.label} | `{path.relative_to(ROOT)}` | `{digest}` |")

    lines += [
        "",
        "## Verification rule",
        "",
        "Run `python tools/dialogue/sync_current_dialogue.py --check`. A non-zero exit means at least one combined manuscript or the sync manifest is stale relative to current atomic dialogue.",
        "",
    ]
    return "\n".join(lines)


def plain_markdown(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^>\s*", "", text)
    text = text.replace("**", "").replace("`", "")
    text = text.replace("*", "")
    return text.strip()


def section_should_skip(heading: str) -> bool:
    low = plain_markdown(heading).lower()
    return any(term in low for term in SKIP_SECTION_TERMS)


def reader_blocks(source_text: str) -> list[tuple[str, str, str | None]]:
    """Return (kind, text, optional speaker) blocks from one atomic source.

    Spoken dialogue is never rewritten: `text` for kind=dialogue is the exact text after
    the Markdown speaker marker.
    """
    blocks: list[tuple[str, str, str | None]] = []
    skip_section = False
    in_fence = False

    for raw in source_text.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        heading = HEADING_RE.match(line)
        if heading:
            title = heading.group(2).strip()
            skip_section = section_should_skip(title)
            if not skip_section:
                cleaned = plain_markdown(title).strip("[]")
                if cleaned:
                    blocks.append(("heading", cleaned, None))
            continue

        if skip_section:
            continue
        if not line.strip():
            continue
        if line.startswith("# "):
            continue
        if any(line.startswith(prefix) for prefix in SKIP_LINE_PREFIXES):
            continue
        if line.startswith("---"):
            continue
        if line.startswith("|"):
            continue
        if line.startswith("-") and not line.startswith("—"):
            # Bullet lists are generally implementation/status lists in these atomics.
            continue

        match = DIALOGUE_RE.match(line)
        if match:
            speaker = match.group(1).strip()
            exact_text = match.group(2).strip()
            blocks.append(("dialogue", exact_text, speaker))
            continue

        stripped = plain_markdown(line)
        if not stripped:
            continue
        upper = stripped.upper()
        if upper.startswith("OBJECTIVE:") or upper.startswith("CURRENT STATE:"):
            continue
        if "DO NOT " in upper and ("REVEAL" in upper or "ADD" in upper or "IDENTIFY" in upper):
            continue
        blocks.append(("prose", stripped, None))

    return blocks


def add_reader_docx(all_sources: dict[str, list[tuple[SourceSpec, Path, bytes, str]]]) -> None:
    try:
        from docx import Document
        from docx.enum.section import WD_SECTION
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.shared import Inches, Pt
    except ImportError as exc:  # pragma: no cover - workflow installs python-docx
        raise RuntimeError("python-docx is required to build the reader") from exc

    READER_OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)

    styles = doc.styles
    styles["Normal"].font.name = "Aptos"
    styles["Normal"].font.size = Pt(10.5)
    styles["Title"].font.name = "Aptos Display"
    styles["Title"].font.size = Pt(26)
    styles["Heading 1"].font.name = "Aptos Display"
    styles["Heading 1"].font.size = Pt(20)
    styles["Heading 2"].font.name = "Aptos Display"
    styles["Heading 2"].font.size = Pt(14)
    styles["Heading 3"].font.name = "Aptos"
    styles["Heading 3"].font.size = Pt(11.5)

    p = doc.add_paragraph(style="Title")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("DIYSE\nChapters 0–3")
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p2.add_run("Spoiler-Free Exact-Dialogue Reader")
    r.bold = True
    r.font.size = Pt(15)
    note = doc.add_paragraph()
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    note.add_run(
        "Current atomic dialogue edition. Spoken lines are copied verbatim from the active production sources; "
        "writer-facing audits, implementation notes, and future-facing production metadata are omitted."
    ).italic = True

    doc.add_page_break()

    for chapter_i, chapter in enumerate(CHAPTERS):
        if chapter_i:
            doc.add_section(WD_SECTION.NEW_PAGE)
        doc.add_heading(f"Chapter {int(chapter.chapter)}", level=1)

        for spec, path, data, _digest in all_sources[chapter.chapter]:
            doc.add_heading(spec.label, level=2)
            blocks = reader_blocks(data.decode("utf-8"))
            last_was_heading = False
            for kind, text, speaker in blocks:
                if kind == "heading":
                    # Avoid a forest of implementation-style microheadings.
                    if text.upper().startswith(("BOSS —", "BATTLE —")):
                        p = doc.add_paragraph()
                        run = p.add_run(text)
                        run.bold = True
                        run.italic = True
                    else:
                        doc.add_heading(text.title() if text.isupper() else text, level=3)
                    last_was_heading = True
                elif kind == "dialogue":
                    p = doc.add_paragraph()
                    p.paragraph_format.space_after = Pt(3)
                    sr = p.add_run(f"{speaker}: ")
                    sr.bold = True
                    p.add_run(text)
                    last_was_heading = False
                else:
                    p = doc.add_paragraph(text)
                    p.paragraph_format.space_after = Pt(4)
                    last_was_heading = False
            if not last_was_heading:
                doc.add_paragraph()

    # Footer with derived-output warning.
    for sec in doc.sections:
        fp = sec.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("DIYSE Chapters 0–3 — derived reader; atomic dialogue files remain authority")
        fr.font.size = Pt(8)

    doc.save(READER_OUT)


def sync_status_append(index_path: Path, chapter: ChapterSpec) -> None:
    """Update only the current status surfaces and append a deterministic closure block.

    Historical audit prose is intentionally left intact. The top status and final closure are
    the current state, while old synchronization discussion remains provenance.
    """
    text = index_path.read_text(encoding="utf-8")
    status_line = (
        f"**Status:** CURRENT WORKING DIALOGUE PRODUCTION — CHAPTER {int(chapter.chapter)} ATOMIC DIALOGUE CURRENT; "
        "CURRENT CHARACTER/PERFORMANCE AUDITS RETAINED; COMBINED READ-THROUGH SYNCHRONIZED"
    )
    text = re.sub(r"(?m)^\*\*Status:\*\*.*$", status_line, text, count=1)

    combined_label = "Single-file read-through" if chapter.chapter == "03" else "Combined read-through"
    combined_line = (
        f"**{combined_label}:** `{chapter.output.name}` — **SYNCHRONIZED AGAINST CURRENT ATOMIC SOURCES**; "
        "source hashes are recorded in `../CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md`"
    )
    text = re.sub(
        rf"(?m)^\*\*{re.escape(combined_label)}:\*\*.*$",
        combined_line,
        text,
        count=1,
    )

    marker = "## Current synchronization closure"
    if marker in text:
        text = text[: text.index(marker)].rstrip()
    text += (
        "\n\n## Current synchronization closure\n\n"
        f"- `{chapter.output.name}` is synchronized against the chapter's current atomic dialogue sources.\n"
        "- source identity and SHA-256 values are recorded in `../CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md`.\n"
        "- the atomic scene files remain exact wording authority; the combined manuscript is a generated read-through.\n"
        "- `python tools/dialogue/sync_current_dialogue.py --check` must pass before the combined manuscript is described as current after any future atomic dialogue edit.\n"
    )
    index_path.write_text(text, encoding="utf-8")


def update_master_index() -> None:
    path = ROOT / "docs/03_DIALOGUE/DIALOGUE_MASTER_INDEX.md"
    text = path.read_text(encoding="utf-8")

    # Current top-level audit state.
    text = re.sub(
        r"(?m)^\*\*Mature-adult speech / profanity audit status:.*$",
        "**Mature-adult speech / profanity audit status: Chapters 0–3 CURRENT.**",
        text,
        count=1,
    )

    # Table/current prose may carry several older variants. Normalize the obvious stale labels.
    replacements = {
        "combined read-through stale for revised scenes": "combined read-through synchronized",
        "combined read-through stale where flagged": "combined read-through synchronized",
        "combined read-through stale": "combined read-through synchronized",
        "atomic files current, combined read-through stale": "atomic files current, combined read-through synchronized",
        "**stale against the current atomic scenes.**": "**synchronized against the current atomic scenes.**",
        "**stale against revised atomic dialogue.**": "**synchronized against revised atomic dialogue.**",
        "**requires resynchronization after atomic dialogue and prior numbering revisions.**": "**synchronized against current atomic dialogue.**",
        "**requires resynchronization after atomic dialogue and later character-balance revisions.**": "**synchronized against current atomic dialogue.**",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    marker = "# Chapters 0–3 synchronization closure"
    if marker in text:
        text = text[: text.index(marker)].rstrip()
    text += (
        "\n\n---\n\n# Chapters 0–3 synchronization closure\n\n"
        "The four combined rehearsal-first manuscripts are synchronized against their current atomic dialogue sources. "
        "The shared source/hash record is `PRODUCTION/CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md`. The reader artifact is generated from the same source set. "
        "After any future atomic dialogue edit, run `python tools/dialogue/sync_current_dialogue.py --check`; a failure means the derived read-throughs must be regenerated before being called current.\n"
    )
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Verify Markdown derived outputs without writing")
    parser.add_argument("--no-docx", action="store_true", help="Do not build the reader DOCX")
    args = parser.parse_args()

    all_sources: dict[str, list[tuple[SourceSpec, Path, bytes, str]]] = {
        chapter.chapter: resolved_chapter_sources(chapter) for chapter in CHAPTERS
    }
    protected_checks(all_sources)

    combined = {
        chapter.chapter: render_combined(chapter, all_sources[chapter.chapter]) for chapter in CHAPTERS
    }
    manifest = render_sync_manifest(all_sources, combined)

    expected: list[tuple[Path, str]] = [(chapter.output, combined[chapter.chapter]) for chapter in CHAPTERS]
    expected.append((SYNC_MANIFEST, manifest))

    if args.check:
        stale: list[str] = []
        for path, wanted in expected:
            got = path.read_text(encoding="utf-8") if path.exists() else ""
            if got != wanted:
                stale.append(str(path.relative_to(ROOT)))
        if stale:
            print("STALE derived dialogue outputs:")
            for path in stale:
                print(f"- {path}")
            return 1
        print("Dialogue combined manuscripts and sync manifest are current.")
        return 0

    for path, text in expected:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")

    for chapter in CHAPTERS:
        sync_status_append(chapter.index, chapter)
    update_master_index()

    if not args.no_docx:
        add_reader_docx(all_sources)
        print(f"wrote {READER_OUT.relative_to(ROOT)}")

    # Verify deterministic Markdown after writing.
    for path, wanted in expected:
        got = path.read_text(encoding="utf-8")
        if got != wanted:
            raise RuntimeError(f"Post-write verification failed for {path}")

    print("Synchronization complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
