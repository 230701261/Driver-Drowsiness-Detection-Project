# Driver Drowsiness Detection Project

A real-time driver drowsiness detection system that uses computer vision and deep learning to monitor driver alertness and provide alerts to prevent accidents.

## Features

- **Real-time Face Detection**: Uses YOLOv8 for efficient face detection
- **Facial Landmark Detection**: Powered by MediaPipe for precise facial feature tracking
- **Drowsiness Indicators**: 
  - Eye Aspect Ratio (EAR) calculation
  - Mouth Aspect Ratio (MAR) for yawn detection
  - Blink rate monitoring
  - Fatigue level percentage
- **Alert System**: Alerts driver when drowsiness is detected
- **Interactive Dashboard**: Streamlit-based visualization of real-time metrics
- **Multi-severity Support**: Mild, Moderate, and Severe drowsiness levels
- **Logging**: Comprehensive logging of detection events

## System Requirements

- Python 3.8+
- OpenCV 4.0+
- PyTorch (for YOLOv8)
- Webcam or video input device

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/230701261/Driver-Drowsiness-Detection-Project.git
cd "Drowsiness Detection"
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the YOLOv8 model
The `yolov8n.pt` (nano model) is included in the repository. If you need a different version:
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

## Usage

### Option 1: Real-time Detection with OpenCV
Run the main detection script:
```bash
python main.py
```
- Press **Q** to exit

### Option 2: Interactive Dashboard
Launch the Streamlit dashboard:
```bash
streamlit run streamlit_app.py
```
Access the dashboard at `http://localhost:8501`

## ⚙️ Configuration

Edit `config.py` to customize detection parameters:

```python
VIDEO_SOURCE = 0              # Webcam index (0 for default)
FRAME_WIDTH = 640            # Frame width
FRAME_HEIGHT = 480           # Frame height

EAR_THRESHOLD = 0.23         # Eye Aspect Ratio threshold
MAR_THRESHOLD = 0.6          # Mouth Aspect Ratio threshold

MILD_FRAMES = 10             # Frames for mild drowsiness
MODERATE_FRAMES = 25         # Frames for moderate drowsiness
SEVERE_FRAMES = 50           # Frames for severe drowsiness

BLINK_EAR_THRESHOLD = 0.20   # Blink detection threshold
```

## Project Structure

```
├── main.py                  # Main OpenCV-based detection script
├── streamlit_app.py         # Dashboard application
├── config.py                # Configuration parameters
├── requirements.txt         # Project dependencies
├── yolov8n.pt              # YOLOv8 nano model
├── src/
│   ├── alert.py            # Alert system
│   ├── detector.py         # Detection utilities
│   ├── face_mesh.py        # Face landmark detection
│   ├── features.py         # Feature calculation (EAR, MAR)
│   ├── pipeline.py         # Processing pipeline
│   └── shared_data.py      # Shared data between processes
└── logs/                    # Event logs directory
```

## How It Works

1. **Face Detection**: YOLOv8 detects faces in each frame
2. **Landmark Detection**: MediaPipe extracts 468 facial landmarks
3. **Feature Calculation**: 
   - Computes Eye Aspect Ratio (EAR) for both eyes
   - Computes Mouth Aspect Ratio (MAR) for yawn detection
4. **Analysis**: 
   - Tracks blink count and rate
   - Monitors yawn frequency
   - Calculates cumulative fatigue level
5. **Alert Generation**: Issues alerts based on drowsiness severity
6. **Visualization**: Displays real-time metrics on screen/dashboard

## Metrics

- **EAR (Eye Aspect Ratio)**: Lower values indicate closed eyes
- **MAR (Mouth Aspect Ratio)**: Higher values indicate open mouth (yawning)
- **Blink Rate**: Number of blinks per minute
- **Fatigue Level**: Percentage-based fatigue accumulation
- **Yawn Count**: Total yawns detected in session

## Output Visualization

The system displays:
- Real-time video feed with facial landmarks
- Live EAR and MAR values
- Blink rate and count
- Fatigue level percentage
- Current drowsiness status

## Logging

Detection events are logged to `logs/` directory with timestamps:
- Drowsiness events
- Alert triggers
- Metrics snapshots

## Alert Levels

- **ALERT**: Mild drowsiness detected (10 frames)
- **WARNING**: Moderate drowsiness detected (25 frames)
- **CRITICAL**: Severe drowsiness detected (50 frames)

##  Dependencies

- **ultralytics**: YOLOv8 object detection
- **opencv-python**: Computer vision operations
- **mediapipe**: Facial landmark detection
- **numpy**: Numerical operations
- **torch**: Deep learning framework
- **streamlit**: Web dashboard framework

##  License

This project is open source. See LICENSE file for details.

##  Author

Created as part of the Driver Safety Project

##  Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

##  Disclaimer

This system is designed for research and safety purposes. Always follow local traffic laws and vehicle safety regulations. Never use this system as a substitute for proper driving practices and regular breaks.
