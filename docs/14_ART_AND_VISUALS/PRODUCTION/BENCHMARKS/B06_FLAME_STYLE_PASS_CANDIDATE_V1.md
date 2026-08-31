# Diyse — B06 Flame Style-Pass Candidate v1

**Benchmark:** B06 — Fire / Light Emitter  
**Status:** **STYLE-PASS CANDIDATE / USER REVIEW PENDING**  
**Source:** verified-CC0 `brackeys_vfx_bundle/flipbooks/flame_01_16x4.tga`  
**Grid:** 16×4 / 64 frames  
**Forge treatment:** `../../../../../tools/asset_forge/vfx_style_engine.py`  
**Source authority:** `../ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

## 1. What this candidate is

This is the first actual Diyse-styled B06 animation treatment. It is not an AI-generated infographic or concept board.

The treatment is applied directly to the real 2048×1024, 64-frame `flame_01_16x4` source sheet while preserving its canvas, frame order, grid registration and alpha channel.

The candidate exists to answer one narrow visual question:

> Can a real production fire animation be pushed toward Diyse's mature painterly/graphic HD-2D language without redrawing its motion or introducing temporal instability?

## 2. Candidate treatment

The v1 transform:
- reduces photographic/high-frequency color noise with a light bilateral treatment;
- remaps fire into broad deep-ember → red-orange → orange → gold → cream value families;
- applies restrained value quantization for painterly/graphic massing;
- adds selective dark accents only on useful outer folds and darker internal transitions;
- deliberately breaks internal dark accents instead of outlining every shape;
- protects bright cores from heavy line pressure;
- preserves source alpha exactly;
- does not move, resize, crop or regenerate any frame.

This is a deterministic treatment. Re-running the same source through the same engine produces the same result.

## 3. Real-sheet technical QA

Measured on the actual `flame_01_16x4` source:

- source canvas: **2048×1024**;
- frame grid: **16×4**;
- frames: **64**;
- alpha preservation: **EXACT**;
- source/styled frame-luminance rhythm correlation: **0.9884485553**;
- source peak frame-to-frame luminance delta: **0.0081487894**;
- styled peak frame-to-frame luminance delta: **0.0105633140**;
- peak-delta ratio: **1.2963046945**;
- temporal gate: **PASS** (`correlation >= 0.95`, `peak ratio <= 1.35`, exact alpha required).

An earlier, more aggressive tuning reached roughly 1.387× peak temporal amplification and was rejected before promotion. The committed v1 candidate uses the softened treatment that passes the declared gate.

## 4. Session review evidence

The 2026-08-31 working session produced the following review artifacts from the real source and deterministic transform:

- `DIYSE_B06_FLAME01_STYLE_CANDIDATE_V1.png` — complete 64-frame styled sheet;
- `DIYSE_B06_FLAME01_SOURCE_VS_STYLE_V1.gif` — animated source-versus-styled proof;
- `DIYSE_B06_FLAME01_FRAME_COMPARE_V1.png` — selected real-frame comparison;
- `DIYSE_B06_FLAME01_QA_V1.json` — measured QA output.

These session files are review evidence, not durable repository binary storage. Repository text remains authority for benchmark status.

## 5. Visual review gate

User review should judge:
- whether the orange/gold/cream hierarchy fits Diyse;
- whether the dark broken accents feel expressive rather than toon-outlined;
- whether the fire remains organic enough despite broader value grouping;
- whether the bright core is appropriately readable without excessive bloom;
- whether the result feels more authored/seinen and less like a stock realistic flipbook;
- whether the treatment remains readable at field and battle scale.

Automatic reject conditions:
- universal black outline;
- flat orange recolor;
- visibly stepped/cheap posterization;
- bright core becoming a static white block;
- temporal pulsing that was not present in the source;
- alpha fringe or registration changes.

## 6. Promotion decision

Current state:

`SOURCE ANALYSIS COMPLETE → TECHNICAL STYLE PILOT READY → STYLE-PASS CANDIDATE / USER REVIEW PENDING`

Do **not** mark B06 STYLE-PASS from this single flame family alone.

If the visual direction is approved, the same grammar should next be validated on:
1. `fire_01_8x8` through its RGB additive/emissive path;
2. `fire_ring_6x5`;
3. `dithered_fire_6x5`;
4. spark + soft-light/flare primitives;
5. field-scale and battle-scale compositing.

Only after those related fire/light families remain coherent should B06 advance to STYLE-PASS.
