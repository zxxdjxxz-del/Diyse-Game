# First Command Warden — Current Working Recertification

**Chapter:** 3  
**Scene:** S020 — Old City Command Station  
**Status:** **WORKING PASS / POWER COMPLETE**

## Actual route-level reference

Cumulative mandatory EXP before the Warden:
- end Chapter 2: **6,400**
- Chapter-3 mandatory EXP earned before the Warden: **4,880**
- total before battle: **11,280 EXP**

That places the mandatory-route party at:
> **Lv11**, 820 EXP short of Lv12.

Fixed optional EXP available before this battle:
- The Marks We Leave — 500
- Regional Hunt #1 — 1,000
- Regional Hunt #2 — 1,500

Completionist fixed-content total before the Warden:
> **14,280 EXP**

That is:
> **Lv12**, only 120 EXP short of Lv13.

Optional-Elite / incidental optional combat can therefore place a high-side completionist at:
> **~Lv13**

Balance references:
- mandatory central — **Lv11**
- completionist fixed-content — **Lv12 approaching Lv13**
- high-side completionist — **~Lv13**

## Current raw line

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 14 | **2,850** | **72** | **72** | **43** | **43** | **30** | 0 | **10** |

Former inherited line:
> Lv14 / 3,723 HP / 57 ATK / 57 MAG / 43 DEF / 43 Spirit / 29 SPD

The old body was too durability-heavy for a boss that already taxes actions through Command Seals, the Command Ring, and Recorded Analogue behavior.

## Architecture
- one continuous HP bar
- State A — **Imposed Authority**
- State B — **Challenged Authority**
- State B begins at **45% HP**
- no HP refill
- no transition damage
- no free threshold attack
- no fresh body
- no Prime refresh

Last Sentinel is not recovered until after this battle, so the party has no Story Prime available here anyway.

## State A — Imposed Authority

### Authority Lance
- one party member
- Physical / Neutral
- **190 Power**
- Base Hit **100**
- no harmful-status rider

### Judgment Pulse
- all conscious party members
- Magical / Colorless
- **140 Power per target**
- Base Hit **100**
- no harmful-status rider
- 2-round repetition lock

### Command Seal
> **Power: N/A — no direct damage**

Target:
- one conscious party member

The Seal visibly records that target's most recently completed ordinary command category:
- Attack
- Ability
- Card
- Item
- Defend

Duration:
> **2 rounds**

It never disables or removes a command.

If the sealed character repeats the marked command category before the Seal expires, their selected action still resolves normally. After it resolves, the Seal triggers once:

#### Seal Reprisal
- sealed character only
- Magical / Colorless
- **100 Power**
- Base Hit **100**
- no status rider
- the Seal then clears

If the character does not repeat the marked category before expiry, the Seal expires harmlessly.

Command Seal itself has a 2-round repetition lock.

This uses only completed action history; it does not read unconfirmed player commands.

## Command Ring

Before a Major Ruling, the suspended Command Ring aligns and becomes targetable for one full Preparation round.

### Command Ring

| HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **260** | 0 | 0 | **40** | **46** | 0 | 0 | 10 |

The Ring is a targetable support object only while aligned.

Reducing it to 0 HP during Preparation:
- disrupts the Ring;
- cancels that Major Ruling;
- does not deal transition damage;
- does not damage the Warden;
- returns the Ring to its suspended inactive state.

The Ring may align again after **3 full rounds**.

It is not a Break gauge or Barrier.

### Major Ruling
Preparation:
> **1 full round**

If the Ring remains functional:
- all conscious party members
- Magical / Colorless
- **210 Power per target**
- Base Hit **95**
- **15% Stun per target**
- 3-round repetition lock after resolution

If the Ring is disrupted:
> Major Ruling is canceled.

## Recorded action system

After an eligible completed ordinary player action, the Warden may record its function.

Eligible:
- ordinary Attack;
- direct-damage Ability.

Never eligible:
- Standard Card;
- Prime;
- Ultimate;
- Item;
- Defend;
- healing/support-only Ability;
- Prepared reaction;
- character-unique non-damage command.

The Warden stores at most one record at a time.

It never copies actor animation, equipment effects, status riders, penetration, element, multihit count, or unique secondary mechanics.

It returns a weaker functional analogue through its own emitter:

### Recorded Physical Analogue
For an eligible recorded Physical attack:
- single-target record — Physical / Neutral — **150 Power**
- AoE record — Physical / Neutral — **105 Power per target**
- Base Hit **100**

### Recorded Magical Analogue
For an eligible recorded Magical attack:
- single-target record — Magical / Colorless — **150 Power**
- AoE record — Magical / Colorless — **105 Power per target**
- Base Hit **100**

### Recorded Hybrid Analogue
For an eligible recorded Hybrid attack:
- 50% ATK / 50% MAG
- single-target record — Neutral — **150 Power**
- AoE record — Neutral — **105 Power per target**
- Base Hit **100**

A recorded multihit becomes one analogue hit. It does not inherit the original hit count.

After use, the record clears.

## State B — Challenged Authority

At 45% HP:
- Command Seal projectors shut down;
- no new Command Seals are created;
- the Command Ring rotates into defensive alignment and is no longer targetable;
- direct offense becomes heavier.

### Earlier Ring handling → opening protection

If the party disrupted at least one Major Ruling during State A:
> Warden gains **10% direct-damage reduction for 1 round** at State-B entry.

If the party disrupted no Major Rulings:
> Warden gains **15% direct-damage reduction for 2 rounds** at State-B entry.

This is the only retained consequence of earlier Ring handling.

No Barrier is created.

### Warden Crush
- one party member
- Physical / Neutral
- **245 Power**
- Base Hit **100**
- no harmful-status rider

### Challenged Verdict
- one party member
- Hybrid / Neutral
- 50% ATK / 50% MAG
- **230 Power**
- Base Hit **100**
- **20% Staggered**
- 1-round repetition lock

### Command Collapse
- all conscious party members
- Magical / Colorless
- **165 Power per target**
- Base Hit **95**
- **15% Stun per target**
- 2-round repetition lock

### Recorded Analogue
The same exact Recorded Physical / Magical / Hybrid coefficients remain available in State B:
- **150 Power single-target**
- **105 Power per target AoE**

The Warden does not gain a stronger copied-action coefficient simply because it entered State B.

## Duration certification

Mandatory-route target:
> **~10–11 rounds**

Completionist fixed-content target:
> **~8–9 rounds**

High-side Lv13 target:
> **~7–8 rounds**

Safety / repeated Ring-disruption / extra recovery:
> **~11–12 rounds**

The 2,850-HP body is intentionally lower than the inherited 3,723 HP because this encounter already consumes player actions through:
- Ring disruption;
- Seal routing;
- healing from heavier rulings;
- Recorded Analogue adaptation.

Completionist progression remains valuable rather than being erased by boss scaling.

## Power-completeness verdict

Every direct-damage action has exact numeric Power:
- Authority Lance — **190**
- Judgment Pulse — **140 AoE**
- Seal Reprisal — **100**
- Major Ruling — **210 AoE**
- Recorded Analogue — **150 single / 105 AoE**
- Warden Crush — **245**
- Challenged Verdict — **230**
- Command Collapse — **165 AoE**

Non-damaging:
- Command Seal — **Power N/A**
- Ring alignment / defensive alignment — **Power N/A**

> **WORKING PASS / POWER COMPLETE**
