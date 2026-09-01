# Diyse — Major Hunt #2: Crownless Siege Marshal → Crownless War Engine
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary enemy-production authority:** compatible **Audit90 / Audit93** plus accepted later tracker roster/action cleanups.  
**Primary raw-stat authority:** **Audit129 + Audit130 / Audit131 / Audit132 / Audit133 / Audit134 / Audit135**.  
**Current whole-project written authority:** **v2.20 / Audit135** plus newer Prime-restoration and turn-entry battle-flow corrections.  
**Migration rule:** later current names, chapter reindexing, four-element rules, removed-system firewalls, current Prime-restoration rules, and current turn-entry battle flow supersede stale earlier enemy text.


| Ref | Encounter / form | Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR | Architecture |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| — | **Crownless Siege Marshal** | 40 | 13,600 | 155 | 110 | 111 | 96 | 41 | 5 | 10 | Form I |
| — | **Crownless War Engine** | 41 | 16,900 | 174 | 122 | 121 | 105 | 39 | 0 | 10 | genuine fresh Form II |

## Unlock
After **Chapter 7**.

## Architecture
Crownless Siege Marshal → Crownless War Engine is a genuine fresh-body transformation. No third form.

Under the current Prime-restoration model, the fresh Form II **does not restore a spent Prime**. Prime availability carries through the transformation exactly as established by `05_BATTLE_SYSTEM/BOSS_FORM_RULES.md` and `07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md`.

## Scaling
Fixed authored tuning.
No dynamic player-level scaling.


## Recertification
Current unlock:
> **after Chapter 7**

Expected party position at first access:
- mandatory-route party: approximately **Lv32**
- all normally available optional EXP before this Hunt: approximately **Lv37**

Current encounter recommendation:
> **Lv41**

Form tuning:
- Crownless Siege Marshal — Lv40
- Crownless War Engine — Lv41

Recertified raw lines:

### Crownless Siege Marshal
- HP **13,600**
- ATK **155**
- MAG **110**
- DEF **111**
- Spirit **96**
- SPD **41**
- EVA **5**
- Status Resistance **10**

### Crownless War Engine
- HP **16,900**
- ATK **174**
- MAG **122**
- DEF **121**
- Spirit **105**
- SPD **39**
- EVA **0**
- Status Resistance **10**

Combined raw body HP:
> **30,500**

The two-form architecture is preserved. War Engine remains a genuine fresh body, but Prime spent/Ready state carries through unchanged.

### Prime-economy revalidation note
The existing Lv41/raw-stat recertification was completed under the older fresh-body Prime-refresh assumption. The numbers are retained in this timing/consistency pass, but this encounter requires runtime balance revalidation under the newer rest-based Prime model before final production certification.

## Power-complete action kit — v74
**Status:** **POWER COMPLETE**

## Form I — Crownless Siege Marshal

### Marshal Cleave
- one party member
- Physical / Neutral
- **340 Power**
- Base Hit100
- **25% Bleed**
- 1-round repetition lock

### Siege Ruin
- one party member
- Hybrid / Ruin
- **75% ATK / 25% MAG**
- **325 Power**
- Base Hit100

### Command Volley
- all conscious party members
- Physical / Neutral
- **245 Power per target**
- Base Hit95
- 2-round repetition lock

### Marshal Guard
> **Power: N/A — no direct damage**

Effect:
> **Defense +15% / Spirit +15% through the end of the following round**

2-round repetition lock.

## Fresh-body transition
At Form-I 0 HP:
> **Crownless War Engine begins with fresh HP**

Rules:
- spent/Ready Prime state carries through unchanged;
- party HP/MP do not refresh;
- no transition attack;
- no third form.

## Form II — Crownless War Engine

True construct:
> **Bleed Immune**

### Engine Crush
- one party member
- Physical / Neutral
- **390 Power**
- Base Hit95
- **30% Staggered**
- 2-round repetition lock

### Ruin Cannon
- one party member
- Magical / Ruin
- **380 Power**
- Base Hit100

### Fire Bombardment
- all conscious party members
- Magical / Fire
- **285 Power per target**
- Base Hit95
- **20% Burn per target**
- 2-round repetition lock

### Shock Ram
- one party member
- Magical / Lightning
- **365 Power**
- Base Hit100
- **25% Stun**
- 2-round repetition lock

### Overrun Preparation
> **Power: N/A — no direct damage**

Rules:
- consumes the War Engine's selected action on its current turn;
- establishes **Overrun** as a pending Prepared follow-up;
- locks **Overrun** as the War Engine's next selected action on its next eligible normal turn if it remains able to act;
- cannot be selected while Overrun is already prepared;
- 3-round repetition lock begins after Overrun resolves;
- no command prediction;
- no free action;
- Preparation alone does not make Overrun Interruptible; interrupt eligibility must be explicitly authored separately.

### Overrun
- all conscious party members
- Physical / Neutral
- **430 Power per target**
- Base Hit95
- **25% Staggered per target**

Overrun is legal only after Overrun Preparation.
