# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline under **Diyse Clean Active Complete Master Canon v1.99 / Audit114**. Older combat proofs and subordinate files remain useful only where compatible with Audit114 and the current active canon.

Controlling combat-system authority:
`docs/canon/AUDIT114_PRIME_COMBAT_ELEMENT_STATUS_AND_BASE_CLASS_NORMALIZATION_LOCK.md`

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

If a queued player hostile action targets an enemy that is defeated before that action resolves in the same round, the action is not wasted.

- Retarget to the next living enemy in encounter-slot order after the original target.
- If no later slot is living, wrap to the first living enemy.
- If no enemies remain living, there is no legal target and battle resolution proceeds as appropriate.
- This rule applies to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly establishes different targeting behavior.
- Retargeting changes only the target; it does not change the action, cost, priority tier, Speed, or actor.
- Presentation/combat logging should expose the retarget clearly enough for the player to understand it.

---

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands without explicit later change control.

---

## Active party

Maximum four active permanent characters. Reserve members are inert while reserved and do not participate through a normal universal mid-battle swap command.

Temporary/guest party participation is authored separately and never expands the permanent roster beyond six.

---

## Ability economy

- MP is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- Content records remain separable from actor engine code wherever practical.
- Focus is selected outside battle and remains fixed for that battle where compatible current equipment rules still use Focus selection.

---

## Standard Card guardrails

Current collection architecture is **24 Standard Cards + 12 Prime Cards = 36 total Cards**.

- Exactly four Standard Cards exist per Face.
- Standard Cards are unlimited-use.
- They are not a deck/hand/draw/discard/charge/rank/duplicate/Essence/refresh-counter system.
- Standard Cards do not summon independent beings. Prime Cards are the collectible manifestation system.
- Card content remains data-driven.
- Standard Cards integrate into the ordinary resolver rather than using a separate timing game.
- Cards are Ancient Diysean artifacts; modern bosses do not create them. A victory/access state may expose or release a pre-existing Card.

The current Faces are Might, Elements, Grace, Acuity, Change, and Ruin.

Any old `30 Standard Cards`, Resource-Face, Break/Stagger-contribution, or obsolete Card-name reference is not current authority.

---

## Prime Card / Prime Manifestation framework

There are exactly **12 Prime Cards**:
- six Story Primes;
- six Major-Hunt Primes.

Current Story Primes:
- Might — **Last Sentinel**
- Elements — **Last Convergence**
- Grace — **Last Sanctuary**
- Acuity — **Last Cartographer**
- Change — **Last Scribe**
- Ruin — **Last Erasure**

Current Major-Hunt Primes:
- Grace — **Dawn Shepherd**
- Might — **Oathbound Colossus**
- Change — **Living Revision**
- Elements — **Prismatic Leviathan**
- Acuity — **Parallax Host**
- Ruin — **Starfall Engine**

### Prime states

Prime progression is exactly:

> **Recovered → Awakened**

There is no Concordant state.

**Recovered**
- One strong Prime manifestation action resolves in the current ordinary round.
- The manifestation then ends.
- Recovered does not persist as a multi-round controllable body.

**Awakened**
- Final and complete Prime state.
- Exactly **3 directly controlled Prime rounds**.
- No later progression state exists.

Removed:
- Prime XP/levels;
- duplicates as progression;
- Prime upgrade materials;
- Concordant harmonization;
- Concordant unlimited duration / HP rules;
- third-stage progression.

Legacy commands formerly labeled Concordant remain in the Awakened kit where otherwise compatible.

### Prime use / form boundaries

- Prime activation uses the Card action.
- A Prime replaces/suspends the active party while its directly controlled Prime rounds are active.
- After the Prime ends, that Prime identity has a **3-full-normal-round cooldown**.
- Each Prime identity may be used once per battle **per genuine boss form**.
- A genuine fresh-HP boss form refreshes that Prime identity's use availability and cooldown.
- Story Primes are acquired Recovered and later Awaken through mandatory story milestones.
- Major-Hunt Primes are obtained already Awakened.

### Direct-control architecture

Preserve the compatible replacement/suspension architecture:

- successful use is bearer/equipment legal and consumes the selected Card action;
- already-locked ordinary actions are not retroactively erased by activation;
- party state can be suspended/frozen while a multi-round Awakened Prime is directly controlled;
- the Prime uses its authored Prime action sheet rather than a substitute universal Attack/Ability/Card/Item/Defend menu;
- one selected Prime command resolves per Prime round, ordered by Prime Speed against hostile actions;
- frozen party state does not tick or become targetable while suspended;
- normal return restores archived party state according to current authored rules.

No Prime had been successfully activated before the modern story.

---

## Damage type and element

Every damaging Ability is authored as exactly one of:
- **Physical**
- **Magical**
- **Hybrid**

Rules:
- Do not offer ordinary selectable Physical/Magical expressions.
- Equipment does not decide an Ability's damage formula.
- Hybrid is only for deliberately dual-axis authored actions.
- Element is separate from formula/type.
- Weapon-independent Ability legality remains intact.

Exactly four standard elements exist:
- **Fire**
- **Ice**
- **Lightning**
- **Earth**

Water and Wind are removed from the current standard element system.

Linked status pairs:
- Fire → Burn
- Ice → Freeze
- Lightning → Stun
- Earth → Staggered

An elemental hit does not automatically inflict the linked status; the action must explicitly carry that rider.

Bleed is non-elemental. Regen is a positive recurring-heal effect.

Exact elemental Weak/Resist damage multipliers, Absorb existence, and normal affinity-profile counts remain open.

---

## Universal harmful statuses

Current set:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Not universal current statuses:
Poison, Confusion, Taunt, Sleep, Silence, Blind, Charm, Fear, separate Shock, Banishment, Instant Defeat, Disable, Jam, Overload, Corrosion.

There is no global Break/Stagger meter/system. `Staggered` is the Earth-linked harmful status only.

### Burn
- 3 rounds.
- Ordinary target: 3% Max HP at end of each affected round.
- Successful reapplication refreshes to 3 rounds.
- No crit; ignores Defense/Spirit; can KO.

### Freeze
- Target cannot act while Frozen.
- First 2 rounds guaranteed.
- 80% persistence check into round 3; 80% persistence check into round 4; max 4 rounds.
- First successful direct Physical hit removes Freeze after the hit.
- Magical/non-Physical damage does not break Freeze merely by dealing damage.
- Cannot refresh while active.

### Stun
- 3 affected turns.
- 40% chance to lose the action on each affected turn.
- Failed roll acts normally.
- Cannot refresh while active.

### Staggered
- 3 rounds.
- Speed −20%.
- Accuracy/Base Hit −20%.
- Evasion −20%.
- Target may still act.
- Reapplication refreshes; does not stack.

### Bleed
- Ordinary target: 2% Max HP when the affected unit successfully takes an action.
- Maximum one Bleed proc per round.
- An action lost to Freeze/Stun does not trigger Bleed.
- Any actual heal restoring at least 1 HP removes Bleed after the heal resolves.
- Regen restoring at least 1 HP also removes Bleed.
- No stack; no crit; ignores Defense/Spirit; can KO.

### Temporary-state lifecycle

- KO clears Burn / Freeze / Stun / Staggered / Bleed / Regen.
- Revival does not restore those cleared temporary effects.
- Battle end clears ordinary temporary combat statuses/effects.
- A genuine fresh-HP boss form clears ordinary temporary statuses unless explicit carryover is authored.

---

## Status application / resistance

Base authored chance bands:
- 10% minor rider
- 20% standard rider
- 35% dedicated status/control
- 50% premium/setup-dependent
- above 50% uncommon / explicitly justified

Matching element/status affinity modifier:
- Weak: +10 percentage points
- Neutral: 0
- Resist: −10 percentage points
- Immune: linked status cannot apply from that elemental hit

Vaelira receives +5 percentage points when **she herself** uses a qualifying Ability whose element matches the linked status being attempted. This is not an automatic bonus for Cards, Primes, Items, other characters, or mismatched pairs.

Status Resistance:
- Normal 0
- Resistant 5
- Highly Resistant 10
- Exceptional 15
- Immune explicit

Ordinary application formula:

> Base Chance + Element Modifier + Vaelira Bonus − Status Resistance

Clamp ordinary legal chance applications to 5%–95% except explicit immunity, guarantee, or script.

High-rank effect conversion:
- Ordinary: full.
- Elite: full by default absent thematic exception.
- Regional Hunt: Freeze max 2 rounds; Stun 25%; Staggered full where legal; Burn/Bleed 75% ordinary damage.
- Major Hunt / mandatory boss: Freeze max 1 round; Stun 20%; Staggered full where legal; Burn/Bleed 50% ordinary damage.

Effect conversion is separate from application chance. Do not use blanket immunity merely to reduce status power.

---

## Remedies and non-status states

Remedy grouping:
- Injury group: Burn + Bleed.
- Control group: Freeze + Stun + Staggered.

Final grouped-remedy display names remain open.

Ordinary remedies do not remove:
- stat changes;
- Fields;
- Guard/Barrier;
- Hunter's Measure;
- Imprints;
- Prepared states;
- protected/scripted encounter states.

Prepared effects, Hunter's Measure, Imprints, Fields, Guard/Barrier, and ordinary stat Up/Down are not the universal harmful statuses listed above.

---

## Prepared effects, universal Attack, and Ability weapon independence

- Attack comes from the currently equipped Weapon. A Conduit Attack is equipment functionality, not a class Ability.
- **No learned Ability or Ultimate requires a particular equipped weapon in order to be legal.** Once learned, an Ability remains usable with any otherwise-legal equipment loadout.
- Weapon choice may change equipment stats, ordinary Attack behavior, and authored presentation, but it does not disable an Ability command or change the Ability's fixed Physical/Magical/Hybrid formula.
- Presentation may use a manifested/spectral weapon, projected strike, Conduit construct, or equivalent visual when the currently equipped weapon does not physically match the technique's traditional form.
- Abilities do not automatically inherit the equipped weapon's ordinary Attack hit pattern unless explicitly authored.
- The one-armed Prepared-effect limit across Abilities and Standard Cards remains active where compatible with later authored effects.
- Presentation cannot invent illegal combat actions merely because a cinematic would look dramatic.

---

## Audit114 Base-class overrides

The detailed current Cyanis and Ilyra Ability names/formula/element/status assignments are controlled by Audit114 and summarized in `docs/ACTIVE_CANON.md`.

Important implementation overrides include:
- Cyanis: Guardian Sigil → **Crest Reprisal**; Harmonizing Ward → **Resonant Pulse**; Resolute Counter → **Sweeping Edge**; Crest Rush → **Twin Advance**.
- Cyanis Crest Rend = Hybrid / Neutral / 35% Bleed.
- Ilyra Warden's Valor no longer rewrites an ally's ordinary Attack; it is Magical / Colorless direct offense.
- Ilyra Gentle Continuance Regen = **4% Max HP for 4 rounds**.
- Healing/output formulas use **Magic**, not Spirit, where Audit114 corrects stale output-stat text.

---

## Determinism and testing

Pure round resolution must remain testable without relying on animation timing.

The regression baseline must cover, where relevant:
- Item priority;
- Defend priority;
- Speed ordering/ties;
- enemy action locking;
- one ordinary selected action per legal unit;
- automatic hostile retargeting including wraparound;
- unlimited Standard Card reuse;
- Prime equipment/use legality;
- Recovered one-action behavior;
- Awakened three-round direct control;
- three-normal-round Prime cooldown;
- genuine fresh-HP boss-form Prime refresh;
- frozen party behavior during multi-round Prime replacement;
- current status timing/application/lifecycle rules.

Tests encoding superseded facts such as Resource, 30 Standard Cards, Concordant, Water/Wind standard elements, Poison, global Break/Stagger, or selectable Physical/Magical Ability expressions must be updated deliberately rather than treated as authority merely because they once passed.

Presentation and animation should consume resolver/state results rather than define combat legality. Future production changes must keep compatible tests green unless a newer approved authority deliberately changes the rule under test.
