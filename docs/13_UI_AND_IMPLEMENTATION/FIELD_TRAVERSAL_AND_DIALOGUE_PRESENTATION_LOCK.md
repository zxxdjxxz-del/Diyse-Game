# Diyse — Field Traversal & Dialogue Presentation Lock

**Status:** CURRENT EXPLICIT USER LOCK  
**Domain:** exploration presentation / dialogue presentation / scene staging  
**Purpose:** keep dialogue authoring aligned with the established gameplay presentation.

## Hard traversal rule

During ordinary field traversal:

> **Cyanis is the only party character represented on the exploration field.**

The rest of the traveling/combat party is present in story and gameplay state, but they do **not** trail behind Cyanis as visible field models during normal traversal.

This remains true when another character is guiding the party. A Torren-led route means Torren is directing the group in story/dialogue; it does **not** require Torren to be rendered walking beside or ahead of Cyanis during normal exploration.

Do not author ordinary traversal staging such as:
- Torren walking ahead on-screen;
- Maevra or Ilyra visibly following Cyanis;
- party members repositioning around route obstacles during free traversal;
- a visible follower formation.

## Scene-trigger exception

When an authored scene triggers and ordinary traversal stops:

> **Other present characters may spawn/use their field models for the scene.**

This is normal and allowed.

A triggered scene may therefore show Cyanis, Ilyra, Torren, Maevra, NPCs, or other present characters together when that helps the scene read spatially.

The important distinction is:
- **ordinary traversal:** Cyanis only;
- **authored triggered scene:** relevant participants may appear as field models;
- **battle:** battle presentation owns the combat models.

Scene-trigger models are not permission for constant choreography. They may simply stand in sensible positions while portraits and the dialogue box carry most of the acting.

## Dialogue presentation rule

The default authored conversation presentation remains intentionally simple:

> **illustrated character portrait(s) + dialogue box over the existing field/background, with scene field models available when a trigger calls for them.**

Portraits carry speaker identity, expression, and most conversational acting.

Do not assume that every line needs body performance, prop interaction, or bespoke animation.

Avoid scripting tiny physical actions unless the scene genuinely needs them, including:
- using a weapon to move foliage;
- crouching to inspect a minor clue;
- adjusting straps or equipment for flavor;
- repeated pointing or turning merely to stage the dialogue;
- incidental prop business;
- repeated hand/head/posture animation that portraits already communicate.

A triggered scene can have the characters physically present without making them perform a miniature animation sequence.

## Environment rule

Diyse's field presentation is **not a fully modeled 3D world**.

The environment uses the established HD-2D / 2.5D grammar:
- authored layered backgrounds and environment art;
- selective depth geometry where gameplay or composition requires it;
- restrained parallax/depth treatment;
- fixed/authored presentation rather than a freely explorable fully 3D cinematic stage.

Do not write dialogue scenes as though every background element can be physically manipulated or inspected through bespoke animation.

## What may receive physical presentation

Physical field presentation is appropriate for:
- Cyanis's normal player traversal;
- field models of relevant characters once an authored scene triggers;
- combat and boss presentation;
- required interaction with a major story object;
- an explicitly authored major reveal or state change;
- another scene where story/implementation authority specifically needs physical action.

Even in a triggered scene, use the simplest blocking that communicates the moment. Often that means the relevant characters appear, hold sensible positions, and portraits/dialogue do the rest.

## Walking dialogue clarification

`WALKING_DIALOGUE_LOCK.md` governs **when dialogue may occur while the player is traversing**. It does not mean the guide must be visibly walking on the field.

For example, Torren may guide Cyanis through a route via portrait/dialogue-box instructions while Cyanis remains the sole visible traversal character. If the game stops for an authored scene, Torren's field model may then appear normally for that scene.

## Authoring consequence

Dialogue manuscripts should primarily author:
- spoken lines;
- required story triggers;
- required major visual facts;
- simple scene blocking where actually needed;
- gameplay handoff points.

They should **not** become micro-animation scripts.

When in doubt:

> **Traversal: Cyanis only. Triggered scene: bring in whoever the scene needs. Let portraits and dialogue carry most of the performance.**
