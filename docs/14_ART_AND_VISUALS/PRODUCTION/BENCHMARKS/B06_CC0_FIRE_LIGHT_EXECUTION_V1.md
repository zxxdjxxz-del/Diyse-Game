# Diyse — B06 Fire / Light Emitter Execution v1

**Benchmark:** B06 — Fire / Light Emitter  
**Status:** **SOURCE ANALYSIS COMPLETE / TECHNICAL STYLE PILOT READY**  
**Primary verified-open source:** `../ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Forge VFX processor:** `../../../../../tools/asset_forge/vfx_processing_engine.py`

## 1. Source decision

B06 should now use the verified-CC0 Brackeys VFX bundle as its primary production source pool rather than relying mainly on the license-unverified Map092 fire material.

The bundle supplies reusable fire/flame flipbooks, predrawn fire sheets, sparks, flares, lights, smoke and paired particle masks that may be directly modified after style/runtime review.

Map092 may remain useful as private/reference comparison material, but it is no longer necessary as the principal B06 production path.

## 2. Representative B06 source families

Primary motion studies:
- `flipbooks/fire_01_8x8.tga` — RGB / 64 frames;
- `flipbooks/flame_01_16x4.tga` — RGBA / 64 frames;
- `predrawn/fire_ring_6x5.png` — 30 frames;
- `predrawn/dithered_fire_6x5.png` — 30 frames.

Secondary construction primitives:
- `particles/opague/fire_01.png` + paired alpha;
- `particles/opague/flame_03.png` + paired alpha;
- `particles/opague/spark_02.png` + paired alpha;
- `particles/opague/light_01.png` + paired alpha;
- `particles/opague/flare_01.png` + paired alpha.

The full verified bundle remains available for alternate smoke/explosion/light/electric construction.

## 3. Structural QA completed

Asset Forge v0.9 now treats VFX grids as fixed-registration source structures.

Full real-bundle QA confirms:
- **28** predrawn/flipbook grid sheets;
- **1,318** declared source frames;
- all 28 sheets can be split and reconstructed with **0 pixel difference** when source padding and palette transparency are preserved;
- **92** particle color sources have matching alpha-mask partners;
- one additional alpha-only smoke variant exists (`smoke_07_strong_a`).

Three sheets contain small intentional trailing canvas padding rather than evenly divisible raw dimensions:
- `star_explosion_6x5.png` — 4 transparent bottom rows;
- `impact_white_6x4.png` — 1 transparent bottom row;
- `flame_02_15x4.tga` — 8 transparent right columns.

Forge preserves that padding and processes only the declared active grid rectangle. The filename-declared frame count remains authoritative for those sheets.

Palette-mode predrawn sheets also retain source palette/transparency metadata during reconstruction.

## 4. B06 style target

The final B06 language should read as Diyse-native **seinen HD-2D fantasy fire/light**, not as generic stock particle effects.

Required behavior:
- bold readable flame/fire silhouettes;
- bright cores with restrained or absent line pressure;
- painterly/graphic internal massing rather than high-frequency noise;
- selective chaotic variable line only on useful dark flame folds, smoke overlaps, ember trails or impact edges;
- warm local spill that integrates into the HD-2D environment;
- bloom restrained enough that fixture/flame geometry remains visible;
- sparks/embers used as accents rather than a constant screen-filling particle cloud;
- field/battle readability maintained at actual runtime scale.

Reject:
- uniform black outline around every flame shape;
- flat orange recolor of source VFX;
- generic mobile-game glow overload;
- independently redrawn animation cells that flicker or drift;
- altered grid registration/frame order;
- destructive alpha reconstruction where additive RGB fire already works correctly.

## 5. RGB fire rule

The four RGB `fire_0X_8x8` flipbooks contain no alpha channel.

They must first be tested through additive/emissive shader treatment in Godot. Do **not** invent alpha merely because RGBA assets are easier to preview.

If runtime additive treatment reads correctly, preserve the original RGB structure and style primarily through color/value/emission behavior.

## 6. Animation treatment rule

B06 should use a structure-preserving treatment:

`SOURCE SHEET → DECLARED GRID RESOLUTION → ANCHOR/SHADER STYLE DECISION → WHOLE-FAMILY PROPAGATION → EXACT REPACK → TEMPORAL QA → RUNTIME TEST`

Do not send 30–64 cells through unrelated generation calls.

Any AI-assisted restyle should be applied through controlled anchors or family-level transforms while the source motion/registration remains fixed.

## 7. First visual pilot scope

The first Diyse B06 style candidate should validate a deliberately small set:
1. one looping open flame (`flame_01_16x4`);
2. one fuller fire body (`fire_01_8x8` additive/emissive path);
3. one fire-ring effect;
4. one dithered/ground-fire effect;
5. one spark primitive + one soft light/flare primitive;
6. neutral, warm-environment and cool/night scene contexts;
7. field scale and battle scale.

This is enough to define the fire/light grammar before treating the wider VFX library.

## 8. Source review evidence

A deterministic technical source board was produced from actual bundle frames during the 2026-08-31 working session:

`DIYSE_B06_CC0_FIRE_LIGHT_SOURCE_REVIEW_V1.png`

The board is source/technical evidence only. It is **not** a style-pass candidate and contains no approval authority.

## 9. Promotion gate

Current state:

`QUEUED → SOURCE ANALYSIS COMPLETE → TECHNICAL STYLE PILOT READY`

B06 may advance to `STYLE-PASS CANDIDATE` only after:
- a real Diyse-styled fire/light treatment exists;
- animation/flicker QA passes;
- additive/emissive behavior is tested where relevant;
- alpha fringes are clean;
- the effect reads correctly at actual field/battle scale;
- the visual result is explicitly reviewed.

Do not mark B06 STYLE-PASS from source quality alone.
