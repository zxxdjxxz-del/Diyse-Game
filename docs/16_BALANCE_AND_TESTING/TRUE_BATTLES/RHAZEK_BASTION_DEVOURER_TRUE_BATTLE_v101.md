# Diyse — Commander Rhazek → Bastion Devourer Representative True-Battle Certification
**Certification:** **v101 — PASS / RETAIN**  
**Encounter:** Commander Rhazek — Reforged Commander → Bastion Devourer  
**Chapter:** 9 — Larkspire / Crownfall / Rhazek  
**Story point:** mandatory Chapter-9 climax  
**Owner:** `09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES/COMMANDER_RHAZEK_REFORGED_COMMANDER_BASTION_DEVOURER.md`

## Verdict

> **TRUE-BATTLE CERTIFIED / PASS / RETAIN**

No change is required to either boss body's HP/raw stats, any authored direct-damage Power, status chance, repetition lock, Demolition Breaker architecture, the 18% Exposed Rhazek state, or the genuine fresh-body transition.

The fight also passes the current Prime-economy stress test:
- Form I → Bastion Devourer gives a genuine fresh HP body but does **not** restore a spent Prime identity;
- a Prime already manifested at the transition remains manifested for its remaining Prime rounds;
- after dismissal, **2 full normal party rounds** are still required before another Ready Prime may be invoked;
- legal chained Awakened Primes improve resource conservation but do not erase encounter duration because the boss still acts during Prime rounds.

This is a **design-layer stochastic certification**, not runtime-engine QA.

---

# 1. Current ruleset used

The certification uses current organized authority only, including:
- fixed Speed-derived turn-entry initiative;
- current Physical / Magical / Hybrid damage formulas;
- current Base Hit / Evasion and Critical rules;
- current percentage temporary-stat rules;
- current five-status rules and v96 Bleed escalation;
- selected-class Traits with learned abilities persisting across class selection;
- current one-use-until-restored Prime economy;
- current 3-Prime-round Awakened manifestation;
- the separate 2-full-normal-round post-dismissal spacing rule;
- current genuine-fresh-body form-transition rules.

No ATB, Confirm Round queue, retired Mastery Points, old Prime MP costs, or fresh-form Prime restoration were used.

---

# 2. Mandatory Chapter-9 snapshot

## Player Level
All four active characters:
> **Lv40**

Mandatory pre-Rhazek EXP:
> **173,800 EXP — Lv40, 800 EXP short of Lv41**

## Class-development state
The post-Volition mandatory CEXP available before Rhazek is sufficient for a base-first route to finish the selected Base classes and begin developing Subclasses.

Reference class state:
- Cyanis — Crest Knight **CL13**, Crest Arcanist approximately **CL5**;
- Ilyra — Blue Warden **CL13**, Vowblade approximately **CL5**;
- Torren — War Archer **CL13**, Routeweaver approximately **CL6**;
- Vaelira — Green Arcanist **CL13**, Axiomblade approximately **CL6**.

For this mandatory climax benchmark, the completed **Base class is selected** for all four characters. Therefore Base Rank-III Traits and Base Ultimates are active, while already learned Subclass abilities remain legally available.

This avoids the artificial assumption that the player must enter the mandatory climax with a still-developing Subclass selected.

## Active four
- Cyanis
- Ilyra
- Torren
- Vaelira

## Prepared ordinary-equipment line
The mandatory prepared line uses explicitly Chapter-9-legal ordinary weapons while keeping armor/secondary choices conservative. No Relic, Legacy, or Standard Card power is included.

- Cyanis — **Deepforge Blade** / Crest Plate / Yahtrean Shield reference;
- Ilyra — **Crucible Wardrod** / Blue Warden Mail / Warding Focus reference;
- Torren — **Storm War Bow** / War Archer Gear reference;
- Vaelira — **Veycross Battlestaff** / Green Arcanist Garb reference.

Resulting Lv40 battle stats:

| Character | HP | MP | ATK | MAG | DEF | Spirit | SPD |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cyanis | 2,070 | 164 | 179 | 150 | 145 | 122 | 41 |
| Ilyra | 1,972 | 204 | 144 | 179 | 108 | 142 | 41 |
| Torren | 1,972 | 173 | 204 | 90 | 111 | 100 | 42 |
| Vaelira | 1,617 | 228 | 88 | 204 | 89 | 132 | 43 |

## Standard Cards
> **None used in the certification baseline.**

## Prepared consumables
The strict prepared line carries:
- 3 Grand Salves;
- 2 Company Salves;
- 2 Highflow Tonics;
- 3 Trauma Remedies;
- 3 Stability Remedies;
- 2 Greater Rousing Salts.

No Emergency Kit, Reservoir Tonic, Emergency Rally, reward-only restoration, Relic, or Legacy is required.

Emergency Kit is intentionally excluded from the Prime stress line because it is an authored Prime-restoration effect; the purpose here is to test persistent Prime spending across the fresh body.

---

# 3. Smart / normal player policy

The policy reacts only to visible state.

### Cyanis
- maintains the Crest Strike → Crest Rend Harmonized Crest cycle;
- uses Crest of Companions when its damage plus party cleanse / Defense +30% / Spirit +30% package has strong value, especially against an imminent Demolition Breaker resolution;
- uses normal recovery/items only when thresholds justify them.

### Ilyra
- uses Mercy Returned when damage plus lowest-HP ally sustain is efficient;
- switches to Mend / Renewal / Clear Warding / Revive / Lifeline as state demands;
- otherwise contributes Warden's Valor.

### Torren
- applies and refreshes Hunter's Measure with Sizing Shot;
- uses Colossus Draw and The Great Beast Falls under Measure;
- uses Throughline for MP efficiency where legal;
- uses learned Set the Pace on Cyanis during a Demolition Breaker warning window so persistent mitigation can resolve before the boss when Speed order permits.

### Vaelira
- alternates standard elements to use Prismatic Flow;
- uses Cinder Bloom / elemental pressure to seek legal Burn;
- uses Stonebreak during Demolition Breaker Preparation to seek Staggered;
- otherwise uses Prism Lance / efficient elemental damage.

### Demolition Breaker response
The simulation does **not** secretly extend Defend duration.

Demolition Breaker Preparation consumes Rhazek's action and creates the authored one-round warning. Since ordinary Defend lasts only from that character's turn through end of round, smart play instead uses the warning for:
- healing;
- status cleanup;
- Set the Pace / initiative preparation;
- Stonebreak's legal Staggered chance;
- Crest of Companions' persistent Defense/Spirit increase;
- or Prime timing.

A correctly timed Defend remains legal where initiative permits it.

---

# 4. Enemy policy

The owner file does not provide hidden deterministic AI weights, so legal boss actions are selected stochastically subject to:
- current form/state;
- repetition locks;
- Demolition Breaker threshold and pending-resolution state;
- the 18% Exposed Rhazek move restrictions.

Single-target choices are distributed among conscious legal targets.

The genuine Form-I → Form-II transition immediately replaces the target body:
- excess damage does not spill;
- Hunter's Measure and other target-body states from Form I do not transfer unless explicitly authored;
- party HP/MP persist;
- Prime spent state persists;
- no free transition attack occurs.

---

# 5. Mandatory Lv40 — no Prime

Runs:
> **20,000**

Results:
- wins: **20,000 / 20,000 = 100%**;
- median duration: **14 rounds**;
- mean duration: **14.48 rounds**;
- P90 duration: **17 rounds**;
- any-KO incidence: **0.08%**;
- defeat incidence: **0%**;
- mean ending party HP: **75.06%** of combined Max HP;
- mean ending party MP: **12.18%** of combined Max MP;
- mean consumables used: **3.45**.

Demolition Breaker remained behaviorally relevant:
- Preparation appeared in **42.55%** of runs;
- Resolution actually fired in **27.97%** of runs.

There is no structural wipe signature. The duration distribution lands directly on the authored paper target:
> **typical 14–16 / safety 16–17**.

---

# 6. Mandatory Lv40 — one Awakened Last Sentinel

Prime policy:
- time Last Sentinel near the end of Reforged Commander rather than opening immediately;
- allow the Prime to carry naturally across the genuine fresh-body transition if its damage reaches 0 HP during manifestation;
- do not restore Last Sentinel at Form II;
- use all remaining Prime rounds normally against Bastion Devourer.

Runs:
> **10,000**

Results:
- wins: **100%**;
- median total combat duration: **15 rounds**;
- mean total duration: **15.34 rounds**;
- P90: **17 rounds**;
- mean normal-party rounds: **12.34**;
- completed Prime rounds: **3** when the manifestation runs its full course;
- any-KO incidence: **0%**;
- mean ending party HP: **81.79%**;
- mean ending party MP: **33.16%**;
- mean consumables used: **2.94**.

Most importantly:
> **Last Sentinel crossed Reforged Commander → Bastion Devourer during its manifestation in 99.04% of timed stress runs.**

In those runs:
- Bastion Devourer began at full HP;
- Last Sentinel stayed spent;
- the same manifestation continued for the remaining Prime rounds;
- no fresh-form Prime refresh was granted.

This directly certifies the current persistent-spend fresh-body rule.

---

# 7. Mandatory Lv40 — legal two-Prime spacing stress

By this story point the mandatory story has four Awakened Story Primes available, including Last Sentinel and Last Convergence.

Stress sequence:
1. invoke **Last Sentinel** near the Form-I end;
2. let it cross naturally into Bastion Devourer where applicable;
3. dismiss after its normal 3 Prime rounds;
4. complete **2 full normal party rounds**;
5. only then invoke **Last Convergence** if the encounter is still active.

Runs:
> **10,000**

Results:
- wins: **100%**;
- median total duration: **15 rounds**;
- mean total duration: **15.17 rounds**;
- P90: **17 rounds**;
- mean normal-party rounds: **9.24**;
- mean Prime rounds: **5.92**;
- any-KO incidence: **0.02%**;
- mean ending party HP: **85.07%**;
- mean ending party MP: **43.77%**;
- mean consumables used: **0.98**;
- Form-I → Form-II transition during Last Sentinel: **99.11%**.

The second Prime is powerful, but it does **not** collapse the fight into a free burst sequence.

The key result is resource preservation:
- no-Prime mean ending MP: **12.18%**;
- chained-Primes mean ending MP: **43.77%**;
- no-Prime mean items: **3.45**;
- chained-Primes mean items: **0.98**.

Total elapsed combat duration still centers at 15 rounds because Rhazek/Bastion Devourer continues receiving enemy turns during Prime manifestation.

That is the intended behavior of the current Prime model.

---

# 8. Completionist references

## Fixed-content completionist — Lv48, no Prime
RH9 is excluded because its exact pre-Crownfall return trigger remains story-owned.

Runs:
> **5,000**

Results:
- wins: **100%**;
- median: **12 rounds**;
- mean: **12.18**;
- P90: **14**;
- any-KO: **0%**;
- mean ending HP: **85.03%**;
- mean ending MP: **31.35%**;
- mean items: **2.51**.

## RH9-legal sensitivity — Lv49, no Prime
Runs:
> **5,000**

Results:
- wins: **100%**;
- median: **12 rounds**;
- mean: **12.06**;
- P90: **14**;
- any-KO: **0%**;
- mean ending HP: **85.76%**;
- mean ending MP: **32.66%**;
- mean items: **2.41**.

## Lv49 chained-Prime stress
Runs:
> **5,000**

Results:
- wins: **100%**;
- median total duration: **13 rounds**;
- mean: **13.32**;
- P90: **14**;
- mean normal-party rounds: **7.76**;
- mean Prime rounds: **5.56**;
- any-KO: **0%**;
- mean ending HP: **90.45%**;
- mean ending MP: **59.10%**;
- mean items: **0.31**;
- Form-I → Form-II transition during Last Sentinel: **99.58%**.

The completionist no-Prime median of **12** lands inside the authored **11–13** target.

---

# 9. Demolition Breaker certification

> **PASS / RETAIN**

The breaker is not a fake telegraph and not an unavoidable wipe check.

It appears often enough to matter, while current systems provide real responses:
- Staggered application can reduce offense/Speed;
- Set the Pace can change next-round relative order;
- Crest of Companions can establish persistent major mitigation before resolution;
- healing and status cleanup can prepare the party;
- Prime manifestation can absorb/suspend ordinary-party exposure when timed legally;
- correctly timed Defend remains available where initiative supports it.

No change is justified to:
- 55% availability threshold;
- protected-preparation classification;
- 1-full-round warning;
- 335 Power resolution;
- 25% Staggered chance;
- 3-round repetition lock.

---

# 10. Representative mandatory no-Prime flow

A representative smart/normal seed cleared in **15 rounds** with no KO and one full Demolition Breaker Preparation → Resolution sequence.

- **R1:** Rhazek uses Hold the Line. Vaelira opens elemental pressure; Torren establishes Hunter's Measure; Ilyra uses Mercy Returned; Cyanis uses Crest Strike.
- **R2:** Torren establishes Throughline; Cyanis consumes Harmonized Crest with Crest Rend; party pressure continues through Rhazek's buffed defenses.
- **R3:** Shieldline Break Staggers Torren; Stability Remedy is used rather than losing the route/Measure role.
- **R4:** Rhazek refreshes Hold the Line; Torren refreshes Measure; Cyanis continues the Strike → Rend cycle.
- **R5:** Torren's The Great Beast Falls lands under Measure for major but non-terminal damage.
- **R6:** Command Rupture pressures the party; Torren's next Great Beast Falls finishes Reforged Commander. Bastion Devourer appears immediately at full HP with **no transition attack and no resource refresh**. Remaining normal-round turns continue against the new body.
- **R7–R11:** the party re-establishes target-body states on Bastion Devourer, manages Bleed/status pressure, and continues normal resource trade.
- **R12:** Bastion Devourer selects **Demolition Breaker — Preparation**. Vaelira uses Stonebreak and successfully applies Staggered; Torren uses Set the Pace on Cyanis; Ilyra contributes offense/sustain; Cyanis continues setup.
- **R13:** the Speed preparation allows Cyanis to resolve **Crest of Companions** before Demolition Breaker. The party receives Defense +30% / Spirit +30% and cleanse support. Demolition Breaker then resolves for survivable direct damage across all four characters rather than producing a death spiral.
- **R14:** the Bastion shell tears open at the authored 18% threshold; no HP refill or Prime refresh occurs. Torren lands another measured Great Beast Falls while Rhazek shifts to the Exposed kit.
- **R15:** Exposed Rhazek uses Last Line; accumulated direct damage plus current Bleed/Burn pressure finishes the remaining Form-II HP. No third body appears.

This representative run demonstrates all major encounter requirements:
1. genuine fresh Form II with no damage spill;
2. no free transition action;
3. target-body state rebuild after the fresh form;
4. meaningful MP/item attrition;
5. an actual Demolition Breaker warning-and-response cycle;
6. short same-bar Exposed Rhazek finish;
7. no third form.

---

# 11. Pacing interpretation

Current evidence validates the authored duration targets rather than forcing a retune.

### Mandatory Lv40, no Prime
> **median 14 / mean 14.48 / P90 17**

### Mandatory Lv40, one Last Sentinel
> **median 15 total combat rounds / mean 15.34 / P90 17**

### Mandatory Lv40, legal two-Prime chain
> **median 15 total / mean 15.17 / P90 17**

### Completionist Lv48–49, no Prime
> **median 12 / mean ~12.1 / P90 14**

The Prime lines are not expected to reduce total elapsed round count monotonically because their 3-round manifestations are real rounds with enemy turns. Their strongest benefit is preserving ordinary-party MP/HP/items while maintaining encounter pressure.

---

# 12. Final certification

> **Commander Rhazek — Reforged Commander → Bastion Devourer — TRUE-BATTLE PASS / RETAIN v101**

Retain unchanged:
- Reforged Commander HP **8,431** and raw line;
- Bastion Devourer HP **10,462** and raw line;
- all current direct-damage Powers;
- all current status chances and repetition locks;
- genuine fresh Form-II architecture;
- persistent spent-Prime state across the fresh body;
- Demolition Breaker;
- 18% Exposed Rhazek same-bar state;
- current rewards and route-level references.

No structural failure was reproduced.

The representative true-battle suite should advance next to:
> **Emperor Vaelkor Draeven — Emperor of the Reforged Host → Sovereign Panoply Unbound — Chapter 12 — mandatory Lv56 / completionist Lv66**

Vaelkor is the next late mandatory full-system two-body certification and should repeat the persistent-Prime-spend stress at a much larger HP/resource scale.