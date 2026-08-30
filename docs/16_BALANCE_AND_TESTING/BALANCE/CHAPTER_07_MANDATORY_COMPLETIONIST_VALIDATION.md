# Chapter 7 — Mandatory vs Completionist Enemy/Boss Validation

**Version:** v83  
**Status:** **PASS / VALIDATED WITH EXPLICIT PLACEMENT DEPENDENCIES**  
**Power-audit status:** **CLOSED — no direct-damage Power changed**

## Purpose
Validate Chapter 7 against the player state that actually exists at each point rather than treating **Lv32** as the whole-chapter baseline.

Chapter 7 is the first full mandatory chapter with all six permanent characters available as one roster:
- Cyanis
- Ilyra
- Torren
- Nimera
- Vaelira
- Seyrik

The active battle party remains:
> **maximum 4**

Sixfold Volition occurs only after the Prison/Change resolution at chapter end. Therefore:
- Chapter-7 mandatory encounters are validated with **Base Classes**, not Subclasses;
- Subclasses do not contribute to Chainworks, Veycross, Prison, First Registrar's Shade, Rift Gate Colossus if attempted before Volition, or the Revision Arbiter;
- post-Volition optional content may use newly unlocked Subclasses according to its own access/training state.

The direct-damage Power audit remains closed. Existing Powers are retained unless a specific encounter fails its intended role.

---

## 1. Chapter-level anchors
Current Chapter-7 progression:
> **Lv27 chapter start → Lv32 chapter end**

Mandatory EXP:
- chapter start: **69,300 EXP = Lv27**;
- Chainworks Behemoth planning point: **~73,300 EXP = Lv27**;
- late Prison / pre-Warden: **92,020 EXP = Lv30**;
- post-Warden: **97,520 EXP = Lv31**;
- Volition handoff / chapter clear: **100,600 EXP = Lv32**.

Fixed optional advantage before Chainworks is approximately **21,900 EXP**, producing a completionist comparison of roughly **Lv31** there.

Late Chapter-7 fixed optional progression can place a completionist route around:
- **Lv33 before Regional Hunt #7 if the Hunt itself is excluded**;
- **Lv34 before the Revision Arbiter** when Regional Hunt #7 is also cleared;
- high-side incidental/Elite progression can approach **Lv35**.

### Practical encounter bands
- Ashford / early Chainworks: mandatory **Lv27→28**, completionist **Lv30→31**;
- Veycross / transfer corridor: mandatory **~Lv28→29**, completionist **~Lv31→32**;
- Prison of Names: mandatory **~Lv29→30**, completionist **~Lv33→34**;
- chapter clear: mandatory **Lv32**.

Completionist advantage comes from higher level, optional gear/rewards, Cards/Primes, and party optimization among six available characters. It does **not** grant a fifth active turn.

---

## 2. Ordinary enemies — Ashford / occupation band
Relevant early identities:
- Occupation Infantry — Lv27 / 760 HP
- Brand Enforcer — Lv28 / 900 HP
- Chain Enforcer — Lv28 / 980 HP
- Red Brand Adept — Lv28 / 680 HP
- Beast-Pen Stalker — Lv28 / 720 HP

Target player state:
- mandatory **Lv27→28**;
- completionist **Lv30→31**.

Representative conservative checks against a fragile Base-Class Vaelira body keep the strongest ordinary single-target actions below roughly **18% Max HP** at mandatory chapter-entry level. AoE pressure is materially lower per target. The sturdier party members sit well below those percentages.

The early roster therefore gets its danger from:
- mixed physical/magical pressure;
- Bleed / Burn / Staggered use;
- formation action economy;
- target-priority decisions;

rather than one-action deletion.

HP values in the **680–980** range remain ordinary-enemy bodies for a four-character Chapter-7 party.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

---

## 3. Ordinary enemies — Veycross / Rift Gate band
Relevant identities:
- Rift Gate Trooper — Lv29 / 960 HP
- Rift Artillerist — Lv29 / 650 HP
- Gate Projector Drone — Lv29 / 600 HP

Target player state:
- mandatory **~Lv28→29**;
- completionist **~Lv31→32**.

The roster correctly shifts toward mixed Ruin/Lightning pressure without creating a raw-durability spike. Artillerist/Drone remain priority targets, while Trooper supplies the sturdier front body.

Completionist parties are allowed to erase fragile backline bodies quickly; this is a reward for optional progression, not a reason to scale the enemies upward.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

---

## 4. Ordinary enemies — Prison of Names band
Relevant identities:
- Registration Guard — Lv30 / 1,000 HP
- Name Clerk — Lv30 / 720 HP
- Redaction Adept — Lv30 / 760 HP
- Role Echo — Lv31 / 820 HP
- Nameless Executor — Lv31 / 1,180 HP

Target player state:
- mandatory **~Lv29→30**;
- completionist **~Lv33→34**.

Nameless Executor is the strongest ordinary physical body in the batch. Against a conservative fragile Lv30 player reference, its 230-Power physical strike and 245-Power Ruin strike remain about **15% Max HP** each; they are threatening in formation context but not deletion attacks.

Role Echo remains bounded at:
> **70% of completed source total Power, clamp 100–220**

and cannot copy riders, permanent state, Prime commands, or command identity.

The Prison roster is therefore safe mechanically while retaining its intended identity pressure.

**Verdict: PASS / RETAIN.**

No raw-stat or Power change.

### Formation boundary
Chapter 7 is not line-complete and no approved exact ordinary-formation table is currently present in the reorganized library.

This pass certifies:
- individual bodies;
- direct-action lethality;
- ordinary durability at early/mid/late chapter levels;
- role compatibility in mixed encounters.

It does **not** invent exact random formations, weights, scene IDs, or encounter counts.

Exact formation-level action-economy certification remains:
> **OPEN — DATA/STORY-PLACEMENT DEPENDENCY**

This is not a Power gap.

---

## 5. Authored / protected Chapter-7 identities
Power-complete authored identities:
- Beast Handler + Bound Rift Hound
- Resistance Saboteur
- Controlled Prisoner
- Command-Seal Warden

Their current Lv29–31 bodies and action kits fit the same Chapter-7 player band as the surrounding ordinary roster.

Controlled Prisoner remains explicitly nonlethal. The Bound Rift Hound encounter does not automatically establish the animal's death at 0 HP.

Because Chapter 7 is not line-complete, exact placement, formation partners, scene-specific protection conditions, and rewards remain story-owned.

**Verdict: PASS ON KITS / OPEN — EXACT PLACEMENT.**

No authored-special Power changed.

---

## 6. Optional Elite — First Registrar's Shade
Current body:
- **Lv33**
- **2,950 HP**
- ATK104 / MAG116 / DEF76 / Spirit82 / SPD44 / EVA10 / SR10
- one bar

Plausible access:
- mandatory **~Lv29→30**;
- completionist **~Lv33→34**.

A conservative four-character serious offense using currently available Base-Class tools produces approximately:
- mandatory Lv30: **~1,070 HP/round** before Cards, Prime burst, affinities, criticals and status value;
- completionist Lv34: **~1,190 HP/round** before the same burst layers.

That places 2,950 HP at roughly:
- mandatory **~2.8 serious rounds**;
- completionist **~2.5 serious rounds**;

before Preserve Record / action variance.

This is inside the standing optional-Elite target of roughly **2–4 serious party rounds**.

**Verdict: PASS / RETAIN 2,950 HP.**

No raw-stat or Power change.

---

## 7. Mandatory named encounter — Chainworks Behemoth
Actual route anchors:
- mandatory **Lv27**;
- completionist fixed-content **Lv31**;
- high-side **~Lv32**.

Retain:
- Lv29 / **5,135 HP**;
- exactly three 240-HP Restraint Anchors;
- Bound → Freed on one continuous HP bar;
- normal release at 55% HP or early release after 2+ Anchors are destroyed;
- no HP refill, free transition attack, or Prime refresh.

Existing duration remains appropriate:
- mandatory center **~9 rounds**;
- completionist **~6–7 rounds**;
- high-side **~5–6 rounds**.

Seyrik's presence expands the roster's offensive options, but with only four active slots he does not add a fifth action. The completionist shortening is deliberate and remains within the intended reward band.

**Verdict: PASS / FORMALLY VALIDATED v83.**

No raw-stat, Anchor, or Power change.

---

## 8. Mandatory climax — Warden of the Nameless / Revision Arbiter
Actual route anchors:
- mandatory **92,020 EXP = Lv30**;
- completionist fixed-content **120,720 EXP = Lv34**;
- high-side **~Lv35**.

Retain:
- Lv34 / **7,600 HP**;
- 3-layer Closed Record opening assertion gate;
- one continuous HP bar;
- Revision Claim action-variation tax;
- Open Revision at 40% HP with two short 40%-reduction layers;
- no fresh body and no Prime refresh.

Sixfold Volition has **not** happened yet, so neither baseline receives Subclass access for this fight.

Existing duration remains appropriate:
- mandatory **~12–13 rounds**;
- completionist **~9–10 rounds**;
- high-side **~8–9 rounds**.

The completionist route is meaningfully safer/faster without bypassing the identity/assertion mechanics.

**Verdict: PASS / FORMALLY VALIDATED v83.**

No raw-stat or Power change.

---

## 9. Regional Hunt #7 — Rift Gate Colossus
Current recommendation:
> **Lv38**

Current body:
- Lv38 / **13,276 HP**
- ATK144 / MAG127 / DEF107 / Spirit98 / SPD36 / EVA0 / SR10
- one continuous bar
- Marching Protocol at 50% HP

Chapter-7 access does **not** mean story-route difficulty.

Reference positions:
- mandatory chapter-clear party: **Lv32**;
- completionist before clearing this Hunt, depending on timing and prior optional content: approximately **Lv33–36**;
- intended preparedness target: **Lv38**.

Conservative fragile-body checks at Lv32 place:
- Gate Hammer around **24% Max HP**;
- Rift Cannon around **17%**;
- Gate Pulse around **12% per target**;
- Marching Crush around **26%**.

This is appropriately dangerous but remains below healthy full-HP one-action deletion.

At the Lv38 recommendation, conservative four-character Base-Class serious throughput is roughly **1,190 HP/round before Cards, Prime burst, affinities, criticals and higher optimization**, implying about **11 serious rounds** against the raw body before those optional burst layers.

That is appropriate Regional-Hunt endurance.

**Verdict: PASS / RETAIN Lv38 AND 13,276 HP.**

No Regional-Hunt Power change.

---

## 10. Major Hunt #2 — Crownless Siege Marshal → Crownless War Engine
Unlock:
> **after Chapter 7**

Current recommendation:
> **Lv41**

First-access player references from the existing recertification:
- mandatory: **~Lv32**;
- completionist with all normally available optional EXP: **~Lv37**.

Retain:
- Crownless Siege Marshal — Lv40 / **13,600 HP**;
- Crownless War Engine — Lv41 / **16,900 fresh HP**;
- combined raw body HP **30,500**;
- genuine fresh Form II, therefore Prime availability refreshes once at the War Engine body;
- no third form.

Regional Hunt #7 recommends Lv38, so the Lv41 Major-Hunt recommendation remains a clear tier above it even for a completionist route.

The prior later-unlock recertification already accounts for the fresh-body Prime refresh with the larger combined HP package. Chapter-7 validation exposes no contradiction requiring reopening that work.

**Verdict: PASS / RECERTIFICATION CARRIED FORWARD AS FORMALLY COMPATIBLE WITH v83.**

No Major-Hunt Power or raw-stat change.

---

## 11. Sixfold Volition boundary
Sixfold Volition occurs after the Chapter-7 Prison/Change resolution and returns the party to Cresthaven.

Therefore:
- all Chapter-7 mandatory combat above is pre-Subclass;
- the chapter-clear party reaches approximately **Lv32** before entering the post-Volition progression state;
- Chapter 8 is the first full main-story chapter designed around Subclass access;
- post-Volition Character Quests / Major Hunt #2 may begin benefiting from Subclass training, but that does not retroactively alter Chapter-7 encounter validation.

---

## 12. v83 change ledger
### Numerical changes
> **NONE**

### Power changes
> **NONE**

### Authority/status cleanup
- Chapter-7 start/middle/end level anchors made explicit.
- Seyrik counted as a permanent playable roster member throughout Chapter 7; active cap remains four.
- Sixfold Volition explicitly excluded from all pre-climax Chapter-7 combat baselines.
- Chapter-7 ordinary roster validated at its early/mid/late bands.
- First Registrar's Shade formally validated at its actual late-chapter band.
- Chainworks Behemoth and Revision Arbiter promoted from preliminary boss recertification to formal Chapter-7 validation.
- Rift Gate Colossus retained as intentionally above-route Lv38 Regional Hunt.
- Major Hunt #2's existing after-Ch7 Lv41 recertification carried forward with no contradiction.
- authored-special placement and exact ordinary formations remain explicit data/story dependencies.

---

# Final Chapter-7 verdict
> **PASS / VALIDATED WITH EXPLICIT PLACEMENT DEPENDENCIES**

Validated anchors:
- chapter start **Lv27 mandatory**;
- Chainworks Behemoth **Lv27 mandatory / Lv31 completionist**;
- Prison late band **~Lv29→30 mandatory / ~Lv33→34 completionist**;
- Revision Arbiter **Lv30 mandatory / Lv34 completionist**;
- chapter end / Sixfold Volition **Lv32 mandatory**;
- Rift Gate Colossus recommendation **Lv38**;
- Major Hunt #2 recommendation **Lv41**, after Chapter 7.

All currently defined Chapter-7 combat bodies and optional difficulty tiers pass without numerical adjustment.

The remaining Chapter-7 combat unknowns are **formation/story placement**, not missing Power or failed raw balance.

## Next frontier
> **Chapter 8 — Lv32 start → Lv37 end**, with Sixfold Volition already complete and Subclass access now legal for the full chapter.
