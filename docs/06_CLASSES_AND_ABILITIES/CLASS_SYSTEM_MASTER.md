# Diyse — Class System Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.


## Current architecture

Each permanent character has:
- one native Base Class;
- one reciprocal Subclass;
- a Base Class cap of **CL13**;
- a Subclass cap of **CL13**.

Subclasses do not become usable before the **Sixfold Volition at the end of Chapter 7**.

Reciprocal donor pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

## Selected-class behavior

The selected class controls:
- the currently active class Trait;
- the selected-class natural-stat package;
- which class receives battle CEXP.

Unlocked learned Abilities remain learned and usable according to current persistent-Ability rules; changing selected class does not erase already learned Abilities.

Equipment does not choose an Ability's Physical / Magical / Hybrid formula.

## Base-Class learning rhythm

| Class Level | Result |
|---:|---|
| CL1 | starting abilities + Trait Rank I |
| CL3 | next Ability + Core Mastery 1 |
| CL6 | next Ability + Core Mastery 2 + Trait Rank II |
| CL9 | next Ability + Core Mastery 3 |
| CL12 | Core Mastery 4 + Trait Rank III |
| CL13 | Base Ultimate + cap |

## Subclass learning rhythm

Current class-specific normalized kits use:

| Class Level | Result |
|---:|---|
| CL1 | Subclass Ability 1 + Trait Rank I + donor Primary access |
| CL3 | Subclass Mastery 1 + donor Armor access |
| CL4 | Subclass Ability 2 |
| CL5 | Subclass Mastery 2 + donor Secondary access |
| CL6 | Trait Rank II |
| CL7 | Subclass Ability 3 + **Equipment Mastery** |
| CL9 | Subclass Ability 4 |
| CL11 | Subclass Ability 5 + **Legacy Mastery** |
| CL12 | Trait Rank III |
| CL13 | Subclass Ultimate + cap |

### Reconciliation note
The short summary near the front of v85 still contains an inherited line placing the fifth normal Subclass Ability at CL10. The later/current normalized class-specific kits consistently place that fifth Ability at **CL11**, and the current Mastery correction also uses CL11 for Legacy Mastery. This extraction follows the specific normalized kits and flags the older generic CL10 line as stale summary text.

## Mastery state — current working override

Audit123's published master-canon version used Mastery Points.

The newer active v85 working decision removes the **Mastery Point resource entirely**.

Current working behavior:
- no Mastery Point grants;
- no banking;
- no spending;
- no respec/refund;
- no replacement skill-point currency;
- Masteries change from **Locked → Unlocked** automatically when the required Class Level is reached.

Mastery completion occurs at:
- Base CL12 for all four Core Masteries;
- Subclass CL11 for all four Subclass Masteries.

This newer Mastery-Point removal is a **working-level override pending formal master-canon promotion**, and must not be misrepresented as already written into Audit123.

## Synthesis
**Removed.**

See `RETIRED_SYNTHESIS_FIREWALL.md`.

## Donor equipment milestones

Current working rules:
- Subclass CL7 / Equipment Mastery opens class eligibility for the donor Base-Class Relic, subject to actually owning that Relic and any other established requirements.
- Subclass CL11 / Legacy Mastery opens class eligibility for the donor Base-Class Legacy, subject to the donor Legacy actually being completed/obtained and any other established requirements.
- A character's own native Base-Class Legacy does **not** require donor Legacy Mastery or Synthesis.

Exact item definitions belong to `08_ITEMS_AND_EQUIPMENT`.
