# Diyse — Economy Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted v85 tracker-level economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


## Design objective
The economy should support:
- routine field maintenance without punishment;
- meaningful but selective ordinary-equipment purchases;
- exploration and authored rewards retaining real value;
- optional content feeling economically useful without becoming mandatory money farming;
- subclass experimentation without forcing the player to preserve every starting item forever.

The intended checkpoint pressure is:
> **one meaningful ordinary equipment purchase + routine consumable restock should usually be affordable without exhausting all funds.**

Buying every available upgrade immediately is not the baseline expectation.

## Economy layers
### Normal commerce
- normal-stock consumables
- ordinary equipment purchase / replacement / requisition
- Auren

### Authored reward layer
- guaranteed ordinary equipment
- Relics
- Legacy precursors/components
- Cards / Primes
- exceptional reward-only consumables
- Forge Components
- quest/story objects

Exceptional equipment is not converted into a normal shop ladder merely because it has economic value.

## No junk-economy requirement
Do not create a large vendor-trash layer merely to feed money back to the player.

General random monster-part / sell-only-junk systems are not assumed by this migration.

## Ownership
- `08` owns item identity/stats/effects/source identity.
- `09` owns enemies/formations.
- `10` owns Player EXP/CEXP.
- `11` owns quest/hunt access and completion state.
- `12` owns Auren, prices, stock and non-EXP reward economy.
