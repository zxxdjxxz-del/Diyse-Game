# Working — Area & Route Layout Production

**Status:** ACTIVE / PHASE A INVENTORY CREATED / BLUEPRINTING STARTED

**Cross-domain owners:**
- `04_WORLD_AND_LORE` — macro geography, place hierarchy, world-map placement, road/travel authority;
- `02_STORY` / `03_DIALOGUE` — scene order, authored gates, story beats and required traversal moments;
- `09_ENEMIES_AND_ENCOUNTERS` — encounter placement and combat-space requirements;
- `14_ART_AND_VISUALS` — environment style, materials, lighting language and HD-2D presentation;
- `13_UI_AND_IMPLEMENTATION` — collision, navigation, transitions, streaming/loading, camera and engine integration.

## Why this is a separate open stream

The world map and macro travel routes are not the same thing as playable area design.

Current authority already tells us where places are and, in many cases, the order in which named local spaces are visited. It does **not** yet define the actual explorable geometry needed to build the game.

Examples of already-known macro authority include:
- chapter travel sequences in `04_WORLD_AND_LORE/MAP/ROADS_AND_CHAPTER_TRAVEL.md`;
- local Character Quest sequences in `04_WORLD_AND_LORE/LOCATIONS/CHARACTER_QUEST_GEOGRAPHY.md`;
- permanent world-map placement and road relationships.

Those files remain authoritative. This stream fills the missing layer between those authorities and a production-ready environment.

## What still has to be designed for each playable area

Each field, town, route, dungeon, facility, Hunt site or quest space eventually needs a **build packet** containing at least:

1. **Playable footprint / blockout**
   - top-down or isometric layout;
   - approximate scale;
   - walkable vs non-walkable boundaries.

2. **Entrances, exits and transitions**
   - where the player arrives;
   - where each exit leads;
   - return routes;
   - one-way transitions where intentionally authored.

3. **Critical path**
   - mandatory traversal line;
   - story-gated checkpoints;
   - required set-piece positions;
   - intended traversal order.

4. **Optional topology**
   - loops;
   - side pockets;
   - shortcuts;
   - dead ends used intentionally for treasure, lore, encounters or visual payoff;
   - revisitable branches where appropriate.

5. **Landmarks and navigation readability**
   - major silhouettes;
   - visible orientation anchors;
   - route-signaling architecture/nature;
   - sightline goals so the player can understand where they are going without relying only on UI arrows.

6. **Elevation / HD-2D composition**
   - foreground, midground and background layering;
   - vertical changes;
   - bridges, ledges, stairs, drops and overlooks;
   - camera-facing composition needs;
   - occlusion rules and readability at gameplay scale.

7. **Combat-space plan**
   - encounter-capable zones;
   - boss/Hunt arena footprints where required;
   - spaces that must remain readable for a four-character party and enemy formations;
   - authored no-combat or protected spaces.

8. **Traversal and gating mechanics**
   - locks, switches, doors, lifts, ladders, environmental gates and one-way drops;
   - chapter-state changes;
   - shortcuts opened from the far side;
   - revisit-state differences where applicable.

9. **Interaction placement**
   - treasure/reward nodes;
   - lore/interactables;
   - save/rest/transition points where applicable;
   - quest objects and authored event triggers.

10. **Pacing targets**
   - approximate first-pass traversal time;
   - combat-to-exploration rhythm;
   - spacing between landmarks and encounters;
   - expected revisit burden.

11. **Environment kit requirements**
   - terrain/material families;
   - architecture kit;
   - vegetation/props;
   - lighting/weather state;
   - unique hero assets;
   - reusable modular pieces.

12. **AI/environment-generation handoff**
   - canonical layout diagram/blockout;
   - written area purpose;
   - required landmarks and forbidden changes;
   - visual/style packet tied to the approved Diyse benchmark set;
   - negative constraints;
   - collision/navigation expectations;
   - export/import assumptions for the production engine.

## Scope inventory

This stream must eventually cover all gameplay-relevant spaces, including:
- Chapter 0 plus Chapters 1–13 mandatory routes;
- persistent towns/hubs and their gameplay-relevant interiors;
- roads, field routes and mountain/forest/canyon approaches;
- mandatory dungeons, facilities and ancient sites;
- all six Character Quest routes/sites;
- ordinary Side Quest areas that require unique or modified layouts;
- Regional Hunt sites;
- Major Hunt approaches/arenas where not fully contained in an existing area;
- late-war Black Host routes;
- The Deepest City / final-operation route and Point-of-No-Return spaces.

## Production order

### Phase A — Area inventory — COMPLETE ENOUGH TO BEGIN MAPPING
Current inventory:
> `PLAYABLE_AREA_INVENTORY_WORKING.md`

The inventory now separates:
- persistent base maps;
- mandatory chapter route/dungeon packets;
- Character Quest sites;
- Side Quest reuse/state variants;
- Regional Hunt branches/arenas;
- Major Hunt destinations;
- high-priority stateful reuse requirements.

Current audit result:
> no production area currently has an approved L3 build-ready topology in repo authority.

### Phase B — Layout blueprints — STARTED
Map each area before asking an environment generator to invent the finished scene.

The blueprint is the canon-constrained source. An AI may beautify/build from it, but must not invent a different route topology, move canonical locations, delete required story spaces, or introduce unsupported geography.

Current first blueprint:
> `AREA_LAYOUTS/BLUEPRINT_001_CH00_CONVOY_WRECK_ROUTE.md`

Blueprint 001 covers:
- Convoy Road;
- Wreck Field;
- Evacuation / Recovery Line;
- Field Triage Camp;
- Brackenwall transition handoff.

It includes provisional 3D dimensions/coordinates, event sockets, sightlines, pacing targets, transition seams, collision rules and camera-test variants.

### Phase C — Representative vertical-slice build
Before bulk production, build at least:
- one outdoor route/field area;
- one settlement/hub slice;
- one dungeon/facility slice.

Use those to validate scale, camera, collision, readability, encounter spacing and HD-2D layering.

### Phase D — Bulk area production
Only after the layout pipeline and visual benchmark pipeline are proven should the project generate/build the remaining environments at scale.

## Relationship to B01–B11 visual certification

**Layout/blockout work can proceed now in parallel with B00/B01–B11.**

Final environment art generation should not be treated as style-certified until the relevant B01–B11 material/environment benchmarks are approved. The route topology does not need to wait for final texture certification; the final rendered environment does.

## Current technical blockout anchors

Current proof runtime establishes useful test baselines, not final presentation canon:
- exploration is `CharacterBody3D`;
- player capsule height is 1.8 units;
- proof movement speed is 5 units/sec;
- proof camera is approximately 5.5 units up / 7.5 behind, −25° pitch, 60° FOV;
- design viewport is 1920×1080.

Blueprint work may use:
> **1 Godot unit ≈ 1 meter**

as a provisional vertical-slice convention until gameplay testing replaces it.

## AI/tool-selection rule

Do not permanently bind Diyse to one external environment-generation AI in canon documentation.

The generation landscape changes quickly. Keep the area packets tool-agnostic, then use the strongest available tool for the needed stage:
- spatial/blockout assistance;
- environment concepting;
- asset/texture generation;
- 3D or 2.5D scene construction;
- engine integration.

Any external AI output is a production draft until it passes the canonical layout, visual-style and gameplay-readability checks.

## Immediate next deliverable

> **Build/test the Chapter-0 graybox from Blueprint 001.**

The graybox must validate scale, movement, Android touch navigation, camera framing, Wreck Field readability and transition seams before Blueprint 001 is promoted to L3.
