# Diyse — Asset Style Conversion Pipeline

**Status:** ACTIVE PRODUCTION GUIDE  
**Locked style target:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Asset inventory authority:** `ASSET_LIBRARY/README.md`

This guide defines how source/reference assets, verified CC0 assets, and Diyse-original work enter the active visual language:

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**

The goal is not merely larger or sharper assets. The goal is a coherent Diyse-native library with mature anime/seinen character language, graphic shape-first environments/materials, chaotic variable line energy, cinematic HD-2D lighting compatibility, and field-scale readability.

**“Painterly” is retired from the active production target.** Do not use it in conversion prompts, review criteria, or family approvals unless explicitly reintroduced by a later user decision.

---

## 1. Provenance lanes

### Lane A — Verified CC0 / redistributable
Examples: Quaternius props/animations; Brackeys VFX bundle with included CC0 declaration.

Allowed: direct restyle, repaint/retexture, remodel, retopology, geometry modification, animation modification, and final integration after style/runtime review.

### Lane B — License-unverified private/reference
Examples: Map001–Map116 extracted material; Supplemental Texture Batch 1.

Allowed internally: inspection, prototyping, structural/composition analysis, temporary private style tests, scale/perspective/animation/atlas/material analysis.

Important final assets should become new Diyse-native replacements rather than assuming a style transformation changes provenance.

### Lane C — Diyse-original
Newly authored characters, enemies, architecture, textures, VFX, landmarks, faction assets, signs/heraldry, and environment modules. Preferred for signature content.

---

## 2. Preservation rule

Never overwrite source/reference archives when stylizing. Preserve originals, retain checksums/provenance, and distinguish **inventory recorded** from **binary durably backed up**.

Current source/intake authorities:
- `ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`
- `ASSET_LIBRARY/SUPPLEMENTAL_INTAKE_INDEX.md`
- `ASSET_LIBRARY/BINARY_PRESERVATION_STATUS.md`

---

## 3. Conversion stages

### Stage 0 — Source verification
Record source archive/file, provenance lane, checksum when available, dimensions/formats, alpha, related animation/lighting/state files, and atlas relationships.

### Stage 1 — Functional analysis
Record material/function, approximate scale, camera relationship, tile/atlas boundaries, transparency, seams, animation cadence, interaction states, lighting relationship, and gameplay-distance visibility.

### Stage 2 — Style decomposition
Separate functional information to preserve from source-specific appearance to replace. Evaluate silhouette, shape hierarchy, value grouping, palette, material noise, line language, highlight/shadow behavior, regional/faction identity, and animation/effect shape language.

### Stage 3 — Graphic blockout
Work large-to-small:
1. major shapes;
2. 2–4 dominant value groups where appropriate;
3. palette;
4. graphic material breakup;
5. remove meaningless micro-noise;
6. improve silhouettes/edges;
7. preserve seams, alpha, UVs, pivots, or frame registration.

### Stage 4 — Chaotic line pass
Use thick-to-thin strokes, tapered cracks/grain/folds, broken contours, selective hatch/scratch clusters, uneven edge emphasis, line disappearance in light, and heavier buildup in occlusion/compression/damage/focal areas.

Do not outline everything, add random scribble/dots, or apply a uniform ink filter.

Environment rule:
> **graphic shape/value structure first; selective ink rhythm second.**

### Stage 5 — Material polish
Ensure stone planes/fractures, wood grain scale, metal highlight geometry, cloth fold grouping, foliage massing, water motion, fire/lava luminosity, snow/ice planes, and leather wear read instantly at gameplay distance.

### Stage 6 — HD-2D integration
Test in a representative scene for character/environment contrast, depth hierarchy, local lighting, shadow behavior, bloom, parallax/occlusion, route readability, and interaction visibility.

### Stage 7 — Runtime-scale review
Review at actual output sizes. Character targets remain approximately **200–220 px battle** and **~80 px field**. Remove detail that aliases, shimmers, or collapses into noise.

### Stage 8 — Acceptance
Promote only after provenance, style, seams/alpha/animation, runtime readability, and versioning all pass.

---

## 4. Asset-type strategy

### Full environment atlases
Analyze functional regions; classify materials; decide what becomes modular; rebuild broad forms and value groups; redesign distinctive ornament; add Diyse regional motifs; reassemble only after modular approval. Never treat a full atlas as one image to simply upscale/filter.

### Isolated props
Preserve useful function/silhouette; redesign surface/ornament; apply graphic material values and selective linework; clean alpha; verify pivot/scale.

### Trees / vegetation
Use large foliage masses, designed branch silhouettes, clustered leaves, grouped light/shadow shapes, reduced leaf noise, and selective tapered accents. Avoid photographic leaf clouds and soft fuzzy canopies.

### Doors / animated interactables
Preserve registration, pivot/alignment, and frame cadence. Upgrade silhouette, hardware, faction identity, materials, graphic values, and selective line accents.

### Water
Preserve loop continuity. Use graphic flow bands, coherent highlight/shadow troughs, irregular authored ripples, and selective energetic accents. Avoid realistic sharpened texture behavior.

### Fire / candle / lava / magic
Use bold anime silhouettes, asymmetrical motion, clear internal value hierarchy, selective dark/tapered accents, bright mostly-unoutlined cores, and controlled glow. Never solve the effect with blur/bloom alone.

### Lighting-state families
Pair with the source color asset, preserve registration, understand direction/state/mask purpose, rebuild values only after the base treatment, and test the family as a coherent sequence.

### Furniture / dressing
Build shared material grammar for wood, metal, cloth, glass, ceramic, and leather; vary design language by region/faction instead of inventing new rendering rules per prop.

### Architecture
Convert as modular kits: wall, floor, trim, corner, door, window, column/post, stairs/ledges, roof/ceiling, damage variants, signage/heraldry, and focal pieces. Architecture must carry original Diyse regional/faction identity.

---

## 5. AI-assisted visual work

AI may assist concept exploration, restyling, or original replacement ideation, but outputs still require provenance, identity, and visual review.

### Character rule
When an exact approved character master exists, treat it as identity/design authority. Do not invent weapons, crests, clothing, facial hair, age changes, or presentation sheets unless explicitly requested. Prefer one clean full-body asset for B00 review.

### CC0 source
Direct transformation is allowed while preserving required function/registration.

### Private-reference source
Use the source only for functional/structural understanding. Create a newly interpreted Diyse asset rather than closely reproducing the source appearance.

### Required style block
> **Mature seinen-inspired HD-2D fantasy, chaotic variable line weight, expressive thick-to-thin tapered ink strokes, irregular broken contours, strong silhouettes, graphic anime-stylized rendering, cel-informed value grouping, shape-first material readability, deliberate hand-authored imperfection, rich controlled palette, cinematic atmospheric lighting, serious emotionally grounded fantasy tone, field-scale readability; not chibi, not photorealistic, not painterly/soft-brushed, not glossy mobile-gacha, not uniform vector line art, not generic texture-pack realism.**

---

## 6. Reusable family prompt language

### General material conversion
> Preserve required dimensions, seams, registration, transparency, and production role. Rebuild the asset with clearer large forms, reduced meaningless micro-noise, graphic anime-compatible value grouping, controlled color, shape-first material breakup, and selective chaotic variable line accents. Do not merely sharpen, upscale, speckle, or filter the source.

### Stone
Broad masonry/rock forms, stylized fractures, sparse tapered dark crack accents, strong graphic light-plane separation, no dense photographic speckle.

### Wood
Broad stylized grain and knots, restrained tapered grain accents, controlled functional wear, clear plank/form readability, no microscopic repeating grain.

### Foliage
Large designed foliage masses, irregular branch silhouettes, selective tapered accents, clustered leaf shapes, grouped light/shadow values, strong HD-2D depth readability.

### Water
Graphic flow bands, irregular authored ripples, clean highlight shapes, selective energetic accents, luminous but not plastic; preserve loop registration/cadence.

### Interior props
Strong silhouette, clear material separation, graphic value groups, authored asymmetrical wear, selective line accents at overlaps/focal edges, simplified microdetail.

### Architecture
Distinct silhouette, readable construction, regional/faction shape language, graphic materials, irregular authored edges, selective chaotic linework, modular-kit compatibility.

### VFX
Bold graphic silhouette, chaotic tapered line energy, readable anticipation-impact-decay, controlled particles, cel-like value masses, controlled emissive spill, mature seinen tone; no stock-photo/fire look and no indiscriminate bloom.

---

## 7. Technical preservation rules

### Dimensions / UVs
Do not change dimensions or UV registration arbitrarily. Update dependent masks/maps consistently.

### Alpha
Preserve meaningful source alpha exactly where required; clean halos/fringing.

### Atlases
Use coordinate-locked patches and deterministic reconstruction. Require seam/identity QA before artistic transforms are trusted.

### Animation
Preserve frame order, canvas size, pivot/registration, and loop cadence. Style families coherently; do not independently redraw every frame when that would cause flicker or structural drift.

### Lighting variants
Preserve spatial/state relationships across `ra`–`rf` or equivalent families.

### Review artifacts
Build deterministic review sheets from actual outputs. Generated infographics or generated status text are never production authority.

---

## 8. Benchmark dependency

B00 is now the primary character-style anchor. Cyanis is the first approved high-resolution B00 master; five party masters remain.

B01/B03/B10 retain within-family approvals but require recheck against the revised graphic-anime B00 authority before final acceptance. B06 remains a technical preservation proof until its fire/light treatment is rebuilt to match the character-side anime language.

Do not bulk-promote the wider library until the benchmark families read as one coherent game under the active visual canon.
