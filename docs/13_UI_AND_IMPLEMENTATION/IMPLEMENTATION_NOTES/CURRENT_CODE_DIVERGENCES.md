# Implementation Notes — Current Code/Canon Divergences
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

These are known engineering gaps in the current proof runtime.

## Recently reconciled — Relic-copy Face terminology
The Kessara Relic-copy ownership layer now canonicalizes the current Face set:
> **Might / Elements / Grace / Perception / Memory / Ruin**

Retired Resource/Acuity/Change values are accepted only as compatibility inputs and normalize to Perception/Memory. They must not reappear as current-facing Face labels.

## Recently reconciled — persistent G wallet / Kessara fee
GameState now has a persistent `wallet_g` with the current **2,500 G** starting baseline.

Save schema is now **v2** with a deliberate v1 → v2 migration. Legacy `rewards.gold` remains isolated as proof battle-result payload and is **not** reinterpreted as the party wallet.

Kessara's closed **6,000 G** fee is now integrated into the service transaction:
- insufficient G fails without component/item mutation;
- successful copy deducts exactly 6,000 G;
- fee deduction + component consumption + forged-copy state are committed through one GameState transaction.

Remaining currency debt is primarily reward/shop/UI integration and removal or containment of legacy proof `gold` naming outside the wallet.

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
- 2 Prime slots/character after Volition;
- Recovered = one signature action/same round;
- Awakened = 3 Prime rounds;
- Prime Invocation costs **0 MP**;
- each Prime identity has **one use until restored** by a valid rest or other explicitly authored Prime-restoration effect;
- a spent Prime remains spent across battle end;
- after a Prime ends, **2 full normal party rounds** must pass before another available Prime may be invoked later in that battle;
- fresh-HP boss forms do **not** restore spent Prime availability.

The proof resource `game/content/cards/first_champion_recovered.tres` is therefore a migration fixture, not current-facing Prime content authority.

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
- Speed changes after initiative is locked do **not** reshuffle that current round, but can affect later round setup if still active.

Do not use the current proof queue/confirm architecture as production battle-flow authority.

## 4. Currency/reward integration — MEDIUM/HIGH
Persistent wallet semantics are now current **G**, but proof battle/reward code still contains technical `gold` keys and old tiny proof reward values.

Current player-facing authority:
- **G**

Retired player-facing currency name:
- **Auren**

Required next work:
- route actual authored encounter/shop/service transactions through the persistent G wallet;
- replace or migration-contain proof `gold` reward payload naming;
- keep final UI labels strictly **G**.

Do not treat proof `42 gold`-style regression values as production economy data.

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
Schema **v2** now proves migration plus persistent G wallet state, but it still does not carry the complete production roster/progression/quest/loadout model.

Do not treat schema-v2 proof completeness as production completeness.

Retired Face labels may still exist in historical saved Relic/component records; current runtime compatibility maps them into the current Face names rather than treating them as new/current identities.

## 7. Chapter IDs / scene-number docs — MEDIUM
Some older authoring documentation still stops at:
- `chapter_12`
- S062

Current:
- through `chapter_13`
- through S073

## 8. Dialogue proof panel — LOW/MEDIUM
Current field proof dialogue panel occupies much more vertical space than the general lower-20–25% production target.

Function is proven; final layout remains open.

## 9. Combat proof UI — HIGH
Current proof:
- large text tables/log;
- proof command/target buttons;
- proof **Confirm Round** button;
- proof Flee button;
- proof numeric summaries;
- stale Prime terminology.

It is not the final battle HUD and does not represent the current turn-entry command flow.

## 10. Kessara service UI — MEDIUM
Core copy eligibility/state logic and the exact 6,000-G transaction are implemented.

Still required:
- production service menu;
- final unlock/timing presentation;
- original-versus-forged-copy presentation;
- confirmation/animation polish.

## 11. Character visual placeholders — MEDIUM
`game/characters/placeholders/` and the proof portrait registry remain runtime stand-ins only.

They must not be treated as production character appearance references. Exact current appearance authority lives in `asset_sources/characters/current/` and `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/`.

Production derivatives should be created in an appropriate runtime asset lane rather than pointing gameplay directly at source-master files.

## 12. Current-facing naming — ONGOING
Legacy technical identifiers may remain internally until safe migration, but player-facing text must use current names.

Examples that still require migration care include `first_champion`, proof `gold` reward keys, and older environment/state IDs whose filenames/keys predate current terminology. Stable technical IDs may be preserved when necessary, but they must not leak retired display names into production UI.
