# Diyse Global Asset Archive Ledger

**Status:** ACTIVE GLOBAL UPLOAD / SOURCE-ARCHIVE INDEX  
**Purpose:** Prevent confusion between the historical Master-v5 source set and later supplemental intakes.

This ledger counts **asset-source ZIP archives**, not every file ever uploaded to the Diyse project. It is the top-level archive-count authority for visual-production source packages currently represented in the project records.

## Current count

### Active / represented source archives: **32 ZIPs**

- **25** archives represented by Asset Library Master v5:
  - **22** Map001–Map116 archive packages;
  - **3** verified-CC0 Quaternius packages.
- **7** post-Master-v5 supplemental archives:
  - **6** user texture archives with provenance pending;
  - **1** verified-CC0 Brackeys VFX archive.

### Superseded diagnostic archive uploads: **3 ZIPs**

Earlier `10-12.zip`, `13-19.zip`, and `20-28.zip` uploads contained zero-byte/incomplete material and were replaced by corrected archives. They remain part of upload history but are not active source authority.

### Total asset ZIP upload events currently identifiable from authoritative records: **35**

This count does **not** include unrelated project recovery bundles, canon ZIPs, exported builds, generated review artifacts, or any asset upload not yet represented by an authoritative intake/source record.

---

## A. Master v5 — Map archives (22)

1. `1-6.zip`
2. `7-9.zip`
3. `10-13.zip`
4. `14-18.zip`
5. `19-22.zip`
6. `23-27.zip`
7. `28-31.zip`
8. `32-39.zip`
9. `40-45.zip`
10. `46-50.zip`
11. `51-60.zip`
12. `61-67.zip`
13. `68-72.zip`
14. `73-75.zip`
15. `76-79.zip`
16. `080.zip`
17. `81-84.zip`
18. `85-90.zip`
19. `91-95.zip`
20. `96-105.zip`
21. `106-111.zip`
22. `112-116.zip`

Authority/checksums:
`SOURCE_ARCHIVE_MANIFEST.md`

Canonicalization note: `080.zip` and `81-84.zip` contain the same 17 Map080 files; the archive uploads remain distinct records while the duplicated Map080 payload is counted once in the canonical file inventory.

---

## B. Master v5 — Verified CC0 Quaternius archives (3)

23. `Fantasy Props MegaKit[Standard].zip`
24. `Universal Animation Library[Standard].zip`
25. `Universal Animation Library 2[Standard].zip`

Authority/checksums:
`SOURCE_ARCHIVE_MANIFEST.md`

These are verified CC0 1.0 / Public Domain Dedication under the included source licenses recorded in Master v5.

---

## C. Supplemental Batch 1 — User texture archives (6)

26. `1.zip`
27. `2.zip`
28. `3.zip`
29. `4.zip`
30. `Bricks.zip`
31. `Emission.zip`

Authority/checksums:
`SUPPLEMENTAL_USER_TEXTURE_INTAKE_2026-08-31_BATCH1.md`

Status:
**USER-SUPPLIED / LICENSE PENDING / INVENTORIED**

Measured batch payload: 4,607 members / 4,606 PNGs / 7 exact duplicate pairs / 4,599 exact-unique PNGs after duplicate canonicalization.

---

## D. Supplemental Batch 2 — Verified CC0 VFX archive (1)

32. `brackeys_vfx_bundle.zip`

Authority/checksum:
`VERIFIED_CC0_VFX_INTAKE_2026-08-31_BATCH2.md`

Status:
**VERIFIED CC0 / INVENTORIED / DIRECT-PRODUCTION SOURCE CANDIDATE**

Measured usable payload: 213 VFX images, including 185 particle textures, 14 predrawn sheets, 14 flipbooks, and 1,318 declared sheet frames.

---

## E. Superseded diagnostic asset ZIP uploads (3)

These are historical upload events only and must not be used as active source authority:

33. `10-12.zip`
34. `13-19.zip`
35. `20-28.zip`

Replacement/correction history is documented in Asset Library Master v5 and `SOURCE_ARCHIVE_MANIFEST.md`.

---

## Scope rule

Do not use the phrase **“all uploaded ZIPs”** when referring only to `SUPPLEMENTAL_INTAKE_INDEX.md`.

Use these terms precisely:

- **Master-v5 source archives** = the 25 active ZIPs in sections A+B;
- **supplemental archives** = the 7 active ZIPs in sections C+D;
- **active asset-source archives** = all 32 active ZIPs;
- **known asset ZIP upload events** = 35 including superseded diagnostic uploads.

If another asset archive is uploaded, it must be appended here as well as to its batch-specific intake record. New character art/reference images do not alter this ZIP count unless supplied as an archive.

## Preservation rule

Archive inventory and checksum authority are separate from durable binary preservation. A source package is not considered durably backed up merely because its filename/checksum appears in this ledger.
