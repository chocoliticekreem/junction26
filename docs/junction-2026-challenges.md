# Junction 2026: Challenges, Tools and Hardware

Scraped from hackjunction.app/participate/45 (Challenges list, 19 challenge detail pages, Developer Tools and Assets tab) and 2026.hackjunction.com/hardware on **Fri 13 Nov 2026, ~19:50 Helsinki time**.

| Deadline | When |
|---|---|
| Preliminary submission | **Tonight, Fri 13 Nov, 23:55** |
| Submissions open | Sat 14 Nov, 12:00 (page countdown read T-16:09 at scrape time, which matches) |
| Final submission deadline | **Sun 15 Nov, 10:00** |

**Hardware alert at snapshot (Fri 19:52):** Meta Ray-Ban Display glasses had **2 of 10 free, 22 waiting requests, 120-minute loan limit**. Any glasses idea has to plan around short, contested device time.

Access codes, promo codes, passwords and API keys that appear on the platform are written here as "on platform". Look them up on the challenge page or the Developer Tools tab.

---

## 1. Summary of all 19 challenges

| Track | Challenge (id) | Partner | Prize | One-line ask | Hard requirements |
|---|---|---|---|---|---|
| Agentic AI | Decode the Noise (357) | Hostinger | 1st 2000 €, 2nd 1000 €, 3rd 500 €; all 3 winners also get 1 yr hosting + domain, swag, social spotlight | AI tool that detects propaganda, bots and bad actors online | **Must be deployed live on Hostinger infrastructure with a public URL** by the end of the hackathon |
| Agentic AI | Earned Trust in AI Code (351) | Tieto | 1st €2,000, 2nd €1,000, 3rd €500 | AI code review concept + reference implementation where a named human stays accountable | Synthetic or cleared sample data only; one sample agent-written change with its requirement ID; deliverables: concept card, live walkthrough, lessons log, demo video/presentation |
| Agentic AI | Spread (349) | Bahn Express | 1st 2000€, 2nd 1000€, 3rd 500€ | Agent that runs a simulated car transport company for a week, maximising gross margin | Play on spread.bahnexpress.com; ≥90% of cars on time; must reach top 10 of the Sun 08:00 final (registration closes 07:30) to present |
| Agentic AI | Break the Agent (328) | AfterQuery | 1st 3,000€ + work trial + merch, 2nd 1,500€ + merch, 3rd 500€ | RL environment where frontier agents fail meaningfully and the reward resists hacking | Must show a reproducible gap vs a stronger reference run; judges rerun with the standard harness (Harbor + OpenCode over MCP); one-command README eval |
| Agentic AI | Trusted Trade Agents (327) | Valio Aimo | 1st 4 000€, 2nd 2 000€, 3rd 1 000€ | Interface + operating model letting external purchasing agents look up, order and get human approval from a food wholesaler | Must enable: product/price/availability lookup; request → order on fixed prices; permission and human-approval management. Build against Valio Aimo's mock APIs (synthetic data) |
| Agentic AI | The Internet Butler / Your Personal Assistant (298) | Exa | 1st $2,500 + $5,000 Exa credits + hoodies + Exa TRMNL dashboard; 2nd $1500 + $3,000 credits + hoodies + macropad; 3rd $500 + $1k credits + hoodies | Personal agent that does tedious real-life tasks using live web info | Must use Exa; demo on a real case; must work on judges' live queries |
| Hardware (Arduino) | The Green European Renaissance (356) | Arduino | 1st Ventuno Q per member; 2nd UNO Q 4G + Plug and Make Kit per member; 3rd Plug and Make Kit per member | Edge AI on Arduino UNO Q for local, green/environmental problems | **Must use Arduino UNO Q / edge AI; must also publish on Arduino Project Hub with tag "Junction Finland 2026"** to be prize-eligible; physical prototype judged |
| Hardware (Arduino) | AI Glasses for Everyone, Everyday (342) | Meta | Best overall: Ray-Ban Meta glasses per member | Everyday use case where a first-person view on Meta AI glasses enables new interactions | **Must use Meta AI glasses** (Ray-Ban Display or RBM Gen 2; web app or Device Access Toolkit); functional prototype + deck |
| Hardware (Arduino) | Stop Simulating, Start Moving: Intel Physical AI Challenge (330) | Ignite Next x Intel | 1st €5,000, 2nd €3,000, 3rd €2,000 | SO-101 arm autonomously picks Duplo bricks, inspects them, sorts good/defective | **Must use the provided station**: SO-101 arm, Physical AI Studio (VLA), Anomalib, OpenVINO on Intel Core Ultra Series 3 laptop (CPU/GPU/NPU); agree to Challenge Terms |
| Hardware (Arduino) | The Robot Teleoperation Challenge (326) | Rokoko | 1st Smartgloves II + SDK licence + blog feature (~€4,990); 2nd Smartsuit Pro II (~€2,295); 3rd Smartgloves I + merch (~€1,095) | Teleoperate robot hands/arms/humanoids with Rokoko mocap | **Must use Rokoko motion capture** (physical robot or simulation) |
| Hardware (Arduino) | Aaltonomous Humanoid (320) | Aalto University | Winner 2,000€ + Aalto robotics lab visit; top ~5 (by sim score) run live on the real Unitree G1 | Give the Unitree G1 a brain: autonomously sort coloured objects into boxes in 2 min | **Submit a Docker image policy server**; must pass sim safety check (no crashes/safety stops, within joint/speed limits, ≥27 commands/s) to run on the real robot; Isaac Sim needs RTX-class GPU (not A100/H100) |
| FinTech | Make Unicorns Real (350) | Cala | 1st: "Cala Comet" per member (~€5,000 for a team of 4: one hackathon/month for 3 months, travel + stay covered) + €1,000 Cala credits + merch; Runner-up: 500€ (detail page says €500 in Cala credits) + merch | Product for founders/investors built on Cala's structured company/funding data | **Cala must be core** to the product (25% of score) |
| FinTech | Personal Economic Trainer (311) | S-Pankki (S-Bank) | 1st 2000€, 2nd 1000€, 3rd 500€ (all Airbnb gift cards) | AI that lets people chat with their own banking data as a financial coach | Use the provided synthetic transaction dataset; mobile app or embeddable web app recommended |
| Healthcare | Equal Care Across Finland (344) | AstraZeneca | 1st 1000€, 2nd 750€, 3rd 250€ | AI system that finds gaps in Finnish cancer care pathways and recommends fixes | Must: cite reliable evidence for every claim; cover ≥1 indicator tied to Goal 3 of the national cancer strategy; give actionable recommendations; working demo (slides alone insufficient) |
| Healthcare | Beyond the Clinic (343) | Aalto University | To be announced | Product that helps people stay well at home after TMS depression treatment | Not stated (laptop + phone are enough) |
| AI Infrastructure (by Verda) | Make Blueprints Talk (335) | Stoa | 1st 1000€ + work trial at Stoa, 2nd 750€, 3rd 250€ | Answer natural-language questions about construction drawings, verifiably | Use Stoa's dataset; answers must show where in the drawing they came from; low inference cost is 25% of score |
| Data | The Web Is Your Real-Time Database (332) | Context.dev | 1st €2,000 + swag, 2nd €500 + swag, 3rd swag | Product that reacts to the live web | Use Context.dev (implied by judging on live web data) |
| Data | Rethinking Recruitment (319) | City of Espoo | 1st 1500€, 2nd 1000€, 3rd 500€ | Improve matching between companies and talent at Espoo recruitment events | Synthetic data only; no automated decisions about individuals without a human; minimise personal data; EU AI Act-compliant privacy |
| Data | Wikipedia Through Time. (307) | MariaDB | 1st €1,000 cash + €1,000 UpCloud credits + MariaDB certification per member (5 vouchers, value 750 USD); 2nd €500; 3rd €250 | Wikipedia tool using MariaDB vector search (RAG) and/or system-versioned tables | **MariaDB must be at the core**; use provided Finnish Wikipedia datasets |

Source-page discrepancies: the list page shows only 1st and 2nd for Hostinger; the detail page adds 3rd 500 €. For Cala, the list page says runner-up "500€ + Cala Merch" and the brief says "€500 in Cala credits and Cala merch". The Exa brief still contains template placeholders ("[cash amount]"), but its structured prize list gives real amounts.

---

## 2. Challenges by track

### Agentic AI Track (6)

#### Decode the Noise (id 357)
- **Partner:** Hostinger
- **Prizes:** 1st 2000 €, 2nd 1000 €, 3rd 500 €. All three winning teams also get one year of Hostinger hosting and a domain, Hostinger swag, and a spotlight on Hostinger's social channels.
- **Problem:** Propaganda, bot networks and bad actors manipulate the open web at scale.
- **Build:** A tool that analyses text, social content or web-traffic patterns to detect coordinated propaganda, bot-driven amplification or bad-actor behaviour. It can be an API, dashboard, explainable classifier or monitoring service for site owners. Hostinger cares more about the strength and honesty of the detection logic, including false-positive handling, than about a polished front end.
- **Directions (pick one or combine):**
  - Spot the swarm: detect coordinated inauthentic behaviour (bot networks, astroturfing, brigading) from posting timing, account similarity, text reuse and amplification patterns, not single posts.
  - Name the technique: classify manipulation techniques (loaded language, fear appeals, whataboutism, fabricated authority) and explain the verdict in plain language.
  - Clean the traffic: separate malicious bots, scrapers and credential stuffing from real visitors in web-server logs, with an actionable view for site owners.
  - Trust the source: score provenance of a page or account (domain age, cloned content, AI-generated text, link networks).
  - Show precision and false-positive rate, not just a happy-path demo.
- **Judging:** Detection quality (accuracy, false-positive handling, explainability) 40%; Technical execution and live deployment on Hostinger 25%; Originality and real-world impact 20%; Demo clarity 15%.
- **Required tech / constraints:** Must be deployed and running live on Hostinger infrastructure by the end of the hackathon, with a public URL judges can open. Any language, framework or model, open-source or hosted, as long as the final product runs on Hostinger.
- **Resources:**
  - Full Hostinger environment free for 1 month per team.
  - Hostinger VPS (KVM 2) per team: 2 vCPU, 8 GB RAM, 100 GB NVMe, 8 TB bandwidth, root access, Docker, free domain, one-click templates for Ollama, n8n, Node.js and Python.
  - Hostinger AI Router credits per team: one API key and shared credit balance for 150+ models (Anthropic, OpenAI, DeepSeek, Mistral, xAI and more), OpenAI- and Anthropic-SDK compatible.
  - Hostinger AI Builder 1-month plan for front ends, dashboards or landing pages.
  - Hostinger Connector, API and CLI to deploy from Claude Code, Cursor, VS Code or any MCP client. Docs: https://docs.hostinger.com/hostinger-connector · API: https://developers.hostinger.com/ · MCP server: https://github.com/hostinger/api-mcp-server
  - Dedicated Hostinger help channel all weekend (link shared at kick-off and at the booth).
  - Talk: "Vibe Coding Solved Building. Now Comes the Hard Part", Sat 13:00. Promising teams get a path to continue with Hostinger engineering after the event.
- **Mentors:** Minijus Savickas (VPS Product), Emilis Strimaitis (Innovations, AI agents), at the Hostinger booth all event.
- **Link:** https://hackjunction.app/participate/45/challenges/357 · https://www.hostinger.com/

#### Earned Trust in AI Code (id 351)
- **Partner:** Tieto
- **Prizes:** 1st €2,000, 2nd €1,000, 3rd €500 (cash).
- **Problem:** Agent tokens passed human tokens in Feb 2026 and reached 7.3 trillion by Aug (OpenRouter data, a16z chart). Reviewing every agent change by hand does not scale, but engineers need a sound basis to trust AI-reviewed code.
- **Build:** Design an AI code review concept and show it works: concept, principles, reference implementation and technology considerations across frontend, backend and security. Question whether line-by-line review is still right. Balance risk, hallucination, transparency, confidence and quality. The output is a reference implementation, not a product.
- **Expected from each team:**
  - Define the concept the "PR review" factory should follow.
  - State key principles, including how it balances risk, hallucination, transparency, confidence and quality.
  - Illustrate it on one sample agent-written change with its requirement ID.
  - Show what the AI found, what it refused to decide, and why.
  - Show how the evidence lets a named human accept the change without a full read.
  - Name the failure modes seen and keep a short decision log.
- **Deliverables:** Concept card (recommendation, principles, trade-offs, limits); live walkthrough showing where trust comes from; lessons log; demo video/presentation.
- **Out of scope:** a finished product, model training, vendor selection.
- **Tieto's trust principles (insight section):** a named engineer owns and signs off each change; the AI review is advice with evidence, never the approval; evidence traces to a requirement; review depth follows risk; humans spot-check the AI reviewer and track misses; trust is earned per area from track record and withdrawn after escapes. The owner signs: what was checked and by whom/what, what was not checked and why, the residual risk accepted. Not accepted: "The AI said it was fine" (an unowned merge); confidence without evidence or an unexplained risk score. Vendor guidance: route human attention by risk; review with full repo context and verify findings before posting; measure outcomes (reverts, incidents), not review activity.
- **Optional directions:** a generalist reviewer covering frontend, backend, security and performance; or a classifier separating code that needs human review from code that meets the standard.
- **Judges will ask:** What would make you not trust your own output? Who owns the decision? How would this scale?
- **Judging:** Clarity 30% (clear recommendation, principles, explicit trade-offs and limits); Practicality 25% (works in a real PR flow and scales, named human owns each decision); Measurement 25% (reverts and incidents don't rise as review time falls, AI findings real and accepted, time to merge, share routed to humans); Evidence 20% (evidence traceable to a requirement lets a named human accept without a full read, including what the AI found, refused to decide, and why).
- **Required tech / constraints:** Synthetic or cleared sample data only. Models from other Junction partners via partner credits on the Junction Platform.
- **Resources:** Tieto's background on good code (standards, security, quality); a requirements set (intent, functional, non-functional); sample agent-written changes each with a requirement ID; model access via partner credits.
- **Mentors / contact:** Not stated.
- **Link:** https://hackjunction.app/participate/45/challenges/351 · https://www.tieto.com/

#### Spread (id 349)
- **Partner:** Bahn Express
- **Prizes:** 1st 2000€, 2nd 1000€, 3rd 500€.
- **Problem / world:** Bahn moves cars for dealers; a freelance driver drives each car. Spread simulates a week in Finland with dealers, cars, deadlines and drivers.
- **Build:** The system that runs the company for the week. Dealers ask you and a competitor for a price; quote too high and you lose the car. Win it, post the drive as a gig in the drivers' app and set the fee; pay too little and no driver takes it in time and the car is late.
- **Scoring:** Gross margin (dealer payments minus driver payments). At least 90% of cars must arrive by deadline.
- **Timeline:** Ranking rounds open Fri 19:30; every team plays the same secret weeks; Bahn's own best system plays every round. Final Sun 08:00: each team plays its own copy of one secret week, running by itself for ~34 minutes. Registration closes 07:30.
- **Judging:** The 10 ranked teams with the highest margin present to the jury (5–10 slides or a short video). The jury judges how elegant, clear, creative and robust the system is. Reaching the top 10 is enough; after that margin no longer counts. No weighted criteria listed.
- **Required tech / constraints:** Join at https://spread.bahnexpress.com/join with the event code (on platform). Handbook, rules, API reference, TypeScript and Python kits and leaderboard are on the site. Agent-readable docs: https://spread.bahnexpress.com/llms.txt
- **Contact:** Bahn booth (rules, the world, real dispatch, hints). Named mentors not stated.
- **Link:** https://hackjunction.app/participate/45/challenges/349 · https://www.bahnexpress.com/

#### Break the Agent (id 328)
- **Partner:** AfterQuery
- **Prizes:** 1st 3,000€ + work trial at AfterQuery (straight to final interview stage with the environments team) + merch; 2nd 1,500€ + merch; 3rd 500€. Finalists get AfterQuery gear.
- **Problem:** Frontier agents still struggle in novel situations. Building a good environment (problem, action/observation space, reward) is a research problem in itself.
- **Build:** An environment an agent can interact with (game, scientific sim, software task, real-world process, anything). Clear goal, actions, checkable reward. Run a frontier agent and compare with a stronger reference run your team can demonstrate and reproduce. Show where the agent falls short and why; difficulty must come from decisions, with the information and tools to succeed available. Judges will hunt for reward hacking.
- **Starting points:** planning several steps ahead; exploring an unfamiliar system; using tools; managing limited resources; adapting when new information arrives. A small environment with a well-chosen challenge can be enough.
- **Stretch:** Train a smaller model on experience from your environment and show whether it improves.
- **Judging rubric:**
  - The gap (30 p): full points if the frontier agent consistently scores below your demonstrated stronger reference run and both reproduce across repeated runs. Zero if there is no measurable gap or it cannot be reproduced or checked.
  - Meaningful difficulty (30 p): full points if you can explain the agent's main mistakes and tie them to task decisions, with needed info/tools available. Zero if the gap comes from withheld information, trick wording, impossible timing or broken tools.
  - Reward integrity (25 p): full points if the reward measures task success and holds up to judges' exploits; doing nothing or stopping early earns little or nothing; completing the task well is the best way to score. Zero if an exploit, loophole or task-avoiding strategy beats successful play.
  - Craft (15 p): full points if rules and behaviour make sense and judges can run the eval from your README with one command and reproduce results. Zero if it only works in your demo.
- **How judging runs:** 10-minute demo. Judges rerun with the standard harness: your reference run, three agent runs, a do-nothing baseline, a stop-early baseline, plus 15 minutes of exploit hunting. Tiebreaker: a smaller model improving after training on your environment.
- **Resources:** Open-source harness Harbor running the OpenCode agent, connecting to your environment over MCP; scoring skeleton; frontier model API credits per team; starter kit (harness docs + rubric); on-site mentors for environment design and reward testing.
- **Mentors:** Daksh Raghuwanshi and Ved Vedere (AfterQuery environments team), on site all weekend.
- **Link:** https://hackjunction.app/participate/45/challenges/328 · https://www.afterquery.com/

#### Trusted Trade Agents (id 327)
- **Partner:** Valio Aimo
- **Prizes:** 1st 4 000€, 2nd 2 000€, 3rd 1 000€.
- **Problem:** Valio Aimo (20,000+ professional kitchens, 25,000 products from 700 suppliers) plans a B2B marketplace. As ordering moves to autonomous purchasing agents, the wholesaler must decide what agents can see, decide and be trusted with. For Junction they mock today's webshop and backend, not the marketplace.
- **Build:** The interface and operating model that lets an external purchasing agent find, compare, order and handle exceptions with Valio Aimo, on open, verifiable standards rather than a single platform's black box.
- **Core (must enable):**
  - Product, price and availability lookup in structured form.
  - Request price and availability, then place an order (fixed prices, not negotiated quotes).
  - Permission and human-approval management: what the agent decides alone vs what goes to a human.
- **Optional (not required to win):** delivery time and sustainability comparison (certificates/labels; category-level carbon ranges as stretch); substitution and exception handling (not scored as core); traceability and explainability.
- **Example request:** "I need 1,000 litres of lactose-free milk by Monday. Find an option that meets our requirements based on price and availability." A hotel chain's agent sends it; the solution returns structured products, prices and availability; the agent orders within its authority or escalates for approval.
- **Problems they'd love tackled:** trust protocol (minimum verification for stock, price, origin claims); guardrails model (spend thresholds, out-of-preference substitutions); response logic (partial availability, good-better-best substitution within Valio Aimo's assortment); audit trail readable by buyer and Valio Aimo.
- **Example scenarios:** need → recipe → order; last-minute event with recipe-logic substitutions; supplier stock-out with recipe-compatible substitute; proactive selling agent; allergen-safe substitution in school/hospital kitchens; standing-order drift detection.
- **Scope note:** they mock a structured data/API interface; whether production becomes a traditional API, MCP-style interface or a service agent is out of scope.
- **Judging:** Working end-to-end demo 30% (full request → lookup → order/approval flow in the mock environment); Solving the problem and user need 20% (precise match to what the buyer asked, least manual correction); Autonomy and controls 20% (guardrails, human sign-off, logging and auditability); Robustness to exception situations 15% (partial availability, substitutions, delivery constraints); Openness and credible path toward production 15% (open documented standards, visible assumptions, justified tech choices, credible next steps).
- **Required tech / constraints:** Build against the synthetic catalog, simulated suppliers and mock APIs. No live or confidential data. Preferred tech: agentic/tool-use frameworks, open data/interop standards, recommendation logic, optional verifiable credentials or trust layers. Agentic payment standards (x402, Nevermined) are relevant context, not required.
- **Resources:** Resource portal https://junction26.valioaimo.fi/ (password: on platform) with datasets, API docs and mock backend access. Mock API key: on platform. Webshop test accounts to be shared separately.
- **Mentors:** Marketplace/Commercial: Hanna Forsström, Pirjo Kaartinen. Online Sales: Minni Ruhtinas. IT/Tech integrations and data governance: Tommi Nurmi-Aro, Ville Takanen, Riku Tapper.
- **Link:** https://hackjunction.app/participate/45/challenges/327 · https://www.valioaimo.fi/

#### The Internet Butler / Your Personal Assistant (id 298)
- **Partner:** Exa
- **Prizes:** 1st $2,500 cash, $5,000 Exa credits, Exa hoodie per person, Exa-branded TRMNL dashboard. 2nd $1500 cash, $3,000 Exa credits, hoodie per person, Exa-branded macropad. 3rd $500 cash, $1k Exa credits, hoodie per person. Participation: every Junction participant gets $50 free Exa credits.
- **Problem:** Everyday tasks (is a rent increase legal, which benefits a family qualifies for, picking a vegan restaurant) need hours of digging across the web.
- **Build:** A personal agent that finds what matters across the web, works out what needs to happen and gets the task as close to done as it can, leaving final approval to the user if needed. Demo on a real case. Areas: planning special occasions, daily errands, rent, missed benefits, business information, travel disruption.
- **Judging (20% each):** Use of Exa (information that could not come from training data alone); Usefulness (to a specific group of real people); Clarity (showing sources); Originality; Working implementation (works on live queries, including the judges' own).
- **Required tech / constraints:** Exa.
- **Resources:** $50 Exa credits per participant (promo code on platform; redeem at https://dashboard.exa.ai/billing). Full API: Search (fast, balanced, deep research modes), Contents (full text, highlights, summaries, subpage crawling), filters by date/domain/category (news, papers, companies, people, personal sites), structured JSON output, past page versions, Websets, Monitors, hosted MCP server, Python and JS SDKs. Demo gallery: https://demos.exa.ai/
- **Mentors:** Exa engineers on site all event, plus a Discord channel. No names stated.
- **Link:** https://hackjunction.app/participate/45/challenges/298 · https://exa.ai/

### Hardware Track by Arduino (5)

#### The Green European Renaissance (id 356)
- **Partner:** Arduino
- **Prizes:** 1st: a Ventuno Q unit per team member. 2nd: UNO Q 4G + Plug and Make Kit per member. 3rd: Plug and Make Kit per member.
- **Problem:** The US and Asia lead the AI revolution. Arduino's pitch: Europe can use edge AI devices like the UNO Q to build local solutions to local problems, independent of governments or big companies, for a greener Europe.
- **Build:** Edge AI and Arduino UNO Q Physical AI for local problems that improve lives and create a greener environment. Example directions: boosting local flora and fauna, saving energy, supporting elderly independence, reducing industrial impact, tackling climate change, energy efficiency, cutting pollution, more livable cities.
- **Judging:** Technical Implementation and Edge AI 30% (use of UNO Q, sensors, on-device AI); Environmental and Social Impact 30%; Creativity and Innovation 20%; Working Prototype and Demo 20% (a functioning physical prototype).
- **Required tech / constraints:** Arduino UNO Q and edge AI. **To be prize-eligible you must publish on Arduino Project Hub as well as submit on the Junction platform**: log in at https://projecthub.arduino.cc/ → + NEW PROJECT → tag "Junction Finland 2026" → fill in required parts.
- **Resources:** Hardware kit with Arduino UNO Q and Modulino sensors from the Arduino Hardware Lab, 5th floor. Install Arduino App Lab: https://www.arduino.cc/en/software/#app-lab-section
- **Mentors / contact:** Not named on the challenge page (Developer Tools tab says Arduino mentors on site).
- **Link:** https://hackjunction.app/participate/45/challenges/356 · https://www.arduino.cc/

#### AI Glasses for Everyone, Everyday (id 342)
- **Partner:** Meta
- **Prizes:** Best overall: each member of the winning team gets a pair of Ray-Ban Meta glasses. Best teams may be invited to a Meta AI forum on Wed 18 Nov 2026 on the future of wearable AI.
- **Problem:** Find where a first-person view creates value beyond mirroring a phone screen.
- **Build:** The best everyday use case on Meta AI glasses, showing how a first-person field of view enables new or better interactions. Clearly state the problem and audience. Deliver a functional prototype and a deck. Display and audio-first experiences count equally, as do web apps and Device Access Toolkit (DAT) mobile integrations. The prototype should handle permissions, errors, performance trade-offs, connectivity and device state changes, and show a plausible path to adoption or a pilot. Interactions must be intuitive and inclusive for all abilities, with appropriate consent and safe data practices.
- **Judging (25% each):** Creativity and use case; Technical execution; Real-world value and feasibility; User experience: input, accessibility and trust.
- **Required tech / constraints:** Meta AI glasses (shared devices, see Hardware section: contested, time-limited loans).
- **Resources:** 10 × Meta Ray-Ban Display and 10 × RBM Gen 2 for use during the hackathon; charging and hygiene materials; developer support at the Meta booth.
- **Mentors:** Amanda Le (challenge mentor and point of contact; Product Marketing, DAT Android). Ming Lin, William La, Amy Lee, Odil Nikadambaev (Software Engineers, Web Apps). Dennis Punjabi (Software Engineer, DAT iOS).
- **Link:** https://hackjunction.app/participate/45/challenges/342

#### Stop Simulating, Start Moving: See It. Detect It. Act on It. The Intel Physical AI Challenge (id 330)
- **Partner:** Ignite Next x Intel
- **Prizes:** 1st €5,000, 2nd €3,000, 3rd €2,000.
- **Problem:** Factories still inspect parts by eye because programming robots takes specialist effort. Physical AI lets a robot learn a policy from a few dozen demonstrations.
- **Build:** Teleoperate an SO-101 arm to record demonstrations, fine-tune a vision-language-action (VLA) policy in Physical AI Studio on cloud GPUs, and train an Anomalib model to tell good Duplo bricks from defective ones (you mark the defects). Combine both: the arm picks each brick, shows it to the inspection camera and drops it into a "good" or "defective" bowl fully autonomously, with models optimised with OpenVINO running on the laptop's CPU, GPU and NPU. Early finishers: faster cycles, messier piles, new defect types, own twist.
- **Insight:** How close can a small low-cost setup get to a reliable inspection cell: how few demos are enough, how the policy copes with new brick positions, how fast the loop runs on CPU/GPU/NPU. Ideas: use the anomaly score to trigger a re-grasp; share cameras between policy and inspection; quantise with OpenVINO.
- **Judging:** Task success 30% (accuracy, cycle time, robustness to shifted/cluttered bricks); Intel technology integration 30% (OpenVINO Physical AI and Robotics AI Suite deployment, offloading to NPU and iGPU); Dataset and pipeline quality 20% (clean teleop data, fine-tuning in Physical AI Studio); System efficiency 20% (inference latency, thermal headroom, power on Core Ultra).
- **Required tech / constraints:** Provided station and Intel stack. Read and accept the Challenge Terms: https://drive.google.com/file/d/1nKs-e-4FNk-AoMq1fCeRKM_6mpIkArRt/view?usp=sharing
- **Resources:** 25 stations, one per team, in the Junction Hardware Lab, each with an Intel Core Ultra Series 3 (Panther Lake) laptop with 64 GB RAM; SO-101 follower arm with wrist camera and leader arm; two external cameras (top view, inspection), at least one RealSense D415 depth camera; Duplo bricks, bowls, markers; cloud GPU instances; Physical AI Studio; Anomalib, OpenVINO, OpenVINO Physical AI; hands-on technical session Sat 12:00.
- **Mentors:** 3–5 Intel robotics and edge AI engineers (Physical AI Studio, OpenVINO, Anomalib) on site every day, supported by Ignite Next.
- **Main contact:** Marvin Müller, Strategic Partnerships & Value Creation Lead, Ignite Next (contact on platform).
- **Link:** https://hackjunction.app/participate/45/challenges/330

#### The Robot Teleoperation Challenge (id 326)
- **Partner:** Rokoko
- **Prizes:** 1st: 1 pair Smartgloves II + 1 SDK licence + featured post on Rokoko's blog + extended support (valued €4,990). 2nd: 1 Smartsuit Pro II (valued €2,295). 3rd: 1 pair Smartgloves I (1st gen) + Rokoko merch (valued €1,095).
- **Problem:** Teaching robots to interact with the physical world is hard; human teleoperation controls robots and collects training data.
- **Build:** An impressive teleoperation application using Rokoko mocap to control robotic hands, arms or humanoids, physically or in simulation. Open-ended; can combine with other hardware and challenges at the event.
- **Interests:** precise manipulation (fragile objects, tools, liquids); collecting human demos to train autonomous policies; creative or entertainment uses.
- **Judging:** Technical execution 35%; Originality and creativity 25%; Usefulness and potential impact 25%; Demonstration of human-controlled robotics 15%.
- **Required tech / constraints:** Rokoko motion capture.
- **Resources:** Smartgloves II, Smartsuit Pro II, Coil Pro, Rokoko Device SDK; access to a Unitree G1 with dexterous hands (coordinated with the humanoid challenge team); possibly a Booster T1; Aalto Robotics Club's Inspire robotic hand integration. Access: create a Rokoko ID → submit email and ID via the form (https://docs.google.com/forms/d/e/1FAIpQLSdCZTfoFzWbZS8fuvpKjhhP8xvOAX_vhJhTKYMpuRB8JMIHIQ/viewform) → get accepted → activate SDK licence per the SDK page.
- **Mentors:** Victoria Stein (Rokoko, on site); Aalto Robotics Club mentors trained on Rokoko tech.
- **Link:** https://hackjunction.app/participate/45/challenges/326 · https://www.rokoko.com/

#### Aaltonomous Humanoid (id 320)
- **Partner:** Aalto University
- **Prizes:** Winning team 2,000€ + a visit to the Aalto robotics lab. Top ~5 teams (by simulation performance) run their solution live on the real Unitree G1.
- **Problem:** Moravec's paradox: the G1 "Väiski" can backflip but cannot sort blocks.
- **Task:** Make the G1 sort objects into boxes autonomously. Legs and waist held stiff; two 7-DoF arms and two Dex3 three-fingered hands. 3–5 printed objects (cubes, cylinders, triangular prisms, ~4.5 cm, red/yellow/blue) at random positions and angles. Three identical unmarked orange boxes (21 cm wide), fixed left/centre/right, 5 cm apart, 40 cm from the torso. Every object into the right box within 2 minutes.
  - Fixed sorting: red → left, yellow → centre, blue → right.
  - Sort by instruction: a text instruction sets the mapping, with unseen phrasings.
  - Stretch: put each object through the matching hole in a lid on one box.
  - Policy inputs: head camera (colour + depth), both wrist cameras, joint states, instruction. Output: target positions for all arm and finger joints at 30 Hz.
- **How it works:** Simulation first in a ready-made Isaac Sim scene, with Verda GPU. Real-robot datasets published on Hugging Face during the event (links in Junction Discord). Submit a Docker image running a small policy server; the runner sends commands through a safety filter. Finals: evaluated in simulation on an unseen scene variant; finalists run on the real robot Sunday; best real-robot score wins.
- **Directions:** CV + classic programming, VLM/LLM planner calling skills, imitation learning or VLA fine-tuning (LeRobot, π0, GR00T), RL in Isaac Lab, sim-to-real matching, combinations. They want robustness to sim/real mismatch, generality beyond one setup, and doing a lot with little real data.
- **Judging:** Real-world result 40% (how well it works on the real robot); Generality 25%; Originality 20%; Presentation 15%.
- **Required tech / constraints:** Docker image policy server. To run on the real robot it must pass the sim safety check: no crashes or safety stops, no commands over joint and speed limits, at least 27 commands per second. Teams never control the robot directly. GPU: RTX-class, ≥24 GB (RTX Pro 6000, L40S, A6000, RTX 4090/5090); ray-traced cameras will not render on A100 or H100 (fine for training). Use on-demand, not spot, instances and a persistent volume.
- **Resources:** Starter repo https://github.com/zupermiez/aaltonomous-humanoid (guide: aaltonomous/cloud/QUICKSTART.md; rules and submission: aaltonomous/docs/participants/). Sim Docker image `aalto-sim-v1.tar.zst` (download location shared at kickoff); commands `aalto sim` (first start 5–10 min), `aalto check` (expect 8 PASS / 0 FAIL), `aalto baseline`, `aalto eval --policy ws://localhost:8000`. No Docker: `bash aaltonomous/cloud/setup_instance.sh` (~30–40 min, no sudo). Policy template in aaltonomous/deploy/; package with aaltonomous/docker/submission.Dockerfile. Starter code includes robot interface, safety filter, classical baseline, policy-server and Dockerfile templates, sim evaluator. Verda compute. ~30 Aalto Robotics Club volunteers.
- **Mentors:** Erkka Lehtonen and Viktor Solianoi, on site all event. Questions via Junction Discord.
- **Link:** https://hackjunction.app/participate/45/challenges/320 · https://aalto.fi/

### FinTech Track (2)

#### Make Unicorns Real (id 350)
- **Partner:** Cala
- **Prizes:** 1st: each member becomes a "Cala Comet" (~€5,000 for a team of four): for three months, one hackathon of their choice per month with travel and accommodation covered by Cala; plus €1,000 Cala credits and merch. Runner-up: 500€ per list page / "€500 in Cala credits" per brief, plus merch.
- **Problem:** Founders and investors decide on scattered, stale information; agents searching the web hit messy, disconnected data.
- **Build:** A product on Cala's structured, sourced data (companies, people, funding rounds, investors and their connections) that solves one real need for founders, investors or both. Focus beats breadth. Aim for something usable at Slush, which starts right after.
- **Starting points:** finding lead investors still active in your space; reading a market (competitors, who raised from whom, funding flow); spotting promising young companies or quick sourced background checks; finding first customers among newly funded companies, market sizing, mapping acquirers.
- **Judging (25% each):** Real need; Execution (works end to end); Originality; Use of Cala (core, not an add-on).
- **Required tech / constraints:** Cala API or MCP must be core.
- **Resources:** Credits for every team. Docs: docs.cala.ai. Redeem promo code (on platform) at console.cala.ai → Billing → Extra credits → Add credits → Add promo code (no payment details). Workshop "Tips & tricks to Make Unicorns Real", Sat 11:00.
- **Mentors:** Issey Masuda (co-founder and CTO) plus Cala engineers (knowledge graphs, data pipelines, LLM agents, MCP).
- **Main contact:** Elies Delgado (Community Growth), (email on platform)
- **Link:** https://hackjunction.app/participate/45/challenges/350 · https://www.cala.ai/

#### Personal Economic Trainer (id 311)
- **Partner:** S-Pankki (S-Bank)
- **Prizes:** 1st 2000€, 2nd 1000€, 3rd 500€, all as Airbnb gift cards.
- **Problem:** Banking stops at statements and transaction lists. S-Bank (3.5M customers; S-mobiili used weekly by 1 in 3 Finnish adults) wants conversational, personalised finance. No Finnish bank yet lets customers chat with their own data.
- **Build:** An AI experience on a large synthetic transaction dataset that lets people chat with their money, from "How much did I spend on taxis last month?" to "What kind of spender am I?", "What is safe for me to spend this week?", "How much could I save if I reduced dining out by 20%?". Pedagogical angle valued: three baskets (mandatory regular, e.g. rent; mandatory irregular, e.g. broken washing machine; everyday leakage, e.g. coffees). MyData spirit: free exploration over fixed charts. Open data benchmarks (e.g. Statistics Finland) encouraged, not mandatory. Interest in plain-language explanations, what-if simulation, safe-to-spend and safe-to-save guidance.
- **Optional bonus:** PSD2 multi-bank view.
- **Judging (20% each):** Impact on financial literacy (incl. pedagogical angle); Originality of AI integration; Clarity of the mobile user experience; Feasibility; Potential to integrate into S-mobiili.
- **Required tech / constraints:** Provided synthetic dataset. Recommended output: mobile app or web app embeddable in a mobile app.
- **Resources:** Data at https://github.com/hackjunction/Junction-2026-S-pankki
- **Mentors:** Carl-Edvard (Calle) Holmberg, Chief Innovation Officer (main contact); an S-Bank IT/AI development representative; a transaction-data data scientist; 1–2 business representatives.
- **Link:** https://hackjunction.app/participate/45/challenges/311 · https://www.s-pankki.fi/

### Healthcare Track (2)

#### Equal Care Across Finland (id 344)
- **Partner:** AstraZeneca
- **Prizes:** Best overall 1000€, 2nd 750€, 3rd 250€.
- **Problem:** Ensure time to diagnosis is optimal and cancer patients start treatment within target timeframes wherever they live in Finland. Known bottlenecks: late detection; primary-to-specialist referral; diagnosis-to-treatment time. Data is limited and closing the data gap is part of the challenge.
- **Build:** An AI-powered system that (1) identifies the gap in access or outcomes, (2) locates where in the pathway it emerges (detection, referral, diagnosis, treatment initiation), and (3) recommends concrete, evidence-based improvements at national or account level. Recommendations are the most important part. Formats: AI analyst explaining indicator trends, monitoring dashboard, early-warning system, intervention simulation. A non-technical decision-maker should get it in under two minutes.
- **Minimum requirements:** reliable evidence from public data and/or AstraZeneca mentor insights with sources for every claim; cover at least one indicator tied to Goal 3 of the national cancer strategy; actionable recommendations; a working demo (slides alone not enough).
- **Judging:** Actionability 30%; Insight 25%; Data quality and transparency 20%; Execution 15% (works live in front of judges); Clarity 10% (key message within two minutes).
- **Required tech / constraints:** Public, aggregate data only; no patient-level data.
- **Resources:** Key insights at the AstraZeneca stand Fri 20:00. Background pack / national cancer strategy 2026–2035 (Finnish): https://files.hackjunction.app/resources/Kansallinen_syopastrategia_2026_2035_FINAL.pdf · Implementation roadmap 2026–2031 (Finnish): https://files.hackjunction.app/resources/Kansallinen_syopastrategia_toimeenpanon_tiekartta_2026_2031.pdf · Source list: https://files.hackjunction.app/resources/Sy%C3%B6p%C3%A4strategiat%20ja%20sy%C3%B6p%C3%A4data_linkkikokoelma.pdf · Finnish Cancer Registry and THL regional health indicators.
- **Beyond Junction:** Possible follow-up project with a Finnish wellbeing services county.
- **Mentors:** Fri 13 Nov from 18:00: Hanna Rusila (Marketing), Hanna Toivola (Diagnostics), Kaisa Kaitila (Medical Affairs), Laura Aaltonen (Marketing), Joanna Tuormaa (Business Excellence). Sat 14 Nov daytime: Kaisa Kaitila. Sun 15 Nov 14:00 judging: Hanna Rusila, Laura Aaltonen, Joanna Tuormaa.
- **Contacts:** Main: Joanna Tuormaa, Innovation and Business Excellence Director, Nordics. Questions: Laura Aaltonen, (phone on platform).
- **Link:** https://hackjunction.app/participate/45/challenges/344

#### Beyond the Clinic (id 343)
- **Partner:** Aalto University
- **Prizes:** To be announced.
- **Problem:** TMS treats severe depression in clinics with daily visits, but depression can return. No good home maintenance treatment exists. Home lacks fMRI/MEG/EEG, blood tests and psychiatrists.
- **Build:** A product that helps people stay well at home after depression treatment, ideally closed-loop: sense how someone is doing, respond with something that helps, learn what works for that person. A laptop and phone are enough.
- **Audiences:** people after TMS; anyone at risk of depression; clinicians tracking patients between visits.
- **Interventions:** sensory stimulation (music, rhythmic lights, colours, touch, smell, taste); social interaction, meditation, yoga, exercise; forest/sea visits or VR; games (e.g. Soihtu, https://soihtudtx.com/).
- **Sensing:** phone (sound, voice, acceleration, facial expressions, sleep, routines); wearables like smart rings (HRV, sleep, activity, autonomic changes).
- **Product directions:** everyday companion; adaptive sensory experience; daily game; smart home light/sound; social peer support; clinician view. Inspiration: Meru Health (https://meruhealth.com/).
- **Judging (25% each):** Usefulness; Ease of use (would someone recovering use it daily?); Smart sensing (clever use of home measurement, learns per person); Creativity.
- **Required tech / constraints:** Not stated.
- **Resources:** Pointers to published studies and open datasets; expert mentors. Subject to lab confirmation: live TMS demo; portable EEG demo at the booth.
- **Mentors:** Researchers from Prof. Risto Ilmoniemi and Prof. Pantelis Lioumis' group (Neuroscience and Biomedical Engineering), plus Aalto Innovation. Main contact: Myungji (MJ) Suh.
- **Link:** https://hackjunction.app/participate/45/challenges/343 · https://aalto.fi/

### AI Infrastructure Track by Verda (1)

#### Make Blueprints Talk (id 335)
- **Partner:** Stoa
- **Prizes:** Best overall 1000€ + work trial at Stoa, 2nd 750€, 3rd 250€.
- **Problem:** Site engineers spend hours a day searching drawings; general AI models fail on complex technical drawings.
- **Build:** A program that answers natural-language questions about construction drawings and building information models, correctly, showing where in the drawing the answer came from so a human can verify in seconds. Preference for approaches next year's frontier models won't make obsolete, e.g. hybrids of frontier models, computer vision, 3D, geometry or small fine-tuned models.
- **Judging (25% each):** Accuracy of answers; How well it visualises reasoning for human verification; Creativity; Low inference cost.
- **Required tech / constraints:** Use the provided dataset (real drawings, many formats and languages, with example questions).
- **Resources:** Preview (0.5 GB): https://fwjydgxpttajiqpfmqtj.supabase.co/storage/v1/object/public/stoa-junction-2026/junction-dataset-preview.zip · Full (10 GB): https://fwjydgxpttajiqpfmqtj.supabase.co/storage/v1/object/public/stoa-junction-2026/junction-dataset.zip
- **Mentors:** Stoa's founding tech team plus a construction engineer. No names stated.
- **Link:** https://hackjunction.app/participate/45/challenges/335 · https://stoabuild.com/
- Note: listed under "AI Infrastructure Track By Verda"; the brief itself does not mention Verda.

### Data Track (3)

#### The Web Is Your Real-Time Database (id 332)
- **Partner:** Context.dev
- **Prizes:** 1st €2,000 + swag, 2nd €500 + swag, 3rd swag.
- **Problem:** Software runs on stale data; analysts copy-paste prices and check sites by hand; fact-checkers can't keep up.
- **Build:** A product that turns live web data into decisions, actions or experiences that weren't possible before. Inspiration: GPU Rental Prices (https://gpurentalprices.com/), Yapper Leaderboard, cve.now, Ferndesk. Themes: Scrape the Economy; The Web, Watched (agents triggered by changes); Brand in a Box (apps that brand themselves from a sign-up email); Truth at Internet Speed (fact-checking with sources). Wild ideas welcome.
- **Judging (20% each):** Real-world impact; Creative use of live web data; Completeness of demo (production readiness); Technical execution (latency and accuracy); Real-timeness (reacts to change vs one-off snapshot).
- **Required tech / constraints:** Context.dev (not stated as mandatory, but judging centres on it).
- **Resources:** 50,000 free non-expiring API credits per team: sign up at https://context.dev/signup, redeem code (on platform) at https://context.dev/dashboard/redeem-credits. Quickstart https://docs.context.dev/quickstart, docs https://docs.context.dev/. Up to 50 concurrent requests per team. Capabilities: search, scrape (markdown, HTML, screenshots, images), crawl, URL mapping, structured extraction, research answers; brand data, company/people search and enrichment, NAICS/SIC; news search, monitors with webhooks; batch API, PDF/document parsing.
- **Mentors:** Beer van der Drift (CTO, main contact, (email on platform)), Yahia Bakour (Founder and CEO), Thomas Oomens (Engineer). On site Fri until 23:00, Sat 09:00 to Sun 02:00, Sun 07:00 to end.
- **Link:** https://hackjunction.app/participate/45/challenges/332

#### Rethinking Recruitment (id 319)
- **Partner:** City of Espoo
- **Prizes:** Best overall 1500€ + chance to present to Espoo's business development and innovation leaders and the national network of cities on talent attraction. 2nd 1000€, 3rd 500€. Runner-ups get Espoo swag bags, features on city channels, and a presentation to the cities of Helsinki and Vantaa.
- **Problem:** At Espoo's online, in-person and hybrid matchmaking events, companies describe needs late and poorly, talent struggles to express strengths, CVs and screening are increasingly AI-generated, organisers can't assess real capabilities (especially tech skills), companies get swamped with irrelevant approaches, platforms are cumbersome and crash at event start, and international recruitment adds compliance, language, culture, relocation and onboarding complexity. Companies doubt a free public-sector service has suitable candidates.
- **Build:** Prototype new ways to help companies and talent find relevant, efficient connections at any stage: registration, during the event, follow-up, or end to end. More signal, less noise. Avoid reinforcing bias by nationality, language, education, career path or other unrelated traits.
- **Judging:** Impact and Relevance 45%; Innovation and User Experience 35%; Responsible and Feasible Execution 20%.
- **Required tech / constraints:** Any tech. Synthetic data. No automated profiling or automated decisions about individuals without human involvement. Minimise personal data and show EU AI Act-compliant privacy.
- **Resources:** Subject-matter experts; example scenarios and user journeys from real events; feedback on concepts; guidance on responsible AI and privacy. Suggested sources: Duunitori, The Hub, Work in Finland open jobs, Job Market Finland; Tavata, Brella; ESCO; National Forum for Skills Anticipation (PDF on tem.fi); Suomi.fi PTV Open API; Business Espoo (https://www.businessespoo.com/).
- **Mentors:** Espoo International Working Life Services and Business Services teams, on site and on Discord. Main contact: Melissa Arni-Hardén, Client relations manager and International Working Life Services team lead.
- **Link:** https://hackjunction.app/participate/45/challenges/319 · https://www.espoo.fi/

#### Wikipedia Through Time. (id 307)
- **Partner:** MariaDB
- **Prizes:** 1st €1,000 cash + €1,000 UpCloud credits + MariaDB certification for every member (5 vouchers at learn.mariadb.com, value 750 USD). 2nd €500. 3rd €250. All winners credited in a blog on mariadb.org.
- **Problem:** Wikipedia search is keyword-based and its full edit history is rarely explored.
- **Build:** A Wikipedia tool that doesn't exist yet, or is badly underused, with MariaDB at the core. Tracks: RAG (recommended; MariaDB native vector search for grounded, source-cited Q&A, e.g. history of Finland research assistant); SVT (advanced; system-versioned tables for point-in-time views, edit wars, how a story was rewritten); Both (e.g. "what did Wikipedia say about this in 2015, and what changed?"). User groups: readers and/or editors. Ideas: source-grounded Q&A, fact-checking, coverage gap detection, cross-language comparison, time-travel views, change visualisations, edit-war or bias detection, edit analytics.
- **Judging (20% each):** Effective and creative use of MariaDB (RAG and/or SVT); Implementation (execution and scalability across the provided datasets); Usefulness for readers or editors; Design and demo quality; Originality. Bonus (0% weight) recognition for SVT or combined tracks.
- **Required tech / constraints:** MariaDB at the core. Source articles are Finnish; a multilingual embedding model is recommended for RAG (no Finnish skills needed). Any LLM, embedding model or frontend.
- **Resources:** MariaDB Server with vector search; system-versioned tables; small, medium and large Finnish Wikipedia (history of Finland) datasets. Repos: https://github.com/MariaDB/mariadb-wikipedia-datasets · https://github.com/MariaDB/mariadb-vector-wikipedia-rag · https://github.com/MariaDB/mariadb-system-versioning-wikipedia (note: the platform hyperlink for this one points to the vector-RAG repo).
- **Mentors:** Kaj Arnö (MariaDB Foundation, Executive Chairman), Robert Silén (MariaDB Foundation, AI Lead).
- **Link:** https://hackjunction.app/participate/45/challenges/307 · https://mariadb.org/

---

## 3. Tech challenges and side prizes

The Challenges page has a "Tech Challenges" tab, but its contents were not in the scrape. What the scraped pages say about side prizes:

| Side prize / tech challenge | Source | What it says |
|---|---|---|
| Best use of Modal | Developer Tools (Modal) | "Best use of Modal is a tech challenge": entered on top of your main challenge by using Modal to power the project. The same project can enter other tech challenges too. Prize not stated. |
| Cloudinary challenge | Developer Tools (Cloudinary) | Use the tools listed at https://cld.media/hackathons. To submit, fill in https://cld.media/hackathon-survey. Prize not stated. |
| MariaDB open award | Developer Tools (MariaDB) | Open to every team in any challenge: most interesting use of the database itself (neat schema, surprising query, a feature used well). Show at the booth or mention MariaDB in the submission; work published and credited on mariadb.org. |
| Exa participation | Challenge 298 | Every Junction participant gets $50 Exa credits. |
| Arduino Project Hub | Challenge 356 | Publishing on Project Hub with tag "Junction Finland 2026" is required for Arduino prizes. |
| Meta AI forum | Challenge 342 | Best submissions may be invited to Meta's AI forum, Wed 18 Nov 2026. |

The scrape mentions no NVIDIA Nemotron challenge. A Verda-branded track exists ("AI Infrastructure Track By Verda", containing only Stoa), and Verda gives €200 credits (below). Gemini appears only as API credits, with no Gemini prize.

---

## 4. Developer Tools and Assets (full list)

| Provider | Offer | How to access |
|---|---|---|
| Verda | €200 credits for AI compute (GPU) and inference API, "to solve any challenge" | Sign up to the Verda Console → claim credits via the form on the hackerpack page → redeem and share with team per Verda docs. https://hackjunction.app/participate/45/hackerpacks/71 |
| OpenAI | $100 Codex credits per participant (prototype apps, build agents, speed up development) | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/70. Redemption steps not stated. |
| MariaDB | MariaDB database, open to every team; credit on mariadb.org (see side prizes) | Booth, or mention MariaDB in submission. https://hackjunction.app/participate/45/hackerpacks/69 |
| Google DeepMind | Gemini API credits for eligible participants | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/68. Eligibility and redemption not stated. |
| Anthropic | $20 Claude API credits per participant | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/67. Redemption not stated. |
| Aiven | $50 free credits on sign-up; docs; runtime templates for open-source frameworks; mentors on site all days | Sign up to Aiven. https://hackjunction.app/participate/45/hackerpacks/66 |
| Arduino | Arduino UNO Q (2 GB RAM, 16 GB eMMC), USB-C cable, USB-C hub (8-in-1), 45 W USB-C PSU, USB camera, Modulino Buzzer, Knob, Thermo; Arduino App Lab software; usable for any challenge | Borrow from Arduino Hardware Lab, 5th floor (Arduino booth); booking at https://2026.hackjunction.com/hardware. Bring a laptop with Arduino App Lab (https://www.arduino.cc/en/software/#app-lab-section). |
| CRACI | Free platform access + €1000 credits per team for CI/CD or any compute; GitHub Actions-compatible runners (`runs-on: craci`, default 2 vCPU / 6 GB, `cracicorp/setup@v1` size 1–32 units of 1 vCPU + 3 GB); CycloneDX SBOMs; AI vulnerability fixes; API (SBOMs, OCI/cache provenance, network traces, job logs, compute usage); 5 mentors | Invite code from #craci on Discord or the CRACI booth (3rd floor, next to the stage). One person per team: sign up at platform.craci.com → create org + invite code → Settings → Builds → Install GitHub → push a workflow. API token under Settings → API tokens; API https://api.craci.com, spec api.craci.com/openapi.json. Docs https://docs.craci.com/, migration skill https://docs.craci.com/skills/craci/SKILL.md |
| Cloudinary | Image and video API (upload, transform, optimise, deliver; AI media features), generous free tier | Tools: https://cld.media/hackathons. Challenge submission form: https://cld.media/hackathon-survey |
| Modal | $100 credits per participant for CPUs/GPUs (T4, L4, A10, L40S, A100 40/80 GB, RTX PRO 6000, H100, H200, B200, B300); Python SDK/CLI, JS and Go SDKs for Sandboxes; web endpoints; Volumes, Dicts, Queues; Modal Dojo for fine-tuning/RL; starter kit (vLLM/SGLang serving, STT, TTS, vision, RAG, agents, RL); mentors | `pip install modal`. Kick-off workshop at the Modal booth (time on Discord). Redemption steps not stated. Best-use-of-Modal tech challenge. https://hackjunction.app/participate/45/hackerpacks/62 |
| Oxylabs | Web API with /search and /scrape (Markdown, HTML, JSON, screenshots); MCP server and agent skills | Code (on platform) gives a full first-month discount on the $500 Flexible plan. **Credit card required; cancel the subscription after use to avoid monthly charges.** |
| Context.dev | 50,000 non-expiring API credits per team; SDKs for TS/Node, Python, Ruby, Go; MCP server; 50 concurrent requests; no credit card | Sign up at https://context.dev/signup, redeem code (on platform) at https://context.dev/dashboard/redeem-credits |
| IronShard | AI-native S3-compatible object storage with MCP; zero-copy bucket forking; challenge datasets preloaded in read-only buckets where applicable; store large artifacts (> GitHub's 100 MiB/file limit) and reference bucket/object in submission; judges get read access | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/59. Sign-up steps not stated. |
| Junction | Hardware Lab | 5th floor (see section 5) |
| Wendy | Open-source tool to deploy apps to Jetson, Raspberry Pi, ESP32, Arduino with `wendy run`; Python, Swift, Rust, ROS; simulator if no hardware | Find the Wendy team at Junction. |
| Qualia | Robot learning data platform: upload SO-101 or Rokoko recordings, auto quality checks for failed takes/timing/inconsistency, curate versioned datasets, export for training (e.g. pi0.5 with LeRobot) | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/53. Access steps not stated. |
| Featherless | Bare-metal GPU credits for selected teams (fine-tuning, embeddings, GPU-heavy work) | Selection process not stated. https://hackjunction.app/participate/45/hackerpacks/52 |
| Featherless | $50 API credits for open-weight model catalog | Dedicated Junction coupon (on platform). https://hackjunction.app/participate/45/hackerpacks/51 |
| Scailab | Scaipipe: annotate images, generate labelled synthetic data from 3D scenes, train/evaluate detection, segmentation, tracking; browser-based (no GPU needed); built-in MCP server | Hackerpack page https://hackjunction.app/participate/45/hackerpacks/50. Access steps not stated. |
| Exa | $50 credits per participant; full Search and Contents APIs, Websets, Monitors, hosted MCP, Python/JS SDKs | Promo code (on platform), redeem at https://dashboard.exa.ai/billing |

Challenge-specific credits and access (in the briefs, not the Tools tab): Hostinger VPS + AI Router credits + AI Builder (357); AfterQuery frontier model credits + Harbor/OpenCode harness (328); Valio Aimo mock APIs and resource portal (327, password and key on platform); Cala credits (350, promo code on platform); Intel cloud GPUs + stations (330); Verda GPU for Aalto humanoid sim (320); Rokoko SDK licence via form (326); Bahn Spread event code (349, on platform); Tieto partner model credits on the Junction Platform (351).

---

## 5. Hardware lending (snapshot Fri 13 Nov 19:52)

Source: https://2026.hackjunction.com/hardware ("Last updated Fri 19:51 · Checked 19:52:19"). 192 items free across 7 types.

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
Speak to a volunteer at the hardware desk to queue a print. The workflow may change; times are estimates. The waiting queue was empty at snapshot.

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

11 of 13 printers free, 2 out of service.

### Borrowing process
From the hardware page:
1. **Choose hardware**: browse availability, sign in with your Junction account at https://2026.hackjunction.com/hardware, and pick a **first and second choice** (max 2 items, in priority order).
2. **Send one request per team.** A request does not reserve stock. A volunteer confirms your equipment at the desk.
3. **Collect, build, return**: go to the desk with your **team name and photo ID**, and return equipment to a volunteer when done.

From the challenge pages and Developer Tools tab: pickup is at the **Arduino Hardware Lab, 5th floor**.

From the task brief (not on the scraped page): the photo ID is the responsible person's, and the team needs its **table number** to request. Our table number was "Not set yet" in the event guide, so set it before requesting.

Loan limits matter for the glasses: Display glasses come back after 120 minutes and GEN2 after 240 minutes, and 22 teams were already queued for the Display at 19:52.
