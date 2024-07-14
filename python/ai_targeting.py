import cv2
import numpy as np
import serial

# Konfigurasi serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Load model AI
net = cv2.dnn.readNetFromCaffe('models/deploy.prototxt', 'models/weights.caffemodel')

def detect_and_target(frame):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.2:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

            # Hitung posisi crosshair
            centerX = (startX + endX) // 2
            centerY = (startY + endY) // 2

            cv2.line(frame, (centerX - 10, centerY), (centerX + 10, centerY), (0, 255, 0), 2)
            cv2.line(frame, (centerX, centerY - 10), (centerX, centerY + 10), (0, 255, 0), 2)

            return centerX, centerY

    return None, None

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    centerX, centerY = detect_and_target(frame)
    if centerX and centerY:
        ser.write(f"{centerX},{centerY},1\n".encode())

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
