# Diyse — Enemy Reward Handoff
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted v85 tracker-level economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


## Ownership
`09_ENEMIES_AND_ENCOUNTERS` owns:
- enemy identity;
- level/stat body;
- encounter formation;
- combat kit.

`10_PROGRESSION_AND_EXP` owns:
- Player EXP;
- CEXP;
- diminishing-return behavior where applicable.

`12_ECONOMY_AND_REWARDS` owns:
- Auren payout tuning;
- economic reward density;
- non-EXP reward balancing.

`08_ITEMS_AND_EQUIPMENT` owns:
- exact item identity/effect;
- authored equipment/material source identity.

## Drop firewall
Do not assume a universal random-drop table.

Ordinary encounters may use occasional explicitly authored Consumable drops if approved, but this migration does not invent probabilities.

Do not introduce by default:
- low-percentage weapon farming;
- low-percentage armor farming;
- sell-only junk;
- generic monster-part crafting economy.

Permanent equipment that is supposed to advance progression should be reliably authored, not dependent on repeated RNG farming.
