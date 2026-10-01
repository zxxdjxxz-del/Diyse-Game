# Diyse — Equipment Balance Verification

**Status:** ACTIVE EQUIPMENT QA CHECKLIST  
**Equipment authority:** `../../08_ITEMS_AND_EQUIPMENT/`

## Catalog
Current equipment count:
- 38 ordinary
- 36 Relics
- 17 Legacies
- **91 total**

Hierarchy:
> Ordinary < Relic < Legacy

## Verification
Test:
- legal slots;
- two-slot commitments;
- class/character eligibility;
- stat application;
- perk/trait activation;
- copy quantities;
- no duplicate stacking bug;
- no illegal Secondary item when Weapon consumes Secondary.

## Specific slot checks
Two-slot:
- Torren Great Bow
- Seyrik Two-Handed Sword
- Nimera native Legacy Conduit

Ilyra:
- Wardrod Weapon
- Shield or Focus Secondary
- no sword identity
- no simultaneous Shield + Focus.

## Relics
Test:
- original ownership;
- forged duplicate mechanically identical;
- max quantity 2 per identity;
- no Legacy copy;
- donor eligibility does not generate ownership/copy.

## Legacies
Balance acceptance:
- stronger than Relics overall;
- role-fitting perk;
- meaningful Legacy Trait;
- no invented unsupported combat subsystem.

Exact stats/traits remain in `08`.
