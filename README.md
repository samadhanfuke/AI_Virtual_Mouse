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

### 1️⃣ Eye Detection

* Webcam captures live video
* MediaPipe Face Landmarker detects facial landmarks
* Eye and iris landmarks are extracted

### 2️⃣ Cursor Movement

* Iris position is mapped to screen coordinates
* Cursor moves according to eye direction
* Smoothing applied to avoid jitter (Configurable in `config.py`)

### 3️⃣ Blink Detection

* Eye Aspect Ratio (EAR) is calculated
* EAR below threshold → blink detected
* Gesture mapping:

  * **Left eye blink** → Left click
  * **Right eye blink** → Right click

---

## 📐 Eye Aspect Ratio (EAR) Formula

$$
EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 \times ||p1 - p4||}
$$

* Low EAR → Eye closed
* High EAR → Eye open

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
