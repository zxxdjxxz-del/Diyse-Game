# Diyse — Recruitment and Starting CEXP
**v92 recruitment-aware correction:** 2026-08-29  
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`

## Recruitment starting state
| Character | Recruitment | Starting Base CL | Starting Base CEXP |
|---|---|---:|---:|
| Cyanis | Ch0 | CL1 | 0 |
| Ilyra | Ch0 | CL1 | 0 |
| Torren | Ch1 / after S009 resolution | CL4 | 600 |
| Nimera | Ch3 / S019 | CL4 | 600 |
| Vaelira | Ch4 / after S022 | CL7 | 1,800 |
| Seyrik | Ch6 / chapter-end recruitment resolution | CL8 | 2,300 |

## CEXP handoff rule
- Starting CEXP is the character's authoritative Base-Class total **at the moment that character becomes a recruited permanent party member**.
- There is **no retroactive CEXP** for mandatory rewards earned before recruitment.
- From the first post-recruitment CEXP award onward, every recruited permanent character receives 100% of the awarded package whether active or reserve; it goes only to the selected class.
- A recruitment milestone's starting CEXP is not added a second time as retroactive chapter CEXP.
- Ordinary encounters are stochastic, so the values below are the **canonical expected-route planning checkpoints used for balance simulation**, not a claim that every player earns an identical random-battle total to the point.

## Canonical recruitment-chapter handoff centers
The prior ~5,500 / ~5,050 etc. Volition rows were inherited planning approximations. v92 resolves the recruitment chapters explicitly for simulation.

| Character | Recruitment chapter CEXP before join | Canonical CEXP remaining after join | Notes |
|---|---:|---:|---|
| Torren | ~200 of Ch1's 350 | **150** | joins after Greenhollow resolution; receives the late Ch1 route/clear stream only |
| Nimera | ~250 of Ch3's 550 | **300** | joins at S019; receives the post-recruit Suppressed Archives / command-route stream |
| Vaelira | ~150 of Ch4's 650 | **500** | joins after S022; receives most of the Reaction Annex crisis stream |
| Seyrik | Ch6's 950 occurs before permanent recruitment | **0** | joins at chapter end; first normal campaign CEXP as a permanent member is Ch7 |

These checkpoint splits preserve the chapter budgets exactly:
- Ch1: 200 pre-Torren + 150 post-Torren = **350**;
- Ch3: 250 pre-Nimera + 300 post-Nimera = **550**;
- Ch4: 150 pre-Vaelira + 500 post-Vaelira = **650**;
- Ch6: 950 pre-Seyrik + 0 post-Seyrik = **950**.

## End-Ch7 / Sixfold Volition — corrected mandatory planning centers
| Character | Arithmetic | Base CEXP at Volition | Approx. Base CL | Deficit to CL13 |
|---|---|---:|---:|---:|
| Cyanis | all Ch1–7 | **4,950** | CL12 | **1,050** |
| Ilyra | all Ch1–7 | **4,950** | CL12 | **1,050** |
| Torren | 600 start + 150 late-Ch1 + Ch2–7 4,600 | **5,350** | CL12 | **650** |
| Nimera | 600 start + 300 late-Ch3 + Ch4–7 3,600 | **4,500** | CL11 | **1,500** |
| Vaelira | 1,800 start + 500 late-Ch4 + Ch5–7 2,950 | **5,250** | CL12 | **750** |
| Seyrik | 2,300 start + Ch7 1,200 | **3,500** | CL10 | **2,500** |

## Why Torren and Vaelira can be slightly ahead of the original pair
This is a consequence of their authored recruitment catch-up packages, not retroactive chapter credit.

Torren starts at **600 CEXP / CL4**. Even if he joined only after all Chapter-1 CEXP were already gone, Chapters 2–7 alone add **4,600**, producing a minimum of **5,200** at Volition. Therefore Torren cannot finish below Cyanis/Ilyra's 4,950 without changing his authored starting CL/CEXP or the global recruited-character CEXP rule.

Vaelira similarly enters at **1,800 CEXP / CL7** and joins early enough in Chapter 4 to receive much of that chapter plus all Ch5–7 CEXP.

The v92 correction therefore does **not** erase catch-up. It removes the exaggerated legacy assumption that Torren effectively received almost all Chapter-1 CEXP in addition to his 600-CEXP starting package.

## Optional-content timing note
Optional CEXP is awarded only to characters already recruited when that activity is cleared. Completionist simulations may defer still-available optional content until later recruits join, but must never grant retroactive CEXP for content already completed before that recruitment.
