# Diyse HD-2D Presentation Runtime

This directory contains reusable runtime presentation contracts introduced under **v1.73 / Audit88**.

These systems are presentation/runtime infrastructure only. They must not decide or lock story dialogue, final ordinary-enemy rosters, Elite placement, Hunt placement, final balance, or final visual assets.

The runtime layer exists so Chapters 0–4 can be implemented against the approved HD-2D grammar now while final sprites/backgrounds/VFX remain replaceable.

Core targets:

- field character target scale: approximately 80 px;
- battle character target scale: approximately 200 px;
- large high-resolution dialogue portraits;
- party-left / enemy-right / open-center battle composition;
- authored environment layers and state swaps;
- bounded cameras and restrained parallax;
- reusable nonlethal resolution and Prime presentation hooks;
- Android quality scaling for decorative effects only.

Do not add chapter-specific Elite placement or dialogue ownership here. Elite placement remains a separate later encounter-design decision unless an individual Elite is explicitly canon-locked elsewhere.

## Player-facing opening intro

The game now launches through `world_intro.tscn` before handing off to the current playable entry scene.

- wording authority: `docs/04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md`
- generated runtime data: `game/content/presentation/player_facing_world_intro.json`
- sync/validation: `tools/dialogue/sync_player_facing_world_intro.py`
- the intro is presented as Nimera's signed text, not as an in-world pre-Chapter-0 conversation
- changes to the authority file must regenerate the runtime JSON; CI rejects drift
