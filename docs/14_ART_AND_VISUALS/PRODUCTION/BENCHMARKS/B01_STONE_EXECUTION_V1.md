# Diyse — B01 Stone Benchmark Execution v1

**Benchmark:** B01 — Stone / Fortified Exterior  
**Status:** SOURCE ANALYSIS COMPLETE / STYLE STUDY READY  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Benchmark authority:** `../STYLE_BENCHMARK_SET_V1.md`  
**Conversion pipeline:** `../ASSET_STYLE_CONVERSION_PIPELINE.md`

## 1. Source Record

**Reference family:** Map086  
**Primary source:** `gt_0_map086_map_color.tga`  
**Supporting source:** `gt_0_map086_map_lighting.tga`  
**Additional lighting states present:** `ra`, `rb`, `rc`, `rd`, `re`, `rf`  
**Shadow asset:** `gt_2_map086_shadow_color.tga`  
**Provenance lane:** Lane B — license-unverified extracted private/reference source.

### Verified technical observations

- Primary atlas dimensions: **2048×2048**.
- Primary source mode: **RGB**; transparency is not carried by the main atlas itself.
- The atlas contains pre-composed irregular fortified/ruin stone-and-ground sections rather than one clean seamless material tile.
- Major visual families present:
  - pale gray masonry;
  - warmer tan/khaki stone;
  - darker gray fracture/crevice structure;
  - moss/grass ground masses;
  - long wall/ledge strips;
  - curved/angled ruin pieces;
  - scattered rock/ground clusters.
- Lighting is handled separately, with a base lighting pass plus six directional/rotation states.

## 2. Functional Information To Preserve

The benchmark must preserve the useful **function** of the source family without preserving its specific source appearance as the final Diyse identity.

Preserve:
- readable wall/ledge boundaries;
- clear stone-vs-ground separation;
- broad light-facing versus recessed planes;
- irregular ruin geometry;
- compatibility with separate directional lighting states;
- recognizable transition between moss/ground and masonry;
- modular use at gameplay camera distance.

Do not preserve by default:
- exact crack drawings;
- exact individual stone shapes;
- exact moss patterns;
- exact warm/gray color distribution;
- exact source-specific edge treatment;
- exact decorative arrangement of atlas pieces.

## 3. B01 Diyse Stone Grammar — Draft Lock

This benchmark establishes the first repeatable environment-material rule for Diyse.

### Shape hierarchy

**Level 1 — Structural mass**  
Walls, ledges, floor shelves, and ruin slabs must read first as large connected forms.

**Level 2 — Stone grouping**  
Each structural mass should break into deliberately uneven block/rock groups. Avoid uniform brick grids unless a specific culture or faction requires them.

**Level 3 — Fractures and wear**  
Use a limited number of decisive cracks, chipped corners, compression lines, and displaced stones.

**Level 4 — Microtexture**  
Keep extremely sparse. Surface grain should support value/material breakup, not become visual noise.

## 4. Chaotic Variable Line Weight Rules For Stone

The B01 line treatment should become the baseline for ordinary environment masonry.

### Heavy line zones

Use the darkest/heaviest line buildup at:
- deep crevices;
- underside overlaps;
- broken wall silhouettes;
- compressed block joints;
- foreground damage clusters;
- major corners where two planes separate;
- occasional focal cracks.

### Medium line zones

Use medium irregular strokes at:
- selected block boundaries;
- chipped edges;
- moss/stone intersections;
- plane changes important to form readability.

### Light/broken line zones

Use thin, tapered, partially missing lines at:
- shallow fractures;
- upper/light-facing edges;
- interior stone texture;
- minor wear.

### Explicit limits

- Do **not** outline every stone.
- Do **not** use a uniform black contour around every atlas piece.
- Do **not** make every crack equally dark.
- Do **not** fill bright stone planes with hatching.
- Do **not** apply an automatic comic-ink filter.

The intended read is **hand-inked seinen environment art**, not western comic-book masonry.

## 5. Value Structure

Target **four broad value groups** before small detail:

1. **Deep occlusion / ink cluster** — reserved darkest value.
2. **Shadow stone** — cool/dark body plane.
3. **Base stone** — dominant mid-value.
4. **Light-facing stone** — restrained highlight plane.

Moss/grass should form its own broad color family but remain compatible with the same value hierarchy.

Avoid extreme black coverage. Dark lines should punctuate form rather than consume the asset.

## 6. Color Direction

B01 should not become a globally desaturated gray wall.

Recommended family:
- cool charcoal-gray recesses;
- muted neutral/cool gray stone base;
- restrained warm ochre/earth variation on selected stones;
- deep natural moss green;
- subdued yellow-green light catching vegetation;
- very limited high-value pale stone accents.

Color variation should occur in **large grouped patches**, not random per-stone rainbow variation.

## 7. Painterly Surface Rule

Stone surfaces should use:
- broad soft brush/value transitions inside planes;
- occasional dry-brush/chalk-like breakup;
- selective edge scumbling;
- simplified mineral staining;
- restrained moss intrusion;
- very limited grain/noise.

The painterly layer carries material richness. The chaotic lines carry structure, weight, and damage.

## 8. Required B01 Style Study Outputs

Before B01 can be marked STYLE-PASS, create the following:

1. **Neutral stone swatch** — representative wall/ledge section with no dramatic scene light.
2. **Broken ruin swatch** — stronger damage and chaotic-line clustering.
3. **Moss transition swatch** — stone-to-ground/vegetation boundary.
4. **Gameplay-scale preview** — demonstrate that the line treatment survives normal field camera scale.
5. **Dramatic-light preview** — directional side light with atmospheric HD-2D treatment.
6. **Line-density comparison** — one intentionally too-clean version, target version, and intentionally too-heavy version to establish the usable middle.

## 9. Runtime Readability Test

At gameplay scale, the viewer should still immediately distinguish:
- vertical wall from horizontal/walkable surface;
- foreground ledge from background masonry;
- intact masonry from damaged ruin;
- moss/grass from stone;
- major path edge from decorative fracture.

If the linework makes individual rocks more noticeable than the route or structural form, line density is too high.

## 10. HD-2D Lighting Compatibility

The stone base art should remain usable under multiple scene lights.

Base texture rules:
- do not bake an extreme single-direction shadow into every stone;
- reserve strongest occlusion for contact/deep crevice areas;
- keep top-facing planes sufficiently neutral for directional lighting passes;
- avoid painted highlights so strong that alternate `ra`–`rf` lighting feels contradictory.

For the eventual Diyse-native set, prefer separating persistent painted material information from scene-dependent lighting wherever practical.

## 11. Originalization Target

B01 is a reference-led benchmark, not permission to make the final Diyse stone kit a direct repaint of Map086.

The approved visual grammar should later be rebuilt into Diyse-original modular components such as:
- straight wall segment;
- broken wall segment;
- corner;
- ledge edge;
- collapsed edge;
- ground-to-wall transition;
- mossy transition;
- rubble cluster;
- narrow pillar/abutment;
- arch/gate-compatible trim.

Those modules can then receive region/faction variants without redrawing the basic grammar from scratch.

## 12. B01 Acceptance Checklist

B01 passes only when all are true:

- [ ] stone reads before cracks;
- [ ] chaotic variable line weight is unmistakable at detail scale;
- [ ] line weight becomes subordinate but still perceptible at gameplay scale;
- [ ] no uniform outline treatment;
- [ ] painterly planes remain visible;
- [ ] moss/ground transitions are readable;
- [ ] no photo-noise dependence;
- [ ] no muddy all-gray result;
- [ ] dramatic lighting does not destroy the base material;
- [ ] source/reference provenance remains recorded;
- [ ] the resulting grammar can be recreated as Diyse-original modular stone.

## 13. Production Decision

**B01 is now ready for visual style-study generation.**

Do not advance to B03 as an accepted benchmark until B01 has at least one STYLE-PASS visual reviewed against this execution sheet.
