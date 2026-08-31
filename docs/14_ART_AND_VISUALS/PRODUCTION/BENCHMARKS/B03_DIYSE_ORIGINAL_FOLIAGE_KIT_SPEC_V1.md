# Diyse — B03 Original Foliage Kit Specification v1

**Benchmark:** B03 — Tree / Foliage Silhouette  
**Status:** ACTIVE KIT SPECIFICATION  
**Style-pass authority:** `B03_FOLIAGE_STYLE_PASS_CANDIDATE_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## 1. Purpose

This specification converts the approved B03 foliage grammar into a reusable **Diyse-original foliage family**. The final production kit must not depend on copying Map084 tree silhouettes or source-specific canopy patterns.

## 2. Core original tree families

The minimum reusable family contains:

1. **Common Broadleaf** — balanced default forest/town-edge tree.
2. **Old-Growth Broadleaf** — wider trunk, heavier canopy mass, stronger asymmetry and branch exposure.
3. **Narrow Roadside Tree** — slimmer vertical profile for routes and settlement edges.
4. **Wind-Shaped Tree** — directional canopy lean for exposed ridges/plains/coasts.
5. **Dead/Broken Tree** — reduced foliage or bare branches with stronger chaotic line concentration at breaks.
6. **Young Tree / Sapling** — simplified narrow canopy and lower detail density.
7. **Dense Canopy Cluster** — modular overlapping foliage mass for forest walls/background density.
8. **Icon/Map Canopy** — dedicated compact symbolic version.

## 3. Required silhouette variation

Each production tree must vary through authored structural choices rather than scale/rotation alone.

Variation axes:
- trunk lean;
- crown width/height ratio;
- dominant canopy side;
- branch exposure;
- lower-canopy openness;
- negative-space placement;
- damage/broken limb state;
- root/base spread;
- canopy tier count.

Avoid procedural-looking repetition. A small family of strong silhouettes is preferable to dozens of weak near-duplicates.

## 4. Modular foliage construction

Where technically practical, original assets should be separable into:
- trunk/base;
- major branch structure;
- canopy cluster groups;
- optional secondary foliage cluster;
- shadow/contact treatment;
- region-specific foliage overlay where needed.

This enables regional variation without redrawing every full tree from zero.

## 5. Render-density tiers

Each important tree family should support at least three presentation tiers.

### Foreground/focal
- full silhouette character;
- 4-value foliage structure;
- selective chaotic line accents;
- visible trunk articulation;
- intentional negative spaces.

### Midground/standard field
- simplified 3–4 value masses;
- reduced line density;
- reduced internal holes;
- stable silhouette at gameplay scale.

### Background
- 2–3 broad masses;
- highly reduced or absent interior lines;
- atmospheric palette shift;
- simplified contour;
- no one-pixel detail.

## 6. Regional adaptation system

Regional variants may alter:
- canopy shape;
- leaf-mass rhythm;
- palette;
- bark hue/value;
- branch exposure;
- density;
- wind/weather damage;
- dryness/wetness;
- seasonal state;
- magical/environmental influence.

Shared grammar must remain:
- strong authored silhouette;
- painterly canopy massing;
- selective chaotic line weight;
- intentional negative space;
- clean alpha edge;
- gameplay readability.

## 7. Material family variants

At minimum, the common broadleaf system should permit:
- healthy green;
- deep forest/shade;
- dry/stressed;
- autumn/warm-season variant where regionally appropriate;
- dead/bare;
- wet/rain-darkened;
- magical contamination/influence only where story/location canon supports it.

Do not make every biome a palette swap; silhouette and growth pattern should carry regional identity too.

## 8. Ground-contact grammar

Tree bases must integrate with environment art through:
- roots or trunk flare;
- contact shadow;
- sparse leaf litter/grass/moss cluster where appropriate;
- terrain-value transition;
- no bright alpha halo at ground contact.

Tree bases should not obscure critical path boundaries unless deliberately used as an occluding foreground layer.

## 9. Lighting behavior

Base foliage art should remain neutral enough for HD-2D scene lighting.

Required test states:
- neutral daylight;
- warm side/sunset light;
- cool sky/night light.

Optional scene states:
- torch/fire spill;
- magical glow;
- fog-heavy low contrast.

Avoid permanently baked directional highlights that conflict with scene-light direction.

## 10. Alpha and export rules

Final sprite/texture exports must:
- preserve clean alpha;
- avoid dark/pale matte contamination;
- remove tiny unstable silhouette spikes;
- avoid dense tiny holes;
- downscale cleanly;
- remain stable during camera movement and scaling.

If an edge detail vanishes or flickers at normal gameplay distance, simplify it in the source artwork rather than relying on runtime filtering to hide it.

## 11. Naming family

Use clear semantic naming consistent with `../VISUAL_ASSET_NAMING_AND_VERSIONING.md`.

Suggested logical IDs:
- `tree_broadleaf_common`
- `tree_broadleaf_oldgrowth`
- `tree_roadside_narrow`
- `tree_windshaped`
- `tree_dead_broken`
- `tree_sapling`
- `foliage_canopy_cluster`
- `icon_tree_canopy`

Variant suffixes should identify region/state rather than arbitrary version-only names.

## 12. Acceptance gate for original foliage kit

The original kit is production-ready only when:
- at least four full-size silhouettes are clearly distinct;
- all still read as the same Diyse visual family;
- alpha edges are clean;
- character hierarchy is preserved;
- foreground/midground/background tiers are coherent;
- lighting states do not break the material;
- icon treatment matches the family without being a blind downscale;
- the kit can build forest, roadside, settlement-edge, and background canopy scenes without obvious repetition.

## 13. Production decision

B03 style direction is approved. This document now controls the first original foliage-family build used for the B03 gameplay proof.