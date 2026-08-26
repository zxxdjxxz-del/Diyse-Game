# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline under **Diyse Clean Active Complete Master Canon v2.01 / Audit116**.

Controlling authorities:

- Card / Prime economy + command packages: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- Global combat / Ruin / status / class Abilities: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- Compatible Prime acquisition/progression/timing: `docs/canon/AUDIT114_PRIME_COMBAT_ELEMENT_STATUS_AND_BASE_CLASS_NORMALIZATION_LOCK.md`

Older combat proofs remain useful only where compatible with these authorities.

---

## Core round structure

Diyse uses traditional discrete rounds.

Accepted compatible resolver behavior:

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. Each enemy locks one legal action from the legitimate beginning-of-round state without inspecting unconfirmed player commands.
3. The player selects one action for every conscious active party member before the round is confirmed.
4. Resolve Item actions first, ordered by current effective Speed.
5. Resolve Defend actions second, ordered by current effective Speed.
6. Resolve all remaining party and enemy actions from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members use player-selected order.
9. Tied enemies/entities use stable deterministic order.
10. Resolve complete action/reaction/state-change packages, then end-of-round processing according to the controlling combat specification.

Speed determines order only. Speed never grants extra ordinary actions.

---

## Automatic hostile retargeting

If a queued player hostile action targets an enemy defeated before that action resolves in the same round:

- retarget to the next living enemy in encounter-slot order after the original target;
- if no later slot is living, wrap to the first living enemy;
- if no enemies remain living, there is no legal target and battle resolution proceeds normally;
- this applies to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly says otherwise;
- retargeting changes only the target, not the action, cost, priority, Speed, or actor.

---

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands without explicit later change control.

Maximum active permanent party size remains **4**. Reserve members are inert under the normal combat rules.

---

## Ability economy

- MP is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- Learned Abilities remain weapon-independent once learned unless an individual later authority explicitly says otherwise.
- Equipment does not choose an Ability's Physical/Magical/Hybrid formula.
- Full current class Ability packages are controlled by Audit115.

---

# Standard Cards — Audit116

Current Card collection architecture remains **24 Standard Cards + 12 Prime Cards = 36 total Cards**.

There are exactly **24 Standard Cards**, distributed unevenly by Face:

- Might — **5**
- Elements — **5**
- Grace — **4**
- Acuity — **4**
- Change — **3**
- Ruin — **3**

Audit106's four-per-Face matrix is superseded.

Each permanent character may equip a maximum of:

> **3 Standard Cards**

Standard Card rules:

- consume the user's normal selected action;
- are reusable after acquisition;
- cost the user's MP;
- currently span **12–36 MP**;
- require enough MP to pay the listed cost;
- are Card commands, not Abilities;
- Ability-only MP reductions do not apply unless an effect explicitly includes Cards/all MP costs;
- no deck/hand/draw/discard, charge, duplicate, rank, Essence, or refresh-counter system exists;
- Standard Cards do not summon independent beings.

Current Standard Card lineups:

### Might
- Iron Testament
- Sunder the Gate
- Relentless Flurry
- March of Blades
- Sanguine Alloy

### Elements
- Cinder Judgment
- Winterglass Spear
- Thunder Chain
- Confluence Sigil
- Worldsplitter

### Grace
- Restoration
- Merciful Reprisal
- Wellspring
- Dawn Recall

### Acuity
- Faultline Sight
- Measured Response
- Predicted Impact
- Decisive Interval

### Change
- Burden Shift
- Reversal Engine
- Split Moment

### Ruin Face
- Calamity Lance
- Devouring Singularity
- Zero Hour

Current exact command formulas/effects are in Audit116.

Important implementation supersessions:

- Chosen Course → **Measured Response**.
- Glassform Rupture → **Burden Shift**.
- Spatial Guillotine → **Split Moment**.
- Sanguine Alloy is **Might**.
- Worldsplitter is **Elements / Earth**.
- `unlimited-use Standard Card` means no charge limit, **not** zero MP.

### Split Moment firewall

Split Moment grants at most **two independently selected actions** on the target's next normal turn, paying each action's full normal costs.

- Extra-action effects do not stack to three or more selected actions.
- Split Moment cannot grant extra Prime rounds/commands or bypass Prime use restrictions.
- If Prime Invocation / party replacement begins in one Split Moment slot, any unresolved ordinary second slot is forfeited.
- Audit115 Bleed remains capped at **one proc per round**, even if two actions are successfully taken.

---

# Prime Card / manifestation framework — Audit116 + compatible Audit114

There are exactly **12 Prime Cards**:

- six Story Primes;
- six Major-Hunt Primes.

Current Story Primes:

- Might — **Last Sentinel**
- Acuity — **Last Cartographer**
- Elements — **Last Convergence**
- Change — **Last Scribe**
- Grace — **Last Sanctuary**
- Ruin — **Last Erasure**

Current Major-Hunt Primes:

- Grace — **Dawn Shepherd**
- Might — **Oathbound Colossus**
- Change — **Living Revision**
- Elements — **Prismatic Leviathan**
- Acuity — **Parallax Host**
- Ruin — **Starfall Engine**

`Last Measure` and `Sheltering Host` are superseded.

## Prime states

Prime progression is exactly:

> **Recovered → Awakened**

There is no Concordant state.

Recovered Story Prime:
- one strong manifestation action resolves in the current ordinary round;
- the manifestation then ends.

Awakened Prime:
- final state;
- replaces/suspends the active party;
- exactly **3 directly controlled Prime rounds**;
- one selected Prime command per Prime round.

Removed:

- Prime XP/levels;
- duplicates as progression;
- Prime upgrade materials;
- Concordant harmonization;
- third-stage progression.

Legacy commands formerly labeled Concordant remain in the Awakened kit where explicitly retained.

## Prime use / form boundaries

- Prime activation uses the Card action.
- After the Prime ends, that Prime identity has a **3-full-normal-round cooldown**.
- Each Prime identity may be used once per battle per genuine fresh-HP boss form.
- A genuine fresh-HP boss form refreshes that identity's use/cooldown state.
- Story Primes are acquired Recovered and later Awaken through mandatory story milestones.
- Major-Hunt Primes are obtained already Awakened.
- Frozen party state does not tick or become targetable during active Awakened Prime rounds unless an authored return/handoff effect explicitly resolves at dismissal.

## Prime Invocation MP

Current canonical Invocation costs:

- Recovered Story Prime — **60 MP**
- Awakened Story Prime — **75 MP**
- Awakened Major-Hunt Prime — **75 MP**

Once manifested:

> **Prime commands cost 0 additional MP**

Prime Invocation must remain a **severe MP commitment**. Old 0-MP Invocation and intermediate 40/48-MP rules are superseded.

The exact numbers may only move through an explicit later global MP balance pass; such a pass must preserve the severe-cost hierarchy unless separately approved.

## Prime command packages

Exact current Story-Prime and Major-Hunt-Prime command tables are controlled by Audit116.

Important Major-Hunt implementation notes:

- none of the current six requires a standalone passive;
- Living Revision Continuance has no healing;
- Prismatic Leviathan has no Adaptive Scales passive, no heal command, and no Colorless offense;
- Prismatic Mantle is the current defensive-rider attack;
- Prismatic Deluge replaces Sixfold Deluge;
- overlap between related Prime commands is explicitly acceptable and is not a reason to rewrite them;
- Prismatic Deluge's exact damage Power remains open for the final numerical pass.

---

# Damage type, element, and Ruin scope

Every damaging **character Ability** is authored as Physical / Magical / Hybrid.

Exactly four standard elements:

- Fire
- Ice
- Lightning
- Earth

Linked status pairs:

- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

An elemental hit does not automatically inflict its linked status; the action must explicitly carry the rider.

Ruin is a special affinity/school, not a fifth standard element.

Audit115 character-Ability Ruin formula:

> **Hybrid / Ruin — 75% Attack / 25% Magic**

This 75/25 formula applies to **character Abilities** dealing Ruin.

Prime commands are a separate command class. Last Erasure and Starfall Engine use the explicit Prime-authored Physical/Magical/Hybrid Ruin formulas listed in Audit116. Do not silently normalize Prime commands to the character-Ability 75/25 formula.

Ruin-Face Standard Cards Calamity Lance, Devouring Singularity, and Zero Hour are explicitly **Magical / Colorless**, not Ruin-affinity attacks.

---

# Universal harmful statuses — Audit115

Exactly:

- Burn
- Freeze
- Stun
- Staggered
- Bleed

## Burn
- 3 rounds.
- Ordinary damage: 3% target Max HP at end of each affected round.
- Reapplication refreshes duration.
- No crit; ignores Defense/Spirit; can KO.

## Freeze
- Target cannot act.
- First 2 rounds guaranteed.
- 80% persistence check into round 3 and separately into round 4.
- Maximum 4 rounds.
- First successful direct Physical hit removes Freeze after the hit.
- Cannot refresh while active.

## Stun
- 3 affected turns.
- 40% action-loss chance on each affected turn.
- Cannot refresh while active.

## Staggered
- 3 rounds.
- Speed −20%.
- Base Hit / Accuracy −20%.
- Evasion −20%.
- Reapplication refreshes; does not stack.

## Bleed
- 2% Max HP when the affected unit successfully acts.
- Maximum one Bleed proc per round.
- Lost actions do not proc Bleed.
- **Any successful HP heal restoring at least 1 HP removes Bleed after the heal.**
- Regen restoring at least 1 HP removes Bleed.
- No stack; no crit; ignores Defense/Spirit; can KO.

## Lifecycle

- KO clears Burn / Freeze / Stun / Staggered / Bleed / Regen.
- Battle end clears ordinary temporary combat statuses/effects.
- A genuine fresh-HP boss form clears ordinary temporary statuses unless explicit carryover is authored.

---

# Status application / resistance

Default authored chance bands:

- 10% minor
- 20% standard
- 35% dedicated
- 50% premium/setup-dependent
- above 50% uncommon and explicitly justified

Standard element/status affinity modifier:

- Weak: +10 percentage points
- Neutral: 0
- Resist: −10 percentage points
- Immune: linked application blocked

Vaelira's qualifying +5 percentage-point specialist bonus applies to **her character Abilities**, not automatically to Cards or Primes.

Status Resistance:

- Normal 0
- Resistant 5
- Highly Resistant 10
- Exceptional 15
- Immune explicit

Ordinary application:

> Base + affinity modifier + Vaelira bonus − Status Resistance

Clamp ordinary legal chances to 5%–95% except explicit immunity, guarantee, or script.

High-rank effect conversion:

- Ordinary: full.
- Elite: full by default absent thematic exception.
- Regional Hunt: Freeze max 2 rounds; Stun 25% action-loss; Staggered full where legal; Burn/Bleed 75% ordinary damage.
- Major Hunt / mandatory boss: Freeze max 1 round; Stun 20% action-loss; Staggered full where legal; Burn/Bleed 50% ordinary damage.

Effect conversion is separate from application chance.

---

# Removed systems / non-status states

Do not recreate under renamed equivalents:

- Card Seals
- global Rune-effect state/system
- Imprints
- Break/Stagger meter

The following are not universal harmful statuses:

- ordinary stat Up/Down effects;
- Fields;
- Guard / Barrier;
- Hunter's Measure;
- Prepared effects;
- class-internal setup states;
- protected/scripted encounter states;
- Audit116 tactical states such as Decisive Opening, Reversal, Perfect Route, Advancing Dawn, Held Sanctuary, Oathbound Momentum.

Ordinary harmful-status remedies do not remove these unless an effect explicitly says otherwise.

---

# Basic Attack / weapon independence

- Attack comes from the currently equipped Weapon.
- Universal Attack does not inflict a harmful status unless current equipment explicitly grants that rider.
- Learned Abilities remain legal with any otherwise-legal equipment loadout unless an individual Ability explicitly says otherwise.
- Equipment does not change an Ability's fixed Physical/Magical/Hybrid formula.
- Presentation may manifest/project a traditional weapon visual when the current equipped weapon differs.

---

# Determinism and regression expectations

Pure combat resolution must remain testable without animation timing.

Regression coverage should include:

- Item priority;
- Defend priority;
- Speed order/ties;
- enemy action locking;
- one ordinary selected action per legal unit except explicit Split Moment;
- Split Moment two-action cap and Prime firewall;
- Bleed maximum one proc per round, including Split Moment turns;
- automatic hostile retargeting;
- Standard Card 3-slot limit and MP payment;
- current 5/5/4/4/3/3 Standard-Card distribution;
- Prime 60/75 Invocation payment;
- Recovered one-action Prime behavior;
- Awakened three-round direct control;
- Prime 3-normal-round cooldown;
- genuine fresh-HP boss-form refresh;
- frozen off-field party behavior during Prime replacement;
- current Audit115 status timing/application/lifecycle;
- Audit115 character-Ability 75/25 Ruin formula;
- Audit116 Prime-specific Ruin formula exception/scope.

Tests encoding superseded facts such as Resource Face, four Standard Cards per Face, zero-MP Standard Cards, zero-MP Prime Invocation, Concordant, Water/Wind standard elements, Poison, Card Seals, Imprints, global Break/Stagger, or universal 75/25 Ruin formulas for Prime commands must be deliberately updated.

Presentation and animation consume resolver/state results; they do not define combat legality.
