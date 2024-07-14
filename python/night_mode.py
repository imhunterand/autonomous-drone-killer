import cv2

def enable_night_mode(frame):
    # Meningkatkan kontras untuk mode malam
    alpha = 1.5 # Kontras kontrol
    beta = 0    # Kecerahan kontrol
    adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    return adjusted

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    night_mode_frame = enable_night_mode(frame)

    cv2.imshow("Night Mode", night_mode_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
