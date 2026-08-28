# Diyse — Combat Engineering Rules

**Current written authority:** **v2.18 / Audit133**  
**Compatible parent authorities:** Audit132 / Audit131 / Audit130 / Audit129 / Audit128 / Audit127 / Audit126 / Audit125 / Audit124 / Audit123 / Audit122 / Audit121 / Audit120 / Audit119 / Audit116 / Audit115 where not superseded.

This is the implementation-facing combat baseline. Historical proofs remain useful only where compatible with the current authority chain.

---

# Core round structure

Diyse uses traditional discrete rounds.

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. Each enemy locks one legal action from the legitimate beginning-of-round state without inspecting unconfirmed player commands.
3. The player selects one action for every conscious active party member before the round is confirmed.
4. Resolve Item actions first, ordered by current effective Speed.
5. Resolve Defend actions second, ordered by current effective Speed.
6. Resolve all remaining party and enemy actions from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members use player-selected order.
9. Tied enemies/entities use stable deterministic order.
10. Resolve complete action/reaction/state-change packages, then end-of-round processing.

Speed determines order only. Speed never grants extra ordinary actions.

---

# Automatic hostile retargeting

If a queued player hostile action targets an enemy defeated before that action resolves in the same round:
- retarget to the next living enemy in encounter-slot order after the original target;
- if no later slot is living, wrap to the first living enemy;
- if no enemies remain living, battle resolution proceeds normally;
- retargeting changes only the target, not the action, cost, priority, Speed, or actor.

Applies to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless specifically overridden.

---

# Permanent command list

Exactly:
- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands without explicit change control.

Maximum active permanent party size = **4**.

---

# Direct-damage formulas

## Physical

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

## Magical

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

## Hybrid

Resolve authored Physical and Magical weighted components independently against Defense and Spirit, apply legal same-axis penetration separately, then combine.

Character-Ability Ruin remains 75% Attack / 25% Magic where the compatible Audit115 rule applies. Prime commands use their explicitly authored formulas.

Same-axis penetration adds in percentage points and caps at **75%**.

There is no universal random damage variance or hidden universal AoE penalty.

---

# Base Hit / Evasion — Audit122

There is no natural Accuracy stat.

For ordinary hit checks:

> **AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers**

> **EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers**

> **FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)**

Authoring targets:
- standard ~100 Base Hit
- heavy 90–95
- precision 105–115
- exceptional precision up to ~120

Exact authored Base Hit controls.

Hit/Evasion is separate from harmful-status application.

---

# Critical Hits — Audit120

- base Critical Chance = 5%
- bonuses add flat percentage points
- ordinary random Critical Chance cap = 50%
- eligible Critical multiplier = 1.5×
- Base Hit/Evasion resolves before the Critical roll
- miss → no Critical roll
- multihit direct actions roll independently per authored hit by default
- one authored Hybrid hit uses one Critical roll on its combined eligible direct damage
- eligible Magical direct hits use the same multiplier
- Crit does not bypass Defense/Spirit
- Crit does not automatically improve harmful-status application
- Burn, Bleed, explicitly no-Crit copied/echo damage, indirect Max-HP damage unless explicitly authored otherwise, and healing cannot Crit.

---

# Damage type / elements / Ruin

Every damaging character Ability is authored Physical / Magical / Hybrid.

Exactly four standard elements:
- Fire
- Ice
- Lightning
- Earth

Linked status pairs where explicitly authored:
- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

An elemental hit does not automatically inflict its linked status.

Ruin is a special affinity/school, not a fifth standard element.

---

# Universal harmful statuses

Exactly:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Compatible Audit115 timing/duration rules remain active except where later audits explicitly supersede them.

## Bleed — Audit122 controlling

Bleed:
- damages each round;
- damages again whenever the affected character acts;
- is indirect status damage and cannot Crit;
- ignores Defense/Spirit;
- may KO unless a specific encounter rule overrides.

The old one-proc-per-round limit is removed.

Bleed clears only when:
1. the affected unit is restored to full HP;
2. an eligible harmful-status clear removes it;
3. an eligible item removes it.

Partial healing and ordinary Regen do not remove Bleed unless full HP is reached or a valid status clear is explicitly included.

## Staggered

Staggered is an ordinary harmful status only, not a Break/Stagger meter.

Where older status wording says `Accuracy` penalty, interpret it as the corresponding **Base Hit percentage modifier**.

---

# Status Resistance

Current general raw stat bands:
- **0** Normal
- **5** Resistant
- **10** Highly Resistant
- **15** Exceptional

Immunity exists only when explicitly authored.

Audit133 does not restore old optional-Elite 60%/80% per-status working tables as a second generic status-resistance resolver. Identity-specific immunities and elemental affinities remain separate authored properties where compatible.

---

# Removed systems / ordinary states

Do not recreate under renamed equivalents:
- Barrier
- Brace
- global Break/Stagger meter
- Card Seals
- global Rune-effect system
- Imprints

Guard remains a valid non-status defensive state.

Ordinary stat Up/Down effects, Fields, Hunter's Measure, Prepared effects, class setup states, and protected/scripted encounter states are not universal harmful statuses merely because they alter combat state.

---

# Ability economy — Audit123 CLOSED

MP is the universal ordinary Ability resource.

Do not create character-specific combat gauges/resources.

Learned Abilities remain weapon-independent once learned unless an individual current authority explicitly says otherwise.

Equipment does not choose an Ability's authored Physical/Magical/Hybrid formula.

**The final class Ability MP certification is CLOSED under Audit123.** The current authored Base/Subclass MP tables pass cross-kit certification; do not reprice them without an explicit later balance failure or rules revision.

---

# Standard Cards

Current collection architecture:
- 24 Standard Cards
- 12 Prime Cards
- 36 total Cards

Standard distribution:
- Might 5
- Elements 5
- Grace 4
- Acuity 4
- Change 3
- Ruin 3

Maximum equipped Standard Cards per character = **3**.

Standard Cards:
- consume the user's selected action;
- are reusable;
- consume MP;
- require enough MP to pay their listed cost;
- are Card commands, not Abilities;
- do not use deck/hand/draw/discard, charges, duplicates, ranks, Essence, or refresh counters.

Current MP range = **18–48 MP**.

Current Acuity quartet:
- Faultline Sight
- Measured Response
- Predicted Impact
- Decisive Interval

Predicted Impact:
- one enemy
- Magical / Colorless
- Power 180
- Base Hit 110
- 28 MP
- 30% Stun on successful damaging hit
- no Break/Stagger-meter contribution.

Split Moment retains its explicit two-selected-action ceiling and Prime firewall under compatible Card authority.

---

# Prime framework

There are exactly 12 Primes: 6 Story + 6 Major Hunt.

Progression:
> **Recovered → Awakened**

No Concordant, Prime XP, Prime levels, duplicate progression, or upgrade-material system.

Current Invocation MP:
- Recovered Story — **50 MP**
- Awakened Story — **80 MP**
- Awakened Major Hunt — **90 MP**
- manifested commands — 0 additional MP

Awakened Prime:
- replaces/suspends the active party;
- exactly 3 directly controlled Prime rounds;
- one selected Prime command per Prime round;
- shared 3-full-normal-round cooldown after dismissal;
- once per identity per battle unless a genuine fresh-HP boss form refreshes availability.

Prime-local statuses vanish on dismissal under compatible current Prime rules.

Current numeric sync:

### Prismatic Deluge
- all enemies
- Magical
- Fire 90 / Ice 90 / Lightning 90 / Earth 90
- 360 total listed Power per target
- 15% linked status check per wave
- maximum 1 newly inflicted harmful status per target for the command.

### Regulator Fang
- one enemy
- Magical
- choose Fire/Ice/Lightning/Earth
- Power 250
- 25% Spirit penetration
- no harmful-status rider.

---

# Raw-stat authority

Mandatory named/special raw body stats:
- Ch1–4 — Audit129 + Audit130
- Ch5–8 — Audit131
- Ch9–13 — Audit132

Optional numbered-chapter Elite raw body stats:
- Audit133
- 12 current Elites
- no approved Ch10 optional Elite
- typical Elite duration ~2–4 serious party rounds
- tier: **Ordinary < Elite << Regional Hunt**

Do not fabricate unresolved targetable-component HP merely to fill a table.

---

# Chapter 4 combat firewall

Chapter 4 uses exactly Fire / Ice / Lightning / Earth in its research/regulation framework.

Wind and Water are removed and their old functions are not reassigned.

The Seventh Reaction is emergent four-element behavior, not a seventh element or reusable player system.

Reaction Conduit replaces Elemental Hexarch and uses only the four standard elements.

Regulation Crucible uses four chambers, exactly two active/targetable at once, with rotation:
> Fire/Ice → Lightning/Earth → Fire/Lightning → Ice/Earth

Former Wind speed/cadence inheritance and Water Barrier/restoration/stabilization inheritance are removed.

Current body HP:
- Regulation Crucible Form I — **2,400**
- The Seventh Reaction fresh Form II — **2,900**
- total body HP — **5,300**

---

# Determinism / regression expectations

Pure combat resolution must remain testable without animation timing.

Regression coverage should include:
- Item priority;
- Defend priority;
- Speed order/ties;
- enemy action locking;
- automatic hostile retargeting;
- Base Hit/Evasion formula and clamp;
- hit-before-Crit ordering;
- current Critical rules;
- Bleed round + action damage cadence;
- Bleed current clearing rules;
- Status Resistance bands;
- no Barrier/Brace/global Break meter;
- Standard Card 3-slot limit and MP payment;
- current 5/5/4/4/3/3 Standard-Card distribution;
- Prime 50/80/90 Invocation payment;
- Recovered/Awakened state behavior;
- Awakened three-round control;
- shared Prime cooldown;
- genuine fresh-HP boss-form refresh;
- current four-element/status architecture;
- Character-Ability 75/25 Ruin scope and explicit Prime exceptions.

Tests encoding superseded facts must be deliberately updated rather than preserved as compatibility behavior.

Presentation and animation consume resolver/state results; they do not define combat legality.
