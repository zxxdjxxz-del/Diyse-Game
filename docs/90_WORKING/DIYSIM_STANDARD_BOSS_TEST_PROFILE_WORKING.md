# DiySim Standard Boss Test Profile

**Status:** WORKING DIYSIM TEST POLICY / NOT OWNER CANON / NOT APPROVED FOR MAIN

Use this profile as the default cross-boss pressure test unless a boss-specific experiment explicitly overrides it.

## Standard pressure profile
- Enemy direct-damage **Power ×1.20**.
- Main boss **ATK/MAG: +5 effective stat levels** using the neutral natural-curve ratio.
- **HP unchanged**.
- **DEF unchanged**.
- **Spirit unchanged**.
- **Speed unchanged** unless a separate turn-order experiment is explicitly requested.

The +5 offensive layer is intentionally separated from durability. Earlier Zevraya testing showed that adding DEF/Spirit at the same time extended fights and compounded hazard exposure. The standard profile is therefore meant to increase threat without automatically making bosses into damage sponges.

## Required comparison
For each executable boss runtime, test at minimum:
1. the encounter's mandatory/central party level;
2. the encounter's established high-side party level.

Record at least:
- win rate;
- wipe rate;
- any-KO rate;
- mean rounds;
- median rounds;
- P10 rounds;
- P90 rounds.

Use the encounter's current competent mechanic-response policy for the primary pacing line. Additional Rush/ignore-mechanic lines may be retained as punishment checks where relevant.

## Current executable registry
The unified report currently includes:
- Hollow Watch Castellan — Lv2 mandatory / Lv3 high-side;
- First Command Warden — Lv11 mandatory / Lv13 high-side;
- Matron Zevraya — Lv24 mandatory / Lv28 high-side, non-diluting structure, Brood → Armor competent line.

Every newly executable boss runtime should be added to the same report so round pacing can be compared under one consistent pressure profile.

This file defines simulator test policy only. It does not rewrite encounter owner stats or promote the profile to game canon.
