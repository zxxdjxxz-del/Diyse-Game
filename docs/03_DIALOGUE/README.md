# 03_DIALOGUE

**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicit user corrections/current domain migrations.  

This is the canonical home for **spoken dialogue and dialogue-scene authoring**.

## Current Dialogue Engine authority

Story function, scene order, required events, knowledge, recruitment, reveal timing, mandatory outcomes, and canon-safe staging requirements live in `02_STORY`. Combat mechanics live in `05_BATTLE_SYSTEM` / `09_ENEMIES_AND_ENCOUNTERS`; Card mechanics live in `07_CARDS`; progression lives in `10_PROGRESSION_AND_EXP`.

Dialogue Engine architecture:
`AGENT_SYSTEM/README.md`

Unified scene-construction stack:
`AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`

Dialogue-facing map/traversal interface:
`../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`

### Full-stack authoring rule

Dialogue is not authored as isolated prose and fitted into the game afterward. Current scenes are built from the relevant story/canon state, character brains, relationship state, lived-world context, map/traversal state, gameplay pressure, dialogue UI, and economical HD-2D presentation.

Working mnemonic:

> **Talk like people. React like anime characters. Time jokes like a comedy. Structure important scenes like a great RPG. Remember they are living through a war. And occasionally let them argue about absolutely nothing.**

### Rehearsal-first rule

Current production follows `AGENT_SYSTEM/REHEARSAL_FIRST_AUTHORING_LOCK.md`:

> **Do not generate the production script directly from canon constraints. Rehearse the people first, edit the rehearsal second, canon-check the edited scene third.**

The Engine generates rich human behavior; the Dialogue Editor cuts aggressively. More natural material is useful, but more lines are not automatically better.

### Knowledge-firewall rule

The writer and Canon Checker police what characters know. Characters should not sound like they are policing the knowledge firewall themselves. Use natural uncertainty, silence, disagreement, mistaken inference, or no comment instead of repeated evidence disclaimers.

### Presentation rule

Ordinary route/dungeon/wilderness traversal shows Cyanis only as the visible controllable field character. Towns, camps, Cresthaven, and authored story triggers may show relevant present characters as simple field models. Portraits + dialogue box carry most acting. Micro-choreography is not the default.

## Current chapter production status

- **Chapter 0 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_00/CHAPTER_00_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- **Chapter 1 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_01/CHAPTER_01_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- **Chapter 2 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_02/CHAPTER_02_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- **Chapter 3 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_03/CHAPTER_03_REHEARSAL_FIRST_WORKING_DIALOGUE_MANUSCRIPT.md`
- Chapters 4–13 remain pending/rebuilding according to current story and authoring-status authority.

`COMPLETE CURRENT WORKING PRODUCTION` means the chapter is assembled end-to-end and is the version to use for implementation and future revision. It remains editable during playtesting; it is not a permanent line lock.

## Current Chapters 0–3 runtime synchronization

The standalone production atomics under `PRODUCTION/CHAPTER_00` through `CHAPTER_03` remain exact spoken-wording authority.

The current game-facing mirror is generated at:

`game/content/dialogue/current/`

Current synchronization contract:
- **60 canonical current runtime scenes**;
- **3,440 spoken lines**;
- generated directly from current production atomics;
- source and spoken-sequence hashes recorded in `game/content/dialogue/current/manifest.json`;
- validated in Godot by `tests/dialogue/validate_current_dialogue_resources.gd`;
- the older sibling `game/content/dialogue/chapter_00` through `chapter_03` S-scene Resources are legacy implementation/proof assets and are not current spoken-wording authority.

Regenerate/check with:

`python tools/dialogue/compile_current_runtime_dialogue.py`  
`python tools/dialogue/compile_current_runtime_dialogue.py --check`

The Chapters 0–3 read-through is also generated from current atomics. Its player-facing world introduction is owned by `04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md`, and its between-beat encounter bridges are guarded against current `09_ENEMIES_AND_ENCOUNTERS` placement authority. Those layers may add reader context but may not alter spoken dialogue.

## Chapter 0–1 source cleanup

The obsolete `LINE_COMPLETE/CHAPTER_00` and `LINE_COMPLETE/CHAPTER_01` source sets have been removed from the live repository tree now that both chapters have complete current rehearsal-first production manuscripts.

The old Chapter-0 locked-manuscript casing overlay, the temporary Chapter-0 quick-pass cumulative manuscript, and the superseded pre-rehearsal Chapter-1 cumulative manuscript have also been removed.

Git history remains the provenance/archive for those superseded versions. They must not be restored as competing dialogue authority.

Historical `LINE_COMPLETE` material for later chapters may remain temporarily until those chapters receive current rehearsal-first replacements. Its presence does not make it current spoken-dialogue authority.

## Explicit exact-line anchors

The only older wording that must survive regeneration verbatim is wording the user has explicitly selected as an exact line/joke anchor.

Current examples:
- Ch1 C04: `old slut` remains the exact joke anchor in the current exchange.
- Ch3 H01:
  - Cyanis: `I bet you use that cape to sneak up on the goats you fuck.`
  - Torren: `You look like a walking dick in armor.`

These anchors do not lock surrounding dialogue.

## What this folder owns

- current spoken dialogue generated through the Dialogue Engine;
- current chapter dialogue manuscripts under `PRODUCTION/CHAPTER_##/`;
- standalone production scene drafts/specs;
- dialogue-specific continuity/presentation rules;
- explicitly preserved line anchors;
- authoring-status gates for chapters not yet rebuilt.

## What this folder does not own

Embedded scene notes may mention mechanics or story structure for context, but those are not editable authority here. Current mechanics and story structure must be read from their canonical system/story folders.

## Current bounded corrections

1. Current Face list is **Might / Elements / Grace / Perception / Memory / Ruin**.
2. Chapter 0 uses two distinct incomplete green-and-gold Card responses; neither is a Prime activation.
3. The recovery casing breaks during Chapter 0 P06; the Card itself survives intact and is carried directly afterward.
4. Chapter 1 C04 preserves the `old slut / old cut` misunderstanding within current early Cyanis/Torren relationship timing.
5. Chapter 1 C05 is `Not Professionally`: Ilyra changes Maevra's splint; limited magic eases pain/strain but cannot mend the broken bone; the private conversation turns to Maevra and Torren.
