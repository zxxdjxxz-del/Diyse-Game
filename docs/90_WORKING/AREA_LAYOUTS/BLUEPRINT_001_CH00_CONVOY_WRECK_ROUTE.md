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

The line-complete S006 aftermath adds a bounded local recovery sweep after the camp confrontation. That sweep is a **Recovery-Line reuse spur**, not a new world-map destination:

> **Triage Camp → bounded survivor sweep south of the wagon line → Brackenwall handoff**

Mandatory scene/combat order:

### S001 — Opening combat
1. Black Host Raider + Black Host Crossbowman + Ruin Shieldbearer
2. Beast Handler + Convoy Rift Hound
3. Ruin Vanguard Pursuer — protected disengagement; concealed Seyrik retreats alive
4. Riftmaw

### S002 — Wreck Field
- exactly one Convoy Rift Hound encounter;
- survivors, wreckage, evacuation routes and suspicious northern withdrawal must be readable.

### S003 — Evacuation Relay Decision
- no combat;
- wounded/civilians and the damaged recovery line must be spatially visible so Cyanis's refusal of the pursuit reads as professional judgment rather than exposition.

### S004 — Field Triage Camp
- Ilyra introduction;
- sealed Card's incomplete protective geometry;
- no standalone combat before S005.

### S005 — Final Broken Convoy confrontation
Current exact dialogue staging establishes:
- S005 continues directly from S004;
- the protection remains along the **defended camp edge**;
- the War-Sorcerer and injured Soldier advance through the **east cut**;
- Cyanis orders everyone behind stone and explicitly protects the camp from becoming another pursuit;
- surviving Soldier withdraws through the east cut.

Therefore:
> **S005 belongs to the Field Triage Camp perimeter, not the earlier Recovery-Line approach.**

### S006 — Aftermath and bounded survivor sweep
Current exact dialogue staging establishes:
- S006 begins in the still-active camp after S005;
- a wounded escort reports tracks south of the wagon line;
- the officer authorizes **one sweep** with **no chase beyond the wreck markers**;
- Cyanis and Ilyra leave the treatment lane for that bounded survivor sweep;
- Brackenwall follows afterward.

Implementation/presentation interpretation:
- S006 dialogue opens in the camp state;
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
| CH00_F02 | Wreck Field | 180 × 140 m | ~180 m | aftermath reading / one fixed encounter |
| CH00_F03 | Recovery Line | 170 × 85 m | ~170 m | evacuation logic / command decision |
| CH00_F04 | Field Triage Camp | 115 × 95 m | ~110 m | Ilyra / S005 perimeter defense / aftermath |
| CH00_F03R | Survivor Recovery Sweep | ~80 × 70 m local spur | ~80–100 m | S006 no-combat bounded sweep / Brackenwall handoff |

Total first-pass critical traversal is roughly **800 m** before Brackenwall, excluding investigation wandering. At 5 m/s this is under three minutes of uninterrupted running; authored dialogue, fixed battles, investigation, staging and first-time navigation provide the actual pacing.

Coordinate convention:
- +X east;
- −X west;
- −Z chapter-forward/northward screen progression convention for this blockout;
- Y elevation.

Coordinates are test targets, not final centimeter locks.

---

# 4. CH00_F01 — Convoy Road

Design: controlled S-curve / switchback through rugged Westways terrain. Terrain shelves and bends prevent all authored encounters from being visible simultaneously while keeping the route unmistakable.

Approximate nodes:

| Node | Local X/Z | Function |
|---|---|---|
| Start | (0, +112) | opening spawn |
| A | (0, +95) | convoy competence framing |
| B | (−8, +55) | S001 encounter 1 |
| C | (+18, +20) | convoy obstacle / route read |
| D | (+10, −15) | S001 encounter 2 |
| E | (−20, −48) | Pursuer / Seyrik disengagement |
| F | (−5, −82) | Riftmaw staging |
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
- mandatory S002 Hound `( +5,−10)`;
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
- S003 decision overlook `(+14,−30)`;
- protected recovery stretch `(0,−60)`;
- camp seam `(0,−82)`.

S003 spatial requirement:
from the decision pocket, framing must communicate both:
- the wounded/civilian recovery line toward camp;
- the competing pursuit direction back toward the attack/withdrawal evidence.

No combat trigger volumes belong in the S003 recovery-line sequence.

---

# 7. CH00_F04 — Field Triage Camp

Design: compact working medical camp, not a boss arena disguised as a hospital.

Approximate local zones:
- arrival lane `(0,+40)`;
- wounded/treatment `(−28,+8)`;
- supply/Blue Warden work area `(+24,+5)`;
- S004 Ilyra/Card focal pocket `(0,−10)`;
- S005 defensive perimeter `(+8,−38)`;
- east cut `(+45,−34)`;
- S006 sweep departure `(0,−48)`.

Hard spatial rules:
- S005 occurs on the **camp edge**;
- treatment/supply zones remain protected no-combat spaces;
- the enemy approach through the east cut is visible/understandable;
- the surviving Soldier's withdrawal direction is eastward through that cut;
- no battle spawn is placed among wounded civilians;
- before S005, the perimeter reads as an ordinary defensible camp edge rather than an obvious boss circle.

After victory, the camp remains active and damaged; it does not become celebratory or empty.

---

# 8. CH00_F03R — S006 Survivor Recovery Sweep

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
- S006's camp-opening dialogue;
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
| S006 survivor sweep | 2–3 min |

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
- S003 recovery-line logic;
- medical-zone protection;
- S005 camp-edge/east-cut staging;
- S006 bounded no-combat survivor sweep;
- Brackenwall as a separate persistent base map.

Forbidden:
- unsupported major geography;
- maze conversion;
- mandatory platforming;
- new permanent quest nodes;
- wounded civilians as combat obstacles;
- making the suspicious north route the critical path;
- turning S006 into another hostile route;
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
8. verify S003, S005 and S006 staging against exact dialogue;
9. verify no world-map/geography contradiction;
10. revise dimensions/topology from playtest evidence;
11. explicitly approve the resulting topology;
12. only then promote to L3 and prepare final environment-generation handoff.

## Immediate next production action
> **Validate and play the Chapter-0 graybox, then revise Blueprint 001 from actual traversal evidence.**
