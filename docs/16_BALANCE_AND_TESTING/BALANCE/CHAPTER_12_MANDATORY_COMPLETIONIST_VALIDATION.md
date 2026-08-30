# Chapter 12 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v88  
**Status:** **PASS / VALIDATED WITH ACTION-WEIGHT, OPTIONAL-PLACEMENT, RH11-TIMING, AND MH6-RUNTIME-DURATION DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate current Chapter 12 — **The Reforged March / final Black Host campaign** — against the player state that actually exists at each encounter point rather than treating **Lv57** as the whole chapter baseline.

Chapter 12 uses the full post-Volition combat framework:
- all six permanent characters are available;
- active battle party remains **maximum 4**;
- Subclasses are legal throughout;
- current Cards, Primes, equipment, Relics/Legacies, Character Quests, Regional Hunts, and Major Hunts may create a real completionist advantage;
- fixed authored enemies do not dynamically scale upward to erase optional progression.

The direct-damage Power audit remains closed. No Chapter-12 action requires a Power retune.

---

## 1. Chapter-level progression anchors
Mandatory campaign spine:
> **Lv52 chapter start → Lv54 Varkesh → Lv56 Vaelkor → Lv57 chapter clear**

Fixed route authority:
- Chapter-11 clear: **299,100 EXP = Lv52**;
- pre-Varkesh ordinary route: **+24,000 EXP**;
- Blackspine / Draevensreach breakthrough: **+3,000 EXP**;
- mandatory pre-Varkesh: **326,100 EXP = Lv54**;
- Varkesh clear: **+6,000 → 332,100 EXP = Lv54**;
- Vhalmarch Forward Hub: **+2,500 → 334,600 EXP = Lv54**;
- post-Varkesh ordinary route: **+23,100 EXP**;
- Vorathen / Veiled Citadel breach: **+3,000 EXP**;
- mandatory pre-Vaelkor: **360,700 EXP = Lv56**;
- Vaelkor clear: **+7,000 → 367,700 EXP = Lv56**;
- war-structure / chapter-clear reward: **+1,400 → 369,100 EXP = Lv57**.

### Practical mandatory route bands
- Blackspine / early campaign: **Lv52→53**;
- Draevensreach / Varkesh pursuit: **Lv53→54**;
- Varkesh final capture: **Lv54**;
- Vhalmarch / Vorathen advance: **Lv54→55**;
- Veiled Citadel: **Lv55→56**;
- Emperor Vaelkor: **Lv56**;
- chapter resolution: **Lv57**.

### Completionist route
Fixed optional advantage normally available by Chapter-12 entry:
- currently available Side Quests — **5,500 EXP**;
- all six Character Quests — **55,000 EXP**;
- Regional Hunts #1–#10 — **56,200 EXP**;
- Major Hunts #1–#5 — **50,000 EXP**.

Total fixed advantage:
> **166,700 EXP**

Therefore, without assuming RH11's unresolved within-Chapter-12 timing:
- Chapter-12 completionist start: **465,800 EXP = Lv63**;
- pre-Varkesh: **492,800 EXP = Lv64**;
- after Varkesh + Vhalmarch activation: **501,300 EXP = Lv65**;
- pre-Vaelkor: **527,400 EXP = Lv66**;
- chapter clear: **535,800 EXP = Lv66**, only 700 EXP short of Lv67.

Regional Hunt #11 grants **13,800 EXP** but its exact pre/post-Varkesh and pre/post-Vaelkor timing remains unresolved. If it is legal and cleared before Vaelkor:
> **541,200 EXP = Lv67** pre-Vaelkor.

This produces the intended late-game split: mandatory route approximately **Lv52→57**, completionist approximately **Lv63→66/67**.

---

## 2. Party / Subclass / Prime boundary
Throughout Chapter 12:
- all six permanent characters are available;
- only **4** act in battle;
- Subclasses are legal;
- no guest expands the active cap;
- current equipped Prime rules are legal where the Prime has been obtained/awakened;
- Vaelkor's genuine fresh second body refreshes Prime availability;
- Varkesh's same-bar late state does not;
- RH11 Sealed Throne → Walking Throne is a genuine fresh body and refreshes Prime availability;
- The Unfinished World's 70% / 35% states are same-bar and do not refresh Prime availability.

The **v91 CEXP recalibration** now places normal full class completion at ~Lv55–60. True-battle testing must use the resulting Class-Level breadth rather than pre-emptively inflating Chapter-12 enemies.

---

## 3. Recovered Chapter-12 formation authority
Current recovered composition source:
> `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_12_RECOVERED_FORMATIONS.md`

The current composition set contains exactly nine ordinary formations.

### Opening
- Reforged Patrol — **7,950 combined HP**;
- Pursuit Line — **8,000**;
- Bulwark Column — **9,870**.

### Middle
- March-Veil Contact — **7,830 combined HP**;
- Veil Screen — **7,650**;
- Transition Guard — **9,140**.

### Late
- Palace Guard — **7,270 combined HP**;
- Veil Crown Cell — **8,000**;
- Inner Stronghold — **11,500**.

All remain below the global 8-enemy cap.

The current reorganized formation file preserves composition but does not expose an exact spawn-weight table. Exact formation-frequency weights therefore remain a data-recovery dependency rather than being invented here.

---

## 4. Ordinary-enemy incoming-pressure validation
Use **Vaelira's Green Arcanist natural body with no equipment HP/Defense/Spirit** as the deliberately fragile reference. Actual geared Chapter-12 parties are safer.

Representative strongest direct actions at their real mandatory-route bands:

### Opening — Lv52→54
- Reforged Legionary — Legion Press: **~14.8% Max HP** at Lv52;
- Imperial Bulwark — Imperial Bash: **~14.8%** at Lv53;
- Imperial Pursuit Lancer — Driving Lance: **~16.1%** at Lv53;
- Host Field Chirurgeon — Cautery Burst: **~9.9%** at Lv54.

### Middle — Lv54→55
- Veiled Blade — Passing Strike: **~15.5% Max HP** at Lv54;
- Crimson Veil Adept — Ruin Veil: **~12.1%** at Lv55;
- Purple Veil Adept — Ruin Lance: **~12.7%** at Lv55.

### Late — Lv56
- Sovereign's Royal Guard — Sovereign Crush: **~17.1% Max HP**;
- Black Host Crown Knight — Imperial Ruin: **~14.5%**;
- Throne Deacon — Throne Ray: **~12.7%**;
- Renewal War-Sorcerer — Ruin Lance: **~13.9%**.

The ordinary roster therefore threatens through:
- 4–7-body action economy;
- Bleed / Stun / Staggered / Burn pressure where authored;
- finite healing and Guard/support turns;
- MP/resource attrition across the imperial march;
not through single-action deletion.

At completionist **Lv63–66** these percentages fall materially, preserving the optional-progression advantage.

**Verdict:**
> **PASS / RETAIN ALL CHAPTER-12 ORDINARY RAW STATS AND POWERS.**

---

## 5. Formation durability / action economy
A conservative mandatory four-character AoE reference using current late ordinary weapons plus the long-established Base-Class AoEs:
- Cyanis — Sweeping Edge;
- Nimera — Weave Burst;
- Vaelira — Stormburst;
- Seyrik — Fracturing Brand;

produces approximately these per-body serious-AoE-round counts at the appropriate route levels:
- Reforged Legionary — **~1.8**;
- Imperial Bulwark — **~2.3**;
- Imperial Pursuit Lancer — **~1.8**;
- Host Field Chirurgeon — **~1.5**;
- Veiled Blade — **~1.6**;
- Crimson Veil Adept — **~1.5**;
- Purple Veil Adept — **~1.6**;
- Sovereign's Royal Guard — **~2.5**;
- Black Host Crown Knight — **~2.3**;
- Throne Deacon — **~1.9**;
- Renewal War-Sorcerer — **~1.7**.

This reference does **not** include:
- Relic/Legacy optimization;
- Subclass burst;
- Standard Cards;
- Prime damage;
- criticals;
- elemental weakness exploitation;
- Base Ultimates.

Therefore even the 7-body Inner Stronghold formation loses its lighter casters/supports quickly and sheds enemy actions before the heavier Guard/Crown bodies finish. The large formations remain resource/status-pressure encounters rather than collections of boss-health enemies.

### Remaining ordinary data dependency
Exact per-action selection weights are not exposed for the full Chapter-12 ordinary roster.

Therefore exact worst-case status-chain frequency remains:
> **OPEN — ACTION-WEIGHT DATA DEPENDENCY**

This is not evidence for a raw-stat or Power retune.

---

## 6. Authored protected encounter — Compelled Relay Bearer
Retain:
> Lv55 / **1,420 HP** / ATK146 / MAG152 / DEF96 / Spirit102 / SPD36

Actions remain:
- Compelled Strike — 175 Power;
- Relay Discharge — 190 Lightning / 15% Stun;
- Relay Surge — 125 AoE;
- Resist the Relay — Power N/A.

On the fragile Lv54–55 reference, its strongest direct action is only about **6–7% Max HP**.

At 0 HP it is safely disabled/disconnected from the immediate relay crisis rather than killed.

**Verdict:**
> **PASS ON KIT / RETAIN NONLETHAL FIREWALL.**

Exact story placement/mechanism remains story-owned and is not converted into a universal possession/control-status rule.

---

## 7. Optional Elite — Lord-Marshal Kharvek
Retain:
> **Lv61 / 6,750 HP / ATK224 / MAG166 / DEF152 / Spirit142 / SPD56 / EVA5 / SR10**

Finite support remains:
> **1 Imperial Bulwark — Chapter-12 body**

No replacement, respawn, transformation, extra action, or Prime refresh.

### Incoming pressure
Against the deliberately fragile unequipped reference:
- mandatory Lv54 — Marshal's Breakthrough: **~23.5% Max HP**;
- mandatory Lv56 — **~22.2%**;
- completionist Lv64 — **~17.9%**;
- completionist Lv66 — **~17.1%**.

### Durability
A conservative four-attacker serious round using current late ordinary weapons and established CL9-or-earlier single-target abilities produces approximately:
- **~1,470–1,530 damage/round** at mandatory Lv54–56;
- about **4.4–4.6 raw serious rounds** against Kharvek's own body before normal Subclass/Card/Prime/critical optimization;
- completionist Legacy-weapon reference at Lv64–66 produces approximately **~1,910–1,970/round**, or about **3.4–3.5 raw rounds**.

The finite Bulwark adds target-priority tax but no hidden extra Kharvek turn.

Because Kharvek's exact within-Chapter-12 placement is not fixed here, an early mandatory party may intentionally be under his Lv61 body. Do not lower him merely to make every possible early access state equal.

**Verdict:**
> **PASS / FORMALLY VALIDATED v88 / RETAIN ALL RAW STATS AND POWERS.**

Dependency:
> exact within-chapter placement remains story-owned.

---

## 8. Mandatory boss — Marshal Varkesh — Final Capture
Actual player references:
- mandatory — **Lv54**;
- completionist fixed-content — **Lv64**;
- high-side — **~Lv65** if additional eligible optional content is cleared.

Retain:
> Lv58 / **17,106 HP** / ATK226 / MAG148 / DEF144 / Spirit131 / SPD55 / EVA5 / SR10

Retain all capture architecture:
- Reforged Command Standard — **900 HP**, no independent turn;
- one Varkesh Black Guard — **1,400 HP**, one ordinary turn;
- East Retreat Beacon — **1,100 HP**, no turn;
- West Retreat Beacon — **1,100 HP**, no turn;
- **3,421 HP / 20% capture floor** while either Beacon survives;
- both Beacons must be destroyed before Varkesh can resolve at 0 HP;
- Varkesh is captured alive.

On the fragile Lv54 reference:
- late Breakthrough Drive with the Command Standard's +10% Attack is roughly **~28% Max HP**;
- even a temporary Standard + Seize Initiative overlap remains roughly **~33%**, threatening but not a healthy one-shot.

At completionist Lv64 the same high pressure falls to roughly **~22–26%**.

Existing duration target remains coherent:
- mandatory — **~11–13 rounds**;
- completionist — **~8–10**;
- high-side — **~7–9**.

**Verdict:**
> **PASS / FORMALLY VALIDATED v88 / RETAIN RAW LINE, SUPPORTS, CAPTURE FLOOR, AND POWERS.**

---

## 9. Mandatory boss — Emperor Vaelkor Draeven → Sovereign Panoply Unbound
Actual player references:
- mandatory — **Lv56**;
- completionist fixed-content — **Lv66**;
- high-side with legally pre-Vaelkor RH11 — **~Lv67**.

Retain Form I:
> Lv60 / **16,800 HP** / ATK223 / MAG209 / DEF155 / Spirit150 / SPD54 / EVA5 / SR10

Retain genuine fresh Form II:
> Lv61 / **20,200 HP** / ATK238 / MAG224 / DEF163 / Spirit157 / SPD55 / EVA0 / SR10

The fresh-body transition:
- does not restore party HP/MP;
- does not spill damage forward;
- does not grant a free transition attack;
- **does refresh Prime availability**.

### Incoming pressure
On the deliberately fragile Lv56 no-equipment reference:
- Panoply Cleave is roughly **~25% Max HP**;
- Sovereign Overrun under Absolute Command's temporary +15% offense is roughly **~30% per target**.

Sovereign Overrun remains telegraphed by one full round of Protected Preparation.

At completionist Lv66 those peaks fall to roughly:
- Panoply Cleave — **~19%**;
- buffed Sovereign Overrun — **~23%**.

Existing user-directed duration target remains coherent:
- mandatory complete encounter — **~18–20 rounds**;
- completionist — **~13–15**;
- high-side — **~12–14**.

**Verdict:**
> **PASS / FORMALLY VALIDATED v88 / RETAIN BOTH RAW BODIES, POWERS, 55% OVERrun RULE, 25% FINAL SOVEREIGNTY RULE, AND PRIME REFRESH.**

No third form, possession reveal, or absolution is introduced.

---

## 10. Regional Hunt #11 — Throne of Emperor Vaelkor
Retain recommendation:
> **Lv61–62 encounter**

Retain Form I:
> Lv61 / **11,800 HP** / ATK228 / MAG234 / DEF172 / Spirit168

Retain fresh Form II:
> Lv62 / **14,200 HP** / ATK240 / MAG221 / DEF166 / Spirit159

Total raw boss-body HP:
> **26,000**

Retain finite non-turn supports:
- Authority Attendant Frame — **1,450 HP**;
- Renewal Attendant Frame — **1,350 HP**, maximum 3 successful 450-HP Renewal triggers encounter-wide.

### Difficulty relationship
- mandatory Chapter-12 clear: **Lv57**, intentionally under the recommendation;
- fully optional Chapter-12 entry: **Lv63**, already slightly above recommendation;
- completionist mid/late Chapter 12: **Lv64–66**, meaningfully advantaged.

At recommended Lv61–62 on the fragile no-equipment reference:
- Sealed Verdict is approximately **~22–23% Max HP**;
- Walking Crush is approximately **~26–27%**;
- the fresh Form-II transition gives one legal Prime-availability refresh.

A conservative ordinary-gear serious-party reference at recommended level projects roughly **~16 raw serious rounds across both boss bodies** before Cards, Primes, Ultimates, criticals, affinities, and support-target optimization. That remains Regional-Hunt endurance rather than mandatory-story pacing.

**Verdict:**
> **PASS / FORMALLY VALIDATED v88 / RETAIN RECOMMENDATION, BOTH BODIES, SUPPORTS, AND POWERS.**

Dependency:
> exact within-Chapter-12 unlock timing relative to Varkesh/Vaelkor remains unresolved and is not invented here.

---

## 11. Post-Vaelkor Major Hunt #6 — The Unfinished World
Unlock remains:
> **Final Archive Arbiter cleared + Vaelkor defeated**

Retain:
> **Lv70 / 78,000 HP / ATK304 / MAG318 / DEF226 / Spirit232 / SPD61 / SR15**

One continuous HP bar:
> WORLDFRAME → WORLDHEART EXPOSED at 70% → FINAL CONSTRUCTION at 35%

No state refreshes Prime availability.

### Actual unlock-level relationship
A pure mandatory-route party is only **Lv56 immediately after Vaelkor** and **Lv57 at Chapter-12 clear**. Because Major Hunt #5 is itself a prerequisite, a route that clears the Arbiter only at this point gains its 18,500 EXP and lands around **Lv58** — still intentionally nowhere near the Lv70 preparedness target.

A true exhaustive completionist can reach approximately:
- Chapter-12 clear with all pre-Ch12 fixed optional content — **Lv66**;
- + RH11 — **Lv67**;
- + post-Vaelkor `What We Build After` — **Lv68**.

Therefore the current Lv70 recommendation remains about two levels above the realistic exhaustive first-prepared completionist state.

### Incoming pressure
Against the deliberately fragile unequipped Lv68 Green Arcanist reference:
- Frame Hammer — **~33% Max HP**;
- Worldheart Flare — **~38%** after State-II Magic Up;
- Final Construction — **~44%** in State III;
- prepared Worldfall — **~37% per target**.

At Lv70 these fall slightly, with Final Construction around **~42%** and Worldfall around **~35%** on that deliberately fragile no-armor reference. Actual endgame geared parties are materially safer.

This is appropriately severe for the ultimate optional superboss and does not produce a healthy-character one-shot on the deliberately fragile reference.

The 78,000-HP one-bar duration is deliberately dependent on the complete late-game toolset — Ultimates, Cards, Primes, Relics/Legacies, affinity play, and optimized builds. It therefore retains a required runtime duration/attrition playtest gate even though the paper two-baseline relationship passes.

**Verdict:**
> **PASS ON TWO-BASELINE PAPER RECERTIFICATION v88 / RETAIN Lv70 AND 78,000 HP / RUNTIME DURATION GATE REMAINS.**

No raw stat or Power is changed in this pass.

---

## 12. Chapter-12 result
### Retained unchanged
- all 11 ordinary enemy raw bodies;
- Compelled Relay Bearer;
- Lord-Marshal Kharvek + one finite Imperial Bulwark;
- Marshal Varkesh final-capture body/support architecture;
- Emperor Vaelkor → fresh Sovereign Panoply Unbound;
- Regional Hunt #11 Sealed Throne → fresh Walking Throne;
- Major Hunt #6 The Unfinished World.

### Numerical changes
> **0**

### Direct-damage Power changes
> **0**

### Remaining Chapter-12 dependencies
- exact ordinary per-action selection weights;
- exact formation-frequency weights;
- exact Lord-Marshal Kharvek within-chapter placement;
- exact RH11 within-chapter timing relative to Varkesh/Vaelkor;
- final runtime duration/resource-attrition playtest for The Unfinished World.

None of these dependencies is permission to reopen the global Power audit.

## Final verdict
> **CHAPTER 12 PASS / VALIDATED v88**

Next validation frontier:
> **Chapter 13 — Lv57 start → Lv60 Last Shelter → Lv62 ending**, with the Last Shelter → Reactor Galleries irreversible threshold tested as a separate pre-/post-PONR resource boundary.
