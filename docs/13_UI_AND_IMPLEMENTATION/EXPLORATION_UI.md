# Diyse — Exploration UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections/current domain migrations.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## CANON REQUIREMENT
Exploration UI should remain restrained so the HD-2D field remains readable.

It must be capable of presenting, when relevant:
- interaction prompt;
- current location/area transition;
- quest/objective update;
- travel availability;
- optional Hunt access;
- save/return warnings;
- field party/menu access.

## Area/traversal authoring integration
Dialogue and exploration share one playable pacing layer.

See:
- `IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`
- `../03_DIALOGUE/AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`

Normal exploration remains gameplay. Dialogue may occur during movement where pressure permits, but Diyse should not default into continuous walk-and-talk presentation.

The field UI/runtime should be able to transition cleanly among:
- ordinary exploration;
- short walking dialogue;
- interaction dialogue;
- authored stop scene;
- post-battle reaction;
- recovery/story-bearing cell;
- return to ordinary exploration.

## Random encounters
Random encounters remain normal hostile-exploration grammar in approved areas.

The field UI must not show a mandatory visible random-encounter meter unless separately approved.

Current runtime internally tracks encounter pressure, but that does **not** establish a player-facing gauge.

### Dialogue-safe traversal
For mandatory authored walking dialogue:
- encounter triggering may be temporarily suppressed for the authored exchange plus a short buffer;
- local encounter pressure is preserved rather than reset/discarded;
- the suppression is not a permanent reduction in the area's encounter identity;
- player-facing UI does not need to announce the suppression unless later explicitly approved.

Long dialogue belongs in a credible safe context or explicitly protected window. A high-pressure pursuit corridor should not be made mechanically toothless merely to fit a conversation.

## Interaction
A contextual interaction prompt may cover:
- Talk;
- Examine;
- Open;
- Use;
- service access.

The exact player-facing wording may be authored per interaction.

Optional NPC/story-bearing-cell interaction should feel attached to the place rather than like portable dialogue content.

## Environmental readability
Exploration UI and dialogue UI should leave major spatial information visible long enough to read.

Examples include:
- landmarks;
- route changes;
- hazards;
- interactable machinery;
- evacuation or civilian flow;
- state-swapped environments;
- major approach reveals.

Do not stack objective text, interaction prompts, dialogue portraits, and other overlays over the same visual reveal if sequencing them would preserve clarity.

## Chapter 0
Chapter 0 is authored/tutorial content, not normal random-encounter UI.

## OPEN PRODUCTION UX
- minimap vs no minimap;
- compass;
- permanent objective tracker;
- interaction icon language;
- encounter-transition overlay;
- exact field HUD density;
- exact walking-dialogue HUD suppression rules;
- exact priority rules when interaction prompts and dialogue-safe traversal overlap.
