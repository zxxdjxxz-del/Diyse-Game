# Current runtime dialogue mirror

This directory is generated from docs/03_DIALOGUE/PRODUCTION/CHAPTER_00 through
CHAPTER_03. Those atomics remain exact spoken-wording authority.

manifest.json is the game-facing catalog for the current Chapters 0-3 dialogue.
Superseded Chapter 1-3 S/H/C runtime resources have been retired from the live
game/content/dialogue tree and remain recoverable through Git history.

Chapter 4 has no approved current runtime dialogue mirror yet. Retired pre-restructure
Chapter 4 S/H/C resources are not kept in the live tree; Git history is provenance only.
Generate Chapter 4 runtime resources only after current Chapter 4 dialogue is authored,
Canon Checker-passed, and approved.

Regenerate with:

python tools/dialogue/compile_current_runtime_dialogue.py
