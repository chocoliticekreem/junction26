#!/usr/bin/env python3
"""Two-tier FOMO -> YOLO cascade benchmark on saved frames (Edge Impulse .eim runners)."""
import csv, os, sys, time
import cv2
from edge_impulse_linux.image import ImageImpulseRunner

YOLO_PATH = os.path.expanduser("~/cascade_bench/yolo.eim")
FOMO_PATH = os.path.expanduser("~/cascade_bench/fomo.eim")
IMAGES_DIR = os.path.expanduser("~/cascade_bench/images")
LOW, HIGH, YOLO_CONF = 0.3, 0.7, 0.5
TARGET_CLASS = None  # FOMO label to score, e.g. "weed"; None = max over all labels
OUT_CSV = os.path.expanduser("~/cascade_bench/results.csv")
EXTS = (".jpg", ".jpeg", ".png", ".bmp")
D = {True: "SPRAY", False: "NO_SPRAY"}


def timed_run(runner, img_bgr):
    """Resize/feature-extract + classify; returns (bounding_boxes, elapsed_ms)."""
    t0 = time.perf_counter()
    feats, _ = runner.get_features_from_image(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    res = runner.classify(feats)
    return res["result"].get("bounding_boxes", []), (time.perf_counter() - t0) * 1000


def main():
    missing = [p for p in (YOLO_PATH, FOMO_PATH, IMAGES_DIR) if not os.path.exists(p)]
    if missing:
        print("Missing input(s):\n  " + "\n  ".join(missing))
        sys.exit(1)
    images = sorted(f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(EXTS))
    if not images:
        print(f"No images ({', '.join(EXTS)}) in {IMAGES_DIR}")
        sys.exit(1)
    fomo, yolo = ImageImpulseRunner(FOMO_PATH), ImageImpulseRunner(YOLO_PATH)
    rows = []
    try:
        fomo.init(), yolo.init()
        for name in images:
            img = cv2.imread(os.path.join(IMAGES_DIR, name))
            if img is None:
                print(f"skip unreadable {name}")
                continue
            fboxes, fomo_ms = timed_run(fomo, img)
            yboxes, yolo_ms = timed_run(yolo, img)  # baseline; reused for tier 2
            score = max((b["value"] for b in fboxes if TARGET_CLASS in (None, b["label"])), default=0.0)
            yolo_dec = any(b["value"] >= YOLO_CONF for b in yboxes)
            if score >= HIGH:
                tier, casc = 1, True
            elif score <= LOW:
                tier, casc = 1, False
            else:
                tier, casc = 2, yolo_dec
            rows.append((name, fomo_ms, yolo_ms, score, tier, casc, yolo_dec))
    finally:
        fomo.stop(), yolo.stop()
    if not rows:
        sys.exit("no readable images")
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["image", "fomo_ms", "yolo_ms", "fomo_score", "tier", "cascade_decision", "yolo_decision"])
        for n, fm, ym, sc, t, c, y in rows:
            w.writerow([n, f"{fm:.2f}", f"{ym:.2f}", f"{sc:.4f}", t, D[c], D[y]])
    n = len(rows)
    y_ms = [r[2] for r in rows]
    c_ms = [r[1] + (r[2] if r[4] == 2 else 0.0) for r in rows]
    deferred, agree = sum(r[4] == 2 for r in rows), sum(r[5] == r[6] for r in rows)
    print(f"{n} images -> {OUT_CSV}")
    print(f"YOLO alone : mean {sum(y_ms)/n:7.1f} ms   max {max(y_ms):7.1f} ms")
    print(f"Cascade    : mean {sum(c_ms)/n:7.1f} ms   max {max(c_ms):7.1f} ms")
    print(f"Deferral rate        : {100*deferred/n:5.1f}%")
    print(f"Agreement with YOLO  : {100*agree/n:5.1f}%")
    print(f"Speed-up factor      : {sum(y_ms)/sum(c_ms):5.2f}x")


if __name__ == "__main__":
    main()
