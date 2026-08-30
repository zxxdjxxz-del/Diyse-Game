# Chapter 13 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v89  
**Status:** **PASS / VALIDATED WITH ACTION-WEIGHT, FORMATION-FREQUENCY, AND FINAL-RUNTIME DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate Chapter 13 — **The Last Command** — against the player state that actually exists at each point of the final act.

The chapter is not treated as one Lv62 block. Its mandatory spine is:
> **Lv57 chapter start → Lv58 Last Weapon Archon → Lv60 Last Shelter / true PONR → Lv61 final boss → Lv62 ending**

The completionist route is deliberately much stronger and may reach the Lv70 cap before the irreversible final sequence. Enemies remain fixed; there is no dynamic scaling to erase that advantage.

---

## 1. Mandatory progression anchors
Chapter-12 clear:
> **369,100 EXP = Lv57**

Pre–Last Shelter mandatory package:
- ordinary EXP — **18,600**;
- Deepest / Deep City / Last Weapon Archive progression — **4,000**;
- fragment-survival truth — **5,000**;
- Last Weapon Archon — **12,000**;
- Last Shelter / final-prep state — **6,700**.

Mandatory pre-Archon:
> **396,700 EXP = Lv58**

After Archon:
> **408,700 EXP = Lv59**

At Last Shelter:
> **415,400 EXP = Lv60 exactly**

True irreversible threshold:
> **Last Shelter → Reactor Galleries**

Post-threshold mandatory package before the final boss:
- ordinary EXP — **11,200**;
- Reactor Galleries / Entity realization — **3,500**;
- Reactor–Crest Interface / final state — **2,500**.

Mandatory pre-final-boss:
> **432,600 EXP = Lv61**

Final two-form reward:
> **+13,500 EXP → 446,100 EXP = Lv61**

Final Severance / ending:
> **+2,000 EXP → 448,100 EXP = Lv62 exactly**

This is the correct Chapter-13 level sequence for encounter certification.

---

## 2. Completionist progression anchors
Established optional proof pool available during the Chapter-13 pre-PONR state:
> **195,000 EXP**

It includes:
- all five ordinary Side Quests;
- all six Character Quests;
- all eleven Regional Hunts;
- Major Hunts #1–#5.

Without MH#6:
- Chapter-13 start: **564,100 EXP = Lv68**;
- pre-Archon: **591,700 EXP = Lv69**, only 2,400 short of Lv70;
- Archon reward itself pushes this route to the **Lv70 cap** before Last Shelter.

Major Hunt #6 — The Unfinished World is also legally available before the true PONR once its prerequisites are satisfied. A full all-content route may therefore already be **Lv70 before the Archon**.

By Last Shelter:
> **completionist reference = Lv70 cap**

Final boss reference:
> **mandatory Lv61 / completionist Lv70**

No boss or ordinary enemy scales upward to remove this difference.

---

## 3. Party / build-state boundary
Throughout Chapter 13:
- all six permanent characters are available;
- battle party remains **maximum 4 active**;
- Subclasses are legal;
- current Base/Subclass abilities, Masteries, equipment, Standard Cards, Story Primes, Relics/Legacies, Ultimates, and legal optional rewards may be used;
- the **v91 CEXP recalibration is complete**; true-battle testing must use its resulting Class-Level state rather than forcing an enemy retune first.

### Last Shelter resource boundary
Last Shelter is the final:
- recovery point;
- save/checkpoint;
- loadout point;
- return point for eligible unfinished content.

Balance requirement:
> the Last Shelter recovery implementation must allow the player to begin the irreversible Reactor Galleries sequence in **full combat-ready condition** rather than forcing Last Weapon Archon attrition into the final boss by accident.

The final boss's fresh Form-II body does **not** restore party HP/MP; it refreshes Prime availability only because it is a genuine fresh-health boss body.

---

## 4. Recovered ordinary formation set
Authority:
> `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_13_RECOVERED_FORMATIONS.md`

### Opening
- Aspect Triad — Hunger Aspect + Ruin Aspect + Fear Aspect — **5,060 combined HP**;
- Quiet Hunger — Hunger Aspect + Silence Aspect + Devouring Echo — **4,600**;
- Fourfold Edge — Ruin Aspect + Silence Aspect + Fear Aspect + Devouring Echo — **6,140**.

### Middle
- Terrain Veil — Terrain Maw + Empty Sky Wraith + Dying-Light Wisp — **4,780 combined HP**;
- Memory Line — Calamity Memory + Devouring Echo + Empty Sky Wraith + Dying-Light Wisp — **5,680**;
- Maw Memory — Terrain Maw + Calamity Memory + Dying-Light Wisp + Devouring Echo — **6,440**.

### Late
- End Pressure — Hunger Aspect + Ruin Aspect + Empty Sky Wraith — **4,800 combined HP**;
- Aspect Memory — Ruin Aspect + Silence Aspect + Fear Aspect + Calamity Memory — **6,500**;
- Final-Domain Knot — Hunger Aspect + Terrain Maw + Empty Sky Wraith + Calamity Memory — **7,080**.

Chapter 13 intentionally uses only **3–4 ordinary bodies** per formation. Difficulty comes from stronger identities, copy/memory pressure, role combinations, and final-act resource management rather than 7–8-enemy swarms.

Exact formation-frequency weights are not currently exposed and remain a data-recovery dependency.

---

## 5. Ordinary-enemy incoming-pressure validation
Use **Vaelira's Green Arcanist natural body with no equipment HP/Defense/Spirit** as the deliberately fragile reference. Real geared parties are materially safer.

At mandatory **Lv57**, representative strongest single-target direct hits are approximately:
- Terrain Maw — Maw Crush: **17.5% Max HP**;
- Fear Aspect — Dread Rush: **15.4%**;
- Terrain Maw — Ruin Bite: **14.8%**;
- Hunger Aspect — Devouring Rend: **14.5%**;
- Dying-Light Wisp — Fading Ray: **13.7%**.

At the post-Shelter **Lv60–61** route state, those same peaks fall to roughly **12–16%**.

At completionist **Lv69–70**, Terrain Maw's Maw Crush falls to roughly **12–13%** on this intentionally fragile, unequipped reference.

Therefore ordinary Chapter-13 pressure is carried by:
- 3–4-body action economy;
- Bleed / Staggered and authored elemental/status riders;
- Devouring Echo / Calamity Memory replay behavior;
- repeated final-domain resource expenditure;
not by healthy-character deletion.

**Verdict:**
> **PASS / RETAIN ALL CHAPTER-13 ORDINARY RAW STATS AND POWERS.**

Exact ordinary per-action selection weights remain a data-recovery dependency.

---

## 6. Copy/replay mechanics
Retain:
- Devouring Echo — **75% completed eligible source total Power / clamp 120–260**;
- Calamity Memory — **85% completed eligible source total Power / clamp 140–300**.

They:
- record only after the eligible player action completes;
- do not predict commands;
- do not copy Prime commands;
- do not copy status/penetration/resource/extra-action riders;
- do not rewrite permanent player state.

Because their replay Power is clamped and stripped of high-value riders, the mechanics add adaptation pressure without allowing a completionist nuke to become an uncontrolled enemy one-shot.

**Verdict:**
> **PASS / RETAIN.**

---

## 7. Optional Elite — Devourer of Names
Retain:
> **Lv63 / 7,000 HP / ATK216 / MAG230 / DEF151 / Spirit159 / SPD57 / EVA10 / SR10**

Mandatory practical access reference:
> **Lv58–60**, depending exact exploration timing.

Completionist reference:
> **Lv69–70**.

On the deliberately fragile no-equipment body:
- Identity Crush is roughly **19.9% Max HP at Lv58**, **18.8% at Lv60**, and **14.5% at Lv70**;
- Namefall Wave is roughly **13.1% per target at Lv58**, falling below **10% at Lv69–70**.

At 60% HP it creates exactly one **900-HP Consumed Echo** with no independent turn and no direct damage. The Echo's +10% Magic / +10 Total Defense tax is finite and removable.

The 7,000-HP body remains compatible with the standing optional-Elite target of roughly **2–4 serious party rounds** once the Chapter-13 party's full legal Base/Subclass/Card/Ultimate toolkit is counted. Completionists clear materially faster.

**Verdict:**
> **PASS / FORMALLY VALIDATED v89 / RETAIN ALL RAW STATS AND POWERS.**

---

## 8. Mandatory guardian — Last Weapon Archon
Actual player references:
- mandatory — **Lv58**;
- broad completionist — **Lv69**;
- full completionist — **Lv70 cap**.

Retain:
> **Lv63 / 20,800 HP / ATK236 / MAG220 / DEF160 / Spirit160 / SPD56 / EVA0 / SR15**

Retain one continuous HP bar:
> Archive Authority → Weapon Protocol Unsealed at **60% HP**

No HP refill, support wave, or Prime refresh occurs at the same-bar transition.

On the deliberately fragile Lv58 no-equipment reference:
- Compression Verdict is roughly **25.1% Max HP**;
- Threefold Execution total is roughly **23.8%**;
- Weapon Discharge is roughly **14.1% per target**.

The one-time visible convergence → compression → discharge sequence therefore creates a serious but survivable final-guardian spike.

Existing pacing target remains coherent:
- mandatory — **~15–17 rounds**;
- broad Lv69 completionist — **~10–12**;
- Lv70 cap — **~9–11**.

**Verdict:**
> **PASS / FORMALLY VALIDATED v89 / RETAIN RAW LINE, POWERS, AND 60% PROTOCOL SHIFT.**

---

## 9. True PONR — Last Shelter
The chapter's mandatory level reaches:
> **Lv60 exactly at Last Shelter**

This is the correct final-preparation checkpoint.

Before crossing:
- eligible unfinished optional content remains reachable;
- completionists can reach the Lv70 cap;
- loadouts may be changed;
- recovery is available.

After crossing:
> no optional-route assumption is added to the mandatory proof.

The post-PONR final-domain ordinary route raises mandatory progression from **Lv60 → Lv61** before the final boss.

**Verdict:**
> **PASS / PONR LEVEL AND RESOURCE SPLIT RETAINED.**

---

## 10. Final boss — Reconstituted Entity → The Last Command
Actual player references:
- mandatory — **Lv61**;
- completionist — **Lv70 cap**.

### Form I — Reconstituted Entity
Retain:
> **Lv63 / 22,500 HP / ATK224 / MAG228 / DEF158 / Spirit163 / SPD55 / EVA5 / SR15**

On the deliberately fragile Lv61 reference:
- Continuity Crush is roughly **21.4% Max HP**;
- Reconstituted Judgment is roughly **18.4%**;
- with Heart Manifestation's temporary Magic +10%, Judgment is roughly **21.1%**.

Heart Manifestation:
- max1;
- 1,100 HP;
- no independent turn;
- no direct damage;
- finite +10 Total Defense / Magic +10% tax.

### Fresh Form II — The Last Command
Retain:
> **Lv64 / 28,500 HP / ATK247 / MAG247 / DEF168 / Spirit168 / SPD58 / EVA5 / SR15**

Fresh-body rules remain:
- no damage spillover;
- no party HP/MP restore;
- no free transition attack;
- **Prime availability refreshes**.

On the deliberately fragile Lv61 reference:
- Total Directive is roughly **22.9% Max HP**;
- Crest Rewrite total is roughly **25.3%**;
- ordinary Final Directive is roughly **26.7% per target**.

A deliberately severe high-side paper overlap of full temporary offense — two live Shards (+10% ATK/MAG total) plus Absolute Continuity (+15%) — puts prepared Final Directive around **35–36% Max HP per target** on this no-armor fragile reference.

At Lv70 the same extreme overlap falls to roughly **29%**.

Final Directive is telegraphed by a full round of Protected Preparation, so this peak has explicit Defend/recovery/mitigation/Prime counterplay and is still nowhere near a healthy one-shot.

Existing complete-fight pacing remains coherent:
- mandatory Lv61 — **~22–24 rounds**;
- completionist Lv70 — **~18–20 rounds**.

Completionists are also materially safer, have stronger resource efficiency, and can exploit a broader final toolkit even where raw round-count advantage is intentionally not enormous.

**Verdict:**
> **PASS / FORMALLY VALIDATED v89 / RETAIN BOTH HP BODIES, SUPPORTS, POWERS, AND FRESH-FORM PRIME REFRESH.**

At Form-II 0 HP:
> combat ends into Final Severance; no third combat body exists.

---

## 11. Final-support objects
Retain:
- Heart Manifestation — max1 / **1,100 HP / Power N/A**;
- Unbound Shard — max2 / **1,050 HP each / Power N/A**.

They have:
- no independent ordinary turn;
- no direct damage;
- no repair;
- no respawn.

They add target-priority and boss-buff tax without adding hidden enemy actions.

**Verdict:**
> **PASS / RETAIN.**

---

## 12. Chapter-13 result
### Retained unchanged
- all nine ordinary enemy bodies;
- all nine recovered 3–4-body formation compositions;
- Devouring Echo / Calamity Memory replay rules;
- Devourer of Names + finite Consumed Echo;
- Last Weapon Archon;
- Reconstituted Entity → fresh The Last Command;
- Heart Manifestation / Unbound Shards;
- Last Shelter Lv60 PONR placement;
- final Lv62 campaign endpoint.

### Numerical enemy changes
> **0**

### Direct-damage Power changes
> **0**

### Remaining Chapter-13 dependencies
- exact ordinary per-action selection weights;
- exact formation-frequency weights;
- runtime final-act resource/attrition validation with real player builds;
- runtime final-boss duration validation with full Cards/Primes/Ultimates/Relics/Legacies;
- implementation must make Last Shelter recovery sufficient for full combat readiness before the true PONR.

None of these dependencies reopens the direct-damage Power audit.

## Final verdict
> **CHAPTER 13 PASS / VALIDATED v89**

## Campaign-wide consequence
With Chapter 13 complete:
> **the planned paper Enemy & Boss Mandatory-vs-Completionist Validation is COMPLETE across Chapters 0–13.**

Specific unrecovered placement/action-weight/quest-boss data and runtime QA gates remain tracked separately, but they no longer block the next progression pass.

Next active balance priority:
> **CEXP recalibration to the Player Lv55–60 full Base + Subclass completion window.**
