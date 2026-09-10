# Diyse — Exploration UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections/current domain migrations.  
**Implementation rule:** current domain canon and newer explicit presentation locks beat older proof code/docs.

## Controlling field-presentation lock

See:
> `FIELD_TRAVERSAL_AND_DIALOGUE_PRESENTATION_LOCK.md`

During ordinary exploration:

> **Cyanis is the only party character visible on the field.**

The rest of the party remains present in story/combat state but is not rendered as visible followers during traversal.

## Canon requirement

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

Normal exploration remains gameplay. Dialogue does not convert ordinary traversal into a physically staged party scene.

The field UI/runtime should transition cleanly among:
- ordinary Cyanis-controlled exploration;
- short legal walking dialogue presented through portraits/text;
- interaction dialogue;
- authored stop dialogue;
- post-battle reaction;
- recovery/story-bearing cell;
- return to ordinary exploration.

A guide such as Torren may direct the group through dialogue while **Cyanis remains the sole visible traversal avatar**.

## Environment presentation

The exploration field follows the established HD-2D / 2.5D grammar rather than a fully modeled 3D-world assumption:
- authored layered backgrounds/environments;
- selective depth geometry only where traversal or composition needs it;
- restrained parallax/depth treatment;
- authored/fixed scene composition.

Do not design dialogue around routine physical manipulation of incidental background details.

## Random encounters

Random encounters remain normal hostile-exploration grammar in approved areas.

The field UI must not show a mandatory visible random-encounter meter unless separately approved.

For mandatory authored walking dialogue:
- encounter triggering may be temporarily suppressed for the exchange plus a short buffer;
- accumulated encounter pressure is preserved rather than reset/discarded;
- player-facing UI does not need to announce the suppression.

## Dialogue presentation during exploration

Dialogue uses the normal portrait + dialogue-box presentation.

Do not require companion field models to appear merely because they speak.
Do not script tiny physical companion actions to sell a line.

## Interaction

A contextual interaction prompt may cover:
- Talk;
- Examine;
- Open;
- Use;
- service access.

The exact player-facing wording may be authored per interaction.

## Environmental readability

Major spatial information should remain visible long enough to read before overlays dominate it.

This applies to genuinely important landmarks, hazards, interactables, major state changes, or story reveals—not to ordinary environmental dressing.

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
