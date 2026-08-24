# Audit114 — Prime, Combat Element / Status, and Base-Class Normalization Lock

**Authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.99 / Audit114**  
**Date:** August 24, 2026  
**Status:** **LOCKED / CONTROLLING** for the post-Audit113 Prime-progression correction, fixed damage-type rule, four-element combat model, harmful-status / Regen model, status application and resistance rules, high-rank status conversion, remedy grouping, and the Cyanis / Ilyra Base-class normalizations defined below.

Audit114 inherits all compatible **v1.98 / Audit113** and earlier canon unless explicitly superseded or clarified below.

---

## 0. Authority contract

Audit114 promotes the approved combat-system and Base-class normalization decisions accumulated after Audit113.

This audit does **not** reopen:
- the Chapter-10 insertion / late-game chapter reindex;
- world-map geography or region terminology;
- the six permanent characters, four-active-member party limit, CL13 class architecture, reciprocal Subclasses, Synthesis, or Legacy architecture except where stale Ability text conflicts with this audit;
- the 24-Standard-Card / 12-Prime-Card collection counts;
- exact final Ability MP costs, Power coefficients, Hybrid weighting, elemental damage multipliers, enemy affinity-profile counts, or exact equipment/enemy raw stats unless explicitly stated below.

Where an older file still contains **Water, Wind, Poison, Shock as a separate status, global Break/Stagger, Concordant Prime progression, selectable Physical/Magical Ability expressions, stale Spirit-as-output healing, or the superseded Cyanis/Ilyra Ability text defined here, Audit114 controls.**

---

# 1. Prime progression — controlling correction

There are exactly **12 Prime Cards**:
- **6 Story Primes**;
- **6 Major-Hunt Primes**.

Prime progression has exactly two states:

> **Recovered → Awakened**

**Awakened is final.**

The following are removed and must not return without explicit reopening:
- **Concordant** as a Prime state;
- Prime XP / Prime levels;
- duplicate-Prime progression;
- Prime upgrade materials;
- a third Prime stage;
- Concordant harmonization;
- the old 50% combined-party-HP Concordant rule;
- unlimited-duration Concordant manifestation;
- Concordant-specific scaling.

Legacy commands formerly labeled Concordant remain part of the final **Awakened** kit where otherwise compatible; old `Concordant Final` presentation becomes Awakened final-art / late-command presentation rather than being deleted merely because the state name is gone.

## 1.1 Recovered

- A Recovered Prime resolves **one strong manifestation action in the current ordinary round**.
- It does not remain as a persistent controllable body across multiple Prime rounds.
- After the action resolves, the manifestation ends.

## 1.2 Awakened

- Awakened is the complete final Prime state.
- The Prime is directly controlled for exactly **3 Prime rounds**.
- The Prime replaces the active party while manifested under the existing compatible direct-control / party-suspension architecture.
- After the Prime ends, that Prime enters a cooldown of **3 full normal rounds**.
- Each Prime identity may be used once per battle **per genuine boss form**.
- A genuine fresh-HP boss form refreshes that Prime identity's use availability and cooldown state.

No state exists beyond Awakened.

## 1.3 Story Prime acquisition / Awakening

Story Primes are acquired **Recovered** and later become **Awakened** through mandatory story milestones tied to their associated character/theme.

- **Last Sentinel / Might / Cyanis** — acquired Chapter 4; Awakened in the Chapter-5 Deepforge sovereign-chamber milestone.
- **Last Cartographer / Acuity / Torren** — acquired Chapter 5; Awakened in Chapter 8 at the Horizon Vault / western-survey culmination.
- **Last Convergence / Elements / Vaelira** — acquired Chapter 6; Awakened at the end of Chapter 7 through the Sixfold Volition culmination.
- **Last Scribe / Change / Nimera** — acquired Chapter 7; Awakened in current Chapter 11 through the Custodian / truth-archive milestone.
- **Last Erasure / Ruin / Seyrik** — acquired Chapter 8; Awakened in current Chapter 12 during The Reforged March.
- **Last Sanctuary / Grace / Ilyra** — acquired Chapter 9; Awakened in Chapter 9 at **Mercy Is Not Surrender**.

Story Prime Awakening is not gated by Character Quests.

## 1.4 Major-Hunt Primes

Major-Hunt Primes are obtained **already Awakened**. The Major Hunt itself is the proof/trial; there is no separate Prime-Sanctuary upgrade step.

- **Ashen Whitehorn** → **Dawn Shepherd / Grace**.
- **Crownless Siege Marshal → Crownless War Engine** → **Oathbound Colossus / Might**.
- **Concordance Guardian** → **Living Revision / Change**.
- **Worldscar Leviathan** → **Prismatic Leviathan / Elements**.
- **Final Archive Arbiter** → **Parallax Host / Acuity**.
- **The Unfinished World / Worldheart** → **Starfall Engine / Ruin**.

Prime materials must not be added to Forge Components, Project Items, global enemy drops, shops, Kessara inventories, or the ordinary economy.

---

# 2. Fixed damage-type rule

Every damaging Ability is authored as exactly one of:
- **Physical**;
- **Magical**;
- **Hybrid**.

Rules:
- Ordinary Abilities do **not** offer selectable Physical/Magical expressions.
- Equipment or hidden resolver logic does not choose whether an Ability becomes Physical or Magical.
- **Hybrid** is used only where the Ability is deliberately authored to combine both attack axes.
- Element is a separate property from damage type/formula.
- Legal combinations include Physical + element, Magical + element, Neutral Physical, Colorless Magical, and deliberately authored Hybrid + element.
- Weapon-independent Ability legality remains intact: an Ability's fixed formula is not a weapon requirement.

This supersedes older generic wording that could be read as requiring every martial/magical-flavored Ability to provide multiple formula expressions.

---

# 3. Element model — exactly four elements

The standard combat element set is exactly:

1. **Fire**
2. **Ice**
3. **Lightning**
4. **Earth**

Removed from the current standard element system:
- **Water**;
- **Wind**.

Do not restore Water or Wind without explicit reopening.

Element and harmful-status identity are related but not automatic. An elemental hit does **not** inflict its linked status unless the action explicitly has a status application rider.

Linked pairs:
- **Fire → Burn**
- **Ice → Freeze**
- **Lightning → Stun**
- **Earth → Staggered**

**Bleed** is non-elemental.

**Regen** is a positive recurring-heal effect, not an element and not a harmful status.

## 3.1 Still open

Audit114 intentionally does **not** lock:
- the exact damage multiplier for elemental Weak / Resist;
- whether elemental **Absorb** exists;
- exact ordinary/boss affinity-profile counts (for example, how many weaknesses/resists/immunities a typical enemy should have).

Those remain for the dedicated affinity / numerical pass.

---

# 4. Removed universal status / meter systems

The current universal harmful-status set is limited to:
- **Burn**
- **Freeze**
- **Stun**
- **Staggered**
- **Bleed**

The following are not universal current statuses and must not be casually reintroduced:
- Poison
- Confusion
- Taunt
- Sleep
- Silence
- Blind
- Charm
- Fear
- Shock as a separate status
- Banishment
- Instant Defeat
- Disable
- Jam
- Overload
- Corrosion

An authored story/boss outcome may still use ordinary English such as banishment or defeat where legally appropriate, but that does not create a reusable universal status system.

## 4.1 Global Break/Stagger system is removed

There is no universal:
- Break meter;
- Stagger meter;
- buildup threshold;
- Break/Stagger vulnerability phase;
- Break/Stagger damage multiplier;
- universal boss Break resistance;
- equipment axis existing solely to build Break/Stagger;
- hidden renamed equivalent of the same meter.

**Staggered** now means only the Earth-linked harmful status defined below.

Older Acuity Card, Prime, Ability, gear, or enemy wording that references `Break/Stagger contribution/effectiveness` is stale and is superseded. Preserve compatible non-Break functions, but replacement riders must be authored in the later Card/Prime/Ability pass rather than inventing a hidden meter now.

---

# 5. Harmful-status mechanics

## 5.1 Burn

- Duration: **3 rounds**.
- Ordinary target damage: **3% target Max HP** at the end of each affected round.
- Full ordinary duration therefore deals 9% Max HP if all three ticks resolve.
- Does not stack.
- Successful reapplication refreshes Burn to 3 rounds.
- Burn cannot crit.
- Burn ignores Defense and Spirit.
- Fire affinity is checked for application; Burn damage itself does not receive an additional Fire multiplier after landing.
- Burn damage does not trigger unrelated on-hit riders, counters, lifesteal, or similar attack-resolution effects.
- Burn may reduce a target to 0 HP.
- Normal eligible cleansing removes Burn.

## 5.2 Freeze

- A Frozen unit **cannot act** while Freeze prevents its turn.
- Rounds 1–2 are guaranteed Freeze duration.
- After round 2, Freeze has an **80% chance** to persist into round 3.
- After round 3, Freeze has an **80% chance** to persist into round 4.
- Maximum duration: **4 rounds**.
- The first successful direct **Physical** damage hit against the Frozen target removes Freeze **after that hit resolves**.
- Elemental Physical damage also breaks Freeze.
- Magical / non-Physical damage does not break Freeze merely by dealing damage.
- Freeze cannot be refreshed while already active.
- It may be reapplied after the prior Freeze ends.

## 5.3 Stun

- Duration: **3 turns**.
- On each affected turn, there is a **40% chance** the unit loses that action.
- If the roll fails, the unit acts normally that turn.
- Stun expires after the third affected turn.
- Stun cannot be refreshed while already active.
- It may be reapplied after the prior Stun ends.

`Shock` does not exist as a separate current status; Lightning-linked action denial is **Stun**.

## 5.4 Staggered

- Duration: **3 rounds**.
- Speed: **−20%**.
- Accuracy / Base Hit: **−20%**.
- Evasion: **−20%**.
- The target can still act.
- Does not stack.
- Successful reapplication refreshes the duration to 3 rounds.

Staggered is a normal harmful status, not a Break/Stagger phase or meter.

## 5.5 Bleed

- Ordinary target damage: **2% target Max HP** when the affected unit successfully takes an action.
- Bleed can trigger at most **once per round**, even if the unit has a multi-action package.
- If the unit's action is skipped/lost because of Freeze or Stun, Bleed does not trigger for that lost action.
- Bleed persists until actual HP healing succeeds.
- Any heal that restores **at least 1 HP** removes Bleed **after the heal resolves**.
- A Regen tick that restores at least 1 HP also removes Bleed.
- A zero-HP-result heal does not remove it.
- KO clears Bleed.
- Bleed does not stack.
- Reapplying Bleed while active does not create an extra immediate Bleed proc.
- Bleed cannot crit.
- Bleed ignores Defense and Spirit.
- Bleed damage does not trigger unrelated on-hit riders, counters, lifesteal, or similar attack-resolution effects.
- Bleed may reduce a target to 0 HP.

Bleed is non-elemental and receives no elemental-affinity application modifier.

---

# 6. Regen and temporary-state lifecycle

**Regen** is a positive recurring HP-restoration effect whose potency and duration are source-specific.

There is no single universal Regen potency/duration.

Current locked Ilyra examples in this audit:
- **Gentle Continuance:** 4% Max HP per round for 4 rounds.
- **Dawn Without End:** 5% Max HP per round for 3 rounds.

A Regen tick that restores at least 1 HP removes Bleed under the global Bleed rule.

## 6.1 Temporary-state lifecycle

- KO clears Burn, Freeze, Stun, Staggered, Bleed, and Regen.
- Revival does not restore the temporary effects that were cleared by KO.
- Battle end clears ordinary temporary combat statuses/effects.
- A genuine fresh-HP boss form clears ordinary temporary statuses unless that encounter explicitly authors carryover.

Reapplication behavior:
- Burn — refreshes.
- Freeze — no refresh while active.
- Stun — no refresh while active.
- Staggered — refreshes.
- Bleed — no stacking / no extra proc from reapplication while active.

There is no universal post-status immunity window unless a specific encounter/action explicitly provides one.

---

# 7. Status application chance

Current authored base-chance bands:
- **10%** — minor rider on an already-strong damaging action.
- **20%** — standard status rider.
- **35%** — dedicated status/control rider.
- **50%** — premium, setup-dependent, or strongly status-focused application.
- **Above 50%** — uncommon and requires explicit specialization, setup, vulnerability, or authored exception.

Older routine 75–90% rider assumptions are removed.

## 7.1 Element affinity modifier to linked status

For the matching element/status pair only:
- target **Weak** to the element: **+10 percentage points** to linked-status application;
- **Neutral**: +0;
- target **Resists** the element: **−10 percentage points**;
- target **Immune** to the element: the linked status cannot be applied from that elemental hit.

This modifier does not apply to mismatched statuses and does not apply to non-elemental **Bleed**.

## 7.2 Vaelira elemental-specialist bonus

When **Vaelira herself** uses a qualifying Ability whose element matches the linked status being attempted:
- **+5 percentage points** to application chance.

This applies to qualifying Vaelira-native Green Arcanist / Axiomblade actions as authored.

It does not automatically apply to:
- Cards;
- Prime commands;
- Items;
- another character's action;
- a mismatched element/status pair.

Do not inflate this into a larger +15/+20 specialist bonus without explicit reopening.

## 7.3 Status Resistance

Final ordinary application chance is:

> **Base Chance + Element Modifier + Vaelira Bonus − Status Resistance**

For ordinary legal chance-based applications, clamp the result to **5%–95%**, except where explicit immunity, guaranteed application, or scripted encounter logic says otherwise.

Status Resistance scale:
- **Normal:** 0 percentage points.
- **Resistant:** 5.
- **Highly Resistant:** 10.
- **Exceptional:** 15.
- **Immune:** explicit immunity.

Typical guidance:
- ordinary enemy: usually 0;
- Elite: usually 0–5;
- Regional Hunt: usually 5–10;
- Major Hunt: usually 10–15;
- mandatory boss: usually 10–15.

Not every boss should automatically sit at the top value.

---

# 8. High-rank status effect conversion

High-rank enemies should not receive blanket immunity merely to reduce status power.

Application chance and post-application effect strength are separate.

## 8.1 Ordinary enemies
- Full status effect.

## 8.2 Elites
- Full status effect by default unless the Elite has an explicit thematic immunity/resistance.

## 8.3 Regional Hunts
- Freeze: maximum **2 rounds**.
- Stun: 3 affected turns at **25%** action-loss chance per turn.
- Staggered: full ordinary effect where legal.
- Burn damage: **75%** of ordinary Burn damage = **2.25% Max HP per tick**.
- Bleed damage: **75%** of ordinary Bleed damage = **1.5% Max HP per proc**.

## 8.4 Major Hunts and mandatory bosses
- Freeze: maximum **1 round**.
- Stun: 3 affected turns at **20%** action-loss chance per turn.
- Staggered: full ordinary effect where legal unless explicitly exempted by encounter mechanics.
- Burn damage: **50%** of ordinary Burn damage = **1.5% Max HP per tick**.
- Bleed damage: **50%** of ordinary Bleed damage = **1% Max HP per proc**.

This effect conversion does not by itself alter application chance; Status Resistance / affinity rules still determine whether the status lands.

---

# 9. Remedy grouping and state boundaries

The two grouped ordinary status-remedy functions are:

- **Injury group:** Burn + Bleed.
- **Control group:** Freeze + Stun + Staggered.

The final display names of the two grouped remedies remain open; do not lock a retired placeholder name merely because the grouping is now fixed.

- General Remedy removes one eligible ordinary harmful status according to its authored target rules.
- Full Remedy removes all eligible ordinary harmful statuses from the conscious target according to its authored target rules.

Ordinary status remedies do **not** remove:
- ordinary stat changes;
- Fields;
- Guard / Barrier states;
- Hunter's Measure;
- Imprints;
- Prepared effects;
- boss-only/scripted configurations or protected states.

Stat changes are a separate system from harmful statuses. Examples include Attack, Magic, Defense, Spirit, Speed, Accuracy, and Status Resistance Up/Down where authored.

---

# 10. Cyanis — Crest Knight Base normalization

Cyanis is complete for the current formula / element / status pass.

The Base unlock positions from Audit104 remain, but the following Ability names/functions now control where they conflict with older class files.

## CL1 — Crest Strike
- Damage type: **Physical**.
- Element: **Neutral**.
- Target: one enemy.
- No harmful-status rider.

## CL1 — Crest Reprisal
Supersedes **Guardian Sigil**.

- No ally target selection.
- Cyanis arms a one-use **Prepared** intercept state on himself.
- The next eligible single-target hostile attack originally aimed at another active party member is intercepted by Cyanis.
- Cyanis becomes the recipient of that hostile action.
- After the hostile action resolves, Cyanis immediately performs a powerful counter against the attacker if it remains a legal target.
- Counter damage type: **Physical**.
- Counter element: **Neutral**.
- No harmful-status rider.
- It does not trigger when Cyanis was already the original target.
- It does not intercept ordinary full-party/multi-target hostile actions.

Exact MP, Prepared duration wording, and counter Power remain for the coefficient pass.

## CL1 — Resonant Pulse
Supersedes **Harmonizing Ward**.

- Damage type: **Magical**.
- Element: **Colorless**.
- Target: one enemy.
- No harmful-status rider.

The old cleanse + Defense/Spirit support function is retired from this slot.

## CL3 — Sweeping Edge
Supersedes **Resolute Counter**.

- Damage type: **Physical**.
- Element: **Neutral**.
- Target: all enemies.
- **10% base Bleed chance per target**.
- No counter / Prepared behavior.
- No defensive rider.

## CL6 — Twin Advance
Supersedes **Crest Rush**.

- Damage type: **Physical**.
- Element: **Neutral**.
- Target: one enemy.
- Exactly **2 hits**.
- No harmful-status rider.
- No self damage-reduction rider.
- No alternate Magical/Spirit-penetration route.

## CL9 — Crest Rend
- Damage type: **Hybrid**.
- Element: **Neutral**.
- Target: one enemy.
- **35% base Bleed chance**.
- The old `Vulnerability` rider is removed/superseded.
- Exact Attack/Magic weighting and Hybrid penetration/defense resolution remain deferred to the coefficient/formula pass.

## CL13 — Crest of Companions
- Enemy damage type: **Magical**.
- Element: **Colorless**.
- Target: all enemies for the damaging portion.
- No harmful-status rider.
- Preserve the compatible established party-cleanse/support component unless separately reopened in a later non-status balance pass.

## Cyanis Trait

**Harmonized Crest** is **not redesigned by Audit114**. Older proposals to create a new Physical↔Magical priming trait were not approved and do not become canon through this audit.

---

# 11. Ilyra — Blue Warden Base normalization

Ilyra is complete for the current formula / element / status pass.

The Base unlock positions and overall preservation/healing identity from Audit104 remain.

## CL1 — Mend
- Healing Ability; no damage type and no element.
- Healing output scales from **Magic**, not Spirit.
- No harmful-status rider.
- Preserve compatible established direct-heal behavior.

## CL1 — Clear Warding
- No damage type and no element.
- Removes **one eligible ordinary harmful status**.
- Current ordinary cleanse set is Burn / Freeze / Stun / Staggered / Bleed, subject to ordinary cleanse legality.
- Its Status Resistance Up effect remains a **stat change**, not a status ailment.
- Do not carry stale Poison/Blind/Silence/Slow cleanse lists forward.

## CL1 — Renewal
- Party healing; no damage type and no element.
- Healing output scales from **Magic**, not Spirit.
- No automatic Regen is added merely because the Ability is named Renewal.
- Preserve compatible established party-heal behavior.

## CL3 — Warden's Valor
The inherited ally-Attack-rewrite effect is retired.

Current function:
- Damage type: **Magical**.
- Element: **Colorless**.
- Target: one enemy.
- Scaling axis: **Magic**.
- Straightforward offensive Blue Warden / Grace projection.
- No healing rider.
- No harmful-status rider.
- Does not modify another ally's ordinary Attack command.

Exact MP and Power remain for the later coefficient pass.

## CL6 — Revive
- No damage type and no element.
- Preserve the established revive-at-HP behavior.
- Remove any redundant explicit `clear Bleed` clause; KO already clears ordinary temporary statuses under Audit114.

## CL9 — Lifeline
- No damage type and no element.
- **Prepared** survival effect, not an ordinary status ailment.
- Its recovery output scales from **Magic**, not Spirit.
- Preserve the compatible established one-trigger survival behavior.

## Gentle Continuance — Base Trait
Preserve compatible established trigger structure, with the following locked Regen correction:
- Regen potency: **4% Max HP per round**.
- Duration: **4 rounds**.
- Trigger remains excess direct healing under the established Trait condition.
- Once per target per action.
- A Regen tick that restores at least 1 HP removes Bleed under the global rule.

Compatible established Trait effects outside this correction remain, including the low-HP direct-heal bonus / cleanse-healing relationship unless separately reopened.

## CL13 — Dawn Without End
- Enemy damage type: **Magical**.
- Element: **Colorless**.
- Healing output scales from **Magic**, not Spirit.
- Remove obsolete Poison wording.
- Cleanses **all eligible ordinary harmful statuses** from affected allies: Burn / Freeze / Stun / Staggered / Bleed, subject to protected/scripted exclusions.
- Applies **Regen: 5% Max HP per round for 3 rounds**.
- Preserve compatible established revive/heal/AoE structure outside the stale status/output-stat corrections.

---

# 12. Downstream stale-reference rules

The following inherited references are now known stale and must be reconciled when their dedicated content passes are reached:

- `Water` / `Wind` standard-element references.
- `Poison` as a universal status.
- `Shock` as separate from Stun.
- global `Break/Stagger contribution/effectiveness` wording in Acuity Cards, Primes, Abilities, equipment, and enemy data.
- `Concordant` Prime-state requirements or commands.
- selectable Physical/Magical Ability-route language.
- healing/output formulas that incorrectly use **Spirit** where **Magic** is the offensive/healing output stat.
- Cyanis names/functions superseded in Section 10.
- Ilyra Warden's Valor two-strike ally-Attack modification superseded in Section 11.

Do not invent replacements merely to eliminate a stale word. Preserve compatible core functions and defer exact new riders to the relevant Ability/Card/Prime/equipment pass.

---

# 13. Open work after Audit114

1. Continue the Base-class formula / element / status pass with **Torren → Nimera → Vaelira → Seyrik**.
2. Run the same normalization across all six Subclasses.
3. Normalize all **24 Standard Cards** against the four-element / five-harmful-status / no-global-Break model.
4. Normalize all **12 Prime Cards** against the same element/status model and the Recovered→Awakened progression lock.
5. Reconcile enemy, Regional Hunt, Major Hunt, and mandatory-boss Ability/status references.
6. Lock exact elemental Weak/Resist damage multipliers and decide whether Absorb exists.
7. Lock enemy affinity-profile construction rules.
8. Complete exact Ability MP/Power, Hybrid weighting/defense resolution, equipment raw stats, enemy raw stats, and downstream economy/drop work in their dedicated passes.
9. Sweep implementation-facing combat/class/Card/Prime files and tests for stale Audit114-invalid terminology and assumptions.

Omission from this audit does not erase compatible older canon. **Audit114 controls only the corrections and locks explicitly defined above; Audit113 and all compatible earlier authorities remain active.**
