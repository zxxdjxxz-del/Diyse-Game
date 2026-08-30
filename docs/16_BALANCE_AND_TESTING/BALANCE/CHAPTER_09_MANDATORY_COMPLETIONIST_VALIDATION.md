# Chapter 9 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v85  
**Status:** **PASS / VALIDATED WITH EXPLICIT FORMATION/HUNT-TIMING DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate Chapter 9 against the player state that actually exists at each point rather than treating **Lv42** as the entire chapter baseline.

Chapter 9 retains the post-Volition combat framework:
- all six permanent characters are available;
- the active battle party remains **maximum 4**;
- Subclasses are legal throughout the chapter;
- completionist level, gear, Card, Prime, Character-Quest, Hunt, and CEXP advantages are allowed to make fixed encounters materially easier;
- enemies do not dynamically scale upward to erase optional progression.

The direct-damage Power audit remains closed. Existing Powers are changed only if a specific encounter fails its intended tier. No such Power failure occurs in Chapter 9.

---

## 1. Chapter-level anchors
Current mandatory campaign spine:
> **Lv37 chapter start → Lv42 chapter end**

The important internal anchors are not evenly distributed.

### Mandatory route
- Chapter-8 clear / Chapter-9 start: **138,800 EXP = Lv37**;
- Equal Mercy sanctuary progression + working Larkspire ordinary slice before the Arbiter: **~146,800 EXP = Lv37**, only 500 EXP short of Lv38;
- Equal Mercy Arbiter + Last Sanctuary resolution moves the route to **~152,800 EXP = Lv38**;
- Crownfall military progression then moves through **Lv38→39→40**;
- pre-Rhazek: **173,800 EXP = Lv40**, 800 EXP short of Lv41;
- post-Rhazek: **181,300 EXP = Lv41**;
- Chapter-clear reward: **184,300 EXP = Lv42 exactly**.

### Completionist route
Fixed optional EXP already legal before Equal Mercy totals approximately **78,200 EXP**, placing the early Chapter-9 completionist around:
> **Lv45**

That package includes:
- The Marks We Leave;
- The Third Caravan;
- Regional Hunts #1–#8;
- Major Hunts #1–#2;
- Vaelira, Cyanis, Nimera, and Seyrik Character Quests.

Therefore:
- Equal Mercy Arbiter: **Lv37 mandatory / Lv45 completionist**;
- immediately after Equal Mercy + Last Sanctuary: approximately **Lv38 mandatory / Lv46 completionist**;
- Rhazek: **Lv40 mandatory / Lv48 completionist if RH9 is not yet legally cleared**, or **Lv49 completionist if RH9 is legally cleared before the Crownfall climax**;
- very exhaustive incidental/Elite combat can push the high side toward **~Lv50**.

Regional Hunt #9 has a Chapter-9 Larkspire optional-return context, but its exact S### trigger is not fixed. This pass therefore validates both legal timing cases rather than inventing a trigger.

### Practical mandatory bands
- Equal Mercy opening/sanctuary: **Lv37→38**;
- Larkspire authored crisis content: **Lv37→38**;
- Crownfall opening/middle: **Lv38→39**;
- late Crownfall / Rhazek approach: **Lv39→40**;
- post-climax chapter clear: **Lv41→42**.

---

## 2. Party / Subclass / Prime boundary
Chapter 9 has:
- six permanent roster members;
- four active battle slots;
- full legal Subclass access;
- two Prime slots per character under the post-Volition rules where otherwise legal;
- normal fixed-enemy scaling only.

Mandatory Subclass training is more mature than it was in Chapter 8, but it is not assumed to be globally mastered. Completionist CEXP can produce broader/deeper Subclass access.

The **v91 CEXP recalibration** now places normal full class completion at ~Lv55–60. True-battle testing must use the resulting exact Class Levels; this paper validation is not a reason to dynamically rescale enemies.

**Last Sanctuary** reaches its mandatory Chapter-9 Story-Prime awakening/resolution during the Equal Mercy half. That progression is available to both mandatory and completionist routes before the Crownfall climax, so it is not treated as a completionist-only advantage.

---

## 3. Ordinary enemies — route validation
Current Chapter-9 ordinary/carryover roster:
- Triage Automaton — Lv38 / 1,050 HP;
- Recovery Hound — Lv38 / 1,120 HP;
- Quarantine Custodian — Lv39 / 1,360 HP;
- Veteran Ruin Cohort — Crownfall Lv40 / 1,320 HP;
- Western War-Sorcerer — Crownfall Lv40 / 1,080 HP;
- Conqueror Shieldbearer — Crownfall Lv40 / 1,480 HP;
- Rift Cannoneer — Crownfall Lv40 / 1,020 HP;
- Siege Engineer — Crownfall Lv40 / 980 HP.

For a conservative lethality reference, use **Vaelira's Green Arcanist natural body with no equipment Defense/Spirit/HP added**. Actual geared parties are safer.

Representative strongest single-target direct damage at plausible mandatory route points:
- Triage Automaton Sterilizing Ray at Lv37 target — **~13.3% Max HP**;
- Recovery Hound Driving Rush at Lv37 target — **~15.9%**;
- Quarantine Custodian physical strike at Lv38 target — **~14.2%**;
- Quarantine Custodian Fire action at Lv38 target — **~9.8%**;
- Veteran Ruin Cohort Ruin Press at Lv39 target — **~13.1%**;
- Western War-Sorcerer Ruin Lance at Lv39 target — **~14.8%**;
- Conqueror Shieldbearer Bash at Lv39 target — **~16.8%**;
- Rift Cannoneer Ruin Shell at Lv39 target — **~14.8%**;
- Siege Engineer Cinder Charge at Lv39 target — **~13.1%**.

Representative AoE pressure on the same under-geared reference is approximately:
> **~6.0–11.1% Max HP per target**

This is appropriate. Chapter-9 ordinary danger comes from:
- mixed physical/magical/Ruin/Fire/Lightning pressure;
- Bleed, Burn, Staggered, and Stun where already authored;
- Shieldbearer/Guard defensive tempo;
- construct repair/guard behavior;
- mixed Crownfall formation action economy;

not from healthy one-action deletion.

Completionist Lv45+ bodies reduce these percentages materially and are allowed to clear fragile ordinary units very quickly.

**Verdict: PASS / RETAIN ALL CHAPTER-9 ORDINARY RAW STATS AND POWERS.**

### Formation dependency
No approved exact Chapter-9 ordinary formation table is currently present in the reorganized library.

This pass certifies:
- individual bodies;
- direct-action lethality;
- early/middle/late durability bands;
- role compatibility in mixed encounters.

It does **not** invent exact random formations, weights, encounter counts, or S### placements.

Formation-level action-economy certification remains:
> **OPEN — DATA/STORY-PLACEMENT DEPENDENCY**

This is not a Power gap.

---

## 4. Authored / protected / nonlethal content
### Mercy Warden
Retain:
- Lv39 / **1,650 HP**;
- Warden Staff 210 Power;
- Mercy Pulse 155 AoE;
- Restraint Shock 220 Lightning / 20% Stun;
- Protective Guard Power N/A;
- 0 HP = disabled/disarmed/unable to continue.

On the same deliberately under-geared reference at Lv38, its strongest direct actions are only about **~12.7–12.8% Max HP**.

### Relay-Fever Patient
Retain:
- Lv38 / **1,100 HP**;
- 155 / 165 Lightning / 110 AoE Powers;
- Resist the Surge Power N/A;
- authored-only crisis use;
- 0 HP = stabilized/safely restrained;
- no random spawn / no patient loot.

Its representative direct pressure at Lv37 is roughly **~7.5–8.8% Max HP** before equipment.

The medical-story firewall remains intact:
- no Poison;
- no disease meter;
- no universal Triage resource;
- no universal Mercy/Stabilize command;
- sick/compromised people are not default random enemies.

**Verdict: PASS / RETAIN.**

Exact scene placement remains story-owned because Chapter 9 is not line-complete.

---

## 5. Optional Elite — Ruin Breach Captain
Current body:
- Lv44;
- **4,350 HP**;
- ATK160 / MAG120 / DEF108 / Spirit99 / SPD46 / EVA5 / SR10;
- one bar.

Plausible Crownfall comparison:
- mandatory **~Lv39→40**;
- completionist **~Lv47→49** depending on RH9 timing and incidental optional combat.

On the no-equipment fragile Lv40 reference:
- Breach Captain Cleave — **~20.6% Max HP**;
- Ruin Breach — **~19.0%**;
- Breachline Sweep — **~15.1% per target**;
- Cinder Breach — **~17.5%**.

At Lv49 completionist reference, the same actions fall to roughly **~11–15%**.

Its 4,350 HP remains inside the intended short-Elite endurance band once four active party members, developed Subclasses, legal Cards/Primes, chapter gear, affinities, criticals, and status play are included.

**Verdict: PASS / RETAIN Lv44 / 4,350 HP AND ALL POWERS.**

No support wave, transformation, or extra action is added.

---

## 6. Mandatory boss — Equal Mercy Arbiter
Actual route references:
- mandatory **Lv37**;
- completionist fixed-content **Lv45**;
- high-side **~Lv46**.

Retain:
- Lv40 / **10,025 HP**;
- one continuous HP bar;
- Mercy Protocol → Open Sanctuary at **45% HP** on the same bar;
- no HP refill / no free transition action / no Prime refresh;
- 50% round-start Sanctuary Restraint until one qualifying support-only action or Defend is completed;
- Open Sanctuary permanently removes the action tax and applies +10 Speed / -10 Total Defense.

On the deliberately under-geared Lv37 fragile body, representative direct pressure is:
- Equal Judgment — **~14.6% Max HP**;
- Open Sanctuary Lance — **~16.0%**;
- Sanctuary Reversal total — **~16.3%**;
- Mercy Is Not Surrender — **~10.7% per target**.

The boss therefore derives its difficulty primarily from the **State-A party action tax and resource/tempo decisions**, not excessive raw lethality.

Existing duration certification remains appropriate:
- mandatory normal care-action rotation — **~12–13 rounds**;
- completionist — **~9–10 rounds**;
- high-side — **~8–9 rounds**.

Completionist speedup is intentional and is not dynamically erased.

**Verdict: PASS / FORMALLY VALIDATED v85.**

No raw-stat, threshold, action-tax, or Power change.

---

## 7. Mandatory climax — Commander Rhazek → Bastion Devourer
Actual route references:
- mandatory **Lv40** pre-boss;
- completionist **Lv48** without RH9 before the climax;
- completionist **Lv49** if RH9 is legally cleared before the climax;
- high-side **~Lv50**.

Retain Form I:
- Reforged Commander — Lv43 / **8,431 HP**.

Retain Form II:
- Bastion Devourer — Lv44 / **10,462 fresh HP**;
- genuine fresh body;
- no spillover;
- no free transition attack;
- party HP/MP do not refresh;
- **Prime availability refreshes once** at the fresh Bastion Devourer body.

Retain Exposed Rhazek:
- begins at **18% Form-II HP**;
- same HP bar;
- no second Prime refresh;
- Total Defense -20 / Speed +10;
- Demolition Breaker and Reinforced Advance unavailable.

On the deliberately under-geared Lv40 fragile body, representative danger is:
- Shieldline Break — **~20.0% Max HP**;
- Devouring Cleave — **~22.7%**;
- Bastion Breaker — **~22.5%**;
- prepared Demolition Breaker — **~23.2% per target**;
- exposed Last Line — **~26.2%**;
- Command Collapse — **~15.2% per target**.

That is appropriate for a two-body chapter climax with a visible prepared breaker: dangerous, but not healthy full-HP one-action deletion on the intentionally under-geared fragile reference.

Existing full-encounter duration certification remains appropriate:
- mandatory typical — **~14–16 rounds**;
- recovery-heavy — **~16–17 rounds**;
- completionist — **~11–13 rounds**;
- high-side — **~10–12 rounds**.

The completionist reference is robust across the unresolved RH9 timing because the existing fight passes at both Lv48 and Lv49.

**Verdict: PASS / FORMALLY VALIDATED v85.**

No raw-stat, form, Prime-refresh, prepared-breaker, story-outcome, or Power change.

---

## 8. Regional Hunt #9 — Mercyfallen Behemoth
Current recommendation:
> **Lv50**

Current body:
- Lv50 / **18,882 HP**;
- ATK176 / MAG191 / DEF128 / Spirit137 / SPD46 / EVA5 / SR10;
- one continuous HP bar;
- Broken Restoration heals 650 HP, maximum 2 successful uses.

### Legal player positions
Because the exact Chapter-9 optional-return trigger is not fixed:
- immediate post-Equal-Mercy mandatory route is approximately **Lv38**;
- completionist at that same broad point is approximately **Lv46**;
- intended preparedness target remains **Lv50**;
- if the Hunt is deferred until/after chapter clear, a completionist can naturally reach approximately **Lv50** before Major Hunt #3.

Against the no-equipment fragile reference:

At **Lv38**:
- Mercyfallen Crush — **~31.2% Max HP**;
- Failed Benediction — **~30.2%**;
- Mercy Shock — **~29.0%**;
- Sanctuary Collapse — **~22.7% per target**.

At **Lv46**:
- strongest single-target pressure is roughly **~21.8–23.7%**;
- Sanctuary Collapse is **~17.1% per target**.

At the proper **Lv50 recommendation**:
- Mercyfallen Crush — **~20.9%**;
- Failed Benediction — **~20.0%**;
- Mercy Shock — **~19.1%**;
- Sanctuary Collapse — **~15.0% per target**.

This is the desired Regional-Hunt shape:
- clearly above Chapter-9 route pressure at immediate access;
- manageable for a developed completionist below recommendation;
- appropriately normalized around the stated Lv50 recommendation;
- still below Major Hunt #3.

Its two finite 650-HP heals add at most **1,300 effective HP** and do not create an endless recovery loop.

**Verdict: PASS / RETAIN recommended Lv50 / 18,882 HP AND ALL POWERS.**

### Timing dependency
The exact S### unlock point remains open. Therefore RH9 is not forced into the pre-Equal-Mercy proof, and Rhazek is validated both with and without RH9's 11,000 EXP having been earned.

---

## 9. Major Hunt #3 — Concordance Guardian
Unlock:
> **after Chapter 9**

Current recommendation:
> **Lv54**

Current body:
- Lv54 / **27,400 HP**;
- ATK194 / MAG210 / DEF144 / Spirit151 / SPD49 / EVA5 / SR15;
- Six Faces → Open Concordance on **one continuous HP bar**;
- Open Concordance begins at 50% HP;
- no HP refill;
- no same-bar Prime refresh.

First-access player references:
- mandatory chapter-clear party — **Lv42**;
- completionist after all normally available through-Chapter-9 optional EXP, including Ilyra's newly unlocked Character Quest if completed before the Hunt — approximately **Lv50**, close to Lv51;
- intended recommendation — **Lv54**.

On the no-equipment fragile reference:

At **Lv42 mandatory first access**:
- ordinary Face Verdicts / Ruin Verdict — roughly **~27–30% Max HP**;
- Concordance Pulse — **~20.8% per target**;
- Open Verdict — **~33.1%**;
- Sixfold Wave — **~24.8% per target**.

At **Lv50 completionist**:
- ordinary Face Verdicts — roughly **~20.6–22.8%**;
- Open Verdict — **~25.5%**;
- Sixfold Wave — **~19.0% per target**.

At the proper **Lv54 recommendation**:
- ordinary Face Verdicts — roughly **~18.2–20.1%**;
- Open Verdict — **~22.6%**;
- Sixfold Wave — **~16.8% per target**.

The mandatory Lv42 party is therefore correctly under the Hunt's intended tier. A completionist Lv50 party can challenge it early, while the stated Lv54 recommendation remains meaningful.

The hierarchy remains correct:
> Chapter-9 route bosses < Regional Hunt #9 Lv50 < Major Hunt #3 Lv54

**Verdict: PASS / EXISTING RECERTIFICATION FORMALLY COMPATIBLE WITH v85.**

No raw-stat, Face-cycle, same-bar architecture, recommendation, or Power change.

---

## 10. v85 change ledger
### Numerical changes
> **NONE**

### Power changes
> **NONE**

### Authority/status cleanup
- Chapter-9 player-state anchors made explicit: **Lv37 start → Lv37 Equal Mercy → Lv38 post-Last-Sanctuary → Lv40 Rhazek → Lv42 clear**.
- All six permanent characters counted as available; active cap remains four.
- Subclass access explicitly legal throughout.
- Last Sanctuary's mandatory Chapter-9 awakening is included before Crownfall rather than treated as optional power.
- Chapter-9 ordinary enemy bodies formally validated at their actual Larkspire/Crownfall route bands.
- Mercy Warden and Relay-Fever Patient formally validated as authored nonlethal crisis content while preserving their medical-story firewalls.
- Ruin Breach Captain formally validated at its optional-Elite tier.
- Equal Mercy Arbiter promoted from preliminary recertification to formal v85 validation.
- Commander Rhazek → Bastion Devourer promoted from preliminary recertification to formal v85 validation.
- Regional Hunt #9 formally validated at recommended Lv50 without inventing its exact S### return trigger.
- Rhazek completionist proof now explicitly works in both RH9 timing cases: **Lv48 without RH9 / Lv49 with RH9**.
- Major Hunt #3's existing after-Ch9 Lv54 recertification formally carried forward against both mandatory Lv42 and completionist ~Lv50 party states.
- exact Chapter-9 ordinary formations and exact RH9 within-chapter trigger remain explicit data/story dependencies.

---

# Final Chapter-9 verdict
> **PASS / VALIDATED WITH EXPLICIT FORMATION/HUNT-TIMING DEPENDENCIES**

Validated anchors:
- chapter start **Lv37 mandatory**;
- Equal Mercy Arbiter **Lv37 mandatory / Lv45 completionist**;
- post-Equal-Mercy / Last Sanctuary **Lv38 mandatory / ~Lv46 completionist**;
- Crownfall late route **Lv39→40 mandatory**;
- Rhazek **Lv40 mandatory / Lv48–49 completionist**;
- chapter clear **Lv42 mandatory**;
- Regional Hunt #9 recommendation **Lv50**;
- Major Hunt #3 recommendation **Lv54 after Chapter 9**.

All currently defined Chapter-9 combat bodies and optional difficulty tiers pass without numerical adjustment.

The remaining Chapter-9 combat unknowns are **exact formation/story timing**, not missing Power or failed raw balance.

## Next frontier
> **Chapter 10 — Lv42 start → Lv47 end**, with Subclass access legal throughout and post-Chapter-9 optional progression carried forward normally.
