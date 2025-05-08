import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model (e.g., yolov8n for speed, yolov8m/yolov8l for accuracy)
model = YOLO("yolo11n.pt") # Downloaded automatically if not present

# Real object height (meters)
KNOWN_HEIGHT = 1.7  # Example: human average height

# Approximate camera focal length (can be calibrated)
FOCAL_LENGTH = 615  # Adjust this experimentally

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    for box in results.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]

        if label == 'person' and conf > 0.5:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            height_px = y2 - y1

            if height_px > 0:
                distance = (KNOWN_HEIGHT * FOCAL_LENGTH) / height_px
                cv2.putText(frame, f"{label} {distance:.2f}m", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imshow("YOLOv8 Distance Estimation", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
