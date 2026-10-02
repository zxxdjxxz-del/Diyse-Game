# Diyse HD-2D Presentation Runtime

This directory contains reusable current presentation/runtime infrastructure for Diyse's HD-2D / 2.5D implementation.

These systems are implementation support only. They must not decide or lock story dialogue, ordinary-enemy or Hunt placement, final balance, or character identity. Current owner-domain authority remains in `docs/`.

## Current presentation direction

- permanent-party field/battle character production uses **rigged 3D models matched to the exact current 2D masters**;
- the old fixed ~80 px field / ~200–220 px battle sprite targets are retired as production requirements;
- runtime readability is validated at the actual field and battle cameras rather than by a dedicated sprite-size lock;
- ordinary route/dungeon/wilderness traversal renders **Cyanis only** as the player field character;
- towns, camps and Cresthaven may show relevant party/NPC field models, and authored triggered scenes may spawn the participants they need;
- battle presentation retains authored party/enemy composition, open readable staging and replaceable presentation assets;
- environment presentation uses authored layered backgrounds, selective depth geometry, bounded cameras and restrained parallax;
- environment/state swaps and nonlethal-resolution hooks remain reusable presentation infrastructure;
- Android quality scaling may reduce decorative effects without changing gameplay state or character identity.

Current routing:
- character scale/silhouette: `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTER_SCALE_AND_SILHOUETTE.md`
- exact character visual masters: `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`
- traversal/dialogue staging: `docs/13_UI_AND_IMPLEMENTATION/FIELD_TRAVERSAL_AND_DIALOGUE_PRESENTATION_LOCK.md`
- enemy/encounter placement: `docs/09_ENEMIES_AND_ENCOUNTERS/`

There is no separate **Elite** encounter category. Stronger enemies that belong to normal pools remain owned by the ordinary-enemy/formation authority.

Runtime character models, backgrounds, VFX and other implementation assets may remain replaceable until explicitly approved, but replacement work must preserve the exact current visual masters and current presentation rules.

## Player-facing opening intro

The game launches through `world_intro.tscn` before handing off to the current playable entry scene.

- wording authority: `docs/04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md`
- generated runtime data: `game/content/presentation/player_facing_world_intro.json`
- sync/validation: `tools/dialogue/sync_player_facing_world_intro.py`
- the intro is presented as Nimera's signed text, not as an in-world pre-Chapter-0 conversation
- changes to the authority file must regenerate the runtime JSON; CI rejects drift
