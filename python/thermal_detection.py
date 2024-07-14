import cv2
import numpy as np

def thermal_detection(frame):
    # Konversi gambar ke skala abu-abu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Deteksi area dengan panas tubuh
    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return heatmap

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    heatmap = thermal_detection(frame)

    cv2.imshow("Thermal Detection", heatmap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
