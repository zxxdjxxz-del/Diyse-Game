# Diyse — Layout Blueprint 002
## Chapter 1 — Briar Passage / Hollow Watch / Wayfinder

**Status:** PROVISIONAL BLOCKOUT BLUEPRINT / UPPER BRIAR FIRST GRAYBOX CREATED  
**Owner stream:** `90_WORKING/AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`  
**Current graybox scene:** `game/exploration/maps/chapter_01/chapter_01_graybox.tscn`

This blueprint follows the current 12-beat Chapter-1 story authority. It is not final production topology. Dimensions, camera values, traversal lengths, encounter weights, and chunk envelopes remain provisional until played and revised.

## 1. Current route authority

> **Brackenwall → first / northern Briar traversal → Greenhollow → Hollow Watch approach → Hollow Watch surface → short Black Host excavation into Diysean corridor → fixed Shield Construct encounter → Hollow Watch landscape depiction → direct transition to Greenhollow → Southern Briar → Thornhide Stalker → Wayfinder Junction → camp → Dunmere next morning**

Current structure:
- Briar Passage is a **major story area**.
- Brackenwall → Greenhollow is short and comparatively readable.
- Southern Briar is **moderately maze-like**, with a few meaningful forks/reconnections rather than dense labyrinth design.
- Hollow Watch is a compact cliff-side fort over older Diysean construction.
- Hollow Watch underground is a **small excavation/corridor with a few accessible rooms**, not a full dungeon.
- no walking dialogue;
- no post-landscape-depiction playable Hollow Watch backtrack;
- Greenhollow owns Torren's permanent recruitment;
- Wayfinder Junction is safe.

## 2. Current enemy placement

### Northern / first Briar
- Thicket Stalker
- Vine Creeper
- Bullhog
- ordinary formation cap: **2**

### Hollow Watch approach / surface
- Black Host Raider
- Black Host Crossbowman
- Black Host Shieldbearer
- ordinary formation cap: **3**

### Hollow Watch underground
- Construct only in the ordinary random pool
- ordinary formation cap: **2**
- one fixed authored **Shield Construct** encounter
- Shield Construct is stronger than normal, **not random**, and **not a miniboss**
- no Black Host enemies after entry into the Diysean corridor

### Southern Briar
- Thicket Stalker
- Vine Creeper
- Bullhog
- Needlewing
- Burrowclaw
- Barkling
- structural ordinary-formation ceiling: **up to 6**
- current authored examples are 3–4 bodies; exact 5–6 body compositions remain open

### Named encounter
- **Thornhide Stalker** — Chapter-1 main/final boss; Thornhide species; normal lethal victory

### Removed Chapter-1 combat
- no Watch Sentry / Watch Ballista / Watch Captain Frame spread
- no Watch Castellan
- no Cistern Devourer
- no Regional Hunt #1

## 3. Technical blockout baseline

Carry forward the current proof-runtime anchors:
- exploration player: `CharacterBody3D`;
- player capsule height: **1.8 units**;
- proof movement speed: **5.0 units/sec**;
- design viewport: **1920×1080**;
- provisional world convention: **1 Godot unit ≈ 1 meter**.

Chapter-1 first-slice camera variants remain development tests only.

## 4. Current planned chunk set

| ID | Area | Status |
|---|---|---|
| CH01_BP_A | First / northern Briar — Brackenwall → Greenhollow | **GRAYBOX CREATED / TEST REQUIRED** |
| CH01_HW_A | Hollow Watch Approach | provisional design |
| CH01_HW_B | Hollow Watch Surface | provisional design |
| CH01_HW_C | Short excavation / Diysean corridor / Shield Construct | provisional design |
| CH01_HW_D | Landscape-depiction chamber | provisional design |
| CH01_BP_B | Southern Briar | provisional design |
| CH01_WF | Wayfinder Junction | provisional design |

Do not restore Six-Channel, surviving-channel, protected-inner, Castellan, or Cistern-Hunt chunks.

## 5. CH01_BP_A — first / northern Briar graybox

Purpose:
- establish Chapter-1 outdoor route scale;
- test a readable first exploration field;
- validate one shallow reconnection loop without making the route maze-like;
- validate one authored halfway stop;
- establish a reliable ruler before building Hollow Watch and Southern Briar.

Approximate current proof nodes:

| Node | X/Y/Z | Function |
|---|---:|---|
| Brackenwall seam | `(-260,0,+10)` | slice entry |
| U1 | `(-190,+2,+20)` | first road bend |
| U2 | `(-105,+4,+5)` | shallow-loop region |
| Halfway stop | `(0,+6,+18)` | Beat-2 story socket |
| U3 | `(+95,+7,+5)` | silent second half |
| U4 | `(+185,+6,-8)` | Greenhollow approach |
| Greenhollow seam | `(+260,+5,0)` | slice exit |

Current proof widths:
- main route: ~7 m;
- optional loop: ~5.2 m;
- pocket connectors: ~4.2 m;
- halfway widening: ~18 × 16 m.

These numbers are test geometry, not canon distance.

Encounter zoning:
> Brackenwall SAFE → west Upper Briar ACTIVE → halfway SAFE → east Upper Briar ACTIVE → Greenhollow SAFE

Do not add a false trail, damaged crossing, civilian-crossing event, separate Old Waystone, or extra route-guidance stop.

## 6. Hollow Watch structure

### CH01_HW_A — Approach
- old watch trail;
- one clean fort reveal;
- light occupation / excavation evidence;
- Torren chooses the less exposed west-wall approach;
- reveal pocket SAFE.

### CH01_HW_B — Surface
- compact occupied fort;
- light Black Host pressure only;
- dead-garrison authored discovery;
- obvious logistics/excavation route downward;
- no watch-room records scene.

### CH01_HW_C — Excavation / Diysean corridor
- fort foundation → Black Host excavation → preexisting Diysean corridor;
- excavation evidence shows sustained work ending abruptly;
- after crossing into the Diysean corridor, **Constructs only**;
- one short main corridor with a few rooms;
- ordinary-person relief/image band;
- fixed Shield Construct room and aftermath buffer;
- no route-unlock function attached to the Shield Construct.

### CH01_HW_D — Landscape depiction
- safe ancient room;
- large preserved regional landscape image;
- fire falling across the region;
- people moving toward/into constructed underground spaces;
- Hollow Watch and the Junction can be recognized geographically;
- Black Host objective remains unresolved;
- direct story transition to Greenhollow after the discovery.

## 7. Southern Briar structure

Southern Briar is the chapter's largest natural exploration/combat area.

Desired route rhythm:
> readable opening → increasing route ambiguity → Thornhide sign/track authored stop → hardest moderate navigation / reconnecting loops → more direct predator-pressure final leg → Thornhide Stalker first clear sighting → boss → quiet route to Wayfinder

Requirements:
- moderately maze-like, not heavily labyrinthine;
- a few meaningful forks;
- one or two reconnecting loops;
- misleading-looking natural branches;
- Torren's route experience matters;
- no guided traversal dialogue;
- no Cistern / overgrown side-access Hunt hook;
- encounter frequency may thin near Thornhide territory;
- immediate boss approach is SAFE;
- post-boss route and Wayfinder are SAFE.

## 8. Wayfinder structure

Wayfinder:
- old roads converge;
- no random encounters;
- monument remains visually unclear until authored interaction;
- revealed surface reads as a **regional western-Diyse map**, not a local crossroads diagram;
- dense overland route lines and numerous ancient city/settlement structures survive;
- a second visually distinct marking system crosses the map;
- production truth is that the second system represents underground infrastructure across the ancient network, but Chapter 1 does not identify it;
- the greatest concentration lies around present-day **Caelora**;
- the Wayfinder is physically broken through the center of that concentration;
- enough surrounding routes/structures survive to make the missing center's scale obvious;
- southeast alignment toward Dunmere remains legible;
- no Cistern notation or Hunt backtrack is required;
- camp sits beside, not inside, the crossroads.

## 9. First-slice graybox instrumentation

Retain:
- camera A/B/C switching;
- reset control;
- desktop and touch movement;
- elapsed traversal timer;
- resolved player-distance counter;
- current encounter-state label;
- story-socket trigger count;
- Beat-2 halfway story marker.

Test:
1. critical-path sprint;
2. normal first-time exploration;
3. completionist loop/pocket sweep.

Record:
- traversal time;
- distance moved;
- whether the loop feels useful or annoying;
- whether the route feels too straight;
- whether elevation feels meaningful without becoming mountainous;
- whether Camera B gives adequate route readability;
- whether the halfway stop lands naturally;
- whether the Greenhollow seam arrives too early or too late.

## 10. Negative constraints

Do not reintroduce:
- southern-Briar false trail;
- route split / overlook decision;
- damaged crossing / civilian crossing;
- separate Old Waystone;
- Lower Woods rescue;
- early Hollow Watch map rubbing;
- watch-room records scene;
- Six-Channel Junction as a separate gameplay room;
- surviving-channel progression;
- protected-inner / forced-door route;
- Watch Captain Frame as Chapter-1 normal-pool content;
- Watch Castellan;
- Cistern Devourer / Regional Hunt #1;
- playable post-landscape-depiction Hollow Watch backtrack;
- early visible Wayfinder monument;
- random combat directly on authored story triggers.

Do not beautify the graybox into production environment art before scale/topology approval.

## 11. Promotion gate

Before expanding beyond the current Upper Briar proof:
1. load `chapter_01_graybox.tscn` successfully;
2. run the Upper Briar slice with Camera A/B/C;
3. verify every path/loop connection;
4. verify optional pockets return cleanly;
5. verify the halfway trigger fires once per reset;
6. verify encounter-state transitions;
7. record sprint / normal / completionist traversal times;
8. revise scale from actual play;
9. approve Upper Briar scale as the Chapter-1 outdoor ruler.

## Immediate production action

> **Run and evaluate CH01_BP_A before building the current Hollow Watch chunks.**
