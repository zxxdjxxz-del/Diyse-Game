# Current runtime dialogue mirror

This directory is generated from docs/03_DIALOGUE/PRODUCTION/CHAPTER_00 through
CHAPTER_03. Those atomics remain exact spoken-wording authority.

manifest.json is the game-facing catalog for the current Chapters 0-3 dialogue.
Superseded Chapter 1-3 S/H/C runtime resources have been retired from the live
game/content/dialogue tree and remain recoverable through Git history.

Chapter 4 has no approved current runtime dialogue mirror yet. Its obsolete pre-restructure
S/H/C implementation resources are quarantined under
game/content/dialogue/proof/legacy_chapter_04/ and are non-authoritative.

Regenerate with:

python tools/dialogue/compile_current_runtime_dialogue.py
