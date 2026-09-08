# Diyse — Dialogue UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections/current domain migrations.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## Scene-construction integration
Dialogue UI is part of the current Dialogue Engine scene stack, not an isolated text-box system.

See:
- `../03_DIALOGUE/AGENT_SYSTEM/SCENE_CONSTRUCTION_STACK.md`
- `IMPLEMENTATION_NOTES/AREA_TRAVERSAL_AUTHORING_INTERFACE.md`
- `../14_ART_AND_VISUALS/ART_VISUAL_MASTER.md`
- `../14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`

The runtime must support scenes in which geography, B00 rigged field models, portraits, camera, lighting, sound, props, background activity, silence, and spoken text all share the performance load.

## Proven architecture
Production dialogue uses:
- `DiyseDialogueSceneDefinition` Resources;
- stable semantic character/expression IDs;
- `DiyseDialoguePortraitRegistry`;
- generic `DialogueRunner`;
- manual advance;
- silent beats;
- separate cue metadata.

## No choices
Hard rule:
> **Diyse has no player dialogue choices.**

Do not implement:
- response wheel;
- tone choice;
- affinity answer;
- persuasion menu;
- romance response;
- morality response.

## Portrait presentation
Current presentation rule:
- high-resolution portrait assets displayed at a restrained dialogue scale;
- generally **~25–35% of screen height**, with **~30%** as the normal starting target;
- dialogue box generally lower 20–25%.

At the 1920×1080 reference viewport, that corresponds approximately to:
- 25% → **270 px** visible portrait height;
- 30% → **324 px** visible portrait height;
- 35% → **378 px** visible portrait height.

Portraits are a major close-performance layer, but they are **not the entire scene**. Current B00 rigged 3D field characters remain visible/meaningful where scene composition calls for physical blocking, facing, movement, gesture, or spatial relationships.

## Environmental-read rule
Important spatial discoveries receive a clean visual read before dialogue UI dominates the frame.

Examples:
- a changed route;
- a damaged bridge;
- a distant landmark;
- evacuation flow;
- a machine visibly misbehaving;
- a new enemy-controlled space;
- a large reveal or state change.

The scene may briefly withhold portraits/text, use a silent beat, or reframe the camera before the first line.

Do not use dialogue to describe in full what the player has just been clearly shown.

## Required beat support
UI/runtime must support:
- speaker label;
- body text;
- left portrait;
- right portrait;
- active-side emphasis;
- portrait change without spoken text;
- true silent beat;
- manual continue;
- movement/input lock;
- clean return to exploration;
- dialogue beat with no portrait change;
- camera/staging cue independent of text;
- field-model movement/facing cue independent of text;
- sound/music cue independent of text;
- environment/state cue independent of text.

## Scene modes
The UI/runtime should support the Dialogue Engine's different scene modes without forcing them into one presentation:

### Full authored stop scene
- movement may lock;
- portraits may carry close acting;
- field models and camera carry spatial relationships;
- silence and staging beats are first-class.

### Walking/traversal dialogue
- movement may remain available;
- portraits/text should not unnecessarily obscure route readability;
- encounter-safe traversal rules come from the area/traversal interface;
- scene ends cleanly back into ordinary exploration.

### Post-battle reaction
- optimized for short exchanges;
- should not create excessive post-combat friction.

### Story-bearing-cell interaction / optional NPC dialogue
- may be lightweight;
- should preserve the environment as part of the scene.

### Character-Life / hub / camp
- may use ordinary props/tasks and restrained camera instead of expensive bespoke animation.

### Story-combat pause
- only where current story/battle authority explicitly allows it;
- presentation never creates illegal actions.

## Economical HD-2D UI principle
The dialogue presentation should help Diyse achieve cinematic performance without demanding fully bespoke animation for every scene.

High-value economical tools include:
- portrait-expression swaps;
- silent beats;
- B00 field-model facing/pose/short gestures;
- restrained camera reframing;
- existing prop interactions;
- lighting shifts;
- sound/music changes;
- background movement;
- environment state swaps.

The goal is not a cheap-looking presentation. It is to spend production complexity where the player will actually feel it.

## Stable IDs
Production scene data references:
> character ID + expression ID

not final image file paths.

Scene/cue data should likewise prefer stable semantic IDs for staging functions over brittle asset paths where practical.

## Current ID correction
Global current chapter IDs extend through:
> `chapter_13`

Current mandatory story sequence extends through:
> **S073**

Older schema documents capped at chapter_12/S062 are stale bookkeeping.

## OPEN PRODUCTION UX
- text speed;
- backlog/history;
- auto mode;
- skip/fast-forward;
- nameplate treatment;
- exact text-box skin;
- exact active/inactive portrait dim amount;
- exact portrait hide/show behavior during environmental-read beats;
- exact walking-dialogue presentation at narrow traversal widths.
