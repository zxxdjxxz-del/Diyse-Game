# Diyse — Field Traversal & Dialogue Presentation Lock

**Status:** CURRENT EXPLICIT USER LOCK  
**Domain:** exploration presentation / dialogue presentation / scene staging  
**Purpose:** keep dialogue authoring aligned with the already-established gameplay presentation instead of inventing a more fully staged 3D party performance.

## Hard traversal rule

During ordinary field traversal:

> **Cyanis is the only party character represented on the exploration field.**

The rest of the traveling/combat party is present in story and gameplay state, but they do **not** trail behind Cyanis as visible field models during normal traversal.

This remains true when another character is guiding the party. A Torren-led route means Torren is directing the group in story/dialogue; it does **not** require Torren to be rendered walking beside or ahead of Cyanis on the field.

Do not author ordinary traversal staging such as:
- Torren walking ahead on-screen;
- Maevra or Ilyra visibly following Cyanis;
- party members repositioning around route obstacles;
- companion field-model reactions during travel;
- formation blocking for the traveling party.

## Dialogue presentation rule

The default authored conversation presentation is intentionally simple:

> **illustrated character portrait(s) + dialogue box over the existing field/background.**

Portraits carry speaker identity, expression and most conversational acting.

Do not assume that every speaker needs a visible field model, body performance, prop interaction, or bespoke animation in order for a dialogue exchange to work.

Ordinary scene directions should therefore avoid scripting tiny physical actions such as:
- using a weapon to move foliage;
- crouching to inspect a minor clue;
- adjusting straps or equipment for flavor;
- stepping to a particular side of the road;
- pointing at ordinary terrain;
- looking back and forth between speakers merely to stage the conversation;
- repeated hand, head, posture or prop business that the portrait/dialogue presentation does not need.

If the line reads clearly through the portrait and dialogue box, that is enough.

## Environment rule

Diyse's field presentation is **not a fully modeled 3D world**.

The environment uses the established HD-2D / 2.5D grammar:
- authored layered backgrounds and environment art;
- selective depth geometry where gameplay or composition requires it;
- restrained parallax/depth treatment;
- fixed/authored presentation rather than a freely explorable fully 3D cinematic stage.

Do not write dialogue scenes as though every background element can be physically manipulated, walked around in bespoke blocking, or inspected through fully simulated character animation.

## What may still receive physical presentation

Physical field/battle action is reserved for things the story or gameplay genuinely requires, such as:
- Cyanis's normal player traversal;
- combat and boss presentation;
- required interaction with a major story object;
- an explicitly authored major reveal or state change;
- a rare scene where current story/implementation authority specifically requires additional visible characters or physical action.

Even in those cases, use the simplest presentation that communicates the event. A state swap, short existing animation, fade, sound cue, or portrait-supported interaction may be preferable to bespoke choreography.

## Walking dialogue clarification

`WALKING_DIALOGUE_LOCK.md` governs **when dialogue may occur while the player is traversing**. It does not mean the guide must be visibly walking on the field.

For example, Torren may guide Cyanis through a route via short portrait/dialogue-box instructions while Cyanis remains the sole visible traversal character.

## Authoring consequence

Dialogue manuscripts should primarily author:
- spoken lines;
- required story triggers;
- required major visual facts;
- gameplay handoff points.

They should **not** become animation scripts or micro-blocking documents for ordinary conversations.

When in doubt:

> **Keep Cyanis on the field, let the portraits talk, and do not invent a physical action unless the story actually needs it.**
