# Diyse — Audit135: Major Hunt Raw-Stat Recertification Lock

**Master-canon version:** **v2.20 / Audit135**  
**Date:** August 27, 2026  
**Status:** **MASTER CANON — CONTROLLING FOR ALL 6 MAJOR-HUNT RAW STATS**  
**Parent authority:** **v2.19 / Audit134** plus compatible older locks.

Audit135 closes the Major-Hunt raw-stat layer against the current Lv70 progression model, combat formulas, Base Hit/Evasion architecture, current Status Resistance, current one-bar/fresh-body discipline, and Prime fresh-form refresh rules.

Major-Hunt recommended level is a **preparedness target, not an access gate**. Fixed authored tuning remains active; there is no dynamic player-level scaling.

Current challenge hierarchy:

> **Ordinary < Elite < mandatory story boss < Regional Hunt < Major Hunt**

---

# 1. Current Major Hunt raw table

| # | Major Hunt / Form | Rec. Lv | HP | ATK | MAG | DEF | Spirit | SPD | EVA | SR |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | **Ashen Whitehorn** | **22** | **11,270** | **96** | **78** | **73** | **68** | **38** | **10** | **10** |
| 2A | **Crownless Siege Marshal** | **28** | **9,360** | **124** | **92** | **90** | **78** | **35** | **5** | **10** |
| 2B | **Crownless War Engine** | **29** | **11,650** | **139** | **102** | **99** | **86** | **33** | **0** | **10** |
| 3 | **Concordance Guardian** | **35** | **18,180** | **146** | **151** | **115** | **118** | **40** | **5** | **15** |
| 4 | **Worldscar Leviathan** | **47** | **30,200** | **187** | **207** | **148** | **156** | **44** | **0** | **10** |
| 5 | **Final Archive Arbiter** | **58** | **43,100** | **229** | **244** | **194** | **198** | **50** | **5** | **15** |
| 6 | **The Unfinished World** | **70** | **78,000** | **304** | **318** | **226** | **232** | **61** | **0** | **15** |

The recovered HP / ATK / MAG / DEF / Spirit / SPD values remain coherent under the current progression model.

**No HP / ATK / MAG / DEF / Spirit / SPD repricing is required.**

Audit135 adds/locks current Evasion and general Status Resistance values as shown.

---

# 2. Evasion and Status Resistance

Evasion intent:
- **10** — Ashen Whitehorn is deliberately evasive.
- **5** — Crownless Siege Marshal, Concordance Guardian, Final Archive Arbiter have modest authored avoidance.
- **0** — Crownless War Engine, Worldscar Leviathan, and The Unfinished World are not tuned around natural Evasion.

General Status Resistance bands remain:
- 0 — Normal
- 5 — Resistant
- 10 — Highly Resistant
- 15 — Exceptional

Major-Hunt assignments:
- **SR10** — Ashen Whitehorn, both Crownless forms, Worldscar Leviathan.
- **SR15** — Concordance Guardian, Final Archive Arbiter, The Unfinished World.

This does **not** create blanket status immunity.

Do not restore obsolete percentage-based per-status rows as a second universal resolver. Explicit identity-specific immunity remains separate where separately authored and compatible. True nonliving-body Bleed exclusions remain identity rules, not a universal Major-Hunt rule. Elemental affinity/resistance also remains separate from Status Resistance.

Existing mandatory/Major-boss status-duration/value restrictions remain separate from the raw SR stat.

---

# 3. Major Hunt #1 — Ashen Whitehorn

Current profile:

> **Lv22 — 11,270 HP / 96 ATK / 78 MAG / 73 DEF / 68 Spirit / 38 SPD / EVA10 / SR10**

Preserve:
- one continuous HP bar;
- physical-forward pressure;
- Driven target focus;
- Last Run as a late same-bar escalation.

Last Run does **not** create a fresh body and does not refresh Prime availability.

Ashen Whitehorn remains clearly above the nearby Crown Prototype Regional Hunt without requiring inflated Attack beyond its encounter identity.

---

# 4. Major Hunt #2 — Crownless Siege Marshal → Crownless War Engine

## Form I — Crownless Siege Marshal

> **Lv28 — 9,360 HP / 124 ATK / 92 MAG / 90 DEF / 78 Spirit / 35 SPD / EVA5 / SR10**

## Form II — Crownless War Engine

> **Lv29 — 11,650 HP / 139 ATK / 102 MAG / 99 DEF / 86 Spirit / 33 SPD / EVA0 / SR10**

Combined raw body endurance:

> **21,010 HP**

Preserve:
- genuine fresh-HP transformation;
- Form II stronger, more durable, and more physically defensive;
- Form II slightly slower rather than receiving arbitrary speed escalation;
- no third fresh-health form.

Because Crownless War Engine is a genuine fresh-health body:

> **Prime availability refreshes at Crownless War Engine.**

---

# 5. Major Hunt #3 — Concordance Guardian

Current profile:

> **Lv35 — 18,180 HP / 146 ATK / 151 MAG / 115 DEF / 118 Spirit / 40 SPD / EVA5 / SR15**

Preserve:

> **Six Faces → Open Concordance**

on **one continuous HP bar**.

Do not convert the six Face behaviors into six HP bars, six sequential minibosses, or six separately targetable bodies.

Open Concordance is same-bar and does not refresh Prime availability.

---

# 6. Major Hunt #4 — Worldscar Leviathan

Current profile:

> **Lv47 — 30,200 HP / 187 ATK / 207 MAG / 148 DEF / 156 Spirit / 44 SPD / EVA0 / SR10**

Preserve:
- one continuous HP bar;
- Magic > Attack;
- Spirit > Defense;
- Prismatic Confluence as the central mechanical escalation.

Prismatic Confluence is same-bar and does not refresh Prime availability.

Zero Evasion is intentional. The encounter's challenge is durability, magical pressure, and Confluence management rather than making a colossal target arbitrarily hard to hit.

---

# 7. Major Hunt #5 — Final Archive Arbiter

Current profile:

> **Lv58 — 43,100 HP / 229 ATK / 244 MAG / 194 DEF / 198 Spirit / 50 SPD / EVA5 / SR15**

Preserve:
- one continuous HP bar;
- Custody Protocols;
- Archive Burden;
- Transfer Windows;
- no hidden fresh-health transformation.

Its large one-bar endurance remains justified by late-game optional positioning and its custody/action-management architecture.

Same-bar state changes do not refresh Prime availability.

---

# 8. Major Hunt #6 — The Unfinished World

Current profile:

> **Lv70 — 78,000 HP / 304 ATK / 318 MAG / 226 DEF / 232 Spirit / 61 SPD / EVA0 / SR15**

Preserve the exact one-bar state spine:
1. **WORLDFRAME**
2. same-bar **WORLDHEART EXPOSED**
3. low-HP **FINAL CONSTRUCTION**

There is:
- no fresh second HP bar;
- no third HP bar;
- no hidden post-defeat body;
- no transformation reset.

Therefore:

> **78,000 HP is the complete primary superboss endurance budget.**

Raw identity:
- highest all-around optional raw-stat profile;
- Magic slightly above Attack;
- Spirit slightly above Defense;
- meaningful Speed;
- no natural Evasion tax.

All three states remain on the same HP bar, so Worldheart Exposed and Final Construction do not refresh Prime availability.

Preserve the four-element world-state matrix only:
- Earth / Stone → Staggered
- Ice / Frost → Freeze
- Lightning / Storm → Stun
- Fire / Flame → Burn

Do not reintroduce Water, Wind, or a fifth standard element.

---

# 9. Regional-to-Major hierarchy check

Representative endurance comparisons:

| Timing band | Regional Hunt | Regional endurance | Major Hunt | Major endurance |
|---|---|---:|---|---:|
| early-mid | Crown Prototype Lv20 | **6,503** | Ashen Whitehorn Lv22 | **11,270** |
| mid | Whitehorn Ravager Lv26 | **8,678** | Crownless Marshal → War Engine Lv28–29 | **21,010 total** |
| mid-late | Winterglass Titan Lv32 | **10,879** | Concordance Guardian Lv35 | **18,180** |
| later | Rift Siege Beast Lv44 | **15,875** | Worldscar Leviathan Lv47 | **30,200** |
| late | Authority Remnant Lv56 | **21,913** | Final Archive Arbiter Lv58 | **43,100** |
| apex | Throne of Emperor Vaelkor Lv61–62 | **26,000 total** | The Unfinished World Lv70 | **78,000** |

Verdict:

> **Regional < Major remains clear.**

Do not force monotonic HP across encounters with different architectures. Crownless Marshal → War Engine has more total fresh-body HP than Concordance Guardian's one bar; that is not a progression error.

Effective challenge also depends on fresh-body count, phase mechanics, action taxes, support objectives, recovery, status pressure, Prime refresh availability, and encounter knowledge.

---

# 10. EXP firewall

Audit135 does **not** import stale historical first-clear EXP figures from older raw-stat tables.

Current optional-EXP authority remains separate:
- Major Hunts #1–5 remain part of the current pre-Last-Shelter optional pool under Audit124;
- Major Hunt #6 remains **24,000 EXP** and excluded from the Lv70 cap proof.

Raw-stat recertification does not reopen the current EXP economy.

---

# 11. Closure

Audit135 closes all 6 Major Hunts for:
- recommended level;
- HP;
- Attack;
- Magic;
- Defense;
- Spirit;
- Speed;
- Evasion;
- Status Resistance;
- current one-bar/fresh-body architecture as it affects endurance and Prime refresh.

The progression-dependent named/boss raw-stat recertification frontier is now **closed across mandatory story encounters, optional Elites, Regional Hunts, and Major Hunts**.

Do not reopen already-closed Ability MP, CEXP, Mastery, mandatory progression, Elite, Regional-Hunt, or Major-Hunt balance layers without later explicit authority or a demonstrated contradiction.

Next current working frontier is implementation/content finalization, led by:

> **Kessara Relic-copy service implementation**

Preserve the already-closed Relic-copy core rule:
- Relic must already be obtained;
- one matching copy component is required;
- maximum one forged duplicate per Relic;
- maximum quantity = 2;
- copy is mechanically identical;
- Legacies cannot be copied.
