# Elemental Forecast Construct

**Character Quest:** Vaelira — *The Sky No One Chose*  
**Unlock:** after Sixfold Volition / Chapter 7 clear  
**Architecture:** one continuous HP bar / no adds / no transformation  
**Status:** **EXACT CURRENT KIT AUTHORED v90 / POWER COMPLETE / MANDATORY-vs-COMPLETIONIST PAPER VALIDATED**

## Balance reference
- immediate mandatory-route access: approximately **Lv32**;
- high optional/completionist access at the same window: approximately **Lv37**;
- intended boss body: **Lv35**.

This is a Character Quest boss, not a Regional or Major Hunt. It is intended to be a meaningful 4-active-member systems fight at first access without being tuned above the post-Chapter-7 Hunt ladder.

## Raw body
| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 35 | **6,200** | 74 | **142** | 82 | **90** | **44** | 5 | 10 |

## Forecast state engine
The current Forecast is always visible **before player command selection**.

Start:
> **Storm**

Each Forecast remains active for exactly **2 Construct selected actions**, then advances before the next player command window:
> **Storm → Blizzard → Heatwave → Storm**

The state advance:
- is automatic;
- consumes no action;
- grants no free attack;
- does not restore HP/MP;
- does not refresh Prime availability or once-per-battle flags;
- does not read or react to unconfirmed player commands.

The Construct never uses Wind or Water damage.

## State-specific action tables
Within each state, use the listed weights after eligibility/repetition locks are checked.

### Storm
#### Storm Forecast
- one party member
- Magical / Lightning
- **260 Power**
- Base Hit100
- **25% Stun**
- weight **55**

#### Stormfront
- all conscious party members
- Magical / Lightning
- **185 Power per target**
- Base Hit95
- **10% Stun per target**
- 2-round repetition lock
- weight **30**

### Blizzard
#### Blizzard Forecast
- one party member
- Magical / Ice
- **250 Power**
- Base Hit100
- **25% Freeze**
- weight **55**

#### Whiteout Front
- all conscious party members
- Magical / Ice
- **180 Power per target**
- Base Hit95
- **10% Freeze per target**
- 2-round repetition lock
- weight **30**

### Heatwave
#### Heatwave Forecast
- one party member
- Magical / Fire
- **270 Power**
- Base Hit100
- **25% Burn**
- weight **55**

#### Thermal Front
- all conscious party members
- Magical / Fire
- **190 Power per target**
- Base Hit95
- **15% Burn per target**
- 2-round repetition lock
- weight **30**

### Stabilize Forecast
Available in all three states.

> **Power: N/A — no direct damage**

Effect:
> **+10 Total Defense through the end of the following round**

- 2-round repetition lock
- weight **15**

## Low-HP pressure
Below **35% HP**:
- state-specific single-target weight **55 → 45**;
- state-specific AoE weight **30 → 40**;
- Stabilize Forecast remains 15.

No extra action is gained.

## Status / element firewall
- Storm = Lightning / Stun.
- Blizzard = Ice / Freeze.
- Heatwave = Fire / Burn.
- Earth is intentionally not part of this three-state forecast identity.
- No Composite Reaction system.
- No Wind/Water/Rain damage state.
- Maximum one status check per target per selected action.

## v90 balance certification
Against the deliberately fragile no-equipment Green Arcanist reference:
- Lv32: 260-Power Storm hit is approximately **18.4% Max HP**; 185-Power Stormfront is approximately **13.1% per target**;
- Lv37: those checks fall to approximately **14.9%** and **10.6%**.

6,200 HP places the boss above a Chapter-7 optional Elite but far below the post-Chapter-7 Major-Hunt body. Expected serious-party duration is approximately **5–6 rounds at immediate mandatory access** and **4–5 rounds for a strong completionist**, before affinity, Prime, Card, critical, and status variance.

**Verdict:** **PASS / EXACT SHEET CLOSED v90**
