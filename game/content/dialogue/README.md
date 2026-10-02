# DIYSE Runtime Dialogue Content

**Current runtime authority:** `game/content/dialogue/current/`

The live Chapters 0-3 dialogue mirror is generated from approved standalone atomics under
`docs/03_DIALOGUE/PRODUCTION/`. Use `current/manifest.json` and the generated per-chapter
Resources for runtime dialogue.

## Retired runtime history

The former direct `chapter_01/`, `chapter_02/`, and `chapter_03/` S/H/C resource folders,
plus the obsolete pre-restructure Chapter 4 proof resources, have been removed from the live
content tree. Git history is the provenance source for those retired implementations.

Chapter 4 does not yet have approved exact runtime dialogue. Do not regenerate or load a
Chapter 4 runtime mirror until current Chapter 4 dialogue has been authored, Canon Checker-passed,
and explicitly approved.

## Source of truth

Exact spoken wording remains owned by approved atomics in
`docs/03_DIALOGUE/PRODUCTION/CHAPTER_##/`, subject to the chapter dialogue authority index.

## Automated layout guard

`python tools/dialogue/validate_authority_naming.py` enforces the live runtime layout.

Allowed direct entries under `game/content/dialogue/` are only:
- `README.md`;
- `current/`.

Direct `chapter_##/`, `proof/`, or other historical runtime folders are a validation failure.
