# Step 7B.6 — Production Handoff Lock

**Status:** IMPLEMENTED; pending CI acceptance on this branch  
**Parent authority:** v1.34 / Audit46  
**Starting `main` commit:** `ae3bcf120cfb6d956f5159519025734f1eb26912`  
**Step 7C:** ON HOLD until explicit user authorization

## Purpose

Step 7B.6 closes the final interface gap between completed dialogue craft and the proven Godot implementation. It does not write any canon scene. It defines the format in which Step 7C scenes can later be authored and consumed without putting story text into engine code.

## Locked handoff decisions

1. Production dialogue is stored as `DiyseDialogueSceneDefinition` Resources.
2. Scene data uses stable semantic IDs instead of portrait asset paths.
3. Portrait assets are resolved through `DiyseDialoguePortraitRegistry`.
4. Every beat has a stable `<SCENE_ID>_B###` identifier.
5. Trigger IDs and completion flags are explicit scene metadata.
6. Presentation/staging information travels as cue metadata separate from spoken text.
7. The accepted `DialogueRunner` remains generic and gains a Resource adapter rather than becoming scene-specific.
8. No player dialogue-choice field exists; known choice/response/branch keys are rejected by validation.
9. Technical proof Resources live under `game/content/dialogue/proof/` and cannot be treated as canon.
10. The accepted 7B.5 gameplay/persistence architecture remains the regression baseline.

## New production interfaces

- `game/dialogue/dialogue_scene_definition.gd`
- `game/dialogue/dialogue_portrait_registry.gd`
- `DialogueRunner.start_scene(scene_definition, registry)`
- `DialogueRunner.scene_finished(scene_id)`
- `DialogueRunner.beat_presented(scene_id, beat_id, cues)`

The beat signal allows later camera/staging/movement systems to consume authored cues without putting those systems inside the text parser.

## Non-canon validation fixture

`PROOF_SCHEMA` exists only to prove the production interface. Its dialogue, portrait assets and cue values are disposable and are not S001, Character-Life content or any other canon scene.

## Acceptance criteria

7B.6 is complete when CI proves:

- the Resource schema and registry load;
- valid stable IDs adapt into existing runner beats;
- silent reactions survive adaptation;
- portrait IDs resolve through registry indirection;
- forbidden player-choice keys are rejected;
- duplicate beat IDs and unknown expressions are rejected;
- a valid Resource actually runs through the accepted `DialogueRunner` UI lifecycle;
- every existing exploration/dialogue/combat/Card/Prime/save regression remains green;
- Android export remains green.

No separate phone acceptance is required because 7B.6 does not change touch controls, layout, rendering, persistence behavior or platform lifecycle. Android CI is retained as a packaging regression check.

## Production boundary after acceptance

After 7B.6 passes, no technical or authoring-format prerequisite remains before Step 7C. Full scene writing nevertheless remains procedurally locked until the user explicitly authorizes Step 7C.
