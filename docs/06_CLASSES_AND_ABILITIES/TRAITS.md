# Diyse — Trait Register
**v93 true-battle recovery normalization**  
**Rank milestones:** Rank I — CL1 / Rank II — CL6 / Rank III — CL12  
**Selection rule:** exactly one selected-class Trait package is active: Base Trait while Base class is selected, Subclass Trait while that Subclass is selected.

This file is the controlling current Trait-effect register. It restores the latest accepted Trait mechanics that survived in the working trackers but were reduced to names during the folder migration.

## Base Traits

### Cyanis — Crest Knight — Harmonized Crest
- **Rank I — CL1:** after a damaging **Physical** Crest Knight Ability, prime Cyanis's next damaging **Magical or Hybrid** Crest Knight Ability; after a damaging **Magical** Crest Knight Ability, prime his next damaging **Physical or Hybrid** Crest Knight Ability. The next qualifying opposite-side action consumes the prime for **+10% final damage**.
- **Rank II — CL6:** consumed-prime bonus becomes **+15% final damage**.
- **Rank III — CL12:** consumed-prime bonus becomes **+20% final damage**.
- A Hybrid Ability may consume either primed state but does not itself establish a new prime. One prime maximum; refresh rather than stack; no gauge or extra action.

### Ilyra — Blue Warden — Gentle Continuance
- **Rank I — CL1:** the first direct-healing Ability Ilyra resolves each round restores an additional **5% target Max HP** if that target began the action below 50% HP.
- **Rank II — CL6:** eligible excess direct healing creates **Regen: 4% Max HP per round for 4 rounds**, once per target per action. Regen remains a positive recurring heal; a tick that restores the target to full HP clears Bleed under the global Bleed rule.
- **Rank III — CL12:** Ilyra's cleansing Abilities gain **+10% healing potency**.

### Torren — War Archer — Veteran's Measure
- **Rank I — CL1:** Torren gains **+10 Base Hit** against targets with **Hunter's Measure**.
- **Rank II — CL6:** Torren gains **+5 percentage points Critical Chance** against Hunter's Measure.
- **Rank III — CL12:** damaging War Archer Abilities gain **15% Defense penetration** against Hunter's Measure, subject to the global same-axis penetration cap.
- Hunter's Measure itself remains a shared authored tactical state: **Evasion −10** and **+10 percentage points party Critical Chance** against the target for the remainder of the current round plus the next 2 full normal rounds.

### Nimera — Cardweaver — Living Archive
- **Rank I — CL1:** Nimera's Standard Cards cost **20% less MP**, rounded normally, minimum 1 MP. Between Nimera's turns, Living Archive records the last **2 eligible allied Abilities or Standard Cards** under the Cardweaver copy firewall.
- **Rank II — CL6:** Living Archive capacity increases **2 → 3 eligible actions** per recording window.
- **Rank III — CL12:** Nimera's personal Standard-Card MP reduction increases **20% → 30%**.
- The ordinary archive clears after Nimera completes her next turn and immediately begins a new recording window; **Perfect Recall** is the explicit exception that can preserve one record beyond that window.

### Vaelira — Green Arcanist — Prismatic Flow
- **Rank I — CL1:** the first damaging action each round whose standard element differs from Vaelira's previous damaging action gains **+10% final damage**. Colorless resets the remembered element without receiving the bonus.
- **Rank II — CL6:** that qualifying different-element action also gains **+10 Base Hit / application reliability**, where relevant.
- **Rank III — CL12:** that qualifying action additionally gains **+15% Spirit penetration** on its Magical-derived portion.
- Vaelira's separately authored matching-element status-specialist bonuses remain separate.

### Seyrik — Ruin Vanguard — Severed Command
- **Rank I — CL1:** Ruin Vanguard Abilities that already carry an authored Bleed rider gain **+5 percentage points Bleed application chance**. This never invents Bleed on a move that lacks it and does not modify Basic Attack, Cards, Items, Primes, equipment riders, or Shardfang autonomous attacks.
- **Rank II — CL6:** while Seyrik remains conscious, **Shardfang +10 Base Hit**.
- **Rank III — CL12:** while Seyrik remains conscious, Shardfang additionally deals **+10% final damage**.

## Subclass Traits

### Cyanis — Crest Arcanist — Crest Resonance
- **Rank I — CL1:** all MP-costing Crest Arcanist Abilities cost **2 less MP**, minimum 1 MP.
- **Rank II — CL6:** damaging **Magical / Colorless** Crest Arcanist Abilities gain **+15% Spirit penetration**.
- **Rank III — CL12:** when **Crest Attunement** is consumed, the empowered Ability additionally deals **+10% final damage**.
- **Crest Attunement:** Arcane Lance establishes it through the end of the following round; Cyanis's next **different** Crest Arcanist Ability consumes it for **+15 Base Hit / application reliability**. One state maximum; refresh, not stack; Arcane Lance cannot consume the state it just created.

### Ilyra — Vowblade — Mercy in Steel
- **Rank I — CL1:** when a Vowblade Ability restores HP to a conscious ally other than Ilyra, she gains **Tempered Mercy** through the end of the following round. Her next damaging Vowblade Ability consumes it for **+10% final damage**.
- **Rank II — CL6:** the consuming Ability also gains **+10 Base Hit**, **+10% Defense penetration** on Attack-derived portions, and **+10% Spirit penetration** on Magic-derived portions.
- **Rank III — CL12:** if that empowered Ability hits a target already **Bleeding**, that target takes an additional **+10% final damage**. Evaluate per target for AoE.
- One Tempered Mercy state maximum; qualifying heals refresh rather than stack.

### Torren — Routeweaver — Route Weaving
- **Rank I — CL1:** after Torren uses **Throughline, Set the Pace, Crossroads, or Covered Crossing**, his next damaging Routeweaver Ability before the end of the following round gains **+10 Base Hit**. One stored benefit maximum; refresh rather than stack.
- **Rank II — CL6:** when an ally successfully benefits from one of Torren's route effects, Torren restores **4% Max MP**, at most **once per normal round**. Qualifying benefits include consuming Throughline's discount, acting while Set the Pace is active, triggering Crossroads, or taking a rerouted turn from Covered Crossing/Open the Way.
- **Rank III — CL12:** the first ally each normal round to successfully benefit from one of Torren's route effects gains **+10 Base Hit / application reliability** for that benefiting action where relevant.
- Route Weaving never creates an extra ordinary action.

### Nimera — Proofhunter — Applied Evidence
- **Rank I — CL1:** whenever Nimera successfully applies or refreshes **Hunter's Measure** with a Proofhunter Ability, she gains **Magic +10% for 4 rounds**. Reapplication refreshes rather than stacks.
- **Rank II — CL6:** damaging Proofhunter Abilities gain **+10 percentage points Critical Chance** against Hunter's Measure.
- **Rank III — CL12:** damaging Proofhunter Abilities gain **15% additional applicable defensive-axis penetration** against targets that both have Hunter's Measure and are currently suffering Defense Down or Spirit Down. This stacks with explicitly authored same-axis penetration subject to the global penetration cap.

### Vaelira — Axiomblade — Formal Equivalence
- **Rank I — CL1:** when Vaelira deals damage with a single-element **Fire / Ice / Lightning / Earth** Ability, that element becomes her current expression through the end of the following round. Her next **Neutral damaging Axiomblade Ability** adopts that stored element and consumes the expression. Authored elemental Axiomblade Abilities are never overwritten; multi-element actions do not establish an expression; one expression maximum.
- **Rank II — CL6:** a Neutral Axiomblade Ability that consumes the expression gains **+10% final damage**.
- **Rank III — CL12:** that consuming Ability also gains **+15% Defense penetration** on Physical-derived portions and **+15% Spirit penetration** on Magical-derived portions.

### Seyrik — Ruin Warden — Ruin's Mercy
- **Rank I — CL1:** whenever Seyrik actually restores HP to himself from an authored **Drain**, also restore HP equal to **15% of the actual HP restored to Seyrik** to the conscious other ally with the lowest HP%. Cannot revive; ties use stable party-slot order.
- **Rank II — CL6:** shared recovery increases **15% → 25%**.
- **Rank III — CL12:** whenever a Ruin Warden Ability restores HP to a conscious ally, that ally gains **+10 Status Resistance through the end of the following round**. Reapplications refresh rather than stack.

## Firewall
- These are Trait effects, not separate commands.
- Do not reintroduce retired Card Seals, Imprints-as-global-resource, Break/Stagger meters, Brace, or any historical trait text superseded by these later accepted packages.
