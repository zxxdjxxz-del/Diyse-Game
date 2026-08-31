# Diyse — B01 Original Modular Stone Kit Specification v1

**Status:** ACTIVE B01 PRODUCTION SPEC  
**Style source:** `B01_STONE_STYLE_PASS_CANDIDATE_V1.md`  
**Execution source:** `B01_STONE_EXECUTION_V1.md`

This specification turns the approved B01 stone rendering grammar into a reusable, Diyse-original environment kit.

## 1. Production goal

Build a modular stone family that can support forts, ruins, dungeons, town foundations, bridges, cliffs, courtyards, interiors, and faction variants without redrawing the underlying material language for every map.

The kit must feel hand-authored and irregular while remaining modular enough for practical level construction.

## 2. Core module families

### Walls
- straight wall — clean;
- straight wall — weathered;
- straight wall — damaged;
- half-height wall;
- broken wall end left/right;
- collapsed wall section;
- wall cap clean/damaged;
- narrow parapet;
- thick defensive parapet.

### Corners and joins
- 90° inner corner;
- 90° outer corner;
- T-junction;
- end cap;
- offset join;
- stepped join;
- irregular ruin join.

### Floors and paths
- large floor slab;
- medium paving block group;
- narrow path strip;
- cracked floor;
- moss-edge floor;
- wet/damp floor;
- broken floor edge;
- floor-to-wall transition.

### Vertical structure
- narrow pillar;
- broad pillar/abutment;
- square support;
- ruined support;
- carved support variant;
- arch spring/base pieces.

### Arches and openings
- narrow arch;
- broad arch;
- door surround;
- gate surround;
- broken arch;
- lintel/header;
- sill/base.

### Height change
- single stair step;
- short stair flight;
- long stair flight;
- landing;
- ramp;
- broken stair;
- ledge edge;
- cliff/retaining edge.

### Damage and scatter
- small rubble cluster;
- medium rubble cluster;
- collapsed masonry pile;
- loose stone singles;
- fractured corner insert;
- chipped edge insert;
- crack/deformation overlays kept sparse and non-repetitive.

## 3. Baseline material variants

Every major structural family should support these material states where useful:

1. **Neutral cut stone** — baseline.
2. **Weathered stone** — softened edges, staining, limited wear.
3. **Damaged stone** — heavier fracture/line clustering and displacement.
4. **Mossy stone** — growth from joints, moisture pockets, base contact.
5. **Wet/damp stone** — darker body values and restrained specular response.
6. **Ancient carved stone** — selective ornament/carving, not all-over decoration.
7. **Etched/ritual stone** — inactive hand-drawn marks with optional emissive active state.

## 4. Shape grammar

- Structural mass reads first.
- Stone grouping reads second.
- Damage reads third.
- Surface microtexture reads last.
- Perfect brick grids are avoided except where a specific culture intentionally uses them.
- Repetition must be disguised by block-group variation, rotated/offset inserts, damage variants, vegetation, and lighting—not by random texture noise.

## 5. Line grammar

### Heavy
Use at:
- silhouettes;
- deep joints;
- undersides;
- broken edges;
- structural compression points;
- focal damage.

### Medium
Use at:
- selected block boundaries;
- important plane changes;
- chipped edges;
- vegetation/stone intersections.

### Light/broken
Use at:
- shallow cracks;
- surface wear;
- light-facing internal edges;
- minor construction marks.

### Never
- uniform outline around every stone;
- uniform mortar black;
- automatic edge-detect inking;
- equal crack density everywhere;
- heavy line clutter across walkable surfaces.

## 6. Painterly material grammar

Stone faces use broad color/value planes with:
- restrained dry-brush breakup;
- selective mineral staining;
- subtle edge scumble;
- sparse pitting;
- limited warm/cool stone variation;
- no photo-based high-frequency noise dependence.

## 7. Palette baseline

Baseline stone family:
- cool charcoal recess;
- muted neutral gray;
- limited warm earth/ochre variation;
- pale stone highlight;
- deep moss green;
- restrained yellow-green vegetation highlight.

Faction and regional palettes may shift hue/value relationships but should preserve readable structural contrast.

## 8. Lighting-state design

The base material should remain neutral enough for scene lighting.

Test states:
- neutral daylight;
- warm sun;
- cool sky;
- overcast;
- torch/fire;
- magical emissive;
- night/moon.

Persistent deep contact occlusion may remain painted. Strong directional highlights/shadows should come from scene-dependent lighting wherever practical.

## 9. Faction/regional derivative system

Variants should be created by changing controlled layers rather than inventing a new stone style each time.

Possible derivative dimensions:
- block size/rhythm;
- masonry precision;
- palette;
- mortar visibility;
- carving/trim;
- vegetation load;
- damage pattern;
- metal reinforcement;
- banners/signage;
- ritual marking;
- weathering.

### Black Host example
- darker, more severe masonry;
- stricter structural rhythm;
- blackened metal reinforcement;
- sparse crimson focal accent;
- reduced organic growth in maintained military sites;
- heavier damage clusters where structures are war-torn;
- no generic skull/spike overload.

## 10. Minimum gameplay-test subset

Before full kit production, create at least:
- 2 straight wall variants;
- 1 damaged wall;
- 1 inner corner;
- 1 outer corner;
- 1 floor tile family;
- 1 ledge/cap;
- 1 short stair;
- 1 arch/door surround;
- 1 pillar;
- 2 rubble clusters;
- 1 moss transition;
- neutral + warm torch + cool/night lighting tests.

This subset is sufficient to construct a compact proof scene for B01 acceptance.

## 11. Gameplay-test scene requirements

Build one compact environment containing:
- a readable traversal path;
- one elevation change;
- one enclosed wall corner;
- one broken/open ruin edge;
- one arch/opening;
- one moss transition;
- one rubble/damage focal area;
- foreground and background stone layers.

Review at actual field scale and under at least two contrasting lighting conditions.

Pass if:
- route reads before cracks;
- walls/floors/ledges separate instantly;
- chaotic line energy remains visible but subordinate;
- repeated modules do not look stamped;
- moss does not swallow the material read;
- lighting does not contradict painted form;
- the scene feels native to Diyse rather than source-derived.

## 12. Promotion rule

B01 becomes `ACCEPTED` only after this minimum gameplay-test subset is represented in an integration proof and passes the B01 execution checklist.

Once accepted, this stone grammar becomes the first locked section of **Diyse Visual Material Grammar v1**.
