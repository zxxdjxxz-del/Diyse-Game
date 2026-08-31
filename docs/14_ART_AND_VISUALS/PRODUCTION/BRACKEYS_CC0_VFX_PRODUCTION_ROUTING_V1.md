# Diyse — Brackeys CC0 VFX Production Routing v1

**Status:** VERIFIED CC0 SOURCE POOL / PRODUCTION ROUTING READY  
**Intake authority:** `ASSET_LIBRARY/VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`  
**Style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Conversion authority:** `ASSET_STYLE_CONVERSION_PIPELINE.md`

## Purpose

Route the verified-CC0 Brackeys VFX bundle into Diyse production by function while preserving its useful technical structure.

This document does **not** style-approve the source art. It identifies where the source can reduce production cost and where Diyse-original treatment remains required.

## 1. B06 — Fire / Light Emitter

Primary source candidates:
- `flipbooks/fire_01_8x8.tga`
- `fire_02_8x8.tga`
- `fire_03_8x8.tga`
- `fire_04_8x8.tga`
- `flame_01_16x4.tga`
- `flame_02_15x4.tga`
- `predrawn/fire_ring_6x5.png`
- `fire_point_6x5.png`
- `dithered_fire_6x5.png`
- flame/fire particle primitives;
- spark, flare, light and spotlight particles.

B06 should compare these clean-provenance candidates with the earlier Map092 reference functionality.

Preferred route:
1. select one fire flipbook as the motion/cadence anchor;
2. preserve frame grid and timing;
3. apply Diyse color/value/edge treatment without per-cell independent hallucination;
4. test additive/emissive rendering for the RGB fire flipbooks before constructing alpha;
5. validate neutral/warm/night scene readability and restrained bloom;
6. keep bright flame core mostly line-free;
7. add variable dark accents only on selected outer flame breakup where useful.

## 2. B09 — Ritual / Magic Surface

Useful construction components:
- `predrawn/wavy_purple_6x5.png`;
- `wavy_blue_6x5.png`;
- `electric_ring_6x5.png`;
- `vortex_6x5.png`;
- `charge_7x6.png`;
- magic particles;
- symbol particles;
- twirl particles;
- star particles;
- sparks/electric energy primitives.

These may supply motion, glow, particles and transition components.

They do **not** define final Diyse ritual geometry. B09 still requires authored original sigil hierarchy/composition rather than importing a generic stock magic-circle identity.

## 3. Combat impact VFX pool

High-value reusable candidates:
- `big_hit_6x5`;
- `impact_white_6x4`;
- `blood_impact_6x5`;
- `star_explosion_6x5`;
- `explosion_6x5`;
- explosion flipbooks;
- slash particles;
- spark particles;
- scorch particles;
- smoke particles/flipbooks;
- dirt/debris particles;
- trace particles.

Potential Diyse uses include:
- physical-hit confirmation;
- Crit emphasis;
- Bleed hit feedback without turning Bleed itself into direct damage;
- Fire/Ice/Lightning/other supported elemental impact layering;
- breakable/environment impacts;
- boss attack staging;
- Prime manifestation/support effects where canon-appropriate.

Effect reuse should be parameterized by scale, rotation, tint, timing, distortion and secondary particles rather than cloning every source effect as a separate bespoke asset.

## 4. Particle color + alpha pairing

The source contains **92 matched color/alpha particle pairs**.

Production rule:
- treat each pair as one logical asset;
- preserve identical registration;
- color treatment may change RGB appearance;
- alpha treatment should remain structure-preserving;
- never independently redraw the mask and color source;
- QA should compare silhouette/fringe behavior after conversion.

The extra alpha-only `smoke_07_strong_a` is a legitimate alternate mask variant, not a missing-color error.

## 5. Spritesheet/flipbook rule

The source contains **28 grid-encoded animation sheets / 1,318 implied frames**.

Do not split and independently generate all 1,318 frames.

Preferred production paths, in order:
1. shader/color/material restyle of the intact sheet;
2. anchor-cell/profile treatment propagated structurally across cells;
3. atlas-safe fixed-coordinate patch processing if needed;
4. only use manual per-cell intervention for isolated failures.

Every output must preserve:
- exact sheet dimensions where runtime registration depends on them;
- column/row count;
- frame order;
- alpha/additive behavior;
- temporal cadence;
- loop continuity where relevant.

## 6. VFX Diyse grammar — provisional

Until the dedicated effect benchmarks are approved, verified CC0 VFX candidates should target:
- strong readable outer motion silhouette;
- 2–4 dominant value/color zones before fine particles;
- bright cores with minimal or no dark line;
- selective chaotic variable line only at darker outer breakup, debris or impact edges;
- deliberate asymmetry;
- restrained bloom;
- controlled particle count;
- no uniform toon outline;
- no glossy gacha-style rainbow overload;
- no noisy full-screen particle fog that obscures combat readability.

## 7. Next validation order

When texture intake is complete enough to resume benchmark production:

1. B04 animated vegetation remains next in the existing benchmark sequence unless explicitly reordered;
2. B06 should use the verified CC0 fire/particle pool as a major source set;
3. B09 should use its magic/energy components as building blocks while retaining original Diyse sigil composition;
4. combat-impact VFX should receive a separate small gameplay-scale readability pass after the core material grammar stabilizes.

## Decision

> **Brackeys VFX bundle is approved as a verified-CC0 source pool, not as unmodified Diyse-final art.**

Direct final use is allowed by provenance, but visual/runtime promotion still requires the active Diyse style and gameplay gates.
