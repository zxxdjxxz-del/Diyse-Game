# Diyse — Audit115: Combat, Ruin, Status, and Full Class Ability Normalization Lock

**Master-canon version:** **v2.00 / Audit115**  
**Date:** August 25, 2026  
**Status:** **MASTER CANON — CONTROLLING**  
**Parent authority:** v1.99 / Audit114 plus all compatible older locks.  
**Purpose:** Promote the completed post-Audit114 combat/class cleanup into master canon, reconcile Ruin and harmful-status rules, remove obsolete effect systems, and lock the current Base/Subclass Ability–Trait–Ultimate packages for all six permanent characters.

Where this audit conflicts with Audit114 or an older working/class-rework file, **Audit115 controls**. Compatible older story, map, chapter, quest, equipment, Prime, progression, and production locks remain active.

---

## 1. Global combat formula lock

Every damaging Ability is authored as exactly one of:

- **Physical**
- **Magical**
- **Hybrid**

An Ability is Physical or Magical unless Hybrid is **deliberate and explicitly authored**.

- Equipment does not choose an Ability's formula.
- Learned Abilities remain weapon-independent once learned unless an individual Ability explicitly says otherwise.
- Element/affinity is separate from damage type.
- Non-Ruin Hybrid actions use their authored weights.
- Current intentional non-Ruin Hybrid examples include Axiomblade at **50% Attack / 50% Magic**, Routeweaver at **50% / 50%**, and Proofhunter **Held Argument** at **50% / 50%**.

### Ruin formula — controlling

**Ruin is a special magical affinity/school, not a fifth standard element.**

Whenever an Ability actually deals **Ruin damage**, its damage formula is:

> **Hybrid / Ruin — 75% Attack / 25% Magic**

This applies to Seyrik's Ruin Vanguard kit, Ilyra's Vowblade Ruin attacks, Ruin Warden Ruin attacks, and any later character Ability explicitly authored as Ruin damage unless a newer canon lock deliberately changes the universal Ruin formula.

Do not classify actual Ruin damage as pure Physical, pure Magical, 50/50 Hybrid, or 60/40 Hybrid.

---

## 2. Elements and harmful statuses

The standard element set remains exactly:

- **Fire**
- **Ice**
- **Lightning**
- **Earth**

Linked harmful statuses:

- Fire → **Burn**
- Ice → **Freeze**
- Lightning → **Stun**
- Earth → **Staggered**

Ruin's thematic harmful-status association is:

- Ruin → **Bleed**

Bleed is **not exclusive to Ruin**. A Physical or other non-Ruin Ability may explicitly inflict Bleed where authored.

An attack's element/affinity does not automatically apply a status. Every status rider must be explicit.

### Basic Attack status rule

The universal **Attack** command does **not** inflict Burn, Freeze, Stun, Staggered, Bleed, or any other harmful status by default.

A basic Attack may carry a harmful-status rider only when the currently equipped weapon/equipment explicitly grants that rider.

Class theme, Physical damage, elemental damage, Ruin affinity, or an equipped weapon's visuals do not silently grant status to basic Attack.

---

## 3. Current harmful-status baseline

Universal harmful statuses remain:

- Burn
- Freeze
- Stun
- Staggered
- Bleed

Regen remains a positive recurring-heal effect.

### Burn
- 3 rounds.
- Ordinary damage: **3% target Max HP** at end of each affected round.
- Reapplication refreshes duration.
- No crit, ignores defensive stats, can KO.

### Freeze
- Target cannot act.
- First 2 rounds guaranteed.
- 80% persistence check into round 3 and separately into round 4.
- Maximum 4 rounds.
- First successful direct Physical hit removes Freeze after the hit.
- Cannot refresh while active.

### Stun
- 3 affected turns.
- 40% action-loss chance on each affected turn.
- Cannot refresh while active.

### Staggered
- 3 rounds.
- Speed −20%.
- Accuracy/Base Hit −20%.
- Evasion −20%.
- Reapplication refreshes, never stacks.

### Bleed
- 2% Max HP when the affected unit successfully acts.
- Maximum one Bleed proc per round.
- Lost actions do not proc Bleed.
- Any successful HP heal restoring at least 1 HP removes Bleed after the heal.
- No stack, no crit, ignores defensive stats, can KO.

### Boss conversion
- Regional Hunt: Burn/Bleed deal 75% ordinary damage; Freeze max 2 rounds; Stun action-loss 25%.
- Major Hunt / mandatory boss: Burn/Bleed deal 50% ordinary damage; Freeze max 1 round; Stun action-loss 20%.
- Staggered remains legal where not explicitly immune.
- High-rank reduction does not imply blanket application immunity.

### Application bands
Default authored bands:
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

Vaelira receives her own qualifying **+5 percentage-point specialist bonus** when her Ability element matches the linked status.

Status Resistance:
- Normal 0
- Resistant 5
- Highly Resistant 10
- Exceptional 15
- Immune explicit

Ordinary application:
> Base + affinity modifier + Vaelira bonus − Status Resistance

Clamp legal ordinary chances to 5%–95% except explicit immunity, guarantee, or script.

---

## 4. Removed combat/effect systems — controlling

The following are removed from current global combat design and must not be recreated under renamed equivalents:

### Card Seals
Card Seals are removed completely:
- no Card-Seal state;
- no Card-Seal resistance;
- no Card-Seal cleanse;
- no Card-Seal immunity;
- no Card-Seal enemy category;
- no protection layer built around Card Seals.

### Rune effects
There is no global Rune-effect state/category, resistance, remedy, suppression layer, or direct-damage subsystem.

The word **Rune** may remain in a flavor/name such as **Siphon Rune**, but the name does not create a Rune mechanic.

**Rune** and **Ruin** are unrelated mechanically.

### Imprints
Imprints are removed completely:
- no application;
- no consume;
- no duration/refresh;
- no coexistence;
- no Imprint-triggered Composite Reaction;
- no mastery bridge;
- no substitute mark renamed to preserve the same system.

Any old Vaelira, Axiomblade, equipment, tutorial, UI, or Card dependency on Imprints is stale.

### Break/Stagger meter
There is no global Break meter or Stagger meter. **Staggered** is only the Earth-linked harmful status.

---

## 5. Non-status state firewall

The following are not universal harmful statuses:

- stat Up/Down effects;
- Fields;
- Guard / Barrier;
- Hunter's Measure;
- Prepared effects;
- class-internal short-duration setup states such as Crest Attunement or Tempered Mercy;
- protected/scripted encounter states.

Ordinary harmful-status remedies do not remove those states unless an effect explicitly says otherwise.

---

## 6. Fields

Fields remain valid globally as battlefield-attached temporary multi-round effects.

- Fields are not harmful statuses.
- Ordinary status remedies do not remove Fields.
- Explicit Field-removal effects may remove them.
- Source-specific replacement/extension rules apply.
- **Crest Arcanist has no Field Ability in its normalized kit.**
- **Routeweaver Crossroads is not a Field.**
- **Routeweaver Open the Way is a Field** and is Torren's intentional Routeweaver Field.

---

# 7. Base-class normalization — all six permanent characters

## 7.1 Cyanis — Crest Knight

- **Crest Strike** — CL1, one enemy, Physical / Neutral, no status.
- **Crest Reprisal** — CL1, Prepared self-intercept/counter, Physical / Neutral, no status.
- **Resonant Pulse** — CL1, one enemy, Magical / Colorless, no status.
- **Sweeping Edge** — CL3, all enemies, Physical / Neutral, **10% Bleed** per target.
- **Twin Advance** — CL6, one enemy, Physical / Neutral, exactly 2 hits, no status.
- **Crest Rend** — CL9, one enemy, Hybrid / Neutral, **35% Bleed**; exact Hybrid weighting/penetration remains a downstream numeric/formula detail.
- **Crest of Companions** — CL13, Magical / Colorless enemy damage with compatible established party cleanse/support structure; no harmful-status rider.

**Harmonized Crest** remains Cyanis's Base Trait unless separately revised.

## 7.2 Ilyra — Blue Warden

Ilyra's healing uses **Magic**, not Spirit.

- **Mend** — direct healing.
- **Clear Warding** — removes one eligible harmful status and retains authored Status Resistance Up as a stat change.
- **Renewal** — party healing; no automatic Regen.
- **Warden's Valor** — one enemy, Magical / Colorless direct offense; no old ally-Attack rewrite.
- **Revive** — revives at 35% Max HP under the current normalized package.
- **Lifeline** — Prepared KO-prevention survival effect; target is prevented from being KO'd, remains at 1 HP, then receives **18% Max HP + 0.80 Magic** recovery.
- **Gentle Continuance** — Regen **4% Max HP × 4 rounds**.
- **Dawn Without End** — Magical / Colorless enemy AoE plus compatible revive/heal/cleanse support and **5% Max HP Regen × 3 rounds**.

Ilyra's primary weapon family is **Wardrods**. Shield is a Secondary; Focus is also a legal Secondary option where current equipment rules permit it. No sword assumption is restored.

## 7.3 Torren — War Archer

- **Cinder Shot** — Physical / Fire, one enemy, **20% Burn**.
- **Quarry Appraisal** — establishes **Hunter's Measure**.
- **Watchful Aim** — Prepared Physical / Neutral reaction.
- **Pinning Strike** — Physical / Neutral with authored Speed Down.
- **Colossus Draw** — heavy Physical / Neutral hard-target attack.
- **Relentless Barrage** — Physical / Neutral multihit.
- **The Great Beast Falls** — heavy single-target Physical / Neutral capstone.
- Trait: **Veteran's Measure**.

Great Bows consume Weapon + Secondary under the current equipment rule.

## 7.4 Nimera — Cardweaver

- **Weave Bolt** — Magical / Colorless, one enemy.
- **Weave Guard** — ally direct-damage reduction 15% through end of following round; target's next Standard Card before expiry gains +10% eligible primary potency.
- **Weave Burst** — Magical / Colorless AoE.
- **Ancient Override** — 3-round Field; removes one hostile Field on creation; allies gain +10 Base Hit and +10 Status Resistance while active; only one Nimera-authored Field at a time.
- **Weave Spark** — Magical / Lightning, one enemy, **20% Stun**.
- **Sovereign Index** — one enemy, Magical / Colorless, **180 Power / 12 MP**; Indexed for 2 rounds; next hostile Standard Card receives 25% defensive-axis penetration, +15 Base Hit/application, and +20pp to one eligible authored chance-based secondary effect; consumes Indexed.
- **Grand Reweaving** — allies for 2 rounds; first Standard Card each round gains +20% eligible primary potency and +15pp to one eligible authored secondary chance.

Trait **Living Archive**:
- Rank I: first Standard Card each round +10% eligible primary potency plus current information-reveal behavior.
- Rank II: +10 Base Hit/application to that qualifying Card.
- Rank III: legal Prime activation restores 5% Max MP, max once per round.

Card Seals, Imprints, Face Concordance, and the old Unravel dependency do not return.

## 7.5 Vaelira — Green Arcanist

Vaelira's Base identity is direct elemental spellcasting and element/status specialization with no Imprint or Composite-Reaction engine.

Current normalized Ability spine:
- CL1 single-target **Magical / Ice**, standard-power attack, **20% Freeze** base; Vaelira specialist bonus makes 25% before other modifiers.
- CL1 single-target **Magical / Earth**, standard-power attack, **20% Staggered** base; specialist 25% before other modifiers.
- CL1 lower-power AoE **Magical / Fire**, **20% Burn** base; specialist 25%.
- CL3 stronger AoE **Magical / Lightning**, **20% Stun** base; specialist 25%.
- CL6 strong single-target Magical attack choosing one of Fire / Ice / Lightning / Earth; no status rider.
- CL9 powerful AoE Magical attack choosing one standard element; no status rider.
- CL13 **Arcanum Ascendant** — four sequential AoE Magical hits in order Fire → Ice → Lightning → Earth; no harmful-status riders.

Trait **Prismatic Flow**:
- Rank I: first damaging action each round whose element differs from Vaelira's previous damaging action gains +10% final damage; Colorless resets remembered element.
- Rank II: same qualifying action gains +10 Base Hit/application.
- Rank III: same qualifying action gains +15% Magic Defense penetration when Magical.

No Base Vaelira Imprints, Composite Reactions, marks, extra-action engine, or Base Field are active.

Exact final names for Vaelira's still-unnamed normalized Base elemental spells remain downstream naming work and are not to be backfilled from obsolete Imprint-era names automatically.

## 7.6 Seyrik — Ruin Vanguard

All actual Ruin damage below is **Hybrid / Ruin, 75% Attack / 25% Magic**.

- **Ruin Cleave** — CL1, one enemy, 165 Power / 4 MP, **20% Bleed**.
- **Rift Lance** — CL1, one enemy, 175 Power / 7 MP, **20% Bleed**.
- **Ember Brand** — CL1, Magical / Fire, one enemy, 150 Power / 8 MP, **20% Burn**.
- **Fracturing Brand** — CL3, AoE Hybrid / Ruin 75/25, lower Power than Rift Lance, **20% Bleed** per target; exact Power/MP remains final numeric-pass work.
- **Call Shardfang** — CL6, 18 MP, summons Shardfang for 3 rounds. Entry **Pounce** = 135 Hybrid / Ruin 75/25, no status. Autonomous **Rend** = 100 Hybrid / Ruin 75/25 against lowest-HP target, **20% Bleed**.
- **Unmaking Blow** — CL9, one enemy, Hybrid / Ruin 75/25, 25% applicable defensive-axis penetration; +15% final damage if target is already Bleeding; no built-in Bleed rider.
- **Controlled Apocalypse** — CL13, AoE Hybrid / Ruin 75/25, 360 Power, 25% applicable defensive-axis penetration; after damage applies Major Attack Down + Major Magic Down for 2 rounds and summons/empowers Shardfang under the authored capstone behavior.

Trait **Severed Command**:
- Rank I: authored Seyrik Base-Ability Bleed riders +5pp; does not affect universal Attack/equipment riders or Shardfang unless explicitly stated.
- Rank II: Shardfang +10 Base Hit.
- Rank III: Shardfang +10% final damage.

Seyrik joins at Base CL8 under the existing progression lock.

---

# 8. Subclass normalization — all six reciprocal subclasses

## 8.1 Cyanis — Crest Arcanist

Identity: Cyanis learns Vaelira's magical discipline through Crest spellcraft: Colorless Crest magic, elemental execution, anti-magic/dispel, and penetration. **No Field Ability exists in this normalized subclass kit.**

### Abilities
- **Arcane Lance** — CL1, one enemy, Magical / Colorless, **220 Power / 16 MP**, 25% Magic Defense penetration; after damage grants **Crest Attunement**.
- **Elemental Crest** — CL4, one enemy, Magical; choose Fire / Ice / Lightning / Earth; **180 Power / 12 MP**; no status, Field, or buff.
- **Nullifying Seal** — CL7, one enemy, Magical / Colorless, **175 Power / 19 MP**; if target has a removable positive buff, +25% final damage; after damage remove up to 2 removable buffs. The word Seal does not create a removed Card-Seal system.
- **Arcane Rupture** — CL9, all enemies, Magical / Colorless, **205 Power / 29 MP**; after damage remove 1 removable hostile Field and apply Magic Down for 2 rounds; exact magnitude deferred.
- **Elemental Convergence** — CL11, one enemy, Magical, four sequential hits Fire / Ice / Lightning / Earth, **240 total Power / 24 MP**; each hit resolves its own affinity; no status.
- **Crest Dominion** — CL13 Ultimate, all enemies, Magical / Colorless, **330 Power**, 35% Magic Defense penetration; after damage remove up to 2 removable buffs from each target and remove 1 hostile Field; no Field creation and no harmful status.

### Crest Attunement
Arcane Lance grants Crest Attunement after damage. It lasts through the end of the following round. The next **different Crest Arcanist Ability** used during that window consumes it and gains **+15 Base Hit/application**. One instance only; refreshes rather than stacks. It is not Prepared, a harmful status, a Field, or a gauge.

### Trait — Crest Resonance
- Rank I: MP-costing Crest Arcanist Abilities cost 2 less MP, minimum 1.
- Rank II: damaging Magical / Colorless Crest Arcanist Abilities gain +15% Magic Defense penetration.
- Rank III: consuming Crest Attunement grants +10% final damage to that Ability.

### Accepted Mastery
- **Arcane Force** — Subclass Mastery Node 1, eligible CL3, cost 1 MP: **Arcane Lance +20 Power** (220 → 240). No other change.

Older Warding Crest / Dominion Crest Field / Card-Seal / Rune-resistance text is superseded. Remaining Crest Arcanist Mastery nodes still require dedicated cleanup; do not silently reuse stale Warded Ground mechanics.

## 8.2 Vaelira — Axiomblade

All intentional Hybrid damage below is **50% Attack / 50% Magic** unless an individual two-hit split explicitly states otherwise.

- **First Principle** — CL1, one enemy, Hybrid / Neutral, **150 Power / 6 MP**, 50/50.
- **Proven Advance** — CL4, one enemy, Hybrid / Fire, **165 Power / 8 MP**, 50/50, **20% Burn**; after damage Defense Up + Magic Defense Up for 2 rounds; magnitude deferred.
- **Counterproof** — CL7, one enemy, Hybrid / Lightning, **190 Power / 10 MP**, 50/50, +15 Base Hit, **20% Stun**; ordinary selected Ability, not Prepared.
- **Axiom Rend** — CL9, one enemy, Hybrid / Neutral, **225 Power / 13 MP**, 50/50; 30% Defense penetration on Attack half and 30% Magic Defense penetration on Magic half.
- **Equivalent Form** — CL11, one enemy, Hybrid / Neutral, **16 MP**; two hits: 120 Physical Attack-vs-Defense then 120 Magical Magic-vs-Magic-Defense, 240 total; no status.
- **Final Axiom** — CL13 Ultimate, all enemies, Hybrid, choose one standard element, **320 Power**, 50/50; 25% Defense penetration on Attack half and 25% Magic Defense penetration on Magic half; no status or Field.

Trait **Formal Equivalence**:
- Rank I: dealing single-standard-element damage stores that element through end of following round. The next Neutral damaging Axiomblade Ability adopts and consumes it. Authored elemental Abilities are not overwritten. New qualifying element replaces old; multi-element damage does not establish.
- Rank II: consuming Formal Equivalence grants +10% final damage.
- Rank III: consuming grants +15% Defense penetration to Physical/Attack portions and +15% Magic Defense penetration to Magical/Magic portions.

No Imprints, Prepared Thread, Field engine, or renamed Imprint substitute exists.

## 8.3 Ilyra — Vowblade

Identity: Ilyra learns Seyrik's Ruin Vanguard survival/offense discipline while retaining mercy and sustain.

All actual Ruin attacks are **Hybrid / Ruin, 75% Attack / 25% Magic**.

- **Vital Edge** — CL1, one enemy, 185 Power / 8 MP; after damage self-heal 15% of eligible HP damage dealt; no automatic Bleed.
- **Mercy Returned** — CL4, one enemy, 215 Power / 10 MP; after damage heal the other conscious ally with lowest HP% for **12% target Max HP + 0.90 Ilyra Magic**; stable-slot tie; no Bleed.
- **Living Covenant** — CL7, self, 18 MP; stance action lasting 3 full following rounds beginning next round; Vowblade direct damage restores an additional 15% of eligible HP damage. No status, Barrier, Regen, or interruption-resistance subsystem.
- **Vowkeeper's Reprisal** — CL9, one enemy, 235 Power / 12 MP; if that enemy damaged at least two conscious allies in the previous round, +20% final damage and heal one qualifying affected ally with lowest HP for **10% Max HP + 0.75 Magic**. Not a reaction/Prepared Ability.
- **Vow of Severance** — CL11, all enemies, 210 Power / 22 MP, **20% Bleed** per target; 20% Defense penetration on Attack share and 20% Magic Defense penetration on Magic share; after damage Defense Down + Magic Defense Down for 2 rounds; magnitude deferred.
- **Mercy's Final Edge** — CL13 Ultimate, one enemy, **520 Power**, 40% Defense penetration on Attack share and 40% Magic Defense penetration on Magic share; after damage Ilyra restores 30% of eligible damage dealt; all other conscious allies heal **10% Max HP + 0.75 Magic**; all conscious allies gain 15% direct-damage reduction through end of following round. No Bleed, revive, Barrier, cleanse, self-damage, or execute rider.

Trait **Mercy in Steel**:
- Rank I: when a Vowblade Ability heals a conscious ally other than Ilyra, gain **Tempered Mercy** through end of following round. Next damaging Vowblade Ability consumes it for +10% final damage. Self-heal alone does not establish it.
- Rank II: consuming also grants +10 Base Hit, +10% Defense penetration to Attack/Physical share, and +10% Magic Defense penetration to Magic/Magical share.
- Rank III: if the empowered Ability hits a target already Bleeding, +10% additional final damage against that target.

## 8.4 Seyrik — Ruin Warden

Identity: Seyrik learns Ilyra's preservation discipline through Ruin logic. Healing scales from **Magic**.

- **Siphon Rune** — CL1, one enemy, Hybrid / Ruin 75/25, **165 Power / 8 MP**; self-heal 35% eligible HP damage, capped at 20% Seyrik Max HP; no automatic Bleed. “Rune” is flavor only.
- **Stolen Grace** — CL4, one enemy, Magical / Colorless, **170 Power / 10 MP**; after damage automatically heal the other conscious ally with lowest HP% for **30% eligible damage + 0.35 Magic**, capped at 25% target Max HP; stable-slot tie.
- **Restoring Ward** — CL7, one conscious ally, **10 MP**; heal **18% target Max HP + 0.90 Magic**, remove one harmful status, and grant +10 Total Defense through end of following round.
- **Withering Mercy** — CL9, all enemies, Magical / Earth, **150 Power / 18 MP**, **20% Staggered**; no cooldown. After all damage, create a recovery pool equal to 12% of total eligible HP damage and divide evenly among conscious permanent allies including Seyrik; each ally capped at 15% Max HP; blocked excess is not redistributed.
- **Reclaimed Breath** — CL11, **24 MP**, revive one KO permanent ally at 25% Max HP; no summons/devices/constructs/Prime.
- **Mercy Through Ruin** — CL13 Ultimate, all enemies plus conscious allies: enemy damage Hybrid / Ruin 75/25, **320 Power**; after damage allies heal **25% Max HP + 1.00 Magic**, cleanse one harmful status, and gain +20 Total Defense for 2 rounds; no Bleed, revive, Barrier, Regen, or Drain rider.

Trait **Ruin's Mercy**:
- Rank I: when Seyrik actually restores HP to himself through authored Drain, heal the other conscious ally with lowest HP% for 15% of the HP actually restored to Seyrik.
- Rank II: share 15% → 25%.
- Rank III: whenever a Ruin Warden Ability restores HP to a conscious ally, that ally gains +10 Status Resistance through end of following round; refreshes, does not stack. Revival itself does not trigger it. Self-only Drain does not grant Seyrik the buff unless another effect heals him as an ally target.

## 8.5 Torren — Routeweaver

Identity: Torren learns Nimera's Cardweaver/Conduit tactical logic into practical routing, hybrid pressure, selective Card support, and one intentional Field. No gauge.

Intentional Hybrid attacks use **50% Attack / 50% Magic** unless separately authored.

- **Throughline** — CL1, one enemy, Hybrid / Neutral, **160 Power / 7 MP**, 50/50; +10 Base Hit vs Hunter's Measure; no apply/consume.
- **Clear Route** — CL4, one conscious ally, **10 MP**; remove one harmful status and grant +10 Speed for 2 rounds; no heal, Barrier, Regen, Prepared, or Field.
- **Crossroads** — CL7, all conscious allies, **16 MP**, choose one:
  - Forward Route: +10 Base Hit and +10 Speed for 2 rounds.
  - Covered Route: +15 Total Defense for 2 rounds.
  Crossroads is **not a Field**.
- **Covered Crossing** — CL9, one conscious ally, **15 MP**; 15% direct-damage reduction through end of following round; target's next Standard Card before expiry gains +10% eligible primary potency; consumed/expiry; no Field or extra Card action.
- **Frozen Passage** — CL11, all enemies, Magical / Ice, **215 Power / 22 MP**, **20% Freeze** per target; no Measure or Field rider.
- **Open the Way** — CL13 Ultimate: creates a **3-round Route Field**. While active, all conscious allies gain +15 Speed, +10 Base Hit, and 10% direct-damage reduction. The first Standard Card used by each conscious ally during the Field gains +10% eligible primary potency once for that ally. No extra Card action, heal, Barrier, harmful status, or Prepared rider.

Trait **Route Weaving**:
- Rank I: after Torren uses a Standard Card, his next damaging Routeweaver Ability before end of following round gains +10% final damage; one stored, refresh no stack.
- Rank II: after any Routeweaver Ability, Torren's next Standard Card before end of following round gains +10 Base Hit/application where relevant; one stored, refresh no stack.
- Rank III: Open the Way base duration increases **3 → 4 rounds**.

## 8.6 Nimera — Proofhunter

**Subclass name:** **Proofhunter**.  
The old subclass name **Truthshot is superseded** and is not current canon.

Identity: Nimera learns Torren's War Archer discipline through Cardweaver/Conduit execution: target assessment, Hunter's Measure, evidence/proof language, precision, interruption, mobility control, hard-target exploitation, and elemental ranged pressure.

Great Bow presentation is literal when equipped; otherwise the learned Ability may manifest/project the bow through Nimera's legal Conduit/manifold presentation. Mechanics are unchanged by weapon.

### Abilities
- **Measured Shot** — CL1, one enemy, Physical / Neutral, **120 Power / 6 MP**; on hit applies **Hunter's Measure for 2 rounds**. If Diysean Appraisal already revealed permitted target data, +10 Base Hit. No Appraised state, Imprint, or new mark.
- **Held Argument** — CL4, one enemy, **Hybrid / Colorless**, **150 Power / 8 MP**, intentional **50% Attack / 50% Magic**. Ordinary selected Ability, **not Prepared**. If target has an eligible Interruptible action queued and unresolved that round, Held Argument may interrupt it using the authored interrupt chance. Against Hunter's Measure: +10 Base Hit and +15 percentage points to the authored interrupt chance. If no eligible action is pending, it simply deals damage. Exact universal interrupt base chance/terminology remains downstream resolver work.
- **Pin the Variable** — CL7, one enemy, Physical / Neutral, **145 Power / 9 MP**; on hit Speed Down for 2 rounds and **15% base Bleed chance**. Against Hunter's Measure: **10% Defense penetration**. Does not consume Measure.
- **Structural Failure** — CL9, one enemy, Physical / Neutral, **210 Power / 12 MP**, **35% Defense penetration**. Against an explicitly authored structural target (components, devices, wards, constructs, equivalent tags): +15% final damage. Against Hunter's Measure: +10 Base Hit. No status.
- **Corroboration** — CL11, all enemies, **Physical / Fire**, **195 Power / 18 MP**, one direct AoE hit per enemy, **15% base Burn chance** per target. Against an individual measured target: +10 Base Hit and 10% Defense penetration. Does not consume Measure. The old 4-hit single-target Corroboration is superseded.
- **Final Annotation** — CL13 Ultimate, one enemy, Physical / Neutral, **360 Power**, +20 Base Hit, **50% Defense penetration**, **20% base Bleed chance**. Against Hunter's Measure: +20% final damage. Against an authored large / Hunt / structural hard-target category: +15% final damage. Both damage bonuses may apply together. Does not consume Measure.

### Trait — Applied Evidence
- Rank I: damaging Proofhunter Abilities gain +10 Base Hit against Hunter's Measure.
- Rank II: additionally +10% Critical Chance against Hunter's Measure.
- Rank III: additionally +15% applicable defensive-axis penetration against Hunter's Measure:
  - Physical → Defense penetration.
  - Magical → Magic Defense penetration.
  - Hybrid → Defense penetration on Attack/Physical share and Magic Defense penetration on Magic/Magical share.

Applied Evidence stacks with explicitly authored penetration on Proofhunter Abilities.

At full Trait rank against Hunter's Measure, **Final Annotation** reaches:
- +30 Base Hit total;
- +10% Critical Chance;
- 65% Defense penetration;
- +20% final damage;
- 20% base Bleed chance;
plus its separate +15% final damage when the target also qualifies as large / Hunt / structural hard target.

---

# 9. Prepared effects after normalization

Known current Prepared generators in the normalized character Ability packages are:

1. Cyanis — **Crest Reprisal**
2. Ilyra — **Lifeline**
3. Torren — **Watchful Aim**

**Held Argument is not Prepared.**  
**Counterproof is not Prepared.**  
No removed Prepared Thread state exists.

The existing one-armed Prepared-effect limit remains where compatible.

---

# 10. Progression architecture retained

- Base Class cap = CL13.
- Subclass cap = CL13.
- Sixfold **Volition** unlocks all reciprocal Subclasses.
- Base/Subclass pairs:
  - Cyanis — Crest Knight / Crest Arcanist
  - Vaelira — Green Arcanist / Axiomblade
  - Ilyra — Blue Warden / Vowblade
  - Seyrik — Ruin Vanguard / Ruin Warden
  - Torren — War Archer / Routeweaver
  - Nimera — Cardweaver / Proofhunter
- Learned Abilities remain weapon-independent.
- Selected class controls its stat package and Trait.
- Mastery architecture remains 4 Core + 4 Subclass + 1 Synthesis, each costing 1 Mastery Point.
- Subclass Mastery Node 4 remains Equipment Mastery at CL10, unlocking donor Relic access.
- Synthesis remains Base CL13 + Subclass CL13 + all eight prior Masteries + authored resolution + 1 MP.
- Level cap remains 70.

---

# 11. Explicitly open/deferred work after Audit115

Audit115 promotes the Ability / Trait / Ultimate normalization and global combat cleanup. The following remain later work unless separately locked:

1. exact Weak/Resist damage multipliers;
2. Absorb existence;
3. broad enemy affinity-profile distribution;
4. final exact Power/MP values still explicitly deferred above;
5. Cyanis Crest Rend final Hybrid weight/penetration;
6. final names for Vaelira's currently unnamed normalized Base elemental spells;
7. final magnitude values for several authored stat Up/Down effects;
8. exact universal interrupt base chance/terminology for Held Argument and other interruptible actions;
9. complete Subclass Mastery cleanup beyond accepted **Arcane Force**;
10. Core Mastery cleanup where stale removed systems remain;
11. final selected-class stat packages where prior Spirit-era or stale packages need normalization;
12. equipment-progression text cleanup where older specs still reference removed mechanics;
13. Standard Card / Prime / equipment dependency sweeps for Card Seals, Rune effects, Imprints, old Break/Stagger contribution, Water/Wind standard elements, and other stale terminology;
14. implementation and regression tests.

The proposed Crest Arcanist Mastery **Elemental Discipline** is **not promoted by Audit115 unless separately approved**; it remains working design.

---

# 12. Supersession / repository synchronization rule

After Audit115:

- `docs/COMBAT_RULES.md` must cite Audit115 as controlling combat authority.
- `docs/ACTIVE_CANON.md` must identify v2.00 / Audit115 as current whole-project authority.
- The six reciprocal Subclass working specs must be synchronized to the normalized Ability/Trait/Ultimate packages in this audit and may remain implementation/detail companions, but **Audit115 controls conflicts**.
- Any file that still treats Truthshot, Imprints, Card Seals, Rune effects, Warding Crest Field, Crossroads Field, Held Argument Prepared, Counterproof Prepared, 50/50 Ruin, 60/40 Ruin, or basic-Attack implicit Bleed/status as active is stale.
- Compatible older chapter/map/story/quest/equipment locks remain active.

**Audit115 is the controlling master-canon promotion for the completed post-Audit114 combat and class-normalization pass.**
