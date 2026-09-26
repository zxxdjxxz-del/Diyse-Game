# Current runtime dialogue mirror

This directory is generated from docs/03_DIALOGUE/PRODUCTION/CHAPTER_00 through
CHAPTER_03. Those atomics remain exact spoken-wording authority.

manifest.json is the game-facing catalog for the current Chapters 0-3 dialogue.
Chapter 0's older S001-S006/C01-C02 runtime mirror has been retired; Git history preserves it. Older sibling chapter_01 through chapter_04 folders remain legacy implementation/proof assets pending their own retirement and must not be used as current dialogue wording authority.

Regenerate with:

python tools/dialogue/compile_current_runtime_dialogue.py
