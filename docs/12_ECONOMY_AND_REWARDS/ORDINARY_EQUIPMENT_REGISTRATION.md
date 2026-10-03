# Diyse — Ordinary Equipment Registration & Repurchase
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current equipment-registration/repurchase authority; Audit/v85 references remain provenance only. Numeric replacement prices are read from the provisional economy price owner.
**Historical catalog provenance:** v603-era archived item/equipment catalog, where not superseded by current repository authority.
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns G denomination, purchase/replacement prices, sell rules, stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


## Permanent-stock principle
All ordinary equipment can ultimately be repurchased.

No ordinary equipment is permanently missable.

## Shop-origin gear
Once unlocked:
- remains purchasable from its original normal vendor while that vendor is accessible;
- enters Cresthaven's consolidated catalog according to the headquarters consolidation state;
- normal stock is unlimited.

## Start/join gear
After:
1. Cresthaven consolidation is active; and
2. the relevant character/equipment family has joined/unlocked;

the starting/join item may be requisitioned in additional copies at its registered replacement price.

## Found / protected-cache / guaranteed-combat ordinary gear
The first authored copy retains exploration/combat value.

After it is obtained:
> the identity registers to Cresthaven requisition stock.

Additional copies then use the registered replacement price in `ORDINARY_EQUIPMENT_PRICING.md`.

## Anti-missability fallback
If the original one-time source permanently closes before the player obtains the ordinary item:
> add the item to Cresthaven at the next appropriate stock update.

The player may lose the free authored copy, but not permanent legal access to the ordinary equipment identity.

## Scope firewall
This anti-missability/registration rule does not automatically apply to:
- Relics
- Legacies
- Cards / Primes
- Forge Components
- Project/Key Items
