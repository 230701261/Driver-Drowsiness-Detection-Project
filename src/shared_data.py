# src/shared_data.py

from collections import deque

class SharedData:
    def __init__(self):
        self.fatigue = deque(maxlen=100)
        self.ear = deque(maxlen=100)
        self.mar = deque(maxlen=100)
        self.blink_rate = deque(maxlen=100)
        self.yawns = deque(maxlen=100)

shared_data = SharedData()