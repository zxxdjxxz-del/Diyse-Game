# Diyse — Dialogue UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections/current domain migrations.  
**Implementation rule:** current domain canon and newer explicit presentation locks beat older proof code/docs.

## Controlling presentation lock

Current field/dialogue presentation authority:
> `FIELD_TRAVERSAL_AND_DIALOGUE_PRESENTATION_LOCK.md`

That lock controls over older wording that implied fully staged party field scenes.

## Core dialogue presentation

Diyse's normal authored conversation presentation is intentionally simple:

> **illustrated portrait(s) + dialogue box over the existing field/background.**

Production dialogue uses:
- `DiyseDialogueSceneDefinition` Resources;
- stable semantic character/expression IDs;
- `DiyseDialoguePortraitRegistry`;
- generic `DialogueRunner`;
- manual advance;
- silent beats;
- separate cue metadata where a genuinely required story event needs one.

## No choices

Hard rule:
> **Diyse has no player dialogue choices.**

Do not implement a response wheel, tone choice, affinity answer, persuasion menu, romance response, or morality response.

## Portrait presentation

Current portrait target:
- high-resolution illustrated portraits;
- generally **~25–35% of screen height**, with **~30%** as the normal starting target;
- dialogue box generally lower 20–25%.

At 1920×1080 this is approximately:
- 25% → **270 px** visible portrait height;
- 30% → **324 px** visible portrait height;
- 35% → **378 px** visible portrait height.

Portraits carry speaker identity, facial/emotional performance, and most ordinary conversational acting.

## Field-character rule

During ordinary traversal:

> **Cyanis is the only party character visible on the exploration field.**

Other party members remain present in story/combat state but are not rendered as a follower train.

A guide such as Torren may speak through the portrait/dialogue UI while directing Cyanis. The guide does not need to be visibly walking beside or ahead of him.

Do not author routine dialogue around companion field-model blocking, facing, stepping, pointing, weapon handling, posture business, or tiny prop interactions.

## Stop scenes

A normal stop scene may simply:
1. pause/lock movement when needed;
2. keep the existing field/background visible;
3. show the speaking portrait(s) and dialogue box;
4. return cleanly to gameplay.

Do not instantiate the whole party physically merely because several people speak.

Additional visible character models or physical choreography require a genuine story/gameplay reason and should be rare.

## Walking/traversal dialogue

Walking dialogue follows `../03_DIALOGUE/AGENT_SYSTEM/WALKING_DIALOGUE_LOCK.md`.

When legal, it does **not** change the single-field-character rule. Cyanis remains the visible traversal avatar while other speakers use portraits/dialogue text.

## Environmental-read rule

Important spatial discoveries may receive a clean visual read before the dialogue UI appears.

Keep this simple. The background is the already-authored HD-2D field, not a fully simulated 3D cinematic stage. Do not invent camera choreography, extra props, or physical party reactions merely to make a discovery feel cinematic.

## HD-2D environment relationship

The background follows the established layered HD-2D / 2.5D grammar:
- authored layered environment art;
- selective depth geometry only where gameplay/composition needs it;
- restrained parallax/depth treatment;
- fixed/authored presentation rather than a freely explorable fully modeled 3D world.

Dialogue authoring must respect that production model.

## Required runtime support

The UI/runtime should support:
- speaker label;
- body text;
- left/right portrait slots;
- active-side emphasis;
- portrait/expression change;
- true silent beat;
- manual continue;
- movement/input lock;
- clean return to exploration;
- short walking dialogue;
- short post-battle reaction;
- required story/event cues when separately justified.

It does **not** need bespoke field-model animation for ordinary dialogue.

## Economical presentation principle

The default economical solution is:

> **existing background + Cyanis field avatar when traversing + portraits + dialogue box.**

Do not treat lighting shifts, camera moves, background activity, prop interactions, field-model gestures, or environment state changes as a checklist. Use one only when the story/gameplay beat genuinely requires it.

## Stable IDs

Production scene data references:
> character ID + expression ID

not final image file paths.

## Current ID correction

Global current chapter IDs extend through:
> `chapter_13`

Current mandatory story sequence extends through:
> **S073**

## OPEN PRODUCTION UX
- text speed;
- backlog/history;
- auto mode;
- skip/fast-forward;
- nameplate treatment;
- exact text-box skin;
- exact active/inactive portrait dim amount;
- exact portrait hide/show behavior during major environmental-read beats;
- exact walking-dialogue HUD suppression rules.
