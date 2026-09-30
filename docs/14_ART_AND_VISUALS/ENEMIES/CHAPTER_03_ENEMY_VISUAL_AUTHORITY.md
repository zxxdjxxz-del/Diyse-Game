# Diyse — Chapter 3 Enemy Visual Authority

**Status:** **ACTIVE — 8 / 8 CHAPTER-3-SPECIFIC LOCKED MASTERS EXACT-BINARY SYNCED — 2026-09-29**  
**Rendering authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Enemy mechanics/placement authority:** `../../09_ENEMIES_AND_ENCOUNTERS/`

This file owns the exact visual-source routing for locked Chapter-3 enemy masters.

## Exact locked Chapter-3-specific masters

Canonical binary destination:
> [`asset_sources/enemies/chapter_03/current/`](../../../asset_sources/enemies/chapter_03/current/)

Machine-readable exact-source authority:
> [`APPROVED_SOURCE_MANIFEST.json`](../../../asset_sources/enemies/chapter_03/current/APPROVED_SOURCE_MANIFEST.json)

| Enemy | Exact approved master | Status |
| --- | --- | --- |
| Maul Construct | [01_maul_construct.png](../../../asset_sources/enemies/chapter_03/current/01_maul_construct.png) | Locked; exact-binary synced |
| Flame Construct | [02_flame_construct.png](../../../asset_sources/enemies/chapter_03/current/02_flame_construct.png) | Locked; exact-binary synced |
| Flash Drone | [03_flash_drone.png](../../../asset_sources/enemies/chapter_03/current/03_flash_drone.png) | Locked; exact-binary synced |
| Blade Drone | [04_blade_drone.png](../../../asset_sources/enemies/chapter_03/current/04_blade_drone.png) | Locked; exact-binary synced |
| Ruin Spider | [05_ruin_spider.png](../../../asset_sources/enemies/chapter_03/current/05_ruin_spider.png) | Locked; exact-binary synced |
| Memory Construct | [06_memory_construct.png](../../../asset_sources/enemies/chapter_03/current/06_memory_construct.png) | Locked; exact-binary synced |
| Authority Construct | [07_authority_construct.png](../../../asset_sources/enemies/chapter_03/current/07_authority_construct.png) | Locked; exact-binary synced |
| Scriptshade | [scriptshade.png](../../../asset_sources/enemies/chapter_03/current/scriptshade.png) | Locked; exact-binary synced |

Scriptshade moved from Chapter 2 to Chapter 3 on 2026-09-27. Its exact locked binary moved with the assignment; do not retain a Chapter-2 copy as visual authority.

## Locked carryover visuals

Chapter 3 also reuses three exact locked masters owned by earlier chapter asset folders. Do **not** duplicate these binaries into the Chapter-3 folder.

| Enemy | Exact approved master | Chapter-3 status |
| --- | --- | --- |
| Construct | [construct.png](../../../asset_sources/enemies/chapter_01/current/construct.png) | Locked carryover |
| Shield Construct | [shield_construct.png](../../../asset_sources/enemies/chapter_01/current/shield_construct.png) | Locked carryover |
| Arcdrift | [arcdrift.png](../../../asset_sources/enemies/chapter_02/current/arcdrift.png) | Locked carryover |

The Chapter-3 manifest records these as `carryover_visuals` and keeps their exact-source ownership in the earlier chapter folders.

## Binary-authority rule

A generated image becomes exact authority only after explicit approval and fingerprint registration.

Never re-encode, crop, resize, recolor, retouch, optimize, or resave an approved master during repository sync. The registered SHA-256 controls binary identity.
