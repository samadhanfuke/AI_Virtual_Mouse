# A PROJECT REPORT ON
# AI VIRTUAL MOUSE USING EYE-GESTURE RECOGNITION

**Submitted in partial fulfillment of the requirements for the degree of**
**Bachelor of Technology**

---

## **ABSTRACT**

In the modern era of Human-Computer Interaction (HCI), hands-free technology is gaining immense importance, especially for individuals with physical disabilities (amputees, paralysis patients). This project, "AI Virtual Mouse," proposes a system to control the mouse cursor using real-time eye movements and clicking operations using eye blinks. The system utilizes a standard webcam and computer vision techniques (OpenCV, MediaPipe) to track facial landmarks without requiring any external hardware or sensors. The proposed system offers a cost-effective, efficient, and user-friendly alternative to traditional input devices.

---

## **CHAPTER 1: INTRODUCTION**

### **1.1 Overview**
The mouse is one of the most essential input devices for computers. However, prolonged use can lead to issues like Carpal Tunnel Syndrome, and it is unusable for people with upper-limb disabilities. This project aims to replace the physical mouse with an "Eye-Controlled Mouse" that tracks the user's iris position to move the cursor and detects excessive blinking for click actions.

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

## **CHAPTER 3: SYSTEM ANALYSIS AND DESIGN**

### **3.1 Technology Stack**
*   **Language**: Python 3.x
*   **Libraries**:
    *   `OpenCV`: Video capture and image processing.
    *   `MediaPipe`: 468-point Face Landmark detection (Face Mesh).
    *   `PyAutoGUI`: Programmatic control of the mouse cursor and clicks.
    *   `NumPy`: Scientific calculations for geometry (Euclidean distance).

### **3.2 System Architecture**
1.  **Input**: Webcam captures video frames.
2.  **Preprocessing**: Frames are flipped (mirrored) and converted to RGB.
3.  **Detection**: MediaPipe model detects face mesh and extracts Eye/Iris landmarks.
4.  **Processing**:
    *   **Gaze Tracking**: Centroid of the Iris is calculated and mapped to screen dimensions using interpolation.
    *   **Blink Detection**: Eye Aspect Ratio (EAR) is calculated. If EAR < Threshold (0.14), a blink is registered.
5.  **Action**: PyAutoGUI executes the cursor move or click event.

---

## **CHAPTER 4: IMPLEMENTATION DETAILS**

### **4.1 Eye Aspect Ratio (EAR)**
To detect blinking, we use the scalar quantity EAR:
$$ EAR = \frac{||p2 - p6|| + ||p3 - p5||}{2 \times ||p1 - p4||} $$
Where p1...p6 are specific 2D landmark points around the eye.
*   **Open Eye**: High EAR (> 0.20)
*   **Closed Eye**: Low EAR (< 0.14)

### **4.2 Cursor Smoothing**
To prevent jittering associated with webcam noise, simple raw coordinates are not used. Instead, a **Moving Average** smoothing technique is applied:
`Current_Screen_X = Previous_X + (Target_X - Previous_X) / Smoothing_Factor`

---

## **CHAPTER 5: RESULTS AND DISCUSSION**

### **5.1 Performance**
*   **Frame Rate**: The system runs at approximately 20-30 FPS on a standard Core i5 laptop without GPU acceleration (`xnnpack` delegate).
*   **Accuracy**: Cursor control is stable in well-lit environments. Blink detection has a success rate of >90% with proper tuning.

### **5.2 Limitations**
*   Performance degrades in low-light conditions.
*   Wearing thick-rimmed glasses may sometimes occlude eye landmarks.
*   The "Active Zone" mapping requires the user to keep their head relatively stable.

---

## **CHAPTER 6: CONCLUSION AND FUTURE SCOPE**

### **6.1 Conclusion**
The AI Virtual Mouse successfully demonstrates the potential of Computer Vision in HCI. It provides a viable, low-cost generic interface for controlling computers without hands, satisfying the core objectives of accessibility and innovation.

### **6.2 Future Scope**
*   Implementation of "Drag and Drop" using long-blink gestures.
*   Integration of AI-based gaze estimation for higher precision.
*   Adding voice command integration for typing (Virtual Keyboard).

---

## **REFERENCES**
1.  MediaPipe Solutions: https://developers.google.com/mediapipe
2.  OpenCV Documentation: https://docs.opencv.org/
3.  PyAutoGUI Documentation: https://pyautogui.readthedocs.io/
