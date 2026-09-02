# Diyse — Runtime Technical-ID Migration Map

**Status:** ACTIVE IMPLEMENTATION MIGRATION FIREWALL  
**Rule:** stable proof/legacy technical IDs may remain temporarily for save/content compatibility, but they do not become current player-facing names.

This file records high-value technical identifiers that require deliberate migration rather than casual search-and-replace.

| Legacy/proof technical value | Current meaning / target | Current handling |
|---|---|---|
| `first_champion` | **Last Sentinel** Story Prime | Proof-only Prime ID/resource. Keep until the Prime runtime/save model is replaced or explicitly migrated. Never treat `First Champion` as current player-facing canon. |
| `gold` | **G** ordinary currency | Legacy technical key may remain temporarily. Production UI/state must present **G** and use current G-scale values. Requires save-safe wallet/state migration. |
| Face `Resource` | **Perception** | Runtime Relic/component registration now canonicalizes to Perception. Retain as compatibility input only. |
| Face `Acuity` | **Perception** | Runtime Relic/component registration now canonicalizes to Perception. Retain as compatibility input only. |
| Face `Change` | **Memory** | Runtime Relic/component registration now canonicalizes to Memory. Retain as compatibility input only. |
| `CH01_EDGELANDS_SETTLEMENT` / `environment.chapter_01.edgelands_settlement` | current Westways-era geography | Legacy environment/state key. Do not expose `Edgelands` as a current formal region name. Rename only with explicit state/save migration. |
| `CH04_SIXFOLD_ANNEX` / `environment.chapter_04.sixfold_annex` | **Reaction Annex** | Legacy environment/state key. Do not expose `Sixfold Annex` as the current location name. Rename only with explicit state/save migration. |
| `environment_southhold_roadside` and related `Southhold` technical naming | **Yahtrenhold** context | Legacy presentation/resource naming. Do not expose Southhold as the current region name. Rename only when references/state are migrated together. |
| `game/characters/placeholders/` | proof-only runtime character/portrait stand-ins | Do not use as production identity authority. Production derivatives must come from the current repository masters and visual locks. |

## Migration rules

1. **Do not rename a stable ID just to make the source tree look cleaner.** First determine whether it is serialized, referenced by authored Resources, tests, scene IDs, flags, or other runtime data.
2. If an ID must change, provide an explicit old→new migration path and update validation in the same implementation pass.
3. Display names and current-facing UI should use current terminology even when a legacy technical ID is temporarily retained underneath.
4. Tests that intentionally verify proof behavior must be labeled/routed as proof tests; they do not convert stale behavior into current canon.
5. Current terminology owners remain:
   - classes → `../../00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`
   - Faces → `../../00_MASTER_CONTROL/FACE_TERMINOLOGY_CURRENT.md`
   - general retired terms → `../../00_MASTER_CONTROL/RETIRED_TERMINOLOGY_MAP.md`
   - character visuals → `../../14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/README.md`

## Current resolved migration

The Kessara Relic-copy state layer now uses the current Face set internally for newly registered records while accepting Resource/Acuity/Change only as migration aliases. This is the preferred pattern for future save-safe terminology migrations: **read old, normalize to current, write current**.
