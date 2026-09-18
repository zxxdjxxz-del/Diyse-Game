# Current runtime dialogue mirror

This directory is generated from docs/03_DIALOGUE/PRODUCTION/CHAPTER_00 through
CHAPTER_03. Those atomics remain exact spoken-wording authority.

manifest.json is the game-facing catalog for the current Chapters 0-3 dialogue.
The older sibling game/content/dialogue/chapter_00 through chapter_03 S-scene
Resources are retained only as legacy implementation/proof assets and must not be used
as current dialogue wording authority.

Regenerate with:

python tools/dialogue/compile_current_runtime_dialogue.py
