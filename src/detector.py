# src/detector.py

from ultralytics import YOLO

class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # lightweight model

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        if results and len(results[0].boxes) > 0:
            return results[0].boxes.xyxy.cpu().numpy()
        return []