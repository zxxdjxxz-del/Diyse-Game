#!/usr/bin/env python3
"""Enforce the policy that superseded project history does not live on main."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY_ARCHIVE_SEGMENT = "99_" + "ARCHIVE"
RETIRED_DOC_REFERENCE_RE = re.compile(
    r"\b(?:RETIRED_[A-Z0-9_]+|REMOVED_SYSTEMS_FIREWALL)\.md\b"
)
HISTORICAL_DOC_ROOTS = (
    ROOT / "docs" / "03_DIALOGUE" / "EXPERIMENTS",
    ROOT / "docs" / "15_AUDIO_AND_MUSIC" / "RESEARCH_ARCHIVE",
    ROOT / "docs" / "14_ART_AND_VISUALS" / "PRODUCTION" / "ASSET_LIBRARY" / "archive",
)
HISTORICAL_REFERENCE_SEGMENTS = (
    "EXPERIMENTS/",
    "RESEARCH_ARCHIVE/",
    "PRODUCTION/ASSET_LIBRARY/archive/",
    "GLOBAL_ASSET_ARCHIVE_LEDGER.md",
    "DIYSE_ASSET_LIBRARY_MASTER_2026-08-30_v5",
    "Asset Library Master v5",
)
RETIRED_RIG_STAGE_TOKENS = (
    "ILYRA_AUTHORED_GEOMETRY_MANIFEST.md",
    "ILYRA_DEFORMATION_AWARE_MANIFEST.md",
    "ILYRA_MODULAR_BLOCKOUT_MANIFEST.md",
    "ILYRA_PRODUCTION_MESH_V04_MANIFEST.md",
    "ILYRA_PRODUCTION_TOPOLOGY_MANIFEST.md",
    "ILYRA_PRODUCTION_V06_LIVE_MANIFEST.md",
    "ILYRA_SECONDARY_MOTION_MANIFEST.md",
    "ilyra_anime_body_ual.",
    "ilyra_authored_geometry.",
    "ilyra_deformation_aware.",
    "ilyra_modular_blockout.",
    "ilyra_production_topology.",
    "ilyra_production_v06_preview.",
    "ilyra_secondary_motion.",
    "ilyra_ual_proxy.",
    "ual_rig_preview.tscn",
    "generate_ilyra_anime_body_proxy.py",
    "Ilyra_AnimeBody_UAL.glb",
    "Ilyra_ProductionMesh_v06",
    "Ilyra_ProductionMesh_v04",
)
PROGRESSION_HISTORY_RE = re.compile(
    r"\b(?:v85|v89|v91|v92|Audit12[3-8])\b"
    r"|Historical migration provenance"
    r"|Historical progression provenance"
    r"|Regional Hunt retirement sync",
    re.IGNORECASE,
)
BALANCE_HISTORY_RE = re.compile(
    r"\bhistorical\b"
    r"|\bretired\b"
    r"|\bsuperseded\b"
    r"|\bobsolete\b"
    r"|PASS/RETAIN"
    r"|\bAudit\d+\b"
    r"|\bv(?:8\d|9\d|10\d)\b",
    re.IGNORECASE,
)
TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".py", ".gd", ".yml", ".yaml", ".cfg",
    ".tres", ".tscn", ".toml", ".ini",
}


def main() -> int:
    errors: list[str] = []

    archive_root = ROOT / "docs" / LEGACY_ARCHIVE_SEGMENT
    if archive_root.exists():
        errors.append(
            f"{archive_root.relative_to(ROOT)} exists; superseded project history belongs in Git history"
        )

    for historical_root in HISTORICAL_DOC_ROOTS:
        if historical_root.exists():
            errors.append(
                f"{historical_root.relative_to(ROOT)} exists; non-production experiment/research history belongs in Git history"
            )

    for path in (ROOT / "docs").rglob("*"):
        if not path.is_file():
            continue
        if path.name.startswith("RETIRED_") or path.name == "REMOVED_SYSTEMS_FIREWALL.md":
            errors.append(
                f"{path.relative_to(ROOT)} is a retired/removed-system prose layer; use current owner authority plus Git history"
            )
        if path.name == "GLOBAL_ASSET_ARCHIVE_LEDGER.md":
            errors.append(
                f"{path.relative_to(ROOT)} is historical asset upload-event bookkeeping; current source manifests own active provenance"
            )
        if path.name == "ARCHIVE_SCRIBE_ENGINE.md":
            errors.append(
                f"{path.relative_to(ROOT)} is a stale duplicate Memory Construct authority; use STORY_BOSSES/MEMORY_CONSTRUCT.md"
            )
        relative_text = path.relative_to(ROOT).as_posix()
        if any(token in relative_text for token in RETIRED_RIG_STAGE_TOKENS):
            errors.append(
                f"{path.relative_to(ROOT)} is a superseded Ilyra rig-preview stage; use the current v0.7 preview path"
            )

    validator_path = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == validator_path:
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if LEGACY_ARCHIVE_SEGMENT in text:
            errors.append(
                f"{path.relative_to(ROOT)} still references the removed dedicated history archive"
            )
        matches = sorted(set(RETIRED_DOC_REFERENCE_RE.findall(text)))
        if matches:
            errors.append(
                f"{path.relative_to(ROOT)} still references removed retired-document layer: {', '.join(matches)}"
            )
        historical_refs = [segment for segment in HISTORICAL_REFERENCE_SEGMENTS if segment in text]
        if historical_refs:
            errors.append(
                f"{path.relative_to(ROOT)} still references removed experiment/research history: {', '.join(historical_refs)}"
            )
        retired_rig_refs = sorted({token for token in RETIRED_RIG_STAGE_TOKENS if token in text})
        if retired_rig_refs:
            errors.append(
                f"{path.relative_to(ROOT)} still references superseded Ilyra rig-preview stage: {', '.join(retired_rig_refs)}"
            )
        if "ARCHIVE_SCRIBE_ENGINE.md" in text:
            errors.append(
                f"{path.relative_to(ROOT)} still references stale Memory Construct duplicate authority"
            )
        relative_path = path.relative_to(ROOT).as_posix()
        if relative_path.startswith("docs/10_PROGRESSION_AND_EXP/") and PROGRESSION_HISTORY_RE.search(text):
            errors.append(
                f"{relative_path} contains migration/version-history language; progression authority must describe the current planning model directly"
            )
        if relative_path.startswith("docs/16_BALANCE_AND_TESTING/") and BALANCE_HISTORY_RE.search(text):
            errors.append(
                f"{relative_path} contains retired/versioned test-history language; balance authority must describe current methods, debt, and certification state directly"
            )

    if errors:
        print("Repository history policy validation FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository history policy validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
