# A PROJECT REPORT ON
# AI VIRTUAL MOUSE USING EYE-GESTURE RECOGNITION

**Submitted in partial fulfillment of the requirements for the degree of**
**Bachelor of Technology**

---

## **ABSTRACT**

In the modern era of Human-Computer Interaction (HCI), hands-free technology is gaining immense importance, especially for individuals with physical disabilities (amputees, paralysis patients). This project, "AI Virtual Mouse," proposes a system to control the mouse cursor using real-time eye movements and clicking operations using eye blinks. The system utilizes a standard webcam and computer vision techniques (OpenCV, MediaPipe) to track facial landmarks without requiring any external hardware or sensors. The proposed system offers a cost-effective, efficient, and user-friendly alternative to traditional input devices.

---

## **TABLE OF CONTENTS**

1.  **Introduction**
2.  **Literature Survey**
3.  **System Design & Architecture**
4.  **Methodology & Algorithms**
5.  **Implementation Details**
6.  **Results & Discussion**
7.  **Conclusion**

---

## **CHAPTER 1: INTRODUCTION**

### **1.1 Overview**
The mouse is one of the most essential input devices for computers. However, prolonging its use can lead to issues like Carpal Tunnel Syndrome, and it is unusable for people with upper-limb disabilities. This project aims to replace the physical mouse with an "Eye-Controlled Mouse" that tracks the user's iris position to move the cursor and detects excessive blinking for click actions.

### **1.2 Problem Statement**
To design and develop a real-time, hands-free virtual mouse system that allows users to perform basic mouse operations (cursor movement, left/right click) using only eye gestures and a webcam, ensuring usability for physically challenged individuals.

### **1.3 Objectives**
*   To implement face and eye landmark detection using MediaPipe.
*   To map eye movements to screen coordinates for cursor control.
*   To detect blink gestures for performing Left and Right clicks.
*   To ensure the system works in real-time with no additional hardware sensors.

---

## **CHAPTER 2: LITERATURE SURVEY**

*   **Existing Methods**: Traditional eye-tracking uses Infrared (IR) sensors or Electrooculography (EOG), which are expensive and intrusive.
*   **Proposed Method**: Our system uses strictly vision-based tracking (RGB Webcam) with Deep Learning models (MediaPipe Face Mesh), which is non-intrusive and highly accurate for geometry-based gesture recognition.

---

## **CHAPTER 3: SYSTEM DESIGN**

### **3.1 System Architecture**
The system consists of four main modules: Capture, detection, Processing, and Action.

```mermaid
graph TD
    A[Webcam Input] -->|Frame Capture| B(Preprocessing)
    B -->|Convert to RGB & Flip| C{Face Detection}
    C -->|No Face| A
    C -->|Face Detected| D[MediaPipe Face Mesh]
    D --> E[Landmark Extraction]
    
    subgraph Processing
    E --> F[Iris Tracking]
    E --> G[Blink Detection]
    end
    
    F -->|Centroid Calculation| H[Cursor Control]
    G -->|EAR Calculation| I[Click Action]
    
    H --> J[PyAutoGUI Mouse Move]
    I --> K[PyAutoGUI Mouse Click]
```

### **3.2 Data Flow**
1.  **Input**: Webcam captures video frames (640x480).
2.  **Preprocessing**: Frames are flipped which is essential for "Mirror Interaction" (Moving head left moves cursor left).
3.  **Model**: MediaPipe FaceLandmarker infers 478 landmarks.
4.  **Logic**:
    *   **Iris**: Landmarks 468-472 (Right) and 473-477 (Left).
    *   **Eyelids**: Upper and Lower eyelid landmarks for blink calculation.

---

## **CHAPTER 4: METHODOLOGY**

### **4.1 Eye Aspect Ratio (EAR)**
To detect blinking, we use the scalar quantity EAR, derived from the Euclidean distance between vertical and horizontal eye landmarks.

$$ EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 \times ||p1 - p4||} $$

*   **Open Eye**: EAR > 0.20
*   **Closed Eye**: EAR < 0.14
*   **Action**: If EAR stays low for 2 consecutive frames, the system registers a "Blink".

### **4.2 Cursor Mapping & Smoothing**
Raw eye tracking is jittery. We used two techniques to solve this:
1.  **Active Zone**: We map only a central rectangle of the camera feed to the full screen. This allows the user to reach screen corners comfortably.
2.  **Exponential Smoothing**: 
    $$ X_{smooth} = \alpha \cdot X_{new} + (1 - \alpha) \cdot X_{prev} $$
    Where $\alpha$ is determined by the `SMOOTHING_FACTOR`. This acts as a Low-Pass Filter.

---

## **CHAPTER 5: IMPLEMENTATION**

### **5.1 Hardware Requirements**
*   **Processor**: Intel Core i3 or higher / AMD Ryzen 3.
*   **RAM**: 4GB Minimum.
*   **Camera**: Standard USB Webcam (720p Recommended).

### **5.2 Software Stack**
*   **Python 3.14**: Primary programming language.
*   **OpenCV**: For frame capture and image manipulation.
*   **MediaPipe**: Google's ML solution for high-fidelity face geometry.
*   **PyAutoGUI**: Cross-platform GUI automation module.

### **5.3 Code Structure**
*   `main.py`: The orchestrator script.
*   `src/eye_tracker.py`: Wrapper for MediaPipe Tasks API.
*   `src/cursor_controller.py`: Handles screen resolution mapping and smoothing.
*   `config.py`: Centralized configuration for sensitivity tuning.

---

## **CHAPTER 6: RESULTS AND DISCUSSION**

### **6.1 Performance Metrics**
*   **Processing Speed**: Average 25 FPS on CPU (Intel i5 11th Gen).
*   **Latency**: < 50ms from movement to cursor reaction.
*   **Accuracy**: 
    *   Blink Detection: ~95% accuracy in good lighting.
    *   Cursor Precision: Pixel-perfect precision is difficult, but button-target precision is achieved.

### **6.2 Limitations**
*   **Lighting**: Requires even lighting on the face; shadows cause landmark jitter.
*   **Glasses**: Reflections on glasses can confuse the iris tracker.

---

## **CHAPTER 7: CONCLUSION**

The AI Virtual Mouse successfully demonstrates that costly hardware is not required for accessibility. By leveraging efficient Deep Learning models like MediaPipe, we can run complex HCI systems on commodity hardware. This project serves as a strong foundation for future assistive technologies.

---
**References**
1.  MediaPipe Solutions: [https://developers.google.com/mediapipe](https://developers.google.com/mediapipe)
2.  Rosebrock, A. (2016). *Real-time eye blink detection using Facial Landmarks*. PyImageSearch.
