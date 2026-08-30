# Diyse — Universal Harmful Status Effects
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135 and newer explicit turn-flow corrections.  
**Migration rule:** current explicit user corrections and current organized domain canon outrank stale/open wording inherited by v85.


## Universal set

Exactly:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

These are the universal harmful statuses.

Regen is beneficial and is **not** a harmful status.

Global round/turn timing is owned by `TURN_AND_ROUND_RULES.md`. The status-specific timing below overrides only where explicitly stated.

## Status application resolver

Default authored application bands:
- **10%** minor
- **20%** standard
- **35%** dedicated
- **50%** premium/setup-dependent
- above 50% is uncommon and requires explicit justification

General Status Resistance:
- **0** — Normal
- **5** — Resistant
- **10** — Highly Resistant
- **15** — Exceptional
- immunity — explicitly authored only

For the compatible ordinary application resolver:

> **FinalStatusChance = BaseChance + AffinityModifier + legal specialist bonuses - StatusResistance**

Ordinary chance is clamped to **5%–95%**, except explicit immunity, guarantee, or script.

The old percentage-based `Normal 100% / Resistant 80% / Strongly Resistant 60%` table must **not** be restored as a second generic Status Resistance resolver. Identity-specific immunities and encounter-specific rules remain separate.

## Burn

Duration:
# **4 rounds**

Ordinary damage:
# **6% target Max HP at the end of each affected round**

While Burn is active:
- **Defense −10%**
- **Spirit −10%**

Timing:
- Burn becomes active immediately when applied, including its Defense/Spirit penalties;
- if Burn is applied during normal turn resolution and remains active through that round's end, the application round is its first affected round and produces its first end-of-round Burn proc;
- ordinary 4-round Burn therefore produces at most **4 end-of-round Burn procs** per uninterrupted application, for **24% Max HP total** ordinary Burn damage;
- reapplication refreshes the remaining duration under the same round-timing rule;
- the Defense/Spirit penalties end when Burn ends or is legally cleared.

Rules:
- Burn's Defense and Spirit penalties do not stack with themselves; reapplication refreshes Burn instead;
- Burn damage does not Crit;
- Burn damage ignores Defense/Spirit;
- Burn damage can KO unless a specific encounter says otherwise.

High-rank damage conversion:
- Regional Hunt — **75%** ordinary Burn damage = **4.5% Max HP per affected round**, up to **18% Max HP total** across 4 uninterrupted rounds;
- Major Hunt / mandatory boss — **50%** ordinary Burn damage = **3% Max HP per affected round**, up to **12% Max HP total** across 4 uninterrupted rounds;
- the high-rank conversion reduces Burn's Max-HP damage only. Burn's **Defense −10% / Spirit −10%** rider remains in force while Burn is active unless an encounter explicitly overrides it.

## Freeze

Base behavior:
- target cannot act;
- first **2 affected rounds** are guaranteed;
- **80%** persistence check into affected round 3;
- separate **80%** persistence check into affected round 4;
- maximum **4 affected rounds**;
- first successful direct Physical hit removes Freeze **after that hit**;
- cannot refresh while active.

For Freeze, an **affected round** is a round in which Freeze is active when the target's normal turn arrives.

Therefore:
- if Freeze is applied before the target's turn in the current round, that current turn is blocked and counts as the first affected round;
- if Freeze is applied after the target already acted, the completed turn is not retroactively lost and the first affected round is the next round in which Freeze is still active when the target's turn arrives;
- persistence checks occur before the target's normal action on the relevant later affected round; if Freeze fails to persist, it clears and the target may act normally on that turn unless another effect prevents it.

High-rank conversion:
- Regional Hunt — maximum **2 affected rounds**
- Major Hunt / mandatory boss — maximum **1 affected round**

## Stun

Base behavior:
- lasts **3 affected turns**;
- **40%** action-loss chance on each affected turn;
- cannot refresh while active.

An affected turn is a normal turn opportunity that begins while Stun is active.

Therefore:
- Stun applied before the target's current turn can affect that turn;
- Stun applied after the target has already acted cannot retroactively affect or count that completed turn;
- whether the action-loss roll succeeds or fails, that turn opportunity counts as one of the 3 affected turns;
- after the third affected turn is processed, the ordinary Stun duration is complete unless it cleared earlier under an explicit owning rule.

High-rank conversion:
- Regional Hunt — **25%** action-loss chance
- Major Hunt / mandatory boss — **20%** action-loss chance

## Staggered

Duration:
# **3 rounds**

Effects:
- **Attack −20%**
- **Magic −20%**

Timing:
- Staggered becomes active immediately when applied;
- its Attack and Magic penalties apply to later eligible actions in the same round;
- under the standard round-duration rule, the application round counts as round 1.

Rules:
- reapplication refreshes duration;
- never stacks;
- this is a normal harmful status;
- it is **not** the retired Break/Stagger meter.

## Bleed

Initial ordinary magnitude:
# **3% Max HP per qualifying Bleed proc**

Escalation:
- Bleed tracks how long the **same uncleared Bleed instance** has remained on the affected unit.
- After the affected unit **completes its third turn while Bleed is still active**, Bleed increases by **1 percentage point**.
- From that point onward, its ordinary magnitude is **4% Max HP per qualifying proc** until Bleed is removed.
- The Bleed-on-action proc associated with that third affected turn still uses the pre-escalation **3%** magnitude; escalation becomes active after that turn resolves.
- Reapplying Bleed while it is already active does **not** reset the three-turn age or remove escalation. If Bleed is fully removed and later applied again, the new Bleed starts at 3% with a fresh turn count.

Current Audit122 cadence:
- one round-based Bleed proc resolves during **end-of-round processing** while Bleed remains active;
- Bleed deals damage **again after each actual action taken by the affected unit**, before the next normal combatant's turn begins;
- if an effect grants more than one actual action, each qualifying action follows the current Bleed-on-action rule unless explicitly overridden.

Action-proc ordering:
1. the affected unit's selected action and its complete immediate action package resolve;
2. if the same Bleed is still active, resolve the Bleed-on-action proc at the current magnitude;
3. complete that unit's turn and advance Bleed's uncleared-turn age;
4. if that was the third completed turn with the same Bleed still active, escalation to 4% begins **after** that turn's action proc.

A lost/no-action turn can advance Bleed's uncleared-turn age because the turn opportunity completed, but it does **not** create a Bleed-on-action proc.

If the action itself fully restores HP or otherwise legally removes Bleed before the post-action Bleed check, there is no action-triggered Bleed proc because Bleed is no longer active.

If Bleed is applied during normal turn resolution and remains active at end-of-round, it qualifies for that round's end-of-round Bleed proc.

The old one-proc-per-round restriction is retired.

Bleed:
- is indirect damage;
- cannot Crit;
- ignores Defense/Spirit;
- may KO unless an encounter explicitly overrides it.

Bleed clears only when:
1. the affected unit reaches **full HP**;
2. an eligible harmful-status clear removes it;
3. an eligible item removes it.

Partial healing does not clear Bleed.
Ordinary Regen does not clear Bleed unless it restores the target to full HP or explicitly includes a valid status clear.

High-rank damage conversion:
- Regional Hunt — **75%** ordinary Bleed damage = **2.25% Max HP per proc initially**, escalating to **3%** after three affected turns uncleared.
- Major Hunt / mandatory boss — **50%** ordinary Bleed damage = **1.5% Max HP per proc initially**, escalating to **2%** after three affected turns uncleared.

## Boss / Hunt principle

High-rank enemies should resist status play more strongly than ordinary enemies without becoming blanket-immune by default.

Explicit thematic immunity remains legal.
True nonliving bodies may be explicitly Bleed Immune.

Duration/magnitude conversions and raw Status Resistance are separate layers.
