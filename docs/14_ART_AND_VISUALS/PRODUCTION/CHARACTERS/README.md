# Diyse Character Visual Authority Index

## Authority order

1. newest explicit user-approved exact source image;
2. exact approved fingerprint in [`EXACT_APPEARANCE_SOURCE_LOCK_2026-09-22.md`](EXACT_APPEARANCE_SOURCE_LOCK_2026-09-22.md) / `APPROVED_SOURCE_MANIFEST.json`;
3. repository master binary only when it matches that fingerprint;
4. matching `*_CURRENT_VISUAL_LOCK.md`;
5. current B00 / HD-2D anime style rules;
6. older prose, archived renders, generated filenames, and historical hashes.

The exact source image controls face, body proportions, hair, clothing/armor construction, equipment/prop placement, palette, silhouette, scale/framing, and incidental minutiae.

## Permanent party

| Character | Exact master | Approved SHA-256 | Lock |
| --- | --- | --- | --- |
| Cyanis | [asset_sources/characters/current/cyanis.jpg](../../../../asset_sources/characters/current/cyanis.jpg) | `9c86bb384051997786fad71fa9fd8427b7386bda77e98b4a52816b0ee76878ea` | [`CYANIS_CURRENT_VISUAL_LOCK.md`](CYANIS_CURRENT_VISUAL_LOCK.md) |
| Ilyra | [asset_sources/characters/current/ilyra.jpg](../../../../asset_sources/characters/current/ilyra.jpg) | `4ab184e960176141367b005d13992efe4bad64058fcd02ec0c5358811e058893` | [`ILYRA_CURRENT_VISUAL_LOCK.md`](ILYRA_CURRENT_VISUAL_LOCK.md) |
| Torren | [asset_sources/characters/current/torren.jpg](../../../../asset_sources/characters/current/torren.jpg) | `ff5a27b8f42c2bdcbb9290219213793860e398225af84e5107600a3ac5377313` | [`TORREN_CURRENT_VISUAL_LOCK.md`](TORREN_CURRENT_VISUAL_LOCK.md) |
| Nimera | [asset_sources/characters/current/nimera.jpg](../../../../asset_sources/characters/current/nimera.jpg) | `4e923f7053a5cc75c61c1a5deb3351743727b53d38ae57383a767a6674883874` | [`NIMERA_CURRENT_VISUAL_LOCK.md`](NIMERA_CURRENT_VISUAL_LOCK.md) |
| Vaelira | [asset_sources/characters/current/vaelira.jpg](../../../../asset_sources/characters/current/vaelira.jpg) | `100b7b6d992c07ec82a4860eebf75fd61d279c41d9dd249db92864a0273875a3` | [`VAELIRA_CURRENT_VISUAL_LOCK.md`](VAELIRA_CURRENT_VISUAL_LOCK.md) |
| Seyrik | [asset_sources/characters/current/seyrik.jpg](../../../../asset_sources/characters/current/seyrik.jpg) | `6655471361fb9e826c8778d15e6c47074cf4f0a7450fa90107e307ed0f8f267b` | [`SEYRIK_CURRENT_VISUAL_LOCK.md`](SEYRIK_CURRENT_VISUAL_LOCK.md) |

## Supporting characters in the same exact-source set

| Character | Exact master | Approved SHA-256 | Lock |
| --- | --- | --- | --- |
| Maevra | [asset_sources/characters/current/maevra.jpg](../../../../asset_sources/characters/current/maevra.jpg) | `b1ada1a13e1301803849b8994ac9017cbaffb7570fd4c78d11732e6ed4247577` | [`MAEVRA_CURRENT_VISUAL_LOCK.md`](MAEVRA_CURRENT_VISUAL_LOCK.md) |
| Crown Princess Mirena Ceryth | [asset_sources/characters/current/mirena.jpg](../../../../asset_sources/characters/current/mirena.jpg) | `a61c0dbf87eef484fc955c3b11d00f2120fcd9169f37c02b319ed470d9be5c77` | [`MIRENA_CURRENT_VISUAL_LOCK.md`](MIRENA_CURRENT_VISUAL_LOCK.md) |

Exact repository-byte promotion is complete. All eight master binaries match the approved fingerprints; older versions remain historical provenance in Git history.

Kessara remains separately locked by the existing `asset_sources/characters/current/kessara.png` master.

## Production rules

Use only the target character's exact approved source for identity. Other characters may guide shared B00 technique, never identity, costume, palette, equipment, or proportions. Do not patch an older image to simulate the current source. Derivatives never replace the exact source without new explicit approval.
