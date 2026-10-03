# Diyse Supplemental Asset Intake Index

**Status:** ACTIVE SUPPLEMENTAL SOURCE INDEX  
**Baseline source identity:** `SOURCE_ARCHIVE_MANIFEST.md`

This file tracks the **7 current supplemental source ZIPs** outside the 25-ZIP baseline manifest.

Current active source count:
- **25** baseline source ZIPs;
- **7** supplemental source ZIPs;
- **32 active asset-source ZIPs total**.

Superseded upload attempts are Git-history provenance and are not included in current counts.

| Batch | Source | Provenance | Measured payload | Production state | Authority |
|---|---|---|---|---|---|
| Batch 1 | `1.zip`, `2.zip`, `3.zip`, `4.zip`, `Bricks.zip`, `Emission.zip` | **USER-SUPPLIED / LICENSE PENDING** | 4,607 file members; 4,606 PNGs; 7 exact duplicate pairs | Inventoried; private/reference until provenance is resolved | `SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md` |
| Batch 2 | `brackeys_vfx_bundle.zip` | **VERIFIED CC0 FROM INCLUDED LICENSE** | 213 usable VFX images; 185 particles; 14 predrawn sheets; 14 flipbooks; 1,318 implied frames | Verified-open source pool; style/runtime validation required | `VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md` |

## Current supplemental totals

- supplemental source ZIP archives: **7**;
- Batch 1 ZIP bytes: **1,422,620,538**;
- Batch 2 ZIP bytes: **28,227,919**;
- combined supplemental ZIP bytes: **1,450,848,457**;
- Batch 1 usable image records: **4,606 PNGs** before exact duplicate canonicalization;
- Batch 2 usable VFX images: **213**.

Each batch keeps its own provenance, checksum, storage state, and production routing.

## Intake rule for future uploads

For every new source archive:

1. compute archive SHA-256;
2. inspect members without extraction where possible;
3. filter packaging metadata without losing provenance accounting;
4. record dimensions, alpha/mode, and technical grouping;
5. detect exact duplicates;
6. identify animation/atlas relationships;
7. inspect included license/readme/provenance evidence;
8. choose an appropriate source lane;
9. record durable-storage state separately from inventory state;
10. route into Asset Forge by family rather than converting file-by-file;
11. append the batch to this current supplemental index or deliberately consolidate it into the baseline manifest.

## Source lanes

### Verified open / redistributable

Examples:
- Quaternius CC0 sources;
- Brackeys VFX Batch 2.

May be directly modified and used after Diyse style/runtime validation.

### User-supplied / license pending

Example:
- Supplemental Batch 1.

May be inventoried, technically analyzed, privately referenced/prototyped, and used to guide Diyse-original rebuilds. Do not publish or relabel as open until provenance is established.

### Diyse original

Assets authored specifically for Diyse. Preferred for signature/faction/story-defining visuals and provenance-sensitive source replacement.

## Storage reminder

Inventory/checksum completion is not binary backup completion. A batch is durably preserved only when a stored binary copy is verified against its controlling checksum in an approved long-term location.
