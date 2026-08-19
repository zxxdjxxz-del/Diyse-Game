# DIYSE — Whole-Game Scene Authoring Standard

**Status:** ACTIVE / REQUIRED  
**Effective:** August 19, 2026  
**Authority:** v1.73 / Audit88  
**Scope:** All new story, Character-Life, hub, quest, Hunt-linked, battle-linked, interlude and aftermath scene authoring from Chapter 5 forward, plus any later explicitly reopened scene.

This standard does **not** reopen Chapters 0–4. Their story/dialogue/gameplay authority is closed, and their HD-2D presentation/implementation conversion is separately locked under Audit88.

## Core rule

Before writing each scene, check it against current canon and the characters actually participating. Draft/review at normal useful scene size. Do not split scenes into tiny blocks just to perform checks.

Diyse should feel like an **HD-2D JRPG with exploration and combat**, not a chain of conversations.

## Mandatory pre-scene check

### 1. Story / continuity

Verify:

- what the scene must accomplish;
- what immediately precedes and follows it;
- location/time/geography;
- roster and guest/permanent state;
- equipment/Card/Prime state;
- chapter progression;
- already-locked outcomes.

Do not reopen closed canon accidentally.

### 2. Knowledge firewall

Check what each participant knows **at that exact point**.

Do not leak later truths about Ancient Diyse, the Entity, the Underground Crest Network, Story Primes, future antagonists, later relationships or any other unrevealed material. Characters may infer from evidence they possess but must not speak from player/master-canon knowledge they have not earned.

### 3. Personality / voice

Re-check current voice anchors for every meaningful participant.

Characters should sound like themselves, not variants of one generic witty JRPG voice. Adults may swear, joke, interrupt, misunderstand, gossip, get petty, be tired, change subjects, say little or leave thoughts unfinished when natural. Do not make someone speak simply because they are present.

Real danger changes behavior: humor can drop; competence and established stress responses take over.

### 4. Relationship state

Check the exact current relationship stage for interacting pairs.

Do not jump ahead in familiarity, intimacy, nicknames, trust, hostility, forgiveness or disclosure. Let progression emerge from accumulated behavior rather than explanatory speeches.

### 5. Adult dialogue + expressive HD-2D/JRPG performance

Dialogue should sound like adults talking rather than people announcing emotions to the audience.

Let performance carry subtext through:

- portrait swaps;
- sudden stares;
- head turns;
- recoils;
- deadpan holds;
- side-eye;
- small ~80 px field-sprite shifts/turns;
- camera timing;
- silence.

Comedy should use timing/reaction, not only punchlines.

### 6. Affordable HD-2D production

Every authored scene must be practical under Audit87/Audit88.

Prefer:

- reusable stand/sit/walk/interaction/casting poses;
- portrait/expression swaps;
- small sprite shifts/turns;
- authored camera framing, pans, inserts and holds;
- ordinary reusable props such as maps, papers, cups, food, tools, Cards, bandages, reports, chairs, tables, weapons and field gear;
- lighting/VFX changes;
- authored environment before/after states;
- layered background workers/crowds rather than crowd AI;
- prepared gate, water-level, machinery, route, damage and room states rather than simulation;
- small reusable battle-background families derived from field geography.

Avoid expensive bespoke animation, physics destruction, fluid simulation, crowd simulation, free-camera choreography or one-use cinematic machinery when established HD-2D grammar can communicate the same meaning.

### 7. Gameplay breathing room

Do not stack mandatory dialogue continuously when fiction supports play between scenes.

Use the established rhythm where appropriate:

**dialogue/story beat → traversal/exploration → combat-capable space → environmental discovery/interaction → next authored dialogue beat**

The player should regularly regain control and have room to move through the world.

### 8. Random battles

Traditional random encounters remain Diyse's ordinary hostile-exploration layer where fiction supports them.

- Build real traversal space between dialogue beats in hostile/unsecured locations.
- Do not pre-author a fixed or approximate number of random battles for an area.
- Encounter quantity emerges from implemented geometry, traversable route length, optional branches, exploration/backtracking, safe pockets, encounter-rate implementation and player route choice.
- Scene scripts define where encounters are enabled/suppressed and how traversal is structured, not a promised count.
- Use chapter-appropriate enemy variety.
- Safe settlements, secured hubs, immediate story pockets and delicate NPC sequences may suppress random encounters.
- Do not replace the random-encounter layer with visible roaming enemies unless a future explicit canon change says so.

Chapter 0's seven authored tutorial encounters remain a historical explicit exception, not a template for later hostile traversal.

### 9. Authored encounters / bosses / Hunts

When a scene touches a mandatory battle, authority encounter, boss, Hunt branch or optional-major route:

- check the controlling encounter study and exact chapter lock;
- preserve nonlethal/lethal intent;
- preserve HP-bar/form architecture;
- preserve first-pass denied branches and post-climax return grammar;
- do not invent extra mandatory fights because a scene feels quiet;
- keep random battles distinct from authored mandatory encounters;
- classify boss thresholds correctly as same-body escalation, genuine new form or Prime-scale entity.

### 10. HD-2D presentation tier

Assign presentation cost deliberately using:

- **C0 — Conversational**
- **C1 — Staged**
- **C2 — Dramatic**
- **C3 — Spectacle**
- **V1 — Common**
- **V2 — Face/class identity**
- **V3 — Named signature**
- **V4 — Prime/boss spectacle**

Most scenes should stay C0–C1. Reserve C2/C3 and V3/V4 for moments that materially need them. Preserve escalation room for Chapters 11–12.

### 11. Scene handoff

Before calling a scene ready for review, check:

- player state on exit;
- whether control returns to exploration, hostile traversal, safe hub, mandatory scene or optional window;
- next trigger and character availability;
- whether enough gameplay space exists between major conversations.

## Review / acceptance workflow

- Draft/review scene by scene at useful size.
- User corrections control immediately.
- Once accepted, preserve exact accepted wording/staging in the chapter source and record acceptance.
- Later corrections supersede earlier accepted material explicitly rather than silently erasing history.
- Complete mandatory scenes **and** associated optional Character-Life/hub scenes before calling a chapter finished.
- After acceptance, run a whole-chapter pass for continuity, voice, relationships, repetition, pacing, random-battle spacing, enemy variety, Hunts/optional content, knowledge firewall, HD-2D affordability and chapter handoff before production Resource conversion.

## Completed Chapters 0–4

Do not re-author them as missing material.

Their approved HD-2D conversion is controlled by:

`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Implementation may simplify old dimensional staging into the approved HD-2D grammar but must not rewrite approved story/dialogue/gameplay.

## Standing intent

This is the default authoring method for the rest of Diyse. The next inherited scene-authoring/production frontier is **Chapter 5 — The Mountain Engine**, unless the user explicitly chooses another task.