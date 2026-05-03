import numpy as np

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [13, 14, 78, 308]

def get_points(landmarks, indices, w, h):
    return [(int(landmarks.landmark[i].x * w),
             int(landmarks.landmark[i].y * h)) for i in indices]

def calculate_ear(eye):
    A = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
    B = np.linalg.norm(np.array(eye[2]) - np.array(eye[4]))
    C = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
    return (A + B) / (2.0 * C + 1e-6)

def calculate_mar(mouth):
    top, bottom, left, right = mouth
    vertical = np.linalg.norm(np.array(top) - np.array(bottom))
    horizontal = np.linalg.norm(np.array(left) - np.array(right))
    return vertical / (horizontal + 1e-6)