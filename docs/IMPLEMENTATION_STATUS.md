# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.20 / Audit135**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapter 4 four-element S022–S026 script/dialogue-runtime synchronization is complete.
- Shared HD-2D runtime foundation remains implemented.
- **Audit135** closes all 6 Major-Hunt recommended levels and raw body stats; Crownless Siege Marshal → Crownless War Engine is a genuine fresh-body fight, and The Unfinished World remains one continuous 78,000-HP superboss bar.
- **Audit134** closes all 11 Regional-Hunt recommended levels and raw body stats; Throne of Emperor Vaelkor is recertified as Sealed Throne → fresh Walking Throne, total 26,000 body HP.
- **Audit133** closes numbered-chapter optional Elite raw stats: 12 current Elites, no approved Ch10 optional Elite.
- **Audit132** closes Chapters 9–13 mandatory named/special raw combat stats and completes the mandatory-story raw-stat layer for all 13 chapters.
- **Audit131** closes Chapters 5–8 mandatory named/special raw combat stats.
- **Audit130** corrects Regulation Crucible Form-I HP to 2,400.
- **Audit129** closes compatible Chapters 1–4 mandatory named/special raw combat stats.
- **Audits126–128** close exact mandatory named/story EXP+CEXP placement for all 13 chapters.
- **Audit125** closes mandatory ordinary-vs-authored EXP allocation and formation CEXP bands.
- **Audit124** closes optional player EXP and the pre-Last-Shelter Lv70 completionist proof.
- **Audit123** closes class Ability MP certification, 6,000-CEXP CL13 curve, exact 8-point Mastery schedule, player-level spine and chapter EXP budgets.
- **Audit122** closes Base Hit/Evasion and current Bleed runtime.
- **Audit121** supplies current system removals, classes/Faces, equipment/items, Chapter-4 four-element reconciliation and Prime numeric sync.

---

# Combat guardrails

Physical:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Same-axis penetration cap = 75%. Spirit is magical defense. Hybrid components resolve independently.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

Status Resistance = 0 Normal / 5 Resistant / 10 Highly Resistant / 15 Exceptional; immunity explicit only. There is no natural Accuracy stat.

Barrier and Brace do not exist. There is no global Break/Stagger meter. Staggered is an ordinary harmful status. Guard remains valid.

Bleed damages each round and whenever the affected character acts; it clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

Genuine fresh-HP boss forms refresh Prime availability. Same-bar changes do not.

---

# Current classes / progression

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Base/Subclass cap = CL13. No permanent Subclass use before Sixfold Volition at end Ch7. Synthesis is removed. Ability MP is CLOSED under Audit123.

CL13 = **6,000 cumulative CEXP**. Exactly 8 automatic Mastery Points: Lv5, Lv10, Lv15, Lv20, Sixfold Volition, Lv40, Lv50, Lv60.

Player-level anchors:
- Ch1 5 / Ch2 9 / Ch3 13 / Ch4 17
- Ch5 22 / Ch6 27 / Ch7 32 / Ch8 37
- Ch9 42 / Ch10 47 / Ch11 52 / Ch12 57
- **Last Shelter 60**
- **normal ending 62**
- cap 70

Normal full Base + Subclass Class-Level completion occurs during Ch12, with Seyrik around end Ch12.

---

# Reward / progression implementation

Pre-Last-Shelter authored optional pool = **195,000 EXP**. Major Hunt #6 is excluded from the cap proof.

Expected ordinary encounter center = **225 total**, planning centers not quotas. Chapter 4 remains 19 expected random encounters / 5,262 ordinary EXP / 11,200 total EXP.

Exact mandatory named/story placement is CLOSED for all chapters under Audits126–128.

Optional Elites/Hunts/quests do not consume mandatory chapter pools. Same-bar changes pay once. Fresh-HP multi-form bosses pay one combined package after final form. Fixed authored packages are exempt from ordinary lower-level enemy EXP diminishing returns. No separate CEXP diminishing-return system.

Ch13 true PONR = **Last Shelter → Reactor Galleries**. Final boss = exactly Reconstituted Entity → The Last Command, two genuine full-HP forms, no third form.

---

# Current raw-stat state

Mandatory named/special raw body stats are CLOSED for all chapters under Audits129–132.

Optional Elite raw stats are CLOSED under Audit133:
- 12 current numbered-chapter Elites;
- no approved Ch10 Elite;
- typical duration ~2–4 serious party rounds.

Regional Hunt raw stats are CLOSED under Audit134:
- recommended levels = **7 / 11 / 15 / 20 / 26 / 32 / 38 / 44 / 50 / 56 / 61**;
- recommendations are preparedness targets, not access gates;
- Hunts #1–10 retain recovered raw lines;
- Hunt #11 Throne of Emperor Vaelkor:
  - Sealed Throne — Lv61, **11,800 HP**, 228 ATK / 234 MAG / 172 DEF / 168 Spirit / 50 SPD / EVA0 / SR10;
  - Walking Throne — Lv62, **14,200 HP**, 240 ATK / 221 MAG / 166 DEF / 159 Spirit / 58 SPD / EVA0 / SR10;
  - total body HP **26,000**;
  - genuine fresh-form Prime refresh;
  - no Attendant HP pools invented;
  - no third form.

Major Hunt raw stats are CLOSED under Audit135:
- Ashen Whitehorn — Lv22, **11,270 HP**, 96 ATK / 78 MAG / 73 DEF / 68 Spirit / 38 SPD / EVA10 / SR10;
- Crownless Siege Marshal — Lv28, **9,360 HP**, 124 ATK / 92 MAG / 90 DEF / 78 Spirit / 35 SPD / EVA5 / SR10;
- Crownless War Engine — Lv29, fresh **11,650 HP**, 139 ATK / 102 MAG / 99 DEF / 86 Spirit / 33 SPD / EVA0 / SR10; combined **21,010 HP** and fresh-form Prime refresh;
- Concordance Guardian — Lv35, **18,180 HP**, 146 ATK / 151 MAG / 115 DEF / 118 Spirit / 40 SPD / EVA5 / SR15;
- Worldscar Leviathan — Lv47, **30,200 HP**, 187 ATK / 207 MAG / 148 DEF / 156 Spirit / 44 SPD / EVA0 / SR10;
- Final Archive Arbiter — Lv58, **43,100 HP**, 229 ATK / 244 MAG / 194 DEF / 198 Spirit / 50 SPD / EVA5 / SR15;
- The Unfinished World — Lv70, **78,000 HP**, 304 ATK / 318 MAG / 226 DEF / 232 Spirit / 61 SPD / EVA0 / SR15;
- The Unfinished World remains one continuous WORLDFRAME → WORLDHEART EXPOSED → FINAL CONSTRUCTION bar with no Prime refresh between those states;
- only Earth/Staggered, Ice/Freeze, Lightning/Stun, Fire/Burn remain in its world-state matrix.

Current challenge hierarchy:
> **Ordinary < Elite < mandatory story boss < Regional Hunt < Major Hunt**

Progression-dependent named/boss raw-stat recertification is now CLOSED across all audited encounter layers.

---

# Equipment / Cards / Chapter 4

- equipment = 38 ordinary + 36 Relics + 17 Legacies = 91
- consumables = 20
- Standard Cards = 24
- Primes = 12, Recovered → Awakened only
- Prime Invocation MP = 50 / 80 / 90
- Ch4 uses exactly Fire / Ice / Lightning / Earth
- Reaction Conduit replaces Elemental Hexarch
- Regulation Crucible Form I = 2,400 HP; Seventh Reaction = fresh 2,900 HP

---

# Active implementation frontier

## **Kessara Relic-copy service implementation**

Closed copy rule:
- Relic must already be obtained;
- one matching copy component is required;
- maximum one forged duplicate per Relic;
- maximum quantity = 2;
- copy is mechanically identical;
- Legacies cannot be copied.

Remaining implementation work may determine:
- exact service/menu unlock timing;
- whether an Auren service fee exists and its value;
- original-vs-copy quantity/UI presentation.

Do not reopen closed combat, MP, CEXP, Mastery, mandatory raw-stat, Elite, Regional-Hunt, or Major-Hunt layers unless later authority explicitly requires it.