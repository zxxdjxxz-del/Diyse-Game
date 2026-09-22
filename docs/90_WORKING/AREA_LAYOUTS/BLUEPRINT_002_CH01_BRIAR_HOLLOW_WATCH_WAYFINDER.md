# Diyse — Layout Blueprint 002
## Chapter 1 — Briar Passage / Hollow Watch / Wayfinder

**Status:** PROVISIONAL BLOCKOUT BLUEPRINT / UPPER BRIAR FIRST GRAYBOX CREATED  
**Owner stream:** `90_WORKING/AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`  
**Current graybox scene:** `game/exploration/maps/chapter_01/chapter_01_graybox.tscn`

This blueprint converts the current Chapter-1 story/dialogue route into testable exploration geometry. It is **not yet L3 build-ready topology**. Dimensions, camera values, traversal lengths and chunk envelopes remain provisional until played and revised.

Current first implementation intentionally covers only:

> **Brackenwall seam → Upper Briar → Greenhollow seam**

The remaining Chapter-1 chunks stay design-approved only at provisional graybox level until the first slice establishes a trustworthy scale.

---

# 1. Current Story / Route Authority

Current Chapter-1 route used by this blueprint:

> **Brackenwall → Briar Passage first traversal → Greenhollow → Hollow Watch approach → Hollow Watch surface fort → Black Host excavation → Six-Channel Junction → sole surviving channel → Castellan → mural → direct transition to Greenhollow → Southern Briar → Briarhide Stalker → Wayfinder Junction → camp → Dunmere next morning**

Current cleanup constraints carried into layout:
- first Briar traversal has one authored halfway stop;
- no guided traversal scene on that leg;
- Hollow Watch approach has one major reveal and then continuous west-wall approach;
- surface fort has one major authored stop: dead garrison;
- no watch-room records scene;
- excavation is mostly continuous environmental progression;
- Six-Channel Junction has five ancient collapsed channels and one surviving route;
- no route choice in the Junction;
- after the mural there is no playable return through Hollow Watch;
- Greenhollow owns Torren's permanent recruitment;
- Southern Briar has no guided traversal dialogue;
- Briarhide track occurs before the hardest route-reading stretch;
- overgrown side access occurs late, in the final third/quarter;
- final Southern Briar route becomes more direct before Briarhide;
- Wayfinder is safe and the monument remains visually hidden until interaction.

---

# 1A. Current Enemy Placement Lock

Chapter-1 enemy names and area assignments are locked for layout work.

**Upper / first Briar**
- Greenhollow Stalker
- Thornvine Creeper
- Briar Boar

**Hollow Watch — Black Host**
- Black Host Raider
- Black Host Crossbowman
- Ruin Shieldbearer

**Hollow Watch — ancient constructs**
- Hollow Watch Sentry
- Hollow Watch Ballista
- Watch Captain Frame

Watch Captain Frame is a strong normal-pool enemy, not optional side-room combat.

**Southern Briar**
- Greenhollow Stalker
- Thornvine Creeper
- Briar Boar
- Needlewing
- Rootmaw
- Brambleback

**Named encounters**
- Hollow Watch Castellan — mandatory mini-boss
- Briarhide Stalker — Chapter-1 main/final boss
- Cistern Devourer — Hunt; optional combat

Placement firewalls:
- no Chapter-1 Black Host or construct random encounters in Briar Passage;
- Southern Briar must visibly support the broader six-enemy natural ecology;
- Southern Briar ordinary formations may contain up to **5 active enemies**; this is a Chapter-1 area-specific exception and does not raise the first-Briar or Hollow-Watch caps;
- Hunts are the only optional combat encounters.

---

# 2. Technical Blockout Baseline

Carry forward the current proof-runtime anchors:
- exploration player: `CharacterBody3D`;
- player capsule height: **1.8 units**;
- proof movement speed: **5.0 units/sec**;
- design viewport: **1920×1080**;
- provisional world convention: **1 Godot unit ≈ 1 meter**.

Chapter-1 first-slice camera variants remain development tests only.

Because Upper Briar trends broadly west → east, the first graybox uses an east-facing camera family:
- A: near;
- B: HD-2D test;
- C: broad-readability test.

Future chunks may use different camera orientation/overrides where topology demands it.

---

# 3. Planned Chunk Set

| ID | Area | Approx. envelope | Approx. critical traversal | Status |
|---|---|---:|---:|---|
| CH01_BP_A | Upper Briar | ~540 × 170 m | ~520 m | **GRAYBOX CREATED / TEST REQUIRED** |
| CH01_HW_A | Hollow Watch Approach | ~260 × 380 m | ~470 m | provisional design |
| CH01_HW_B | Hollow Watch Surface | ~115 × 90 m | ~190–230 m | provisional design |
| CH01_HW_C | Excavation | ~165 × 115 m | ~240–280 m | provisional design |
| CH01_HW_D | Six Channels + surviving channel | ~150 × 135 m | ~170–210 m | provisional design |
| CH01_HW_E | Protected Inner / Castellan | ~115 × 95 m | ~120 m pre-boss | provisional design |
| CH01_HW_F | Mural | ~65 × 50 m | ~50–70 m | provisional design |
| CH01_BP_B | Southern Briar | ~370 × 720 m | ~900 m | provisional design |
| CH01_WF | Wayfinder Junction | ~145 × 120 m | ~100–140 m | provisional design |

Do not use these numbers as canon distance.

---

# 4. CH01_BP_A — Upper Briar First Graybox

Purpose:
- establish Chapter-1 outdoor route scale;
- test the first normal exploration field;
- validate one shallow reconnection loop without making the route maze-like;
- validate one authored halfway stop;
- test optional-pocket density;
- establish a reliable ruler before building Hollow Watch and Southern Briar.

Approximate main nodes:

| Node | X/Y/Z | Function |
|---|---:|---|
| Brackenwall seam | `(-260,0,+10)` | slice entry |
| U1 | `(-190,+2,+20)` | first road bend |
| U2 | `(-105,+4,+5)` | shallow-loop region |
| Halfway stop | `(0,+6,+18)` | Beat-2 story socket |
| U3 | `(+95,+7,+5)` | long silent second half |
| U4 | `(+185,+6,-8)` | Greenhollow approach |
| Greenhollow seam | `(+260,+5,0)` | slice exit |

First-pass width:
- main route: ~7 m;
- optional loop: ~5.2 m;
- pocket connectors: ~4.2 m;
- halfway widening: ~18 × 16 m.

Current optional topology:
- one shallow loop that reconnects directly to the main road;
- Pocket U1 off the loop;
- Pocket U2 off the second-half route.

Reward identities are not locked here. These are reward sockets only.

---

# 5. Upper Briar Encounter / Story Zoning

Development debug states:

> **ACTIVE** = ordinary random-encounter-capable traversal  
> **SAFE** = encounter-suppressed story/seam buffer

Current first slice:

> Brackenwall SAFE → west Upper Briar ACTIVE → halfway SAFE → east Upper Briar ACTIVE → Greenhollow SAFE

The Beat-2 halfway socket is the only authored story trigger in the playable first slice.

Do not add:
- another route-guidance stop;
- a separate Greenhollow threshold scene;
- a false trail;
- a damaged crossing;
- a civilian-crossing event;
- an Old Waystone.

---

# 6. Upper Briar Landmark / Camera Intent

Upper Briar should remain the most readable major Briar leg.

Required:
- main route silhouette stays understandable;
- shallow loop reads as optional/reconnecting, not a second destination;
- optional pockets are visible enough to reward curiosity;
- halfway stop feels like natural widened terrain, not a designated dialogue stage;
- Greenhollow is not visible from the entire area;
- foreground vegetation frames rather than persistently obscures the player.

The current first graybox intentionally uses primitive forest-wall boundaries. They are collision/readability tests, not environment art.

---

# 7. Planned Hollow Watch Structure

After Upper Briar scale is validated, build in this order:

1. **CH01_HW_A — Approach**
   - old watch trail;
   - service-path shelf;
   - ridge shoulder;
   - single Hollow Watch hero reveal;
   - concealed west-wall approach;
   - fort seam.

2. **CH01_HW_B — Surface**
   - west-wall entry;
   - compact occupied fort;
   - dead-garrison lateral stop;
   - one small optional service/supply room;
   - obvious downward logistics route.

3. **CH01_HW_C — Excavation**
   - fort basement;
   - active Black Host excavation;
   - mixed Yahtrean/Diysean construction;
   - predominantly Diysean structure;
   - ordinary enemy-family transition from Host to ancient defenses.

4. **CH01_HW_D — Six Channels**
   - large circular landmark chamber;
   - five ancient collapsed channels;
   - one surviving channel;
   - human-use relief;
   - no fake route choice.

5. **CH01_HW_E — Protected Inner / Castellan**
   - intact protected access;
   - Host wall bypass;
   - increasingly intact route;
   - safe pre-boss buffer;
   - Castellan chamber.

6. **CH01_HW_F — Mural**
   - short protected passage;
   - mural-dominant chamber;
   - no optional loot;
   - direct story transition to Greenhollow.

---

# 7A. Hollow Watch Encounter Zoning

**Approach / surface**
- Black Host formations only.
- Fort-reveal and dead-garrison authored pockets are SAFE.

**Excavation**
- early basement: Black Host only;
- transition sector: Black Host pool or construct pool, but never mixed inside one battle;
- deep Diysean sector: constructs only;
- Watch Captain Frame becomes eligible only in the deep sector.

**Six Channels**
- relief chamber / authored reading pocket: SAFE;
- surviving channel: constructs only, including Watch Captain eligibility.

**Protected Inner**
- construct encounters remain legal before the pre-boss buffer;
- immediate pre-Castellan buffer: SAFE;
- Castellan chamber: authored mini-boss only.

**Mural**
- SAFE.

---

# 8. Planned Southern Briar Structure

Southern Briar should be the chapter's most naturally ambiguous field without becoming a puzzle labyrinth.

Required order:

> readable opening → Briarhide track → hardest navigation / reconnecting loops → late overgrown side access → more direct final leg → Briarhide first sighting → boss → quiet post-boss route → Wayfinder

The late side access must remain close enough to Wayfinder that the cleanup return for the Cistern branch is short.

No guided traversal dialogue.

---

# 8A. Southern Briar Encounter Zoning

**Readable opening**
- Predator Trail
- Rooted Skirmish
- Bramble Wall
- no five-enemy formation

**Briarhide-track pocket**
- SAFE

**Hard-navigation / reconnecting-loop middle**
- all six Southern-Briar formations
- Canopy Rush may reach the locked five-enemy cap here

**Late side-access approach**
- Predator Trail
- Rooted Skirmish
- Rootbound Growth
- Bramble Wall

**Overgrown side-access pocket**
- SAFE

**More-direct final leg**
- Predator Trail
- Bramble Wall
- Heavy Woods
- Canopy Rush

**Briarhide sighting / boss buffer**
- SAFE

**Post-boss route / Wayfinder**
- SAFE

Cleanup return to the Cistern access:
- uses the final-leg encounter pool until the side-access SAFE pocket.

---

# 9. Planned Wayfinder Structure

Wayfinder:
- old roads converge;
- no random encounters;
- central ancient object initially reads as a broad low fitted mass;
- monument itself is not visually legible before the authored clearing interaction;
- clearing reveals the cartographic surface rather than causing a giant structure to rise;
- camp sits beside, not in, the crossroads;
- southeast road continues toward Dunmere;
- Southern Briar remains revisitable during cleanup.

---

# 10. First-Slice Graybox Instrumentation

The current Chapter-1 graybox adds:
- camera A/B/C switching;
- reset control;
- desktop and touch movement via existing exploration controller;
- elapsed traversal timer;
- resolved player-distance counter;
- current encounter-state label;
- story-socket trigger count;
- Beat-2 halfway story marker.

The first test should be run three ways:
1. critical-path sprint;
2. normal first-time exploration;
3. completionist pocket/loop sweep.

Record:
- traversal time;
- distance moved;
- whether the loop feels useful or annoying;
- whether the road feels too straight;
- whether elevation feels meaningful but not mountainous;
- whether Camera B gives adequate route readability;
- whether the halfway stop lands naturally;
- whether the Greenhollow seam arrives too early or too late.

---

# 11. Negative Constraints

Do not reintroduce:
- southern-Briar false trail;
- route split / overlook decision;
- damaged crossing / civilian crossing;
- separate Old Waystone;
- Lower Woods rescue;
- Greenhollow Briarhide Stalker fight;
- early Hollow Watch map rubbing;
- watch-room records scene;
- Black Host testing five alternate Six-Channel routes;
- playable post-mural Hollow Watch backtrack;
- early visible Wayfinder monument;
- random combat directly on top of authored story triggers.

Do not beautify the graybox into production environment art before scale/topology approval.

---

# 12. Promotion Gate

Before expanding Blueprint 002 into Hollow Watch geometry:

1. load `chapter_01_graybox.tscn` successfully in Godot;
2. run the Upper Briar slice with Camera A/B/C;
3. verify movement across every ramp/path segment;
4. verify loop entry and exit are physically connected;
5. verify both optional pockets are reachable and return cleanly;
6. verify halfway trigger fires once per reset;
7. verify encounter-state transitions are sensible;
8. record sprint / normal / completionist traversal times;
9. revise width, length, elevation and loop geometry from actual play;
10. explicitly approve Upper Briar scale as the Chapter-1 outdoor ruler.

## Immediate next production action

> **Run and evaluate CH01_BP_A — Upper Briar before building Hollow Watch.**
