# Diyse — CC0 Prop Material Grammar v1

**Status:** ACTIVE PRODUCTION GRAMMAR  
**Derived benchmark:** `BENCHMARKS/B10_STYLE_PASS_APPROVAL_V1.md`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Automation:** `ASSET_FORGE_AUTOMATION.md`

## Purpose

This file defines the shared-material grammar used when verified-CC0 3D prop libraries are adapted into Diyse's seinen HD-2D visual language.

The source library may retain useful geometry and shared UV trim architecture. Diyse identity comes from controlled material treatment, selective line influence, lighting behavior, authored emitters, gameplay-scale hierarchy and prop-specific overrides where needed.

## Family validation status

| Family | Current status | Source-pack reach |
|---|---|---:|
| Furniture | **B10 APPROVED** | 41 models |
| Metal | **B10 APPROVED** | 60 models |
| Props | **FAMILY CANDIDATE — BROADER REAL-MODEL VALIDATION REQUIRED** | 39 models |
| Cloth | **FAMILY CANDIDATE — BROADER REAL-MODEL VALIDATION REQUIRED** | 10 models |

Do not silently promote Props/Cloth to the same validation status as Furniture/Metal until their representative real-model batch passes.

## Shared rules for all families

- preserve UV registration and source dimensions;
- broad material planes read before small texture detail;
- reduce high-frequency noise;
- use selective, irregular dark accents rather than universal outlines;
- never outline every polygon/UV island;
- retain source Normal/ORM maps unless QA identifies a specific incompatibility;
- validate neutral, warm and cool lighting;
- validate actual glTF models, not just texture sheets;
- validate physical/gameplay scale rather than individually zoomed hero renders;
- model-specific overlays are allowed when a shared sheet cannot carry unique faction/use/wear information cleanly.

## Furniture — APPROVED

Visual target:
- warm-to-neutral wood families with 3–5 broad value groups;
- grain direction follows form but stays subordinate;
- strongest dark accents at construction joints, deep splits, underside overlaps and selected damage;
- sparse irregular grain accents may echo chaotic variable line weight;
- worn highlights concentrate at handling/contact edges;
- no dense pore noise or equal-width dark grain everywhere.

PBR target:
- predominantly matte;
- retain source ORM when compatible;
- attenuate excessive normal relief after QA rather than flattening the entire sheet by default.

## Metal — APPROVED

Visual target:
- cool/neutral dark-to-mid metal planes with selective warm corrosion where source/use supports it;
- stronger plane/value contrast than wood;
- restrained sharp highlights on selected edges and turns;
- dark joint/overlap accents;
- sparse dents/scratches only where readable;
- no chrome realism and no constant-width black contour shell.

PBR target:
- moderately rough by default;
- source ORM remains valid while it avoids mirror-gloss behavior;
- normal data remains source-strength unless QA flags excess.

## Props — FAMILY CANDIDATE

`T_Trim_Props` is a mixed-use atlas rather than one physical substance. It includes painted objects, books, bottles, tools, food/produce-like surfaces, decorative panels and other small-prop regions.

Therefore its grammar is **hue-preserving**, not a single forced palette.

Target:
- keep authored hue/category separation so different prop types remain identifiable;
- compress values into broad readable groups;
- modestly reduce saturation/noise rather than recoloring the whole sheet into one Diyse hue;
- preserve large intentional graphic marks and decorative motifs;
- use only sparse dark accents around meaningful large structural boundaries;
- do not turn every painted edge or icon boundary into ink;
- small props must remain readable at field scale without becoming high-contrast confetti.

Current source PBR read:
- normal XY >0.5 ratio approximately 13.1%;
- normal XY >0.75 ratio approximately 4.2%;
- roughness median approximately 0.71;
- roughness <0.5 ratio approximately 6.6%.

Current interpretation:
> no automatic Normal or ORM rebuild is required before broader validation.

## Cloth — FAMILY CANDIDATE

Cloth must not inherit the hard edge grammar of wood or metal.

Target:
- broad fold/value masses;
- source hue identity retained with slightly restrained saturation;
- soft low-frequency variation;
- selective deeper fold shadow only at major compression/overlap;
- minimal or no contour-like texture ink on ordinary cloth surfaces;
- graphic insignia/decal regions remain crisp where intentionally authored;
- fabric remains visually matte and soft beside metal/wood.

Current source PBR read:
- normal XY >0.5 ratio approximately 4.1%;
- normal XY >0.75 ratio approximately 0.9%;
- roughness median approximately 1.0;
- roughness <0.5 ratio approximately 0.1%.

Current interpretation:
> the source Cloth Normal/ORM pair is already suitably restrained/matte for the first family validation pass.

## Line-density hierarchy

From strongest to weakest expected texture-space line influence:

1. Metal structural joints / deep recesses;
2. Furniture construction joints / selected damage;
3. mixed Props large structural accents;
4. Cloth ordinary surface detail.

This hierarchy prevents every prop family from competing at the same dark-line density.

## Emissive exception

Light sources are data-driven exceptions:
- bright cores should remain largely free of dark texture linework;
- surrounding fixture structure follows its base material grammar;
- emitter position/range/color should be exported as runtime data where possible;
- bloom/light spill belongs to runtime lighting, not baked into every BaseColor state.

## Automation rule

Asset Forge must resolve **material → BaseColor image** from the actual glTF texture bindings. Do not infer family solely from material names, because valid source materials include names such as `MI_Banner` and `MI_Trim_Props_Vertex`.

## Broader validation batch

The first post-B10 family validation should include at least:
- `Bottle_1` — Props-only;
- `Book_5` — Props-only;
- `Potion_1` — Props-only;
- `Banner_1_Cloth` — Cloth + Metal;
- `Bag` — Cloth + Furniture;
- `Bed_Twin1` — Cloth + Furniture + Metal.

Props/Cloth become production-approved only after this or an equivalent real-model batch demonstrates:
- correct material routing;
- stable neutral/warm/cool appearance;
- readable physical scale;
- no destructive UV/PBR changes;
- coherent style beside approved Furniture/Metal.
