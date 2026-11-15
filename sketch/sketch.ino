#include <Arduino_RouterBridge.h>

const int SERVO_PIN  = 9;
const int BUTTON_PIN = 2;          // jumper to GND = STOP (disarms)
const int REST_DEG     = 180;
const int SQUEEZED_DEG = 80;
const int SQUEEZE_MS   = 400;
const int RETURN_MS    = 300;
const int N            = 15;       // 0.3 s of "pressed" to count as a press

int count = 0;
bool armed = false;                // starts disarmed
bool fireRequested = false;

int toUs(int deg) { return 544 + (long)deg * 1856 / 180; }
void pulse(int us) { digitalWrite(SERVO_PIN, HIGH); delayMicroseconds(us); digitalWrite(SERVO_PIN, LOW); delay(20); }
void hold(int deg, int holdMs) { for (int i = 0; i < holdMs / 20; i++) pulse(toUs(deg)); }
void ramp(int fromDeg, int toDeg, int rampMs) {
  int steps = rampMs / 20; long a = toUs(fromDeg), b = toUs(toDeg);
  for (int i = 1; i <= steps; i++) pulse(a + (b - a) * i / steps);
}

// Called from Python. Only queues a shot if armed.
void fire() {
  if (armed) fireRequested = true;
}
void set_armed(bool a) { armed = a; }

void setup() {
  pinMode(SERVO_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Bridge.begin();
  Bridge.provide_safe("fire", fire);          // runs between loop() passes
  Bridge.provide_safe("set_armed", set_armed);
}

void loop() {
  bool pressed = (digitalRead(BUTTON_PIN) == LOW);
  count = pressed ? count + 1 : 0;
  if (count >= N) { armed = false; fireRequested = false; }   // STOP

  if (fireRequested) {
    fireRequested = false;
    ramp(REST_DEG, SQUEEZED_DEG, SQUEEZE_MS);
    hold(REST_DEG, RETURN_MS);
    armed = false;                 // one shot, then disarm
  } else {
    hold(REST_DEG, 20);
  }
}
