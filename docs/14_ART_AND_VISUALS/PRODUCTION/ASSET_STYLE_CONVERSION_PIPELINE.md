# Diyse — Asset Style Conversion Pipeline

**Status:** ACTIVE PRODUCTION GUIDE  
**Locked style target:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Asset inventory authority:** `ASSET_LIBRARY/README.md`

This guide defines how existing source/reference assets, verified CC0 assets, and new original work are converted into the active Diyse visual language:

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight**

The goal is not to make every asset merely sharper or higher resolution. The goal is to build a coherent **Diyse-native visual library** with mature anime/seinen character language, painterly environments, chaotic variable line energy, cinematic HD-2D lighting compatibility, and field-scale readability.

---

## 1. Provenance Lanes

Every source asset enters one of three lanes before visual work begins.

### Lane A — Verified CC0 / redistributable source

Examples:
- Quaternius Fantasy Props MegaKit;
- Quaternius Universal Animation Libraries.

Allowed production treatment:
- direct repaint;
- direct remodel;
- direct retopology;
- texture replacement;
- geometry modification;
- animation retargeting/modification;
- stylization;
- integration into final production assets.

These may become direct final Diyse assets after passing style and technical review.

### Lane B — License-unverified extracted private/reference source

Examples:
- Map001–Map116 extracted texture archives.

Allowed internal treatment:
- private inspection;
- prototyping;
- composition/functional analysis;
- temporary internal repaint experiments;
- measurement of scale, perspective, animation cadence, atlas organization, and material behavior.

Important final assets should move toward a new Diyse-native replacement rather than assuming a repaint/upscale changes provenance.

### Lane C — Diyse-original source

Examples:
- newly painted textures;
- newly modeled landmark architecture;
- original faction pieces;
- custom signs/heraldry;
- original character/enemy assets;
- new environment modules derived from Diyse design requirements.

This is the preferred destination for final signature content.

---

## 2. Working Directory Model

Recommended production structure:

```text
asset_sources/
  private_reference/
    maps_001_116/
  third_party_cc0/
    quaternius/

assets/
  environment/
    working_conversion/
    diyse_original/
    shared_effects/
  props/
    working_conversion/
    diyse_original/
  characters/
  enemies/
  vfx/
  ui/
```

Never overwrite the source/reference archive when stylizing. Preserve originals, work from copies, and retain source/provenance metadata.

---

## 3. Conversion Stages

Every visual asset should move through the following stages.

### Stage 0 — Source verification

Before touching the asset:

- identify source archive/file;
- identify provenance lane;
- verify checksum when applicable;
- record original dimensions/formats;
- identify related animation/lighting/state files;
- identify whether alpha is meaningful;
- identify whether the asset is a complete atlas or isolated element.

For the current archive set use:

`ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`

and:

`tools/verify_asset_archives.py`

### Stage 1 — Functional analysis

Ask what the asset actually does.

Record:
- material/function;
- approximate physical scale;
- expected camera angle;
- tile/atlas boundaries;
- transparency behavior;
- required seams;
- animation frame count/cadence;
- interaction state needs;
- lighting-pass relationship;
- gameplay-distance visibility.

Do not begin aesthetic repainting until function is understood.

### Stage 2 — Style decomposition

Identify what must change to reach Diyse style:

- silhouette;
- shape hierarchy;
- value grouping;
- palette;
- material noise;
- line language;
- highlight/shadow behavior;
- regional/faction identity;
- painterly treatment;
- animation/effect shape language.

Separate **functional information to preserve** from **source-specific appearance to replace**.

### Stage 3 — Blockout / broad repaint

Work large-to-small.

1. establish major shapes;
2. establish value groups;
3. establish palette;
4. rebuild material breakup;
5. remove unnecessary micro-noise;
6. improve silhouettes/edges;
7. preserve required seams, alpha, or frame registration.

Do not add final chaotic line detail yet.

### Stage 4 — Chaotic line pass

Apply the style canon intentionally.

Use:
- thick-to-thin strokes;
- tapered cracks/grain/folds;
- broken contours;
- selective scratch/hatch clusters;
- uneven edge emphasis;
- line disappearance in light;
- heavier buildup in occlusion, compression, damage, or focal areas.

Do **not**:
- outline every object edge;
- add random scribble everywhere;
- apply a uniform “ink filter”;
- use line noise to hide weak shapes.

Environment rule:
> painterly structure first; ink rhythm second.

### Stage 5 — Material polish

Ensure each material reads instantly.

Check:
- stone planes and fractures;
- wood grain scale;
- metal highlight geometry;
- cloth fold grouping;
- foliage massing;
- water motion language;
- fire/lava luminosity;
- snow/ice plane readability;
- leather roughness/wear.

### Stage 6 — HD-2D integration pass

Test the asset in a representative scene, not only against a transparent checkerboard.

Check:
- character/environment contrast;
- atmospheric perspective;
- foreground/midground/background hierarchy;
- local lighting compatibility;
- shadow behavior;
- bloom susceptibility;
- parallax or occlusion role;
- route readability;
- interaction visibility.

### Stage 7 — Runtime-scale review

Review at actual or representative output sizes.

For environment assets:
- inspect at normal gameplay camera distance;
- inspect under brighter/darker scene lighting;
- inspect on target device scale.

For character derivatives:
- field target approximately 80 px;
- battle target approximately 200–220 px;
- portrait/high-res retains full line language.

Remove details that alias, shimmer, or collapse into noise.

### Stage 8 — Acceptance and promotion

Only promote to final production directories after:

- provenance is recorded;
- style rubric passes;
- seams/alpha/animation are valid;
- runtime-scale readability passes;
- no accidental source/reference overwrite occurred;
- final naming/versioning follows `VISUAL_ASSET_NAMING_AND_VERSIONING.md`.

---

## 4. Conversion Strategy by Asset Type

### A. Full environment atlases

These need the most caution because many source-specific forms are baked together.

Preferred process:
1. identify useful functional regions;
2. classify walls/floors/roof/cliff/trim/props;
3. decide which pieces should become modular Diyse-native components;
4. repaint/rebuild broad materials;
5. redesign distinctive source-specific ornament;
6. introduce Diyse-specific regional motifs;
7. reassemble into a production atlas only after modular pieces are approved.

Do not treat a full atlas as a single image to upscale and sharpen.

### B. Isolated props / transparent scenery

Good conversion candidates.

Process:
- preserve silhouette/function when useful;
- repaint palette/materials;
- redesign ornamental details;
- apply selective chaotic linework;
- clean alpha edges;
- verify pivot/scale in engine.

CC0 props may be directly transformed. Private-reference props should be treated as structural reference for final signature use.

### C. Trees / vegetation

Process:
- simplify into large foliage masses;
- redesign branch silhouette;
- reduce leaf noise;
- use tapered branch/leaf-cluster marks;
- separate light/shadow foliage masses;
- create seasonal/regional palette variants only when needed.

Avoid a “photographic leaf cloud” look.

### D. Doors / gates / animated interactables

Preserve:
- frame registration;
- open/closed alignment;
- collision/pivot assumptions;
- frame count unless deliberately changed.

Upgrade:
- silhouette;
- hardware;
- regional/faction ornament;
- materials;
- line accents;
- lighting consistency.

### E. Water systems

Preserve animation continuity before changing style.

Process:
1. inspect loop cadence;
2. establish new broad flow shapes;
3. create coherent highlights/shadow troughs;
4. add irregular graphic ripple accents;
5. keep all frames registered;
6. check loop seam;
7. test under scene lighting.

Water should feel graphic/painterly, not like a sharpened realistic normal-map texture.

### F. Fire / candle / lava / magical effects

These can carry more chaotic line energy than normal environment materials.

Use:
- bold silhouettes;
- asymmetrical motion;
- tapered edge flicker;
- dark/ink-like impact accents where appropriate;
- clear bright-core hierarchy;
- controlled glow.

Do not blur the entire effect into bloom.

### G. Lighting-pass textures

Do not independently stylize lighting passes without understanding the base color texture.

Process:
- pair with its source color asset;
- determine whether the pass represents direction, state, mask, or baked illumination;
- preserve spatial registration;
- rebuild values after the color repaint if necessary;
- test all states in sequence.

For `ra`–`rf` families, keep direction/state relationships coherent.

### H. Furniture / interior dressing

Good candidates for batch conversion.

Create a shared material language for:
- wood;
- brass/iron;
- cloth;
- glass;
- ceramic;
- leather.

Then vary design language by location/faction rather than inventing completely new rendering rules per object.

### I. Architecture

Architecture should be converted as a **kit**, not one wall at a time.

For each regional/faction kit define:
- wall module;
- floor;
- trim;
- corner;
- doorway;
- window;
- column/post;
- stair/ledge where needed;
- roof/ceiling language;
- damage/ruin variants;
- signage/heraldry;
- focal landmark pieces.

This is where Diyse originality matters most.

---

## 5. Regional / Faction Originalization Pass

A technically successful repaint is not enough for final identity assets.

For important locations, add original Diyse vocabulary through:

- silhouette motifs;
- architecture ratios;
- trim profiles;
- heraldry;
- signs;
- banners;
- door/window shapes;
- metalwork;
- masonry patterns;
- vegetation choices;
- lighting palette;
- recurring iconography.

The same stone/wood base can support multiple regions if the structural language changes enough.

---

## 6. Recommended First Conversion Benchmark Set

Before mass-processing 3,000+ texture records, build a small **style benchmark pack**.

Recommended representative set:

1. **stone/ruin** — one large wall/floor family;
2. **wood/interior** — one timber/furniture family;
3. **vegetation** — one tree plus one grass/reed system;
4. **water** — one 30-frame water loop plus splash;
5. **fire/light** — one fire/fireplace/candle family;
6. **cave** — one Map105–114 cavern family;
7. **high-status interior** — one Map092/104-type furnished set;
8. **magic/ritual** — one Map053/061/116-type motif;
9. **CC0 prop** — one Quaternius barrel/chair/workbench or similar;
10. **Black Host test piece** — an originalized wall/door/metal motif designed specifically for Diyse.

Do not batch-convert the whole library until this benchmark set looks like one coherent game.

---

## 7. Batch Conversion Order

After the benchmark is approved:

### Tier 1 — universal reusable materials
- stone;
- wood;
- metal;
- cloth;
- vegetation;
- water;
- fire;
- shadows.

### Tier 2 — common modular architecture
- doors/windows;
- walls/floors;
- fences;
- furniture;
- cave modules;
- snow/ice;
- desert/cactus;
- rural/town modules.

### Tier 3 — regional/faction kits
- Yahtrean regional families;
- Black Host architecture;
- ancient/archive/ritual architecture;
- other location-specific kits.

### Tier 4 — hero assets
- unique landmarks;
- story structures;
- signature statues/monuments;
- boss arenas;
- Prime/Card spaces;
- major faction iconography.

Custom effort should increase as the asset becomes more narratively important.

---

## 8. AI-Assisted Repaint / Generation Rules

AI may be used as a production aid for concepts, repaint exploration, or original replacement ideation, but outputs still require visual and provenance review.

### For CC0 source

Prompt may explicitly request transformation of the supplied asset while preserving function and silhouette where useful.

### For private-reference source

Preferred final prompt language:

> Use the source only as functional/structural reference. Create a newly interpreted original fantasy asset serving the same production role, with new surface design, new ornament, new material breakup, and Diyse’s mature seinen HD-2D chaotic-variable-line visual language. Do not merely upscale, trace, or closely reproduce the source appearance.

### Required style block

> Mature seinen-inspired HD-2D fantasy, chaotic variable line weight, expressive thick-to-thin tapered ink strokes, irregular broken contours, painterly stylized rendering, strong silhouette and shape hierarchy, deliberate hand-authored imperfection, rich controlled palette, cinematic atmospheric lighting, serious emotionally grounded fantasy tone, field-scale readability; not chibi, not photorealistic, not glossy mobile-gacha, not uniform clean vector line art, not generic texture-pack realism.

---

## 9. Reusable Prompt Pack

### General texture repaint

> Reinterpret this material into Diyse’s mature seinen HD-2D fantasy style. Preserve required functional dimensions, seams, registration, transparency, and production role, but rebuild the visual treatment with clearer large forms, reduced meaningless micro-noise, painterly material breakup, rich controlled color, cinematic value structure, and selective chaotic variable line accents. Use tapered, broken, irregular strokes around important edges, fractures, grain, folds, damage, or focal details. Do not simply sharpen or upscale the source.

### Original replacement from reference

> Use the supplied source only to understand function, approximate scale, camera relationship, and required asset categories. Create a new original Diyse asset with different specific surface shapes, ornamentation, edge patterns, and design details. Render it as mature seinen HD-2D fantasy with chaotic variable line weight, painterly environment treatment, strong material readability, intentional asymmetry, and cinematic lighting compatibility.

### Stone

> Rebuild as a Diyse stone material: broad readable masonry/rock forms, irregular silhouettes, stylized fractures, sparse tapered ink-dark crack accents, painterly light-plane separation, reduced speckle/noise, mature fantasy palette, strong gameplay-distance readability.

### Wood

> Rebuild as a Diyse wood material: broad stylized grain, irregular knots, tapered ink-like grain accents, controlled edge wear, strong plank/form readability, painterly value grouping, no microscopic repeating grain.

### Foliage

> Rebuild as Diyse foliage: large designed foliage masses first, irregular branch silhouettes, selective tapered line accents, clustered leaf shapes rather than individual noisy leaves, painterly light/shadow groups, cinematic HD-2D depth readability.

### Water

> Rebuild as Diyse water: graphic flow bands, irregular hand-authored ripples, clean highlight shapes, painterly depth, selective energetic ink accents on waves/splashes, luminous but not plastic, preserve loop registration and cadence.

### Interior prop

> Reinterpret this prop into Diyse’s mature seinen fantasy language: strong silhouette, clear material separation, painterly surfaces, asymmetrical authored wear, selective chaotic variable line accents at overlaps and focal edges, simplified microdetail, serious handcrafted finish.

### Architecture

> Create a modular Diyse architecture piece in mature seinen HD-2D fantasy style. Prioritize a distinct silhouette, readable construction, regional/faction shape language, painterly materials, irregular hand-authored edge treatment, and selective chaotic linework. It must work as part of a reusable kit rather than only as a standalone illustration.

### VFX

> Create a Diyse combat/environment effect with bold graphic silhouette, chaotic tapered line energy, clear anticipation-impact-decay, controlled particles, painterly glow, strong gameplay readability, and a mature seinen fantasy tone. Avoid generic stock-particle noise and indiscriminate bloom.

---

## 10. Technical Preservation Rules

### Dimensions

Do not change dimensions arbitrarily. Resize only when the runtime pipeline has a clear target and all dependent masks/frames are updated consistently.

### Alpha

Preserve edge registration. Clean halos/fringing after repaint or upscale.

### Animation

For numbered frames:
- preserve frame order;
- preserve canvas size;
- preserve pivot/registration;
- validate seamless loops;
- ensure line/paint treatment does not visibly jump between frames.

### Lighting-state families

For A/B/C or `ra`–`rf` states:
- preserve corresponding geometry/mask alignment;
- review as a family;
- never approve one state in isolation if the asset rotates/changes lighting in use.

### Atlases

Maintain safe padding where filtering/mipmaps could cause bleeding. Do not expand painted content across atlas boundaries unless layout is intentionally rebuilt.

---

## 11. Quality Gates

### Gate A — Functional

- correct dimensions;
- correct alpha;
- correct registration;
- correct animation/state count;
- no broken seams;
- correct pivot/collision assumptions documented.

### Gate B — Style

- major shapes read clearly;
- material is painterly/stylized;
- chaotic variable line language is present where appropriate;
- linework is intentional, not random noise;
- palette/value treatment matches scene family;
- no photorealistic texture-pack residue dominates.

### Gate C — Diyse identity

For signature/final assets:
- does the piece include original Diyse design language?
- does it avoid looking like an untouched stock/source asset?
- does region/faction identity read?
- does it belong next to approved character masters?

### Gate D — Runtime

- readable at gameplay scale;
- no excessive shimmer/aliasing;
- no line-detail collapse;
- interactables remain visible;
- characters remain separated from background;
- acceptable target-device performance.

---

## 12. Conversion Grades

Use these grades in the tracker/inventory.

### `REF`
Private/reference source only. Not visually converted.

### `PROTO`
Temporary direct transformation or prototype. Useful for building/testing, not final authority.

### `STYLE-PASS`
Successfully converted to Diyse rendering language but not yet fully region/faction-originalized or runtime-approved.

### `DIYSE-FINAL`
Passes provenance, style, identity, functional, and runtime gates for final project use.

### `REPLACE`
Asset remains useful as reference but should not survive into final production.

---

## 13. Tracking Fields

For each converted family record:

- source archive;
- source filename(s);
- provenance lane;
- current grade;
- intended Diyse use;
- conversion owner/tool;
- working asset path;
- final asset path;
- source dimensions;
- output dimensions;
- animation/state count;
- palette/faction family;
- style-review result;
- runtime-review result;
- replacement/originalization notes.

---

## 14. First Production Pass — Recommended Scope

Do **not** begin by converting all 3,214 extracted texture records.

First create a compact style-proof set containing:

- one stone environment;
- one wood/interior environment;
- one tree/vegetation asset;
- one animated grass/reed system;
- one 30-frame water loop plus splash;
- one fire/candle effect;
- one cave environment;
- one high-status interior;
- one magic/ritual environment;
- several CC0 props;
- one completely original Diyse faction/region module.

Place those together in a representative HD-2D scene. Only after they read as a single coherent game should the pipeline be scaled across the library.

---

## 15. Completion Definition

The source library has completed its role when final production no longer depends on visual inconsistency between unrelated source families.

A successful final Diyse asset library should feel as if:

- the same art team designed every material family;
- the same line philosophy shaped characters, props, VFX, and focal environments;
- each region/faction has its own design identity;
- HD-2D lighting unifies the scene;
- source-pack origins are no longer visually obvious;
- important final art reads as **Diyse**, not as upgraded borrowed/stock material.

---

## 16. Production Shorthand

For all conversion reviews:

> **FUNCTION → SHAPE → VALUE → PALETTE → PAINT → CHAOTIC LINE PASS → HD-2D INTEGRATION → RUNTIME TEST → DIYSE IDENTITY**

Skipping directly from source asset to “AI upscale” does not satisfy this pipeline.
