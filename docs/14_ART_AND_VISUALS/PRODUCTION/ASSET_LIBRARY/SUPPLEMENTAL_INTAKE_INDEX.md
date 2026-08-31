# Diyse Supplemental Asset Intake Index

**Status:** ACTIVE INTAKE INDEX  
**Master authority:** Asset Library Master v5 remains unchanged until deliberate consolidation.

Use this index for source archives received after Master v5 was locked. Each intake batch preserves its own provenance, checksum, storage state and production routing rather than being silently merged into the master library.

| Batch | Source | Provenance | Measured payload | Production state | Authority |
|---|---|---|---|---|---|
| Batch 1 | `1.zip`, `2.zip`, `3.zip`, `4.zip`, `Bricks.zip`, `Emission.zip` | **USER-SUPPLIED / LICENSE PENDING** | 4,607 file members; 4,606 PNGs; 7 exact duplicate pairs | Inventoried; family routing ready; private/reference until provenance is resolved | `SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md` |
| Batch 2 | `brackeys_vfx_bundle.zip` | **VERIFIED CC0 FROM INCLUDED LICENSE** | 213 usable VFX images; 185 particles; 14 predrawn sheets; 14 flipbooks; 1,318 implied sheet frames | Verified-open source pool; style/runtime validation required | `VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md` |

## Current supplemental totals

Across the two intake batches currently recorded:

- source ZIP archives: **7**;
- Batch 1 ZIP bytes: **1,422,620,538**;
- Batch 2 ZIP bytes: **28,227,919**;
- combined ZIP bytes: **1,450,848,457**;
- Batch 1 usable image records: **4,606 PNGs** before exact duplicate canonicalization;
- Batch 2 usable VFX images: **213**;
- known provenance lanes remain separate.

Do not add these numbers to the historical Master v5 totals unless a future deliberate Master v6+ consolidation pass explicitly does so.

## Parallel-work lock

**B00 character work, visual-style revision, benchmark work, VFX work, and Asset Forge development do not close or supersede this intake track.**

The seven uploaded archives above remain independently tracked source batches until a deliberate consolidation pass explicitly changes their state. A character-art approval must never delete, replace, merge away, or cause the project to forget an uploaded asset batch.

When new archives are uploaded, append them as new batches and preserve the older entries. Do not renumber/reuse an existing batch identity for unrelated files.

## Intake rule for future uploads

For every new source archive:

1. compute archive SHA-256;
2. inspect members without extraction where possible;
3. filter packaging metadata without deleting it from provenance accounting;
4. record dimensions, alpha/mode and technical grouping;
5. detect exact duplicates;
6. identify animation/atlas relationships;
7. inspect included license/readme/provenance evidence;
8. choose one of the source lanes below;
9. record durable-storage state separately from inventory state;
10. route into Asset Forge by family rather than immediately converting file-by-file.

## Source lanes

### Verified open / redistributable

Examples:
- Quaternius CC0 sources;
- Brackeys VFX Batch 2 with included CC0 declaration.

May be directly modified and used after Diyse style/runtime validation. Eligible for the project’s verified third-party source-storage lane.

### User-supplied / license pending

Example:
- Supplemental Batch 1.

May be inventoried, technically analyzed, privately referenced/prototyped, and used to guide Diyse-original rebuilds. Do not publish/relabel as open until provenance is established.

### Diyse original

Assets authored specifically for Diyse. Preferred for signature/faction/story-defining visuals and any source replacement where provenance or visual identity makes direct adaptation unsuitable.

## Storage reminder

Inventory/checksum completion is **not** binary backup completion.

A batch is only durably preserved when a stored binary copy is verified against its controlling archive checksum in an approved long-term location.
