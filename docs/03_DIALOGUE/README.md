# 03_DIALOGUE

**Current authority:** live owning-domain files, current production atomics, and later explicit approved revisions.  

This is the canonical home for **spoken dialogue and dialogue-scene authoring**.

## Current Dialogue Engine authority

Story function, scene order, required events, knowledge, recruitment, reveal timing, mandatory outcomes, and canon-safe staging requirements live in `02_STORY`. Combat mechanics live in `05_BATTLE_SYSTEM` / `09_ENEMIES_AND_ENCOUNTERS`; Card mechanics live in `07_CARDS`; progression lives in `10_PROGRESSION_AND_EXP`.

Dialogue Engine architecture:
`AGENT_SYSTEM/README.md`

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

### Presentation and timing rule

Ordinary route/dungeon/wilderness traversal shows Cyanis only as the visible controllable field character. Towns, camps, Cresthaven, and authored story triggers may show relevant present characters as simple field models. Portraits + dialogue box carry most acting. Micro-choreography is not the default.

> **No spoken dialogue runs during player-controlled traversal or active combat.**

Route conversations use authored stop triggers with movement/input paused. Battle-related dialogue occurs immediately before combat begins or after combat has fully ended.

## Current chapter production status

- **Chapter 0 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_00/CHAPTER_00_DIALOGUE_MANUSCRIPT.md`
- **Chapter 1 — LOCKED CURRENT WORKING PRODUCTION — SYNCHRONIZED 2026-09-25**  
  `PRODUCTION/CHAPTER_01/CHAPTER_01_DIALOGUE_MANUSCRIPT.md`
- **Chapter 2 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_02/CHAPTER_02_DIALOGUE_MANUSCRIPT.md`
- **Chapter 3 — COMPLETE CURRENT WORKING PRODUCTION**  
  `PRODUCTION/CHAPTER_03/CHAPTER_03_DIALOGUE_MANUSCRIPT.md`
- Chapters 4–13 remain pending/rebuilding according to current story and authoring-status authority.

`COMPLETE CURRENT WORKING PRODUCTION` means a chapter is assembled end-to-end and is the version to use for implementation and future revision. Chapter 1 is additionally **LOCKED CURRENT**: its present atomic wording is the active authority until an explicit later revision reopens it. Playtesting can still motivate a deliberate future revision.

## Current Chapters 0–3 runtime synchronization

The standalone production atomics under `PRODUCTION/CHAPTER_00` through `CHAPTER_03` remain exact spoken-wording authority.

The current game-facing mirror is generated at:

`game/content/dialogue/current/`

Current synchronization contract:
- **52 canonical current runtime scenes**;
- **2,015 spoken lines**;
- generated directly from current production atomics;
- source and spoken-sequence hashes recorded in `game/content/dialogue/current/manifest.json`;
- validated in Godot by `tests/dialogue/validate_current_dialogue_resources.gd`;
- the former direct `game/content/dialogue/chapter_00` through `chapter_03` runtime folders and obsolete Chapter-4 proof resources are retired from the live tree and recoverable through Git history; only `current/` is the live generated mirror, while `proof/` contains only two non-canon dialogue-engine test fixtures.

Regenerate/check with:

`python tools/dialogue/compile_current_runtime_dialogue.py`  
`python tools/dialogue/compile_current_runtime_dialogue.py --check`

The Chapters 0–3 read-through is also generated from current atomics. Its player-facing world introduction is owned by `04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md`, and its between-beat encounter bridges are guarded against current `09_ENEMIES_AND_ENCOUNTERS` placement authority. Those layers may add reader context but may not alter spoken dialogue.

## Superseded dialogue source cleanup

Obsolete `LINE_COMPLETE/` source sets are not kept in the live repository tree. Chapters 0–3 are represented by their current `PRODUCTION/` atomics, and the retired pre-restructure Chapter-4 S022–S026 / H05 / C08–C09 material is Git-history provenance only until current Chapter-4 dialogue is authored.

The migration-era `CURRENT_DIALOGUE_CORRECTIONS.md` overlay, `EXACT_SOURCE_MANIFEST.md` checksum ledger, and dated cross-chapter `CHAPTERS_00_03_FULL_SOURCE_CLOSURE_2026-09-13.md` recap have also been removed from the live authority surface. Their historical content and hashes remain recoverable through Git history; current chapter authority indexes, story owners, production atomics, and generated runtime manifests now carry the live information needed for implementation.

The old Chapter-0 locked-manuscript casing overlay, the temporary Chapter-0 quick-pass cumulative manuscript, and the superseded pre-rehearsal Chapter-1 cumulative manuscript have also been removed.

Git history remains the provenance/archive for superseded dialogue versions. Historical overlays and checksum ledgers must not be restored as competing dialogue authority or used as current Chapter-4 production seed material.

## Explicit exact-line anchors

The only older wording that must survive regeneration verbatim is wording the user has explicitly selected as an exact line/joke anchor.

Current examples:
- Ch1 C03: `CYANIS: Old slut?` / `TORREN: Bitch.` remains the exact joke anchor; the later `TORREN: Bitch.` / `CYANIS: Old slut.` callback also remains protected.
- Ch3 C06 (historical H01 anchor):
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
3. The recovery casing breaks during Chapter 0 B06; the Card itself survives intact and is carried directly afterward.
4. Chapter 1 C03 preserves the `old slut` / `old cut` misunderstanding and the protected `Old slut?` / `Bitch.` exchange within current early Cyanis/Torren relationship timing.
5. Chapter 1 C04 is `Not Professionally`: Ilyra changes Maevra's splint; limited magic eases pain/strain but cannot mend the broken bone; the private conversation turns to Maevra and Torren.
