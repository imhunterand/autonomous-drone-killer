#include <Servo.h>
#include "motor_control.h"
#include "camera_servo_control.h"
#include "target_lock.h"

void setup() {
  initMotorControl();
  initCameraServo();
  initTargetLock();
}

void loop() {
  updateMotorControl();
  updateCameraServo();
  updateTargetLock();
}
