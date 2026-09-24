# Diyse — Field Traversal & Dialogue Presentation Lock

**Status:** CURRENT EXPLICIT USER LOCK  
**Domain:** exploration presentation / dialogue presentation / scene staging  
**Purpose:** keep dialogue authoring aligned with the established gameplay presentation.

## Hard traversal rule

During ordinary route/dungeon/wilderness traversal:

> **Cyanis is the only party character represented on the exploration field.**

The rest of the traveling/combat party is present in story and gameplay state, but they do **not** trail behind Cyanis as visible field models during normal traversal.

This remains true when another character is guiding the party. A Torren-led route means the route is being directed in story and at authored stop scenes; it does **not** create dialogue while Cyanis is moving or require Torren to be rendered walking beside or ahead of Cyanis during normal exploration.

Do not author ordinary traversal staging such as:
- Torren walking ahead on-screen;
- Maevra or Ilyra visibly following Cyanis;
- party members repositioning around route obstacles during free traversal;
- a visible follower formation.

## Town / camp / Cresthaven exception

Towns, camps, and **Cresthaven** are not governed by the Cyanis-only traversal presentation in the same way as ordinary routes and dungeons.

> **Party members and relevant NPCs may be physically present as field models in towns, camps, and Cresthaven.**

They may occupy sensible standing/resting/work/social positions in those spaces and be available for authored or optional interaction as current story authority allows.

This does **not** mean the whole party must always be visible at once. Placement should follow the location, current story state, and scene needs.

Cresthaven is explicitly included in this hub-style presentation rule.

## Scene-trigger exception

When an authored scene triggers and ordinary traversal stops:

> **Other present characters may spawn/use their field models for the scene.**

This is normal and allowed.

A triggered scene may therefore show Cyanis, Ilyra, Torren, Maevra, NPCs, or other present characters together when that helps the scene read spatially.

The important distinction is:
- **ordinary route/dungeon/wilderness traversal:** Cyanis only;
- **towns / camps / Cresthaven:** relevant party members and NPCs may already be present as field models;
- **authored triggered scene:** relevant participants may appear as field models;
- **battle:** battle presentation owns the combat models.

Scene-trigger and hub-area models are not permission for constant choreography. They may simply stand in sensible positions while portraits and the dialogue box carry most of the acting.

## Dialogue presentation rule

The default authored conversation presentation remains intentionally simple:

> **illustrated character portrait(s) + dialogue box over the existing field/background, with field models available when the location or scene calls for them.**

Portraits carry speaker identity, expression, and most conversational acting.

Do not assume that every line needs body performance, prop interaction, or bespoke animation.

Avoid scripting tiny physical actions unless the scene genuinely needs them, including:
- using a weapon to move foliage;
- crouching to inspect a minor clue;
- adjusting straps or equipment for flavor;
- repeated pointing or turning merely to stage the dialogue;
- incidental prop business;
- repeated hand/head/posture animation that portraits already communicate.

A triggered scene or hub conversation can have the characters physically present without making them perform a miniature animation sequence.

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
- party/NPC presence in towns, camps, and Cresthaven;
- field models of relevant characters once an authored scene triggers;
- combat and boss presentation;
- required interaction with a major story object;
- an explicitly authored major reveal or state change;
- another scene where story/implementation authority specifically needs physical action.

Even in a triggered scene, use the simplest blocking that communicates the moment. Often that means the relevant characters appear, hold sensible positions, and portraits/dialogue do the rest.

## Dialogue timing boundary

> **There is no dialogue during ordinary player-controlled traversal and no dialogue during active combat.**

If a route needs conversation:
1. reach an authored trigger or natural stopping point;
2. pause/lock player movement;
3. run the dialogue scene;
4. return cleanly to exploration.

If a battle needs character dialogue, place it immediately before combat begins or after combat has fully ended. Active combat itself remains dialogue-free.

Town/camp/Cresthaven conversations may begin with the relevant character already physically present in the location.


## Authoring consequence

Dialogue manuscripts should primarily author:
- spoken lines;
- required story triggers;
- required major visual facts;
- simple scene blocking where actually needed;
- gameplay handoff points.

They should **not** become micro-animation scripts.

When in doubt:

> **Route traversal: Cyanis only. Town/camp/Cresthaven: relevant characters may be present. Triggered scene: bring in whoever the scene needs. Let portraits and dialogue carry most of the performance.**
