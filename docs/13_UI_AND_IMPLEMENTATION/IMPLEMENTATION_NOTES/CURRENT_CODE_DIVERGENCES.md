# Implementation Notes — Current Code/Canon Divergences
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` main commit `b150921b277578f6169fbaa9ba36b45c984a6f42`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


These are known engineering gaps in the current proof runtime.

## 1. Mastery Points — HIGH
Repository proof/older docs may still contain an 8-point Mastery schedule.

Current authority:
> Mastery Points removed.

Required production implementation:
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
- 1 Prime slot/character from Chapter-4 Prime-loadout access until Sixfold Volition; 2 Prime slots/character after Volition;
- Recovered = one signature action/same round;
- Awakened = 3 Prime rounds;
- Prime Invocation costs **0 MP**;
- each Prime identity has **one use until restored by valid rest or an explicitly authored restoration effect**;
- Prime spent/Ready state **persists across battle end** until valid restoration;
- after any Prime manifestation ends, **3 full normal party rounds** must pass before another Ready Prime may be invoked;
- genuine fresh-HP enemy bodies/forms do **not** refresh spent Prime identities;
- same-bar phase/state changes do **not** refresh spent Prime identities;
- form/body transitions do **not** create a new automatic Prime-use allowance and do not erase or shorten an active 3-full-normal-round post-dismissal spacing gate;
- valid rest and explicitly authored restoration effects such as Emergency Kit can restore eligible spent Prime identities without bypassing the spacing gate.

## 3. Normal battle turn flow — HIGH
Proof runtime still implements the retired whole-round queue model.

Current proof code currently:
- locks enemy actions at round start;
- asks the player to select actions for all conscious party members;
- requires **Confirm Round** before resolution;
- sorts **Item** before **Defend** before ordinary commands through `round_resolver.gd`;
- resolves the queued combined action list afterward.

Current production battle flow:
- remains **discrete round-based**, not ATB;
- establishes normal turn order at round start from current effective Speed and tie rules;
- when a player character's turn arrives, the player selects that character's action and target/content from the current battle state;
- that action resolves before the next normal combatant acts;
- enemy/entity AI likewise chooses its legal action when its turn arrives from the then-current legitimate state;
- **Item** and **Defend** have no separate universal priority phases;
- there is no whole-party action queue and no universal **Confirm Round** step;
- Speed changes during the round affect later round ordering unless an explicit authored effect overrides the normal rule.

Do not use the current proof queue/confirm architecture as production battle-flow authority.

## 4. Currency — HIGH
Proof state:
- technical identifier `gold` and old proof values may remain.

Current player-facing currency terminology:
- **G**

Retired player-facing currency name:
- **Auren**

Detailed prices, payouts, balances, and liquidity values are rebuild-pending and must not be hard-coded from old proof fixtures during cleanup. Requires version-safe production state/schema/UI work. Internal migration may preserve a legacy technical identifier temporarily, but final player-facing presentation must use **G** and must not revive Auren.

## 5. Proof equipment/content — HIGH
GameState defaults still include:
- Proof Sword;
- Proof Warden Blade;
- proof armor;
- Potion;
- four-character proof party only.

They are fixtures, not current equipment/content authority.

Ilyra's current primary weapon family is:
> **Wardrods**

## 6. Save schema completeness — HIGH
Schema v1 proves persistence but does not yet carry the complete production progression/quest/loadout state.

Do not treat schema v1 proof completeness as production completeness.

## 7. Dialogue proof panel — LOW/MEDIUM
Current field proof dialogue panel occupies much more vertical space than the general lower-20–25% production target.

Function is proven; final layout remains open.

## 8. Combat proof UI — HIGH
Current proof:
- large text tables/log;
- proof command/target buttons;
- proof **Confirm Round** button;
- proof Flee button;
- proof numeric summaries;
- stale Prime terminology.

It is not the final battle HUD and does not represent the current turn-entry command flow.

## 9. Kessara service UI — MEDIUM
Service logic exists.
No production service menu/fee/timing presentation yet.

## 10. Current-facing naming — ONGOING
Legacy technical identifiers may remain internally until safe migration, but player-facing text must use current names.
