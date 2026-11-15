# SprayGuard 🌿

**Edge-AI spot-spraying safety demo on an Arduino UNO Q — built at Junction 2026 (Arduino green challenge).**

SprayGuard is a tabletop prototype of a smart agricultural sprayer that decides, shot by shot, whether it is safe to spot-spray a weed. A camera watches a printed "field" board from above, an on-device AI model detects weeds, and a servo squeezes a spray bottle — but only when the firmware's safety interlocks allow it. The prototype sprays **water only**.

## What I built

- **Trained a custom weed detector** on Edge Impulse (YOLO-Pro object detection, single class `weed`, 320×320 input) using tiled drone photos of weeds in maize from the Weed-AI ImageWeeds dataset, and deployed it to run fully on-device on the UNO Q (~250–370 ms per frame, no cloud).
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

- Map camera pixels → board centimetres via four corner markers (homography).
- Predict the spray footprint from wind (fan speed/direction) and nozzle mode.
- **Block** any shot whose footprint overlaps a protected plant (unknown plants count as protected); log every decision as ALLOWED/BLOCKED with the reason.
- Operator dashboard with an explicit ARM button.

## Known limits

- The model was trained on drone imagery, not photos of the demo board — it finds roughly 40–45% of weeds (validation mAP@50 ≈ 0.57) and does worse on printed props.
- No Python-side rate limit beyond the 1.5 s detection debounce; the firmware's arm-per-shot rule is the real guard.
