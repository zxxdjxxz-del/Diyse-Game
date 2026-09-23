# Diyse — Layout Blueprint 001
## Chapter 0 — Convoy Road / Wreck Field / Recovery Line / Field Triage Camp / Survivor Sweep

**Status:** PROVISIONAL BLOCKOUT BLUEPRINT / FIRST GODOT GRAYBOX CREATED  
**Owner stream:** `90_WORKING/AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`  
**Inventory source:** `90_WORKING/PLAYABLE_AREA_INVENTORY_WORKING.md`  
**Graybox scene:** `game/exploration/maps/chapter_00/chapter_00_graybox.tscn`

This blueprint converts Chapter 0's locked story/dialogue order into testable 3D exploration geometry. It is **not yet an L3 final topology**. Dimensions and camera values remain vertical-slice test constants until the graybox is actually played and approved.

---

# 1. Canon Route and Scene Order

Macro travel remains:

> **Convoy Road → Wreck Field → Evacuation / Recovery Line → Field Triage Camp → Brackenwall**

The line-complete P07 aftermath adds a bounded local recovery sweep after the camp confrontation. That sweep is a **Recovery-Line reuse spur**, not a new world-map destination:

> **Triage Camp → bounded survivor sweep south of the wagon line → Brackenwall handoff**

Mandatory scene/combat order:

### P01 — Opening combat
1. Black Host Raider + Black Host Crossbowman
2. Black Host Raider + Ruin Shieldbearer
3. 2 Convoy Rift Hounds

### P02 — Wreck Field
4. Black Host Crossbowman + Convoy Rift Hound
5. exactly one Convoy Rift Hound encounter threatening the survivor route;
- survivors, wreckage, evacuation routes and suspicious northern withdrawal must be readable.

### P03 — Evacuation Relay Decision
- no combat;
- wounded/civilians and the damaged recovery line must be spatially visible so Cyanis's refusal of the pursuit reads as professional judgment rather than exposition.

### P04 — Field Triage Camp
- Ilyra introduction;
- first incomplete Card flare;
- Cyanis + Ilyra become the active combat pair.

### P05 — Concealed Ruin Vanguard
- Ruin Vanguard Pursuer only;
- concealed Seyrik;
- protected disengagement;
- no Card-derived protection;
- real noncombat reset follows.

### P06 — Combined final Broken Convoy boss
Current exact story/dialogue staging establishes:
- Riftmaw + Convoy War-Sorcerer advance through the defended camp edge / east-cut approach;
- the second incomplete Card flare is active at battle opening;
- Cyanis + Ilyra receive the current three-round Defense/Spirit protection;
- the recovery casing breaks during the fight;
- there is no injured Iron Cohort Soldier;
- both Riftmaw and the War-Sorcerer are defeated in this same encounter.

Therefore:
> **P06 belongs to the Field Triage Camp perimeter, not the earlier Recovery-Line approach.**

### P07 — Aftermath and bounded survivor sweep
Current exact dialogue staging establishes:
- P07 begins in the still-active camp after P06;
- a wounded escort reports tracks south of the wagon line;
- the officer authorizes **one sweep** with **no chase beyond the wreck markers**;
- Cyanis and Ilyra leave the treatment lane for that bounded survivor sweep;
- Brackenwall follows afterward.

Implementation/presentation interpretation:
- P07 dialogue opens in the camp state;
- the player-controlled sweep may use/re-enter the `CH00_RECOVERY_LINE` environment family;
- it must not become a second dungeon, combat route or open-ended pursuit.

---

# 2. Technical Blockout Baseline

Current proof-runtime anchors:
- exploration uses `CharacterBody3D`;
- player collision capsule height = **1.8 units**;
- proof movement speed = **5.0 units/sec**;
- design viewport = **1920×1080**;
- proof camera ≈ **(0, +5.5, +7.5)**, **−25°**, **60° FOV**.

For Blueprint 001 only:
> **1 Godot world unit ≈ 1 meter**

This is a graybox convention, not an in-world measurement canon.

First-pass widths:
- convoy road: **8–10 m**;
- ordinary connector: **5–6 m**;
- intentional narrow passage: **3.5–4 m minimum**;
- story gathering pocket: **12–18 m**;
- fixed encounter-transition staging pocket: **20–28 m**.

Ordinary/fixed combat resolves in the dedicated combat presentation, so the field needs readable pre-battle staging and transition space rather than full battle-formation geometry.

---

# 3. Graybox Chunks

| ID | Area | Approx. envelope | Critical-path target | Primary role |
|---|---|---:|---:|---|
| CH00_F01 | Convoy Road | 220 × 100 m | ~260 m | movement/tutorial combat cadence |
| CH00_F02 | Wreck Field | 180 × 140 m | ~180 m | aftermath reading / two solo fights |
| CH00_F03 | Recovery Line | 170 × 85 m | ~170 m | evacuation logic / command decision |
| CH00_F04 | Field Triage Camp | 115 × 95 m | ~110 m | Ilyra / P05 Seyrik / P06 combined final boss / aftermath |
| CH00_F03R | Survivor Recovery Sweep | ~80 × 70 m local spur | ~80–100 m | P07 no-combat bounded sweep / Brackenwall handoff |

Total first-pass critical traversal is roughly **800 m** before Brackenwall, excluding investigation wandering. At 5 m/s this is under three minutes of uninterrupted running; authored dialogue, fixed battles, investigation, staging and first-time navigation provide the actual pacing.

Coordinate convention:
- +X east;
- −X west;
- −Z chapter-forward/northward screen progression convention for this blockout;
- Y elevation.

Coordinates are test targets, not final centimeter locks.

---

## Chapter-0 combat-spacing sockets

Exact distances/timing remain graybox-playtest variables. The following separation is structural:

### Convoy Road / P01
- Combat 1 pocket;
- **route-clearing / survivor-movement socket**;
- Combat 2 pocket;
- **wreckage/readability movement socket**;
- Combat 3 pocket;
- **late-road breathing / seam approach**;
- enter Wreck Field.

No P01 fight is an immediate reinforcement wave from the prior fight.

Current graybox intent:
- Combat 1 around `(-8,+55)`;
- first breathing socket around `(+18,+20)`;
- Combat 2 around `(+10,-15)`;
- second breathing socket around `(-4,-33)`;
- Combat 3 around `(-20,-48)`;
- late-road breathing / Wreck Field seam approach around `(-5,-82)`.

### Wreck Field / P02
Before Combat 4:
- survivor/wounded lobe;
- short rescue route;
- trapped-survivor interaction;
- stone-line route read.

Then:
- Combat 4 — Crossbowman + Hound;
- **survivor-movement / lower-stone-line socket**;
- Combat 5 — lone Hound;
- north-withdrawal sightline / officer exchange;
- no more Cyanis-solo combat.

Current graybox intent:
- Combat 4 around `(+5,+18)`;
- lower-stone-line breathing socket around `(-8,+2)`;
- Combat 5 around `(+5,-10)`.

### Recovery Line / P03
Entire sequence is combat-free.

### Triage Camp / P04–P06
- P04 has no standalone battle;
- short perimeter-control interval before P05;
- P05 occurs on the camp edge;
- a genuine noncombat reset occurs after P05;
- P06 cannot auto-chain from the P05 result screen;
- P06 remains the final combat.

These are presentation/spacing sockets, not final traversal-time locks.

---

# 4. CH00_F01 — Convoy Road

Design: controlled S-curve / switchback through rugged Westways terrain. Terrain shelves and bends prevent all authored encounters from being visible simultaneously while keeping the route unmistakable.

Approximate nodes:

| Node | Local X/Z | Function |
|---|---|---|
| Start | (0, +112) | opening spawn |
| A | (0, +95) | convoy competence framing |
| B | (−8, +55) | P01 combat 1 — Raider + Crossbowman |
| C | (+18, +20) | convoy obstacle / route read |
| D | (+10, −15) | P01 combat 2 — Raider + Shieldbearer |
| E | (−20, −48) | P01 combat 3 — 2 Convoy Rift Hounds |
| F | (−5, −82) | late-road breathing / seam approach |
| Exit | (0, −105) | Wreck Field seam |

Only shallow roadside pockets are allowed. No true branch should make the player uncertain about chapter progression.

Landmark hierarchy:
1. convoy wagons/supply silhouettes;
2. distant smoke toward Wreck Field;
3. ridge / road-cut silhouette;
4. repeated Yahtrean convoy markers.

---

# 5. CH00_F02 — Wreck Field

Design: broad asymmetrical investigation bowl. Wider and more exploratory than F01, but not an open-world field and not a maze.

Approximate nodes relative to the Wreck Field chunk:
- entry `(0,+60)`;
- survivor/wreck lobe `(−45,+20)`;
- damaged convoy lobe `(+38,+12)`;
- P02 mixed pressure — Crossbowman + Convoy Rift Hound `(+5,+18)`;
- P02 survivor-route Hound `(+5,−10)`;
- evacuation evidence `(−28,−42)`;
- suspicious northern-withdrawal sightline `(+30,−62)`;
- Recovery-Line exit `(0,−70)`.

Topology rule:
> use a looped investigation bowl rather than three long dead ends.

Required evidence must sit on or immediately beside the natural investigation loop. No pixel-hunting through wreck clutter.

The north-withdrawal location is a **sightline/evidence read**, not the player's chapter-progression exit.

---

# 6. CH00_F03 — Evacuation / Recovery Line

Design: mostly linear recovery road with a widened relay yard and a decision overlook.

Approximate nodes:
- entry `(0,+78)`;
- damaged evacuation traffic `(+8,+35)`;
- relay yard `(−12,0)`;
- P03 decision overlook `(+14,−30)`;
- protected recovery stretch `(0,−60)`;
- camp seam `(0,−82)`.

P03 spatial requirement:
from the decision pocket, framing must communicate both:
- the wounded/civilian recovery line toward camp;
- the competing pursuit direction back toward the attack/withdrawal evidence.

No combat trigger volumes belong in the P03 recovery-line sequence.

---

# 7. CH00_F04 — Field Triage Camp

Design: compact working medical camp, not a boss arena disguised as a hospital.

Approximate local zones:
- arrival lane `(0,+40)`;
- wounded/treatment `(−28,+8)`;
- supply/Blue Warden work area `(+24,+5)`;
- P04 Ilyra/Card focal pocket `(0,−10)`;
- P05 concealed-Seyrik pressure pocket `(−8,−34)`;
- P06 combined final-boss perimeter `(+24,−38)`;
- east cut `(+45,−34)`;
- P07 sweep departure `(0,−48)`.

Hard spatial rules:
- P05 and P06 occur on the **camp edge**;
- treatment/supply zones remain protected no-combat spaces;
- the enemy approach through the east cut is visible/understandable;
- no battle spawn is placed among wounded civilians;
- before P05/P06, the perimeter reads as an ordinary defensible camp edge rather than an obvious boss circle.

After victory, the camp remains active and damaged; it does not become celebratory or empty.

---

# 8. CH00_F03R — P07 Survivor Recovery Sweep

This is a **bounded stateful reuse of the Recovery-Line visual/environment family**, attached after the camp scene. It is not an atlas node and should not receive its own permanent location label in final player-facing travel UI.

First graybox local path from the camp:
- sweep start `(0,−48)`;
- wagon-line spur `(−18,−58)`;
- tracks `(−36,−70)`;
- wreck-marker limit `(−34,−86)`;
- sweep-complete bend `(−12,−98)`;
- Brackenwall handoff `(0,−108)`.

Hard rules:
- **no combat**;
- no chase branch beyond the wreck markers;
- no supernatural discovery that competes with the Card mystery;
- route should feel like a short recovery duty, not another adventure zone;
- the player's task is to complete the bounded sweep and proceed toward Brackenwall.

The first graybox uses this spur to reconcile:
- P07's camp-opening dialogue;
- the `PLAYER_CONTROLLED_SURVIVOR_SWEEP` presentation intent;
- the macro route's Triage Camp → Brackenwall handoff.

---

# 9. Pacing Targets

First-pass exploration targets, excluding combat resolution and dialogue:

| Segment | First-time target |
|---|---:|
| Convoy Road | 3–5 min |
| Wreck Field | 4–6 min |
| Recovery Line | 2–3 min |
| Triage Camp exploration/staging | 3–5 min |
| P07 survivor sweep | 2–3 min |

Chapter 0 should remain authored and compact. It is a prologue/tutorial, not a large labyrinthine exploration chapter.

---

# 10. Camera Comparison

The graybox exposes three provisional camera variants:

### A — proof-near
- offset `(0,5.5,7.5)`
- pitch `−25°`
- FOV `60°`

### B — HD-2D test
- offset `(0,6.5,8.5)`
- pitch `−30°`
- FOV `56°`

### C — broader route readability
- offset `(0,7.5,9.5)`
- pitch `−34°`
- FOV `54°`

Validate on desktop and Android:
- player silhouette readability;
- foreground occlusion;
- touch navigation;
- fork/loop readability without assuming a minimap;
- sprite grounding in 3D;
- whether scene scale feels toy-like, cramped or too distant.

No camera becomes production canon from this document alone.

---

# 11. Collision and Boundary Rules

- visible terrain/props should explain collision whenever possible;
- use ridges, wrecks, brush, embankments and camp structures instead of long naked invisible walls;
- route shoulders may be walkable, but should not imply miles of fake exploration;
- required interactions must be touch-friendly and not require precision strafing;
- preserve comfortable clearance for a 1.8-unit player capsule;
- if the player falls outside the provisional graybox, the test scene may reset them; final maps must solve boundaries naturally.

---

# 12. Environment Kit Reservation

Final environment art is downstream of the current visual benchmark pipeline. Blockout should reserve reusable categories only:

### Westways route
- packed dirt / worn convoy road;
- stone/earth banks;
- scrub, grouped grass and sparse trees;
- Yahtrean convoy markers;
- wagon/crate/canvas logistics props.

### Wreck state
- broken wagon variants;
- scattered cargo;
- authored scorch/battle damage;
- damaged route markers;
- survivor shelter/recovery props.

### Triage state
- medical tents;
- stretchers/cots;
- supply tables/crates;
- Blue Warden identifiers;
- field lighting;
- restrained protective-geometry event VFX socket.

Do **not** use the provisional stone/foliage benchmark boards as final GOLD authority.

---

# 13. External AI / Scene-Builder Handoff

An external environment builder eventually receives:
1. this blueprint;
2. approved graybox/topology export;
3. entrances/exits and transition seams;
4. story-event sockets;
5. required sightlines;
6. no-combat/protected zones;
7. current Diyse visual benchmarks;
8. negative constraints;
9. Godot/export assumptions.

The builder may beautify/construct but must preserve:
- encounter order;
- Wreck Field investigation loop;
- north-withdrawal sightline;
- P03 recovery-line logic;
- medical-zone protection;
- P06 camp-edge/east-cut staging;
- P07 bounded no-combat survivor sweep;
- Brackenwall as a separate persistent base map.

Forbidden:
- unsupported major geography;
- maze conversion;
- mandatory platforming;
- new permanent quest nodes;
- wounded civilians as combat obstacles;
- making the suspicious north route the critical path;
- turning P07 into another hostile route;
- final environment art before relevant visual benchmarks are approved.

---

# 14. Promotion Gates to L3

Before Blueprint 001 becomes build-ready locked topology:
1. load the graybox successfully in Godot;
2. verify generated F01/F02/F03/F04/F03R geometry and marker sockets;
3. test route seams;
4. test Android touch movement;
5. compare camera A/B/C;
6. test Wreck Field readability without relying on a minimap;
7. measure traversal pacing;
8. verify P03, P06 and P07 staging against exact dialogue;
9. verify no world-map/geography contradiction;
10. revise dimensions/topology from playtest evidence;
11. explicitly approve the resulting topology;
12. only then promote to L3 and prepare final environment-generation handoff.

## Immediate next production action
> **Validate and play the Chapter-0 graybox, then revise Blueprint 001 from actual traversal evidence.**
