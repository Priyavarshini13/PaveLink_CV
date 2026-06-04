from ultralytics import YOLO
import cv2

model = YOLO("y8best.pt")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    results = model.predict(
        source=frame,
        conf=0.5,
        show_labels=True,
        show_conf=True,
        verbose=False
    )

    # Print detections in terminal
    for box in results[0].boxes:
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        print(f"{model.names[cls]}: {conf:.2f}")

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Webcam", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()