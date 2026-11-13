# Junction 2026: What People Want to Build

Source: Junction Community Discord, read 2026-11-12. That covers about 115 real 2026 posts in #team-building, about 95 people in #introduce-yourself, plus #connect and #general. Counts are approximate because many posts span several spaces.

**The main point: about 85% of posts are skill profiles that say "open to any track". Fewer than 10 name a concrete idea.** Most teams will decide what to build Friday night, once the challenges drop.

## Who's coming
- About 2,000 builders. A Discord poll found about 65% travelling from outside Finland.
- About 65% are students; the rest are working engineers, founders and serial hackathon winners.
- The big groups come from Finland (Aalto, LUT), India, Italy, the UK (several from Imperial), Spain and Portugal.
- Most people are AI/LLM-agent engineers or full-stack devs (about 55–60%). Next come ML researchers (Meta, CERN, ETH, Imperial), then hardware/embedded people (about 12–17).
- There are very few designers or business people.

## Spaces, from most to least crowded

| Space | Approx. people/posts | What they want to build | Tech named |
|---|---|---|---|
| **Agentic AI / LLM** | 40+ (the most crowded) | Agent orchestration, RAG, trust/guardrails for agents, "not another GPT wrapper" | Claude Code, MCP, LangGraph/CrewAI, n8n, Ollama |
| **Hardware / robotics / physical AI** | ~15 | Arduino Hardware Lab builds, drones, ROS2, VLM + robotics. Several beginner teams just want to learn | Arduino UNO Q, NVIDIA, ESP32, Raspberry Pi, Atech "physical API for agents" |
| **Healthcare / bio** | ~10 | A health summary patients carry and doctors can trust, AI for early disease detection, triage of data from smart devices | Open health datasets |
| **Cybersecurity × AI** (not an official track) | ~7 | Intrusion detection, checking agent actions before they run, AI security for apps | OpenCV |
| **Fintech / quant** | ~5–7 | Prediction-market and trading analytics, e-invoicing | Polymarket and Yahoo Finance APIs |
| **Data** | ~5 | Pipelines, forecasting, LLMs over messy data, sports analytics | Keboola, Databricks |
| **Defence / drones** | ~5 | Counter-drone decision support, monitoring drones | |
| **Civic / edu / sustainability / agritech** | ~8 | Knowledge maps, a circular farm with IoT, public services | IoT |
| **Quantum** | ~4 | Quantum ML for disease detection, quantum-grade optimizers for hardware | |
| **AI infrastructure (Verda's track)** | ~2 | Local agent orchestration | **Verda mentioned 0 times** |

## Concrete ideas people have stated
1. **tiyuk99 + hadsamer:** Arduino/NVIDIA embedded × AI, robotics with VLMs, maybe VR. Strong team: 1st at PwC, BME robotics and n8n; 2nd at ElevenLabs.
2. **Meg:** a portable patient health summary that doctors trust, pitched toward investors. Team full.
3. **senthazalravi:** "Odin, the Bot Father", local-first agent orchestration. A CEO agent hires and fires sub-agents, controlled over Telegram and WhatsApp.
4. **Kir:** a "trust layer for the agentic web".
5. **Tuguldur:** Tollgate, a control layer that checks agent actions before they reach real systems.
6. **D_sab's team (French cyber engineers):** Cybersecurity × AI. They say they're studying past winners and aiming for 1st.
7. **zineb_hazm:** AI and quantum ML for early detection of breast cancer.
8. **Michella:** triage of health data from smart devices, plus monitoring drones.
9. **Gab:** an AI knowledge-map learning tool (Risorgi). He came 2nd at the Cursor and Claude hackathons.
10. **Victor Onofre:** quantum-grade operations-research optimizers applied to hardware challenges.
11. **Boualem:** Green Loop Farm, a circular farm (aquaponics, poultry, bees, solar) with AI and IoT. A prototype already exists, which is a risk under the no-prior-code rule.
12. **roxer25:** "something very ambitious in mobility" using the Hardware Lab.
13. **arslannizzet1:** basketball analytics with LLMs.
14. **Watcher:** prediction-market and trading analytics.
15. **Dynatos:** LLMs over messy data. The team includes a YC company's ex-chief of staff.
16. **Cala (sponsor):** the "Make Unicorns Real" challenge, a product for founders or VCs built on Cala's company/people/funding knowledge graph (API/MCP).

## Strong players to watch
| Who | Why |
|---|---|
| tiyuk99 | Multiple 1st places. Hardware × AI × VLMs |
| Blacbrd | Ex-Meta/HubSpot, 6x winner. Wants hardware or ML |
| vladpikaciu | 3x winner. One win became a research paper, another a funded app |
| Fle4ka | 1st at the KLM AI hackathon, builds agents at Keboola. Targeting Agentic AI and Data |
| nam__p | AI engineer at CERN, YC hackathon podium |
| Unc. Cookie / Shafir | Won DDH26 with a counter-drone build |
| luso + David (IST) | Won JunctionX Lisbon 2026 |
| wech / TibiGeo / Mateo | About 9, 10 and 15+ hackathons respectively |
| imcvampire | Has won Junction before |

## Supply and demand for roles
- **Hardest to find:** UI/UX and design engineers, asked for by 10+ teams.
- **Also wanted:** pitch and business leads, and MedTech domain experts.
- **Oversupplied:** AI-agent and full-stack engineers.
- **Hardware:** lots of interest but little skill; many teams are beginners.

## Gaps and openings: the numbers

### Method and limits
- The sample is **248 posts about Junction 2026**: 118 team-building posts and 130 intros. Each was keyword-matched for domain, track, partner and role.
- **This is a biased sample.** About 250 of roughly 2,000 attendees posted (~12%), and they skew toward people still looking for a team. Treat the figures as relative signals, not headcounts.
- Team-building posts were cut at 1,500 characters, so partner mentions are undercounted. A post can count toward several spaces.

### Crowding vs partner attention
**Crowding** is the share of the 248 posts that mention the space. **Partner footprint** counts what Junction has visibly put behind it: track ownership, workshops, keynotes, booths and grand-jury seats, all from the official guide and venue map.

| Space | Crowding | Track named explicitly | Partner footprint | Read |
|---|---|---|---|---|
| **AI infrastructure** | 14 (5.6%) | **0** | **Very high.** Verda owns the track and has a Fri workshop, Sun keynote, booth F3-6 and its **CTO on the jury**. Modal: workshop and booth F5-4. NVIDIA: opening keynote. Also Featherless, Aiven, IronShard | **Best ratio in the event.** Lots of attention, almost no competition |
| **Agentic AI** | 69 (27.8%) | 15 | **Highest.** DeepMind: keynote, workshop, booth, judge. Context.dev: booth, workshop, **CTO judge**. AfterQuery: booth, **RL lead judge**. Cala and Exa: workshops and booths. Also OpenAI, Atech | Rich, but you split it about 5 ways. Win with a vertical or a hard technical edge |
| **Hardware / physical AI** | 45 (18.1%) | 4 | **High.** Arduino: track, Fri workshop, **Sun keynote**, whole Hardware Lab. Intel x Ignite Next: workshop and booth F5-10. Also NVIDIA, Atech, Rokoko | Crowded on paper, but at least 14 posts say "beginner" or "first hackathon". Few experienced hardware + AI teams |
| **Healthcare** | 27 (10.9%) | 7 | Medium. AstraZeneca booth F3-4. Aalto booth F5-11 (AR4U voice AI for older adults) | **Expertise gap.** Only 1 post asks for a domain expert and only 3 offer one. Pharma comes up 3 times, elder care 5 |
| **Fintech** | 24 (9.7%) | 7 | Low to medium. S-Pankki booth F5-6. Cala (VC/startup data) is next door | **"Bank" is never mentioned.** S-Pankki's space is uncontested |
| **Data** | 19 (7.7%) | **1** | Medium, spread out. Oxylabs, Exa, Cala, Aiven, MariaDB, Tieto booth F5-12 | Almost nobody identifies with the Data track. Web-data tools come up 2 times |
| Cybersecurity | 17 (6.9%) | not a track | None | Popular with no home track. These teams will need a partner challenge to land in |
| Quantum / defence / XR | 8 / 6 / 3 | not tracks | Low (XR Creator Con, Rokoko) | Niche |

### Partner challenges with almost no takers
Expect each booth partner to set its own challenge. These have prizes and near-zero stated interest:

| Partner (booth) | Their domain | Posts touching it |
|---|---|---|
| **Valio Aimo** (F3-1) | Foodservice wholesale: 20k pro customers, 25k products, AI transformation | **4** (food or restaurant) |
| **S-Pankki** (F5-6) | Retail banking | **0** |
| **City of Espoo** (F5-7) | Public business services, possible real pilot afterward | 8 (civic or public sector) |
| **AstraZeneca** (F3-4) | Pharma | 3 |
| **Aalto University** (F5-11) | Voice AI for older adults | 5 |
| **Rokoko** | Motion capture / 3D | 3 |
| **Oxylabs** | Web data | 2 |

### Talent market
Counts come from "looking for..." phrases vs self-descriptions ("I'm a...", "experience in...").

| Role | Wanted | Offered | Read |
|---|---|---|---|
| Design / UI-UX | 9 | 8 | Tight. The earlier qualitative read found 10+ teams asking |
| Business / pitch | 7 | 10 | Roughly balanced, but the offers are mostly non-coders |
| Frontend | 8 | 5 | **Short.** More teams want it than offer it |
| Backend / full-stack | 16 | 32 | Oversupplied |
| ML / AI | 8 | 23 | **Oversupplied about 3:1** |
| Hardware | 6 | 9 | Thin on both sides |
| Domain expert (health, finance) | 1 | 3 | Nearly absent |

### Field strength
- **46 of 248 posts (19%)** cite a prior hackathon win. The serious end of the field is strong.
- **14 (6%)** say they're beginners or at their first hackathon, and they cluster in hardware.
- About 104 mention being students, and 43 mention founder or startup experience.

### What this means for strategy
1. **Easiest path to a partner prize: AI Infrastructure on Verda.** It has the most partner investment, almost no stated competitors, and a judge on the main jury. Something like an inference, eval or cost tool on Verda GPUs and Modal fits.
2. **Second: an uncontested booth partner challenge** (Valio Aimo, S-Pankki, City of Espoo). Expect far fewer submissions and a prize per partner. You can enter several challenges with one project, so pair one with a track.
3. **The main prize goes through peer review.** About 2,000 hackers choose the top 5, so a clear demo and polished UI matter more than a niche track. A strong frontend/design person is the rarest asset; protect that role on your team.
4. **Avoid generic agent projects.** That's 28% of the field and the most serious winners. If you go agentic, pick a vertical that uses a partner's data (Cala, Exa, Oxylabs) so you qualify for both a tech challenge and a track.
5. **Hardware is beatable** if you have real embedded skill. The beginner-heavy field and Arduino's Sunday keynote slot point to a hardware winner getting stage time.

Caveat: everything above was written before the challenge briefs came out. See the update below.

## Update after the challenges came out (Fri 13 Nov, ~19:50)

The full briefs are in `junction-2026-challenges.md`. Here's what changes from the predictions above:

- **AI Infrastructure is smaller than predicted.** The Verda track holds only one challenge, Stoa's "Make Blueprints Talk" (€1,000 + work trial / €750 / €250). Verda's own contribution is €200 compute credits for every participant. The track is still uncrowded, but the prize is small. It's a good second entry, not the main target.
- **The biggest partner prizes:**
  - Intel Physical AI: €5,000 / 3,000 / 2,000 (hardware, on-device OpenVINO)
  - Cala "Make Unicorns Real": about €5,000 in travel for a team of 4, plus credits
  - Valio Aimo "Trusted Trade Agents": €4,000 / 2,000 / 1,000
  - AfterQuery "Break the Agent": €3,000 + a work trial
  - Exa "Internet Butler": $2,500 + $5,000 in credits
- **Uncontested challenges still pay well.**
  - Valio Aimo (4 people posted about food) has the second-highest cash prize.
  - S-Pankki "Personal Economic Trainer" (0 people mentioned banking): €2,000 / 1,000 / 500.
  - Espoo "Rethinking Recruitment": €1,500 / 1,000 / 500.
- **Hardware is the richest track:** Intel €10,000 across 3 places, Rokoko gear worth about €8,400, Aalto €2,000 plus the real G1 humanoid, Arduino boards, and Meta glasses.
- **Gemini and NVIDIA Nemotron have no challenge on the platform.** Both were pitched on stage as side prizes, but there's nothing to submit to. Check the Tech Challenges tab and Discord before counting on them.
- **Meta glasses:** 10 Display glasses (1–2 free at 19:52, 22 teams waiting, 120-minute loans) and 10 Gen 2. Very few teams can even get hardware, which keeps competition low. Judging is 25% each for creativity, technical execution, real-world value, and UX/accessibility/trust.
