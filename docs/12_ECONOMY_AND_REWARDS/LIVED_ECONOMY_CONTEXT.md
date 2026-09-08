# Diyse — Lived Economy Context

**Status:** ACTIVE ECONOMY-CONTEXT AUTHORITY  
**Domain:** `12_ECONOMY_AND_REWARDS`  
**Purpose:** define how current economy canon should enter character/NPC reasoning and dialogue without turning authoring calibration numbers into omniscient in-world knowledge.

This file does not reopen the closed G economy. Exact prices, stock, reward values, and commerce rules continue to be owned by the existing files in this domain.

## Current ordinary currency

The current player-facing and ordinary in-world currency term is:
> **G**

The retired term **Auren** must not return as a current ordinary currency.

The authoring calibration `1 economy unit = 200 G` is a design scale. Characters should not speak about "economy units" unless a separate in-world source explicitly establishes that phrase.

## What characters may experience economically

Economic life can appear through concrete needs and constraints:
- food and drink;
- replacement clothing and gear;
- ordinary equipment repair/replacement;
- medicine and field supplies;
- lodging and temporary shelter;
- transport and route access;
- tools and work materials;
- requisition and quartermaster access;
- household or community supply pressure;
- damaged infrastructure;
- delayed deliveries;
- disrupted trade routes;
- scarcity caused by evacuation, occupation, weather, damage, or military movement;
- the practical difference between having money and having something available to buy.

These pressures should be grounded in the current location/story state rather than assumed globally.

## Commerce structure agents may reference when plausible

Current Regional Markets are exactly:
1. Brackenwall
2. Dunmere
3. Caelora
4. Ivorybridge
5. Stonewake
6. Frostmere
7. Westguard
8. Larkspire
9. Cerythvale

Separate current endpoints include:
- **Cresthaven Quartermaster** — long-term requisition/backfill role;
- **Vhalmarch Forward Supply / Requisition** — forward logistics after its relevant story state.

A character only knows or discusses a market/endpoint when their location, travel history, profession, or legitimate information makes that knowledge plausible.

## Price knowledge is not universal knowledge

Exact prices may be used by a character when:
- the item is ordinary and the character has reason to know the local/current price;
- the scene or shop context supplies the price;
- their profession plausibly tracks the cost;
- the information has already been established in continuity.

Agents must not treat every numeric economy file as common knowledge.

Authoring/balance values such as:
- mandatory-route total G;
- completionist direct-cash totals;
- percent-of-route income shares;
- full catalog ceiling values;
- chapter liquidity stress-test balances

are **design authority, not things characters know because they exist in the repo**.

## No invented civilian macroeconomy

Unless an owning current source establishes it, agents must not invent fixed canon for:
- average wages;
- salaries by profession;
- rent tables;
- tax rates;
- universal meal prices;
- exchange rates to a second ordinary currency;
- household income bands;
- standardized ration allotments;
- lending/interest systems;
- national inflation figures.

A scene may establish a local concrete transaction when needed, but that new fact should not silently become a universal economy rule.

## Scarcity and availability

The existence of G does not guarantee availability.

A settlement under pressure may have money moving while particular goods are scarce. A convoy delay, damaged road, evacuation, occupation, weather event, local demand spike, or military requisition can change what is practically obtainable without changing the closed global price architecture by implication.

Likewise, a functioning market should not be written as starving merely because the campaign contains a war.

Location/story authority decides the condition.

## Military and civilian economic language

G rewards do not always have to be imagined as literal coins taken from an enemy body.

Current economy authority already permits appropriate presentation such as:
- requisition credit;
- secured funds;
- bounty;
- operational reserve;
- other authored economic handoffs.

In dialogue, soldiers, quartermasters, civilians, merchants, healers, craftspeople, and administrators may therefore understand the same G economy through different practical language.

## Ordinary people and work

People should have economic roles independent of the party:
- merchants sell because they operate businesses or stalls;
- craftspeople need tools/materials and time;
- transport workers care about routes and loads;
- recovery workers care about housing, supply distribution, records, and movement;
- soldiers and commanders care about requisition, replacement, transport, and reserve capacity;
- healers care about medical stock and the consequences of scarcity;
- households care about food, shelter, repairs, safety, and continuity.

Exact professions and institutions remain owned by current character/world/story files when already established.

## Permanent-six perception examples

These are reasoning lenses, not new mechanical abilities:
- **Cyanis** tends to notice whether supplies, people, transport, and responsibilities actually line up.
- **Ilyra** notices when scarcity changes care quality, rest, sanitation, medicine, or recovery choices.
- **Torren** notices the route and transport causes behind availability problems.
- **Nimera** notices records, classification, provenance, mismatched inventories, and what paperwork does or does not prove.
- **Vaelira** notices technical-resource constraints where elemental infrastructure or regulation is genuinely relevant.
- **Seyrik** notices institutional procedure, military supply logic, and Black Host practices he legitimately knows.

The character files in `01_CHARACTERS` remain the authority for their personalities and knowledge boundaries.

## Dialogue rule

Economic texture should usually enter dialogue as a concrete human problem:
- "We have three beds and seven people."
- a delayed wagon;
- somebody saving a good bottle;
- a repair that must wait for a part;
- the price of replacing something actually being discussed;
- a quartermaster refusing an impossible request;
- a merchant complaining about a blocked route;
- a medic rationing time rather than delivering an economy lecture.

Do not turn ordinary scenes into exposition about the campaign's balance model.

## Runtime-agent boundary

Agent runtime context may carry selected current economy anchors for grounding, but it is a **synthesis layer only**. If runtime context conflicts with this domain, this domain wins.

Primary authority remains:
- `ECONOMY_MASTER.md`
- price/stock owner files in this folder
- current story/location state for local availability.