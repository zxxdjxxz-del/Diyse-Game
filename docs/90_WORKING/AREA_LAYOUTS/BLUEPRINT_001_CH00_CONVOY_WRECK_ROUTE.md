# Diyse — Layout Blueprint 001
## Chapter 0 — Convoy Road / Wreck Field / Recovery Line / Field Triage Camp

**Status:** PROVISIONAL BLOCKOUT BLUEPRINT / READY FOR FIRST 3D TEST BUILD  
**Owner stream:** `90_WORKING/AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`  
**Inventory source:** `90_WORKING/PLAYABLE_AREA_INVENTORY_WORKING.md`

This blueprint converts Chapter 0's locked story order into testable 3D exploration geometry. It is **not yet an L3 final topology**. Dimensions/camera values below are first-pass vertical-slice constants and may change after the route is played on desktop and Android.

---

# 1. Canon Constraints

The route must preserve this mandatory order:

> **Convoy Road → Wreck Field → Evacuation / Recovery Line → Field Triage Camp → Brackenwall**

Chapter-0 combat/story order must remain compatible with:

### S001 — opening-combat segment
1. Black Host Raider + Black Host Crossbowman + Ruin Shieldbearer
2. Beast Handler + Convoy Rift Hound
3. Ruin Vanguard Pursuer — protected disengagement; concealed Seyrik retreats alive
4. Riftmaw

### S002 — Wreck Field
- exactly one Convoy Rift Hound encounter;
- survivors, wreckage, threats, evacuation routes and suspicious northern withdrawal must be readable.

### S003 — Evacuation Relay Decision
- no combat;
- decision must occur in a space where wounded/civilians and the damaged line are visibly relevant.

### S004 — Field Triage Camp
- Ilyra introduction;
- no standalone combat before S005.

### S005 — final Broken Convoy confrontation
- Convoy War-Sorcerer + injured Iron Cohort Soldier;
- War-Sorcerer is victory target;
- surviving Soldier withdraws.

### S006 — aftermath
- no combat;
- Brackenwall handoff.

Do not add:
- Prime manifestation;
- optional dungeon branches;
- mandatory loot detours;
- a second rearguard battle after the final confrontation;
- a large open-world field that weakens the authored tutorial pacing.

---

# 2. Technical Blockout Baseline

Current runtime proof anchors:
- exploration uses `CharacterBody3D`;
- player collision capsule height = **1.8 units**;
- proof movement speed = **5.0 units/sec**;
- proof camera offset = approximately **(0, +5.5, +7.5)** from player;
- proof pitch = **−25°**;
- proof FOV = **60°**;
- design viewport = **1920×1080**.

For Blueprint 001 only:
> **1 Godot world unit ≈ 1 meter**

This is a blockout convention, not a lore/canon measurement system.

## First-pass path widths
- convoy-capable road: **8–10 m**;
- ordinary walkable connector: **5–6 m**;
- intentional narrow passage: **3.5–4 m minimum**;
- story gathering pocket: **12–18 m** across;
- major authored battle-transition staging pocket: **20–28 m** across.

Because ordinary combat transitions to a dedicated combat scene, field clearings do **not** need to contain the entire battle formation. They need enough room for readable pre-battle staging, encounter triggering and cinematic handoff.

---

# 3. Scene Chunk Strategy

For the first production test, build Chapter 0 as **four connected 3D field chunks** plus the Brackenwall transition.

| Scene ID | Area | Approx. envelope | Critical-path distance | Purpose |
|---|---|---:|---:|---|
| CH00_F01 | Convoy Road | 220 × 100 m | ~260 m | movement/tutorial combat cadence |
| CH00_F02 | Wreck Field | 180 × 140 m | ~180 m | aftermath reading / one encounter |
| CH00_F03 | Recovery Line | 170 × 85 m | ~170 m | evacuation logic / command decision |
| CH00_F04 | Field Triage Camp | 115 × 95 m | ~110 m | Ilyra intro / final confrontation / aftermath |

Total critical-path walk distance before Brackenwall:
> approximately **720 m**

At the current 5 m/s proof movement speed, pure uninterrupted running would be ~144 seconds. Authored stops, inspections, combat transitions, dialogue and cautious first-time navigation should make the actual Chapter-0 field experience substantially longer without padding the route.

---

# 4. Coordinate Convention

Each chunk uses a local X/Z plane:
- **+X = east**
- **−X = west**
- **−Z = forward/north along chapter progression**
- Y = elevation

Coordinates are blockout targets, not final centimeter-perfect placements.

---

# 5. CH00_F01 — Convoy Road

## Envelope
- width: **100 m**
- length: **220 m**
- elevation range target: **0–12 m**
- dominant road width: **9 m**

## Core shape
A controlled S-curve/switchback road through rugged Westways terrain. The player should repeatedly see the road continuing ahead, but bends/terrain shelves prevent all four authored encounters from being visible at once.

### Critical nodes

| Node | Approx. X/Z | Function |
|---|---|---|
| F01-A | (0, +95) | opening spawn / convoy competence framing |
| F01-B | (−8, +55) | Encounter 1 staging pocket |
| F01-C | (+18, +20) | brief convoy-obstacle/navigation beat |
| F01-D | (+10, −15) | Encounter 2 staging pocket |
| F01-E | (−20, −48) | Pursuer encounter/disengagement pocket |
| F01-F | (−5, −82) | Riftmaw approach pocket |
| F01-X | (0, −105) | transition seam to Wreck Field |

## Topology

```text
START / convoy rear
      |
      |  broad road
      v
 [A] Opening shelf
      |
  bend left
      v
 [B] Encounter 1 clearing
      \
       \ raised shoulder / sightline
        [C] obstructed convoy lane
          \
           [D] Handler + Hound pocket
             |
         descending bend
             |
         [E] Pursuer pocket
             |
        short recovery stretch
             |
         [F] Riftmaw pocket
             |
       blind bend / seam
             v
        WRECK FIELD
```

## Side-space rule
Only **two shallow side pockets** should exist:
1. a 10–15 m shoulder near C for environmental/tutorial inspection;
2. a 12–16 m rocky verge between E and F for breathing-room composition.

Neither is a true branch. Player must never wonder which road advances the chapter.

## Landmark hierarchy
1. convoy wagons / supply silhouettes;
2. distant smoke plume toward the Wreck Field direction;
3. rugged ridge/road-cut silhouette;
4. repeated Yahtrean convoy markers establishing route identity.

## Transition seam
Use a road bend with rising terrain/foreground occluder so F01 can unload before F02 is visually exposed.

---

# 6. CH00_F02 — Wreck Field

## Envelope
- width: **180 m**
- depth: **140 m**
- elevation range: **−3 to +8 m**

## Design purpose
This is the first area that asks the player to **read a situation**, not merely advance through encounters.

It should feel wider and less linear than F01 without becoming an open-world field.

## Core shape
A broad asymmetrical wreck basin with one obvious forward evacuation line and three readable investigation lobes.

### Critical nodes

| Node | Approx. X/Z | Function |
|---|---|---|
| F02-A | (0, +60) | arrival from Convoy Road |
| F02-B | (−45, +20) | survivor/wreck lobe |
| F02-C | (+38, +12) | damaged wagon/threat-reading lobe |
| F02-D | (+5, −10) | mandatory Convoy Rift Hound encounter |
| F02-E | (−28, −42) | evacuation-route evidence lobe |
| F02-N | (+30, −62) | sightline toward suspicious northern withdrawal |
| F02-X | (0, −70) | Recovery Line exit |

## Topology

```text
                [B] survivor wrecks
               / 
ENTRY [A] ----+---- [D] hound pressure ---- [C] damaged convoy lobe
               \          |
                \         v
                 [E] evacuation evidence
                    \     /
                     [N] north-withdrawal sightline
                          |
                          v
                    RECOVERY LINE
```

This is a **looped investigation bowl**, not three dead-end corridors. The player may inspect B/C/E in different order while D controls the middle and the final exit remains visually understandable.

## Northern withdrawal read
At F02-N the player should be able to see a distant route cut/ridge opening oriented away from the civilian recovery path. Do not require a literal visible enemy army; the geometry should make the withdrawal direction legible through tracks, smoke, broken formation or distant silhouettes depending on final art/staging.

## Wreck density
- center: moderate debris, enough clear movement space;
- B/C: denser wreck clusters;
- E/X corridor: deliberately clearer so evacuation logic reads visually.

## No hidden mandatory object rule
Any required story evidence must lie on or immediately beside the natural investigation loop. Do not require pixel-hunting among wreck props.

---

# 7. CH00_F03 — Evacuation / Recovery Line

## Envelope
- width: **85 m**
- length: **170 m**
- elevation range: **0–9 m**

## Design purpose
This route proves why Cyanis refuses the unsound pursuit. The environment must visibly communicate:
- wounded people moving slowly;
- damaged convoy logistics;
- limited safe staffing;
- a real route to abandon if the party chases north.

## Shape
A mostly linear recovery road with one widened relay yard and one overlook/decision pocket.

### Critical nodes

| Node | Approx. X/Z | Function |
|---|---|---|
| F03-A | (0, +78) | entry from Wreck Field |
| F03-B | (+8, +35) | evacuation traffic / damaged line |
| F03-C | (−12, 0) | relay yard / civilians and wounded visible |
| F03-D | (+14, −30) | S003 decision overlook |
| F03-E | (0, −60) | protected recovery stretch |
| F03-X | (0, −82) | Triage Camp seam |

## Topology

```text
WRECK FIELD
    |
 [A] recovery road
    |
 [B] damaged convoy flow
    |
 [C] relay yard ===== wounded/civilian activity
      \
       [D] command-decision overlook
        |
       [E] recovery stretch
        |
        v
   TRIAGE CAMP
```

## S003 staging requirement
The player/superior officer decision position at D should see both:
- the recovery line continuing toward camp;
- a partial/distant view back toward the northward pursuit direction.

This lets the argument be spatially obvious rather than delivered in an abstract dialogue box.

## Combat rule
No combat trigger volumes in this scene.

---

# 8. CH00_F04 — Field Triage Camp

## Envelope
- width: **115 m**
- depth: **95 m**
- mostly level; max elevation change **4 m**

## Design purpose
Compact, human-scale decompression space that can transform into the final confrontation without making a medical camp feel like a boss arena.

## Core zones

| Zone | Approx. X/Z | Function |
|---|---|---|
| F04-A | (0, +40) | arrival/check-in lane |
| F04-B | (−28, +8) | wounded treatment tents |
| F04-C | (+24, +5) | supplies / Blue Warden work area |
| F04-D | (0, −10) | Ilyra / sealed Card S004 focal pocket |
| F04-E | (+8, −38) | camp perimeter / S005 confrontation staging |
| F04-F | (−15, −45) | Soldier withdrawal vector / aftermath visibility |
| F04-X | (0, −52) | Brackenwall road transition |

## Topology

```text
RECOVERY LINE
     |
 [A] arrival lane
   /     \
 [B]     [C]
 wounded  supplies / Warden activity
    \     /
      [D] Ilyra + Card focal space
        |
   camp lane / no combat
        |
      [E] perimeter confrontation
       / \
 [F] withdrawal   [X] Brackenwall road
```

## S004 protection
Before S005, E must read as an **ordinary camp perimeter/approach**, not a glowing obvious boss circle.

The final encounter can stage there because it is the most defensible open edge of the camp, not because the camp was architected around a fight.

## Medical-space firewall
Do not place battle damage, enemy spawn points or aggressive encounter dressing inside B/C treatment spaces. S005 pressure reaches the perimeter; it does not turn wounded civilians into decorative combat obstacles.

## Aftermath state
After S005:
- hostile staging props clear/disable;
- Soldier withdrawal path remains visually readable;
- camp returns to recovery activity;
- Brackenwall exit becomes the strongest navigational cue.

---

# 9. Brackenwall Transition

Blueprint 001 does **not** design Brackenwall itself.

For now F04-X ends at:
- road crest / tree or wall occlusion;
- transition trigger;
- location card / load seam into future Brackenwall base map.

Do not fake a one-off Chapter-0 Brackenwall strip that later has to be discarded.

---

# 10. Pacing Targets

First-pass target excluding combat resolution and dialogue time:

| Segment | First-time exploration target |
|---|---:|
| Convoy Road | 3–5 min |
| Wreck Field | 4–6 min |
| Recovery Line | 2–3 min |
| Triage Camp | 3–5 min |

The route should feel authored and compact. Chapter 0 is a tutorial/prologue, not the place to establish huge labyrinthine field maps.

---

# 11. Camera / HD-2D Test Plan

Do not lock final camera from the proof scene yet.

For the first blockout, test these three camera variants using the same route:

### Variant A — proof-near
- offset: (0, 5.5, 7.5)
- pitch: −25°
- FOV: 60°

### Variant B — slightly more authored HD-2D
- offset: (0, 6.5, 8.5)
- pitch: −30°
- FOV: 55–58°

### Variant C — broader route readability
- offset: (0, 7.5, 9.5)
- pitch: −32° to −35°
- FOV: 52–56°

Evaluate:
- player silhouette readability;
- foreground occlusion;
- touch-control navigation on Android;
- ability to read forks/loops without minimap;
- whether environment scale feels too toy-like or too distant;
- billboard sprite grounding in 3D scene lighting.

No camera variant becomes canon until gameplay comparison.

---

# 12. Collision / Navigation Rules

- invisible collision should follow visible terrain/props whenever possible;
- road shoulders may be walkable in limited depth but should not invite fake exploration miles beyond the authored route;
- use terrain, wrecks, brush, embankments and camp structures to form believable soft boundaries;
- avoid long naked invisible walls;
- ensure no 1.8 m player capsule clips under foreground hero props;
- preserve at least ~1 m lateral clearance beyond the player collision radius in narrow navigation spaces;
- all required interactables must be reachable with touch movement without precision strafing.

---

# 13. Environment Kit Placeholder

Final style/materials are downstream of visual benchmark approval. The blockout should nevertheless reserve categories for:

### Westways convoy route kit
- packed dirt / worn military road;
- exposed stone/earth banks;
- scrub/grass clusters;
- sparse trees/branches;
- Crown/Yahtrean convoy markers;
- wagons/crates/canvas/logistics props.

### Wreck-state kit
- broken wagon variants;
- scattered cargo;
- scorch/battle damage decals or meshes;
- damaged route markers;
- survivor shelter props.

### Triage kit
- canvas medical tents;
- stretchers/cots;
- supply tables/crates;
- Blue Warden medical identifiers;
- field lanterns / restrained magical-medical focal props where later approved.

Do not use current provisional stone/foliage texture boards as final GOLD style authority.

---

# 14. External AI / Scene-Builder Handoff

An external builder receives:
- this blueprint;
- a simple top-down blockout image exported from the coordinates above;
- current world/region visual authority;
- approved visual benchmarks once available;
- collision and transition requirements;
- exact story-event sockets.

## Required preservation
The builder may beautify and optimize but must preserve:
- four-scene order;
- encounter order;
- Wreck Field investigation loop;
- northern-withdrawal sightline;
- S003 recovery-line spatial logic;
- camp medical-zone protection;
- final confrontation at camp perimeter;
- Brackenwall as a separate future persistent base map.

## Forbidden changes
Do not:
- invent a river, castle, giant bridge or other major geography not supported by current world authority;
- turn Wreck Field into a maze;
- create mandatory platforming;
- add permanent quest nodes not in Chapter 0;
- make wounded civilians part of the combat arena;
- make the suspicious northern route the player progression route;
- build final art before the relevant visual benchmark set is approved.

---

# 15. Approval Gates for Blueprint 001

Before promoting this to L3:

1. create graybox CH00_F01–F04 in Godot or a compatible 3D blockout tool;
2. test all transition seams;
3. test movement on Android touch controls;
4. compare camera variants A/B/C;
5. test Wreck Field route readability without a minimap;
6. verify pure traversal/pacing targets;
7. confirm story/cutscene event sockets are large enough;
8. confirm no route geometry contradicts world/story authority;
9. revise coordinates/dimensions from playtest evidence;
10. only then lock the final topology and produce the environment-generation packet.

## Next production action
> **Build the Chapter-0 graybox from this blueprint.**
