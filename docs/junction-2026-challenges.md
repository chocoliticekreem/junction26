# Junction 2026: Challenges, Tools and Hardware

Scraped from hackjunction.app/participate/45 on **Fri 13 Nov 2026, ~20:20 Helsinki time** (page countdowns read T-15:41 to Sat 12:00). Sources: the Main Challenges and Tech Challenges lists, all 19 main challenge pages, all 19 tech challenge pages, and the Dashboard, Developer Tools and Assets, Project Submission, Your Submissions, Peer Review, Partners and Guide tabs, plus the public event page. The hardware section comes from 2026.hackjunction.com/hardware (snapshot Fri 19:52).

Access codes, promo codes, event codes, passwords and API keys are written as "on platform". Personal emails and phone numbers of partner staff are written as "contact on platform". Look them up on the challenge page, the Developer Tools tab or Discord.

## Deadlines and schedule

| What | When (Helsinki, UTC+2) |
|---|---|
| Preliminary submission (draft, for team count) | **Fri 13 Nov, 23:55** on the platform (the Guide says 23:59) |
| Submissions open | Sat 14 Nov, 12:00 |
| **Final submission deadline** | **Sun 15 Nov, 10:00**. The form closes automatically; no late submissions. |
| Live peer review | Sun 15 Nov, 10:30 to 13:00 (Guide schedule). Guide rules text says 10:30 to 14:00. |
| Review time / Final ceremony | Sun 14:00 to 16:05: Arduino and Verda keynotes, Top 5 pitches 14:15 to 15:10, challenge winners 15:10 to 15:50, Junction winner 15:50 to 16:05 |
| Event ends / doors close | Sun 17:00 / 18:00 |

Bahn Express (Spread) has its own clock: ranking rounds have been open since Fri 19:30, and the final is **Sun 08:00** (registration closes 07:30).

## How entering and scoring work

- **Main challenges sit inside tracks.** There are 19 main challenges in 6 tracks: Agentic AI (7), Hardware by Arduino (5), Healthcare (2), AI Infrastructure by Verda (1), Data (3), FinTech (1). On the submission form, "Challenge Picker" selects the main challenge track. Every team must enter at least one challenge.
- **Tech (side) challenges are open to every team and stack on top.** There are 19, run by tool partners (Verda, OpenAI, Google DeepMind, NVIDIA, Arduino, Context.dev, Aiven, CRACI, Cloudinary, Modal, Oxylabs, Atech, and 6 by Major League Hacking). Choose them in the submission form's "Tech Challenge Participation" multi-select. Several also need an extra step: a form, a Discord post, a Project Hub listing or a note in the submission (see table B).
- **One project can enter several challenges.** The Guide says "You are allowed to submit a project for multiple challenges", and the Modal brief says "The same project can enter other tech challenges too."
- **Who picks winners.** Each challenge partner picks its own winners and runners-up using its own criteria. The overall Junction winner is chosen differently: live peer review on Sunday picks the Top 5, who pitch on stage (3 min pitch plus 3 min Q&A), and a panel of 7 judges votes. **Main prize: €10,000. Total prize pool: €100,000.**
- **Peer review criteria (overall prize):** Innovation, Impact and Implementation. You must take part in live peer review to be eligible for the main prize.

---

## A. Main challenges (19)

| Track | Challenge (id) | Partner | Prizes (exact) | Ask | Hard requirements |
|---|---|---|---|---|---|
| Agentic AI | Decode the Noise (357) | Hostinger | 1st 2000 €, 2nd 1000 €, 3rd 500 €; all three winning teams also get one year of Hostinger hosting and a domain, Hostinger swag, and a spotlight on Hostinger's social channels | AI tool that detects propaganda, bots and bad actors online | **Deployed and running live on Hostinger infrastructure with a public URL** by the end of the hackathon |
| Agentic AI | Earned Trust in AI Code (351) | Tieto | 1st €2,000 cash, 2nd €1,000 cash, 3rd €500 cash | AI code review concept and reference implementation in which a named human stays accountable | Synthetic or cleared sample data only; one sample agent-written change with its requirement ID; deliverables: concept card, live walkthrough, lessons log, demo video or presentation |
| Agentic AI | Make Unicorns Real (350) | Cala | 1st: 5,000€ to attend any hackathon on the planet (each member becomes a "Cala Comet", ~€5,000 for a team of four) + 1,000€ Cala credits + Cala merch; Runner-up: 500€ + Cala merch (the brief says "€500 in Cala credits") | Product for founders or investors built on Cala's structured company and funding data | **Cala API/MCP must be core** (25% of score) |
| Agentic AI | Spread (349) | Bahn Express | 1st 2000€, 2nd 1000€, 3rd 500€ | Agent that runs a simulated car-transport company for a week and maximises gross margin | Play on spread.bahnexpress.com; at least 90% of cars on time; reach the **top 10 in the Sun 08:00 final** (registration closes 07:30) to present |
| Agentic AI | Break the Agent (328) | AfterQuery | 1st 3,000€ + work trial at AfterQuery + merch; 2nd 1,500€ + merch; 3rd 500€ | RL environment where frontier agents fail in meaningful ways and the reward resists hacking | Show a reproducible gap against a stronger reference run; judges rerun it with Harbor + OpenCode over MCP; one-command eval from the README |
| Agentic AI | Trusted Trade Agents (327) | Valio Aimo | 1st 4 000€, 2nd 2 000€, 3rd 1 000€ | Interface and operating model that let external purchasing agents look up, order and get human approval from a food wholesaler | Must enable lookup of product, price and availability; request then order at fixed prices; permission and human-approval management. Build against the mock APIs (synthetic data). |
| Agentic AI | The Internet Butler / Your Personal Assistant (298) | Exa | 1st $2,500 cash + $5,000 Exa credits + Exa hoodie per person + Exa TRMNL dashboard; 2nd $1500 cash + $3,000 credits + hoodie per person + Exa macropad; 3rd $500 cash + $1k credits + hoodie per person; every participant gets $50 Exa credits | Personal agent that handles tedious real-life tasks using live web information | Must use Exa; demo on a real case; must work on the judges' own live queries |
| Hardware (Arduino) | The Green European Renaissance (356) | Arduino | 1st Ventuno Q unit per member; 2nd UNO Q 4G + Plug and Make Kits per member; 3rd Plug and Make Kit per member | Edge AI on the Arduino UNO Q for local green and environmental problems | **UNO Q + edge AI; also publish on Arduino Project Hub with tag "Junction Finland 2026"** to be prize-eligible; a physical prototype is judged |
| Hardware (Arduino) | AI Glasses for Everyone, Everyday (342) | Meta | Best overall: a pair of Ray-Ban Meta glasses per member | Everyday use case where a first-person view on Meta AI glasses enables new interactions | **Meta AI glasses** (Ray-Ban Display or RBM Gen 2; web app or Device Access Toolkit); functional prototype and a deck |
| Hardware (Arduino) | Stop Simulating, Start Moving: The Intel Physical AI Challenge (330) | Ignite Next x Intel | 1st €5,000, 2nd €3,000, 3rd €2,000 | SO-101 arm autonomously picks Duplo bricks, inspects them and sorts good from defective | **Use the provided station** (SO-101, Physical AI Studio VLA, Anomalib, OpenVINO on a Core Ultra Series 3 laptop CPU/GPU/NPU); accept the Challenge Terms |
| Hardware (Arduino) | The Robot Teleoperation Challenge (326) | Rokoko | 1st 1 pair Smartgloves II + 1 SDK licence + featured blog post + extended support (valued €4,990); 2nd 1 Smartsuit Pro II (valued €2,295); 3rd 1 pair Smartgloves I + merch (valued €1,095) | Teleoperate robot hands, arms or humanoids with Rokoko mocap | **Rokoko motion capture** (physical robot or simulation) |
| Hardware (Arduino) | Aaltonomous Humanoid (320) | Aalto University | Winner 2,000€ + visit to the Aalto robotics lab; top ~5 teams (by simulation score) run live on the real Unitree G1 | Give the Unitree G1 a brain: sort coloured objects into boxes autonomously within 2 min | **Submit a Docker image policy server**; to run on the real robot it must pass the sim safety check (no crashes or safety stops, within joint and speed limits, at least 27 commands/s) |
| Healthcare | Equal Care Across Finland (344) | AstraZeneca | Best overall 1000€, 2nd 750€, 3rd 250€ | AI system that finds gaps in Finnish cancer care pathways and recommends fixes | Sources for every claim; at least one indicator tied to Goal 3 of the national cancer strategy; actionable recommendations; working demo (slides alone are not enough); public aggregate data only |
| Healthcare | Beyond the Clinic (343) | Aalto University | To be announced | Product that helps people stay well at home after TMS depression treatment | Not stated (a laptop and a phone are enough) |
| AI Infrastructure (by Verda) | Make Blueprints Talk (335) | Stoa | Best overall 1000€ + work trial at Stoa, 2nd 750€, 3rd 250€ | Answer natural-language questions about construction drawings, verifiably | Use Stoa's dataset; show where in the drawing each answer came from; low inference cost is 25% of the score |
| Data | The Web Is Your Real-Time Database (332) | Context.dev | 1st €2,000 + swag, 2nd €500 + swag, 3rd swag | Product that reacts to the live web | Context.dev implied (judging centres on live web data and real-timeness) |
| Data | Rethinking Recruitment (319) | City of Espoo | Best overall 1500€ (+ pitch to Espoo and national city leaders); 2nd 1000€; 3rd 500€; runners-up get swag bags and features on city channels | Better matching between companies and talent at Espoo recruitment events | Synthetic data only; no automated decisions about individuals without a human; minimise personal data; EU AI Act-compliant privacy |
| Data | Wikipedia Through Time. (307) | MariaDB | 1st €1,000 cash + €1,000 UpCloud credits + MariaDB certification for every member (5 vouchers, value 750 USD); 2nd €500 cash; 3rd €250 cash; all winners credited in a blog on mariadb.org | Wikipedia tool using MariaDB vector search (RAG) and/or system-versioned tables | **MariaDB at the core**; provided Finnish Wikipedia datasets |
| FinTech | Personal Economic Trainer (311) | S-Pankki (S-Bank) | 1st 2000€, 2nd 1000€, 3rd 500€ (all Airbnb gift cards) | AI that lets people chat with their own banking data as a financial coach | Provided synthetic transaction dataset; mobile app or embeddable web app recommended |

Source discrepancies:
- **Hostinger:** the list page shows only 1st and 2nd. The detail page adds 3rd 500 €.
- **Cala:** the list page says the runner-up gets "500€ + Cala Merch"; the brief says "€500 in Cala credits and Cala merch". Cala is listed under the **Agentic AI** track (7 challenges), not FinTech. FinTech holds only S-Pankki.
- **Exa:** the brief still contains template placeholders ("[cash amount]"), but the structured prize list gives real amounts.
- **Stoa:** listed under "AI Infrastructure Track By Verda", but the brief does not mention Verda.

## B. Tech (side) challenges (19)

| Challenge (id) | Partner | Prizes (exact) | What qualifies | How to submit / claim |
|---|---|---|---|---|
| Verda Compute Track (56) | Verda | 1st $10,000 Verda cloud credits + Verda hoodies; 2nd $2,500 cloud credits; 3rd $2,500 cloud credits | Any challenge, built with Verda products where compute makes the idea possible | Tick it in the form, **document your process and post a link to a summary in Verda's Discord channel** |
| Best Use of MongoDB Atlas (55) | Major League Hacking | Best overall: M5Stack IoT Kit (per member, per brief) | Hack built on MongoDB Atlas | Tick it in the form; resources at mlh.link/mongodb |
| Best Use of Vultr (54) | Major League Hacking | Best overall: M5Stack mini programmable monitor | Project deployed on Vultr cloud or GPUs | Tick it in the form; mlh.link/vultr |
| Best Use of Tiger Data (53) | Major League Hacking | Best overall: Stream Deck Mini | Most innovative, impactful, performance-driven use of Tiger Data (Postgres for time series) | Tick it in the form; mlh.link/tigerdata |
| Best Use of Solana (52) | Major League Hacking | Best overall: Unruggable Hardware Wallets (per member, per brief) | Project built on Solana | Tick it in the form; mlh.link/solana |
| Best Use of Entire (51) | Major League Hacking | Best overall: Mini Portable Projector | Use as many of Entire's capabilities as possible (Sessions, Graph, Brain, Trails) and show token efficiency | Tick it in the form; claim the code at mlh.link/junction-26; mlh.link/entire |
| Best Use of ElevenLabs (50) | Major League Hacking | Best overall: Wireless Earbuds | Voice/audio built with ElevenLabs | Tick it in the form; claim the code at mlh.link/junction-26; mlh.link/elevenlabs |
| Best Use of Codex (49) | OpenAI | 1st $10 000 API credits; 2nd $5000 API credits; 3rd $2500 API credits | Meaningful use of Codex in building the project; open to any challenge | Tick it in the form; $100 credits per participant via redemption links on the hackerpacks page |
| Best Use of Gemini API (48) | Google DeepMind | 1st 4000€ + $1,000 Google Cloud credits per member; 2nd 2000€; 3rd 1000€ | Meaningful, innovative use of the Gemini API (not just "an LLM added"); **18+ only** | Tick it in the form; the submission should explain the problem, the integration, what is innovative and why Gemini matters |
| Best Use of Gemma (47) | Google DeepMind | Top 3: €1,000 per team, no ranking between winners | Most innovative and impactful use of Gemma open models | Tick it in the form |
| Best Use of Nemotron (46) | NVIDIA | Two best teams: 1x NVIDIA RTX 5080 each | Must use **Nemotron 3.5 Super VL** in core functionality, visible in the demo | Tick it in the form, **plus a text explanation in the submission form** (model used, what it does, why it matters, how you improved its outputs) |
| Best use of Arduino Uno Q (45) | Arduino | Each member of the winning team gets an Arduino UNO Q + Arduino Plug and Make Kit | UNO Q + Modulino + on-device AI in any challenge; working physical prototype | Tick it in the form **and publish on Arduino Project Hub with tag "Junction Finland 2026"** |
| Best Use of Context.dev: Fully Structured Web (44) | Context.dev | 1st €750 + swag; 2nd €250 + swag; 3rd swag | At least one Context.dev endpoint in the core flow, and its data visibly drives the demo | Tick it in the form; submit the GitHub repo + demo + **a short note on which endpoints you used and why** |
| Best Use of Aiven (43) | Aiven | Best use 1000€; 2nd 750€; 3rd 500€ | At least one Aiven service as a meaningful part of the project | Tick it in the form |
| Best use of CRACI (42) | CRACI | 1st LEGO set per member; 2nd 24-pack of Red Bull per member; 3rd invite to the CRACI x OpenAI lunch at Slush; Top 5: 50,000 CRACI build minutes per member + chance to interview for a job | **The project's CI must run on CRACI** (`runs-on: craci`), and creative use of SBOMs, AI fixes, provenance and the API | Tick it in the form |
| Best Use of Cloudinary (41) | Cloudinary | 1st: $500 Amazon gift cards per member | Use one of the four tools at cld.media/hackathons in a meaningful role (not just as a CDN) | Tick it in the form **and fill in https://cld.media/hackathon-survey** (required) |
| Best use of Modal (40) | Modal | 1st team: $2000 cash + $3000 Modal credits | Modal powers the project (inference, Sandboxes, training, batch) | Tick it in the form |
| Best agentic usecase of Oxylabs Web API (32) | Oxylabs | Winning team: €1,000 Apple gift voucher + $500 Oxylabs credits per member | At least one live /search or /scrape call at runtime (pre-downloaded data does not count); show source URLs | Same repo and demo as the main challenge + **a short note on which Web API endpoints you used and why** |
| Atech Real World Challenge (29) | Atech | Best overall: special Pro Atech kit for the team; runners-up: Atech kits + swag; top teams invited to show on Atech channels and visit Copenhagen | Atech modules used in a live demo solving a real problem | **Post a summary link in Atech's Discord**; live demo on hardware; public GitHub repo or exported Atech project; ~2-minute video |

Notes: MongoDB, Vultr, Tiger Data, Solana, Entire, ElevenLabs, Codex and Gemma publish no judging criteria. "Tick it in the form" means the Tech Challenge Participation field on the Project Submission tab.

---

## 1. Main challenges by track

### Agentic AI Track (7)

#### Decode the Noise (id 357)
- **Partner:** Hostinger
- **Prizes:** 1st 2000 €, 2nd 1000 €, 3rd 500 €. All three winning teams also get one year of Hostinger hosting and a domain, Hostinger swag, and a spotlight on Hostinger's social media channels.
- **Problem:** Propaganda, bot networks and bad actors manipulate the open web at scale.
- **Build:** A tool that analyses text, social content or web-traffic patterns to detect coordinated propaganda, bot-driven amplification or bad-actor behaviour. It can be an API, a dashboard, an explainable classifier or a monitoring service for site owners. Hostinger cares more about strong, honest detection logic (including how it handles false positives) than about a polished front end.
- **Directions (pick one or combine):**
  - Spot the swarm: detect coordinated inauthentic behaviour (bot networks, astroturfing, brigading) from posting timing, account similarity, text reuse and amplification patterns, not single posts.
  - Name the technique: classify manipulation techniques (loaded language, fear appeals, whataboutism, fabricated authority) and explain the verdict in plain language.
  - Clean the traffic: separate malicious bots, scrapers and credential stuffing from real visitors in web-server logs, with an actionable view for site owners.
  - Trust the source: score the provenance of a page or account (domain age, cloned content, AI-generated text, link networks).
  - Show precision and false-positive rate, not just a happy-path demo.
- **Judging:** Detection quality (accuracy, false-positive handling, explainability) 40%; Technical execution and live deployment on Hostinger 25%; Originality and real-world impact 20%; Demo clarity 15%.
- **Requirements:** Deployed and running live on Hostinger infrastructure by the end of the hackathon, with a public URL judges can open. Any language, framework or model (open-source or hosted) is fine, as long as the final product runs on Hostinger.
- **Resources:**
  - Full Hostinger environment, free for 1 month, per team.
  - Hostinger VPS (KVM 2) per team: 2 vCPU, 8 GB RAM, 100 GB NVMe, 8 TB bandwidth, root access, Docker, free domain, one-click templates for Ollama, n8n, Node.js and Python.
  - Hostinger AI Router credits per team: one API key and one shared credit balance for 150+ models (Anthropic, OpenAI, DeepSeek, Mistral, xAI and more); compatible with the OpenAI and Anthropic SDKs.
  - Hostinger AI Builder 1-month plan for front ends, dashboards or landing pages.
  - Hostinger Connector, API and CLI for deploying from Claude Code, Cursor, VS Code or any MCP client. Docs: https://docs.hostinger.com/hostinger-connector · API: https://developers.hostinger.com/ · MCP server: https://github.com/hostinger/api-mcp-server
  - Dedicated Hostinger help channel all weekend (link shared at kick-off and at the booth).
  - Talk "Vibe Coding Solved Building. Now Comes the Hard Part", Sat 13:00 (main stage). Promising teams get a path to keep talking with Hostinger engineering after the event.
- **Mentors:** Minijus Savickas (VPS Product) and Emilis Strimaitis (Innovations, AI agents), at the Hostinger booth all event.
- **Link:** https://hackjunction.app/participate/45/challenges/357 · https://www.hostinger.com/

#### Earned Trust in AI Code (id 351)
- **Partner:** Tieto
- **Prizes:** 1st €2,000, 2nd €1,000, 3rd €500 (cash).
- **Problem:** Agent tokens overtook human tokens in Feb 2026 and reached 7.3 trillion by Aug (OpenRouter data, a16z chart). Reviewing every agent change by hand does not scale, yet engineers need a sound basis to trust AI-reviewed code. The guiding question: "How can AI review the code made by AI so that humans can trust it?"
- **Build:** An AI code review concept, shown to work: the concept, its principles, a reference implementation and technology considerations across frontend, backend and security. Question whether line-by-line review is still the right model. Balance risk, hallucination, transparency, confidence and quality. The output is a reference implementation, not a product. Tieto weights the concept above the technical implementation.
- **Expected from each team:**
  - Define the concept the "PR review" factory should follow.
  - State key principles, including how it balances risk, hallucination, transparency, confidence and quality.
  - Illustrate it on one sample agent-written change with its requirement ID.
  - Show what the AI found, what it refused to decide, and why.
  - Show how the evidence lets a named human accept the change without a full read.
  - Name the failure modes you saw and keep a short decision log.
- **Code input:** https://github.com/te-industry-tech-office/junction26-messagepack-csharp (make your own copy first). The branches hold AI-made changes to MessagePack-CSharp: `ju26-issue-2283` (bug #2283, 4 files), `ju26-issue-2234` (bug #2234, 4 files), `ju26-issue-2129` (issue #2129, 28 files), `ju26-issue-2297` (issue #2297, 237 files).
- **Deliverables:** Concept card (recommendation, principles, trade-offs, limits); live walkthrough showing where the trust comes from; lessons log; demo video or presentation.
- **Out of scope:** a finished product, model training, vendor selection.
- **Tieto's trust principles:** a named engineer owns and signs off each change. The AI review is advice backed by evidence, never the approval itself. Evidence traces to a requirement. Review depth follows risk. Humans spot-check the AI reviewer and track what it misses. Trust is earned per area from track record and withdrawn after escapes. The owner signs off on what was checked and by whom or what, what was not checked and why, and the residual risk they accept. Not accepted: "The AI said it was fine" (an unowned merge), or confidence without evidence or a risk score nobody can explain. Vendor guidance: route human attention by risk; review with full repo context and verify findings before posting; measure outcomes (reverts, incidents), not review activity.
- **Optional directions:** a generalist reviewer covering frontend, backend, security and performance; or a classifier that separates code needing human review from code that meets the standard.
- **Judges will ask:** What would make you not trust your own output? Who owns the decision? How would this scale?
- **Judging:** Clarity 30% (clear recommendation, principles, explicit trade-offs and limits); Practicality 25% (works in a real PR flow and scales, a named human owns each decision); Measurement 25% (reverts and incidents don't rise as review time falls, AI findings are real and accepted, time to merge, share routed to humans); Evidence 20% (evidence traceable to a requirement lets a named human accept a change without a full read, including what the AI found, what it refused to decide, and why).
- **Requirements:** Synthetic or cleared sample data only.
- **Resources:** Tieto background on good code (standards, security, quality); a requirements set (intent, functional, non-functional); sample agent-written changes, each with a requirement ID; model access through other partners' credits on the Junction Platform.
- **Mentors / contact:** Not stated.
- **Link:** https://hackjunction.app/participate/45/challenges/351 · https://www.tieto.com/

#### Make Unicorns Real (id 350)
- **Partner:** Cala
- **Prizes:** 1st: each member becomes a "Cala Comet" (~€5,000 for a team of four): for three months, one hackathon of their choice per month, with travel and accommodation covered by Cala. The team also gets €1,000 in Cala credits and merch. Runner-up: 500€ + merch on the list page, or "€500 in Cala credits and Cala merch" in the brief.
- **Problem:** Founders and investors make decisions from scattered, stale information. Agents that search the web hit messy, disconnected data.
- **Build:** A product on Cala's structured, sourced data (companies, people, funding rounds, investors and the links between them) that solves one real need for founders, investors or both. Focus beats breadth. Aim for something founders and investors could use at Slush, which starts right after the hackathon.
- **Starting points:** finding lead investors still active in your space; reading a market (competitors, who raised from whom, funding flows); spotting promising young companies or running quick, sourced background checks; finding first customers among newly funded companies; market sizing; mapping likely acquirers.
- **Judging (25% each):** Real need (a clear user with a problem worth solving); Execution (works smoothly end to end); Originality (a fresh angle); Use of Cala (core, not an add-on).
- **Requirements:** The Cala API or MCP must be core.
- **Resources:** Each team gets all the credits it needs. Docs: docs.cala.ai. Redeem the promo code (on platform) at console.cala.ai → Billing → Extra credits → Add credits → Add promo code (no payment details needed). Workshop "Tips & tricks to Make Unicorns Real", Sat 11:00 to 11:30, Loft, 4th floor (Guide), hosted by Elies Delgado: how to query companies, people, investors and funding rounds, and what the judges look for.
- **Mentors:** Issey Masuda (co-founder and CTO) plus Cala engineers (knowledge graphs, data pipelines, LLM agents, MCP), on site throughout.
- **Main contact:** Elies Delgado (Community Growth), contact on platform.
- **Link:** https://hackjunction.app/participate/45/challenges/350 · https://www.cala.ai/

#### Spread (id 349)
- **Partner:** Bahn Express
- **Prizes:** 1st 2000€, 2nd 1000€, 3rd 500€.
- **Problem / world:** Bahn moves cars for dealers, and a freelance driver drives each car. Spread simulates one week in Finland with dealers, cars, deadlines and drivers.
- **Build:** The system that runs the company for the week. A dealer asks you and a competitor for a price; quote too high and you lose the car. If you win it, you post the drive as a gig in the drivers' app and set the fee. Pay too little and no driver takes it in time, so the car arrives late.
- **Scoring:** Gross margin (what dealers pay minus what you pay drivers). At least 90% of cars must arrive by their deadline.
- **Timeline:** Ranking rounds open from Fri 19:30. Every team plays the same secret weeks, and Bahn's own best system plays every round. Final on Sun 08:00: each team plays its own copy of one secret week, which runs by itself for ~34 minutes. Registration closes 07:30.
- **Judging:** The 10 ranked teams with the highest margin present to the jury (5 to 10 slides or a short video). The jury judges how elegant, clear, creative and robust the system is. Reaching the top 10 is enough; after that, margin no longer counts. No weighted criteria are listed.
- **Requirements:** Create your team at https://spread.bahnexpress.com/join with the event code (on platform). The handbook, rules, API reference, TypeScript and Python kits, and the leaderboard are on the site. Agent-readable docs: https://spread.bahnexpress.com/llms.txt
- **Contact:** Bahn booth (rules, the world, real dispatch, hints). No named mentors.
- **Link:** https://hackjunction.app/participate/45/challenges/349 · https://www.bahnexpress.com/

#### Break the Agent (id 328)
- **Partner:** AfterQuery
- **Prizes:** 1st 3,000€ + work trial at AfterQuery (straight to the final interview stage with the environments team) + merch; 2nd 1,500€ + merch; 3rd 500€. Finalists get AfterQuery gear.
- **Problem:** Frontier agents still struggle in novel situations. Designing a good environment (problem, action and observation space, reward) is a research problem in itself.
- **Build:** An environment an agent can interact with: a game, a scientific simulation, a software task, a real-world process or anything else. It needs a clear goal, actions and a checkable reward. Run a frontier agent and compare it with a stronger reference run your team can demonstrate and reproduce. Show where the agent falls short and why. The difficulty must come from decisions, with the information and tools needed to succeed available to the agent. Judges will hunt for reward hacking.
- **Starting points:** planning several steps ahead; exploring an unfamiliar system; using tools; managing limited resources; adapting when new information arrives. A small environment with a well-chosen challenge can be enough.
- **Stretch:** Train a smaller model on experience from your environment and show whether it improves.
- **Judging rubric:**
  - The gap (30%): full points if the frontier agent consistently scores below your demonstrated stronger reference run and both reproduce across repeated runs. Zero if there is no measurable gap, or it cannot be reproduced or checked.
  - Meaningful difficulty (30%): full points if you can explain the agent's main mistakes and tie them to task decisions, with the needed information and tools available. Zero if the gap comes from withheld information, trick wording, impossible timing or broken tools.
  - Reward integrity (25%): full points if the reward measures task success and holds up to judges' exploits: doing nothing or stopping early earns little or nothing, and completing the task well is the best way to score. Zero if an exploit, loophole or task-avoiding strategy beats successful play.
  - Craft (15%): full points if the rules and behaviour make sense and judges can run the eval from your README with one command and reproduce your results. Zero if it only works in your demo.
- **How judging runs:** 10-minute demo. Judges then rerun with the standard harness: your reference run, three agent runs, a do-nothing baseline and a stop-early baseline, plus 15 minutes of exploit hunting. Tiebreaker: a smaller model that improves after training on your environment.
- **Resources:** Open-source harness Harbor running the OpenCode agent, connecting to your environment over MCP; a scoring skeleton; frontier model API credits per team; a starter kit (harness docs and the rubric); on-site mentors for environment design and reward testing.
- **Mentors:** Daksh Raghuwanshi and Ved Vedere (AfterQuery environments team), on site all weekend.
- **Link:** https://hackjunction.app/participate/45/challenges/328 · https://www.afterquery.com/

#### Trusted Trade Agents (id 327)
- **Partner:** Valio Aimo
- **Prizes:** 1st 4 000€, 2nd 2 000€, 3rd 1 000€.
- **Problem:** Valio Aimo (20,000+ professional kitchens, 25,000 products from 700 suppliers) plans a B2B marketplace. As ordering moves to autonomous purchasing agents, the wholesaler must decide what agents can see, decide and be trusted with. For Junction it mocks today's webshop and backend, not the marketplace.
- **Build:** The interface and operating model that let an external purchasing agent find, compare, order and handle exceptions with Valio Aimo, built on open, verifiable standards rather than a single platform's black box. Not a chatbot over the existing UI.
- **Core (must enable):**
  - Product, price and availability lookup in structured form.
  - Request price and availability, then place an order (fixed prices, not negotiated quotes).
  - Permission and human-approval management: what the agent decides alone and what goes to a human.
- **Optional (not required to win):** comparing delivery time and sustainability (certificates and labels, with category-level carbon ranges as a stretch); substitution and exception handling (not scored as core); traceability and explainability.
- **Example request:** "I need 1,000 litres of lactose-free milk by Monday. Find an option that meets our requirements based on price and availability." A hotel chain's agent sends it. The solution returns structured products, prices and availability, and the agent orders within its authority or escalates for approval.
- **Problems they would like tackled:** a trust protocol (the minimum verification needed to trust claims about stock, price and origin); a guardrails model (spend thresholds, substitutions outside stated preferences); response logic (partial availability, good-better-best substitution within Valio Aimo's assortment); an audit trail readable by both the buyer and Valio Aimo.
- **Example scenarios:** need → recipe → order; a last-minute event with recipe-logic substitutions; a supplier stock-out covered by a recipe-compatible substitute; a proactive selling agent; allergen-safe substitution in school or hospital kitchens; detecting drift in standing orders.
- **Scope note:** Valio Aimo is mocking a structured data/API interface. Whether production ends up as a traditional API, an MCP-style interface or a service agent is out of scope.
- **Judging:** Working end-to-end demo 30% (the full request → lookup → order/approval flow in the mock environment); Solving the problem and user need 20%; Autonomy and controls 20% (guardrails, human sign-off, logging and auditability); Robustness to exception situations 15%; Openness and credible path toward production 15%.
- **Requirements:** Build against the synthetic catalogue, simulated suppliers and mock APIs. No live or confidential data. Preferred tech: agentic/tool-use frameworks, open data and interop standards, recommendation logic, and optionally verifiable credentials or trust layers. Agentic payment standards (x402, Nevermined) are relevant context but not required.
- **Resources:** Resource portal https://junction26.valioaimo.fi/ (password on platform) with datasets, API docs and access to the mock backend. Mock API key: on platform. Webshop test accounts will be shared separately.
- **Mentors:** Marketplace/Commercial: Hanna Forsström, Pirjo Kaartinen. Online Sales: Minni Ruhtinas. IT/Tech integrations and data governance: Tommi Nurmi-Aro, Ville Takanen, Riku Tapper.
- **Link:** https://hackjunction.app/participate/45/challenges/327 · https://www.valioaimo.fi/

#### The Internet Butler / Your Personal Assistant (id 298)
- **Partner:** Exa
- **Prizes:** 1st $2,500 cash, $5,000 Exa credits, Exa hoodie per person, Exa-branded TRMNL dashboard. 2nd $1500 cash, $3,000 Exa credits, hoodie per person, Exa-branded macropad. 3rd $500 cash, $1k Exa credits, hoodie per person. Participation trophy: every Junction participant gets $50 free Exa credits.
- **Problem:** Everyday tasks (is a rent increase legal, which benefits does a family qualify for, which vegan restaurant to pick) take hours of digging across the web.
- **Build:** A personal agent that finds what matters across the web, works out what needs to happen and gets the task as close to done as it can, leaving final approval to the user where needed. Demo it on a real case. Areas: planning special occasions, daily errands, rent, missed benefits, business information, travel disruption.
- **Judging (20% each):** Use of Exa (information that could not come from training data alone); Usefulness (to a specific group of real people); Clarity (in showing sources); Originality; Working implementation (works on live queries, including the judges' own).
- **Requirements:** Exa.
- **Resources:** $50 Exa credits per participant (promo code on platform; redeem at https://dashboard.exa.ai/billing). Full API: Search (fast, balanced and deep research modes), Contents (full text, highlights, summaries, subpage crawling), filters by date, domain and category (news, papers, companies, people, personal sites), structured JSON output, past page versions, Websets, Monitors, hosted MCP server, Python and JS SDKs. Demo gallery: https://demos.exa.ai/. Exa workshop Sat 16:30 to 17:00, Loft, 4th floor.
- **Mentors:** Exa engineers on site all event, plus a Discord channel. No names given.
- **Link:** https://hackjunction.app/participate/45/challenges/298 · https://exa.ai/

### Hardware Track by Arduino (5)

#### The Green European Renaissance (id 356)
- **Partner:** Arduino
- **Prizes:** 1st: a Ventuno Q unit per team member. 2nd: UNO Q 4G + Plug and Make Kits per member. 3rd: Plug and Make Kit per member.
- **Problem:** The US and Asia lead the AI revolution. Arduino's pitch is that Europe can use edge AI devices like the UNO Q to build local solutions to local problems, independent of governments or big companies, for a greener Europe.
- **Build:** Edge AI and Physical AI on the Arduino UNO Q for local problems, improving people's lives and the environment. Example directions: boosting local flora and fauna, saving energy, supporting elderly people's independence, reducing industrial impact, tackling climate change, energy efficiency, cutting pollution, more liveable cities.
- **Judging:** Technical Implementation and Edge AI 30% (use of the UNO Q, sensors, on-device AI); Environmental and Social Impact 30%; Creativity and Innovation 20%; Working Prototype and Demo 20% (a functioning physical prototype).
- **Requirements:** Arduino UNO Q and edge AI.
- **Extra submission step (prize eligibility):** publish on Arduino Project Hub as well as submitting on the Junction platform. Log in at https://projecthub.arduino.cc/ → + NEW PROJECT → select tag **"Junction Finland 2026"** → fill in the required parts.
- **Resources:** Hardware kit with an Arduino UNO Q and Modulino sensors from the Arduino Hardware Lab, 5th floor. Install Arduino App Lab: https://www.arduino.cc/en/software/#app-lab-section. Arduino workshop Fri 20:30 to 21:00 in the Hardware Lab.
- **Mentors:** Not named. Arduino mentors are at the Hardware Lab and on Discord.
- **Link:** https://hackjunction.app/participate/45/challenges/356 · https://www.arduino.cc/

#### AI Glasses for Everyone, Everyday (id 342)
- **Partner:** Meta
- **Prizes:** Best overall: each member of the winning team gets a pair of Ray-Ban Meta glasses. The best teams may be invited to a Meta AI forum on Wed 18 Nov 2026 about the future of wearable AI.
- **Problem:** Find where a first-person view creates value beyond mirroring a phone screen.
- **Build:** The best everyday use case on Meta AI glasses, showing how a first-person field of view enables new or better interactions. State the problem and audience clearly, and deliver a functional prototype and a deck. Display and audio-first experiences count equally, as do web apps and Device Access Toolkit (DAT) mobile integrations. The prototype should handle permissions, errors, performance trade-offs, connectivity and device state changes, and show a plausible path to adoption or a pilot. Interactions must be intuitive and inclusive for all abilities, with appropriate consent and safe data practices.
- **Judging (25% each):** Creativity and use case; Technical execution; Real-world value and feasibility; User experience: input, accessibility and trust.
- **Requirements:** Meta AI glasses (shared devices with contested, time-limited loans; see section 4).
- **Resources:** 10 × Meta Ray-Ban Display and 10 × RBM Gen 2 for use during the hackathon; charging and hygiene materials; developer support at the Meta booth.
- **Mentors:** Amanda Le (challenge mentor and point of contact; Product Marketing, DAT Android). Ming Lin, William La, Amy Lee and Odil Nikadambaev (Software Engineers, Web Apps). Dennis Punjabi (Software Engineer, DAT iOS).
- **Link:** https://hackjunction.app/participate/45/challenges/342

#### Stop Simulating, Start Moving: See It. Detect It. Act on It. The Intel Physical AI Challenge (id 330)
- **Partner:** Ignite Next x Intel
- **Prizes:** 1st €5,000, 2nd €3,000, 3rd €2,000.
- **Problem:** Factories still inspect parts by eye because programming a robot for the job takes specialist effort. Physical AI lets a robot learn a policy from a few dozen demonstrations.
- **Build:** Teleoperate an SO-101 arm to record demonstrations, then fine-tune a vision-language-action (VLA) policy in Physical AI Studio on cloud GPUs. In parallel, train an Anomalib model to tell good Duplo bricks from defective ones (you mark the defects yourself). Then combine them: the arm picks each brick, shows it to the inspection camera and drops it into the "good" or "defective" bowl fully autonomously, with the models optimised with OpenVINO and running on the laptop's CPU, GPU and NPU. Early finishers can push for faster cycles, messier piles, new defect types or their own twist.
- **Insight:** How close can a small, low-cost setup get to a reliable inspection cell? How few demonstrations are enough, how does the policy cope with bricks in new positions, and how fast does the loop run on CPU/GPU/NPU? Suggested ideas: use the anomaly score to trigger a re-grasp; share cameras between the policy and inspection; quantise with OpenVINO.
- **Judging:** Task success 30% (accuracy, cycle time, robustness to shifted or cluttered bricks); Intel technology integration 30% (deployment with OpenVINO Physical AI and the Robotics AI Suite, offloading to NPU and iGPU); Dataset and pipeline quality 20% (clean teleop data, fine-tuning in Physical AI Studio); System efficiency 20% (inference latency, thermal headroom, power on Core Ultra).
- **Requirements:** The provided station and Intel stack. Read and accept the Challenge Terms: https://drive.google.com/file/d/1nKs-e-4FNk-AoMq1fCeRKM_6mpIkArRt/view?usp=sharing
- **Resources:** 25 stations in the Junction Hardware Lab, one per team. Each has an Intel Core Ultra Series 3 (Panther Lake) laptop with 64 GB RAM; an SO-101 follower arm with wrist camera and a leader arm; two external cameras (top view and inspection), at least one a RealSense D415 depth camera; Duplo bricks, bowls and markers. Also provided: cloud GPU instances, Physical AI Studio, Anomalib, OpenVINO and OpenVINO Physical AI. Hands-on technical session Sat 12:00 to 12:30, Hardware Lab, 5th floor.
- **Mentors:** 3 to 5 Intel robotics and edge AI engineers (Physical AI Studio, OpenVINO, Anomalib), on site every day, supported by Ignite Next.
- **Main contact:** Marvin Müller, Strategic Partnerships & Value Creation Lead, Ignite Next (contact on platform).
- **Link:** https://hackjunction.app/participate/45/challenges/330

#### The Robot Teleoperation Challenge (id 326)
- **Partner:** Rokoko
- **Prizes:** 1st: 1 pair of Smartgloves II + 1 SDK licence + a featured post on Rokoko's blog + extended support (valued at €4,990). 2nd: 1 Smartsuit Pro II (valued at €2,295). 3rd: 1 pair of Smartgloves I (1st gen) + Rokoko merch (valued at €1,095).
- **Problem:** Teaching robots to interact with the physical world is hard. Human teleoperation can control robots and collect training data.
- **Build:** An impressive teleoperation application that uses Rokoko mocap to control robotic hands, arms or humanoids, physically or in simulation. The brief is open-ended, and you can combine it with other hardware and challenges at the event.
- **Interests:** precise manipulation (fragile objects, tools, liquids); collecting human demonstrations to train autonomous policies; creative or entertainment uses.
- **Judging:** Technical execution 35%; Originality and creativity 25%; Usefulness and potential impact 25%; Demonstration of human-controlled robotics 15%.
- **Requirements:** Rokoko motion capture.
- **Resources:** Smartgloves II, Smartsuit Pro II, Coil Pro, Rokoko Device SDK; access to a Unitree G1 with dexterous hands (coordinated with the humanoid challenge team); possibly a Booster T1; an Inspire robotic hand integration by Aalto Robotics Club. Access: create a Rokoko ID → submit your email and ID via the form (https://docs.google.com/forms/d/e/1FAIpQLSdCZTfoFzWbZS8fuvpKjhhP8xvOAX_vhJhTKYMpuRB8JMIHIQ/viewform) → get accepted by Rokoko reps → activate the SDK licence following the SDK page.
- **Mentors:** Victoria Stein (Rokoko, on site); Aalto Robotics Club mentors trained on Rokoko tech.
- **Link:** https://hackjunction.app/participate/45/challenges/326 · https://www.rokoko.com/

#### Aaltonomous Humanoid (id 320)
- **Partner:** Aalto University
- **Prizes:** Winning team 2,000€ + a visit to the Aalto robotics lab. The top ~5 teams (by simulation performance) run their solution live on the real Unitree G1.
- **Problem:** Moravec's paradox: the G1 "Väiski" can do a backflip but cannot sort blocks.
- **Task:** Make the G1 sort objects into boxes autonomously.
  - Setup: legs and waist held stiff; two 7-DoF arms and two Dex3 three-fingered hands. 3 to 5 printed objects (cubes, cylinders, triangular prisms, ~4.5 cm, red/yellow/blue) lie at random positions and angles. Three identical unmarked orange boxes (21 cm wide) sit fixed at left, centre and right, 5 cm apart and 40 cm from the torso. Every object must go into the right box within 2 minutes.
  - Fixed sorting: red → left, yellow → centre, blue → right.
  - Sort by instruction: a text instruction sets the mapping, with phrasings you have not seen.
  - Stretch: put each object through the matching hole in a lid on one box.
  - Policy inputs: head camera (colour + depth), both wrist cameras, joint states, the instruction. Output: target positions for all arm and finger joints at 30 Hz.
- **How it works:** Simulation first, in a ready-made Isaac Sim scene, with GPU from Verda. Real-robot datasets are published on Hugging Face during the event (links in the Junction Discord). Submit a Docker image running a small policy server; the runner sends its commands through a safety filter. Finals: submissions are evaluated in simulation on an unseen scene variant; finalists run on the real robot on Sunday, and the best real-robot score wins.
- **Directions:** CV plus classic programming; a VLM/LLM planner calling your own skills; imitation learning or VLA fine-tuning (LeRobot, π0, GR00T); RL in Isaac Lab; sim-to-real matching; combinations. They want robustness to sim/real mismatch, generality beyond one setup, and a lot done with little real data.
- **Judging:** Real-world result 40% (how well it works on the real robot); Generality 25%; Originality 20%; Presentation 15%.
- **Requirements:** Docker image policy server. To run on the real robot it must pass the sim safety check: no crashes or safety stops, no commands over joint and speed limits, at least 27 commands per second. Teams never control the robot directly; Aalto's runner applies joint, speed and workspace limits plus a watchdog, and staff stand at the e-stop. GPU: RTX-class with at least 24 GB (RTX Pro 6000, L40S, A6000, RTX 4090/5090). The ray-traced cameras will not render on A100 or H100 (fine for training). Use on-demand instances, not spot, with a persistent volume.
- **Resources:** Starter repo https://github.com/zupermiez/aaltonomous-humanoid (guide: `aaltonomous/cloud/QUICKSTART.md`; rules and submission: `aaltonomous/docs/participants/`). Sim Docker image `aalto-sim-v1.tar.zst` (download location shared at kickoff). Commands: `aalto sim` (first start takes 5 to 10 min), `aalto check` (expect 8 PASS / 0 FAIL), `aalto baseline`, `aalto eval --policy ws://localhost:8000`. Without Docker: `bash aaltonomous/cloud/setup_instance.sh` (~30 to 40 min, no sudo). Policy template in `aaltonomous/deploy/`; package it with `aaltonomous/docker/submission.Dockerfile`. Starter code includes the robot interface, safety filter, classical baseline, policy-server and Dockerfile templates, and a sim evaluator. Verda compute. Around 30 Aalto Robotics Club volunteers.
- **Mentors:** Erkka Lehtonen and Viktor Solianoi, on site all event. Questions via the Junction Discord.
- **Link:** https://hackjunction.app/participate/45/challenges/320 · https://aalto.fi/

### Healthcare Track (2)

#### Equal Care Across Finland (id 344)
- **Partner:** AstraZeneca
- **Prizes:** Best overall 1000€, 2nd 750€, 3rd 250€.
- **Problem:** Make sure time to diagnosis is optimal and cancer patients start treatment within target timeframes wherever they live in Finland. Known bottlenecks: late detection; the referral from primary to specialist care; time from diagnosis to treatment. Data is limited, and closing the data gap is part of the challenge.
- **Build:** An AI-powered system that (1) identifies the gap in access or outcomes, (2) locates where in the pathway it emerges (detection, referral, diagnosis, treatment initiation), and (3) recommends concrete, evidence-based improvements at national or account level. Recommendations matter most. Possible formats: an AI analyst explaining indicator trends, a monitoring dashboard, an early-warning system, an intervention simulation. A non-technical decision-maker should get the point in under two minutes.
- **Minimum requirements:** reliable evidence from public data and/or AstraZeneca mentor insights, with sources for every claim; at least one indicator tied to Goal 3 of the national cancer strategy; actionable recommendations; a working demo (slides alone are not enough).
- **Judging:** Actionability 30%; Insight 25%; Data quality and transparency 20%; Execution 15% (works live in front of judges); Clarity 10% (key message within two minutes).
- **Requirements:** Public, aggregate data only; no patient-level data.
- **Resources:** Key insights at the AstraZeneca stand, Fri 20:00 (3rd floor, booth 4, per the dashboard announcement). Background pack / national cancer strategy 2026–2035 (Finnish): https://files.hackjunction.app/resources/Kansallinen_syopastrategia_2026_2035_FINAL.pdf · Implementation roadmap 2026–2031 (Finnish): https://files.hackjunction.app/resources/Kansallinen_syopastrategia_toimeenpanon_tiekartta_2026_2031.pdf · Source list: https://files.hackjunction.app/resources/Sy%C3%B6p%C3%A4strategiat%20ja%20sy%C3%B6p%C3%A4data_linkkikokoelma.pdf · Finnish Cancer Registry and THL regional health indicators. Mentors are also available as interview partners.
- **Beyond Junction:** A possible follow-up project with a Finnish wellbeing services county.
- **Mentors:** Fri 13 Nov from 18:00: Hanna Rusila (Marketing), Hanna Toivola (Diagnostics), Kaisa Kaitila (Medical Affairs), Laura Aaltonen (Marketing), Joanna Tuormaa (Business Excellence). Sat 14 Nov daytime: Kaisa Kaitila. Sun 15 Nov 14:00 judging: Hanna Rusila, Laura Aaltonen, Joanna Tuormaa.
- **Contacts:** Main: Joanna Tuormaa, Innovation and Business Excellence Director, Nordics. Questions: Laura Aaltonen (contact on platform).
- **Link:** https://hackjunction.app/participate/45/challenges/344

#### Beyond the Clinic (id 343)
- **Partner:** Aalto University
- **Prizes:** To be announced.
- **Problem:** TMS treats severe depression in clinics through daily visits, but depression can return, and no good maintenance treatment exists for home. Home lacks fMRI/MEG/EEG, blood tests and psychiatrists.
- **Build:** A product that helps people stay well at home after depression treatment, ideally closed-loop: sense how someone is doing, respond with something that helps, and learn what works for that person. A laptop and a phone are enough.
- **Audiences:** people after TMS; anyone at risk of depression; clinicians following patients between visits.
- **Interventions:** sensory stimulation (music, rhythmic lights, colours, touch, smell, taste); social interaction, meditation, yoga, exercise; visits to forests or the sea, or VR when going out is hard; games (e.g. Soihtu, https://soihtudtx.com/).
- **Sensing:** phone (sound, voice, acceleration, facial expressions, sleep, routines); wearables like smart rings (HRV, sleep, activity, autonomic changes).
- **Product directions:** everyday companion; adaptive sensory experience; daily game; smart-home light and sound; social peer support; clinician view. Inspiration: Meru Health (https://meruhealth.com/).
- **Judging (25% each):** Usefulness; Ease of use (would someone recovering use it daily?); Smart sensing (clever use of home measurement, learns per person); Creativity.
- **Requirements:** Not stated.
- **Resources:** Pointers to published studies and open datasets; expert mentors. Subject to lab confirmation: a live TMS demo and a portable EEG demo at the booth.
- **Mentors:** Researchers from Prof. Risto Ilmoniemi's and Prof. Pantelis Lioumis' group (Neuroscience and Biomedical Engineering), plus Aalto Innovation. Main contact: Myungji (MJ) Suh.
- **Link:** https://hackjunction.app/participate/45/challenges/343 · https://aalto.fi/

### AI Infrastructure Track by Verda (1)

#### Make Blueprints Talk (id 335)
- **Partner:** Stoa
- **Prizes:** Best overall 1000€ + work trial at Stoa, 2nd 750€, 3rd 250€.
- **Problem:** Site engineers spend hours a day searching drawings, and general AI models fail on complex technical drawings.
- **Build:** A program that answers natural-language questions about construction drawings and building information models correctly, and shows where in the drawing each answer came from so a human can verify it in seconds. Stoa prefers approaches that next year's frontier models won't make obsolete, such as hybrids of frontier models, computer vision, 3D, geometry or small fine-tuned models.
- **Judging (25% each):** Accuracy of answers; How well it visualises its reasoning for human verification; Creativity; Low inference cost.
- **Requirements:** Use the provided dataset (real drawings in many formats and languages, with example questions).
- **Resources:** Preview (0.5 GB): https://fwjydgxpttajiqpfmqtj.supabase.co/storage/v1/object/public/stoa-junction-2026/junction-dataset-preview.zip · Full (10 GB): https://fwjydgxpttajiqpfmqtj.supabase.co/storage/v1/object/public/stoa-junction-2026/junction-dataset.zip
- **Mentors:** Stoa's founding tech team plus a construction engineer. No names given.
- **Link:** https://hackjunction.app/participate/45/challenges/335 · https://stoabuild.com/

### Data Track (3)

#### The Web Is Your Real-Time Database (id 332)
- **Partner:** Context.dev
- **Prizes:** 1st €2,000 + swag, 2nd €500 + swag, 3rd swag.
- **Problem:** Software runs on stale data. Analysts copy-paste prices and check sites by hand, and fact-checkers can't keep up.
- **Build:** A product that turns live web data into decisions, actions or experiences that weren't possible before. Inspiration: GPU Rental Prices (https://gpurentalprices.com/), Yapper Leaderboard, cve.now, Ferndesk. Themes: Scrape the Economy; The Web, Watched (agents triggered by changes); Brand in a Box (apps that brand themselves from a sign-up email); Truth at Internet Speed (fact-checking with sources). Wild ideas are welcome.
- **Judging (20% each):** Real-world impact; Creative use of live web data; Completeness of demo (production readiness); Technical execution (latency and accuracy); Real-timeness (reacts to change rather than taking a one-off snapshot).
- **Requirements:** Context.dev is not stated as mandatory, but judging centres on it. This pairs naturally with tech challenge 44.
- **Resources:** 50,000 free, non-expiring API credits per team: sign up at https://context.dev/signup and redeem the code (on platform) at https://context.dev/dashboard/redeem-credits. Quickstart https://docs.context.dev/quickstart, docs https://docs.context.dev/. Up to 50 concurrent requests per team. Capabilities: search, scrape (markdown, HTML, screenshots, images), crawl, URL mapping, structured extraction, research answers; brand data, company and people search and enrichment, NAICS/SIC; news search, monitors with webhooks; batch API, PDF and document parsing. Context.dev workshop Sat 17:30 to 18:00, Loft, 4th floor (Guide).
- **Mentors:** Beer van der Drift (CTO, main contact, contact on platform), Yahia Bakour (Founder and CEO), Thomas Oomens (Engineer). On site Fri until 23:00, Sat 09:00 to Sun 02:00, Sun 07:00 to the end.
- **Link:** https://hackjunction.app/participate/45/challenges/332

#### Rethinking Recruitment (id 319)
- **Partner:** City of Espoo
- **Prizes:** Best overall 1500€ + a chance to present to Espoo's business development and innovation leaders and the national network of cities working on talent attraction. 2nd 1000€, 3rd 500€. Runners-up get Espoo swag bags, features on city channels, and a presentation to the cities of Helsinki and Vantaa.
- **Problem:** At Espoo's online, in-person and hybrid matchmaking events: companies describe their needs late and poorly; talent struggles to express its strengths; CVs and screening are increasingly AI-generated; organisers can't assess real capabilities (especially tech skills); companies get swamped by irrelevant approaches; platforms are cumbersome and crash at event start; and international recruitment adds compliance, language, culture, relocation and onboarding complexity. Companies also doubt that a free public-sector service has suitable candidates.
- **Build:** Prototype new ways to help companies and talent make relevant, efficient connections at any stage: registration, during the event, follow-up, or end to end. More signal, less noise. Avoid reinforcing bias by nationality, language, education, career path or other unrelated traits.
- **Judging:** Impact and Relevance 45%; Innovation and User Experience 35%; Responsible and Feasible Execution 20%.
- **Requirements:** Any tech. Synthetic data only. No automated profiling or automated decisions about individuals without human involvement. Minimise personal data and show EU AI Act-compliant privacy.
- **Resources:** Subject-matter experts; example scenarios and user journeys from real events; feedback on concepts; guidance on responsible AI and privacy. Suggested sources: Duunitori, The Hub, Work in Finland open jobs, Job Market Finland; Tavata, Brella; ESCO; National Forum for Skills Anticipation (PDF on tem.fi); Suomi.fi PTV Open API; Business Espoo (https://www.businessespoo.com/).
- **Mentors:** Espoo's International Working Life Services and Business Services teams, on site and on Discord. Main contact: Melissa Arni-Hardén, Client relations manager and International Working Life Services team lead.
- **Link:** https://hackjunction.app/participate/45/challenges/319 · https://www.espoo.fi/

#### Wikipedia Through Time. (id 307)
- **Partner:** MariaDB
- **Prizes:** 1st €1,000 cash + €1,000 UpCloud credits + MariaDB certification for every member (5 vouchers at learn.mariadb.com, value 750 USD). 2nd €500 cash. 3rd €250 cash. All winners are credited in a blog post on mariadb.org.
- **Problem:** Wikipedia search is keyword-based, and its full edit history is rarely explored.
- **Build:** A Wikipedia tool that doesn't exist yet, or exists but is badly underused, with MariaDB at the core. Tracks: RAG (recommended; MariaDB native vector search for grounded, source-cited Q&A, e.g. a research assistant on the history of Finland); SVT (advanced; system-versioned tables for point-in-time views, edit wars, how a story was rewritten); Both (e.g. "what did Wikipedia say about this in 2015, and what has changed since?"). User groups: readers and/or editors. Ideas: source-grounded Q&A, fact-checking, coverage-gap detection, cross-language comparison, time-travel views, change visualisations, edit-war or bias detection, edit analytics. Note that an LLM's world view can differ from Wikipedia's neutral point of view (NPOV).
- **Judging (20% each):** Effective and creative use of MariaDB (RAG and/or SVT); Implementation (execution and scalability across the provided datasets); Usefulness for readers or editors; Design and demo quality; Originality. Bonus (0% weight): recognition for taking the SVT track or combining both.
- **Requirements:** MariaDB at the core. Source articles are in Finnish, so a multilingual embedding model is recommended for RAG (no Finnish skills needed). Any LLM, embedding model or frontend.
- **Resources:** MariaDB Server with vector search; system-versioned tables; small, medium and large Finnish Wikipedia datasets (history of Finland). Repos: https://github.com/MariaDB/mariadb-wikipedia-datasets · https://github.com/MariaDB/mariadb-vector-wikipedia-rag · https://github.com/MariaDB/mariadb-system-versioning-wikipedia (the platform's hyperlink for this last one points to the vector-RAG repo). The Guide lists a "Maria01" workshop on Sat 18:00 to 18:30, Loft, 4th floor (presumably MariaDB).
- **Mentors:** Kaj Arnö (MariaDB Foundation, Executive Chairman), Robert Silén (MariaDB Foundation, AI Lead).
- **Link:** https://hackjunction.app/participate/45/challenges/307 · https://mariadb.org/

### FinTech Track (1)

#### Personal Economic Trainer (id 311)
- **Partner:** S-Pankki (S-Bank)
- **Prizes:** 1st 2000€, 2nd 1000€, 3rd 500€, all as Airbnb gift cards.
- **Problem:** Banking stops at statements and transaction lists. S-Bank (3.5M customers; its S-mobiili app is used weekly by one in three Finnish adults) wants conversational, personalised finance. No Finnish bank yet lets customers chat with their own data.
- **Build:** An AI experience on a large synthetic transaction dataset that lets people chat with their money, from "How much did I spend on taxis last month?" to "What kind of spender am I?", "What is safe for me to spend this week?" and "How much could I save if I reduced dining out by 20%?". A pedagogical angle is valued, built on three baskets: mandatory regular (e.g. rent), mandatory irregular (e.g. a broken washing machine) and everyday leakage (e.g. coffees). Work in the MyData spirit: free exploration over fixed charts. Open benchmark data (e.g. Statistics Finland) is encouraged but not mandatory. S-Bank is interested in plain-language explanations, what-if simulation, and safe-to-spend and safe-to-save guidance.
- **Optional bonus:** a PSD2 multi-bank view.
- **Judging (20% each):** Impact on financial literacy (including the pedagogical angle); Originality of AI integration; Clarity of the mobile user experience; Feasibility; Potential to integrate into S-mobiili.
- **Requirements:** Use the provided synthetic dataset. Recommended output: a mobile app, or a web app that can be embedded in a mobile app.
- **Resources:** Data at https://github.com/hackjunction/Junction-2026-S-pankki
- **Mentors:** Carl-Edvard (Calle) Holmberg, Chief Innovation Officer (main contact); an S-Bank IT/AI development representative; a transaction-data data scientist; 1 to 2 business representatives.
- **Link:** https://hackjunction.app/participate/45/challenges/311 · https://www.s-pankki.fi/

---

## 2. Tech challenges (full detail)

#### Verda Compute Track (id 56)
- **Partner:** Verda
- **Prizes:** 1st $10,000 in Verda cloud credits + Verda hoodies; 2nd $2,500 cloud credits; 3rd $2,500 cloud credits.
- **Ask:** Pick any Junction challenge and use Verda products to build something you couldn't build on a laptop. Suggestions: train locomotion or manipulation policies for Aalto's G1 in simulation at scale; train imitation-learning or VLA policies from the Intel arm demos or Rokoko teleop data; run thousands of rollouts in an AfterQuery environment and fine-tune a smaller model; embed MariaDB's full Wikipedia dataset with batch jobs and serve RAG; run open-weight models in Europe for the banking coach or recruitment tool. Anything compute-heavy counts, except crypto mining, which gets you banned.
- **Looking for:** an ambitious idea that compute makes possible; the right Verda product with a clear reason for choosing it; your path from idea to prototype; bonus for showing how it scales to real users.
- **Minimum requirements:** document your process; share a link to a summary by **posting it in Verda's Discord channel**.
- **Judging (25% each):** Ambition (what compute let you do); Fit (right Verda services, used well); Working prototype (runs, process documented); Path to scale.
- **Technology:** Inference API (open-weight models); GPU instances and Instant Clusters (training and fine-tuning); CPU instances (agents and backends); auto-scaling containers; batch jobs; an NVIDIA Nemotron endpoint hosted by Verda with NVIDIA.
- **Credits:** Free credits for every team. Scan the QR code on your table or go to verda.com/blog/junction-2026. The Developer Tools tab lists €200 per participant (see section 3).
- **Support:** Mentors on site all weekend, 3rd floor, Booth 6. Workshop "Getting started with Verda", Fri 20:30 to 21:00 (sign-up, credits, every product).
- **Link:** https://hackjunction.app/participate/45/tech-challenges/56 · http://verda.com/

#### Best Use of MongoDB Atlas (id 55)
- **Partner:** Major League Hacking
- **Prize:** Best overall: M5Stack IoT Kit (the brief says for you and each member of your group).
- **Ask:** Build a hack using MongoDB Atlas. Students get $50 credit, or use the free-forever tier (no credit card). Free resources from MongoDB University.
- **Judging:** Not stated.
- **Resources:** https://mlh.link/mongodb
- **Link:** https://hackjunction.app/participate/45/tech-challenges/55

#### Best Use of Vultr (id 54)
- **Partner:** Major League Hacking
- **Prize:** Best overall: M5Stack mini programmable monitor.
- **Ask:** Take your hack to the cloud with Vultr (one-click deployment, cloud compute, Cloud GPUs). Sign up and claim free cloud credits.
- **Judging:** Not stated.
- **Resources:** https://mlh.link/vultr
- **Link:** https://hackjunction.app/participate/45/tech-challenges/54

#### Best Use of Tiger Data (id 53)
- **Partner:** Major League Hacking
- **Prize:** Best overall: Stream Deck Mini.
- **Ask:** The most innovative, impactful and performance-driven use of Tiger Data (PostgreSQL extended for real-time data, time-series metrics and analytics; continuous aggregates; 90%+ compression). Examples: real-time IoT monitoring, AI analytics dashboards, financial prediction engines.
- **Judging:** Not stated beyond "innovative, impactful, performance-driven".
- **Resources:** https://mlh.link/tigerdata
- **Link:** https://hackjunction.app/participate/45/tech-challenges/53

#### Best Use of Solana (id 52)
- **Partner:** Major League Hacking
- **Prize:** Best overall: Unruggable Hardware Wallets (for you and each team member, per the brief).
- **Ask:** Build on Solana: games, social or consumer apps with high-frequency transactions, trading/lending/DEX, or supply chain, identity or payments at volume.
- **Judging:** Not stated.
- **Resources:** https://mlh.link/solana
- **Link:** https://hackjunction.app/participate/45/tech-challenges/52

#### Best Use of Entire (id 51)
- **Partner:** Major League Hacking
- **Prize:** Best overall: Mini Portable Projector.
- **Ask:** Use as many of Entire's core capabilities as possible. Entire is a Git forge for agent-human collaboration. Its capabilities: Sessions (shared agent-session checkpoints for context and memory), Graph (codebase map; `entire graph search` claims up to 71% fewer tokens), Brain (persistent project knowledge, queryable via CLI or MCP) and Trails (an issue/PR combo where an agent does the work and an agent reviews it). They want seamless human-AI collaboration, clean code history and measurable token efficiency.
- **Judging:** Not stated beyond the above.
- **Resources:** Claim your code at https://mlh.link/junction-26; guide at https://mlh.link/entire
- **Link:** https://hackjunction.app/participate/45/tech-challenges/51

#### Best Use of ElevenLabs (id 50)
- **Partner:** Major League Hacking
- **Prize:** Best overall: Wireless Earbuds.
- **Ask:** Give your project a voice with ElevenLabs: realistic, expressive voices for AI companions, narration or voice-enabled apps.
- **Judging:** Not stated.
- **Resources:** Claim your code at https://mlh.link/junction-26; guide at https://mlh.link/elevenlabs
- **Link:** https://hackjunction.app/participate/45/tech-challenges/50

#### Best Use of Codex (id 49)
- **Partner:** OpenAI
- **Prizes:** 1st $10 000 API credits; 2nd $5000 API credits; 3rd $2500 API credits.
- **Ask:** Use Codex as part of your development process to build, iterate and ship an ambitious project. Open to any challenge. The key is showing meaningful use of Codex in building the solution.
- **Judging:** Not stated.
- **Resources:** https://developers.openai.com/codex · quickstart https://developers.openai.com/codex/quickstart · https://platform.openai.com/docs. $100 credits per participant through unique redemption links distributed by Junction, on the hackerpacks page (https://hackjunction.app/participate/45/hackerpacks).
- **Link:** https://hackjunction.app/participate/45/tech-challenges/49

#### Best Use of Gemini API (id 48)
- **Partner:** Google DeepMind
- **Prizes:** 1st 4000€ + $1,000 Google Cloud credits per team member; 2nd 2000€; 3rd 1000€.
- **Ask:** An open innovation challenge for a meaningful, innovative, technically impressive use of the Gemini API that goes beyond "simply adding an LLM". The submission should explain the problem and why it matters, how the Gemini API is integrated, what makes the use innovative or technically impressive, and why Gemini is important to the solution.
- **Eligibility:** Participation and the Google-provided accounts are restricted to **participants aged 18 or older**.
- **Judging:** No weighted criteria (meaningful, innovative, technically impressive).
- **Resources:** Google AI Studio (https://aistudio.google.com/) for API keys; docs https://ai.google.dev/gemini-api/docs; quickstart https://ai.google.dev/gemini-api/docs/quickstart. Gemini API credits for up to 400 teams; eligible teams receive account instructions during the event. Support at the Google DeepMind booth. Workshop "Build with Google DeepMind", Fri 20:00 to 20:30.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/48

#### Best Use of Gemma (id 47)
- **Partner:** Google DeepMind
- **Prizes:** Top 3: €1,000 per team, no ranking between winners.
- **Ask:** The most innovative and impactful use of Google's Gemma open models: creative applications, strong technical execution, open models solving real problems.
- **Judging:** No weighted criteria.
- **Access:** Featherless AI (hosted Gemma API, https://featherless.ai/models?families=gemma), Modal (serverless GPU), Verda (cloud GPU), Google AI Studio (browser), Hugging Face (https://huggingface.co/google). Docs: https://ai.google.dev/gemma/docs. Check the Junction hackerpacks for event credits.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/47

#### Best Use of Nemotron (id 46)
- **Partner:** NVIDIA
- **Prizes:** Two best teams: 1x NVIDIA RTX 5080 each.
- **Ask:** A project where NVIDIA Nemotron plays a meaningful role in doing real work (reasoning, tool use, coordinated workflows) for a clear audience. Any track. Nemotron 3.5 Super VL: 120B parameters with 12B active per token; reads text, images, documents and video.
- **Minimum requirements:** use the **Nemotron 3.5 Super VL** model in the working solution; demonstrate its contribution to core functionality; **submit a short text explanation in the submission form** naming the model used, what it does, why it matters and how you improved its outputs. (The form has no dedicated field, so put it in the Description.)
- **Judging (25% each):** Meaningful Nemotron usage; Technical execution (architecture, data flow, tool use, latency, error handling); Quality of AI output (useful, grounded, improved via prompting, evaluation or feedback loops); Creativity and differentiation.
- **Getting started:** NVIDIA Build, free hosted APIs, OpenAI-compatible, base URL https://integrate.api.nvidia.com/v1 (example model `nvidia/nemotron-3.5-lightning-30b-a3b`). The free tier is rate-limited (~40 requests/min per key, per developer forums), so use retries with backoff and give each teammate their own key. OpenRouter: `:free` variants are capped at 20 requests/min and 50/day (1,000/day after buying 10 credits). Hugging Face open weights for local runs, fine-tuning or deployment on Brev. Verda also hosts a Nemotron endpoint.
- **Support:** NVIDIA Discord channel and the NVIDIA table. Mentors: Maxime Pariente and Ryan Reese. Main contact: Elliot Winch, Community Program Manager EMEA (contact on platform). Judges: the NVIDIA team.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/46

#### Best use of Arduino Uno Q (id 45)
- **Partner:** Arduino
- **Prize:** Each member of the winning team gets an Arduino UNO Q and an Arduino Plug and Make Kit.
- **Ask:** Use the Arduino UNO Q and Modulino sensors in a project for any challenge: run AI on the device, sense the real world and make things move, light up or react. Best projects pair a working physical prototype with smart use of on-device AI.
- **Judging:** Use of Arduino hardware and Edge AI 50%; Working prototype and demo 30%; Creativity 20%.
- **Extra submission step (prize eligibility):** publish on Arduino Project Hub as well as the Junction platform: https://projecthub.arduino.cc/ → + NEW PROJECT → tag **"Junction Finland 2026"** → fill in the required parts.
- **Resources:** Borrow kits from the Arduino Hardware Lab, 5th floor (booking: https://2026.hackjunction.com/hardware). Kit: UNO Q (2 GB RAM, 16 GB eMMC), USB-C cable, USB-C hub (8-in-1), 45 W USB-C PSU, USB camera, Modulino Buzzer, Knob and Thermo. Bring a laptop with Arduino App Lab (https://www.arduino.cc/en/software/#app-lab-section).
- **Mentors:** At the Arduino Hardware Lab and on Discord.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/45

#### Best Use of Context.dev: Fully Structured Web (id 44)
- **Partner:** Context.dev
- **Prizes:** 1st €750 + swag; 2nd €250 + swag; 3rd swag.
- **Ask:** Plug the Context.dev API into whatever you're building: pages, brands, companies, people and news as structured data in one call.
- **Minimum requirements:** at least one Context.dev endpoint in the core flow (not a side feature); its data must visibly drive something in the demo.
- **What to submit:** GitHub repo + demo + **a short note on which Context.dev endpoints you used and why**.
- **Judging:** Creative use of Context.dev 40% (unusual sources, combining endpoints); How central live web data is to the product 30%; Technical execution 30% (accuracy, latency, handling change over time).
- **Getting started:** Sign up at https://context.dev/signup (coding agents can use context.dev/auth.md) → redeem the code (on platform) at https://context.dev/dashboard/redeem-credits for 50,000 non-expiring credits per team → copy a secret key from https://context.dev/dashboard/api-keys → `npm install context.dev` or `pip install context.dev` → scrape your first page via the Quickstart. MCP server at https://mcp.context.dev/mcp. SDKs for TS/Node, Python, Ruby, Go; CLI, agent skill, Playground. No credit card, no rate limit, max 50 concurrent requests per organisation. No starter repo.
- **Tips:** check each output's success flag (a 200 can contain a failed output); set `maxAgeMs: 0` for fresh data (results are cached up to 3 days and cached results cost the same); crawls, batches and monitors are async (poll or use webhooks, e.g. via Cloudflare Tunnel locally); respect site terms.
- **Mentors:** Beer van der Drift (CTO, challenge lead and lead judge; contact on platform), Yahia Bakour (Founder and CEO), Thomas Oomens (Engineer). On site Fri until 23:00, Sat 09:00 to Sun 02:00, Sun 07:00 to the end. Status: status.context.dev.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/44

#### Best Use of Aiven (id 43)
- **Partner:** Aiven
- **Prizes:** Best use of Aiven 1000€; 2nd 750€; 3rd 500€.
- **Ask:** Use at least one Aiven service as a meaningful part of your project, alongside your main challenge. Options: host on Aiven Runtime, PostgreSQL, Valkey caching, Kafka events, ClickHouse for observability, OpenSearch. One well-executed service can match a multi-service build.
- **Judging:** Meaningful use of Aiven technology 40%; Technical implementation 30%; Impact on the overall solution 20%; Creativity 10%.
- **Resources:** Sign up at https://console.aiven.io/signup for $50 free credits; docs https://aiven.io/docs/; runtime templates https://templates.aiven.io/. Aiven mentors on site all days.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/43

#### Best use of CRACI (id 42)
- **Partner:** CRACI
- **Prizes:** 1st LEGO set per member; 2nd 24-pack of Red Bull per member; 3rd invite to the CRACI x OpenAI lunch event during Slush. Top 5 teams: 50,000 CRACI CI/CD build minutes per member + an opportunity to interview for a job at CRACI.
- **Ask:** Any project qualifies **as long as its CI/CD runs on CRACI**. Go beyond adding `runs-on: craci`: use the build data (SBOMs, AI vulnerability fixes, provenance, network traces, the API) for software that defends itself, e.g. an agent that patches your app overnight, a live map of everything the internet ships into your code, or catching a malicious package as a build pulls it in.
- **Judging:** Technical depth 50%; How creatively you use CRACI's features 50% (original ideas score highest).
- **Resources and setup:** €1000 in credits per team for CI/CD or any compute; setup takes ~10 min (full steps in section 3).
- **Mentors:** Juho Niemi (CEO), Dennis Marttinen (CTO), Petteri Pulkkinen (CISO), Veeti Poutsalo (Software Engineer), Roope Ripatti (Forward Deployed Engineer). CRACI booth, 3rd floor next to the stage.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/42 · https://craci.com/

#### Best Use of Cloudinary (id 41)
- **Partner:** Cloudinary
- **Prize:** 1st: $500 worth of Amazon gift cards (your local Amazon) per team member.
- **Ask:** An innovative solution using one of the four tools listed at https://cld.media/hackathons that uses images and video for a more engaging, intelligent experience. Cloudinary must play a meaningful role, not just serve as a CDN. Any language or framework.
- **Judging:** Innovation 30%; Technical implementation 20%; UX/Design 30%; Impact/Usefulness 20%.
- **Extra submission step:** you **must** fill in https://cld.media/hackathon-survey to be considered.
- **Resources:** Generous free tier; docs https://cloudinary.com/documentation; https://cloudinary.com/pages/hackathons/
- **Mentors:** Jen Looper (Director, Developer Relations), Balazs Kemenesi (Lead Program Manager).
- **Link:** https://hackjunction.app/participate/45/tech-challenges/41

#### Best use of Modal (id 40)
- **Partner:** Modal
- **Prize:** 1st team: $2000 cash + $3000 Modal credits.
- **Ask:** Use Modal to power the project you're already building for your main challenge: serve an open model on a GPU, run agent code in Sandboxes, fine-tune on your own data, or fan out a batch job. They want the most ambitious working AI system where Modal does the heavy lifting.
- **Judging:** Effective use of Modal 40%; Technical ambition 25%; Impact (solves a real problem from your main challenge) 20%; Demo 15% (a live, deployed app judges can use).
- **Resources:** $100 credits per participant (valid one year from redemption). Sign up for Modal, then redeem through the Modal fillout form at https://modal.fillout.com/t/qMXCmRGseUus with the code on platform. Full tooling list in section 3. Modal workshop Sat 13:30 to 14:00, Loft, 4th floor.
- **Mentors:** Modal engineers and DevRel (inference, agents and Sandboxes, fine-tuning and RL, real-time audio and video), at the Modal booth and on Discord. Main contact: Filip Makraduli, Developer Relations Engineer.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/40 · https://modal.com/

#### Best agentic usecase of Oxylabs Web API (id 32)
- **Partner:** Oxylabs
- **Prize:** Winning team: €1,000 Apple gift voucher + $500 Oxylabs product credits per team member.
- **Ask:** Use the Oxylabs Web API at runtime in the agent or product you're building for your main challenge ("search to find, scrape to read"), so it acts on what is true on the web right now and proves its sources. Ideas: compare one product's price across European countries with geo-targeted search; a fact-checker that reads full pages; compare what ChatGPT, Gemini, Perplexity and Google AI Mode say on a topic with what the web says; watchers for regulations, tenders, grants or competitors.
- **Minimum requirements:** the demo makes at least one live /search or /scrape call at runtime (pre-downloaded data does not count); the solution shows source URLs for what it states or decides.
- **How to submit:** the same GitHub repo and demo as your main challenge, plus **a short note on which Web API endpoints you used and why**.
- **Judging:** Use of the Web API 30%; Real-world value 25%; Trust 20% (current, sourced, honest about failures); Execution 15%; Originality 10%.
- **Getting started:** Create a free account at dashboard.oxylabs.io → buy the $500 Flexible plan with the Junction checkout code (on platform), which gives a full first-month discount. **A credit card is required; cancel the subscription after the challenge to avoid monthly charges.** Then + Add product instance → Web API → copy the API key → `export OXYLABS_WEB_API_KEY=...` → follow https://developers.oxylabs.io/get-started/quick-start-web-api. No SDK; Python 3.10+ or Node 18+. MCP server and agent skills are available.
- **Contact:** Justas Kašėta (technical contact), contact on platform.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/32

#### Atech Real World Challenge (id 29)
- **Partner:** Atech
- **Prizes:** Best overall: a special Pro Atech kit for the team. Runners-up: Atech kits and swag. Top teams are invited to show their project on Atech's channels and visit Atech in Copenhagen.
- **Ask:** A physical device that solves a real problem for a real person, with Atech modules as its body and AI as its brain. Atech hardware is required. Ideas: assistive devices (fall detection, posture, reminders), sustainability sensing, an LLM or vision model in a loop with sensors and actuators, giving robots new senses, tools for makers.
- **Minimum requirements:** Atech modules used in the demo alongside a real-world solution; **share a link to a summary/post in Atech's Discord**.
- **Submission requirements:** a live demo on the hardware; a public GitHub repo or exported Atech project; a ~2-minute video or live demo.
- **Judging:** Real-world validation of usefulness 25%; Real-world impact 25%; Use of Atech 25%; Working demo and storytelling 25%. Bonus (0%): combining several modules, or connecting to AI models and external APIs.
- **Technology:** Snap-together ESP32 modules (distance, IMU, temp/humidity, air quality, mic, speakers, motors) plus an AI platform that writes the firmware from a plain-language description and flashes it from the browser. `pip install atech` for coding agents; an emulator; Wi-Fi or Bluetooth.
- **Access:** Pick up the team kit at the Atech booth (2 to 4 boards + modules per team depending on demand, first come first served; return everything after the final demos). Create a free account at atech.dev and redeem the code (on platform). Use Chrome or Edge (WebSerial; Safari and Firefox can't flash), a data USB-C cable, and on Linux add your user to the `dialout` group.
- **Support:** #atech on the Junction Discord + the Atech booth, with mentors throughout including a night shift. Docs atech.dev/docs; starter repos github.com/atechdotdev. Contacts: Gustav Hugod (CCO) and Tomas Harmer (CTO), contact on platform.
- **Link:** https://hackjunction.app/participate/45/tech-challenges/29 · https://atech.dev/

---

## 3. Developer Tools and Assets (full list)

The Developer Tools and Assets tab (hackjunction.app/participate/45/hackerpacks) lists 19 cards.

| Provider | Offer | How to access |
|---|---|---|
| Verda | €200 credits for AI compute (GPU) and inference API, "to solve any challenge" | Sign up to the Verda Console → claim credits via the form on the hackerpack page → redeem and share with your team per Verda's docs. The tech challenge page adds: scan the QR code on your table, or go to verda.com/blog/junction-2026. https://hackjunction.app/participate/45/hackerpacks/71 |
| OpenAI | $100 Codex credits per participant (prototype apps, build agents, speed up development) | Unique redemption links distributed by Junction on the hackerpacks page. https://hackjunction.app/participate/45/hackerpacks/70 |
| MariaDB | MariaDB database, open to every team; most interesting use of the database (neat schema, surprising query, a feature used well) gets published and credited on mariadb.org | Show it at the booth, or mention MariaDB in your submission. https://hackjunction.app/participate/45/hackerpacks/69 |
| Google DeepMind | Gemini API credits for eligible participants (up to 400 teams; 18+) | Eligible teams get account instructions during the event; keys via Google AI Studio. https://hackjunction.app/participate/45/hackerpacks/68 |
| Anthropic | $20 Claude API credits per participant | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/67. Redemption steps not stated. |
| Aiven | $50 free credits on sign-up; docs; runtime templates for open-source frameworks; mentors on site all days | Sign up at https://console.aiven.io/signup. https://hackjunction.app/participate/45/hackerpacks/66 |
| Arduino | Arduino UNO Q (2 GB RAM, 16 GB eMMC), USB-C cable, USB-C hub (8-in-1), 45 W USB-C PSU, USB camera, Modulino Buzzer, Knob and Thermo; Arduino App Lab software; usable for any challenge | Borrow from the Arduino Hardware Lab, 5th floor (Arduino booth); booking at https://2026.hackjunction.com/hardware. Bring a laptop with Arduino App Lab (https://www.arduino.cc/en/software/#app-lab-section). https://hackjunction.app/participate/45/hackerpacks/65 |
| CRACI | Free platform access + €1000 credits per team for CI/CD or any compute; GitHub Actions-compatible runners (`runs-on: craci`, default 2 vCPU / 6 GB; `cracicorp/setup@v1` with `size` 1 to 32 units of 1 vCPU + 3 GB); CycloneDX SBOMs per job and cache; AI vulnerability fixes; API (SBOMs, OCI image and cache provenance, network traces, job logs, compute usage); 5 mentors | 1) Get the Junction invite code from #craci on Discord or the CRACI booth (3rd floor, next to the stage). 2) One person per team signs up at platform.craci.com and creates an org with the invite code. 3) Settings → Builds → Install GitHub; grant repo access and wait for "configured". 4) Push a workflow with `runs-on: craci`. 5) An org admin creates an API token under Settings → API tokens (shown once); API https://api.craci.com, spec api.craci.com/openapi.json. Docs https://docs.craci.com/; migration skill https://docs.craci.com/skills/craci/SKILL.md. https://hackjunction.app/participate/45/hackerpacks/64 |
| Cloudinary | Image and video API (upload, transform, optimise, deliver; AI media features); generous free tier | Tools: https://cld.media/hackathons. Challenge submission form: https://cld.media/hackathon-survey. https://hackjunction.app/participate/45/hackerpacks/63 |
| Modal | $100 credits per participant for CPUs/GPUs (T4, L4, A10, L40S, A100 40/80 GB, RTX PRO 6000, H100, H200, B200, B300), valid 1 year; Python SDK/CLI (`pip install modal`), JS and Go SDKs for Sandboxes; web endpoints (FastAPI, WebSockets, WebRTC); Volumes, Dicts, Queues; Modal Dojo for fine-tuning/RL; Junction starter kit (vLLM/SGLang serving, STT, TTS, vision, RAG, agents, RL); mentors | Sign up for Modal → redeem via the Modal fillout form (https://modal.fillout.com/t/qMXCmRGseUus) with the code on platform. Kick-off workshop at the Modal booth (time on Discord; the Guide lists Sat 13:30). https://hackjunction.app/participate/45/hackerpacks/62 |
| Oxylabs | Web API: /search and /scrape (Markdown, HTML, JSON, screenshots); 50+ dedicated scrapers; AI Parsing; LLM answer queries; MCP server and agent skills | Junction code (on platform) for a full first-month discount on the $500 Flexible plan. **Credit card required; cancel after use to avoid monthly charges.** https://hackjunction.app/participate/45/hackerpacks/61 |
| Context.dev | 50,000 non-expiring API credits per team; SDKs for TS/Node, Python, Ruby, Go; MCP server; up to 50 concurrent requests; no credit card | Sign up at https://context.dev/signup, then redeem the code (on platform) at https://context.dev/dashboard/redeem-credits. https://hackjunction.app/participate/45/hackerpacks/60 |
| IronShard | AI-native S3-compatible object storage with MCP; zero-copy bucket forking; challenge datasets preloaded in read-only buckets where applicable; store large artifacts (beyond GitHub's 100 MiB per-file limit) and reference bucket/object in the submission; judges get read access | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/59. Sign-up steps not stated. |
| Junction | Hardware Lab | 5th floor (see section 4). https://hackjunction.app/participate/45/hackerpacks/57 |
| Wendy | Open-source tool to deploy apps to Jetson, Raspberry Pi, ESP32 and Arduino with `wendy run`; Python, Swift, Rust, ROS; simulator if you have no hardware | Find the Wendy team at Junction. https://hackjunction.app/participate/45/hackerpacks/56 |
| Qualia | Robot-learning data platform: upload SO-101 or Rokoko recordings, automatic quality checks for failed takes, timing and inconsistency, curated versioned datasets, export for training (e.g. pi0.5 with LeRobot) | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/53. Access steps not stated. |
| Featherless | Bare-metal GPU credits for selected teams (fine-tuning, embeddings, GPU-heavy work) | Selection process not stated. https://hackjunction.app/participate/45/hackerpacks/52 |
| Featherless | $50 API credits for the open-weight model catalogue (includes hosted Gemma) | Dedicated Junction coupon (on platform). https://hackjunction.app/participate/45/hackerpacks/51 |
| Scailab | Scaipipe: annotate images, generate labelled synthetic data from 3D scenes, train and evaluate detection, segmentation and tracking; runs in the browser (no GPU needed); built-in MCP server | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/50. Access steps not stated. |
| Exa | $50 credits per participant; full Search and Contents APIs, Websets, Monitors, hosted MCP, Python/JS SDKs; demo gallery demos.exa.ai | Promo code (on platform); redeem at https://dashboard.exa.ai/billing. https://hackjunction.app/participate/45/hackerpacks/49 |

Credits and access that appear only in challenge briefs, not on the Tools tab:
- Hostinger VPS, AI Router credits and AI Builder (357)
- AfterQuery frontier model credits and the Harbor/OpenCode harness (328)
- Valio Aimo resource portal and mock API (327; password and key on platform)
- Cala credits (350; promo code on platform)
- Intel stations and cloud GPUs (330)
- Verda GPU for the Aalto humanoid sim (320)
- Rokoko SDK licence via form (326)
- Bahn Spread event code (349; on platform)
- Tieto partner model credits on the Junction Platform (351)
- Atech kits and platform code (29; on platform)
- MLH partner codes via mlh.link/junction-26 (50, 51)
- NVIDIA Build free API keys (46)

---

## 4. Hardware lending (snapshot Fri 13 Nov 19:52)

Source: https://2026.hackjunction.com/hardware ("Last updated Fri 19:51 · Checked 19:52:19"). 192 items were free across 7 types.

**Hardware alert:** Meta Ray-Ban Display glasses had **2 of 10 free, 22 waiting requests and a 120-minute loan limit**. Any glasses idea has to plan around short, contested device time.

| Item | Free / total | Waiting requests | Loan limit | Contents / notes |
|---|---|---|---|---|
| Arduino dev kit | 153 / 160 | 19 | No time limit | 1 power supply, 1 knob, 1 thermo, 1 buzzer, 1 UNO Q, 1 USB-C hub, 1 USB camera |
| Atech dev kit | 5 / 7 | 6 | No time limit | Motherboard, 4 DC motors, distance sensor, 2 LED arrays, 2 orientation sensors, 2 buttons, speaker, knob, screen |
| Intel Core Ultra X9 Series 3 AI PC | 22 / 25 | 13 | No time limit | Dell XPS 16 [DA16260], HP OmniBook Ultra [C2NM8AV] |
| **Meta Ray-Ban Display Glasses** | **2 / 10 ("Running low")** | **22** | **120 minutes** | Black Standard Frame |
| Meta Ray-Ban GEN2 | 5 / 10 | 9 | 240 minutes | Wayfarer, Shiny Black, Transitions Graphite Green lens |
| ROKOKO Smartgloves | 5 / 8 | 5 | No time limit | |
| ROKOKO Suit | 0 / 1 (all checked out) | not shown | No time limit | ★ Special item: one per team at a time |

### 3D printing (desk-managed queue)
Speak to a volunteer at the hardware desk to queue a print. The workflow may change, and times are estimates. The waiting queue was empty at the snapshot.

| Printer | Model | Status |
|---|---|---|
| B1 | Prusa Core One | Free |
| B2 | Bambu Lab P1S | Free |
| B3 | Bambu Lab P1S | Free |
| B4 | Prusa Core One | Free |
| B5 | Original Prusa MK4 | Free |
| B6 | Original Prusa MK4 | Free |
| B7 | Original Prusa I3 | Out of service |
| F1 | Bambu Lab P1S | Out of service |
| F2 | Bambu Lab P1S | Out of service |
| F3 | Bambu Lab P1S | Free |
| F4 | Bambu Lab P2S | Free |
| F5 | Prusa Core One Plus | Free |
| F6 | Prusa Core One Plus | Free |

10 of 13 printers free; 3 out of service (B7, F1, F2).

### Borrowing process
From the hardware page:
1. **Choose hardware.** Browse availability, sign in with your Junction account at https://2026.hackjunction.com/hardware, and pick a **first and second choice** (max 2 items, in priority order).
2. **Send one request per team.** A request does not reserve stock. A volunteer confirms your equipment at the desk.
3. **Collect, build, return.** Go to the desk with your **team name and photo ID**, and return the equipment to a volunteer when done.

From the challenge pages and Developer Tools tab: pickup is at the **Arduino Hardware Lab, 5th floor**. Atech kits are handed out at the Atech booth; Intel stations are in the Hardware Lab.

From the task brief (not on the scraped page): the photo ID is the responsible person's, and the team needs its **table number** to request. Our table number was "Not set yet" in the event guide, so set it before requesting.

Loan limits matter for the glasses: Display glasses come back after 120 minutes and GEN2 after 240 minutes, and 22 teams were already queued for the Display at 19:52.

---

## 5. Project Submission, Your Submissions and Peer Review

### Project Submission tab (hackjunction.app/participate/45/project)
Status at scrape: Closed. The countdown runs to Sat 12:00, when submissions open. The form has a Preview toggle and Draft status, and two buttons: **Save Draft** and **Submit Final**. Saving is disabled until every required field is filled.

| Field | Required | Rules |
|---|---|---|
| Project Name | Yes | Clear and descriptive, max 30 characters |
| Punchline | Yes | One-liner capturing the essence, max 200 characters |
| Description | Yes | What you built and the problem it solves, max 5000 characters, supports Markdown |
| Challenge Picker | Yes | "Select which challenge track your project is participating in" |
| Project Demo | No | Link where the project can be experienced live |
| Source Code | No (form) | Link to the source repository. **Junction rules require a source link.** |
| Video | No (form) | Link to the recorded demo (YouTube, Loom, etc.). **Junction rules require a pitch video of max 2 minutes.** |
| Other Link | No | Any other relevant link |
| Presentation | No | Upload PDF, PPTX, PPT, ODP or KEY, max 20 MB (stored on S3) |
| Tech Challenge Participation | No | Multi-select of the tech challenges the project enters |

The Guide's list for final submission is longer than the form: project name, punchline, description; challenge; technologies used; a 2-minute video pitch (publicly viewable on YouTube, Vimeo or similar, "not a second longer than 2 minutes, and we will be very strict"); demo and source code links; source code publicity; whether you want to be credited; pitch deck (PDF); team members' phone numbers (they call winners); Discord usernames. Several of these fields were not on the form at scrape time, so check again when the form opens on Saturday.

Submission rules from the Guide:
- One team member creates the project submission. A draft by Fri 23:59 is used for the team count.
- **Set the project from DRAFT to FINAL before Sun 10:00. Draft projects are not reviewed.** You can edit at any time before the deadline, including final projects.
- The form closes automatically, and late submissions are not accepted.
- You can change your chosen challenge after the Friday pre-submission, and you can submit to multiple challenges.
- Top teams are contacted about pitching before the Closing Ceremony.

Junction rules (prize eligibility, including the €10,000 main prize):
- No code written before the event.
- Team size 1 to 4.
- Take part in at least one challenge.
- Take part in Sunday's live peer review (required for the main prize).
- Include a pitch video of at most 2 minutes.
- Link your source code. All code outside open-source libraries must be written at the event. Pre-written code for the idea, or a project tied to an existing company, means disqualification.
- All submissions are licensed under MIT, and organisers must be able to access the source.
- Partner APIs and materials remain subject to partner terms.

### Your Submissions tab (hackjunction.app/participate/45/submissions)
At scrape time: "You have no submissions yet. Start one to get going." It has a **New submission** button that links to the Project Submission tab. (The Dashboard showed a placeholder draft card, "Project Title", with an Edit Submission link.)

### Peer Review tab (hackjunction.app/participate/45/peer-review)
At scrape time: "Pitching rounds have not been assigned to your team yet. Check back later."

How peer review works (Guide):
- Partner review and peer review run in parallel straight after the deadline.
- Every hacker must be at the venue for live peer review on Sunday (10:30 to 13:00 per the schedule; 10:30 to 14:00 per the rules text).
- Each participant reviews the projects assigned to them. If the pitching team is not at its table, press **"not present"**.
- Skipping peer review makes your team ineligible for the main prize.
- Peer review criteria: **Innovation** (new or different from projects already presented), **Impact** (significant societal impact, share of affected people helped), **Implementation** (realistic, viable, feasible).
- The Top 5 by peer review pitch on stage: exactly 3 minutes (mics cut at time) plus 3 minutes of judges' questions, one handheld mic, and you can demo from your own laptop (connection checked beforehand). There is no separate rehearsal slot after review ends. A panel of 7 judges picks the winner.

---

## 6. Workshops and talks (Guide schedule)

| When | What | Where |
|---|---|---|
| Fri 18:30 to 19:10 | Keynote: Google DeepMind, NVIDIA, MLH | Main stage, 3rd floor |
| Fri 20:00 to 20:30 | Build with Google DeepMind | Registration area 2nd floor (schedule) / Loft 4th floor (workshop list) |
| Fri 20:30 to 21:00 | Verda: Getting started with Verda | Registration area 2nd floor / Loft 4th floor |
| Fri 20:30 to 21:00 | Arduino | Arduino Hardware Lab, 5th floor |
| Fri 21:00 to 21:30 | MLH x GitHub | Registration area, 2nd floor (TBA) |
| Sat 11:00 to 11:30 | Cala: Tips & tricks to Make Unicorns Real | Loft, 4th floor |
| Sat 12:00 to 12:30 | Intel hands-on session | Hardware Lab, 5th floor |
| Sat 13:00 to 13:45 | Hostinger keynote: "Vibe Coding Solved Building. Now Comes the Hard Part" | Main stage |
| Sat 13:30 to 14:00 | Modal | Loft, 4th floor |
| Sat 14:30 to 15:15 | Can It Be a Company? with Kiuas (business-case sparring) | Loft, 4th floor |
| Sat 16:30 to 17:00 | Exa | Loft, 4th floor |
| Sat 17:30 to 18:00 | Context.dev | Loft, 4th floor |
| Sat 18:00 to 18:30 | "Maria01" (likely MariaDB) | Loft, 4th floor |

Org contact: hello@hackjunction.com. Discord is the main channel (#announcements, challenge-specific channels, #teambuilding).

---

## 7. Scrape notes

- **Errored page:** `partnerChallenges.txt` (hackjunction.app/partners/45/challenges) timed out, so it has no content. It is the partner-side view, so nothing participant-facing is lost.
- **Rethinking Recruitment (319)** loaded with "Status: Loading..." in the header, but its full brief and criteria were captured.
- The Partners tab includes AstraZeneca, Intel and Meta with no description. Lifeline Ventures and XR Creator Con appear as partners with no challenge.
- The Team tab was scraped too. Its member contact details are deliberately left out of this doc.
