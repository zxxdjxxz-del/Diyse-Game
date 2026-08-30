# Implementation Notes — Current Code/Canon Divergences
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


These are known engineering gaps at repository checkpoint `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.

## 1. Mastery Points — HIGH
Repository docs still state an 8-point Mastery schedule.

Current v85 authority:
> Mastery Points removed.

Required later implementation:
- delete/avoid point persistence;
- delete/avoid point counters;
- derive automatic unlocks from Base/Subclass CL.

## 2. Prime proof model — HIGH
Proof runtime still uses:
- `first_champion`;
- bearer lock;
- old proof direct-control assumptions;
- stale Prime timing/state behavior.

Current production:
- Last Sentinel current name;
- any acquired Prime can occupy any legal character Prime slot;
- 2 Prime slots/character after Volition;
- Recovered = one signature action/same round;
- Awakened = 3 Prime rounds;
- Prime Invocation costs **0 MP**;
- each Prime identity has **one use until restored** by a valid rest or other explicitly authored Prime-restoration effect;
- a spent Prime remains spent across battle end;
- after a Prime ends, **2 full normal party rounds** must pass before another available Prime may be invoked later in that battle;
- fresh-HP boss forms do **not** restore spent Prime availability.

## 3. Currency — HIGH
Proof state:
- `gold`

Current:
- **Auren**

Requires version-safe production state/schema work.

## 4. Proof equipment/content — HIGH
GameState defaults still include:
- Proof Sword;
- Proof Warden Blade;
- proof armor;
- Potion;
- four-character proof party only.

They are fixtures, not current equipment/content authority.

Ilyra's current weapon is:
> **Wardrod**

## 5. Save schema completeness — HIGH
Schema v1 proves persistence but does not yet carry the complete production progression/quest/loadout state.

Do not treat schema v1 proof completeness as production completeness.

## 6. Chapter IDs / scene-number docs — MEDIUM
Some older authoring documentation still stops at:
- `chapter_12`
- S062

Current:
- through `chapter_13`
- through S073

## 7. Dialogue proof panel — LOW/MEDIUM
Current field proof dialogue panel occupies much more vertical space than the general lower-20–25% production target.

Function is proven; final layout remains open.

## 8. Combat proof UI — HIGH
Current proof:
- large text tables/log;
- proof command/target buttons;
- proof Flee button;
- proof numeric summaries.

It is not the final battle HUD and still contains stale Prime terminology.

## 9. Kessara service UI — MEDIUM
Service logic exists.
No production service menu/fee/timing presentation yet.

## 10. Current-facing naming — ONGOING
Legacy technical identifiers may remain internally until safe migration, but player-facing text must use current names.
