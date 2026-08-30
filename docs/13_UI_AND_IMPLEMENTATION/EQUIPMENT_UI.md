# Diyse — Equipment UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Functional slots
Exactly:
1. Weapon
2. Secondary
3. Armor

No general Accessory slot.

## Two-slot commitments
Always consume Weapon + Secondary:
- Torren Great Bow
- Seyrik Two-Handed Sword
- Nimera native Legacy two-handed Conduit

The UI must make the Secondary commitment visible and prevent illegal simultaneous equipment.

## Character-specific current rules
### Ilyra
Weapon:
- Wardrod

Secondary:
- Shield **or** Focus

No sword assumption.
No simultaneous Shield + Focus.

### Vaelira
Weapon:
- Arcane Staff

Secondary:
- Focus may remain available because Arcane Staff is one-slot.

### Nimera
- ordinary/Base Relic Conduits are one-slot unless individually stated;
- native Legacy Conduit is two-slot.

## Equipment comparison
Final UI should be able to compare current vs candidate:
- core stat changes;
- legal slot commitment;
- trait/perk text;
- restrictions;
- quantity/ownership.

Exact visual comparison format remains OPEN.

## Relic / Legacy
Hierarchy:
> Ordinary < Relic < Legacy

Relic-copy inventory:
- one Relic identity may have quantity 1 or 2;
- forged duplicate is mechanically identical.

Exact original-vs-copy visual distinction:
> OPEN.

Legacies cannot be copied.

## No formula selection
Equipment UI must never imply equipment chooses whether an Ability uses Physical/Magical/Hybrid formula.
