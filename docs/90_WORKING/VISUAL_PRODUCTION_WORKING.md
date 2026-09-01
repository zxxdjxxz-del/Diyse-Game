# Working — Visual Production / Style Certification

**Owner:** `14_ART_AND_VISUALS`

**Status:** **ACTIVE**

This file tracks only unresolved production gates. It does not duplicate or override the visual canon.

## Locked direction
Current production target:
> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**

Primary authority:
- `../14_ART_AND_VISUALS/DIYSE_VISUAL_STYLE_CANON.md`
- `../14_ART_AND_VISUALS/README.md`

## Immediate gate — B00 Permanent Party Character Style Anchor
Authority:
`../14_ART_AND_VISUALS/PRODUCTION/BENCHMARKS/B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`

Current state:
- Cyanis — **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED**;
- Ilyra — **PROVISIONAL DESIGN TARGET / CLEAN REMAKE + CLOTHING REVIEW OPEN**;
- Torren — new-style master pending;
- Nimera — new-style master pending;
- Vaelira — new-style master pending;
- Seyrik — new-style master pending.

B00 is not complete until:
1. all six permanent-party high-resolution masters are explicitly approved;
2. battle-scale derivative logic is validated;
3. field-scale derivative logic at approximately 80 px character height is validated;
4. character readability holds against the environment/VFX line-density hierarchy.

The preferred review asset for each character is a single clean full-body render unless another view is specifically needed.

## Environment / material benchmark gate — B01–B11
Authority:
`../14_ART_AND_VISUALS/PRODUCTION/STYLE_BENCHMARK_SET_V1.md`

Open benchmark families:
- B01 stone / fortified exterior;
- B02 wood / rustic interior;
- B03 tree / foliage silhouette;
- B04 animated vegetation;
- B05 water + splash;
- B06 fire / light emitter;
- B07 cave / subterranean material;
- B08 high-status interior;
- B09 ritual / magic surface;
- B10 verified-CC0 prop cluster;
- B11 fully original Black Host fortified wall/gate module.

Do not bulk-convert the preserved 3,214-file environment library until the benchmark set reads as one coherent game at actual gameplay scale.

## Post-benchmark deliverable
Accepted benchmark results should become a **Diyse Visual Material Grammar v1** governing repeatable treatment for stone, wood, metal, cloth, foliage, caves/minerals, water, fire/emissives, magical surfaces, luxury interiors, faction architecture, 3D prop integration, and line-density rules by asset class/scale.

## Conversion / automation lane
Production references:
- `../14_ART_AND_VISUALS/PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`
- `../14_ART_AND_VISUALS/PRODUCTION/ASSET_FORGE_AUTOMATION.md`
- `../../tools/asset_forge/forge.py`

Asset Forge may inventory, hash, classify, plan, preserve/generate, QA-check, and build deterministic review sheets. It does not independently define the art style and must not damage atlas seams or animation-frame consistency through uncontrolled redraws.

## Guardrails
- newest explicitly approved character/location visual controls derivatives unless later revised;
- B00 changes rendering treatment and only changes character design details when explicitly approved;
- do not bulk-convert before benchmark acceptance;
- do not promote source/reference assets directly as Diyse-final merely because they are available;
- preserve provenance routing and license boundaries;
- gameplay-scale readability is a required acceptance test, not an optional cleanup pass.

## Current next action
> **Resolve Ilyra's clean B00 remake/clothing review, then continue the remaining permanent-party B00 masters.**
