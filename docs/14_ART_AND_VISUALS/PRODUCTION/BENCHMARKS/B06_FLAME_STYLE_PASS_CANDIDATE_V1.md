# Diyse — B06 Flame Technical Preservation Proof v1

**Benchmark:** B06 — Fire / Light Emitter  
**Status:** **TECHNICAL PRESERVATION PROOF / VISUAL STYLE REJECTED — INSUFFICIENTLY ANIME/SEINEN**  
**Source:** verified-CC0 `brackeys_vfx_bundle/flipbooks/flame_01_16x4.tga`  
**Grid:** 16×4 / 64 frames  
**Forge treatment:** `../../../../../tools/asset_forge/vfx_style_engine.py`  
**Source authority:** `../ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

## 1. Authority correction

This file was originally promoted as a B06 STYLE-PASS candidate. That promotion is **retired**.

User review identified the core visual failure: the deterministic treatment moved the stock flame toward a painterly/material-filter look, but Diyse's locked visual authority is **seinen anime HD-2D fantasy with chaotic variable line weight**. The result therefore does not satisfy the same-game visual gate against the approved anime character masters.

The result remains valuable only as proof that Asset Forge can transform a real animation while preserving motion structure.

> **Do not use this v1 flame treatment as B06 art-direction authority.**

## 2. What the proof establishes

The treatment was applied directly to the real 2048×1024, 64-frame `flame_01_16x4` source sheet while preserving:
- canvas size;
- frame order;
- 16×4 grid registration;
- source alpha exactly;
- temporal motion rhythm within the declared QA bounds.

This proves the technical pipeline can alter rendering behavior without independently redrawing 64 frames or destabilizing the animation.

## 3. Technical QA retained

Measured on the actual source:

- source canvas: **2048×1024**;
- frame grid: **16×4**;
- frames: **64**;
- alpha preservation: **EXACT**;
- source/styled frame-luminance rhythm correlation: **0.9884485553**;
- source peak frame-to-frame luminance delta: **0.0081487894**;
- styled peak frame-to-frame luminance delta: **0.0105633140**;
- peak-delta ratio: **1.2963046945**;
- temporal gate: **PASS** (`correlation >= 0.95`, `peak ratio <= 1.35`, exact alpha required).

These measurements are technical evidence only. Passing temporal QA does not imply visual approval.

## 4. Why the visual treatment is rejected

The v1 treatment:
- reduced photographic noise successfully;
- preserved alpha and animation timing successfully;
- but remained too dependent on soft painterly filtering;
- did not establish a sufficiently hand-drawn/cel-shaped anime flame language;
- did not carry Diyse's chaotic tapered/broken line character strongly or deliberately enough;
- could read as a stylized material filter rather than an authored seinen-anime VFX pass.

The rejection is therefore visual, not structural.

## 5. Correct B06 anime/seinen target

The replacement candidate must preserve the technical wins while moving much more clearly toward Diyse's anime identity:

- **3–5 large cel-like flame value/color masses** rather than soft photographic gradients;
- readable deep ember/red → orange → gold → pale cream core hierarchy;
- hand-drawn-looking shape breaks and asymmetry;
- selective chaotic thick-to-thin or broken/tapered dark accents only on useful outer folds, overlap pockets, smoke joins, or impact edges;
- bright cores mostly or completely unoutlined;
- no universal black toon shell;
- controlled emissive spill/bloom added at runtime rather than baked into every edge;
- sparse embers/sparks used compositionally;
- source motion silhouette and registration retained;
- field/battle readability tested against anime character art.

The goal is not cheap flat cel shading. It is **mature seinen anime VFX with HD-2D lighting integration**.

## 6. Session evidence status

The following 2026-08-31 files remain useful only as technical comparison evidence:

- `DIYSE_B06_FLAME01_STYLE_CANDIDATE_V1.png`;
- `DIYSE_B06_FLAME01_SOURCE_VS_STYLE_V1.gif`;
- `DIYSE_B06_FLAME01_FRAME_COMPARE_V1.png`;
- `DIYSE_B06_FLAME01_QA_V1.json`.

They are **not approved visual references**.

## 7. Current promotion state

Corrected state:

`SOURCE ANALYSIS COMPLETE → TECHNICAL PRESERVATION PROOF COMPLETE → ANIME STYLE PILOT REQUIRED`

B06 has **not** reached STYLE-PASS CANDIDATE.

The next visual pilot must first prove the anime/seinen treatment on the real `flame_01_16x4` family. Only after that visual grammar is approved should it be propagated to:
1. `fire_01_8x8` through the RGB additive/emissive path;
2. `fire_ring_6x5`;
3. `dithered_fire_6x5`;
4. spark + soft-light/flare primitives;
5. field-scale and battle-scale compositing.
