# Diyse — Visual Style Benchmark Set v1

**Status:** ACTIVE BENCHMARK AUTHORITY  
**Style target:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion pipeline:** `ASSET_STYLE_CONVERSION_PIPELINE.md`  
**Asset inventory:** `ASSET_LIBRARY/README.md`

This benchmark set exists to prove the active Diyse visual style on a deliberately small range of representative materials before attempting broad conversion of the 3,214-file environment library.

> **Do not bulk-convert the library until this benchmark set reads as one coherent game.**

The benchmark target is:

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight**

The benchmark is not a contest to preserve the source look. It is a test of whether different asset categories can be translated into a single Diyse-native visual language while retaining gameplay readability.

---

## 1. Benchmark Principles

Each benchmark must test a different production problem:

- broad architecture/terrain readability;
- wood and interior material treatment;
- foliage and transparent-edge treatment;
- animated vegetation coherence;
- water motion language;
- fire/light-emitter treatment;
- cave/subterranean material language;
- high-status interior ornament control;
- ritual/magic visual language;
- CC0 3D-prop stylization;
- a fully original Diyse faction piece that proves the style is not dependent on source material.

Every result is reviewed at both **source/detail scale** and **actual gameplay scale**.

---

## 2. Locked Benchmark Source Set

### B01 — Stone / Fortified Exterior

**Reference family:** Map086  
**Primary source:** `gt_0_map086_map_color.tga`  
**Supporting source:** `gt_0_map086_map_lighting.tga`

**Why this asset:** relatively simple gray fortified/ruin material family; useful for proving that chaotic line energy can be added without turning stone into visual noise.

**Target treatment:**
- larger, cleaner stone masses;
- deliberate irregular block edges;
- sparse broken ink accents on fractures and overlaps;
- painterly value grouping;
- reduced micro-noise;
- strong silhouette and edge readability.

**Pass test:** reads as mature hand-inked fantasy stone at gameplay distance without looking comic-book outlined.

---

### B02 — Wood / Rustic Interior

**Reference family:** Map093  
**Primary source:** `gt_0_map_093_map_color.tga`  
**Supporting pieces:** `gt_2_map_093_boardf_color.tga`, `gt_3_map_093_boardb_color.tga`

**Why this asset:** clear timber/stone workshop language with boards and display surfaces.

**Target treatment:**
- broad stylized wood grain;
- darker clustered line weight at joints, cracks, nail points and overlaps;
- clean material separation between timber, stone and display surfaces;
- restrained grime;
- hand-authored asymmetry.

**Pass test:** wood feels illustrated and tactile without becoming noisy or photoreal.

---

### B03 — Tree / Foliage Silhouette

**Reference family:** Map084  
**Primary source:** `gt_1_map084_tree_color.tga`  
**Supporting source:** `gt_4_map084_icon_tree_color.tga`

**Why this asset:** isolated transparent vegetation makes edge treatment easy to judge.

**Target treatment:**
- grouped foliage masses rather than leaf-by-leaf realism;
- irregular broken contour line weight concentrated at major silhouette turns;
- darker trunk/branch clusters;
- painterly internal value masses;
- clean alpha edges.

**Pass test:** tree reads immediately at field scale and still carries the same line-energy family as character art.

---

### B04 — Animated Vegetation

**Reference family:** Map081  
**Primary sequence:** `gt_1_map081_grass_color_0.tga` through `gt_1_map081_grass_color_7.tga`

**Why this asset:** tests whether the style survives animation without line boil becoming distracting.

**Target treatment:**
- clustered blade/tuft shapes;
- selective variable-line accents;
- consistent line-density across frames;
- controlled secondary motion;
- no frame-to-frame random redraw noise.

**Pass test:** motion feels organic and illustrated, not flickery.

---

### B05 — Water + Splash

**Reference family:** Map111  
**Primary sequence:** `gt_1_map111_watersurface_color_0.tga` through `gt_1_map111_watersurface_color_29.tga`  
**Secondary sequence:** `gt_4_map111_watersplash1_color_0.tga` through `gt_4_map111_watersplash1_color_7.tga`

**Why this asset:** tests a long loop plus a short impact effect in one material family.

**Target treatment:**
- broad luminous water bands;
- graphic ripple shapes;
- sparse dark line accents only at selected overlaps/edges;
- painterly color movement;
- sharper chaotic-line energy in splash impact than in calm surface water.

**Pass test:** water remains fluid and atmospheric while the splash carries clear seinen-style impact energy.

---

### B06 — Fire / Light Emitter

**Reference family:** Map092  
**Primary sequence:** `gt_5_map092_fire_color_0.tga` through `gt_5_map092_fire_color_5.tga`  
**Secondary sequence:** `gt_6_map092_fireplace_color_0.tga` through `gt_6_map092_fireplace_color_5.tga`

**Why this asset:** tests emissive rendering and whether chaotic lines can support light rather than muddy it.

**Target treatment:**
- strong graphic flame silhouettes;
- tapered ink-like tongues only at darker flame edges;
- bright interior kept mostly line-free;
- restrained bloom compatibility;
- warm light spill designed for HD-2D compositing.

**Pass test:** reads as powerful illustrated fire, not stock particle fire or photoreal flame footage.

---

### B07 — Cave / Subterranean Material

**Reference family:** Map109  
**Primary source:** `gt_0_map109_map_color.tga`

**Why this asset:** cave assets are a major reusable family and easily become muddy when over-textured.

**Target treatment:**
- large rock planes and ledges first;
- sparse fracture lines with irregular weight;
- deep ink buildup only in crevices/occlusion;
- painterly moss/mineral breakup;
- clear traversal surfaces.

**Pass test:** dark atmosphere without losing walkable-space readability.

---

### B08 — High-Status Interior

**Reference family:** Map104  
**Primary source:** `gt_0_map104_map_color.tga`  
**Supporting pieces:** `gt_2_map104_curtain_color.tga`, `gt_4_map104_bed_color.tga`, `gt_5_map104_flower_color.tga`

**Why this asset:** tests ornament, fabric, furniture and luxury without drifting into glossy gacha rendering.

**Target treatment:**
- controlled ornament density;
- richer but restrained palette;
- variable line accents on seams, folds, carved edges and overlaps;
- soft painterly fabrics;
- sharp selective metal/detail highlights;
- cinematic light-shaft compatibility.

**Pass test:** luxurious and mature, never plastic or over-rendered.

---

### B09 — Ritual / Magic Surface

**Reference family:** Map116  
**Primary source:** `gt_0_map116_map_color.tga`

**Why this asset:** directly tests the game's magical graphic language.

**Target treatment:**
- cleaner original sigil hierarchy;
- controlled asymmetry and hand-drawn irregularity;
- variable line weight in inactive marks;
- brighter graphic treatment when active;
- selective glow rather than blanket bloom;
- clear central focal read.

**Pass test:** feels ancient, dangerous and authored rather than like a generic stock magic circle.

---

### B10 — Verified CC0 Prop Cluster

**Source:** Quaternius Fantasy Props MegaKit — verified CC0.

**Required representative props:**
- `Barrel`
- `Chair_1`
- `Lantern_Wall`
- `Workbench`

**Why these assets:** tests hard/soft wood, metal, furniture silhouette, emissive prop treatment, and direct final-use stylization on assets with clean provenance.

**Target treatment:**
- preserve useful geometry where appropriate;
- repaint/rebuild textures to Diyse material language;
- simplify small surface noise;
- introduce selective inked edge treatment through textures/shaders where it reads cleanly;
- avoid uniform black outlines around entire 3D models;
- test compatibility with scene lighting.

**Pass test:** the props feel native beside painterly 2D/HD-2D environment art rather than obviously imported low-poly assets.

---

### B11 — Fully Original Diyse Faction Piece

**Source lane:** Diyse-original. No extracted-source tracing or direct paint-over.

**Benchmark subject:** **Black Host fortified wall/gate module**.

**Purpose:** prove that the style can generate an original production asset without leaning on the extracted library.

**Design requirements:**
- severe authoritarian silhouette;
- dark metal and blackened masonry language;
- disciplined repeating structural rhythm interrupted by controlled damage/wear;
- crimson accent used sparingly;
- oppressive vertical emphasis;
- chaotic variable line weight concentrated at damage, seams, shadows and focal edges;
- no generic skull/spike overload;
- must remain modular enough to build multiple Black Host locations.

**Pass test:** instantly reads as Black Host while still belonging to the same visual system as B01–B10.

---

## 3. Required Output for Each Benchmark

Each benchmark should produce, where technically applicable:

1. **Source/reference capture** — private when provenance requires it.
2. **Style study** — palette, shape grouping, line-density decisions.
3. **STYLE-PASS asset** — first coherent Diyse rendering treatment.
4. **Gameplay-scale preview** — field/battle-size test, not just zoomed art.
5. **Lighting test** — neutral + one dramatic HD-2D scene-light condition.
6. **Notes** — what worked, what failed, and what becomes a repeatable rule.
7. **Provenance tag** — CC0 / private reference / Diyse-original.

Animated systems additionally require:
- loop preview;
- frame-consistency check;
- line-boil/flicker check;
- timing/cadence confirmation.

---

## 4. Shared Benchmark Palette/Rendering Rules

The benchmark set must look related even though the subjects differ.

### Value
- 3–5 broad value masses per material/focal object before micro-detail;
- deep blacks reserved for focal occlusion, impact and line clusters;
- avoid crushing entire environments into black.

### Line
- visible thick-to-thin variation;
- broken contours allowed;
- line density highest near weight, overlap, tension and damage;
- bright/emissive cores lose linework rather than gaining it;
- environment line treatment remains lighter than portrait/character treatment.

### Texture
- broad painterly material breakup;
- no photo-noise dependence;
- no uniform sharpening pass masquerading as stylization;
- microdetail must disappear gracefully at gameplay scale.

### Color
- world base colors controlled and somewhat restrained;
- focal accents richer;
- magic/emissive effects may exceed environmental saturation;
- avoid global brown-gray mud and avoid rainbow saturation.

### HD-2D integration
- test foreground/midground/background separation;
- test local atmospheric haze;
- test directional light compatibility;
- bloom is selective and never used to hide weak art;
- silhouettes must survive depth-of-field treatment.

---

## 5. Benchmark Acceptance Gate

Bulk conversion may begin only when the benchmark set passes these questions:

- Do all eleven benchmarks look like they came from the same game?
- Is chaotic line weight visible without damaging readability?
- Are characters/props/environment materials clearly separated by line-density hierarchy?
- Do dark scenes remain navigable?
- Do animated textures avoid distracting line boil?
- Do emissive assets remain bright and clean?
- Do CC0 props stop looking like imported generic low-poly assets?
- Does the original Black Host module feel as convincing as the converted/reference-led pieces?
- Does the style survive actual field/battle scale?
- Can the treatment be repeated without requiring a unique art process for every asset?

If any answer is **no**, adjust the style implementation before broad conversion.

---

## 6. Production Order

Recommended sequence:

1. **B01 Stone** — establishes environmental line/noise baseline.
2. **B03 Tree** — establishes alpha-edge and organic line grammar.
3. **B10 CC0 props** — establishes 3D/2D integration.
4. **B08 High-status interior** — tests material variety and ornament.
5. **B07 Cave** — tests dark-scene readability.
6. **B05 Water** — tests long-loop stylization.
7. **B06 Fire** — tests emissive/VFX treatment.
8. **B04 Grass** — tests animated organic line stability.
9. **B09 Ritual** — locks magic/sigil language.
10. **B02 Rustic interior** — validates everyday lived-in materials.
11. **B11 Original Black Host module** — final proof that the style has become Diyse-native rather than source-dependent.

---

## 7. Result of This Benchmark Pass

Once accepted, the benchmark outcomes become the source for a **Diyse Visual Material Grammar v1** covering:

- stone;
- wood;
- metal;
- cloth;
- foliage;
- caves/minerals;
- water;
- fire/emissives;
- magical surfaces;
- luxury interiors;
- faction architecture;
- 3D prop integration;
- line-density rules by asset class and scale.

That material grammar should control later batch conversion of the larger environment library.
