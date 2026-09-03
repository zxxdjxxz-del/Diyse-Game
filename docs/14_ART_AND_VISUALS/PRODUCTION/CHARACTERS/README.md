# Diyse Character Visual Authority Index

This folder is the canonical production index for Diyse character visual locks.

## Authority order

When character visual sources disagree, use this order:

1. **The current repository master image** in [`asset_sources/characters/current/`](../../../../asset_sources/characters/current/).
2. **The matching `*_CURRENT_VISUAL_LOCK.md` file** in this folder.
3. Current approved project-wide B00 / HD-2D anime style rules.
4. Older prose descriptions, archived renders, generated filenames, historical hashes, or superseded concept notes.

The repository master image controls exact face, body proportions, hair, clothing/armor construction, equipment placement, palette, silhouette, and incidental visual minutiae. A lock document may explain intent and prohibited regressions, but it must never override the current master image.

Do not infer or add surnames that are not explicitly canonical. Current repository filenames use the characters' actual names only.

## Permanent party — current visual masters

| Character | Master image | Visual lock |
| --- | --- | --- |
| Cyanis | [`cyanis.jpg`](../../../../asset_sources/characters/current/cyanis.jpg) | [`CYANIS_CURRENT_VISUAL_LOCK.md`](CYANIS_CURRENT_VISUAL_LOCK.md) |
| Ilyra | [`ilyra.jpg`](../../../../asset_sources/characters/current/ilyra.jpg) | [`ILYRA_CURRENT_VISUAL_LOCK.md`](ILYRA_CURRENT_VISUAL_LOCK.md) |
| Torren | [`torren.jpg`](../../../../asset_sources/characters/current/torren.jpg) | [`TORREN_CURRENT_VISUAL_LOCK.md`](TORREN_CURRENT_VISUAL_LOCK.md) |
| Nimera | [`nimera.jpg`](../../../../asset_sources/characters/current/nimera.jpg) | [`NIMERA_CURRENT_VISUAL_LOCK.md`](NIMERA_CURRENT_VISUAL_LOCK.md) |
| Vaelira | [`vaelira.jpg`](../../../../asset_sources/characters/current/vaelira.jpg) | [`VAELIRA_CURRENT_VISUAL_LOCK.md`](VAELIRA_CURRENT_VISUAL_LOCK.md) |
| Seyrik | [`seyrik.jpg`](../../../../asset_sources/characters/current/seyrik.jpg) | [`SEYRIK_CURRENT_VISUAL_LOCK.md`](SEYRIK_CURRENT_VISUAL_LOCK.md) |

These six are the permanent playable party and should be treated as one coherent B00 character-production set.

## Supporting characters — current visual masters

| Character | Master image | Visual lock |
| --- | --- | --- |
| Maevra | [`maevra.jpg`](../../../../asset_sources/characters/current/maevra.jpg) | [`MAEVRA_CURRENT_VISUAL_LOCK.md`](MAEVRA_CURRENT_VISUAL_LOCK.md) |
| Kessara | [`kessara.png`](../../../../asset_sources/characters/current/kessara.png) | [`KESSARA_CURRENT_VISUAL_LOCK.md`](KESSARA_CURRENT_VISUAL_LOCK.md) |

Maevra and Kessara have current authoritative visual masters but are **not part of the permanent six-character party**.

## Downstream character derivatives

Current masters are now the source layer for purpose-specific derivatives; derivatives never become replacement identity masters.

Portrait production is controlled by:
- [`PORTRAIT_DERIVATIVE_PIPELINE.md`](PORTRAIT_DERIVATIVE_PIPELINE.md) — derivative rules and runtime handoff;
- [`PORTRAIT_PRODUCTION_MANIFEST.md`](PORTRAIT_PRODUCTION_MANIFEST.md) — current source readiness and approved derivative tracking.

Source/output lanes:
- `asset_sources/characters/derivatives/dialogue/` — dialogue portrait/bust derivatives;
- `asset_sources/characters/derivatives/ui/` — menu/status/party portrait derivatives.

The dialogue runtime already supports stable semantic `character_id` + `expression_id` lookup through `DiyseDialoguePortraitRegistry`. Production portraits should enter through that indirection after approval rather than wiring story data directly to B00 image paths.

The current SVG portraits in `game/characters/placeholders/portraits/` remain proof-only stand-ins. They are not production derivatives and do not compete with the current masters.

## Production rules

- Use only the target character's authoritative master as the subject/identity reference for redraws.
- Other approved character masters may guide shared B00 technique and cohesion, never subject identity, palette, costume, equipment, or props.
- Preserve exact left/right equipment placement when the master establishes it.
- For a clean redraw, rebuild rather than patching an older image.
- Do not revive superseded character designs merely because an older document or render contains more detail.
- Derived runtime assets may simplify for HD-2D production, but must remain recognizably faithful to the current master.
- Never overwrite/resave a current master as part of a derivative crop, expression, transparency, resize, or export pass.

## Current B00 direction

The shared character-side target is Diyse's established mature anime / seinen-inspired HD-2D presentation: deliberate variable line weight, graphic cel-informed value grouping, readable materials and silhouettes, clean anatomy, restrained artifact-free detail, and no painterly or glossy mobile-gacha finish.

This index should be updated whenever a character master is explicitly replaced or a new authoritative visual master is added.
