# 14_ART_AND_VISUALS

Canonical home for Diyse's active visual authorities, production rules, environment language, character master routing, VFX presentation, asset provenance, and retired-concept firewalls.

## Active visual target

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**

Full rendering/style authority:

`DIYSE_VISUAL_STYLE_CANON.md`

Top-level art routing:

`ART_VISUAL_MASTER.md`

The style authority controls **how** designs are rendered. Exact approved visual masters control **what the designs are**.

Older pixel-art-first, generic clean-anime, photoreal, painterly/soft-brushed, or glossy mobile-gacha directions are not the active production target.

## Current character authority

Canonical character-production index:

`PRODUCTION/CHARACTERS/README.md`

Current repository master images:

`../../asset_sources/characters/current/`

Current image-master set:
- permanent party — Cyanis, Ilyra, Torren, Nimera, Vaelira, Seyrik;
- additional current masters — Maevra and Kessara.

Maevra is supporting/recurring allied command. Kessara has a current authoritative visual master; this art index does not assert a story role for her. Neither is part of the permanent six-character party.

For these characters, use this authority order:
1. current repository master image;
2. matching current visual-lock document;
3. current B00 / Diyse visual-style rules;
4. older prose, archived renders, historical hashes, generated filenames, and superseded concepts.

Do not infer or restore surnames for the eight current master characters from retired migration filenames.

The repository master controls exact face, body proportions, hair, clothing/armor construction, equipment placement, palette, silhouette, and incidental visual minutiae. The lock document records intent, production constraints, and prohibited regressions without overriding the image.

## Character runtime direction

The active B00 field/battle direction uses **rigged 3D character models** validated against the exact current image masters.

Active runtime gate:

`PRODUCTION/BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

Runtime readability authority:

`PRODUCTION/CHARACTER_SCALE_AND_SILHOUETTE.md`

The former mandatory ~80 px field and ~200–220 px battle sprite targets are retired as production gates. Optional 2D derivatives may still be created where a feature explicitly needs them, but they remain subordinate to the current master and are not a separate character identity.

## Asset style-conversion authority

The practical pipeline for turning source/reference and verified-CC0 libraries into the locked style is:

`PRODUCTION/ASSET_STYLE_CONVERSION_PIPELINE.md`

It controls provenance lanes, rebuild order, line/style application, environment/material conversion, HD-2D integration tests, runtime-scale checks, originalization/faction identity, conversion grades, and reusable production prompts.

**Painterly is retired from the active Diyse art direction.** Conversion work should use the current graphic shape-first / anime-stylized material language defined by `DIYSE_VISUAL_STYLE_CANON.md`.

## Asset Forge automation

Implementation support:

`PRODUCTION/ASSET_FORGE_AUTOMATION.md`

Code:

`../../tools/asset_forge/forge.py`

Asset Forge inventories, hashes, classifies, plans, generates/preserves, QA-checks, and builds deterministic review sheets from actual output files. It does not override the style canon, current master images, character authority index, or conversion authority.

## Benchmark gates

Representative style/material benchmark work lives under:

`PRODUCTION/BENCHMARKS/`

B00 is the permanent-party character benchmark. Other benchmark families cover representative environment/material/prop/VFX requirements before broad propagation.

Do not bulk-promote a source library merely because individual assets are technically usable. Representative benchmarks must first demonstrate that the converted result belongs to the same game at actual gameplay scale.

## Asset library authority

The authoritative production inventory and provenance routing live at:

`PRODUCTION/ASSET_LIBRARY/README.md`

The asset library records what source material exists and its provenance/production role. It does not override active visual style, exact character/location masters, environment-language rules, or newer explicit approvals.

## Retired concepts

Historical visual concepts may remain in Git history or explicitly retired documentation, but must not silently reactivate when they conflict with current authority.

See:

`RETIRED_VISUAL_CONCEPTS_FIREWALL.md`

Current production documents should point forward to active masters and locks rather than depending on obsolete migration filenames or memory-based reconstructions.
