# Diyse — CL13 Class EXP Working Model

**Status:** ACTIVE WORKING DESIGN — POST-INSERTION NUMERICAL TIMING ON HOLD  
**Current whole-project authority:** v1.98 / Audit113  
**Current fixed caps:** Base CL13 / Subclass CL13  
**Timing hold:** `docs/canon/POST_INSERTION_PROGRESSION_TIMING_HOLD_2026-08-23.md`

This file previously contained a complete 12-chapter CEXP pacing proof built around an obsolete Level ~55 / Level 60 campaign model and the pre-insertion late-game chapter spine. Those chapter-by-chapter budgets are **retired as current guidance** after insertion of Chapter 10 — The Last Blank and the later Level-70 progression authority.

Do not recover or reuse the old Ch1–12 CEXP tables as current implementation numbers. Exact Chapter-10 through Chapter-13 CEXP pacing will be rebuilt in the dedicated progression/item pass.

---

## 1. Current fixed class-level curve

Audit104 remains controlling for the shared cumulative threshold curve unless later explicitly revised:

| Class Level | Cumulative CEXP | CEXP to next |
|---:|---:|---:|
| CL1 | 0 | 150 |
| CL2 | 150 | 200 |
| CL3 | 350 | 250 |
| CL4 | 600 | 350 |
| CL5 | 950 | 400 |
| CL6 | 1,350 | 450 |
| CL7 | 1,800 | 500 |
| CL8 | 2,300 | 550 |
| CL9 | 2,850 | 600 |
| CL10 | 3,450 | 700 |
| CL11 | 4,150 | 800 |
| CL12 | 4,950 | 1,050 |
| CL13 | **6,000** | — |

Base and Subclass CEXP remain separate.

---

## 2. Current Base learning schedule

| Base CL | Major class result | Cumulative CEXP |
|---:|---|---:|
| 1 | Trait I + Base Abilities 1–3 + starting equipment | 0 |
| 3 | Base Ability 4 | 350 |
| 5 | Native advanced equipment permission where authored | 950 |
| 6 | Base Ability 5 + Trait II | 1,350 |
| 9 | Base Ability 6 | 2,850 |
| 12 | Trait III | 4,950 |
| 13 | Base Ultimate | 6,000 |

Do not fabricate class-symmetry permissions that are not separately authored.

---

## 3. Current Subclass learning schedule

| Subclass CL | Major class result | Cumulative CEXP |
|---:|---|---:|
| 1 | donor Primary + Trait I + Ability 1 | 0 |
| 3 | donor Armor | 350 |
| 4 | Ability 2 | 600 |
| 5 | donor advanced equipment / Secondary package where applicable | 950 |
| 6 | Trait II | 1,350 |
| 7 | Ability 3 | 1,800 |
| 9 | Ability 4 | 2,850 |
| **10** | **Equipment Mastery becomes available as Subclass Mastery Node 4; purchasing it unlocks donor Relic access** | **3,450** |
| 11 | Ability 5 | 4,150 |
| 12 | Trait III | 4,950 |
| 13 | Subclass Ultimate | 6,000 |

Equipment Mastery remains a purchased Mastery node; reaching CL10 does not grant it automatically.

---

## 4. Current story timing around Subclasses

Use **The Sixfold Volition**, not `Sixfold Accord`.

Current story timing:
- Chapter 6 ends with Seyrik's conditional permanent recruitment.
- Chapter 7 — The Prison of Names — is the first full-six integration chapter.
- No permanent character has or uses a Subclass before the Volition.
- The Sixfold Volition occurs at the end of Chapter 7 / Cresthaven return.
- All six Subclasses unlock at the Volition at their approved starting state.
- Chapter 8 is the first full mandatory chapter built around sustained post-Volition Subclass use.

Any old CEXP proof that assumed a fresh Subclass begins at the **start** of Chapter 7 is therefore retired.

---

## 5. Recruitment Base-CL inputs

The following authored starting points remain usable working inputs where not separately revised:

| Character | Recruitment | Starting Base CL | Starting cumulative CEXP |
|---|---|---:|---:|
| Cyanis | Chapter 0 | CL1 | 0 |
| Ilyra | Chapter 0 | CL1 | 0 |
| Torren | Chapter 1 | CL4 working | 600 |
| Nimera | Chapter 3 | CL4 working | 600 |
| Vaelira | Chapter 4 | CL7 working | 1,800 |
| Seyrik | Chapter 6 | CL8 | 2,300 |

Values explicitly marked working remain subject to the dedicated progression pass.

---

## 6. Reserve-party CEXP working rule

The approved working decision remains:

**All recruited permanent party members receive 100% of awarded CEXP for their own currently selected class, whether active or in reserve.**

Boundaries:
- the selected Base or Subclass receives the reward;
- the unselected class receives 0 CEXP;
- reserve status does not reduce the reward;
- unrecruited characters do not accumulate CEXP offscreen;
- temporary/guest allies do not enter the permanent class-progression economy unless separately authored.

This keeps the meaningful training choice on **which class the character is developing**, not whether the character occupied one of four active battle slots.

---

## 7. Post-insertion chapter-number map

Current late-game labels:
- Chapter 10 — **The Last Blank**
- Chapter 11 — **Crown Engine / Calder / Custodian / Truth**
- Chapter 12 — **The Reforged March**
- Chapter 13 — **The Last Command**

Historical translation:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

This translation corrects labels only. It does **not** validate old CEXP numbers at the new labels.

---

## 8. Exact numerical pacing now pending

The dedicated progression/item pass must rebuild:

1. expected mandatory/random encounter counts for current Chapters 1–13;
2. exact Light / Standard / Heavy CEXP awards;
3. mandatory authored-combat CEXP budgets;
4. Regional Hunt / Major Hunt CEXP awards;
5. Base-focused, Subclass-focused, split-focus, and optional-heavy simulations;
6. exact timing of Base CL13 and Subclass CL13 under the current Volition placement;
7. late Chapter-12 Synthesis eligibility pacing;
8. interaction with the current **Level-70** character EXP curve;
9. the approximately **55–65 minute** mandatory Chapter 10 contribution;
10. late-game enemy/reward/economy pacing that depends on the extra chapter.

Do not silently compress Chapter 10 out of the curve and do not simply graft an old full-chapter CEXP budget onto it without balance testing.

---

## 9. Synthesis timing boundary

Synthesis remains an endgame completion system under Audit104.

Fixed eligibility still requires:
- Base CL13;
- Subclass CL13;
- all four Core Masteries;
- all four Subclass Masteries;
- the authored resolution/integration requirement;
- 1 unspent MP.

The three mandatory pair-resolution scenes occur in **late Chapter 12**.

Exact numerical proof of when each character can satisfy both CL13 requirements is pending the progression pass and must not be inferred from the retired 12-chapter model.

---

## 10. Superseded assumptions from the prior version of this file

The following are explicitly retired:
- campaign-only Level ~55 finish;
- optional Level 56–60 completion space as the current absolute model;
- Level-60-era endgame assumptions;
- `Sixfold Accord` terminology;
- Subclass unlock at the start of Chapter 7;
- a complete Ch1–12 CEXP budget as current authority;
- Subclass CL13 proof based on the old Chapter-12 campaign ending;
- any exact Ch10/Ch11/Ch12 CEXP value inherited solely from the pre-insertion spine.

Current player level cap is **70**.

---

## 11. Conflict rule

Where this working file conflicts with Audit104 mechanics, Audit107 Volition placement, Audit113 chapter numbering, or the post-insertion progression timing hold, the later authority wins.

No new exact CEXP numbers are canonized by this cleanup.
