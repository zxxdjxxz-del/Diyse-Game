# Diyse Supplemental User Texture Intake — 2026-08-31 Batch 1

**Status:** INTAKE INVENTORIED / PROVENANCE PENDING / NOT YET MERGED INTO MASTER v5  
**Intake tool:** `../../../../../tools/asset_forge/zip_intake_engine.py`  
**Repository safety:** raw ZIPs remain outside public Git authority until licensing/provenance is established.

## 1. Scope

Six user-supplied ZIP archives were received as a new supplemental texture batch:

- `1.zip`
- `2.zip`
- `3.zip`
- `4.zip`
- `Bricks.zip`
- `Emission.zip`

This batch is **not** silently folded into DIYSE Asset Library Master v5. Master v5 remains the current canonical inventory for the earlier Map001–Map116/CC0 source set. This document records the new material as a separate intake layer until provenance and durable binary storage are resolved.

## 2. Batch totals

- archives: **6**
- ZIP bytes: **1,422,620,538**
- file members: **4,607**
- PNG members: **4,606**
- non-image members: **1** (`.ini`)
- uncompressed bytes: **1,428,899,744**
- SHA-confirmed exact duplicate pairs inside the new batch: **7**
- exact-unique members after those duplicate pairs: **4,600**
- exact-unique PNGs after those duplicate pairs: **4,599**
- exact duplicate groups crossing different new archives: **0**

The duplicate count above was first detected by ZIP CRC32 + byte size and then confirmed by SHA-256 on every candidate pair.

## 3. Archive checksums and measured contents

| Archive | ZIP bytes | Files | Uncompressed bytes | SHA-256 | Path-aware content summary | Main image sizes |
|---|---:|---:|---:|---|---|---|
| `1.zip` | 161,847,615 | 421 | 162,889,106 | `2b8a3cfdabd1d86ccc0ba627959a286be498d3755f19679c94b55ed2bf38306c` | brick 247; fire 114; ritual/mystic 60 | 256×256: 293; 512×512: 128 |
| `2.zip` | 304,397,186 | 1,629 | 306,557,247 | `acbccb364bd8700e9c32306bed7298426cc0b9e883d024f06e05866bb9344923` | metal 1,228; emission/light 214; marble 103; misc 71; concrete 7; brick 6 | 256×256: 881; 512×512: 354; 128×256: 342; 512×256: 28 |
| `3.zip` | 340,062,097 | 971 | 341,086,045 | `ca8f38e84614ecde98f6f5eb2182ff9a31334e6284e31a69c09fded8824fa2cb` | terrain 480; wood 380; water 40; metal 33; foliage 25; fire/lava 6; brick 6; glass 1 | 512×512: 535; 256×256: 297; 128×256: 132; 512×256: 6 |
| `4.zip` | 219,455,470 | 1,029 | 220,304,272 | `a98ee6cc6ace217cad7457b579a91221fc02b72d8fe93b5a41650892a834ad51` | concrete 901; brick 66; glass/window 62 | 256×256: 804; 512×512: 204; 64×256: 14; 128×256: 7 |
| `Bricks.zip` | 393,093,168 | 529 | 393,824,136 | `008384b4f7c9effef6f184e8fcb17fe65152b1b5cf20feddb6263211efa07eea` | brick 529 | 512×512: 465; 64×256: 25; 256×512: 14; 128×512: 13 |
| `Emission.zip` | 3,765,002 | 28 | 4,238,938 | `6b8cfd2783bb0efb01c6c7334155c3341192cc3c22523179889070cab5d3d8df` | emission/support 28 | 256×256: 14; 128×256: 11; 512×256: 1; 512×512: 1; 512×521: 1 |

## 4. Broad new production capability

Path-aware classification across the batch currently resolves approximately:

- Metal — **1,261**
- Concrete — **908**
- Brick/masonry — **854**
- Terrain/outdoor stone/sand/canyon — **480**
- Wood — **380**
- Emission/light-support — **242**
- Fire/lava — **120**
- Marble — **103**
- Miscellaneous/wallpaper — **71**
- Glass/window — **63**
- Ritual/mystic — **60**
- Water — **40**
- Foliage — **25**

These are intake-routing counts, not final semantic asset identities. Some mixed-use trim sheets may later be reclassified by actual production role.

## 5. Animation/effect families

`1.zip` contains a structured animated-effects set:

### Fire
Six families:
- A through F
- **19 files per family**
- **114 fire animation images total**

### Mystic / ritual
Six families:
- A through F
- **10 source images per family**
- **60 mystic animation images total**

The source naming in Mystic A/B is slightly irregular, so frame ordering must be normalized by the ZIP intake/animation pipeline rather than assumed from lexical filename sort alone.

`Emission.zip` contains a separate **10-frame `ANIM_Mistic` emission/support sequence**, plus light, door, lava and metal-support images. It must be treated as companion/emissive data rather than assumed BaseColor content.

This batch therefore materially strengthens B04/B06/B09-style testing and suggests a paired color/emission animation path should be supported by Asset Forge.

## 6. Exact duplicate pairs

All seven confirmed exact pairs occur inside `Bricks.zip`:

1. `Flat tiles/BRICK_flat_tiles_BIG_half-wall_4.png` = `Flat tiles/BRICK_flat_tiles_BIG_half-wall_5.png`
2. `Medieval Flat/BRICK_medieval_flat_diamond_tile_3.png` = `..._5.png`
3. `Medieval Flat/BRICK_medieval_flat_random_size_2.png` = `..._4.png`
4. `Medieval Flat/BRICK_medieval_flat_thick_3.png` = `..._5.png`
5. `Medieval Flat/BRICK_medieval_flat_tile_3.png` = `..._5.png`
6. `Medieval Flat/BRICK_medieval_flat_wall_3.png` = `..._5.png`
7. `Medieval Flat/BRICK_medieval_flat_wall_alt-size_3.png` = `..._5.png`

Canonicalization should keep one member per exact pair for conversion/budget purposes while retaining the original archive manifest for provenance.

## 7. Provenance and storage status

Current provenance for this supplemental batch is:

> **USER-SUPPLIED / LICENSE NOT YET VERIFIED**

Therefore:
- do not commit the raw ZIPs or extracted images to the current public repository;
- do not label the assets CC0/open-source merely because they were uploaded by the user;
- do not merge them into redistributable asset folders until license evidence is recorded;
- safe uses pending provenance are inventory, technical analysis, private reference/prototyping, benchmark planning, and original Diyse rebuild guidance under the existing conversion policy.

Archive SHA-256 values above are the identity anchors for this exact uploaded batch.

## 8. Forge routing decision

Asset Forge v0.8 adds ZIP-native intake through:

`tools/asset_forge/zip_intake_engine.py`

The tool can inspect archives without extraction and records:
- archive SHA-256;
- member count and uncompressed size;
- member path/size/CRC;
- optional member SHA-256;
- image dimensions/mode/alpha;
- path-aware material family;
- animation family/frame metadata;
- duplicate groups.

Recommended command for future uploads:

```bash
python tools/asset_forge/zip_intake_engine.py \
  /path/to/1.zip /path/to/2.zip /path/to/3.zip \
  --output .asset_forge/supplemental_intake.json
```

Use `--hash-members` when an authoritative member-level duplicate/provenance manifest is needed.

## 9. Immediate production implications

This batch should be integrated by **family**, not file-by-file.

Priority implications:
1. animated Fire + Mystic families are strong candidates for the B06/B09/effect pipeline;
2. the dedicated `Emission.zip` suggests explicit BaseColor/emission companion pairing should be added before broad effect conversion;
3. the large Metal / Concrete / Brick groups should be family-clustered before any generation budget is spent;
4. Wood and terrain families can expand the later B02/B07/material grammar tests;
5. Water provides another source family for B05 validation;
6. the older `.old_bricks` subtree should remain identifiable as legacy/source grouping rather than being silently mixed with the newer `Bricks.zip` families.

## 10. Promotion gate

This intake becomes part of a future canonical Asset Library Master only after:

1. provenance/license status is recorded;
2. durable private or redistributable storage routing is decided;
3. archive identities are preserved by checksum;
4. duplicate canonicalization is applied without losing provenance;
5. Forge family grouping is reviewed;
6. the active Diyse conversion/originalization policy is applied.

Until then:

> **Master v5 stays authoritative; Supplemental Batch 1 is an inventoried pending-provenance extension.**
