# Warden of the Nameless / Revision Arbiter

**Chapter:** 7 — The Prison of Names  
**Role:** mandatory Chapter-7 climax boss  
**Status:** **VALIDATED v83 / POWER COMPLETE**

## Identity / architecture

This is:
> **one enemy identity / one continuous HP bar**

Current state structure:
1. **Warden of the Nameless — Closed Record**
2. **Revision Arbiter — Adjudication**
3. **Open Revision** at 40% HP

These are same-body state changes.

There is:
- no fresh HP body;
- no damage spill/reset issue;
- no free transition attack;
- no intermediate reward;
- no Prime availability refresh.

The encounter preserves the story requirement that:
> multiple party members prove/assert continuity of self before direct combat fully opens.

No dialogue choices are introduced.

No new permanent combat command is introduced.

---

# ROUTE-LEVEL REFERENCE

Chapter 6 ends:
> **69,300 mandatory EXP = Lv27**

Before the Warden, Chapter 7 has already awarded:
- all **14,120 ordinary mandatory EXP**;
- Chainworks Behemoth — 3,200;
- Ashford / Chainworks control dismantled — 1,200;
- Veycross transit controls — 2,000;
- Prison records authenticated — 2,200.

Mandatory pre-Warden total:
> **92,020 EXP**

That is:
> **Lv30**, 1,780 EXP short of Lv31.

Fixed optional progression legally available by this late Chapter-7 point:
- The Marks We Leave — 500
- Regional Hunts #1–#7 — 23,700
- Major Hunt #1 — Ashen Whitehorn — 4,500

Total fixed optional advantage:
> **28,700 EXP**

Completionist pre-Warden total:
> **120,720 EXP**

That is:
> **Lv34**, 1,980 EXP short of Lv35.

Optional Elites / incidental optional combat can push the high side toward:
> **~Lv35**

Balance references:
- mandatory — **Lv30**
- completionist fixed-content — **Lv34**
- high-side — **~Lv35**

After the Warden's 5,500 EXP:
- mandatory route becomes 97,520 EXP = Lv31;
- the 3,080 EXP Volition handoff then lands exactly at 100,600 EXP = Lv32.

This preserves the current Chapter-7 level spine.

---

# CURRENT RAW LINE

| Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 34 | **7,600** | **124** | **138** | **86** | **92** | **42** | 5 | 10 |

Inherited baseline:
> Lv34 / 8,913 HP / 112 ATK / 120 MAG / 84 DEF / 89 Spirit / 40 SPD

Working change:
- HP **8,913 → 7,600**
- ATK **112 → 124**
- MAG **120 → 138**
- DEF **84 → 86**
- Spirit **89 → 92**
- SPD **40 → 42**
- EVA5 / SR10 retained

Rationale:
- Closed Record and Open Revision already consume party action value;
- the encounter should pressure the mandatory Lv30 route rather than merely outlast it;
- lower HP plus stronger authored attacks keeps the climax active;
- completionist Lv34 progression remains meaningfully rewarded.

---

# CLOSED RECORD — OPENING ASSERTION GATE

At battle start:
> **Closed Record has 3 Assertion Layers**

While at least one layer remains:
> Warden takes **80% less direct HP damage**.

This is an authored boss-state reduction.

It is **not Barrier**.

## Removing Assertion Layers

The first completed ordinary action by each distinct conscious active party member removes one Assertion Layer after that action resolves.

Eligible ordinary actions:
- Attack
- Ability
- Card
- Item
- Defend

Rules:
- a character can remove only one opening layer;
- repeated actions by the same character do not remove additional layers;
- the action itself resolves normally first;
- direct damage from that action still suffers the current Closed Record reduction if a layer remained at the time damage resolved;
- once the third distinct character completes an action, Closed Record ends immediately.

The Warden does not inspect unconfirmed commands.

No special sixth command is added.

This makes the party demonstrate continuity through its existing combat identities rather than through a dialogue-choice prompt.

## Opening pressure

While Closed Record remains active, Warden action preference favors:
- Name Redaction
- Registry Pulse

and avoids its strongest late-state attacks.

---

# STATE A — WARDEN / ADJUDICATION

## Name Redaction
- one party member
- Magical / Colorless
- **220 Power**
- Base Hit **100**
- no harmful-status rider
- 1-round repetition lock

## Registry Pulse
- all conscious party members
- Magical / Colorless
- **145 Power per target**
- Base Hit **100**
- no harmful-status rider
- 2-round repetition lock

## Severing Writ
- one party member
- Physical / Neutral
- **205 Power**
- Base Hit **100**
- **20% Staggered**
- 1-round repetition lock

## Revision Lance
- one party member
- Magical / Colorless
- **245 Power**
- Base Hit **95**
- **20% Stun**
- 2-round repetition lock

## Reconciliation Order
> **Power: N/A — no direct damage**

Target:
> one conscious party member

Effect:
> Attack −15% and Magic −15% for 2 rounds.

This is an ordinary temporary stat Down effect, not a harmful-status addition.

2-round repetition lock.

---

# REVISION CLAIM — ACTION-TAX RECONCILIATION

Beginning after Closed Record ends, the Warden may issue one Revision Claim at a time.

### Revision Claim
> **Power: N/A — no direct damage**

Target:
> one conscious party member

The Claim records that character's most recently completed command category:
- Attack
- Ability
- Card
- Item
- Defend

Duration:
> until the target completes **one different command category**, maximum 2 rounds.

While unresolved:
> that character deals **25% less final direct damage to the Warden**.

The Claim:
- never disables a command;
- never increases MP cost;
- never skips a turn;
- never reads an unconfirmed command;
- clears immediately after the target completes a different category.

Only one Revision Claim may exist at once.

Revision Claim has a 2-round repetition lock.

This is the encounter's continuing action-tax architecture:
> the player may accept reduced output or vary that character's ordinary command usage.

It does not duplicate the First Command Warden's reprisal mechanic because:
- repeating the command causes no counterattack;
- no damage is triggered by the Claim;
- the tax is a temporary damage-output reduction only.

---

# OPEN REVISION — 40% HP SAME-BAR STATE

At:
> **40% HP**

the Warden enters:
> **Open Revision**

Transition:
- no HP refill;
- no free attack;
- no Prime refresh;
- any active Revision Claim clears;
- Reconciliation Order becomes unavailable.

## Open Revision Layers

On entry:
> gain **2 Open Revision Layers**

While at least one remains:
> Warden takes **40% less direct HP damage**.

Each layer is removed by:
> the first completed ordinary action from a distinct active party member after Open Revision begins.

A character can remove only one Open Revision Layer.

Actions resolve normally before layer removal.

Again:
> no new command is created.

After both layers are gone:
> no further global direct-damage reduction remains.

This is a short reconciliation tax, not a second phase bar.

---

# OPEN REVISION ACTION KIT

## Open Revision Lance
- one party member
- Magical / Colorless
- **280 Power**
- Base Hit **95**
- **20% Stun**
- 1-round repetition lock

## Identity Severance
- one party member
- Hybrid / Neutral
- **50% ATK / 50% MAG**
- **270 Power**
- Base Hit **100**
- **20% Staggered**
- 1-round repetition lock

## Rewrite Wave
- all conscious party members
- Magical / Colorless
- **180 Power per target**
- Base Hit **95**
- no harmful-status rider
- 2-round repetition lock

## Recursive Judgment
- one party member
- Magical / Colorless
- **2 × 140 Power = 280 total**
- Base Hit **100 per hit**
- no harmful-status rider
- 2-round repetition lock

## Final Reconciliation
> **Power: N/A — no direct damage**

Target:
> one conscious party member

Effect:
> Defense −15% and Spirit −15% for 2 rounds.

2-round repetition lock.

---

# PRIME INTERACTION

Any legally acquired/equipped Prime at this story point follows normal Prime rules.

Because:
> Warden → Revision Arbiter → Open Revision

is one continuous HP body:
> **no state change refreshes Prime availability**.

Assertion/Open Revision Layers do not refresh Primes.

---

# DURATION CERTIFICATION

The boss is intentionally the Chapter-7 climax and should run longer than Chainworks Behemoth.

## Mandatory Lv30
Expected:
- aggressive / clean command variation: **~11–12 rounds**
- normal: **~12–13 rounds**
- support/recovery-heavy: **~13–14 rounds**

## Completionist Lv34
Expected:
> **~9–10 rounds**

## High-side ~Lv35
Expected:
> **~8–9 rounds**

The completionist route is roughly 2–3 rounds faster despite the same fixed boss.

---

# POWER-COMPLETENESS VERDICT

Adjudication direct damage:
- Name Redaction — **220**
- Registry Pulse — **145 per target**
- Severing Writ — **205**
- Revision Lance — **245**

Open Revision direct damage:
- Open Revision Lance — **280**
- Identity Severance — **270**
- Rewrite Wave — **180 per target**
- Recursive Judgment — **2 × 140**

Non-damaging:
- Closed Record — **Power N/A**
- Reconciliation Order — **Power N/A**
- Revision Claim — **Power N/A**
- Open Revision Layers — **Power N/A**
- Final Reconciliation — **Power N/A**

> **WORKING PASS / POWER COMPLETE**

## Reward continuity

Warden of the Nameless / Revision Arbiter:
> **5,500 EXP / 190 CEXP**

Current Standard Card reward:
> **Split Moment — Change**

Sixfold Volition remains a later separate story handoff after the Prison/Change resolution.
