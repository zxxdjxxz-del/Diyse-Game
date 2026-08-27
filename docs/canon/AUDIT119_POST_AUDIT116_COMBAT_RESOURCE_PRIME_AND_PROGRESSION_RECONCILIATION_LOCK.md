# Diyse — Audit119: Post-Audit116 Combat, Resource, Prime, and Progression Reconciliation Lock

**Master-canon version:** **v2.04 / Audit119**  
**Date:** August 26, 2026  
**Status:** **MASTER CANON — CONTROLLING**  
**Parent authority:** **v2.03 / Audit118** plus all compatible older locks.  
**Purpose:** Reconcile the remaining current post-Audit116 tracker decisions that were outside Audit117/Audit118's equipment scope: the universal HP-damage resolver, the later Standard-Card/Prime MP economy, the late MP-restorative expansion, named-combat resistance hierarchy, Prime manifestation scaling/control rules, and current high-level EXP/progression directives. It also explicitly quarantines tracker branches that are stale or still provisional.

Where this audit conflicts with Audit118/Audit117 in equipment domains, those audits continue to control. Where this audit explicitly changes Card/Prime MP values or Prime numerical/control rules from Audit116, **Audit119 controls**. Audit115 remains controlling for compatible status definitions, class-Ability effects, elements, and Ruin rules. Audit113 remains controlling for current chapter numbering.

---

# 1. Tracker supersession / quarantine firewall

The cumulative tracker is design history and contains branches that must not be promoted merely because they appear later in the file.

The following are explicitly **not** current canon:

- the temporary Story-Prime state label **Reactive**; current progression remains **Recovered → Awakened**;
- old 60/75/75, 70/90/90, and 55/80/90 Prime Invocation ladders where they conflict with Section 4 below;
- the exact v494–v503 Chapter-1–13 player/enemy level bands and encounter-count calibration, which were later reopened for a dedicated EXP rebalance;
- the exact v465 selected-class natural-stat multiplier table where it conflicts with newer class identities/kit work; the neutral-stat/natural-growth layer remains subject to its dedicated revalidation;
- old class-specific MP tables written against retired/currently changed Subclass identities; they remain useful numerical history, not current implementation authority;
- the v480–v493 ordinary-side-quest roster reductions as a current roster authority; a later project correction supersedes that branch as summarized in Section 10;
- provisional HP-consumable values from v479 where final enemy-damage certification was explicitly still pending;
- exact named-enemy raw-stat arrays that depend on the deferred chapter-level/encounter rebalance, except the late Major-Hunt anchors explicitly retained in Section 9.

---

# 2. Universal final-damage equation — promoted from tracker v511

For one Physical or Magical damage component:

> **Component Damage = Weight × (Power / 100) × Offense × 1.50 × [150 / (150 + Effective Defensive Stat)]**

Axes:

- Physical: **Attack vs Defense**
- Magical: **Magic vs Spirit**
- pure Physical/Magical Weight = **1.00**
- 50/50 Hybrid = **0.50 / 0.50**
- character Ability Ruin = **0.75 Attack / 0.25 Magic**
- any other Hybrid uses its explicitly authored weights

Global constants:

- **Offense scale = 1.50**
- **Defense constant = 150**

## Penetration

For each defensive axis:

1. resolve current Defense/Spirit changes;
2. collect legal same-axis penetration;
3. add percentage-point penetration sources;
4. cap effective penetration at **75%**;
5. calculate `Effective Defensive Stat = Current Defensive Stat × (1 - Effective Penetration)`;
6. carry the unrounded value into the damage equation.

Do not:

- average Defense and Spirit;
- transfer unused penetration between axes;
- exceed the 75% cap;
- round the penetrated defensive stat early.

## Hybrid resolution

Hybrid damage resolves each component independently on its own axis and then adds the components before affinity/final-damage layers. Do not average Attack/Magic or Defense/Spirit.

## Basic Attack

The universal **Attack** command is:

- **100 Power**
- **Physical**
- **Neutral** unless equipment explicitly authors another affinity
- no harmful-status rider unless equipment explicitly grants one.

## Final damage order

For ordinary direct damage:

1. establish Power;
2. establish damage formula/weights;
3. establish current offense;
4. establish current defenses after ordinary stat changes;
5. resolve same-axis penetration;
6. calculate components;
7. combine Hybrid components;
8. apply elemental/Ruin/Colorless affinity;
9. apply authored whole-action final-damage bonuses;
10. apply target-side final/direct-damage reductions;
11. resolve Guard/Barrier/interception under their own authored rules;
12. round final HP damage **once**.

Separately authored final-damage modifiers multiply unless an effect explicitly defines a shared/replacement bucket.

There is **no hidden universal AoE penalty**. Authored Power already accounts for target count. Multihit actions resolve their listed hit Powers individually.

Burn, Bleed, fixed/%Max-HP damage, reflected percentage damage, healing, revival, and fixed-value barriers remain outside this equation where separately authored.

There is **no universal random ±damage variance**. The same legal inputs produce the same pre-rider damage result.

The universal Critical multiplier/resolution order remains open; this resolver certifies non-critical damage and does not invent a Crit payout.

---

# 3. Standard Card MP rebase — exact current costs

Audit116 Card identities/effects remain controlling where compatible, but its older 12–36 MP cost table is superseded here.

Current Standard-Card MP range:

> **18–48 MP**

### Might
- Iron Testament — **22 MP**
- Sunder the Gate — **28 MP**
- Relentless Flurry — **30 MP**
- March of Blades — **32 MP**
- Sanguine Alloy — **26 MP**

### Elements
- Cinder Judgment — **24 MP**
- Winterglass Spear — **26 MP**
- Thunder Chain — **32 MP**
- Confluence Sigil — **34 MP**
- Worldsplitter — **38 MP**

### Grace
- Restoration — **28 MP**
- Merciful Reprisal — **28 MP**
- Wellspring — **36 MP**
- Dawn Recall — **44 MP**

### Acuity
- Faultline Sight — **18 MP**
- Measured Response — **24 MP**
- Predicted Impact — **28 MP**
- Decisive Interval — **36 MP**

### Change
- Burden Shift — **26 MP**
- Reversal Engine — **40 MP**
- Split Moment — **48 MP**

### Ruin
- Calamity Lance — **34 MP**
- Devouring Singularity — **42 MP**
- Zero Hour — **48 MP**

This is a cost-only supersession. Card Power, targeting, penetration, statuses, healing, and action-economy rules remain controlled by Audit116 unless separately revised.

---

# 4. Prime Invocation MP — latest current tracker ladder

Current Prime progression remains:

> **Recovered → Awakened**

Current Invocation costs:

- **Recovered Story Prime — 50 MP**
- **Awakened Story Prime — 80 MP**
- **Awakened Major-Hunt Prime — 90 MP**
- manifested Prime commands — **0 additional MP**

This supersedes older 60/75/75, 70/90/90, and 55/80/90 ladders.

Prime Invocation remains a severe resource commitment. No per-Prime-round MP drain is added after manifestation.

---

# 5. Class-Ability MP direction after later class changes

The user-directed resource rule remains:

- MP costs are **higher across the board** than the older low-cost class tables;
- Subclass abilities should generally carry a **modest MP premium** because they unlock later;
- Mastery/Trait cost reductions apply **after** the authored base cost.

However, the exact v467/v469 Base/Subclass tables were written against an older class/subclass identity set. They are **not** promoted wholesale by Audit119.

Until the current class-kit pass is numerically reconciled, do not treat obsolete low Audit115 MP values or the retired-name v467/v469 tables as final implementation costs. Exact current-kit Ability MP remains an open numerical pass.

---

# 6. Consumable catalog — late MP-restorative expansion

The current consumable catalog is:

> **21 Consumables**

This supersedes Audit106's 20-consumable count by adding one late-game MP restorative.

Current MP-restoration family:

- **Flow Tonic — restore 50 MP**
- **Deepflow Tonic — restore 80 MP**
- **Highflow Tonic — restore 120 MP**
- **Reservoir Tonic — restore 75% Max MP**
- **Emergency Kit — restore 60% Max MP** as its MP component of the broader exceptional package

Roles:

- Flow Tonic remains ordinary/core MP stock;
- Deepflow Tonic is stronger later/specialist stock;
- **Highflow Tonic** is the late-game purchasable fixed-value tier, intended for advanced stock roughly in the late campaign;
- Reservoir Tonic remains rare/reward-only and not normal-shop stock;
- Emergency Kit remains exceptional/not normal-shop stock.

No restorative may exceed Max MP; excess restoration is lost.

The exact final vendor placement, price, and currency denomination remain open.

The v479 HP values remain **provisional**, including Field/Restorative/Vital/Company Salve exact numbers and Emergency Kit's HP component. Emergency Rally's exact revive/heal percentages also remain open.

---

# 7. Named-combat elemental/status resistance hierarchy — promoted from v507

Named combat should be more resistant than ordinary enemies without becoming blanket-immune.

## Elemental damage multipliers

- Weak — **125%**
- Neutral — **100%**
- Resistant — **80%**
- Strongly Resistant — **60%**
- Immune — **0%**

No generic absorption/reflection/elemental healing is implied.

## Harmful-status application susceptibility

- Normal — **100%**
- Resistant — **80%**
- Strongly Resistant — **60%**
- Immune — **0%**

Status susceptibility multiplies the authored application chance. It is separate from Audit115's boss-tier duration/magnitude conversions.

Status-resolution order:

1. check explicit immunity;
2. calculate authored application chance;
3. multiply by target susceptibility;
4. roll application;
5. if successful, apply the status;
6. then apply target-tier duration/magnitude rules.

## Tier rules

Ordinary enemies normally have little resistance and commonly retain exploitable weaknesses.

Optional Elites normally have at least one elemental resistance and at least two defended statuses; broad blanket resistance is not normal.

Mandatory bosses normally have one Strong Resistance or two ordinary elemental Resistances plus at least two resisted statuses. The normal ceiling is one status immunity; elemental immunity is rare/thematic.

Regional Hunts normally have one Strong Resistance + one Resistance, or two Resistances, plus two to three resisted statuses. They must not permanently wall all four standard elements.

Major Hunts normally have at least two defended elemental relationships and three defended statuses. At least one standard element must remain Neutral or Weak at a given time under normal conditions unless a specific temporary mechanic says otherwise.

True nonliving constructs may be **Bleed Immune**. Elemental identity may justify one obvious linked immunity, but elemental resistance never automatically creates status immunity.

Named enemies may still have weaknesses. Resistance exists to create preparation/choice, not to erase elemental/status builds.

## Current Major-Hunt static resistance profiles

- **Ashen Whitehorn:** Ice 60%; Earth 80%; Freeze 60%; Staggered 60%; Stun 80%.
- **Crownless Siege Marshal:** Earth 60%; Fire 80%; Staggered 60%; Stun 80%; Bleed 80%.
- **Crownless War Engine:** Earth 60%; Lightning 80%; Bleed Immune; Stun 60%; Staggered 60%.
- **Concordance Guardian:** Lightning 80%; Earth 80%; Bleed Immune; Stun 60%; Freeze 80%; Staggered 80%.
- **Worldscar Leviathan:** Earth 80%; currently stored/released element 60% while active; Staggered 60%; Freeze 60%; Stun 60%; Burn 80%.
- **Final Archive Arbiter:** Lightning 60%; Earth 80%; Bleed Immune; Stun 60%; Freeze 80%; Staggered 80%.
- **The Unfinished World:** current World-State element 60%; other standard elements Neutral; Ruin 80%; Burn/Freeze/Stun/Staggered 60%; Bleed 80%.

Temporary authored encounter states may supersede the static line while active.

The same v507 tier philosophy continues to the current mandatory-boss, Regional-Hunt, and optional-Elite rosters. Exact static profiles preserved in the working tracker remain valid where those encounter identities remain unchanged, but raw-stat/level arrays remain separately subject to the progression rebalance.

---

# 8. Prime status/control defense — promoted from v523

Primes do not receive blanket harmful-status immunity.

Default Prime application susceptibility:

> **80% for all five canonical harmful statuses**

This applies to Story and Major-Hunt Primes unless an individual Prime is explicitly authored otherwise.

Prime-local status effects disappear on dismissal and do not transfer to the returning party.

### Burn
- 80% application susceptibility;
- full Prime-local 3% Max-HP end-round value;
- cannot outlive the remaining manifestation duration.

### Bleed
- 80% application susceptibility;
- full 2% Max HP on successful Prime action;
- maximum once per Prime round.

### Staggered
- 80% application susceptibility;
- full -20% Speed / Base Hit / Evasion effect.

### Freeze
- 80% application susceptibility;
- may deny at most **one selected Prime command** per application;
- then ends;
- direct Physical damage still breaks Freeze after the hit under the normal rule.

### Stun
- 80% application susceptibility;
- **20%** chance to lose the selected Prime command on an affected Prime turn;
- one Stun application may cause at most one lost Prime command.

### Control Guard

Across one three-round manifestation, Freeze/Stun together may deny at most **one selected Prime command**. After that hard-control loss, the Prime becomes Freeze/Stun immune for the remainder of that manifestation.

This prevents a legal three-round Prime from being reduced to zero functional commands while preserving status interaction.

---

# 9. Prime manifestation scaling architecture / retained late-Hunt anchors

Prime manifestation remains a deterministic battle-time stat package, not a Prime-level system.

There is:

- no Prime XP;
- no Prime levels;
- no Prime duplicate progression.

## Reference Level

> **Reference Level = highest current level among the four active permanent-party members at Invocation**, clamped 1–70.

The Prime does not store that level permanently and does not inherit the invoker's stats, equipment, buffs, current HP%, or harmful statuses.

## Neutral manifestation baseline

At Reference Level `L`, using the current neutral natural-character values at that level:

- Prime HP baseline = **2.25 × Neutral HP(L)**
- Prime Attack baseline = **4.75 × Neutral ATK(L)**
- Prime Magic baseline = **4.75 × Neutral MAG(L)**
- Prime Defense baseline = **1.65 × Neutral DEF(L)**
- Prime Spirit baseline = **1.65 × Neutral SPR(L)**
- Prime Speed baseline = **Neutral SPD(L) + 8**

The neutral natural-growth formula itself remains subject to the separate progression/stat revalidation. If that neutral curve is revised later, regenerate Prime raw arrays from the same promoted manifestation architecture unless the Prime architecture is explicitly reopened.

## State multipliers

| State | HP | ATK/MAG | DEF/SPR | Speed |
|---|---:|---:|---:|---:|
| Recovered Story | 0.85 | 0.82 | 0.85 | 0.95 |
| Awakened Story | 1.00 | 1.00 | 1.00 | 1.00 |
| Awakened Major Hunt | 1.08 | 1.06 | 1.08 | 1.04 |

## Prime identity multipliers

| Prime | HP | ATK | MAG | DEF | Spirit | SPD |
|---|---:|---:|---:|---:|---:|---:|
| Last Sentinel | 1.12 | 1.16 | 0.74 | 1.18 | 0.95 | 0.90 |
| Last Cartographer | 0.96 | 1.10 | 0.82 | 0.90 | 0.92 | 1.18 |
| Last Convergence | 0.90 | 0.70 | 1.18 | 0.86 | 1.10 | 1.02 |
| Last Scribe | 0.95 | 0.78 | 1.08 | 0.94 | 1.12 | 1.08 |
| Last Sanctuary | 1.05 | 0.72 | 1.05 | 1.05 | 1.20 | 0.92 |
| Last Erasure | 1.10 | 1.12 | 1.08 | 1.08 | 0.92 | 0.90 |
| Dawn Shepherd | 1.08 | 1.05 | 1.05 | 1.00 | 1.15 | 1.00 |
| Oathbound Colossus | 1.18 | 1.20 | 0.65 | 1.22 | 0.90 | 0.82 |
| Living Revision | 1.05 | 1.00 | 1.00 | 1.03 | 1.03 | 1.05 |
| Prismatic Leviathan | 1.10 | 0.65 | 1.18 | 1.00 | 1.18 | 0.90 |
| Parallax Host | 0.98 | 1.02 | 1.02 | 0.90 | 0.90 | 1.18 |
| Starfall Engine | 1.15 | 1.12 | 1.12 | 1.08 | 0.92 | 0.88 |

Implementation order:

1. determine Reference Level;
2. calculate neutral natural stat at that level;
3. apply Prime-neutral baseline multiplier;
4. apply state multiplier;
5. apply Prime identity multiplier;
6. round final raw stat to nearest whole number; do not round intermediate values.

Primes have **no MP stat** because manifested commands cost 0 additional MP.

Current retained late-Major-Hunt numerical anchors:

- **Final Archive Arbiter:** 43,100 HP / 229 ATK / 244 MAG / 194 DEF / 198 Spirit / 50 SPD.
- **The Unfinished World:** 78,000 HP / 304 ATK / 318 MAG / 226 DEF / 232 Spirit / 61 SPD.

The Unfinished World remains **78,000 HP**. Do not apply the old proposed 72,000/68,000 cuts.

Other named-enemy raw-stat tables remain preserved working data but must be re-certified against the dedicated current progression/enemy-level pass before being promoted as final master numbers.

---

# 10. Current progression / EXP high-level locks

The following are current design constraints even though detailed chapter bands remain open:

- **Chapter 0 grants no character levels.** It is level-static.
- Player level cap remains **70**.
- Chapters 1–7 should keep the party somewhat lower than a near-linear curve would suggest; a deliberate faster progression ramp begins **after Chapter 7**.
- Expected **Chapter 12 campaign-only clear target = Level 60**.
- The additional late-campaign EXP needed to reach that target should be distributed backward through the **Chapter 9 onward** campaign rather than dumped into one Chapter-12 spike.
- Enemy progression and EXP must be jointly balanced: ordinary enemies should become **stronger and worth more EXP from the start to the end of a chapter**, rather than using one flat chapter-wide enemy/EXP band.
- Old/weak enemies must award **substantially reduced EXP** to an overlevelled party.
- Fixed first-clear/completion EXP packages for authored Hunts/quests are not automatically reduced merely because the player is overlevelled; weak-enemy diminishing returns primarily govern repeatable enemy-kill EXP unless a reward explicitly says otherwise.

The exact current Chapter 1–13 player-level bands, enemy-level bands, encounter counts, per-formation EXP, and exact diminishing-return percentage table remain **deferred to the dedicated EXP rebalance**. Do not treat the v494–v503 exact chapter tables as final current canon.

---

# 11. Ordinary side-quest tracker correction

The cumulative tracker contains a stale v480–v493 side-quest reduction branch. Do not use that branch as current roster authority.

The current project snapshot retains the following ordinary Side Quests:

### Edda Harth — The Marks We Leave
- Greenhollow;
- unlock after Torren joins in Chapter 1;
- remains available through the normal returnable window;
- early route-welfare quest;
- low/zero required combat;
- reuses existing Chapter-1 spaces rather than creating quest-only map nodes.

### Edda Harth — When the Roads Open
- late sequel to The Marks We Leave;
- available in the **post-Vaelkor cleanup window (current Chapter 12)**;
- route-reopening / route-certification payoff.

### Talia Rell — The Third Caravan
- unlock after Chapter 8;
- route: **Greenhollow → Ashford**;
- authored sequence: Recovery Depot → Old Supply Cut → Failed Handoff → Temporary Shelter → Settlement Approach.

### Talia Rell — The Living List
- unlock after Chapter 10;
- Ashford anchor;
- authored sequence: Recovery Office → Temporary Quarter → Alderwick → Old Census Post.

Dialogue remains deferred until the dedicated dialogue phase. Reused enemies are legal with chapter-appropriate stats.

Older tracker statements removing When the Roads Open or The Living List are superseded by this current project correction.

---

# 12. Remaining open/deferred items surfaced by the tracker audit

The prior compact open-item audit missed several still-relevant dependencies. Current open/deferred items include:

1. **Exact current Base/Subclass Ability MP table** after the latest class-kit/class-name changes; preserve the higher-cost direction, but do not implement retired-name tables as final.
2. **Legacy elemental/status interaction requirement** from the post-Audit116 tracker: Relics have been reconciled, but the Legacy layer still needs an explicit decision whether elemental/status interaction remains a universal Legacy requirement or is replaced/partially replaced by the newer HP/MP/Accuracy/Evasion capstone-perk identity.
3. **Exact 17-Legacy raw stats + capstone perk assignments** from working v600 — pending user approval.
4. **Global Accuracy vs Evasion hit-resolution formula**.
5. **Universal Critical payout / resolution order**.
6. **Exact HP-consumable values** and **Emergency Rally** final revive/heal numbers.
7. **Exact Mastery Point grant total** after Synthesis removal leaves eight active Mastery nodes.
8. **Prismatic Deluge exact Power** if still unresolved by a later Prime-command pass.
9. The four Audit116 **Standard Card acquisition homes** still explicitly open: Restoration, Cinder Judgment, Iron Testament, Sunder the Gate.
10. **Detailed Ch1–13 EXP/enemy-level/encounter-count calibration**.
11. **Named enemy/boss raw-stat re-certification** where those values depend on the reopened progression curve; Final Archive Arbiter and The Unfinished World anchors above remain retained.
12. **Consumable shop timing/pricing and final currency denomination**.
13. **Kessara Relic-copy service fee/UI and exact physical pickup presentation** for some Forge/Legacy-project sources.
14. Final **Relic / Legacy / Legacy-Component / Forge-variant naming** remains deferred until dialogue/voice is sufficiently complete.
15. Side-quest line dialogue and exact final reward packages remain deferred.

---

# 13. Conflict order after Audit119

For affected domains:

1. **Audit119** — universal final-damage resolver, current Standard-Card/Prime MP costs, 21-consumable MP ladder, named resistance hierarchy, Prime scaling/control, progression directives, and the side-quest tracker correction explicitly stated here.
2. **Audit118** — exact ordinary/Relic catalog, Relic Traits/placements, settled Legacy Traits, Forge source matrix.
3. **Audit117** — class/equipment access structure, Synthesis removal, Legacy project architecture.
4. **Audit116** — compatible Standard-Card/Prime command identities/effects not changed by Audit119.
5. **Audit115** — compatible global statuses/elements/Ruin/class-Ability effects.
6. **Audit113** — current 13-chapter numbering.
7. compatible older authority where not superseded.

The historical cumulative tracker remains archival design history. Future working passes should use the consolidated current tracker rather than appending to the 165,000-line archive.