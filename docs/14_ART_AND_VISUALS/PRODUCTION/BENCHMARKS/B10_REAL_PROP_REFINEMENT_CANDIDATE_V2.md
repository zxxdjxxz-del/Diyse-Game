# Diyse — B10 Real Prop Refinement Candidate v2

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** VISUAL REFINEMENT CANDIDATE V2 / USER REVIEW PENDING  
**Execution authority:** `B10_CC0_PROP_CLUSTER_EXECUTION_V1.md`  
**Style-study authority:** `B10_CC0_PROP_STYLE_STUDY_SPEC_V1.md`  
**Previous technical baseline:** `B10_DETERMINISTIC_MATERIAL_BASELINE_PILOT_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## 1. What changed from the first technical baseline

The first real four-prop pilot proved the shared-material pipeline but deliberately left four visual/technical issues open:
- wood line density was too busy;
- metal was too flat under neutral lighting;
- Lantern_Wall used only a validation glow hint rather than exportable emissive data;
- Furniture normal relief triggered PBR review.

Candidate v2 addresses all four without spending image-generation calls.

## 2. Wood refinement

The previous deterministic BaseColor treatment generated dark accents from a broad Laplacian edge field. On the Furniture trim that promoted too many existing grooves into ink and made the result busier than the Diyse environment hierarchy allows.

v2 changes the material algorithm to:
- preserve the source trim atlas layout exactly;
- build broad painterly value planes first;
- preserve only sparse, larger existing dark strokes;
- reject small isolated edge fragments through connected-component filtering;
- reduce wood ink strength;
- retain only low-frequency surface variation.

Result:
> Barrel, Chair_1, and Workbench retain wood identity and construction seams while the grain/line field is visibly quieter than the v1 baseline.

## 3. Metal refinement

v2 strengthens metal readability through two coordinated changes:
- the shared Metal BaseColor uses broader cool-gray value planes and more selective highlights;
- the validation renderer now reads the source ORM map and adds restrained roughness/metalness-aware specular separation.

This is intentionally not photoreal PBR rendering. The goal is to make hoops, brackets, fasteners, and the wall-lantern structure separate clearly from wood while retaining the painterly HD-2D target.

## 4. Furniture normal-map compatibility

Source PBR QA on `T_Trim_Furniture_Normal.png` reported:
- XY strength `> 0.5`: approximately **25.2%** of pixels;
- XY strength `> 0.75`: approximately **13.4%** of pixels.

Because this crossed the current `strong_normal_review` gate, v2 automatically generates a UV-identical Furniture normal candidate with **0.72 X/Y strength**.

Rebalanced result:
- XY strength `> 0.5`: approximately **16.6%**;
- XY strength `> 0.75`: **0%**.

The source Metal normal does not receive the same automatic attenuation because its current QA profile does not require the stronger Furniture correction.

The source ORM maps remain unchanged in this pass because their roughness distributions are already compatible enough for continued validation:
- Furniture is predominantly matte;
- Metal remains moderately rough rather than mirror-glossy.

## 5. Authored Lantern_Wall emitter

The source Lantern_Wall glTF contains no emissive material. Candidate v2 therefore does not pretend an emissive texture exists.

Asset Forge now derives and exports a dedicated model-space emitter anchor from the lower hanging cage geometry.

Real pilot anchor:
- model-space position approximately **(0.000000, 0.486414, 0.810444)**;
- core radius approximately **0.081287** source units;
- baseline light range approximately **1.136456** source units;
- warm source color baseline: **RGB 255 / 176 / 82**.

This metadata can later drive:
- an emissive overlay/core;
- a Godot local light;
- restrained bloom;
- authored warm spill.

The deterministic validation renderer uses the same model-space logic for its visible light core and halo instead of a fixed screen-space effect.

## 6. Gameplay-scale integration proof

Candidate v2 adds a deterministic gameplay-scale workshop preview.

The preview:
- uses the actual glTF physical extents;
- scales all four props relative to one another;
- includes a neutral **1.75-unit** character measurement silhouette;
- prevents independent close-up framing from hiding scale/readability problems;
- keeps the preview background intentionally simple so it is a readability test rather than final environment art.

Verified real source extents used by the pilot:
- Barrel: approximately **0.698 × 0.898 × 0.698**;
- Chair_1: approximately **0.581 × 1.123 × 0.549**;
- Lantern_Wall: approximately **0.357 × 1.337 × 1.302**;
- Workbench: approximately **2.019 × 0.895 × 1.024**.

## 7. Current candidate read

Internal technical/art read before user approval:
- **PASS candidate:** shared wood family now reads more quietly;
- **PASS candidate:** metal separates more clearly from wood;
- **PASS:** all four actual glTF silhouettes remain recognizable;
- **PASS:** neutral/warm/cool validation paths remain stable;
- **PASS:** Furniture normal relief is reduced deterministically after QA flagging;
- **PASS:** Lantern_Wall now has exportable emitter metadata;
- **PASS:** gameplay-scale relative-size preview is automated;
- **PASS:** still **0 image-generation calls** for this deterministic candidate;
- **USER REVIEW REQUIRED:** final artistic desirability of the v2 wood/metal treatment.

## 8. Promotion rule

Do **not** mark B10 `STYLE-PASS` from this document alone.

Current state:

`TECHNICAL MATERIAL PILOT PASS → VISUAL REFINEMENT CANDIDATE V2 → USER REVIEW`

If the v2 real-prop treatment is approved, the next production steps are:
1. promote B10 to STYLE-PASS;
2. generate a controlled shared-material specification for Furniture / Metal / Props / Cloth;
3. validate the same grammar on a broader CC0 prop sample;
4. move B10 into gameplay/runtime testing rather than returning to AI-generated concept boards.
