# 🖱️ AI Virtual Mouse Using Eye-Gesture Recognition

## 📌 Project Overview

The **AI Virtual Mouse Using Eye-Gesture Recognition** is an AI-ML based computer vision project that allows users to control the mouse cursor using **eye movements and blinking gestures** instead of a physical mouse.

This system uses a **webcam** to track eye landmarks in real time and converts eye gestures into mouse actions such as:

* Cursor movement
* Left click
* Right click

The project demonstrates concepts of **Artificial Intelligence, Machine Learning, Computer Vision, and Human–Computer Interaction (HCI)**.

---

## 🎯 Key Features

* Real-time eye tracking using webcam
* Mouse movement controlled by iris position
* Blink-based mouse click detection
* No external hardware required
* Works on **Windows & Linux**
* Lightweight and easy to run
* College-level AI-ML project (viva friendly)

---

## 🧠 Technologies Used

* **Python 3**
* **OpenCV** – video processing
* **MediaPipe** – face & eye landmark detection (Tasks API)
* **NumPy** – numerical operations
* **PyAutoGUI** – mouse control
* **Math & Geometry** – blink detection logic

---

## 📂 Project Structure

```
AI_Virtual_Mouse/
│
├── main.py                  # Main execution file
├── config.py                # Configuration settings (sensitivity, thresholds)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── face_landmarker.task     # MediaPipe Model File
│
└── src/
    ├── eye_tracker.py       # Eye and iris tracking logic
    ├── gesture_processor.py # Blink detection using EAR
    ├── cursor_controller.py # Mouse movement & click actions
    └── camera_manager.py    # Webcam video capture
```

---

## ⚙️ System Requirements

### Hardware

* Laptop / Desktop
* Webcam (inbuilt or external)
* Minimum 4 GB RAM

### Software

* Python **3.8 or above**
* Windows 10 / 11 **OR** Linux (Ubuntu/Debian recommended)

---

## 🖥️ Installation Instructions

### 🔹 Step 1: Install Python

Download and install Python from:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

⚠️ **Important:**
While installing on Windows, **check the box**
✅ *“Add Python to PATH”*

Verify installation:

```bash
python --version
```

---

### 🔹 Step 2: Clone or Download Project

```bash
git clone https://github.com/your-username/AI_Virtual_Mouse.git
cd AI_Virtual_Mouse
```

OR
Download ZIP → Extract → Open folder in terminal.

---

### 🔹 Step 3: Create Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🔹 Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If `face_landmarker.task` is missing, run:
```bash
python download_model.py
```

---

## ▶️ How to Run the Project

### Windows

```bash
python main.py
```

### Linux

```bash
python3 main.py
```

📷 **Allow webcam access when prompted**

---

## 🧪 How It Works (Logic Explanation)

### 1️⃣ Face & Landmark Detection
* The system captures frames from the webcam using OpenCV.
* Frames are flipped horizontally for a mirror effect (Natural Interaction).
* **MediaPipe Face Landmarker** processes the RGB frame to detect **478 facial landmarks**.
* We specifically extract landmarks for the **Left Eye**, **Right Eye**, and **Irises**.

### 2️⃣ Gaze & Cursor Control
* **Iris Tracking**: We calculate the **centroid** (center point) of the specific eye's iris landmarks.
* **Screen Mapping**: The iris position is mapped from the camera's resolution to the monitor's screen resolution (e.g., 1920x1080).
* **Smoothing**: To ensure usability, we apply a mathematical **Moving Average** filter. This reduces the "jitter" caused by webcam noise or micro-movements.
* **Active Zone**: A subset of the camera frame is mapped to the full screen, allowing you to reach screen edges comfortably without straining your eyes.

### 3️⃣ Blink Detection & Clicking
* We use the **Eye Aspect Ratio (EAR)** geometry formula to detect blinks.
* **Logic**: If `EAR < 0.14` (Threshold configured in `config.py`), the eye is considered **closed**.
* **Debouncing**: The system waits for `2 consecutive frames` of closure to confirm a deliberate blink, preventing accidental clicks.
* **Action Trigger** (Mirrored):
  * **Left Eye Blink** (Physical) → **Left Click**
  * **Right Eye Blink** (Physical) → **Right Click**

---

## 📐 Eye Aspect Ratio (EAR) Formula

$$
EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 \times ||p1 - p4||}
$$

* Low EAR → Eye closed
* High EAR → Eye open

---

## 🔍 Implementation Insights

### 1️⃣ Mirrored Interaction
The camera feed is **flipped horizontally** (mirrored) to make the interaction intuitive (e.g., looking left moves cursor left).
* **Challenge**: MediaPipe detects landmarks relative to the *image*.
* **Solution**: We swapped the click logic in `main.py`.
    * **Physical Left Eye** → Appears as "Right Eye" in frame → Triggers **Left Click**.
    * **Physical Right Eye** → Appears as "Left Eye" in frame → Triggers **Right Click**.

### 2️⃣ Cursor Smoothing
To prevent the cursor from jittering due to micro-movements of the eye/head, we implemented a **Moving Average** smoothing algorithm in `src/cursor_controller.py`.
* **Logic**: `current_pos = prev_pos + (target_pos - prev_pos) / smoothing_factor`
* **Config**: `SMOOTHING_FACTOR = 5` (Found to be the sweet spot between responsiveness and stability).

### 3️⃣ Blink Sensitivity
We fine-tuned the `BLINK_THRESHOLD` to **0.14**.
* **Reason**: Standard values (0.2-0.3) triggered false clicks during normal looking.
* **Debounce**: A blink must persist for `BLINK_CONSEC_FRAMES` (2 frames) to register as a valid click.

---

## ⚠️ Important Notes

* Use project in **well-lit environment**
* Keep face clearly visible to webcam
* Avoid fast head movements
* Recommended distance: **40–70 cm** from camera

---

## 🐞 Common Issues & Fixes

### Webcam not opening

* Close other apps using the camera (Zoom, Teams)
* Check camera permissions
* Change `CAMERA_INDEX` in `config.py`

### Cursor shaking

* Increase `SMOOTHING_FACTOR` in `config.py`
* Improve lighting

### PyAutoGUI fail-safe

* If the mouse moves to a corner, the program stops. This is a safety feature.

---

## 🚀 Future Enhancements

* ML-based gesture classification
* Voice + eye hybrid control
* On-screen calibration window
* Accessibility mode for disabled users
* Performance optimization for low-end systems

---

## 🎓 Academic Use

This project is suitable for:

* BE / BTech / Diploma final-year project
* AI-ML & Computer Vision coursework
* Project demonstration & viva

---

## 👨‍💻 Author

**Samadhan Fuke**
AI-ML | Computer Vision | Linux | DevOps

---

## 📜 License

This project is for **educational purposes only**.

---
