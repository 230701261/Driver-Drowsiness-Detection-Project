from config import *
from src.alert import mild_alert, warning_alert, critical_alert
import time

class DrowsinessPipeline:
    def __init__(self):
        self.closed_frames = 0
        self.yawn_frames = 0
        self.yawn_count = 0

        self.blink_count = 0
        self.eye_closed = False
        self.start_time = time.time()

    def process(self, ear, mar):
        # ---- BLINK DETECTION ----
        if ear < BLINK_EAR_THRESHOLD:
            if not self.eye_closed:
                self.blink_count += 1
                self.eye_closed = True
        else:
            self.eye_closed = False

        elapsed_time = time.time() - self.start_time
        blink_rate = (self.blink_count / elapsed_time) * 60 if elapsed_time > 0 else 0

        # ---- EYE DROWSINESS ----
        if ear < EAR_THRESHOLD:
            self.closed_frames += 1
        else:
            self.closed_frames = 0

        # ---- YAWN ----
        if mar > MAR_THRESHOLD:
            self.yawn_frames += 1
        else:
            if self.yawn_frames > 10:
                self.yawn_count += 1
            self.yawn_frames = 0

        # ---- FATIGUE SCORE ----
        fatigue = min(100, (
            (self.closed_frames / SEVERE_FRAMES) * 60 +
            (self.yawn_count * 10)
        ))

        # ---- STATUS ----
        if fatigue > 80:
            status = "CRITICAL"
            critical_alert()
        elif fatigue > 50:
            status = "WARNING"
            warning_alert()
        elif fatigue > 25:
            status = "TIRED"
            mild_alert()
        else:
            status = "ALERT"

        return status, fatigue, self.yawn_count, self.blink_count, int(blink_rate)