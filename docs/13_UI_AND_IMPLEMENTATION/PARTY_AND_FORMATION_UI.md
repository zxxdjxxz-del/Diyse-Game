# Diyse — Party & Formation UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## Permanent roster
Exactly six:
- Cyanis
- Ilyra
- Torren
- Nimera
- Vaelira
- Seyrik

Stable implementation IDs:
- `cyanis`
- `ilyra`
- `torren`
- `nimera`
- `vaelira`
- `seyrik`

Current display names are first-name-only and must not be reconstructed from retired surname text in old proof/dialogue material.

## Active combat party
Maximum:
> **4**

Recruitment and active-party membership are separate state.

An unrecruited permanent character:
- remains a known implementation identity;
- does not appear as an available formation choice;
- cannot occupy a production active-party slot.

The persistent active-party list must contain unique recruited permanent-character IDs only.

## IMPLEMENTED FOUNDATION
Current GameState/schema-v3 foundation now provides:
- all six stable permanent character records;
- per-character recruitment state;
- separate active-party stable-ID list;
- maximum-four validation;
- rejection of duplicate, unknown or unrecruited active-party entries;
- first-name-only display identity normalization;
- per-character reserved persistent-state envelope;
- save/load and v2 → v3 migration coverage.

The older four-character `party` array remains as a legacy proof battle fixture only. It is **not** the permanent-roster/formation authority.

No final party/formation menu has been implemented yet.

## Recruitment timing visibility
The menu must not expose unrecruited characters.

Permanent join sequence:
- Cyanis — start
- Ilyra — Ch0
- Torren — Ch1
- Nimera — Ch3
- Vaelira — Ch4
- Seyrik — end Ch6

Recruitment events must update production roster state through the stable character ID rather than by inserting display-name-only records into the proof party array.

## Formation
The player must be able to form a legal active party from recruited permanent characters once more than four are available.

Exact:
- swap animation;
- field leader selection;
- formation ordering UI;
- whether battle slots are visually numbered

remain OPEN unless separately locked.

## Reserves
Permanent characters outside the active combat party:
- do not act as normal combatants;
- do not take normal battle damage merely for being recruited;
- do not share temporary battle effects merely for being on the recruited roster.

This does not add a Row, front/back line, reserve-assist, or mid-battle Swap mechanic.

## Guests
Maevra may appear as an authored guest where story authority allows.

She is not:
- seventh permanent member;
- normal reserve roster character;
- permanent class/Card loadout target.

Kessara is nonplayable.
