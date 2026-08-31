# Diyse — B03 Foliage Benchmark Execution v1

**Benchmark:** B03 — Tree / Foliage Silhouette  
**Status:** SOURCE ANALYSIS COMPLETE / STYLE STUDY READY  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Benchmark authority:** `../STYLE_BENCHMARK_SET_V1.md`  
**Conversion pipeline:** `../ASSET_STYLE_CONVERSION_PIPELINE.md`

## 1. Source record

**Reference family:** Map084  
**Primary source:** `gt_1_map084_tree_color.tga`  
**Supporting source:** `gt_4_map084_icon_tree_color.tga`  
**Lighting support:** base lighting plus `ra`–`rf` directional states for both tree and icon-tree assets.  
**Provenance lane:** Lane B — license-unverified extracted private/reference source.

### Verified technical observations

Primary tree sheet:
- dimensions: **1024×1024**;
- mode: **RGBA**;
- transparent background is meaningful;
- contains four tall tree variants/silhouettes arranged horizontally;
- foliage is built from broad dark-green masses rather than leaf-level realism;
- trunk remains visually simple and subordinate to canopy mass;
- source palette is strongly green-biased with limited warm trunk color.

Icon tree:
- dimensions: **128×128**;
- mode: **RGBA**;
- compact rounded canopy cluster;
- high-density internal green value breakup;
- no visible trunk in the icon presentation.

## 2. Functional information to preserve

Preserve:
- transparent silhouette behavior;
- clear canopy-vs-trunk separation;
- broad foliage massing;
- overall vertical tree read;
- compatibility with directional lighting states;
- field-scale recognizability;
- icon-scale recognizability for map/minimap/UI use where applicable.

Do not preserve by default:
- exact canopy lobes;
- exact internal green patches;
- exact trunk shape;
- exact source palette;
- exact holes/negative spaces in foliage;
- source-specific highlight placement.

## 3. B03 Diyse foliage grammar — draft lock

### Shape hierarchy

**Level 1 — Full silhouette**  
The tree must read as one strong organic mass first.

**Level 2 — Major canopy clusters**  
Break the crown into 4–8 deliberate foliage masses depending on tree type and scale.

**Level 3 — Branch/trunk anchors**  
Branches should support canopy weight and create selective negative spaces rather than filling the whole tree with visible branch detail.

**Level 4 — Leaf-edge accents**  
Use sparse clustered edge shapes and brush marks; avoid individual-leaf rendering on standard field trees.

## 4. Chaotic variable line weight rules for foliage

Foliage should carry the Diyse line identity without becoming a black cutout.

### Heavy line zones

Use strongest line buildup at:
- major silhouette turns;
- underside canopy overlaps;
- trunk/canopy contact;
- deep branch forks;
- damaged/broken limb areas;
- foreground focal trees.

### Medium line zones

Use medium irregular strokes at:
- selected canopy-cluster boundaries;
- trunk plane changes;
- branch emergence points;
- selective leaf-mass overlaps.

### Light/broken line zones

Use thin/tapered/broken marks at:
- light-facing foliage edges;
- minor branch accents;
- sparse internal leaf-group indications;
- small bark texture marks.

### Explicit limits

- Do not outline every foliage lobe.
- Do not place a uniform black border around the entire tree.
- Do not draw individual leaves across the whole canopy.
- Do not use random scribble as a substitute for mass design.
- Do not let line density destroy transparent silhouette clarity.

## 5. Alpha-edge rule

B03 must establish a clean alpha standard for organic assets.

Requirements:
- no dark matte fringe around transparent edges;
- no bright halo from premultiplied-alpha mismatch;
- edge breakup must be deliberate, not noisy pixel chatter;
- small silhouette notches should support organic rhythm rather than create shimmering detail;
- at gameplay scale, the outer tree shape must remain stable under movement/camera scaling.

## 6. Value structure

Use 4 broad foliage value bands:

1. deep canopy occlusion;
2. shadow foliage mass;
3. dominant mid-green/local color;
4. restrained light-catching foliage plane.

Trunk/branch values should separate from foliage but not become more visually dominant than the canopy.

Avoid both:
- flat one-green foliage;
- noisy high-frequency mottling everywhere.

## 7. Color direction

Baseline forest foliage should use:
- deep cool green in recesses;
- muted natural mid-green as body color;
- restrained olive/yellow-green light accents;
- limited warm/brown trunk colors;
- occasional regional hue shifts where appropriate.

Color should cluster by canopy mass, not random leaf-to-leaf variation.

## 8. Painterly surface rule

Foliage texture should rely on:
- broad opaque/soft brush masses;
- selective dry-brush breakup near cluster edges;
- limited internal texture;
- controlled overlap shadows;
- occasional sharper marks near focal edges.

The canopy should look illustrated and painterly before the line layer is added.

## 9. Tree-vs-character hierarchy

At normal exploration scale:
- player silhouette must remain stronger than ordinary tree internal detail;
- tree silhouettes may be bold, but interior line density should stay lower than character portraits/battle art;
- foreground trees can carry heavier edge treatment than background trees;
- background foliage should simplify further with depth.

## 10. Required B03 style-study outputs

Before B03 can become STYLE-PASS:

1. **Full tree neutral-light study** — tall field tree with grouped canopy masses.
2. **Silhouette comparison** — too smooth / target / too noisy.
3. **Line-density comparison** — too clean / target / too heavy.
4. **Alpha-edge close-up** — verify no fringe/halo and controlled edge breakup.
5. **Gameplay-scale preview** — tree beside representative field-character scale.
6. **Depth test** — foreground, midground, background versions of the same foliage grammar.
7. **Icon-tree conversion** — compact 128px-class canopy that retains the same family identity.
8. **Lighting preview** — at minimum neutral daylight + cool/night or warm sun.

## 11. Runtime readability test

At field scale the viewer should immediately read:
- canopy silhouette;
- trunk position;
- major negative spaces;
- foreground/background depth;
- tree versus walkable route;
- tree versus character.

If individual leaf marks become the first thing noticed, detail density is too high.

## 12. Originalization target

B03 is reference-led. Final production foliage should become Diyse-original tree families rather than a direct repaint of Map084.

The approved grammar should later support original modules such as:
- broadleaf forest tree;
- old-growth broadleaf;
- narrow roadside tree;
- dead/broken tree;
- scrub/sapling;
- dense canopy cluster;
- isolated icon/map canopy;
- region-specific tree families.

Regional identity should change silhouette, canopy rhythm, palette, bark, growth pattern, damage, and seasonal/weather response while preserving the common Diyse foliage rendering grammar.

## 13. B03 acceptance checklist

B03 passes only when:

- [ ] full silhouette reads before internal leaf detail;
- [ ] canopy is grouped into deliberate masses;
- [ ] chaotic line weight is visible but selective;
- [ ] no uniform black outline surrounds the asset;
- [ ] alpha edges remain clean;
- [ ] no shimmering/noisy silhouette at gameplay scale;
- [ ] painterly masses remain visible;
- [ ] trunk supports rather than competes with canopy;
- [ ] foreground/midground/background simplification is coherent;
- [ ] icon-scale version still feels like the same visual family;
- [ ] source/reference provenance remains recorded;
- [ ] grammar can be rebuilt into Diyse-original tree families.

## 14. Production decision

**B03 is ready for visual style-study generation.**

Do not mark it STYLE-PASS until the alpha-edge, silhouette, line-density, gameplay-scale, and depth tests have been visually reviewed.
