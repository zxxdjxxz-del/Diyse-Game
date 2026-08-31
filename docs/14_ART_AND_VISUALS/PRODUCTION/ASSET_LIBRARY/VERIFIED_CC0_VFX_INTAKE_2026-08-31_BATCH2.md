# Diyse Verified CC0 VFX Intake — 2026-08-31 Batch 2

**Status:** INTAKE INVENTORIED / INCLUDED LICENSE VERIFIED CC0 / DIRECT-PRODUCTION CANDIDATE  
**Archive:** `brackeys_vfx_bundle.zip`  
**VFX intake tool:** `../../../../../tools/asset_forge/vfx_intake_engine.py`  
**General ZIP intake:** `../../../../../tools/asset_forge/zip_intake_engine.py`

## 1. Provenance decision

This supplemental archive contains its own `LICENSE & CREDITS.txt`.

The included license states that the assets were repackaged and in some cases modified by Brackeys and declares:

> **LICENSE for all assets: Creative Commons Zero (CC0)**

The included credit record names:
- particle textures — Picster and Kenney;
- flipbooks — Thomas Iché;
- predrawn spritesheets — CodeManu.

This is materially different from Supplemental Texture Batch 1, whose provenance is still pending. Batch 2 may be treated as **verified-open CC0 source material** for Diyse production, modification, redistribution, and direct final-use candidates subject to the active style/runtime gates.

The original included license/credit file should remain preserved with any durable copy of the source bundle.

## 2. Archive identity

- archive: `brackeys_vfx_bundle.zip`
- ZIP bytes: **28,227,919**
- SHA-256: `ac0fbf5d5a07688a5d4d35fd0bbae783597d819a3d8a92893b05eb69ddb144c5`
- raw non-directory ZIP file members: **446**
- macOS metadata/resource-fork members ignored for production intake: **232**
- usable non-metadata members: **214**
- usable image members: **213**
- usable uncompressed bytes: **74,786,895**
- image uncompressed bytes: **74,786,416**
- exact duplicate image groups in the usable asset set: **0**

Usable file types:
- PNG: **199**
- TGA: **14**
- TXT: **1** (`LICENSE & CREDITS.txt`)

## 3. Production structure

The clean VFX payload is divided into three source roles:

### Particle textures

**185 images total**

- color/opaque particle sprites: **92**
- alpha-mask particle sprites: **93**
- matched color + alpha pairs: **92**
- unmatched color sprites: **0**
- alpha-only variants: **1** — `smoke_07_strong_a`

The archive directory spells the color directory `opague`; this is source naming and should not be silently corrected inside provenance records.

All particle source textures are **512×512**.

The paired color/alpha architecture should be preserved through conversion rather than independently restyling the two sides of a pair.

### Predrawn spritesheets

**14 sheets**

Grid metadata is encoded in the filenames:
- most are `6x5` → 30 source frames;
- `impact_white_6x4` → 24 frames;
- `charge_7x6` → 42 frames.

Total implied predrawn source frames: **426**.

Named studies include:
- wavy purple / blue;
- star explosion;
- big hit;
- explosion;
- fire ring;
- light streaks;
- blood impact;
- white impact;
- electric ring;
- vortex;
- charge;
- fire point;
- dithered fire.

These should be treated as fixed-grid animation atlases. Frame registration and grid boundaries must not drift during any style treatment.

### Flipbooks

**14 sheets**

Source grid types:
- `8x8` → 64 frames;
- `16x4` → 64 frames;
- `15x4` → 60 frames.

Total implied flipbook source frames: **892**.

Families include:
- wispy smoke 01–03;
- fire 01–04;
- flame 01–02;
- explosion 01–02;
- explosion smoke 01;
- cloud 01–02.

Most are 1024×1024. The two flame strips are 2048×1024.

## 4. Aggregate animation capability

Across predrawn + flipbook sheets:

- spritesheet assets: **28**
- implied source frames: **1,318**

This does **not** mean Diyse should export 1,318 independent source files. The source sheets should remain atlas/flipbook assets where that is efficient and technically appropriate.

## 5. Broad VFX routing

Filename/path-aware intake resolves the 213 image assets approximately as:

- Magic / arcane: **43**
- Energy / sparks / light: **41**
- Utility / traces / circles / generic effects: **38**
- Impact / explosion / hit / slash: **31**
- Smoke / cloud: **27**
- Fire / flame: **25**
- Debris / scratch / dirt: **8**

These are routing families, not final gameplay-effect identities.

## 6. Image technical profile

Primary dimensions:
- 512×512: **185** — particle textures;
- 1024×1024: **12** — most flipbooks;
- 2048×1024: **2** — flame flipbooks;
- predrawn sheets use varied source dimensions while retaining explicit grid metadata.

Image modes across the 213 usable images:
- RGBA: **140**
- palette/P: **44**
- LA: **13**
- L: **12**
- RGB: **4**

Images with alpha/transparency information detected: **159**.

The four RGB flipbooks are the fire sheets. Their lack of alpha should not be interpreted as a defect; shader/additive treatment may be the intended route and must be tested in Godot rather than normalized blindly.

## 7. Relationship to Diyse benchmarks

This source set materially improves multiple pending visual benchmarks:

### B06 — Fire / Light Emitter

Strongest immediate source value:
- four fire flipbooks;
- two flame flipbooks;
- fire ring / fire point / dithered fire predrawn sheets;
- flame/fire particle primitives;
- sparks, flares, light streaks and spotlight particles.

B06 should now use this verified-CC0 set as a major source/reference pool rather than relying only on the earlier license-unverified Map092 fire source.

### B09 — Ritual / Magic Surface

Useful source material:
- magic particle families;
- wavy purple/blue;
- vortex;
- charge;
- electric ring;
- star/symbol/twirl primitives.

The source may provide effect construction components, but Diyse ritual/sigil geometry still needs authored original composition under the active style canon.

### Combat impact VFX

The bundle also adds useful direct-production candidates for:
- hit flashes;
- explosions;
- blood impact;
- slash shapes;
- muzzle/scorch forms;
- sparks;
- smoke and debris.

These can later support physical attacks, elemental effects, status feedback, environmental breakage, and battle readability without requiring each effect to be generated from scratch.

## 8. Forge routing rule

Asset Forge must preserve source technical structure:

**Particle color/alpha pairs**
- treat as one logical asset pair;
- never independently distort the mask silhouette;
- style color behavior while preserving paired registration;
- validate fringe/alpha behavior at runtime scale.

**Predrawn sheets / flipbooks**
- parse grid columns/rows from filename metadata;
- preserve exact canvas size and cell registration;
- prefer anchor/style propagation or shader/color treatment over independently hallucinating every cell;
- run temporal/flicker QA after conversion;
- do not rearrange frame order.

**RGB fire flipbooks**
- test additive/emissive shader treatment before attempting destructive alpha reconstruction.

## 9. VFX style-direction rule

The source bundle is CC0, but it is **not automatically Diyse-final**.

Diyse conversion should preserve useful motion/silhouette while moving presentation toward:
- mature seinen HD-2D fantasy;
- bold readable effect silhouettes;
- painterly/graphic internal value grouping;
- selective chaotic variable-line influence only where it helps shape/readability;
- bright cores with restrained line pressure;
- controlled bloom and additive energy;
- strong gameplay readability at battle and field scale;
- no generic mobile-game VFX overload;
- no noisy micro-particles simply because the source offers many primitives.

## 10. Storage status

Because the archive includes a CC0 license, it is **eligible for redistributable third-party source storage** under the existing project policy, including a future `asset_sources/third_party_cc0/` durable copy if desired.

Current sandbox upload is **not durable archival storage**.

Open preservation action:
- place the archive and its included license file in a durable approved source location;
- verify the stored archive against SHA-256 `ac0fbf5d5a07688a5d4d35fd0bbae783597d819a3d8a92893b05eb69ddb144c5`.

## 11. Production decision

> **VERIFIED CC0 VFX SOURCE SET — INTAKE COMPLETE / STYLE AND RUNTIME VALIDATION REQUIRED**

This archive should be added to the active verified-open source pool. It does not alter Master v5 counts retroactively; it is a separately inventoried supplemental open-source expansion until the next deliberate Asset Library Master consolidation.
