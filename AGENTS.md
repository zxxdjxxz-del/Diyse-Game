# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code or production content, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/chapters/README.md`
4. the relevant current chapter file under `docs/chapters/`
5. the latest controlling canon audit for the subject
6. `docs/PRESENTATION_RULES.md`
7. the relevant subsystem document
8. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before dialogue Resource work
9. `docs/TECHNICAL_PROOF.md` only as compatible historical engineering evidence

If a task conflicts with these files or a newer explicit user instruction, stop and surface the conflict. Do not silently reinterpret canon.

## Current authority state

- Whole-project written authority: **Diyse v2.07 / Audit122**.
- Current Base Hit/Evasion + Bleed runtime authority: `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`.
- Current systems/item/equipment/progression reconciliation: `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`.
- Current Critical/direct-damage authority: `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md` where compatible with Audit121/Audit122.
- Compatible combat/resource/Prime/progression authority: `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`.
- Exact ordinary/compatible Relic/Forge numerical catalog: `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`.
- Equipment/Legacy/class-access structure: `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md` where compatible.
- Compatible Card/Prime command authority: `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`.
- Compatible status/element/Ruin/class-Ability authority: `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md` where compatible with Audit122 Bleed.
- Current chapter-number reconciliation: `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`.
- Current world-map / region authority remains the compatible Audit111 chain plus Audit121 place-name corrections.
- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level; Audit121 controls the Chapter-4 four-element mechanical reconciliation.
- HD-2D is the sole active presentation target.

Historical audit filenames and trackers remain provenance, not automatic current authority.

---

## Current combat firewall — Audit122 / Audit121 / Audit120

### Direct damage / Critical Hits

Physical direct damage:

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

Magical direct damage:

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

- Physical = Attack vs Defense.
- Magical = Magic vs Spirit.
- Character-Ability Ruin remains 75% Attack / 25% Magic where compatible Audit115 rules apply.
- Same-axis penetration adds in percentage points and caps at **75%**.
- No cross-axis penetration transfer.
- No hidden universal AoE penalty.
- No universal random damage variance.
- Basic Attack = 100 Power / Physical / Neutral unless equipment explicitly changes affinity.

Critical rules:
- base Critical Chance = **5%**;
- Critical bonuses are flat percentage-point additions;
- ordinary random Critical Chance cap = **50%**;
- eligible Critical multiplier = **1.5×**;
- resolve Base Hit/Evasion before Critical Chance;
- a miss gets no Critical roll;
- each authored direct hit in a multihit action rolls independently by default;
- one authored Hybrid hit uses one Critical roll on its combined eligible direct damage;
- eligible Magical direct hits use the same 1.5× multiplier;
- Critical does not bypass Defense/Spirit;
- Critical does not automatically improve harmful-status application;
- Burn, Bleed, explicitly no-Crit copied/echo damage, indirect Max-HP damage unless explicitly authored otherwise, and healing cannot Crit.

Use **Base Hit**, never `Accuracy`, as the current hit-stat term.

### Removed combat systems

- **Barrier does not exist.** Do not implement or preserve Barrier wording/effects.
- **Brace does not exist.**
- There is **no global Break/Stagger meter**.
- **Staggered** is only an ordinary harmful status where authored.
- **Guard** remains valid.

### Base Hit / Evasion — Audit122

There is no natural Accuracy stat.

> **AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers**

> **EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers**

> **FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)**

Normal authoring: ~100 standard, 90–95 heavy, 105–115 precision, exceptional up to ~120. Hit/Evasion, Critical, and harmful-status application are separate.

### Bleed — Audit122

Bleed damages each round and again when the affected character acts. The old one-proc-per-round rule is superseded. Bleed clears only on full-HP restoration, an eligible harmful-status clear, or an eligible item. Partial healing/Regen does not clear it unless full HP is reached or a valid status clear is explicitly included.

### Standard Cards

Exactly 24 Standard Cards; maximum 3 equipped per character.

Cards are reusable and MP-consuming. Do not implement a charge/deck/draw/discard/duplicate/rank system.

Current Card MP range remains **18–48 MP** under Audit119/Audit121 compatibility.

Current Acuity quartet:
- Faultline Sight
- Measured Response
- Predicted Impact
- Decisive Interval

Predicted Impact = Magical/Colorless, Power 180, Base Hit 110, 28 MP, 30% Stun on successful damaging hit, with no Break/Stagger-meter rider.

### Primes

Progression:

> **Recovered → Awakened**

Current Invocation MP:
- Recovered Story — 50 MP
- Awakened Story — 80 MP
- Awakened Major Hunt — 90 MP
- manifested commands — 0 additional MP

Awakened Primes replace/suspend the party for exactly 3 Prime rounds, then trigger the shared 3-full-normal-round cooldown. Prime use remains once per identity per battle / genuine fresh-HP form.

No Prime XP, levels, duplicates, or upgrade-material progression.

Audit121 numeric sync:
- Prismatic Deluge = 4 elemental waves × 90 Power = **360 total listed Power per target**.
- Regulator Fang = **250 Power / 25% Spirit penetration**, choose Fire/Ice/Lightning/Earth, no harmful-status rider.

---

## Current class / Mastery architecture

Permanent six:
- Cyanis — **Crest Knight / Crest Arcanist**
- Ilyra — **Blue Warden / Vowblade**
- Torren — **War Archer / Routeweaver**
- Nimera — **Cardweaver / Proofhunter**
- Vaelira — **Green Arcanist / Axiomblade**
- Seyrik — **Ruin Vanguard / Ruin Warden**

Faces:
- Cyanis — Might
- Ilyra — Grace
- Torren — **Acuity**
- Nimera — Change
- Vaelira — Elements
- Seyrik — Ruin

Base and Subclass caps are both **CL13**.

No permanent character uses a Subclass before Sixfold Volition at the end of Chapter 7.

**Synthesis is removed.** Never implement a Synthesis Mastery, Synthesis cost/passive, Base+Subclass cap gate, or duplicate shared Legacy artifact.

Exactly **8 active Mastery nodes** remain:
- 4 Core
- 4 Subclass

Eligibility:
- Core: Base CL3 / 6 / 9 / 12
- Subclass: CL3 / 5 / 7 / 11
- purchase Subclass Mastery 3 at CL7 → donor Relic access
- purchase Subclass Mastery 4 / Legacy Mastery at CL11 → donor Legacy access

Donor pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

Linked donor use equips the donor's actual obtained item. No duplicate artifact. Trait travels with the item. No universal off-owner nerf.

A character's own native Legacy does not require Synthesis or donor Legacy Mastery.

### Open progression work

- Full CEXP redo is still required.
- Final class Ability MP check/certification is still required.
- Exact 8-point Mastery Point schedule is still open.
- Normal full class completion should occur around **player Lv62**.
- The Lv5/10/15/20/Volition/40/50/60 MP schedule is simulation-only until the progression pass closes.

Do not treat an existing class-Ability MP table as final certification merely because working costs exist.

---

## Equipment / Relic / Legacy firewall

Current active catalog:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- **91 total**

Hierarchy:

> **Ordinary < Relic < Legacy**

Exact 38/38 ordinary-equipment source/numeric architecture remains closed under Audit118.

Audit121 locks all **17/17 native Legacy** raw stats, perks, and Traits and the listed Relic cleanup deltas.

Slot rules:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik Two-Handed Sword — Weapon + Secondary.
- Nimera ordinary/surviving Relic Conduits — one-slot.
- Nimera native Legacy Conduit — Weapon + Secondary.

Native Legacy completion retains the compatible Base/Character Quest/component/precursor/Gate-A/Gate-B/Kessara requirements. Native Legacy does not require Synthesis.

Linked donor access uses the donor's actual obtained item; no separate shared artifact is created.

Relic copies remain limited to one forged duplicate after the original is obtained. Legacies remain unique.

No equipment may depend on Barrier, Brace, or a global Break/Stagger meter.

---

## Consumables / economy firewall — Audit121

Current Consumable count = **20**.

Currency = **Auren**; **1 economy unit = 20 Auren**.

HP Salves:
- Field 250 HP / 20 Auren
- Restorative 750 HP / 50 Auren
- Vital 1,500 HP / 120 Auren
- Grand 2,250 HP / 240 Auren
- Company 30% Max HP to all conscious active-party members / 200 Auren

MP:
- Flow 50 MP / 80 Auren
- Deepflow 80 MP / 200 Auren
- Highflow 120 MP / 360 Auren
- Reservoir 75% Max MP / reward-only / 640 Auren equivalent

Revival:
- Rousing Salts 25% Max HP / 60 Auren
- Greater Rousing Salts 50% Max HP + 25% Max MP / 160 Auren

Other normal stock:
- Trauma Remedy — Burn/Bleed / 15 Auren
- Stability Remedy — Freeze/Stun/Staggered / 15 Auren
- General Remedy — one eligible ordinary harmful status / 50 Auren
- Full Remedy — all eligible ordinary harmful statuses / 140 Auren
- Blinding Mist — eligible ordinary random-encounter escape / 10 Auren
- Null Seal — one eligible enemy positive effect / 70 Auren
- Balance Seal — ordinary negative stat changes toward normal / 60 Auren

Reward-only:
- Emergency Kit — 75% Max HP + 60% Max MP + established eligible cleanse/stat restoration; no revive / 300 Auren equivalent
- Emergency Rally — revive all unconscious active-party members at 60% Max HP + 35% Max MP; no cleanse/stat restoration / 500 Auren equivalent

Do not use the old 21-consumable count or old 250/600/1200 HP ladder.

---

## Commerce / place-name firewall

Current Regional Markets:
- Brackenwall
- Dunmere
- Caelora
- Ivorybridge
- Stonewake
- Frostmere
- **Westguard**
- Larkspire
- Cerythvale

**Westguard** replaces Westreach and Yahtrens Stand.

Greenhollow, Ashford, Veycross, Deepforge, and Emberforge are not Regional Markets.

Cresthaven Quartermaster remains the full normal-stock consolidation/requisition endpoint.

Vhalmarch is forward supply/requisition after capture, not a civilian Regional Market.

---

## Chapter 4 elemental firewall

Chapter 4 uses exactly:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed from the Chapter-4 regulation/research framework and their old functions are not reassigned.

The Seventh Reaction is emergent four-element behavior, not a seventh element or reusable player system.

Reaction Conduit replaces Elemental Hexarch and uses only the four standard elements.

Regulation Crucible uses four chambers with two active/targetable at once and the locked rotation Fire/Ice → Lightning/Earth → Fire/Lightning → Ice/Earth. Former Wind speed inheritance and Water Barrier/restoration/stabilization inheritance are removed.

Cinder Judgment comes from the Reaction Annex/regulation-system protected cache.

---

## Progression / enemy balance firewall

- Player level cap = 70.
- Chapter 0 grants no character levels.
- Chapters 1–7 intentionally sit somewhat below a near-linear curve.
- Faster level gain begins after Chapter 7.
- Full class progression should be about to max around **player Lv62**.
- Detailed Ch1–13 player bands, enemy bands, encounter counts, formation EXP, CEXP, Mastery cadence, and diminishing-return percentages remain open for the dedicated progression redo.

Do not implement old exact progression tables as final current values.

---

## Post-insertion chapter-number firewall

The game has Chapter 0 plus Chapters 1–13.

Current late-game numbering:
- Chapter 10 — **The Last Blank**
- Chapter 11 — **Crown Engine**
- Chapter 12 — **The Reforged March**
- Chapter 13 — **The Last Command**

Historical translation:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Never implement the pre-insertion late-game numbering.
