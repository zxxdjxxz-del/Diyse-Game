# Diyse — CC0 Props / Cloth Family Validation Candidate v1

**Status:** **REAL-MODEL FAMILY CANDIDATE — USER REVIEW PENDING**  
**Parent grammar:** `DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`  
**B10 benchmark:** `BENCHMARKS/B10_STYLE_PASS_APPROVAL_V1.md`  
**Automation checkpoint:** Asset Forge v0.7 family routing

## Purpose

Validate the two shared material families not directly proven by the four-object B10 benchmark:
- `T_Trim_Props`;
- `T_Trim_Cloth`.

Furniture and Metal are already B10-approved. This pass tests whether Props/Cloth can join them as production-ready shared families without reverting to one-art-job-per-model.

## Real source models tested

Props-focused:
- `Bottle_1` — Props only;
- `Book_5` — Props only;
- `Potion_1` — Props only.

Cloth/mixed:
- `Banner_1_Cloth` — Cloth + Metal;
- `Bag` — Cloth + Furniture;
- `Bed_Twin1` — Cloth + Furniture + Metal.

All validation models are actual glTF assets from the verified CC0 Quaternius Fantasy Props MegaKit.

## Routing correction proven by this pass

Asset Forge v0.7 resolves actual glTF:

`MATERIAL → baseColorTexture INDEX → TEXTURE → IMAGE URI → SHARED FAMILY`

It no longer relies on material-name guesses.

This is necessary because real source materials include:
- `MI_Trim_Props_Vertex` → Props;
- `MI_Banner` → Cloth.

Those names cannot be routed reliably by looking for the words `Props` or `Cloth` alone.

## Props family candidate

The Props atlas is intentionally mixed-use and includes multiple object/color roles. The first deterministic treatment therefore preserves authored hue differences while simplifying value/noise structure rather than forcing one palette.

Real-model candidate read:
- `Bottle_1` remains a clear narrow bottle silhouette under neutral/warm/cool lighting;
- `Book_5` preserves the book/page-cover separation and readable edge hierarchy;
- `Potion_1` retains a distinct vessel/band read rather than collapsing into the same color treatment as the bottle;
- the shared Props treatment does not require unique authoring per model.

Current source PBR QA:
- Normal XY >0.5 ratio: approximately **13.1%**;
- Normal XY >0.75 ratio: approximately **4.2%**;
- roughness median: approximately **0.71**;
- roughness <0.5 ratio: approximately **6.6%**.

Decision from current QA:
> no automatic Props Normal/ORM rebuild is required for the first family candidate.

## Cloth family candidate

The Cloth treatment uses broad fold/value modulation with very low texture-space ink pressure.

Real-model candidate read:
- `Banner_1_Cloth` remains soft/matte and separates from its Metal mounting points;
- `Bag` remains clearly cloth-like in color/value behavior even though the low-poly source geometry still contributes faceted silhouette shading;
- `Bed_Twin1` successfully combines Cloth, Furniture and Metal shared families in one real model without material-routing collision;
- cloth does not inherit the hard dark-edge treatment used by metal or structural wood.

Current source PBR QA:
- Normal XY >0.5 ratio: approximately **4.1%**;
- Normal XY >0.75 ratio: approximately **0.9%**;
- roughness median: approximately **1.0**;
- roughness <0.5 ratio: approximately **0.1%**.

Decision from current QA:
> preserve the source Cloth Normal/ORM pair for the first family candidate; it is already highly matte and restrained.

## Physical scale verification

Real glTF extents used by the candidate:
- `Bottle_1`: approximately **0.113 × 0.365 × 0.113**;
- `Book_5`: approximately **0.213 × 0.064 × 0.287**;
- `Potion_1`: approximately **0.114 × 0.140 × 0.114**;
- `Banner_1_Cloth`: approximately **0.810 × 2.246 × 0.057**;
- `Bag`: approximately **0.655 × 0.799 × 0.544**;
- `Bed_Twin1`: approximately **1.876 × 0.805 × 2.412**.

A deterministic scale preview compares these real dimensions against the same **1.75-unit character marker** used by B10-scale validation.

Result:
- tiny Props assets remain intentionally small rather than being misleadingly hero-scaled;
- Banner height reads as architectural/decorative rather than handheld;
- Bag and Bed proportions remain plausible beside the character marker;
- mixed shared materials stay readable at real relative scale.

## Lighting validation

All six models were rendered under:
- neutral;
- warm;
- cool.

Candidate result:
- no family collapses to black under alternate light;
- cloth remains softer/more matte than metal;
- Props maintains useful hue separation;
- approved Furniture/Metal behavior remains stable when combined with candidate Cloth.

## Generation cost

This candidate uses:

> **0 image-generation calls**

The conversion is produced by the UV-safe local deterministic backend and actual real-model validation.

## Internal gate result

Technical candidate status:
- **PASS:** actual material-to-texture routing;
- **PASS:** Props source dimensions/UV architecture preserved;
- **PASS:** Cloth source dimensions/UV architecture preserved;
- **PASS:** source PBR data remains compatible enough for first-pass reuse;
- **PASS:** mixed-material real models render without family collisions;
- **PASS:** neutral/warm/cool paths remain stable;
- **PASS:** physical-scale readability proof completed;
- **USER REVIEW REQUIRED:** artistic desirability of the Props and Cloth family treatments.

## Promotion rule

Do not mark Props/Cloth production-approved from this document alone.

Current state:

`FAMILY CANDIDATE → USER REVIEW`

If approved:
1. promote Props + Cloth to **APPROVED** in `DIYSE_CC0_PROP_MATERIAL_GRAMMAR_V1.md`;
2. treat all four major CC0 shared material families as the default pack grammar;
3. move the remaining 94-model pass to exception detection/overrides rather than broad restyling;
4. keep final game/runtime validation separate from material-family approval.
