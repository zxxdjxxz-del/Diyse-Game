# Diyse — Class / CEXP / Mastery UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


# CURRENT WORKING OVERRIDE
> **Mastery Points do not exist.**

This file intentionally supersedes the stale repository UI implication from Audit123-era documents.

## Class display
For each permanent character, UI must be able to show:
- Base Class;
- Subclass after Sixfold Volition;
- selected class for CEXP receipt;
- current Class Level;
- cumulative CEXP toward next Class Level;
- learned Abilities;
- Trait rank;
- Ultimate unlock;
- Mastery state.

Base/Subclass cap:
> **CL13**

Cumulative CL13 CEXP:
> **6,000**

Base and Subclass CEXP are separate.

## CEXP assignment
Every recruited permanent character receives the full awarded CEXP package.

That character's currently selected class receives:
> **100%**

Unselected class receives:
> **0**

The UI therefore must clearly indicate which class is currently selected for that character.

Exact switching workflow/restrictions should follow the gameplay implementation authority; do not invent hidden penalties.

## Automatic Masteries
Base:
- CL3 Core 1
- CL6 Core 2
- CL9 Core 3
- CL12 Core 4

Subclass:
- CL3 Subclass 1
- CL5 Subclass 2
- CL7 Equipment Mastery
- CL11 Legacy Mastery

UI state:
> **Locked → Unlocked**

No:
- spend;
- purchase;
- point icon;
- points remaining;
- respec;
- refund.

## Donor eligibility
At Subclass CL7:
- donor Relic class eligibility may open, subject to actual ownership.

At Subclass CL11:
- donor Legacy class eligibility may open, subject to actual donor Legacy completion/ownership.

The UI must distinguish:
> class eligibility

from:
> item ownership.

A locked item should explain the actual missing condition rather than inventing Mastery Point cost.
