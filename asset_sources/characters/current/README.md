# Current Character Visual Masters

This folder is the canonical repository location for the current approved source/reference character master images.

These files are source/reference masters, not runtime deployable assets. Approved downstream source derivatives belong under [`../derivatives/`](../derivatives/) before purpose-specific runtime integration.

For the complete visual-authority hierarchy, permanent-party classification, redraw rules, lock-document index, and portrait derivative pipeline, use [`docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md).

## Authority rule

The image files in this folder are the **exact current visual source of truth**. If an older render, generated filename, historical hash, archived description, derivative portrait, runtime export, or prose detail conflicts with a current master, the current master image wins until the user explicitly replaces it.

Never overwrite/resave these masters as part of crop, transparency, expression, resize, framing, UI, or runtime-export work.

## Permanent party masters

- `cyanis.jpg`
- `ilyra.jpg`
- `torren.jpg`
- `nimera.jpg`
- `vaelira.png`
- `seyrik.jpg`

## Supporting character masters

- `maevra.jpg`
- `kessara.png`

Maevra and Kessara have authoritative current visual masters but are not part of the permanent six-character party.

Canonical filenames use the characters' actual names only. Do not infer or add surnames that are not explicitly canonical.

The original supplied current masters for Cyanis, Ilyra, Torren, Nimera, Seyrik, and Maevra use `.jpg` because their repository source bytes are JPEG/JFIF. Kessara and the **2026-09-12 replacement Vaelira B00 master** are native PNGs and remain `.png` without lossy re-encoding.

## Downstream derivative lanes

- `../derivatives/dialogue/` — approved dialogue portrait/bust derivatives.
- `../derivatives/ui/` — approved menu/status/party portrait derivatives.

Controlling portrait pipeline:
[`PORTRAIT_DERIVATIVE_PIPELINE.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/PORTRAIT_DERIVATIVE_PIPELINE.md)

A downstream derivative never replaces the current master as identity authority.

## Visual-lock documents

Each current image master has a corresponding authority document under `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/`:

- `cyanis.jpg` → [`CYANIS_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/CYANIS_CURRENT_VISUAL_LOCK.md)
- `ilyra.jpg` → [`ILYRA_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md)
- `torren.jpg` → [`TORREN_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/TORREN_CURRENT_VISUAL_LOCK.md)
- `nimera.jpg` → [`NIMERA_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/NIMERA_CURRENT_VISUAL_LOCK.md)
- `vaelira.png` → [`VAELIRA_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/VAELIRA_CURRENT_VISUAL_LOCK.md)
- `seyrik.jpg` → [`SEYRIK_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/SEYRIK_CURRENT_VISUAL_LOCK.md)
- `maevra.jpg` → [`MAEVRA_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/MAEVRA_CURRENT_VISUAL_LOCK.md)
- `kessara.png` → [`KESSARA_CURRENT_VISUAL_LOCK.md`](../../../docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/KESSARA_CURRENT_VISUAL_LOCK.md)

The repository image controls exact appearance. The corresponding visual-lock document records identity/design intent, derivative constraints, and prohibited regressions.

## Integrity fingerprints

### 2026-09-02 retained masters

- `nimera.jpg` — SHA-256 `c24f819b287baf2cf087e12f14f2aee0be1c94dd1ea56ca4cc6747b89ced0330`
- `cyanis.jpg` — SHA-256 `c622ed107cd7b735dec44b36dce0ee6e078b687abef639d5b9f9780e086b854f`
- `torren.jpg` — SHA-256 `5ea50d69d667cd53460e27b757dbaf2a8190f2291614cda29ca0197e9035ae98`
- `ilyra.jpg` — SHA-256 `46dbfd2783d9aa3da04209b0938122517cb0bd2077b6da809fe3da50aa7dd358`
- `seyrik.jpg` — SHA-256 `51aca401cfd41b9d6f042c57f9850b70eb9ddcde2a43510e7bee6d44b7f57f23`
- `maevra.jpg` — SHA-256 `9e2b3affd3c208f7dd9e9568ed46da8faf194a98c0a6936e8d6b412f0d452c94`

### Current replacement masters

- `vaelira.png` — approved 2026-09-12 B00 replacement; SHA-256 `a7ca249cf57f48b9e3045dacc7c1349b691d464c80bffdc2833b2fbd5635868a`; generation authority `98e6cf8a-4d34-4411-b789-85e60e1123c9`.

Kessara was added directly to the repository as the approved native PNG master. Its repository blob SHA is `c773505a1b031788849588a38e677dcc09727108`; a SHA-256 source fingerprint can be added later if the exact source bytes are available locally for verification.
