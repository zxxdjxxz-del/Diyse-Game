# Diyse — Retired UI & Runtime Firewall
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


Do not implement current-facing UI for:

## Removed systems
- Mastery Points
- Synthesis
- Barrier
- Brace
- global Break/Stagger meter
- natural Accuracy stat
- general Accessory slot
- Prime Concordant
- Prime XP/levels
- Standard Card charges/deck/hand/draw/discard
- character-specific resource gauges not currently canon

## Retired terminology
- Resource Face
- Last Measure
- MDEF as primary display term
- Blackstone
- Crownhold / The Crownhold
- Southhold
- Edgelands
- Diysereach
- Westreach
- Yahtrens Stand
- Sixfold Accord
- Sixfold Annex
- Elemental Hexarch
- Sixfold Crucible

## Proof-only content
Do not ship proof names as final content:
- Potion placeholder where the current Consumable catalog supplies final names;
- Proof Sword / Proof Armor records;
- proof enemy/card IDs;
- `first_champion` as a player-facing Prime label;
- `Gold` as final currency;
- `Diyse 7B.5F` / `Audit98` proof screen titles.

## Old progression UI
Do not expose the Audit123-era 8-point Mastery schedule.

Current v85:
> automatic Masteries by Class Level.
