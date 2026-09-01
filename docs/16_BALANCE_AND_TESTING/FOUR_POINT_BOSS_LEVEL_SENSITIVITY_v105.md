# Diyse — Four-Point Boss Level Sensitivity — v105

**Status:** WORKING DIFFICULTY STUDY / NOT OWNER CANON  
**Global test layer:** enemy direct-damage Power × **1.20**  
**Purpose:** compare mandatory-route Player Level against the highest practical pre-boss Player Level while holding equipment, consumables, selected classes/learned ability set, tactics, and boss owner mechanics constant.

## Isolation rule
This pass isolates **Player Level** as the route advantage.

Within each boss pair:
- same active party;
- same ordinary equipment;
- same consumable stock;
- same selected classes and learned ability set as the mandatory snapshot;
- same tactical policy;
- no Relic/Legacy advantage;
- no extra optional-only abilities are granted to the max-level line;
- no Prime is used in the core comparison;
- only Player Level and the natural-stat changes caused by that Player Level differ.

Therefore the max-level line is deliberately conservative. A real exhaustive route may also have extra CEXP/abilities, Cards, Relics/Legacies, or broader Prime options.

The ×1.20 layer affects hostile ordinary direct-damage Power only. HP, boss raw stats, status chance/magnitude, AI, cooldowns, support healing, support actions, form architecture, and turn count are unchanged.

This is a calibrated design-layer stochastic sensitivity, not runtime-engine QA.

---

# 1. Route pairs

## Chapter 3 — First Command Warden
Current owner route levels:
- mandatory — **Lv11**;
- fixed completionist — Lv12 approaching Lv13;
- practical high-side / max-preboss reference — **~Lv13**.

Core comparison:
> **Lv11 vs Lv13**

Active four:
- Cyanis
- Ilyra
- Torren
- Nimera

Same conservative ordinary equipment both lines:
- Cyanis — Dunmere Steel / Crest Plate / Yahtrean Shield;
- Ilyra — Blue Wardrod / Blue Warden Mail / Warding Focus;
- Torren — Yahtrean War Bow / War Archer Gear;
- Nimera — Twin Token / Cardweaver Garb.

## Chapter 6 — Matron Zevraya → Perfected War Mother
Current owner route levels:
- mandatory — **Lv24**;
- fixed completionist — Lv27;
- high-side / max-preboss reference — **~Lv28**.

Core comparison:
> **Lv24 vs Lv28**

Active four:
- Cyanis
- Ilyra
- Torren
- Vaelira

Same conservative ordinary equipment both lines:
- Cyanis — Deepforge Blade / Caeloran Plate / Yahtrean Shield;
- Ilyra — Crucible Wardrod / Warden Fieldmail / Warding Focus;
- Torren — Command War Bow / Annex Guard Mail;
- Vaelira — Arcanist Staff / Green Arcanist Garb.

Important:
> this pass uses Zevraya's **current owner Reservoir action structure**, not the separate working non-diluting Reservoir candidate. That structural candidate is evaluated elsewhere.

## Chapter 9 — Commander Rhazek → Bastion Devourer
Current owner route levels:
- mandatory — **Lv40**;
- fixed completionist — Lv48–49;
- exhaustive high-side / max-preboss reference — **~Lv50**.

Core comparison:
> **Lv40 vs Lv50**

Same active four:
- Cyanis
- Ilyra
- Torren
- Vaelira

Same prepared ordinary equipment both lines:
- Cyanis — Deepforge Blade / Crest Plate / Yahtrean Shield;
- Ilyra — Crucible Wardrod / Blue Warden Mail / Warding Focus;
- Torren — Storm War Bow / War Archer Gear;
- Vaelira — Veycross Battlestaff / Green Arcanist Garb.

The mandatory selected-class/learned-ability package from v101 is used on both level lines.

## Chapter 12 — Emperor Vaelkor Draeven → Sovereign Panoply Unbound
Current owner route levels:
- mandatory — **Lv56**;
- fixed completionist — Lv66;
- high-side / max-preboss reference — **~Lv67**.

Core comparison:
> **Lv56 vs Lv67**

Same active four:
- Cyanis
- Ilyra
- Torren
- Vaelira

Same late ordinary equipment both lines:
- Cyanis — Deepforge Blade / Crestguard Plate / War Shield;
- Ilyra — Crucible Wardrod / High Warden Mail / Warding Focus;
- Torren — Storm War Bow / Campaign Mail;
- Vaelira — Veycross Battlestaff / Arcanist Weave.

The mandatory selected-class/learned-ability package from v102 is used on both level lines.

---

# 2. Natural-stat advantage from level only

Holding equipment/classes constant, the approximate primary-offense increase from mandatory to max-preboss level is:
- Ch3 Lv11 → Lv13 — **~+6%**;
- Ch6 Lv24 → Lv28 — **~+8%**;
- Ch9 Lv40 → Lv50 — **~+16%**;
- Ch12 Lv56 → Lv67 — **~+16%**.

HP/Defense/Spirit rise simultaneously, so later optional leveling buys substantially more safety than the small early-game level gaps.

The modeled fight-duration center is shortened only by this same-level-driven offensive gain. No extra optional class kit is used to accelerate the max-level line.

---

# 3. 20,000-run ×1.20 results

## Summary

| Chapter / boss | Level | Win rate | Any temporary KO | Wipe | Mean ending HP |
|---|---:|---:|---:|---:|---:|
| Ch3 First Command Warden | **Lv11 mandatory** | **100%** | **~0.13%** | **0%** | **~67.0%** |
| Ch3 First Command Warden | **Lv13 max** | **100%** | **~0.01%** | **0%** | **~67.9%** |
| Ch6 Zevraya → War Mother | **Lv24 mandatory** | **100%** | **~4.4–4.8%** | **0%** | **~62.1%** |
| Ch6 Zevraya → War Mother | **Lv28 max** | **100%** | **~0.7–1.0%** | **0%** | **~63.2%** |
| Ch9 Rhazek → Bastion Devourer | **Lv40 mandatory** | **100%** | **~0.45–0.5%** | **0%** | **~61.7%** |
| Ch9 Rhazek → Bastion Devourer | **Lv50 max** | **100%** | **~0–0.02%** | **0%** | **~64.2%** |
| Ch12 Vaelkor → Panoply | **Lv56 mandatory** | **100%** | **~6.8–7.0%** | **0% observed** | **~57.0%** |
| Ch12 Vaelkor → Panoply | **Lv67 max** | **100%** | **~0.3–0.4%** | **0%** | **~60.5%** |

## Historical-calibration check
The same model at current authored Power (×1.00) lands close to the existing late true-battle KO evidence:
- Rhazek Lv40 — ~0.09% modeled any-KO vs **0.08%** in v101;
- Vaelkor Lv56 — ~1.3% modeled any-KO vs **1.98%** in v102.

Therefore treat the exact percentages as sensitivity estimates, not runtime guarantees, but the relative movement is useful.

---

# 4. Read by chapter

## Chapter 3
×1.20 is still far too safe for a mandatory major boss if the revised goal is that KOs become a meaningful consequence of weak play/preparation.

The max-level line is safer, but the difference is mostly academic because both are near-zero KO environments.

Verdict:
> **GLOBAL +20% ALONE INSUFFICIENT — LOCAL PRESSURE TUNING REQUIRED**

First Command Warden has several action-tax/non-damage windows:
- Command Seal;
- Ring Preparation/cancel interaction;
- weaker Recorded Analogues.

Simply increasing every hit further is inefficient compared with tightening how often the fight produces meaningful pressure.

## Chapter 6
×1.20 creates a visible level-driven safety gap even under the current owner structure:
- Lv24 mandatory — about **4–5% any-KO**;
- Lv28 max — about **1%**.

However this still understates the desired mandatory danger.

Separately, the already-open non-diluting Reservoir structural candidate plus ×1.20 has shown a much stronger profile. Therefore Zevraya is evidence that **structural action-density correction + the global floor** is more effective than escalating the universal scalar.

Verdict:
> **LEVEL GAP WORKS / CURRENT OWNER PRESSURE STILL TOO SAFE / STRUCTURAL CANDIDATE REMAINS PREFERRED**

## Chapter 9
Rhazek remains unexpectedly safe even with ×1.20:
- mandatory rises from the historical ~0.08% KO environment to only around **0.5%**;
- max-level same-gear becomes essentially KO-free.

This is a clear local-fight issue rather than evidence that +20% is too small globally.

Rhazek's long fight contains:
- Hold the Line support turns;
- a visible Protected Preparation;
- an exposed low-defense end segment;
- strong player sustain/mitigation by this point in progression.

Verdict:
> **GLOBAL +20% ALONE INSUFFICIENT — RHAZEK NEEDS BOSS-LOCAL PRESSURE TUNING**

## Chapter 12
Vaelkor reacts much more strongly to ×1.20:
- mandatory any-KO rises from the old very-safe ~2% historical environment toward **~7%**;
- max-level same-gear remains below **1%**.

This proves the Player-Level gap is materially rewarding while the equipment is identical.

But even this line still produced no meaningful wipe tail under competent prepared play.

Verdict:
> **PROMISING BUT STILL BELOW THE NEW CLIMAX-DANGER TARGET**

Vaelkor likely needs a smaller local pressure increase than Rhazek because the global scalar is already doing useful work here.

---

# 5. Supplemental boss-only scalar scan

To determine whether simply raising the universal scalar further would solve the weak bosses, the same snapshots were sampled at ×1.25 / ×1.30 / ×1.35.

Approximate mandatory any-KO movement:

| Boss | ×1.20 | ×1.25 | ×1.30 | ×1.35 |
|---|---:|---:|---:|---:|
| First Command Warden | ~0.1% | ~0.2% | ~0.4% | ~0.5% |
| Zevraya | ~4.8% | ~6.7% | ~8.8% | ~11.7% |
| Rhazek | ~0.5% | ~0.7% | ~1.2% | ~1.5% |
| Vaelkor | ~7.0% | ~10.3% | ~13.6% | ~17.4% |

No meaningful wipe tail appears before the very high end; even ×1.35 remains inefficient for First Command Warden and Rhazek.

This is strong evidence against solving the campaign by pushing the **global** scalar above 20–25% merely to rescue low-pressure boss architectures.

---

# 6. v105 conclusion

The requested mandatory-vs-max-level same-equipment test supports a two-layer difficulty model:

1. **Global enemy direct-damage floor: ×1.20 remains promising.**
   - ordinary-enemy Chapter-5 safety work already supports it;
   - it meaningfully increases boss danger where the encounter already has healthy pressure structure;
   - max-preboss Player Level creates a clear safety reward without better gear.

2. **Major bosses need local pressure tuning on top.**
   - Chapter 3 First Command Warden — local pressure/action-density pass;
   - Chapter 6 Zevraya — use/finish the non-diluting Reservoir structural candidate;
   - Chapter 9 Rhazek — local pressure/mechanic pass;
   - Chapter 12 Vaelkor — smaller local climax-pressure pass after ×1.20.

Do **not** raise the whole enemy roster to ×1.35 merely because First Command Warden or Rhazek stay safe.

Current working recommendation:
> **Keep ×1.20 as the global test floor and tune boss pressure individually above it.**

No owner Power values are changed by this report.
