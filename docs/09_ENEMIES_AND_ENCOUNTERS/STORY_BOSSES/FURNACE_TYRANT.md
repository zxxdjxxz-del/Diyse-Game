# Furnace Tyrant — Current Working Recertification

**Chapter:** 5 — The Mountain Engine  
**Role:** mandatory miniboss  
**Status:** **WORKING PASS / POWER COMPLETE**

## Recovered identity preserved

Furnace Tyrant remains:
- a Black Host siege officer using captured Greyspires forge armor;
- **one body / one continuous HP bar**;
- a visible Heat risk/reward encounter;
- supported by a finite Furnace Servitor deployment;
- a same-bar late escalation, not a transformation.

It never gains a second ordinary action per round.

## Actual route-level reference

Chapter 5 begins at:
> **25,600 mandatory EXP = Lv17**

The Furnace Tyrant is the first named Chapter-5 reward, after the occupied forge-country entry segment.

Current entry-segment planning anchor:
> **~3,300 ordinary mandatory EXP before the Tyrant**

This uses part of Chapter 5's existing ordinary-EXP budget; it is not a hidden fixed award.

Mandatory pre-boss planning total:
> **~28,900 EXP = Lv18**

Fixed optional EXP available before Chapter 5:
- The Marks We Leave — 500
- Regional Hunt #1 — 1,000
- Regional Hunt #2 — 1,500
- Regional Hunt #3 — 2,200
- Regional Hunt #4 — 3,000

Fixed optional advantage:
> **8,200 EXP**

Completionist pre-boss planning total:
> **~37,100 EXP = Lv20**

The optional Ruin Forgemaster can be cleared on the approach and incidental optional combat can push the high side toward:
> **~Lv21**

Balance references:
- mandatory central — **Lv18**
- completionist — **Lv20**
- high-side — **~Lv21**

## Current raw line

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 23 | **3,400** | **100** | **72** | **66** | **56** | **32** | 0 | 5 |

Inherited baseline:
> Lv23 / 3,801 HP / 87 ATK / 51 MAG / 61 DEF / 50 Spirit / 30 SPD

Working change:
- HP **3,801 → 3,400**
- ATK **87 → 100**
- MAG **51 → 72**
- DEF **61 → 66**
- Spirit **50 → 56**
- SPD **30 → 32**
- EVA0 / SR5 retained

The fight is shorter but more threatening turn-to-turn.

---

# HEAT — LOCAL ENCOUNTER STATE

Heat is visible and encounter-specific.

Exactly three states:
> **Controlled → Heated → Overheated**

It is not:
- MP;
- a character resource;
- a Face;
- a universal gauge;
- a new standard combat subsystem.

The Tyrant begins:
> **Controlled**

## Controlled
- Tyrant direct damage: **−10% final damage**
- Tyrant: **+10 Total Defense**

## Heated
> baseline offense and defense

## Overheated
- Tyrant direct damage: **+15% final damage**
- Tyrant: **−15 Total Defense**

The risk/reward is deliberate:
> more Heat means more danger and a softer defensive body.

## Raising Heat
Raise Heat one state after resolution:
- **Furnace Ram**
- **Scouring Jet**
- Furnace Servitor **Feed Furnace**

Beginning Foundry Breaker Preparation also raises Heat one state.

Heat never rises above Overheated.

## Lowering Heat
A successful direct **Ice** damaging action against the Tyrant lowers Heat one state after damage.

Limit:
> at most **one Ice-driven Heat reduction per round**

This prevents multihit abuse.

The two authored Coolant Valves can also each lower Heat one state once.

Heat never falls below Controlled.

---

# ACTION KIT

## Furnace Lash
- one party member
- Physical / Neutral
- **195 Power**
- Base Hit **100**
- **20% Bleed**
- 1-round repetition lock
- does not change Heat

## Furnace Ram
- one party member
- Physical / Neutral
- **235 Power**
- Base Hit **95**
- no harmful-status rider
- raises Heat one state after resolution
- 1-round repetition lock

## Scouring Jet
- one party member
- Magical / Fire
- **185 Power**
- Base Hit **100**
- no harmful-status rider
- raises Heat one state after resolution

## Heat Wash
- all conscious party members
- Magical / Fire
- **135 Power per target**
- Base Hit **95**
- no harmful-status rider
- available only while Heated or Overheated
- 2-round repetition lock

## Stabilize Armor
> **Power: N/A — no direct damage**

Effects:
- lower Heat one state;
- +10 Total Defense through end of following round.

The Tyrant cannot select Stabilize Armor during Siege Without Return.

2-round repetition lock.

---

# FINITE FURNACE SERVITORS

At:
> **60% HP**

two Furnace Servitors enter once.

They:
- take ordinary enemy slots;
- never respawn;
- never grant the Tyrant an extra action;
- may be ignored or destroyed.

Encounter-instance body:

| HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **280** | 48 | **78** | 44 | 47 | 31 | 0 | 5 |

## Servitor — Scalding Vent
- one party member
- Magical / Fire
- **150 Power**
- Base Hit **100**
- **20% Burn**
- 1-round repetition lock

## Servitor — Feed Furnace
> **Power: N/A — no direct damage**

Effects:
- raises Furnace Tyrant Heat one state;
- the Servitor becomes **Overheated** until its next selected action.

Feed Furnace has a 2-round repetition lock.

## Servitor — Overheat Vent
Passive on-defeat trigger, only if that Servitor is currently Overheated:
- all conscious party members
- Magical / Fire
- **80 Power per target**
- Base Hit **100**
- **10% Burn per target**

This passive:
- is not an extra ordinary action;
- triggers at most once per Servitor.

---

# COOLANT VALVES

Two one-use battlefield support objects are present.

Each:

| HP | DEF | Spirit | EVA | SR |
|---:|---:|---:|---:|---:|
| **1** | 0 | 0 | 0 | 0 |

They deal no damage:
> **Power: N/A**

When a party action successfully reduces a Valve to 0 HP:
- that Valve is permanently spent;
- Furnace Tyrant Heat falls one state after the action resolves.

A Valve cannot reduce Heat below Controlled.

Using a Valve consumes the party member's normal selected action through the ordinary targeting/damage rules; no sixth combat command is created.

---

# FOUNDRY BREAKER

Foundry Breaker becomes eligible once the Tyrant is at or below:
> **50% HP**

## Preparation
Classification:
> **Interruptible Preparation**

Duration:
> **1 full round**

Beginning Preparation:
- consumes the Tyrant's selected action;
- raises Heat one state;
- visibly seals the furnace vents.

## Explicit interruption routes
Foundry Breaker is interrupted if, during its Preparation round:
1. Furnace Tyrant is reduced to **Controlled Heat** through legal Ice/coolant interaction; or
2. an action whose own sheet explicitly states that it can interrupt an eligible Interruptible Preparation succeeds.

Ordinary direct damage alone does not interrupt it.

Stun is not automatically interruption.

## Resolution
If not interrupted:
- all conscious party members
- Physical / Neutral
- **285 Power per target**
- Base Hit **95**
- **25% Staggered per target**

The current Heat final-damage modifier applies normally.

After resolution or interruption:
> **3-round repetition lock**

Failing to interrupt is intended to be survivable with Defend/mitigation.

---

# SIEGE WITHOUT RETURN

At:
> **30% HP**

the same body enters Siege Without Return.

No refill.
No free attack.
No Prime refresh.

For the rest of battle:
- Heat cannot fall below **Heated**;
- Stabilize Armor is unavailable;
- action priority shifts toward Furnace Lash / Furnace Ram / Scouring Jet / Heat Wash / Foundry Breaker;
- no second ordinary action is gained.

Because Heat cannot return to Controlled:
> Foundry Breaker can no longer be interrupted through cooling once Siege Without Return begins.

Explicit eligible interruption effects remain legal.

---

# PRIME INTERACTION

Recovered Last Sentinel may be used under normal Prime rules.

Sentinel Impact:
> **340 Power / 40% Defense penetration**

Furnace Tyrant's same-bar Heat/Siege transitions:
> **do not refresh Prime availability**

---

# DURATION CERTIFICATION

Target pacing:

### Mandatory Lv18
- aggressive high-Heat route: **~8–9 rounds**
- normal mixed Heat/support route: **~9–10 rounds**
- safety/cooling/support-clear route: **~10–11 rounds**

### Completionist Lv20
- typical: **~7–8 rounds**

### High-side ~Lv21
- typical: **~6–7 rounds**

Completionist progression is intentionally allowed to shorten the encounter.

## Verdict

Direct-damage Power is explicit for:
- Furnace Lash — **195**
- Furnace Ram — **235**
- Scouring Jet — **185**
- Heat Wash — **135 per target**
- Foundry Breaker — **285 per target**
- Servitor Scalding Vent — **150**
- Servitor Overheat Vent — **80 per target**

Non-damaging:
- Stabilize Armor — **Power N/A**
- Feed Furnace — **Power N/A**
- Coolant Valves — **Power N/A**

> **WORKING PASS / POWER COMPLETE**
