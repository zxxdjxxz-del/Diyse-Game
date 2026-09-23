# Diyse — Art & Visual Master

**Status:** ACTIVE ART/VISUAL NAVIGATION AUTHORITY  
**Rendering authority:** `DIYSE_VISUAL_STYLE_CANON.md`  
**Current character authority:** `PRODUCTION/CHARACTERS/README.md`  
**Current character masters:** `../../asset_sources/characters/current/`  
**Character runtime gate:** `PRODUCTION/BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

This document is a top-level visual routing guide. Exact character and location masters control identity; the style canon controls shared rendering language; production documents control runtime translation and asset workflows.

## Active rendering style

The current canonical rendering style is:

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**

Full style authority:

`DIYSE_VISUAL_STYLE_CANON.md`

Production conversion guide:

`PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`

**Painterly is retired from the active Diyse art direction.** Do not use painterly treatment as a production target, review criterion, or conversion requirement unless explicitly reintroduced later.

## Style pillars

- mature seinen-inspired character language;
- chaotic variable line weight with tapered, broken, irregular authored strokes;
- graphic cel-informed value grouping;
- clean, readable silhouettes;
- graphic shape-first environments/materials with selective ink accents;
- cinematic HD-2D depth, atmosphere, and lighting;
- rich but controlled color;
- graphic readable magical/combat VFX;
- restrained detail and controlled noise;
- readable JRPG battle staging;
- authored visual depth rather than photoreal simulation.

## Character master policy

The current repository image masters in `asset_sources/characters/current/` are the exact operational appearance authorities for the characters represented there.

Use the authority order in `PRODUCTION/CHARACTERS/README.md`:
1. newest explicit user-approved exact source image;
2. registered exact approved fingerprint;
3. repository master binary matching that fingerprint;
4. matching current visual-lock document;
5. current B00 / visual-style rules;
6. older prose, archived renders, old hashes, generated filenames, or superseded concepts.

Current permanent-party masters:
- Cyanis;
- Ilyra;
- Torren;
- Nimera;
- Vaelira;
- Seyrik.

Current supporting masters in the same repository set:
- Maevra;
- Crown Princess Mirena Ceryth;
- Kessara.

Do not infer additional surnames for these characters from retired migration filenames or older art documents.

## Enemy visual authority

Current enemy visual index:
> `ENEMIES/README.md`

Chapter 0 locked enemy design authority:
> `ENEMIES/CHAPTER_00_ENEMY_VISUAL_AUTHORITY.md`

These files control silhouette, anatomy, armor/clothing/material language, palette family, signature visual read, movement presentation, and prohibited design drift. Enemy combat data remains in `../09_ENEMIES_AND_ENCOUNTERS/`.

## Character reference format

High-resolution character masters use a clean studio/reference presentation when appropriate so face, age read, costume, silhouette, proportions, palette, and equipment placement remain easy to judge. The exact repository image—not the background convention—is the authority.

## In-game character presentation

Primary field and battle character presentation follows the active **rigged 3D model** B00 direction.

The former dedicated approximately **80 px field** and **200–220 px battle** sprite targets are retired as required production gates. Historical 2D simplification principles may still guide optional derivatives, but they do not define the active runtime plan or character identity.

Runtime characters must be checked at actual field and battle camera distances. Simplify with mesh/material LOD, outline tuning, authored secondary-motion budgets, and screen-space readability treatment while preserving the exact master-controlled identity.

Dialogue, portraits, menus, Cards/Primes, illustrated cut-ins, promotional art, and other deliberately 2D presentations may continue to use high-resolution 2D character art.

## Battle composition

Standard battle staging remains:
- party left;
- enemies right;
- open center lane for actions/VFX.

Active party maximum:
> **4**

## Environment composition

Prefer:
- authored layered backgrounds;
- graphic shape-first material treatment;
- selective chaotic ink accents rather than uniform outlines;
- foreground/midground/background depth;
- modest/selective parallax;
- selective geometry;
- prop-state swaps and before/after states;
- controlled camera framing;
- reusable battle-background families;
- atmospheric perspective and directional lighting.

Avoid defaulting to:
- giant seamless modeled cities when authored segmentation is clearer;
- fully simulated crowds where staged representation is sufficient;
- unnecessary physics destruction;
- photorealistic texture-pack noise;
- glossy mobile-gacha rendering;
- uniform sterile digital linework;
- random speckle/grunge as detail.

Secondary motion, cloth, hair, and foliage simulation may be used selectively when stable, readable, and justified by the runtime budget; they are not visual goals by themselves.

## Asset conversion

Existing source/reference assets are not visually upgraded merely because they are enlarged or sharpened. Conversion must follow:

`PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`

The conversion process must improve shape/value hierarchy, material readability, palette cohesion, authored irregularity, line character where relevant, HD-2D scene compatibility, gameplay-distance clarity, and Diyse identity/originalization where appropriate.

## Exact-master rule

If a textual summary conflicts with the current approved repository image:
> **the current repository master image wins for appearance**

unless a newer explicit approval intentionally replaces that master.
