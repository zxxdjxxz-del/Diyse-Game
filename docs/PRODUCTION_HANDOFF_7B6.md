# Step 7B.6 — Production Handoff Lock

**Status:** COMPLETE / PASS — historical technical acceptance record  
**Authority at original acceptance:** v1.35 / Audit47  
**Current whole-project authority:** **v1.64 / Audit79**  
**Original parent at implementation start:** v1.34 / Audit46  
**Starting `main` commit:** `ae3bcf120cfb6d956f5159519025734f1eb26912`  
**Accepted implementation merge:** `96c6bdc77f39c988f2185634b4e51546f2a0d76b`

This document records what Step 7B.6 technically proved. Its old v1.35/Audit47 phase labels and former Step 7C hold are historical context, not current project status. Current canon and production status are controlled by v1.64/Audit79, `AGENTS.md`, `docs/ACTIVE_CANON.md`, and `docs/IMPLEMENTATION_STATUS.md`.

## Purpose

Step 7B.6 closed the final interface gap between completed dialogue craft and the proven Godot implementation. It did not write canon scenes. It defined the format in which production scenes can be authored and consumed without putting story text into engine code.

## Locked compatible handoff decisions

1. Production dialogue is stored as `DiyseDialogueSceneDefinition` Resources.
2. Scene data uses stable semantic IDs instead of portrait asset paths.
3. Portrait assets are resolved through `DiyseDialoguePortraitRegistry`.
4. Every beat has a stable `<SCENE_ID>_B###` identifier.
5. Trigger IDs and completion flags are explicit scene metadata.
6. Presentation/staging information travels as cue metadata separate from spoken text.
7. The accepted `DialogueRunner` remains generic and gains a Resource adapter rather than becoming scene-specific.
8. No player dialogue-choice field exists; known choice/response/branch keys are rejected by validation.
9. Technical proof Resources live under `game/content/dialogue/proof/` and cannot be treated as canon.
10. The accepted 7B.5 gameplay/persistence architecture remains a regression baseline where compatible with current canon.

## Production interfaces proven by 7B.6

- `game/dialogue/dialogue_scene_definition.gd`
- `game/dialogue/dialogue_portrait_registry.gd`
- `DialogueRunner.start_scene(scene_definition, registry)`
- `DialogueRunner.scene_finished(scene_id)`
- `DialogueRunner.beat_presented(scene_id, beat_id, cues)`

The beat signal allows later camera/staging/movement systems to consume authored cues without putting those systems inside the text parser.

## Non-canon validation fixture

`PROOF_SCHEMA` exists only to prove the production interface. Its dialogue, portrait assets and cue values are disposable and are not S001, Character-Life content or any other canon scene.

## Accepted validation

CI proved:

- the Resource schema and registry load;
- valid stable IDs adapt into existing runner beats;
- silent reactions survive adaptation;
- portrait IDs resolve through registry indirection;
- forbidden player-choice keys are rejected;
- duplicate beat IDs and unknown expressions are rejected;
- a valid Resource runs through the accepted `DialogueRunner` UI lifecycle from start through completion;
- every existing exploration/dialogue/combat/Card/Prime/save regression of that checkpoint remained green;
- Android debug APK export remained green.

No separate phone acceptance was required because 7B.6 did not change touch controls, layout, rendering, persistence behavior or platform lifecycle. Android CI remained a packaging regression check.

## Historical authority promotion

At the time of acceptance, the handoff was promoted into Clean Active Master v1.35, Technical Annex v1.35, Dialogue Development Annex v1.2, and Audit47. Those checkpoints are now recovery history beneath later complete-master authority.

## What happened after 7B.6

Step 7C is **no longer on hold**.

Production dialogue has since used the 7B.6 contract through the completed early-game block:

- Chapter 0 — S001–S006 + C01/C02: implemented/validated/merged.
- Chapter 1 — S007–S011 + C03–C05: exact source-parity + continuity validated/merged.
- Chapter 2 — S012–S016 + C06/C07: exact source-parity + continuity validated/merged.
- Chapter 3 — S017–S021 + H01–H04: exact source-parity + continuity/Cresthaven validation passed and merged.

There is no remaining Chapter 0–3 dialogue-Resource conversion backlog. **Chapter 4 — The Seventh Reaction** is the next exact scene-authoring frontier.

## Current authority boundary

7B.6 controls the accepted **technical dialogue interface**, not current story facts, Card counts, Prime names/mechanics, geography, chapter completion state, or later content decisions. If an old proof fixture or phase statement conflicts with v1.64/Audit79, the current master wins.
