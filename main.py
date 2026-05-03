import cv2
from config import *
from src.face_mesh import FaceMeshDetector
from src.features import *
from src.pipeline import DrowsinessPipeline
from src.shared_data import shared_data

cap = cv2.VideoCapture(VIDEO_SOURCE)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)

face = FaceMeshDetector()
pipeline = DrowsinessPipeline()

def draw_text(frame, text, y, color):
    cv2.putText(frame, text, (10, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

print("🚀 Running... Press Q to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    landmarks = face.get_landmarks(frame)

    if landmarks:
        left_eye = get_points(landmarks, LEFT_EYE, w, h)
        right_eye = get_points(landmarks, RIGHT_EYE, w, h)
        mouth = get_points(landmarks, MOUTH, w, h)

        ear = (calculate_ear(left_eye) + calculate_ear(right_eye)) / 2
        mar = calculate_mar(mouth)

        status, fatigue, yawns, blinks, blink_rate = pipeline.process(ear, mar)

        draw_text(frame, f"{status}", 20, (0,255,0))
        draw_text(frame, f"EAR:{round(ear,2)}", 40, (255,255,0))
        draw_text(frame, f"MAR:{round(mar,2)}", 60, (255,0,255))
        draw_text(frame, f"Yawns:{yawns}", 80, (0,255,255))
        draw_text(frame, f"Blinks:{blinks}", 100, (255,165,0))
        draw_text(frame, f"Rate:{blink_rate}/m", 120, (200,200,255))
        draw_text(frame, f"Fatigue:{int(fatigue)}%", 140, (0,0,255))

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()