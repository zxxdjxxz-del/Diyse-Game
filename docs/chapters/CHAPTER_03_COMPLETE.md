# Chapter 3 — The Old City and Last Sentinel — COMPLETE

**Whole-project authority:** Diyse Clean Active Complete Master Canon **v1.64 / Audit79**  
**Chapter line-complete checkpoint:** **Audit77**, plus the bounded S020→S021 Cresthaven correction inherited into v1.64  
**Closed set:** S017–S021 + H01–H04  
**Runtime status:** Story/dialogue/continuity/relationship/affordable-2.5D authority CLOSED; production Godot dialogue Resource conversion and validation COMPLETE.

The exact approved Chapter 3 dialogue lives in `docs/chapters/dialogue/chapter_03/`. The validated production translation lives in `game/content/dialogue/chapter_03/`. Use those sources, not older summaries or the discarded pre-correction S020/S021 transition.

## Controlling scene files

- [S017 — Containment at Caelora](dialogue/chapter_03/S017.md)
- [S018 — Order That Should Not Exist](dialogue/chapter_03/S018.md)
- [S019 — Scholar in Redacted Stacks](dialogue/chapter_03/S019.md)
- [S020 — Oath Sentinel](dialogue/chapter_03/S020.md)
- [S021 — Four Answers, Not One](dialogue/chapter_03/S021.md)
- [H01 — Nimera Takes Over a Table](dialogue/chapter_03/H01.md)
- [H02 — Torren and Maevra, Unsupervised](dialogue/chapter_03/H02.md)
- [H03 — Ilyra and Nimera](dialogue/chapter_03/H03.md)
- [H04 — Last Sentinel Is Not Invited](dialogue/chapter_03/H04.md)

## Production Resource checkpoint

Production Resources:
- `game/content/dialogue/chapter_03/S017.tres`
- `S018.tres`
- `S019.tres`
- `S020.tres`
- `S021.tres`
- `H01.tres`
- `H02.tres`
- `H03.tres`
- `H04.tres`
- `chapter_03_dialogue_registry.tres`

Permanent validators:
- `tests/dialogue/validate_chapter_03_resources.gd` — exact Markdown→Resource speaker/text parity, schema, metadata, locations, triggers, and participants.
- `tests/dialogue/validate_chapter_03_continuity.gd` — authority encounters, Nimera/choose-four handoff, Warden limits, Last Sentinel timing, corrected Cresthaven handoff, geography, optional-scene access, and durable end-state locks.

H01/H02/H03 retain their approved earlier **story-eligibility** points but require actual **Cresthaven location access** before playback, because their approved staging is at Cresthaven. H04 remains post-S021 only. This is runtime gating, not a story rewrite.

## Geography hard lock

**Caelora → Old City / Suppressed Archives → separate Cresthaven**

Cresthaven is not the Warden chamber, a Suppressed Archive room, a wing of the Old City, or a Caeloran district.

### Final S020→S021 handoff

The bounded v1.64 correction is controlling:

1. Defeating the First Command Warden clears the command state and opens a command-record room behind it.
2. The room preserves the authentic judicial declaration and custody authorization as separate inputs plus the false order produced from them. This proves **how the false order was assembled**, while leaving who initiated it and why unresolved.
3. Torren notices a second routing display that reads to him like a map and makes a practical copy of its roads/high ground/water/destination geometry.
4. The party returns to Caelora with the authenticated evidence and Torren's drawing.
5. Mirena recognizes the destination as **Cresthaven — an abandoned Crown outpost in Southhold**.
6. Mirena sends survey/work crews, records staff, medical support, supplies, and security. The party stops for the night.
7. S021 begins **the next morning** with Mirena already at Cresthaven turning the outpost into the party's **working headquarters, temporary until they understand what is going on**.

The older ending in which the party somehow already knew Cresthaven or followed an unexplained “old site reference” is superseded.

## Scene / system locks

- **S017:** containment is not arrest. The sealed recovered Card is still unidentified. Legitimate procedure contains a missing/bypassed initiating declaration; Maevra owns lawful-order verification and Mirena owns substantial political accountability.
- **S018:** exactly two authored nonlethal authority confrontations. Lawful personnel are not farmable enemies. Preserve `The order was protecting itself`, `Prove it`, `I know it is contradictory`, `Belief is not the standard`, and `Neither is pretending`.
- **S019:** Nimera joins permanently. Choose-four becomes meaningful immediately. Maevra remains an authored guest and dialogue cannot assume who the player benches. Nimera's Living Index Tablet is a Conduit that manifests an airborne spear-form for ordinary Attack; Cards remain separate.
- **S019 Hunt branch:** first-pass judgment/adjudication branch is hard-denied with no Hunt prompt or boss tease.
- **S020 Warden:** one HP bar, two authored behavior states, Command Seals + targetable Command Ring pressure, weaker functional equivalents of completed eligible ordinary actions only. No Cards/Primes/Ultimates/unique commands copied; use the Warden's own mechanical strike/emitter.
- **Glassform Rupture:** recovered from a protected Ancient repository/cache before the Warden; it is not a Warden drop or creation.
- **Last Sentinel output:** no pre-Warden Ruby flicker. After defeat the exact machine output is `/PREVIOUS ERROR/` then `/LAST SENTINEL CONFIRMED/`. Only then does the sealed Card resolve to stable deep Ruby. S020 does **not** identify Might or Prime and contains no manifestation.
- **S021:** four bounded answers only — **Prime; Might; Last Sentinel; ultimate meaning still unknown**. Last Sentinel becomes Recovered/usable without manifestation. The first later real-battle use is the first verified modern Prime manifestation/sighting.
- Mirena and Lysara remain substantial political/authority actors. Lawful personnel are not retroactively villainized because a compromised record path existed.
- Chapter 3 establishes only the immediate Cresthaven safe loop; later hub services unlock in later phases.

## Optional hub / relationship locks

- **H01:** mundane Nimera table takeover; no mandatory Prime-history payload.
- **H02:** owns Torren's first deliberate **“Maevra.”** Preserve the impossible-order reread, old `weather: wet` callback, moved-river analogy, left-arm/shoulder callback, and `Don't disappear before morning. / I'll be here.`
- **H03:** Ilyra treats Nimera's minor cut without therapy framing; respect for `no`, `Good fuck or bad fuck?`, terrible bread, and thanks remain.
- **H04:** static Ruby Card case at dinner; no glow/personality/activation/lore dump. Preserve the chair gag and ending **“He's sleeping in the fucking Archive.”**

Pair progression remains: Ch1 Harth/Solmar → Ch2 one involuntary `Torren!` then Harth → H02 first deliberate `Maevra` → T/Mae only later.

## Optional return / affordable-2.5D locks

After the Cresthaven/home beat, the previously denied Archive judgment branch may be returned to for Regional Hunt #3 — Archive Judgment Engine. The player travels back to the Old City/Archive from the separate Cresthaven hub.

Use reusable portraits/poses, papers/seals/tables, authored gates/route states, ordinary interaction poses, camera inserts, machine emitters, lighting, and layered background activity. Do not introduce systemic facility simulation, crowd AI, actor-body mimicry, or physics spectacle to implement closed prose.

## Follow-on implementation rule

The line-complete scene files and validated production Resources are now the Chapter 3 dialogue baseline. Follow-on work may wire world triggers, location access, hub services, encounter consumers, presentation assets, portraits, and other runtime systems, but may not restore discarded geography, alter exact approved dialogue, move relationship milestones, leak future knowledge, change party state, or undo the corrected S020→S021 Cresthaven establishment sequence.
