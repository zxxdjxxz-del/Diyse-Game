# Diyse — Raw-Stat Certification Index
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Current raw-stat certification chain:

- Audit129 — mandatory named/special Ch1–4
- Audit130 — Regulation Crucible Form-I HP correction to 2,400
- Audit131 — mandatory named/special Ch5–8
- Audit132 — mandatory named/special Ch9–13
- Audit133 — 12 current numbered-chapter optional Elites
- Audit134 — all 11 Regional Hunts
- Audit135 — all 6 Major Hunts

Controlled fields:
- Level/recommended level where applicable
- HP
- Attack
- Magic
- Defense
- Spirit
- Speed
- Evasion
- Status Resistance

Exact tables live in:
`09_ENEMIES_AND_ENCOUNTERS`

## Current closure
Mandatory story:
> all 13 numbered chapters certified.

Optional Elite:
> 12 certified; no Ch10 Elite.

Regional Hunts:
> 11 certified.

Major Hunts:
> 6 certified.

## Testing principle
Use these certified lines as regression oracles.

Do not duplicate them into a second editable balance database in this folder.


## Current route-recertification overrides
The Audit129–135 tables remain the historical baseline, but newer mandatory-vs-completionist recertification overrides individual rows as the active pass advances.

Current Chapter-5 override:
- Furnace Tyrant — Lv23 / HP3,400 / ATK100 / MAG72 / DEF66 / Spirit56 / SPD32 / EVA0 / SR5.

Read the current owning `09_ENEMIES_AND_ENCOUNTERS` boss file for the live row.


Current Chapter-6 route-recertification override:
- Crownstorm Roc — Lv26 / HP4,800 / ATK100 / MAG112 / DEF60 / Spirit66 / SPD43 / EVA10 / SR10.


Current Chapter-6 route-recertification overrides:
- Matron Zevraya — Blood Matron — Lv28 / HP4,400 / ATK90 / MAG122 / DEF68 / Spirit76 / SPD40 / EVA5 / SR10.
- Perfected War Mother — Lv29 / HP5,200 / ATK112 / MAG132 / DEF72 / Spirit80 / SPD42 / EVA5 / SR10.


Current Chapter-6 route-recertification override:
- Masked Ruin Vanguard — Seyrik — Lv27 / HP4,000 / ATK104 / MAG79 / DEF63 / Spirit59 / SPD38 / EVA5 / SR10; protected disengagement at 800 HP.


Current Chapter-7 route-recertification result:
- Chainworks Behemoth — **raw line RETAINED** at Lv29 / HP5,135 / ATK109 / MAG57 / DEF77 / Spirit59 / SPD32 / EVA0 / SR5.
- New Power-complete action/support sheet does not require raw-stat inflation.


Current Chapter-7 route-recertification override:
- Warden of the Nameless / Revision Arbiter — Lv34 / HP7,600 / ATK124 / MAG138 / DEF86 / Spirit92 / SPD42 / EVA5 / SR10.


Current Chapter-8 route-recertification result:
- Western Rift Engine — **raw line RETAINED** at Lv36 / HP9,775 / ATK86 / MAG133 / DEF97 / Spirit89 / SPD33 / EVA0 / SR10.
- Completionist overlevel is preserved rather than answered with dynamic/stat inflation.


Current Chapter-8 route-recertification result:
- Marshal Varkesh / Rift Conqueror — **raw lines RETAINED**.
- Marshal: Lv38 / HP7,326 / ATK140 / MAG93 / DEF93 / Spirit85 / SPD44 / EVA5 / SR10.
- Rift Conqueror: Lv39 / HP8,485 / ATK151 / MAG107 / DEF97 / Spirit91 / SPD45 / EVA5 / SR10.
- Completionist overlevel is preserved rather than answered with boss scaling.


Current Chapter-9 route-recertification result:
- Equal Mercy Arbiter — **raw line RETAINED** at Lv40 / HP10,025 / ATK105 / MAG140 / DEF89 / Spirit107 / SPD43 / EVA0 / SR10.
- Completionist overlevel is preserved rather than answered with boss stat inflation.


Current Chapter-9 route-recertification result:
- Commander Rhazek / Bastion Devourer — **raw lines RETAINED**.
- Reforged Commander: Lv43 / HP8,431 / ATK163 / MAG100 / DEF111 / Spirit96 / SPD44 / EVA5 / SR10.
- Bastion Devourer: Lv44 / HP10,462 / ATK175 / MAG131 / DEF107 / Spirit104 / SPD46 / EVA0 / SR10.
- Completionist advantage is preserved rather than answered with dynamic/stat inflation.


Current Chapter-10 route-recertification result:
- Registry Warden — **raw line RETAINED** at Lv49 / HP13,514 / ATK157 / MAG172 / DEF124 / Spirit126 / SPD46 / EVA0 / SR10.
- Its current Power-complete status-neutral kit does not require raw-stat inflation.


Current Chapter-11 route-recertification result:
- Chancellor Othmar Calder — **raw line RETAINED** at Lv54 / HP10,133 / ATK137 / MAG193 / DEF118 / Spirit134 / SPD50 / EVA5 / SR10.
- Crown-Bound Living Anchor — **raw line RETAINED** at Lv55 / HP13,662 / ATK181 / MAG204 / DEF139 / Spirit139 / SPD47 / EVA0 / SR10.
- Active balance pass authors exact support-object values without changing either boss raw body.


Current Chapter-11 route-recertification result:
- The Custodian — **raw line RETAINED** at Lv55 / HP16,017 / ATK177 / MAG190 / DEF144 / Spirit146 / SPD48 / EVA0 / SR10.
- Active balance pass adds exact Acuity Node / Ruin Containment Seal values without changing the Custodian raw body.


Current Chapter-12 route-recertification result:
- Marshal Varkesh — Final Capture — **raw line RETAINED** at Lv58 / HP17,106 / ATK226 / MAG148 / DEF144 / Spirit131 / SPD55 / EVA5 / SR10.
- Exact capture/support architecture is now authored without changing the boss raw body.


Current Chapter-12 route-recertification result:
- Emperor Vaelkor Draeven — **HP ADJUSTED** to Lv60 / HP16,800 / ATK223 / MAG209 / DEF155 / Spirit150 / SPD54 / EVA5 / SR10.
- Sovereign Panoply Unbound — **HP ADJUSTED** to Lv61 / HP20,200 / ATK238 / MAG224 / DEF163 / Spirit157 / SPD55 / EVA0 / SR10.
- v54 changes HP only to hit the 18–20 mandatory-round target; all other raw stats remain as previously certified.


Current Chapter-13 pre-Shelter route-recertification result:
- Last Weapon Archon — **HP ADJUSTED** to Lv63 / HP20,800 / ATK236 / MAG220 / DEF160 / Spirit160 / SPD56 / EVA0 / SR15.
- v56 changes HP only to hit the 15–17 mandatory-round target; all other raw stats remain certified.


Current final-boss route-recertification result:
- Reconstituted Entity — **HP ADJUSTED** to Lv63 / HP22,500 / ATK224 / MAG228 / DEF158 / Spirit163 / SPD55 / EVA5 / SR15.
- The Last Command — **HP ADJUSTED** to Lv64 / HP28,500 / ATK247 / MAG247 / DEF168 / Spirit168 / SPD58 / EVA5 / SR15.
- Non-HP raw stats remain from the inherited certified lines.
- Final mandatory boss pacing target: ~22–24 rounds at Lv61.
- Mandatory story-boss route recertification is complete through the final boss.
