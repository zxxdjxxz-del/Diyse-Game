# Diyse — B06 Fire / Light Emitter Execution v1

**Benchmark:** B06 — Fire / Light Emitter  
**Status:** **SOURCE ANALYSIS COMPLETE / TECHNICAL PRESERVATION PROOF COMPLETE / ANIME STYLE PILOT REQUIRED**  
**Primary verified-open source:** `../ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Forge VFX processor:** `../../../../../tools/asset_forge/vfx_processing_engine.py`

## 1. Source decision

B06 should use the verified-CC0 Brackeys VFX bundle as its primary production source pool rather than relying mainly on the license-unverified Map092 fire material.

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

Asset Forge v0.9 treats VFX grids as fixed-registration source structures.

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

## 4. Locked B06 visual target — anime/seinen first

The final B06 language must read as **Diyse-native mature seinen anime VFX integrated into HD-2D lighting**, not as realistic stock fire, a painterly texture filter, or generic mobile-game particles.

Diyse environments may use painterly shape-first rendering, but character and VFX identity must still belong unmistakably to the same anime/seinen visual world.

Required behavior:
- bold readable anime flame/fire silhouettes;
- **3–5 large cel-like graphic value/color masses** rather than soft photographic gradients;
- deep ember/red → orange → gold → pale cream core hierarchy;
- hand-drawn-looking asymmetry and shape breaks;
- bright cores with restrained or absent line pressure;
- selective chaotic variable-line accents on useful dark outer folds, smoke overlaps, ember trails, impact edges or contact pockets;
- those accents should taper, break, bunch or disappear rather than forming a uniform contour;
- warm local spill integrated through HD-2D runtime lighting;
- restrained bloom so flame/fixture geometry remains visible;
- sparks/embers as intentional accents rather than constant screen-filling noise;
- strong field/battle readability against the approved anime character presentation.

Reject:
- realistic/photo-like fire left largely intact;
- soft painterly filtering presented as the anime style pass;
- uniform black outline around every flame shape;
- cheap flat cel shading with no depth or material integration;
- flat orange recolor of source VFX;
- generic gacha/mobile glow overload;
- independently redrawn animation cells that flicker or drift;
- altered grid registration/frame order;
- destructive alpha reconstruction where additive RGB fire already works correctly.

## 5. Technical preservation proof — visual rejection recorded

A first deterministic treatment was run on `flame_01_16x4`.

It successfully proved:
- 2048×1024 source canvas retained;
- 16×4 / 64-frame registration retained;
- source alpha retained **exactly**;
- frame-luminance rhythm correlation **0.9884485553**;
- peak temporal amplification **1.2963046945×** under the declared 1.35 cap.

However, user review correctly identified the visual result as **too painterly/material-filter-like and insufficiently anime/seinen**.

That treatment is therefore retained only as a technical preservation proof. Its former STYLE-PASS CANDIDATE promotion is retired.

Authority:
`B06_FLAME_STYLE_PASS_CANDIDATE_V1.md`

Despite the legacy filename, that file now explicitly records:
> **TECHNICAL PRESERVATION PROOF / VISUAL STYLE REJECTED — INSUFFICIENTLY ANIME/SEINEN**

## 6. RGB fire rule

The four RGB `fire_0X_8x8` flipbooks contain no alpha channel.

They must first be tested through additive/emissive shader treatment in Godot. Do **not** invent alpha merely because RGBA assets are easier to preview.

If runtime additive treatment reads correctly, preserve the original RGB structure and style primarily through color/value/emission behavior.

## 7. Animation treatment rule

B06 should use a structure-preserving treatment:

`SOURCE SHEET → DECLARED GRID RESOLUTION → ANIME STYLE ANCHOR/SHADER DECISION → WHOLE-FAMILY PROPAGATION → EXACT REPACK → TEMPORAL QA → RUNTIME TEST`

Do not send 30–64 cells through unrelated generation calls.

Any AI-assisted restyle, if later used, must operate from a tightly isolated visual anchor and must not receive benchmark/status/dashboard context. Review boards remain deterministic and are built from actual outputs.

## 8. Replacement visual pilot scope

The next B06 visual candidate must first prove the corrected anime/seinen grammar on:
1. one looping open flame (`flame_01_16x4`);
2. **only after that is approved**, one fuller fire body (`fire_01_8x8` additive/emissive path);
3. fire ring;
4. dithered/ground fire;
5. one spark primitive + one soft light/flare primitive;
6. neutral, warm-environment and cool/night contexts;
7. field scale and battle scale.

The first item is the immediate visual gate. Do not propagate an unapproved treatment across the wider VFX library.

## 9. Source review evidence

A deterministic technical source board was produced from actual bundle frames during the 2026-08-31 working session:

`DIYSE_B06_CC0_FIRE_LIGHT_SOURCE_REVIEW_V1.png`

The board is source/technical evidence only. It is **not** a style-pass candidate and contains no approval authority.

The previous `flame_01` comparison files are also technical evidence only after the visual rejection.

## 10. Promotion gate

Current corrected state:

`QUEUED → SOURCE ANALYSIS COMPLETE → TECHNICAL PRESERVATION PROOF COMPLETE → ANIME STYLE PILOT REQUIRED`

B06 may advance to `STYLE-PASS CANDIDATE` only after:
- a real anime/seinen Diyse fire/light treatment exists;
- user visual review accepts that treatment;
- animation/flicker QA passes;
- additive/emissive behavior is tested where relevant;
- alpha fringes are clean;
- the effect reads correctly at actual field/battle scale.

Do not mark B06 STYLE-PASS from technical QA or source quality alone.
