# NoHerbs 🌿

**Spot sprayers cost over €100k, so we built one for €98 a nozzle: edge AI on an Arduino UNO Q that sprays the weed and spares the crop.** Built at Junction 2026 for Arduino's Green European Renaissance challenge.

## Why

Spot spraying cuts herbicide use by around half ([John Deere, 59% average in 2024](https://deere.com/en/news/all-news/see-spray-herbicide-savings)), but today it only comes as a whole new machine: an Ecorobotix ARA 6 m costs [€105,000](https://www.futurefarming.com/ecorobotix-ara), and a Greeneye boom about [$239–250k](https://www.farmprogress.com/farming-equipment/greeneye-spray-booms-are-here-but-hard-to-get). 63.8% of the EU's 9.1 million farms are under 5 ha ([Eurostat](https://ec.europa.eu/eurostat/de/web/products-eurostat-news/w/ddn-20230403-2)), so most farms keep spraying the whole field. NoHerbs is the same idea unbundled: one module per nozzle that bolts onto the boom a farm already owns.

| Prototype bill of materials | € |
|---|---|
| Arduino UNO Q (2 GB) | 60 |
| Arduino USB camera | 35 |
| MG90S servo | 3 |
| **Per nozzle (electronics)** | **98** |

A production module with a 12 V solenoid valve and weatherproof housing comes to an estimated €200–230 per nozzle at retail prices, so 6 m of boom costs about €2,600 against €105,000.

## The prototype

NoHerbs is a tabletop prototype of a smart agricultural sprayer that decides, shot by shot, whether it is safe to spot-spray a weed. A camera watches a printed "field" board from above, an on-device AI model detects weeds, and a servo squeezes a spray bottle — but only when the firmware's safety interlocks allow it. The prototype sprays **water only**.

## What I built

- **Trained a custom weed detector** on Edge Impulse (YOLO-Pro object detection, single class `weed`, 320×320 input) using tiled drone photos of weeds in maize from the ImageWeeds dataset (see Credits), and deployed it to run fully on-device on the UNO Q (~250–370 ms per frame, no cloud).
- **Built the Arduino App** (this repo) with the two halves the UNO Q offers:
  - **Linux/MPU side (Python, `python/main.py`)** — runs the camera + AI pipeline via App Lab's `video_object_detection` brick (confidence ≥ 0.4, 1.5 s debounce) and requests a spray over the Router Bridge when a weed is seen.
  - **Microcontroller side (sketch, `sketch/sketch.ino`)** — owns the servo and **all safety rules**. Python can only *ask*; the firmware decides.
- **Built the rig**: UNO Q ("PippaBoard") with a USB webcam fixed overhead, a servo mounted to squeeze a spray-bottle trigger (D9), and a desk fan to simulate wind for the next stage of the demo.

## Safety design

The firmware is deliberately paranoid:

- **Starts disarmed.** `fire` does nothing unless the sketch has been armed via `set_armed`.
- **One shot, then auto-disarm.** Every spray requires a fresh arm.
- **Hardware STOP**: holding pin D2 to GND for 0.3 s disarms and cancels any queued shot.
- **A squeeze, once started, always completes** — the servo ramps 180°→80° over 400 ms and returns, with bit-banged servo pulses so timing is fully under the sketch's control.
- Bridge handlers are registered with `provide_safe`, so they run between `loop()` passes, never mid-squeeze.

## How it works

```
USB webcam → video_object_detection brick (Edge Impulse model, on-device)
          → Python callback on "weed"
          → Router Bridge: set_armed(true), fire()
          → sketch: if armed → queue shot → squeeze servo → auto-disarm
```

> Current demo shortcut: Python arms immediately before each fire so the detection→spray loop can be shown end-to-end. In the target design, arming comes only from the operator (dashboard ARM button).

## Repo layout

```
app.yaml            App manifest: video_object_detection brick + model ei-model-1164455-1
python/main.py      Detection pipeline and Bridge calls
sketch/sketch.ino   Servo control, arming state machine, STOP input
sketch/sketch.yaml  Sketch library pins
docs/               Junction 2026 event notes and challenge research
```

## Running it

Requires an Arduino UNO Q with Arduino App Lab, the app installed on the board, and the Edge Impulse model (`ei-model-1164455-1`) installed. Start the app from App Lab; detections and spray decisions are printed to the app log.

Suggested bring-up order (what I used):

1. Sketch alone — servo should rest at 180°.
2. Bridge test — `set_armed(True)` then `fire()` gives exactly one squeeze; a second `fire()` without re-arming does nothing.
3. Detection → fire with a weed picture in view.
4. Only then add water.

## Status & next steps

Working now: on-device weed detection driving a real, interlocked spray actuation.

Next (designed, not yet implemented):

- **Detection cache:** the Qualcomm side runs the accurate model once per weed; the STM32 tracks the weed from tractor speed and fires the moment it passes under the nozzle, so model latency stops limiting speed (only the camera's look-ahead does).
- Map camera pixels → board centimetres via four corner markers (homography).
- Predict the spray footprint from wind (fan speed/direction) and nozzle mode.
- **Block** any shot whose footprint overlaps a protected plant (unknown plants count as protected); log every decision as ALLOWED/BLOCKED with the reason.
- Operator dashboard with an explicit ARM button.

## Known limits

- The model was trained on drone imagery, not photos of the demo board — it finds roughly 40–45% of weeds (validation mAP@50 ≈ 0.57) and does worse on printed props.
- No Python-side rate limit beyond the 1.5 s detection debounce; the firmware's arm-per-shot rule is the real guard.

## Credits

- Training images: **ImageWeeds** dataset, Rai, N., Villamil Mahecha, M., Christensen, A., Quanbeck, J., Howatt, K., Ostlie, M., Zhang, Y., Sun, X. (2023), North Dakota State University, Mendeley Data, [doi:10.17632/8kjcztbjz2.2](https://doi.org/10.17632/8kjcztbjz2.2), licensed CC BY 4.0.
- Model trained and deployed with Edge Impulse; app built with Arduino App Lab.
