# Diyse — Character Quest Boss Register
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current exact-sheet closure:** **v90 — dedicated Character Quest boss completion pass**

Current Character Quest boss identities:

| Character | Character Quest | Boss | Exact sheet status |
|---|---|---|---|
| Vaelira | The Sky No One Chose | **Elemental Forecast Construct** | **CLOSED v90** — `ELEMENTAL_FORECAST_CONSTRUCT.md` |
| Cyanis | The Weight of the Crest | **Crest-Exhausted Warden** | **CLOSED v90** — `CREST_EXHAUSTED_WARDEN.md` |
| Nimera | The Archive That Remembers | **None** | no boss by current design |
| Seyrik | The Name That Remains | **Black Host Remnant Captain** | **CLOSED v90** — `BLACK_HOST_REMNANT_CAPTAIN.md` |
| Ilyra | Mercy Has a Voice | **None** | no boss by current design |
| Torren | The Road That Returns | **Old Relay Warden** | **CLOSED v90** — `OLD_RELAY_WARDEN.md` |

## Current architecture locks

### Elemental Forecast Construct
- one continuous HP bar;
- no adds / no transformation;
- visible Forecast cycle **Storm → Blizzard → Heatwave**;
- Lightning / Ice / Fire only;
- Stun / Freeze / Burn mappings retained.

### Crest-Exhausted Warden
- one continuous HP bar;
- no adds / no transformation;
- visible **Primary Load** target state;
- Primary Load is not Taunt and does not remove commands;
- tests Guard / Barrier / Defense / Spirit / healing through visible protection play.

### Black Host Remnant Captain
- one continuous HP bar;
- no transformation;
- exact previously authored kit retained;
- v90 supplies the missing raw body.

### Old Relay Warden
- one continuous HP bar;
- no adds / no transformation;
- v90 deliberately authors the formerly deferred exact numerical sheet;
- Relay Hammer carries 25% Staggered;
- electrical Capacitor Arc / Terminal Discharge carry bounded Stun.

## Numerical boundary — CLOSED v90
The prior blanket statement that exact Character Quest boss bodies were deferred is superseded for the four current combat Character Quests.

All four current Character Quest bosses now have:
- exact Level / HP / ATK / MAG / DEF / Spirit / SPD / EVA / SR;
- explicit direct-damage Power or `Power: N/A`;
- Base Hit;
- action weights / eligibility rules;
- status/stat riders;
- architecture and action-economy firewalls;
- mandatory-vs-completionist paper validation.

Nimera and Ilyra intentionally have no boss and require no numerical boss sheet.
