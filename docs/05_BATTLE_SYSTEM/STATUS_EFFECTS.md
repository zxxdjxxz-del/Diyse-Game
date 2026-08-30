# Diyse — Universal Harmful Status Effects
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current domain authority checked:** repository `docs/COMBAT_RULES.md`, current through **v2.20 / Audit135**, plus compatible Audit115, Audit120, Audit122, Audit135.  
**Migration rule:** current master canon outranks stale/open wording inherited by v85.


## Universal set

Exactly:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

These are the universal harmful statuses.

Regen is beneficial and is **not** a harmful status.

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
# **3 rounds**

Ordinary damage:
# **3% target Max HP at the end of each affected round**

Rules:
- reapplication refreshes duration;
- does not Crit;
- ignores Defense/Spirit;
- can KO unless a specific encounter says otherwise.

High-rank damage conversion:
- Regional Hunt — **75%** ordinary Burn damage
- Major Hunt / mandatory boss — **50%** ordinary Burn damage

## Freeze

Base behavior:
- target cannot act;
- first **2 rounds** are guaranteed;
- **80%** persistence check into round 3;
- separate **80%** persistence check into round 4;
- maximum **4 rounds**;
- first successful direct Physical hit removes Freeze **after that hit**;
- cannot refresh while active.

High-rank conversion:
- Regional Hunt — maximum **2 rounds**
- Major Hunt / mandatory boss — maximum **1 round**

## Stun

Base behavior:
- lasts **3 affected turns**;
- **40%** action-loss chance on each affected turn;
- cannot refresh while active.

High-rank conversion:
- Regional Hunt — **25%** action-loss chance
- Major Hunt / mandatory boss — **20%** action-loss chance

## Staggered

Duration:
# **3 rounds**

Effects:
- **Speed −20%**
- **Base Hit −20%**
- **Evasion −20%**

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
- deals its Bleed damage **each round**;
- deals it **again when the affected character acts**;
- if an effect grants more than one actual action, each qualifying action follows the current Bleed-on-action rule unless explicitly overridden.

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
