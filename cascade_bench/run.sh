#!/bin/sh
# Make the Edge Impulse runners executable, then run the benchmark inside the venv.
cd "$(dirname "$0")" || exit 1
for f in yolo.eim fomo.eim; do [ -f "$f" ] && chmod +x "$f"; done
exec ./venv/bin/python cascade.py
