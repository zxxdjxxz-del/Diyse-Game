# Diyse — Ruin Vanguard
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Master-canon class/resource authority:** **v2.08 / Audit123**, with compatible **Audit115** class normalization and later current working corrections, including the approved 2026-08-30 Ability-MP reduction.  
**Authority treatment:** explicit/newer working corrections are preserved as working overrides when they have not yet been promoted into the audit chain.


**Owner:** Seyrik  
**Class line:** Native Base Class  
**Identity:** high-HP/high-Attack physical-forward Ruin Hybrid Vanguard with Bleed/Burn pressure and one signature ordinary summon  
**Trait:** **Severed Command**  
**Ultimate:** **Controlled Apocalypse**

## Ability spine
| Unlock | Ability | MP | Current effect |
|---:|---|---:|---|
| CL1 | **Ruin Cleave** | 9 | One enemy; Hybrid / Ruin **75% Attack / 25% Magic**; **165 Power**; **20% Bleed**. |
| CL1 | **Rift Lance** | 10 | One enemy; Hybrid / Ruin **75% Attack / 25% Magic**; **175 Power**; **10% Staggered**. |
| CL1 | **Ember Brand** | 10 | One enemy; Hybrid / Fire **75% Attack / 25% Magic**; **150 Power**; **20% Burn**. |
| CL3 | **Fracturing Brand** | 17 | All enemies; Hybrid / Ruin **75% Attack / 25% Magic**; **145 Power per target**; **20% Bleed** per target. |
| CL6 | **Call Shardfang** | 26 | **Power: N/A for Seyrik's selected command.** One enemy + battlefield; deploy **Shardfang Hound for 3 normal rounds including deployment**. Entry attack **Ruinbound Pounce** hits the selected enemy for **135 Power, Hybrid / Ruin 75% Attack / 25% Magic, Base Hit 100**. Only one Shardfang may exist; Call Shardfang is unavailable while that instance remains active. |
| CL9 | **Unmaking Blow** | 26 | One enemy; Hybrid / Ruin **75% Attack / 25% Magic**; **245 Power**; **25% applicable defensive-axis penetration**; against a Bleeding target deals **+15% final damage**. |
| CL13 | **Controlled Apocalypse** | 51 | Base Ultimate; all enemies; Hybrid / Ruin **75% Attack / 25% Magic**; **360 Power per target**; **25% applicable defensive-axis penetration**; applies **Attack −30% / Magic −30% for 2 rounds**. After the AoE/debuff package, resolve the current Shardfang branch defined below. |

## Shardfang Hound — ordinary summon rules
Shardfang is Seyrik's one signature ordinary summon.

It:
- is AI-controlled;
- uses no active-party slot;
- is not a Card, Prime, permanent party member, or separate command menu;
- creates no summon gauge, charge system, or build/spend resource;
- leaves immediately if Seyrik becomes incapacitated and does not automatically return if Seyrik is later revived;
- ends when its 3-normal-round duration expires or battle ends.

### Snapshot statistics
When Shardfang is created, snapshot the following from Seyrik's then-current effective combat values and round to the nearest whole number:
- **Max HP: 38%** of Seyrik's effective Max HP;
- **Attack: 90%** of Seyrik's effective Attack;
- **Magic: 70%** of Seyrik's effective Magic;
- **Defense: 70%** of Seyrik's effective Defense;
- **Spirit: 60%** of Seyrik's effective Spirit;
- **Speed: 105%** of Seyrik's effective Speed.

Those snapshot values remain Shardfang's own values for that manifestation; later changes to Seyrik's stats do not continuously recalculate them. Trait bonuses that explicitly affect Shardfang apply separately while their conditions are satisfied.

### Deployment and duration
Shardfang's 3-round duration uses normal-round timing:
- the round in which it is deployed counts as **round 1**;
- Ruinbound Pounce is part of Seyrik's deployment action and is Shardfang's only attack created by the deployment round itself;
- because current-round initiative was already fixed before Shardfang existed, deployment does not insert a new autonomous turn into that round;
- if Shardfang survives into the next normal round, include it in that round's initiative using its snapshot Speed;
- after the third counted normal-round duration checkpoint, Shardfang dismisses.

### Autonomous action — Shardfang Rend
On each eligible normal-round turn Shardfang actually receives after deployment:
- automatically choose the **living enemy with the lowest current HP percentage**; exact ties use stable encounter-slot order;
- use **Shardfang Rend**: Hybrid / Ruin **75% Attack / 25% Magic**, **100 Power**, **Base Hit 100**, **20% Bleed**;
- Shardfang receives at most **one autonomous Rend turn per normal round**.

**Bound Fang** raises Ruinbound Pounce **135 → 145 Power** and ordinary Shardfang Rend **100 → 110 Power**.

**Severed Command Rank II** gives Shardfang **+10 Base Hit** while Seyrik remains conscious.  
**Severed Command Rank III** gives Shardfang **+10% final damage** while Seyrik remains conscious.

The Bleed on Shardfang Rend is its own authored rider. Severed Command Rank I does not add another +5pp to it because that Rank applies to qualifying Ruin Vanguard Abilities, not Shardfang attacks.

### Awakened Prime interaction
When an Awakened Prime suspends the ordinary party:
- Shardfang is suspended with the ordinary party side;
- it receives no autonomous turns during Prime rounds;
- Prime rounds do **not** consume its normal-round duration checkpoints;
- it does not attack alongside the manifested Prime or become a Prime command;
- if Seyrik was conscious when suspension began, Shardfang resumes with its existing snapshot values and remaining normal-round duration when ordinary party combat returns.

## Controlled Apocalypse — Shardfang branch
Resolve Controlled Apocalypse in this order:
1. resolve the **360-Power Hybrid / Ruin** AoE against all enemies;
2. apply **Attack −30% / Magic −30% for 2 rounds** to eligible surviving enemies;
3. resolve exactly one of the following Shardfang branches;
4. establish/refresh Shardfang's 3-normal-round duration as specified.

### If Shardfang is absent
After the AoE/debuff package:
- deploy a fresh Shardfang with its normal snapshot statistics and **3-normal-round duration**;
- if at least one legal enemy survives, Ruinbound Pounce targets the surviving enemy with the **lowest current HP percentage**;
- this deployment costs no additional MP beyond Controlled Apocalypse.

### If Shardfang is already active
After the AoE/debuff package:
- Shardfang immediately performs **Empowered Shardfang Rend** against the surviving legal enemy with the lowest current HP percentage;
- Empowered Shardfang Rend is **Hybrid / Ruin 75% Attack / 25% Magic, 150 Power, Base Hit 100, 20% Bleed**;
- **Bound Fang** raises its Power **150 → 160**;
- after that immediate follow-up, refresh Shardfang's remaining duration to a fresh **3 normal rounds including the current round**;
- the immediate Empowered Rend is part of Controlled Apocalypse's resolution package and does **not** consume a separate normal turn or remove an already-existing later autonomous Shardfang turn in that same round.

Controlled Apocalypse does not add a direct Bleed rider to its own AoE; Bleed remains on Shardfang's Rend package and other separately authored Ruin Vanguard Abilities.

## Masteries
| Unlock | Mastery | Current effect |
|---:|---|---|
| CL3 | **Sharper Ruin** | Ruin Cleave +15 Power; Rift Lance +15 Power. |
| CL6 | **Branding Force** | Ember Brand Burn 20% → **30%**; Fracturing Brand Bleed 20% → **30% base**. |
| CL9 | **Bound Fang** | Shardfang Pounce 135 → **145 Power**; Rend 100 → **110 Power**; Controlled Apocalypse's Empowered Rend 150 → **160 Power**. |
| CL12 | **Controlled Unmaking** | Unmaking Blow costs 2 less MP: 26 → **24**; its Bleeding-target final-damage bonus +15% → **+20%**. |

All four Core Masteries unlock automatically at the listed Class Levels under the current v85 working override.


## Global references
- Damage/penetration/Ruin Hybrid rules: `05_BATTLE_SYSTEM/DAMAGE_FORMULAS.md` and `ABILITY_RULES.md`
- Hit/Evasion: `05_BATTLE_SYSTEM/BASE_HIT_AND_EVASION.md`
- Turn/round timing: `05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`
- Temporary stat changes: `05_BATTLE_SYSTEM/STAT_CHANGES.md`
- Elements/statuses: `05_BATTLE_SYSTEM/ELEMENTS.md` and `STATUS_EFFECTS.md`

## Firewall
Do not restore the retired Shardfang Defense-Down rider, summon gauge, controllable summon command menu, Rune subsystem, or the older first-Ruin-Ability-per-round damage Trait. Controlled Apocalypse keeps the current 75% Attack / 25% Magic Ruin-Hybrid rule rather than restoring an older superseded 60/40 split.
