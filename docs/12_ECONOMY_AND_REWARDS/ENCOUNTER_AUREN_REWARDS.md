# Diyse — Encounter Auren Rewards
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted v85 tracker-level economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


## Current ownership split
- enemy identity/formation/difficulty → `09`
- Player EXP/CEXP → `10`
- Auren payout tuning → `12`

## Ordinary encounters
Current exact per-formation Auren values are not comprehensively certified in the migration source.
Use the current chapter-income bands as balancing references rather than inventing a universal formula.

Enemy count may influence a formation payout, but:
> a large weak formation should not automatically become the best money farm.

Reward should consider:
- local content band;
- formation difficulty;
- enemy role/tier;
- encounter complexity;
- authored Elite/named status.

## Elites/named encounters
Older work proposed larger direct-currency bands, with lower cash when the encounter already supplies high-value authored equipment/material rewards.

That is preserved as a **tuning principle**, not a locked exact table.

## No automatic duplicate reward
Do not assume an enemy must also drop:
- a material;
- sell-only junk;
- an equipment piece;

simply because it awards Auren.
