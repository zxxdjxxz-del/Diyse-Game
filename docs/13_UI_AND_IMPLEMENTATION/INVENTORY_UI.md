# Diyse — Inventory & Materials UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Current inventory families
The final UI must be able to represent:
- Consumables — current catalog **20**
- ordinary equipment
- Relics
- Legacies
- Standard Cards
- Primes
- Forge Components
- Character Quest Legacy Components / project materials

## Sellability boundaries
Ordinary sellable inventory must remain separate from:
- Forge Components;
- unique Legacy Components;
- non-sellable project materials;
- non-sellable unique exceptional equipment where current item rules say so.

Do not let a generic `Sell All Materials` interaction consume protected project items.

## Forge Components
Current total:
> **30**

Per Face:
- 2 Legacy-gate components;
- 3 Relic-copy components.

Gate and copy components are not interchangeable.

## Character Quest Legacy Components
Exactly six unique project items.

They are:
- unique;
- non-consumable;
- non-equippable;
- non-sellable;
- not generic Forge Components.

## OPEN PRODUCTION UX
- inventory category names/icons;
- sorting;
- favorites;
- item detail pane layout;
- key/project-material tab naming.
