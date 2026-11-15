#!/bin/sh
# One-time venv bootstrap for cascade_bench on an Arduino UNO Q (Python 3.13, no system pip).
set -e
cd "$(dirname "$0")"
mkdir -p images
python3 -m venv --without-pip venv
curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
./venv/bin/python get-pip.py --no-cache-dir -q && rm get-pip.py
./venv/bin/pip install --no-cache-dir -q -r requirements.txt
# edge_impulse_linux imports pyaudio at package init; no aarch64 wheel, audio never used here.
./venv/bin/python -c "import pyaudio" 2>/dev/null || \
  printf '# stub: audio API is never used by cascade.py\n' > venv/lib/python3.13/site-packages/pyaudio.py
./venv/bin/python -c "from edge_impulse_linux.image import ImageImpulseRunner; import cv2; print('OK', cv2.__version__)"
chmod +x run.sh
