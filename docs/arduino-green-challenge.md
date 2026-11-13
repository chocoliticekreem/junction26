# Deep Dive: The Green European Renaissance (Arduino)

Team focus for Junction 2026. Sources: the platform brief (challenge 356), the "Best use of Arduino UNO Q" tech challenge (45), the Developer Tools tab, the hardware lab site, and Discord, all scraped Fri 13 Nov 2026.

## The brief (full)

**Tagline:** Make Europe Green through Edge AI using Arduino.

**Introduction (Arduino's words):** "Do you feel the world is moving to a Cyberpunk dystopian future where Europe is just the place where rich people drink Spritz? Let's change that! If you like LEDs but not megacorp tech corporations, I have a challenge for you! Let's use Edge AI and Arduino UNO Q to do the Green Renaissance of Europe!"

**The challenge:** AI and LLMs are reshaping how we work and solve problems, and Physical AI will soon run in every small appliance. America and Asia are taking the lead, and their big companies will control these tools. That isn't inevitable. With edge AI devices like the UNO Q, Europe can build **local solutions to local problems that don't depend on governments or private companies**. Many of these problems have a large environmental impact, which is the chance to build, step by step, "a Greener, high-technological and human Europe."

**What they're looking for:** solutions that use **Edge AI and the Arduino UNO Q to build Physical AI for local problems**, improving people's lives while creating a greener environment to live and work in.

**Example directions (from the brief):**
- boosting local flora and fauna
- saving energy and improving energy efficiency
- supporting elderly people's independence
- reducing industrial impact
- tackling climate change
- cutting pollution
- making cities more livable and human

## Judging

| Criterion | Weight | What it means |
|---|---|---|
| Technical Implementation & Edge AI | **30%** | How well the UNO Q, the sensors and **on-device AI** are used |
| Environmental & Social Impact | **30%** | How much it improves the environment and people's lives |
| Creativity & Innovation | 20% | Originality of the idea and the approach |
| Working Prototype & Demo | 20% | A functioning **physical** prototype |

What follows from this: 50% of the score is about the physical device actually running AI on the board. Cloud-only AI scores badly. Impact is the other 30%, so put a number on it (kWh saved, waste diverted, CO₂ avoided, people helped).

## Prizes

| Place | Prize (per team member) |
|---|---|
| 1st | **Arduino VENTUNO Q**: Qualcomm Dragonwing IQ8 octa-core SoC + STM32H5 MCU, 40 TOPS NPU, 16 GB RAM, ROS 2. Pre-order price about $299 each |
| 2nd | UNO Q 4G + Plug and Make Kit |
| 3rd | Plug and Make Kit |

## Eligibility: two submissions

1. **Junction Platform**, where peer review and judging happen. Final deadline **Sun 10:00**. The preliminary draft is due **Fri 23:55**, and challenge registration opens at **midnight**.
2. **Arduino Project Hub.** Without this you can't win.
   - Log in at https://projecthub.arduino.cc/
   - Click **+ NEW PROJECT**
   - Select the tag **Junction Finland 2026**
   - Fill in the required parts

## Hardware: what the kit actually has

From the hardware lab ("Arduino dev kit", no time limit, borrowed with a photo ID deposit):

| Item | Use |
|---|---|
| Arduino UNO Q (2 GB RAM, 16 GB eMMC) | Linux (Debian) on a Qualcomm Dragonwing QRB2210 + a real-time MCU. Runs App Lab apps, Python and containerised AI models |
| USB camera | Vision: detection and classification |
| Modulino Thermo | Temperature and humidity |
| Modulino Knob | Input |
| Modulino Buzzer | Audio output |
| USB-C hub (8-in-1), 45 W PSU, cable | Power and peripherals |

**Missing: actuators (motors, servos, relays) and other sensors** (air quality, light, distance, microphone). Options:
- Use the board's onboard LED matrix and the buzzer as outputs.
- Ask at the Arduino booth or desk for extra Modulinos. The brief mentions "a variety of Modulino sensors".
- 3D-print enclosures and mounts: DM the STL, table number and team name to Printing Personnel on Discord.
- Bringing your own hardware is allowed (organizer answer).

## Software: Arduino App Lab

- Install App Lab before building: https://www.arduino.cc/en/software/#app-lab-section (the Arduino team's own tip).
- App Lab combines Arduino sketches, Python scripts and containerised AI models into one app.
- **Bricks** are plug-and-play modules that add AI models, web servers or API clients.
- **Preloaded on-device models:** object and person detection, face detection, image classification, anomaly detection, sound recognition and keyword spotting.
- **Custom models:** Edge Impulse supports deploying trained models to App Lab on the UNO Q.
- Help: Arduino mentors at the Hardware Lab (5th floor) and on Discord.

## Stack these on the same project

| Side challenge | Prize | Why it fits | Extra step |
|---|---|---|---|
| **Best use of Arduino UNO Q** | UNO Q + Plug and Make Kit per member | Same hardware. Judging: Arduino hardware & edge AI 50%, working prototype 30%, creativity 20% | Same Project Hub post |
| Best Use of Gemma (Google DeepMind) | €1,000 to each of 3 teams | Gemma is Google's open on-device model family. Check what fits in 2 GB, or run it on a laptop at the edge | See the challenges doc |
| Best Use of Gemini API | €4,000 + $1k GCP per member / €2k / €1k | A cloud companion such as a dashboard, reports or a voice interface. Keep the core AI on the board for Arduino's score | 18+ only |
| Best use of Modal | $2,000 + $3,000 credits | Train a custom model on Modal GPUs, then deploy it to the board | |
| Rokoko Robot Teleoperation (main) | Gloves + SDK (~€4,990) | Only if you also have gloves and something to move | Rokoko SDK licence approval |

Useful free tools from the Developer Tools tab:
- **Wendy:** deploy to Arduino or ESP32 with `wendy run`, with a simulator if you have no hardware.
- **Scailab Scaipipe:** synthetic labelled images for training vision models, in the browser, with an MCP server.
- **Qualia:** curates teleoperation datasets, which pairs with Rokoko.

## Competition snapshot

- Arduino kits: 160 total, 127 free at 20:29 Fri, so roughly 30+ teams have one. Not all of them will enter the Green challenge.
- Many hardware teams on Discord described themselves as beginners. A team that really runs an AI model on the board and has a polished demo will stand out.

## Why edge AI: the test every idea must pass

Edge AI is 30% of the score, and the brief's whole argument is about *not depending* on distant companies and infrastructure. If the same idea works equally well by sending data to a cloud API, the board is decoration and judges will notice. **An idea passes only if at least one of the reasons below makes the cloud impossible, illegal or clearly worse.**

| Edge advantage | When it makes edge *indispensable* | Evidence |
|---|---|---|
| **Works offline** | No or unreliable connectivity: forests, fields, waterways, archipelago, basements, disaster zones | A cloud model stops working without internet; an edge model doesn't care ([Digital Citizen](https://www.digitalcitizen.life/edge-ai-vs-cloud-ai-when-your-device-handles-tasks-without-internet/)) |
| **Energy and battery life** | Battery or solar devices that would otherwise stream images | On-device CNN inference + sending only the result cut total energy up to **5×** and transmission energy **5–14×**, stretching battery life from weeks to months or years; tiny results also make LoRaWAN/NB-IoT feasible ([Send Less, Save More, arXiv 2510.24829](https://arxiv.org/html/2510.24829v2)). Sending JPEGs for cloud inference cost **524 mJ per inference**, the most of any option measured ([Alif Semiconductor](https://alifsemi.com/its-official-local-ai-inference-at-the-edge-uses-less-power-than-the-cloud/)) |
| **Privacy / GDPR** | Cameras or microphones in homes, offices, schools or public spaces | GDPR applies the moment a person is recognisable. On-device processing that only emits counts or events is the privacy-by-design pattern regulators accept ([asmag](https://www.asmag.com/showpost/35380.aspx), [Fluendo](https://fluendo.com/blog/privacy-preserving-ai-video-surveillance-with-edge-intelligence/)) |
| **Latency** | A physical reaction is needed within milliseconds | Edge under ~50 ms (often under 10 ms) vs cloud at 100–300 ms plus jitter ([Clarifai](https://clarifai.com/blog/edge-vs-cloud-ai)) |
| **Bandwidth and running cost at scale** | Hundreds of devices or continuous video | Sending only insights instead of raw feeds cuts bandwidth, storage and cloud cost ([Coursera](https://coursera.org/articles/edge-ai-vs-cloud-ai)) |
| **Sovereignty** | The brief's own thesis: local solutions not dependent on US/Asian platforms | The device keeps working if an API changes, gets more expensive or disappears. This is a pitch line, not a technical necessity on its own |

**Pitch rule:** name the specific constraint that kills the cloud version, then show the number. For example: "this sits in a forest with no signal, on a battery, for a whole season", or "a camera in a bedroom can never stream to a server."

## Ideas scored against the edge test

| Idea | Kills the cloud version | Edge verdict |
|---|---|---|
| **Remote biodiversity / invasive-species monitor** (birds, pollinators, invasive plants in Finnish forests or waterways) | No connectivity + battery/solar + only a few bytes per detection to send | ✅ **Indispensable** (offline + energy) |
| **Privacy-first occupancy energy saver** (camera counts people per room and cuts heating or lighting in empty rooms; no image leaves the device) | GDPR: you can't stream office or school video to a cloud. Space heating is the biggest share of building energy in cold climates | ✅ **Indispensable** (privacy), plus a clear kWh/CO₂ impact |
| **Elderly fall and anomaly detection at home** | Bedroom or bathroom camera: privacy rules out the cloud; it must also alert when the Wi-Fi is down | ✅ **Indispensable** (privacy + offline). The brief lists elderly independence explicitly |
| Smart recycling bin | Instant feedback and cost at scale help, but a cloud API would also work | ⚠️ Advantageous, not indispensable |
| Food-waste tracker in kitchens | Works just as well with photos sent to the cloud | ❌ Edge is decoration |

## Idea directions that hit every criterion

| Idea | Edge AI on the board | Impact story | Kit fit |
|---|---|---|---|
| **Smart waste sorting bin** | Camera classifies recyclables | Contamination in recycling, a local municipal problem | Camera + LED matrix + buzzer feedback |
| **Building energy watchdog** | Thermo plus a person-detection camera spots heating or lighting empty rooms | kWh and CO₂ saved in offices and schools | Camera + Thermo |
| **Wildlife / pollinator monitor** | Camera identifies birds or insects; sound classification | Local biodiversity data without the cloud | Camera (+ mic, if borrowed) |
| **Elderly independence sensor** | Fall or person detection, with anomaly detection on the room's temperature | Lets older people live at home safely, with privacy since nothing leaves the device | Camera + Thermo + buzzer alert |
| **Food-waste tracker for kitchens** | Camera classifies discarded food | Ties into Valio Aimo's foodservice world | Camera |

## Checklist

- [ ] Kit collected (photo ID deposit at the 5th-floor desk)
- [ ] App Lab installed on every laptop that will develop on the board
- [ ] Idea locked; register for Arduino 356 + Best use of Arduino UNO Q when the form opens at midnight
- [ ] Draft submission on the platform by Fri 23:55
- [ ] On-device model running by Sat noon
- [ ] Impact numbers worked out, with sources
- [ ] Project Hub page published with the tag "Junction Finland 2026"
- [ ] Final platform submission (FINAL, not draft) by Sun 10:00: demo, 2-min video, repo, deck
