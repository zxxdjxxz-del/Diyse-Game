#!/usr/bin/env python3
"""Synchronize DIYSE Chapters 0-3 combined dialogue manuscripts and reader.

Standalone Markdown scene files under docs/03_DIALOGUE/PRODUCTION/CHAPTER_## are
exact wording authority. This tool derives every combined/readable output from those
atomics so a generated manuscript can never silently become a competing authority.

Generated outputs:
- CHAPTER_##_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md for Chapters 0-3
- docs/03_DIALOGUE/PRODUCTION/CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md
- build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx

Use --check to verify generated Markdown/manifest state without writing anything.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

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

# Writer-facing sections are excluded from the spoiler-free reader *and* from guards
# that are supposed to inspect player-visible content. This prevents audit prose such
# as "the premature Nimera reference was removed" from being mistaken for story text.
SKIP_SECTION_TERMS = (
    "production note",
    "production notes",
    "person-brain / ensemble check",
    "person-brain / role-balance check",
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
    "presentation / canon check",
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


def plain_markdown(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^>\s*", "", text)
    text = text.replace("**", "").replace("`", "").replace("*", "")
    return text.strip()


def section_should_skip(heading: str) -> bool:
    low = plain_markdown(heading).lower()
    return any(term in low for term in SKIP_SECTION_TERMS)


def reader_blocks(source_text: str) -> list[tuple[str, str, str | None]]:
    """Return reader-visible (kind, text, speaker) blocks for one atomic source.

    Dialogue text is copied exactly after its Markdown speaker marker. Writer-facing
    audits/implementation sections are omitted.
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

        if skip_section or not line.strip() or line.startswith("# "):
            continue
        if any(line.startswith(prefix) for prefix in SKIP_LINE_PREFIXES):
            continue
        if line.startswith("---") or line.startswith("|"):
            continue
        if line.startswith("-") and not line.startswith("—"):
            continue

        match = DIALOGUE_RE.match(line)
        if match:
            blocks.append(("dialogue", match.group(2).strip(), match.group(1).strip()))
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


def resolve_source(chapter: ChapterSpec, spec: SourceSpec) -> Path:
    matches = [p for p in chapter.directory.glob(spec.pattern) if p.is_file()]
    matches = [p for p in matches if p != chapter.output and "AUTHORITY_INDEX" not in p.name]
    if len(matches) != 1:
        rels = [str(p.relative_to(ROOT)) for p in matches]
        raise RuntimeError(
            f"{chapter.title} / {spec.label}: {spec.pattern!r} must resolve exactly once; "
            f"found {len(matches)}: {rels}"
        )
    return matches[0]


def resolved_chapter_sources(chapter: ChapterSpec) -> list[tuple[SourceSpec, Path, bytes, str]]:
    out: list[tuple[SourceSpec, Path, bytes, str]] = []
    seen: set[Path] = set()
    for spec in chapter.sources:
        path = resolve_source(chapter, spec)
        if path in seen:
            raise RuntimeError(f"Duplicate atomic source selected: {path}")
        seen.add(path)
        data = path.read_bytes()
        data.decode("utf-8")
        out.append((spec, path, data, sha256_bytes(data)))
    return out


def visible_chapter_text(sources: list[tuple[SourceSpec, Path, bytes, str]]) -> str:
    chunks: list[str] = []
    for _spec, _path, data, _digest in sources:
        blocks = reader_blocks(data.decode("utf-8"))
        for kind, text, speaker in blocks:
            if kind == "dialogue":
                chunks.append(f"{speaker}: {text}")
            else:
                chunks.append(text)
    return "\n".join(chunks)


def protected_checks(all_sources: dict[str, list[tuple[SourceSpec, Path, bytes, str]]]) -> None:
    raw_by_ch = {
        ch: "\n".join(data.decode("utf-8") for _, _, data, _ in sources)
        for ch, sources in all_sources.items()
    }

    must_exist = {
        "01": ("**CYANIS:** Old slut?", "**TORREN:** Bitch."),
        "03": (
            "PREVIOUS ERROR",
            "LAST SENTINEL CONFIRMED",
            "**CYANIS:** I bet you use that cape to sneak up on the goats you fuck.",
            "**TORREN:** You look like a walking dick in armor.",
            "Might. Elements. Grace. Memory. Perception. Ruin.",
        ),
    }
    for chapter, needles in must_exist.items():
        for needle in needles:
            if needle not in raw_by_ch[chapter]:
                raise RuntimeError(f"Protected anchor missing in Chapter {int(chapter)}: {needle}")

    stale_face_list = "Might. Elements. Grace. Resource. Perception. Ruin."
    if stale_face_list in raw_by_ch["03"]:
        raise RuntimeError("Stale Chapter-3 Resource Face list is present; expected Memory.")

    # Nimera is not met until Chapter 3. Search reader-visible Chapter-1 content only,
    # not writer-facing notes that may legitimately mention the correction itself.
    ch1_visible = visible_chapter_text(all_sources["01"])
    if re.search(r"\bNimera\b", ch1_visible, flags=re.IGNORECASE):
        raise RuntimeError("Reader-visible Chapter 1 still references Nimera before her Chapter-3 meeting.")


def render_combined(chapter: ChapterSpec, sources: list[tuple[SourceSpec, Path, bytes, str]]) -> str:
    lines: list[str] = [
        f"# DIYSE — {chapter.title} — Synchronized Rehearsal-First Working Dialogue Manuscript",
        "",
        "**Status:** CURRENT DERIVED READ-THROUGH — SYNCHRONIZED AGAINST CURRENT ATOMIC DIALOGUE SOURCES",
        "",
        "**Authority rule:** standalone atomic scene files remain exact wording authority. This file is generated, not hand-authored. After any atomic edit, rerun `python tools/dialogue/sync_current_dialogue.py` before describing this manuscript as current.",
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
        lines.extend(
            [
                f"## {spec.label}",
                "",
                f"**Atomic source:** `{path.name}`  ",
                f"**Source SHA-256:** `{digest}`",
                "",
                data.decode("utf-8").rstrip(),
                "",
                "---",
                "",
            ]
        )

    lines.extend(
        [
            "## Synchronization footer",
            "",
            "This derived manuscript was assembled exclusively from the atomics listed above. No dialogue wording was rewritten during assembly.",
            "",
        ]
    )
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
        "The atomics remain exact wording authority. Combined manuscripts and the reader are generated derivatives.",
        "",
        "## Combined manuscripts",
        "",
        "| Chapter | Combined manuscript | Combined SHA-256 | Atomic sources |",
        "|---|---|---|---:|",
    ]
    for chapter in CHAPTERS:
        lines.append(
            f"| {int(chapter.chapter)} | `{chapter.output.relative_to(ROOT)}` | "
            f"`{sha256_bytes(combined[chapter.chapter].encode('utf-8'))}` | "
            f"{len(all_sources[chapter.chapter])} |"
        )

    for chapter in CHAPTERS:
        lines.extend(
            [
                "",
                f"## Chapter {int(chapter.chapter)} sources",
                "",
                "| Order | Canonical slot | Path | SHA-256 |",
                "|---:|---|---|---|",
            ]
        )
        for i, (spec, path, _data, digest) in enumerate(all_sources[chapter.chapter], start=1):
            lines.append(f"| {i} | {spec.label} | `{path.relative_to(ROOT)}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## Verification rule",
            "",
            "Run `python tools/dialogue/sync_current_dialogue.py --check`. A non-zero exit means a combined manuscript or this manifest is stale relative to current atomics.",
            "",
        ]
    )
    return "\n".join(lines)


def add_reader_docx(all_sources: dict[str, list[tuple[SourceSpec, Path, bytes, str]]]) -> None:
    try:
        from docx import Document
        from docx.enum.section import WD_SECTION
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.shared import Inches, Pt
    except ImportError as exc:
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

    title = doc.add_paragraph(style="Title")
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.add_run("DIYSE\nChapters 0–3")

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sr = subtitle.add_run("Spoiler-Free Exact-Dialogue Reader")
    sr.bold = True
    sr.font.size = Pt(15)

    note = doc.add_paragraph()
    note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    nr = note.add_run(
        "Current atomic dialogue edition. Spoken lines are copied verbatim from active production sources; "
        "writer-facing audits, implementation notes, and future-facing production metadata are omitted."
    )
    nr.italic = True
    doc.add_page_break()

    for chapter_i, chapter in enumerate(CHAPTERS):
        if chapter_i:
            doc.add_section(WD_SECTION.NEW_PAGE)
        doc.add_heading(f"Chapter {int(chapter.chapter)}", level=1)

        for spec, _path, data, _digest in all_sources[chapter.chapter]:
            doc.add_heading(spec.label, level=2)
            last_was_heading = False
            for kind, text, speaker in reader_blocks(data.decode("utf-8")):
                if kind == "heading":
                    if text.upper().startswith(("BOSS —", "BATTLE —")):
                        p = doc.add_paragraph()
                        r = p.add_run(text)
                        r.bold = True
                        r.italic = True
                    else:
                        doc.add_heading(text.title() if text.isupper() else text, level=3)
                    last_was_heading = True
                elif kind == "dialogue":
                    p = doc.add_paragraph()
                    p.paragraph_format.space_after = Pt(3)
                    who = p.add_run(f"{speaker}: ")
                    who.bold = True
                    p.add_run(text)
                    last_was_heading = False
                else:
                    p = doc.add_paragraph(text)
                    p.paragraph_format.space_after = Pt(4)
                    last_was_heading = False
            if not last_was_heading:
                doc.add_paragraph()

    for sec in doc.sections:
        fp = sec.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("DIYSE Chapters 0–3 — derived reader; atomic dialogue files remain authority")
        fr.font.size = Pt(8)

    doc.save(READER_OUT)


def sync_status_append(index_path: Path, chapter: ChapterSpec) -> None:
    """Mark a chapter combined read-through current only after successful generation."""
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
        f"- `{chapter.output.name}` is synchronized against the chapter's current atomics.\n"
        "- source identity and SHA-256 values are recorded in `../CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md`.\n"
        "- atomics remain exact wording authority; the combined manuscript is generated.\n"
        "- `python tools/dialogue/sync_current_dialogue.py --check` must pass before this combined manuscript is called current after future atomic edits.\n"
    )
    index_path.write_text(text, encoding="utf-8")


def update_master_index() -> None:
    path = ROOT / "docs/03_DIALOGUE/DIALOGUE_MASTER_INDEX.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"(?m)^\*\*Mature-adult speech / profanity audit status:.*$",
        "**Mature-adult speech / profanity audit status: Chapters 0–3 CURRENT.**",
        text,
        count=1,
    )

    replacements = {
        "combined read-through stale for revised scenes": "combined read-through synchronized",
        "combined read-through stale where flagged": "combined read-through synchronized",
        "atomic files current, combined read-through stale": "atomic files current, combined read-through synchronized",
        "combined read-through stale": "combined read-through synchronized",
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
        "The shared source/hash record is `PRODUCTION/CHAPTER_0_3_DIALOGUE_SYNC_MANIFEST.md`. "
        "The reader artifact is generated from the same source set. After any future atomic dialogue edit, "
        "run `python tools/dialogue/sync_current_dialogue.py --check`; a failure means the derived read-throughs "
        "must be regenerated before being called current.\n"
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
    expected: list[tuple[Path, str]] = [
        (chapter.output, combined[chapter.chapter]) for chapter in CHAPTERS
    ] + [(SYNC_MANIFEST, manifest)]

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

    for path, wanted in expected:
        if path.read_text(encoding="utf-8") != wanted:
            raise RuntimeError(f"Post-write verification failed for {path}")

    print("Synchronization complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
