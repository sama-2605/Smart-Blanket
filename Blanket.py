from ultralytics import YOLO
import cv2
import time

# Load YOLOv11 model (downloaded automatically)
model = YOLO("yolov11n.pt")  # You can replace with yolov11m or yolov11x for higher accuracy

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open camera.")
    exit()

print("Starting detection... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ----- FACE DETECTION -----
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # ----- YOLOv11 BLANKET DETECTION -----
    results = model(frame, verbose=False)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = model.names[cls]
            
            if conf > 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Display results
    cv2.imshow("Blinky Blanket - Face & YOLOv11 Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
