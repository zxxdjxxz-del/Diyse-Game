# Crest-Exhausted Warden

**Character Quest:** Cyanis — *The Weight of the Crest*  
**Unlock:** after Chapter 7  
**Architecture:** one continuous HP bar / no adds / no transformation  
**Status:** **EXACT CURRENT KIT AUTHORED v90 / POWER COMPLETE / MANDATORY-vs-COMPLETIONIST PAPER VALIDATED**

## Balance reference
- immediate mandatory-route access: approximately **Lv32**;
- high optional/completionist access at the same window: approximately **Lv37**;
- intended boss body: **Lv35**.

## Raw body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 35 | **6,800** | **132** | **128** | **98** | **98** | 35 | 0 | 10 |

## Actions
### Crest Hammer
- one party member
- Physical / Neutral
- **260 Power**
- Base Hit100
- no fixed harmful-status rider
- weight **30**

### Relay Pulse
- one party member
- Magical / Colorless
- **240 Power**
- Base Hit100
- weight **25**

### Evacuation Sweep
- all conscious party members
- Magical / Colorless
- **180 Power per target**
- Base Hit95
- 2-round repetition lock
- weight **15**

### Load Redistribution
> **Power: N/A — no direct damage**

Effect:
> **+15 Total Defense through the end of the following round**

- 2-round repetition lock
- weight **10**

### Assign Primary Load
> **Power: N/A — no direct damage**

Rules:
- choose one conscious party member and display **Primary Load** visibly;
- the designation lasts until the Warden's next selected action;
- Primary Load is **not Taunt**;
- it does not force the player character to act;
- it does not prevent allies from Guarding, healing, applying Barrier, or otherwise protecting the target;
- while Primary Load exists, the Warden's next selected action is forced to **Load-Bearing Test** if the Warden remains able to act;
- cannot be selected while Primary Load already exists;
- weight **20**.

### Load-Bearing Test
Only legal after Assign Primary Load.

- Primary Load target
- Hybrid / Neutral
- **50% ATK / 50% MAG**
- **300 Power**
- Base Hit100
- **25% Defense penetration** on the physical share
- **25% Spirit penetration** on the magical share

If the target is **Guarding** or has an active **Barrier** at resolution:
> **Load-Bearing Test final direct damage −30%**

After resolution:
- clear Primary Load;
- no extra action.

## Crest Exhaustion
At first reaching **40% HP**:
> **Crest Exhaustion** activates for the remainder of battle.

Effects:
- Attack +10%
- Magic +10%
- Speed +10
- Total Defense −10

The state change:
- is same-bar;
- grants no free action;
- does not refill HP/MP;
- does not refresh Prime availability.

## Firewall
Primary Load:
- is a visible boss-specific target state;
- is not a universal resource;
- does not delete commands;
- does not read hidden player intent;
- does not create free interception;
- does not require generic Break;
- does not make any character permanently expendable.

## v90 balance certification
Against the deliberately fragile no-equipment Green Arcanist reference at Lv32:
- Crest Hammer is approximately **18.8% Max HP**;
- Relay Pulse is approximately **14.7%**;
- unmitigated Load-Bearing Test is approximately **20.1%** before its penetration adjustment;
- the telegraphed defensive answer reduces the Test by **30% final direct damage**.

At Lv37 the same baseline drops materially. The **6,800 HP** body is intended to produce approximately **5–6 serious rounds at immediate mandatory access** and **4–5 for a strong completionist**, with Load Redistribution and Primary Load creating action-tax/defense decisions rather than a second health bar.

**Verdict:** **PASS / EXACT SHEET CLOSED v90**
