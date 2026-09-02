# 14_ART_AND_VISUALS
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written authority:** **v2.20 / Audit135** plus newer explicit visual approvals/corrections already accepted in the project conversation.  
**Inherited presentation authority:** Audit86 Cyanis exact visual lock, Audit87 HD-2D production grammar, Audit88 compatible Chapters 0–4 production conversion, Audit111 final world-map visual/spatial authority.  
**Runtime checkpoint:** `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Visual rule:** the newest explicitly approved visual reference for a character/location controls all derivative field sprites, battle sprites, portraits, cut-ins, model sheets, and promotional derivatives unless that exact visual is later revised.

Canonical home for:
- exact character appearance authority;
- portrait/sprite derivation rules;
- HD-2D presentation grammar;
- environment visual families;
- world-map visual authority handoff;
- VFX presentation tiers;
- element/Face/Card/Prime visual language;
- production-scale visual reuse rules;
- asset inventory and provenance routing;
- retired visual concepts;
- open visual-production work.

## Active visual target

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight**

Full rendering/style authority:

`DIYSE_VISUAL_STYLE_CANON.md`

This keeps HD-2D as the presentation framework while locking a more specific art identity: mature seinen character language, expressive thick-to-thin/broken/irregular linework, graphic shape-first environments, cinematic atmosphere, and graphic readable VFX.

Older active `2.5D`, `3D`, pixel-art-first, or generic clean-anime direction is retired as the production target.

Diyse may use pixel-scale field/battle sprites as part of HD-2D presentation, but:
> the game's identity is not a retro pixel-art reinterpretation of the approved character masters.

## Character master policy
The currently approved anime-inspired white-background studio renders are **appearance authorities**.

In-game derivatives may simplify:
- line count;
- ornament density;
- micro-texture;
- tiny jewelry detail;
- strand-level hair detail;

only where output scale requires it.

They may not casually change:
- apparent age;
- ethnicity/skin tone;
- face identity;
- hair identity;
- silhouette;
- primary palette;
- iconic equipment/clothing language;
- body proportion;
- established scars/major features.

The new style authority changes **rendering treatment**, not previously approved character identity.

## Asset style-conversion authority

The practical pipeline for turning the current source/reference and CC0 libraries into the locked style is:

`PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`

It controls:
- provenance lanes;
- repaint/rebuild order;
- chaotic line application;
- environment/material conversion;
- HD-2D integration tests;
- runtime-scale checks;
- originalization/faction identity;
- conversion grades (`REF`, `PROTO`, `STYLE-PASS`, `DIYSE-FINAL`, `REPLACE`);
- reusable production prompts.

## Asset Forge automation

The implementation tool for scaling repetitive conversion work is:

`PRODUCTION/ASSET_FORGE_AUTOMATION.md`

Code:

`../../tools/asset_forge/forge.py`

Asset Forge inventories, hashes, classifies, plans, generates/preserves, QA-checks, and builds deterministic review sheets from actual output files. It does **not** override the style canon or conversion authority, and it does not independently redraw atlas/animation frames where doing so would damage seams or frame consistency.

The image model creates asset candidates; the Forge builds exact review boards and tracks technical metadata.

## Active benchmark gate

Before broad asset conversion begins, the locked style must be proven on the representative benchmark set at:

`PRODUCTION/STYLE_BENCHMARK_SET_V1.md`

The benchmark covers stone, rustic wood/interior materials, trees, animated grass, water/splash, fire/fireplace, cave materials, high-status interiors, ritual/magic surfaces, verified-CC0 props, and one fully original Black Host modular architecture piece.

> **Do not bulk-convert the 3,214-file environment library until the benchmark set reads as one coherent game at actual gameplay scale.**

Accepted benchmark results become the basis for a later Diyse Visual Material Grammar controlling broad conversion work.

## Asset library authority
The authoritative production inventory and provenance routing live at:

`PRODUCTION/ASSET_LIBRARY/README.md`

The current preserved inventory is **DIYSE Asset Library Master v5**, including the exact source-archive checksum manifest and byte-identical split preservation of the full master inventory.

The asset library records what source material exists, what is verified CC0 versus license-unverified reference material, and what production capabilities the library can support. It does **not** override the active visual style, exact character/location visual authority, environment-language rules, or newer explicit visual approvals. Assets must be adapted, replaced, or rebuilt where necessary to satisfy current Diyse art direction.

## Image-file boundary
This migration records visual authority and production rules.

It does **not** fabricate replacement image binaries for approved masters that are not physically present in this artifact package.
