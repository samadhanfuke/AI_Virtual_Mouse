# 🖱️ AI Virtual Mouse Using Eye-Gesture Recognition

## 📌 Project Overview

The **AI Virtual Mouse Using Eye-Gesture Recognition** is an AI-ML based computer vision project that allows users to control the mouse cursor using **eye movements and blinking gestures** instead of a physical mouse.

This system uses a **webcam** to track eye landmarks in real time and converts eye gestures into mouse actions such as:

* Cursor movement
* Left click
* Right click
* Scroll / Drag (optional)

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
* **MediaPipe** – face & eye landmark detection
* **NumPy** – numerical operations
* **PyAutoGUI** – mouse control
* **Math & Geometry** – blink detection logic

---

## 📂 Project Structure

```
AI_Virtual_Mouse/
│
├── main.py                  # Main execution file
├── eye_tracker.py           # Eye and iris tracking logic
├── blink_detector.py        # Blink detection using EAR
├── mouse_controller.py      # Mouse movement & click actions
├── utils.py                 # Helper functions
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── demo_video.mp4           # Project demo (optional)
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

If `requirements.txt` is not available:

```bash
pip install opencv-python mediapipe numpy pyautogui
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
* MediaPipe Face Mesh detects facial landmarks
* Eye and iris landmarks are extracted

### 2️⃣ Cursor Movement

* Iris position is mapped to screen coordinates
* Cursor moves according to eye direction
* Smoothing applied to avoid jitter

### 3️⃣ Blink Detection

* Eye Aspect Ratio (EAR) is calculated
* EAR below threshold → blink detected
* Gesture mapping:

  * Left eye blink → Left click
  * Right eye blink → Right click
  * Both eyes blink → Scroll / Drag (optional)

---

## 📐 Eye Aspect Ratio (EAR) Formula

[
EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 \times ||p1 - p4||}
]

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

### Cursor shaking

* Increase smoothing factor
* Improve lighting

### PyAutoGUI permission error (Linux)

```bash
sudo apt install python3-tk python3-dev
```

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
