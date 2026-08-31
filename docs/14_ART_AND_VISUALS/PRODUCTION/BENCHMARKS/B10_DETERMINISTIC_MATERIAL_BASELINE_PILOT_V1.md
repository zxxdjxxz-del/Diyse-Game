# Diyse — B10 Deterministic Material Baseline Pilot v1

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** TECHNICAL PILOT PASS / VISUAL STYLE-PASS NOT YET APPROVED  
**Date:** 2026-08-31  
**Source:** Quaternius Fantasy Props MegaKit [Standard] — verified CC0

## Purpose

Run the first real B10 production-output pilot without depending on unconstrained image generation.

The pilot tests whether the shared Furniture and Metal trim atlases can be transformed while preserving exact UV registration, then reused on the actual Barrel, Chair_1, Lantern_Wall, and Workbench glTF models.

## Pipeline used

1. extract the real glTF models and shared texture dependencies from the CC0 ZIP;
2. preserve the original glTF geometry and UV coordinates;
3. apply the deterministic UV-safe `material_style_engine.py` to the Furniture and Metal BaseColor sheets;
4. retain original Normal and ORM maps for this baseline test;
5. render the four actual glTF models through `model_render_engine.py`;
6. validate neutral model presentation using a Y-up camera;
7. use warm/cool render modes for lighting checks;
8. use a validation-only emissive hint for Lantern_Wall until a real emissive mask/material is authored.

This baseline spends **zero image-generation calls**.

## Technical results

### UV registration

**PASS.**

The deterministic material backend does not move, crop, resize, or regenerate texture geometry. Every output pixel remains at the same atlas coordinate as the source.

### Model reuse

**PASS.**

The same styled Furniture and Metal BaseColor sheets successfully render across the representative real models:
- Barrel;
- Chair_1;
- Lantern_Wall;
- Workbench.

### Renderer orientation

The first validation render exposed an incorrect camera presentation for upright furniture. The renderer was corrected to use glTF's +Y up convention and a stable three-quarter review camera.

The corrected Chair_1 and Workbench renders are upright and readable.

### Material identity

**PASS as technical baseline.**

The deterministic treatment provides:
- grouped wood values;
- stronger dark construction/grain accents;
- darker neutral iron/metal;
- preserved readable material separation;
- no universal post-process toon-outline shell.

## Full 94-prop pack material reuse finding

A full glTF dependency scan of the verified CC0 pack found **94 models** and only a small set of major shared BaseColor trim families.

Model usage by major BaseColor family:
- `T_Trim_Metal_BaseColor.png` — **60 models**;
- `T_Trim_Furniture_BaseColor.png` — **41 models**;
- `T_Trim_Props_BaseColor.png` — **39 models**;
- `T_Trim_Cloth_BaseColor.png` — **10 models**.

A small page/noise family is used by only two models and is not part of the main reusable prop-material grammar.

This strongly validates a **material-first conversion strategy**: a handful of approved shared-material treatments can affect most of the 94-prop library before any model-specific override work begins.

## B10 four-prop shared-material finding

For the four benchmark props specifically:
- Barrel uses Furniture + Metal;
- Chair_1 uses Furniture + Metal;
- Lantern_Wall uses Metal;
- Workbench uses Furniture + Metal.

Therefore the representative benchmark's BaseColor identity is controlled primarily by only **two shared material sheets**.

## Visual findings — baseline strengths

The baseline already demonstrates several useful Diyse traits:
- Barrel reads clearly with darker metal hoops and grouped warm wood;
- Chair silhouette remains clean and legible after the material transformation;
- Workbench retains its broad work-surface read;
- dark edge accents come from material structure rather than a constant outer contour;
- the treatment scales across different geometry without unique repaint work per model.

## Visual findings — refinement still required

Do **not** promote this baseline directly to B10 STYLE-PASS yet.

### Wood

Current deterministic wood is useful but can still become too line-dense where the original trim sheet already contains repeated grain marks.

Refinement target:
- suppress more low-value repeated grain at gameplay distance;
- keep heavier dark accents concentrated at joints, damage, and high-value grain turns;
- preserve larger quiet painterly wood planes.

### Metal

Current deterministic metal is readable but too uniformly charcoal in some regions.

Refinement target:
- strengthen controlled plane/highlight separation;
- retain darker recessed/joint accents;
- allow sparse cool or warm reflected highlights;
- avoid making every etched source line equally dark.

### Lantern emissive

The current warm glow is a **renderer validation hint only**.

Before B10 approval, Lantern_Wall needs:
- an authored emissive mask or material region;
- a bright core that remains mostly free of dark ink;
- restrained warm spill/bloom;
- bright-scene and dark-scene validation.

### PBR integration

Normal and ORM maps were intentionally left unchanged in this baseline.

The next runtime test must determine whether:
- original Normal maps remain compatible with the painterly BaseColor treatment;
- original ORM data is too glossy/strong;
- roughness/metallic values need a Diyse-specific rebalance.

## Decision

**B10 deterministic shared-material pipeline: PASS.**

**B10 final visual style: NOT YET APPROVED.**

The important production conclusion is now locked:

> Shared 3D prop libraries should be converted material-first, not model-first.

The next B10 refinement pass should focus on:
1. gameplay-scale wood line-density reduction;
2. stronger controlled metal value/highlight grammar;
3. real Lantern_Wall emissive authoring;
4. original Normal/ORM compatibility test;
5. neutral/warm/cool four-prop review renders;
6. deterministic review sheet from those actual renders.
