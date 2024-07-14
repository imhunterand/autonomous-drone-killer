#include <Servo.h>

Servo servoX;
Servo servoY;

void initCameraServo() {
  servoX.attach(11);
  servoY.attach(12);
}

void updateCameraServo() {
  // Implementasi logika kontrol servo kamera
}
