# Diyse — Exact Character Appearance Source Lock (2026-09-22)

**Status:** **LOCKED — NEWEST EXPLICIT USER APPROVAL**

The eight images approved together on 2026-09-22 are the exact current appearance authorities for Cyanis, Ilyra, Torren, Nimera, Vaelira, Seyrik, Maevra, and Crown Princess Mirena Ceryth.

Machine-readable fingerprints: [`asset_sources/characters/current/APPROVED_SOURCE_MANIFEST.json`](../../../../asset_sources/characters/current/APPROVED_SOURCE_MANIFEST.json)

## Exact-source rule

The approved image itself controls face, facial proportions, hair, eyes as depicted, body proportions, clothing, armor, jewelry, equipment/props, palette, materials, silhouette, stance, scale/framing, and incidental visual detail. Do not reconstruct these appearances from older prose.

## Canonical permanent-party height lock

Canonical in-world heights are separate scalar authority from the individual source-image framing:

| Character | Canonical height |
| --- | ---: |
| Seyrik | **6'6"** |
| Cyanis | **6'1"** |
| Torren | **5'11"** |
| Ilyra | **5'9"** |
| Vaelira | **5'6"** |
| Nimera | **5'4"** |

Rules:
- do **not** infer relative in-world height from the separate master-image pixel dimensions, crop, margins, or individual framing;
- do **not** resize, crop, or otherwise alter the locked source masters merely to encode these heights;
- ensemble/model/runtime scaling should respect the canonical height table while preserving each exact appearance master as the visual identity authority.

## Hair-length ceiling

The approved Nimera and Vaelira masters are also the maximum allowed current hair length for those characters.

- **Nimera:** do not lengthen her current locs/twists beyond the locked master silhouette.
- **Vaelira:** do not lengthen her current crimson hair beyond the locked master silhouette.

Shortening or otherwise redesigning those silhouettes is also not implied; any change requires a new explicit visual revision.

| Character | Exact master | Dimensions | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| Cyanis | [asset_sources/characters/current/cyanis.jpg](../../../../asset_sources/characters/current/cyanis.jpg) | 1280 × 1536 | 206567 | `9c86bb384051997786fad71fa9fd8427b7386bda77e98b4a52816b0ee76878ea` |
| Ilyra | [asset_sources/characters/current/ilyra.jpg](../../../../asset_sources/characters/current/ilyra.jpg) | 1280 × 1536 | 198138 | `4ab184e960176141367b005d13992efe4bad64058fcd02ec0c5358811e058893` |
| Torren | [asset_sources/characters/current/torren.jpg](../../../../asset_sources/characters/current/torren.jpg) | 1280 × 1536 | 250994 | `ff5a27b8f42c2bdcbb9290219213793860e398225af84e5107600a3ac5377313` |
| Nimera | [asset_sources/characters/current/nimera.jpg](../../../../asset_sources/characters/current/nimera.jpg) | 1280 × 1536 | 156104 | `4e923f7053a5cc75c61c1a5deb3351743727b53d38ae57383a767a6674883874` |
| Vaelira | [asset_sources/characters/current/vaelira.jpg](../../../../asset_sources/characters/current/vaelira.jpg) | 1280 × 1536 | 158620 | `100b7b6d992c07ec82a4860eebf75fd61d279c41d9dd249db92864a0273875a3` |
| Seyrik | [asset_sources/characters/current/seyrik.jpg](../../../../asset_sources/characters/current/seyrik.jpg) | 1280 × 1536 | 201706 | `6655471361fb9e826c8778d15e6c47074cf4f0a7450fa90107e307ed0f8f267b` |
| Maevra | [asset_sources/characters/current/maevra.jpg](../../../../asset_sources/characters/current/maevra.jpg) | 1075 × 1536 | 170705 | `b1ada1a13e1301803849b8994ac9017cbaffb7570fd4c78d11732e6ed4247577` |
| Crown Princess Mirena Ceryth | [asset_sources/characters/current/mirena.jpg](../../../../asset_sources/characters/current/mirena.jpg) | 1229 × 1536 | 175309 | `a61c0dbf87eef484fc955c3b11d00f2120fcd9169f37c02b319ed470d9be5c77` |

## Binary-sync state

**Exact source bytes: repository promotion COMPLETE.**

All eight repository masters match the SHA-256 values above exactly. Older binary versions are historical provenance only and may not override this lock.

The exact source must not be recompressed, converted, resized, cropped, retouched, color-corrected, or resaved merely to make repository sync easier.

Kessara's existing repository master remains locked separately and is unaffected by this eight-image replacement.

Nonvisual biography, story, combat, class, and equipment rules remain owned by their normal numbered domains.
