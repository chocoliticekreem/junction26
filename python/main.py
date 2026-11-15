# SPDX-FileCopyrightText: Copyright (C) Arduino s.r.l. and/or its affiliated companies
#
# SPDX-License-Identifier: MPL-2.0

from arduino.app_utils import App, Bridge
from arduino.app_bricks.video_objectdetection import VideoObjectDetection

# Report weeds the model is at least 40% sure about, at most once every 1.5 s
video_detector = VideoObjectDetection(confidence=0.4, debounce_sec=1.5)


# Called when a weed is detected (no arguments allowed)
def on_weed_detected():
    print("🌿 Weed detected! Requesting spray")
    # The sketch fires once, then disarms itself
    Bridge.call("set_armed", True)
    Bridge.call("fire")


video_detector.on_detect("weed", on_weed_detected)


# Called with everything detected in a frame (one dict argument)
def on_all_detections(detections: dict):
    # Example: {"weed": [{"confidence": 0.82, "bounding_box_xyxy": (10, 20, 110, 220)}]}
    print("All detections:", detections)


video_detector.on_detect_all(on_all_detections)

# Keep the video detection loop running
App.run()
