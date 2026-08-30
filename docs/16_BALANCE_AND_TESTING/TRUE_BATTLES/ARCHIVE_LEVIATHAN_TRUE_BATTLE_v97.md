# Archive Leviathan — Representative True-Battle Certification

**Version:** v97  
**Chapter / Scene:** Chapter 2 / S013 — Sunken Archive  
**Encounter:** Archive Leviathan  
**Test type:** design-layer stochastic true-battle simulation  
**Verdict:** **PASS / RETAIN**

## Purpose
This test replaces the earlier paper-only pacing proof with a reproducible battle model using the actual Chapter-2 party state, current Ability/MP rules, equipment, hit/evasion, Criticals, statuses, action locks, current v96 Bleed escalation, healing/cleansing, and the finalized Recorded Pattern trigger below.

This is not runtime-engine QA. It is the current design oracle for implementation and later engine testing.

## Encounter authority used
Archive Leviathan:
- Lv9
- HP **1,900**
- ATK **50**
- MAG **52**
- DEF **31**
- Spirit **33**
- SPD **25**
- EVA **0**
- SR **5**
- one continuous HP bar
- Emergent state at **45% HP**
- no refill, transition damage, fresh body, or Prime refresh

Actions:
- **Leviathan Rend** — one target; Physical / Neutral; **220 Power**; Base Hit 100; 25% Bleed; 1-round repetition lock
- **Vault Crash** — all conscious party members; Physical / Neutral; **140 Power per target**; Base Hit 95; 15% Staggered per target; 2-round repetition lock
- **Archive Undertow** — Emergent only; all conscious party members; Magical / Colorless; **150 Power per target**; Base Hit 100; no status; 2-round repetition lock

Where no exact current action-selection percentage exists, the current enemy action-selection fallback applies: uniform selection among currently legal actions after state and repetition-lock restrictions.

## Recorded Pattern — exact v97 trigger
Recorded Pattern is **Power: N/A** and never predicts an unconfirmed command.

Eligibility:
- Basic Attack;
- direct-damage Ability;
- direct-damage Standard Card.

Not eligible:
- Items;
- healing/support-only commands;
- a counter/reaction that did not actually resolve;
- Prime commands.

Exact trigger:
1. Track each actor's most recently completed eligible direct-damage action identity.
2. If that actor next completes the **same exact eligible direct-damage action** on their next offensive action, that use is a **repeat candidate**.
3. A non-eligible action by that actor breaks that actor's consecutive-offense repetition chain.
4. The repeat that creates the candidate deals its normal full damage; Recorded Pattern never taxes the action retroactively.
5. At the end of the full party round, if one or more repeat candidates occurred, the **last repeated eligible action to resolve that round** becomes the single visible Recorded Pattern.
6. Action identity is actor-qualified. Cyanis's Basic Attack and Ilyra's Basic Attack are different identities.
7. While the Pattern remains active, later use of that same actor-qualified action against the Leviathan deals **20% less final direct damage**.
8. A later qualifying repeat may replace/refresh the single Pattern; Patterns never stack.

Duration:
- State A: **2 full party rounds**;
- Emergent: newly created Patterns last **1 full party round**;
- an already-active Pattern carries its remaining duration through the 45% threshold.

This implements the authored identity of reacting to **repeated completed offense**, not randomly recording an unrelated first use.

## Party snapshot — mandatory route
**Player Level:** Lv6  
**Active party:** Cyanis / Ilyra / Torren / Maevra  
**Primes:** unavailable  
**Subclass:** unavailable  
**Starting state:** full HP / full MP at the pre-basin recovery pocket

### Cyanis — Crest Knight CL3
- HP 417 / MP 40
- ATK 68 / MAG 55 / DEF 71 / Spirit 56 / SPD 24
- Crestblade: +37 ATK / +28 MAG
- Crest Plate: +28 DEF / +21 Spirit
- Yahtrean Shield: +15 DEF / +10 Spirit
- legal tested offense: Basic Attack, Crest Strike, Resonant Pulse
- Harmonized Crest Rank I active

### Ilyra — Blue Warden CL3
- HP 397 / MP 50
- ATK 54 / MAG 70 / DEF 42 / Spirit 68 / SPD 24
- Wardrod: +29 ATK / +30 MAG
- Blue Warden Mail: +18 DEF / +22 Spirit
- Warding Focus: +9 MAG / +19 Spirit
- legal tested package: Basic Attack, Mend, Clear Warding, Warden's Valor
- Gentle Hands active
- Clear Warding: remove 1 eligible harmful status and grant **+5 Status Resistance for 2 rounds**

### Torren — War Archer CL4
- HP 377 / MP 40
- ATK 81 / MAG 23 / DEF 46 / Spirit 40 / SPD 28
- Yahtrean War Bow: +48 ATK
- War Archer Gear: +24 DEF / +18 Spirit
- legal tested package: Basic Attack, Cinder Shot

### Maevra — story guest
- HP 417 / MP 38
- ATK 50 / MAG 23 / DEF 36 / Spirit 34 / SPD 25 / EVA 5 / SR 5
- Command Spear: +18 ATK
- Commander's Harness: +9 DEF / +9 Spirit
- legal tested package: Basic Attack, Linebreaker, Decisive Thrust

### Prepared consumable snapshot
Legal early-core purchased stock used for the canonical prepared test:
- 3 × Field Salve
- 2 × Trauma Remedy
- 1 × Rousing Salts

Total listed purchase value: **150 Auren**.

This is a reproducible test inventory, **not** a new mandatory free grant.

## Party snapshot — completionist/high-side
**Player Level:** Lv7  
**Active party:** same four  
**Class Levels:** same early-Chapter-2 Base-class availability band  
**Starting state:** full HP / full MP

Legal high-side upgrades included:
- Cyanis — Dunmere Steel weapon line
- Ilyra — Blue Wardrod weapon line
- Torren/Maevra — current legal gear carried forward

Reference stats:
- Cyanis — HP456 / MP43 / ATK75 / MAG61 / DEF73 / Spirit57 / SPD24
- Ilyra — HP434 / MP54 / ATK60 / MAG77 / DEF44 / Spirit70 / SPD25
- Torren — HP412 / MP43 / ATK83 / MAG25 / DEF48 / Spirit42 / SPD29
- Maevra — HP456 / MP41 / ATK52 / MAG24 / DEF38 / Spirit35 / SPD26 / EVA5 / SR5

Same prepared consumable snapshot was used so the level/gear advantage remains the main comparison variable.

## Current Bleed rule used
Party-side Bleed uses v96 authority:
- **3% Max HP per qualifying proc** initially;
- one round proc plus one proc whenever the affected unit takes an actual action;
- after that unit completes 3 turns with the same Bleed uncleared, magnitude becomes **4% per proc** until removal.

The Leviathan is a mandatory boss, so party-applied Bleed uses the established 50% boss magnitude conversion.

## Fixed normal-play policy
The stochastic test uses a fixed, legal tactical policy rather than omniscient optimization.

- Cyanis alternates legal Crest offense where MP permits and avoids knowingly repeating the currently visible Recorded Pattern when a reasonable alternative exists.
- Torren uses Cinder Shot while MP permits unless that exact action is currently Pattern-taxed, then falls back to Basic Attack.
- Maevra uses Decisive Thrust / Linebreaker while legal and useful, then Basic Attack.
- Ilyra removes Bleed promptly when legal, heals materially injured allies, and otherwise contributes Warden's Valor / Basic Attack.
- Trauma Remedy is used to clear dangerous Bleed when item use is preferable to spending Ilyra's turn/MP.
- Field Salve is used for materially low HP.
- Rousing Salts is reserved for a KO.
- No future enemy action, hit/miss result, Critical, status roll, or target is known to the party when commands are selected.

## 20,000-run results — mandatory Lv6 prepared
- wins: **100%**
- mean duration: **10.05 rounds**
- median duration: **10 rounds**
- 10th–90th percentile: **9–11 rounds**
- any individual KO incidence: **0.05%**
- mean party HP remaining: **53.74%**
- Bleed encountered: **70.90%**
- Staggered encountered: **75.93%**
- Bleed reached 4% escalation: **4.87%**
- mean Recorded-Pattern-taxed hits: **4.99**
- mean Burn ticks on Leviathan: **1.23**
- median Emergent-state entry: **round 6**

Mean item use:
- Field Salve: **0.84**
- Trauma Remedy: **1.02**
- Rousing Salts: **0.0003**

### Mandatory verdict
The original mandatory-normal target was **~9–10 rounds**. The true battle lands essentially on target at a 10-round median and 10.05-round mean.

The updated Bleed rule creates real cleansing/resource pressure without making the fight unstable when the player uses legal early-game recovery tools.

## 20,000-run results — completionist/high-side Lv7 prepared
- wins: **100%**
- mean duration: **8.58 rounds**
- median duration: **9 rounds**
- 10th–90th percentile: **8–9 rounds**
- any individual KO incidence: **0%**
- mean party HP remaining: **59.02%**
- Bleed encountered: **63.81%**
- Staggered encountered: **70.35%**
- Bleed reached 4% escalation: **2.63%**
- mean Recorded-Pattern-taxed hits: **2.85**
- mean Burn ticks on Leviathan: **1.23**
- median Emergent-state entry: **round 5**

Mean item use:
- Field Salve: **0.19**
- Trauma Remedy: **0.88**
- Rousing Salts: **0**

### Completionist verdict
The existing high-side target was **~8–9 rounds**. The true battle lands directly inside that window and preserves a meaningful advantage over the mandatory route.

## No-item mandatory stress check
A separate Lv6 stress test used the same battle rules but **no consumables**.

- win rate: **99.955%**
- mean duration: **9.84 rounds**
- median duration: **10 rounds**
- 10th–90th percentile: **9–11 rounds**
- any individual KO incidence: **40.96%**
- mean party HP remaining: **37.9%**
- Bleed reached escalation: **57.09%**

This is not the canonical normal-prepared line. It demonstrates why the stronger v96 Bleed meaningfully rewards cleansing and early consumable preparation instead of behaving like negligible background damage.

## Representative mandatory battle log
Representative seed: **1500000**  
Result: **10-round win / no KO / 1 Field Salve / 1 Trauma Remedy**.

### Round 1 — 1,900 → 1,583 HP
- Torren — Cinder Shot: 91
- Maevra — Decisive Thrust: 80
- Leviathan — Rend on Maevra: 64
- Ilyra — Warden's Valor: 81
- Cyanis — Crest Strike: 65

### Round 2 — 1,583 → 1,274 HP
- Torren — Cinder Shot: 91
- Maevra — Decisive Thrust: 80
- Leviathan — Vault Crash: Cyanis29 / Ilyra38 + Staggered / Torren36 / Maevra41
- Ilyra — Warden's Valor: 81
- Cyanis — Resonant Pulse: 57
- Recorded Pattern becomes Ilyra / Warden's Valor for 2 rounds.

### Round 3 — 1,274 → 1,001 HP
- Torren — Cinder Shot Critical: 136
- Maevra — Basic Attack: 31
- Leviathan — Rend on Torren: 57
- Cyanis — Crest Strike: 72
- Ilyra — Basic Attack: 34
- Recorded Pattern becomes Torren / Cinder Shot for 2 rounds.

### Round 4 — 1,001 → 830 HP
- Torren — Basic Attack: 59
- Maevra — Basic Attack: 31
- Leviathan — Rend on Maevra: 64
- Cyanis — Basic Attack: 47
- Ilyra — Basic Attack: 34
- 45% threshold is crossed; Emergent state begins next round.
- Recorded Pattern becomes Ilyra / Basic Attack for 1 round.

### Round 5 — 830 → 666 HP
- Torren — Basic Attack: 59
- Maevra — Basic Attack: 31
- Leviathan — Vault Crash: Cyanis29 / Ilyra38 / Torren miss / Maevra41
- Ilyra — Basic Attack: 27 after Recorded Pattern reduction
- Cyanis — Basic Attack: 47
- Recorded Pattern becomes Cyanis / Basic Attack for 1 round.

### Round 6 — 666 → 505 HP
- Torren — Basic Attack: 59
- Maevra — Basic Attack: 31
- Leviathan — Rend on Ilyra: 60 + Bleed
- Ilyra — Basic Attack: 34; Bleed action proc: 12
- Cyanis — Basic Attack: 37 after Recorded Pattern reduction

### Round 7 — 505 → 378 HP
- Ilyra — Bleed round proc: 12
- Ilyra uses Trauma Remedy; Bleed removed before her normal action
- Torren — Basic Attack: 59
- Maevra — Basic Attack: 31
- Leviathan — Archive Undertow: Cyanis38 / Ilyra34 / Torren44 / Maevra47
- Cyanis — Basic Attack: 37 after Recorded Pattern reduction

### Round 8 — 378 → 217 HP
- Torren — Basic Attack: 59
- Maevra — Basic Attack: 31
- Leviathan — Rend on Cyanis: 45
- Ilyra — Basic Attack: 34
- Cyanis — Basic Attack: 37 after Recorded Pattern reduction

### Round 9 — 217 → 56 HP
- Torren — Basic Attack: 59
- Maevra — Basic Attack: 31
- Leviathan — Vault Crash: Cyanis29 / Ilyra miss / Torren36 / Maevra41
- Ilyra — Basic Attack: 34
- Cyanis — Basic Attack: 37 after Recorded Pattern reduction

### Round 10 — 56 → 0 HP
- Maevra commits a Field Salve at command lock because of low HP.
- Torren acts first and Basic Attacks for 59, defeating the Leviathan.

The final-round healing choice is deliberately retained in the representative log: commands are locked before normal actions, so the party cannot know Torren will definitely end the fight before Maevra's committed item resolves.

## Final certification
> **ARCHIVE LEVIATHAN — TRUE-BATTLE PASS / RETAIN**

Retain unchanged:
- HP **1,900**
- ATK50 / MAG52 / DEF31 / Spirit33 / SPD25 / EVA0 / SR5
- Rend **220 Power**
- Vault Crash **140 Power per target**
- Undertow **150 Power per target**
- status application chances
- 45% same-bar threshold
- one-bar architecture
- v96 Bleed rule

No direct-damage Power is reopened.

### Design closure added by v97
Only the deterministic **Recorded Pattern formation trigger** was completed. It resolves an implementation ambiguity and does not change the existing 20% penalty, durations, or threshold.

## Next representative anchor
**Regulation Crucible → Seventh Reaction** — Chapter 4 fresh-HP transformation test.
