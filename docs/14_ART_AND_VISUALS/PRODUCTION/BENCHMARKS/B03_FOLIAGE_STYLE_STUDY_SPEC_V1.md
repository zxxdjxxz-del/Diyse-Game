# Diyse — B03 Foliage Style Study Specification v1

**Benchmark:** B03 — Tree / Foliage Silhouette  
**Status:** STYLE STUDY SPEC LOCKED / VISUAL PASS PENDING  
**Execution authority:** `B03_FOLIAGE_EXECUTION_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## 1. Purpose

B03 establishes the first reusable Diyse foliage grammar. The source is useful because the main Map084 tree sheet already exposes the exact problem we need to solve: large transparent silhouettes, broad foliage masses, simple trunks, internal negative-space holes, and multiple variants that must still read as one family.

The final target is not a direct repaint of Map084. The target is a **Diyse-original foliage language** that can be applied across broadleaf forest trees, roadside trees, old-growth trees, dead trees, shrubs, canopy clusters, and map/icon foliage.

## 2. Source-specific read

The inspected 1024×1024 RGBA source sheet contains four tall variants arranged left-to-right. Each variant is built from a narrow trunk supporting three primary vertical canopy tiers. The canopy is unusually elongated rather than round, with large pointed organic protrusions, deep silhouette notches, and several transparent negative-space holes through the foliage.

The inspected 128×128 RGBA icon-tree source uses a compact, nearly circular canopy cluster with dense painterly internal green value breakup and no visible trunk.

These two source forms are functionally different and therefore useful together:
- the tall tree tests field-scale silhouette, trunk hierarchy, alpha stability, and negative space;
- the icon tree tests whether the same foliage family remains recognizable after radical simplification and compression.

## 3. Diyse target silhouette

The field tree must read first as one authored organic silhouette, not as a stack of leaf blobs.

Target requirements:
- retain a strong vertical read without copying the exact Map084 contour;
- use 3–6 major canopy masses for a standard tree;
- allow one dominant asymmetry so left/right balance does not feel procedural;
- use selective silhouette cuts and holes, but fewer and more intentional than the source;
- reserve the most complex contour activity for one or two focal zones;
- keep the lower canopy sufficiently open that the trunk/base and route relationship remain readable.

### Negative-space rule

Transparent holes inside foliage must be designed as shapes, not left as accidental noise.

Use them to:
- show branch structure;
- break large dark masses;
- create depth between canopy layers;
- reveal sky/light selectively;
- establish regional silhouette identity.

Avoid peppering the canopy with many tiny alpha holes, because those become shimmer/noise at gameplay scale.

## 4. Foliage line grammar

Foliage uses the same chaotic-variable-line family as B01 stone, but with a softer organic hierarchy.

### Heavy line

Use sparingly at:
- underside of major canopy masses;
- trunk-to-canopy contact;
- deep branch forks;
- broken limbs;
- the darkest one or two silhouette turns on foreground trees.

### Medium line

Use at:
- selected canopy overlap boundaries;
- trunk plane changes;
- branch emergence points;
- major folds of foliage mass.

### Fine/broken line

Use at:
- light-facing outer edges;
- a few internal leaf-group accents;
- bark texture marks;
- small branch suggestions;
- dry-brush edge breakup.

### Hard limits

- no uniform black outline around the full tree;
- no equal line weight around every canopy lobe;
- no leaf-by-leaf inking on normal field assets;
- no random scratch field across the canopy;
- no deep-black internal maze that competes with character silhouettes.

The correct read is **ink rhythm carried by organic mass**, not “tree with a comic outline.”

## 5. Painterly canopy structure

Build the tree in this order:

1. full silhouette;
2. 3–6 broad canopy masses;
3. deep overlap shadows;
4. local-color mids;
5. restrained light-catching planes;
6. trunk/branch support;
7. selective chaotic line accents;
8. minimal edge texture.

The painterly masses must work before any line layer is added.

## 6. Value and color baseline

### Four foliage values

- **F0 deep occlusion:** very dark cool green; limited coverage;
- **F1 shadow mass:** dark muted green;
- **F2 local foliage:** dominant controlled mid-green;
- **F3 light plane:** restrained olive/yellow-green or region-specific equivalent.

### Trunk

- muted brown/gray family;
- one dominant shadow plane;
- one restrained light plane;
- sparse bark marks;
- lower contrast than a player character at the same camera distance.

### Color grouping rule

Hue/value shifts follow canopy masses, not individual leaves. A single tree should not read as confetti.

## 7. Depth variants

B03 must lock three render-density tiers.

### Foreground / focal tree

- strongest silhouette accents;
- full 4-value structure;
- visible but selective interior line rhythm;
- small bark/edge details allowed;
- largest alpha notches may remain.

### Midground / normal exploration tree

- simplified 3–4 value structure;
- fewer interior lines;
- fewer alpha holes;
- broad canopy masses dominate;
- silhouette remains strong.

### Background tree

- 2–3 value masses;
- minimal or no internal linework;
- simplified contour;
- atmospheric hue/value shift;
- no tiny holes or chatter.

Depth should be created by simplification and atmosphere, not blur alone.

## 8. Alpha-edge acceptance standard

At the final working scale:
- transparent edges must not carry black or pale fringe;
- alpha must remain stable under scaling and camera movement;
- silhouette notches smaller than the gameplay read threshold must be removed;
- edge brush breakup should cluster into readable groups;
- downscaled versions should not show sparkling one-pixel protrusions.

The benchmark should be rejected if a still image looks attractive at 100% but shimmers during movement.

## 9. Icon-tree grammar

The 128px-class icon/map canopy should not be a simple downscale of the full field tree.

Build it as a dedicated compact symbol:
- near-circular or region-appropriate canopy silhouette;
- 4–7 large lobes;
- 3 major value masses;
- one deep central/recess cluster;
- one restrained highlight cluster;
- no trunk unless function requires it;
- almost no interior linework;
- optional irregular dark contour accents only at selected silhouette turns.

The icon and field tree should feel related by palette, mass rhythm, and edge language rather than identical geometry.

## 10. Required visual board layout

When a fresh B03 visual pass is generated, it must contain **foliage only** and should be labeled clearly enough that it cannot be confused with B01.

Required panels:

1. `B03 — FOLIAGE / TREE SILHOUETTE` title.
2. Source-functional analysis silhouettes.
3. Diyse target full tree in neutral light.
4. Too smooth / target / too noisy silhouette comparison.
5. Too clean / target / too heavy line-density comparison.
6. Alpha-edge close-up.
7. Foreground / midground / background density test.
8. Player-scale comparison.
9. Neutral-day / warm-light / cool-night lighting test.
10. 128px-class icon-tree interpretation.
11. Diyse-original tree-family preview showing at least 4 distinct silhouettes.

No stone-atlas or masonry panels should appear on the B03 board.

## 11. Gameplay-scale pass criteria

B03 visually passes only if:
- canopy reads before small detail;
- character silhouette remains visually dominant nearby;
- trunk location is obvious;
- route/walkable edge is not obscured by unnecessary low foliage;
- transparent holes remain stable;
- no alpha halo is visible;
- the same art language survives foreground, midground, and background simplification;
- the icon tree is clearly from the same family;
- line energy is recognizably Diyse without making foliage look black or scratchy.

## 12. Original Diyse tree-family target

After B03 style approval, build a specification for these original families:
- common broadleaf;
- old-growth broadleaf;
- narrow roadside tree;
- wind-shaped tree;
- dead/broken tree;
- young tree/sapling;
- dense canopy cluster;
- isolated icon/map canopy.

Regional variants may change:
- silhouette rhythm;
- canopy density;
- bark shape;
- palette;
- leaf mass shape;
- weather damage;
- seasonal treatment;
- local magical/environmental influence.

They should not abandon the shared foliage grammar.

## 13. Decision

**B03 source analysis and style-study specification are complete.**

Current promotion state:

`SOURCE ANALYSIS → STYLE STUDY SPEC LOCKED → VISUAL STYLE-PASS PENDING`

The recent repeated B01 stone image generations are explicitly **not** B03 results and must not be used as foliage authority.
