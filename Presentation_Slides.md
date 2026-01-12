# 📊 Presentation Slides: AI Virtual Mouse

## **Slide 1: Title Slide**
*   **Project Title**: AI Virtual Mouse Using Eye-Gesture Recognition
*   **Presented By**: Samadhan Fuke
*   **Guide/Dept**: Dept. of Computer Science / AI-DS
*   *(Add College Logo)*

---

## **Slide 2: Introduction**
*   **What is it?**: A hands-free system to control the mouse cursor using eye movements and blinks.
*   **Target Audience**: Amputees, paralysis patients, and HCI researchers.
*   **Key Idea**: Replace physical hardware with Computer Vision (Software).

---

## **Slide 3: Problem Statement**
*   **Current Limitation**: Physical mice require fine motor control of hands. Usage is impossible for people with upper-limb disabilities.
*   **Solution**: Use the **Eyes** (which are almost always active) as a pointer device.
*   **Challenge**: Doing this in real-time on a standard consumer laptop webcam.

---

## **Slide 4: Objectives**
1.  Real-time Face & Eye detection.
2.  Cursor movement based on Iris position.
3.  Click actions (Left/Right) based on Eye Blinks.
4.  Low latency and high accuracy.

---

## **Slide 5: Technology Stack**
*   **Python 3**: Core Logic.
*   **OpenCV**: Image Acquisition & Processing.
*   **MediaPipe**: The "Brains" - Deep Learning model for Face Mesh (478 Landmarks).
*   **PyAutoGUI**: The "Hands" - Controlling the OS mouse.

---

## **Slide 6: System Architecture (Flowchart)**
1.  **Start** Webcam.
2.  **Detect** Face Mesh.
3.  **Extract** Eye ROI (Region of Interest).
4.  **Calculate** EAR (Eye Aspect Ratio).
    *   If EAR < 0.14 → **Click**.
5.  **Calculate** Iris Center.
    *   Map to Screen Coordinates → **Move Cursor**.
6.  **Repeat**.

---

## **Slide 7: Implementation Logic**
*   **Blink Detection**:
    *   Uses geometric distance between eyelids.
    *   **Formula**: EAR = (Vertical Dist) / (Horizontal Dist).
*   **Cursor Mapping**:
    *   We map a small "Active Zone" on the camera to the full HD screen.
    *   Includes **Smoothing** (Math filter) to stop the cursor from shaking.

---

## **Slide 8: Advantages & Applications**
*   **Advantages**:
    *   No external sensors/wearables needed.
    *   Hygienic (Contactless).
    *   Cost-effective (Free software).
*   **Applications**:
    *   Assistive Technology.
    *   Public Kiosks (prevent germ spread).
    *   Gaming/VR interaction.

---

## **Slide 9: Results (Demo)**
*   *(Include Screenshot of the App running with landmarks specific)*
*   Achieved **20+ FPS** on CPU.
*   Successfully performs Left/Right clicks.
*   Fail-safe mechanism implemented for safety.

---

## **Slide 10: Conclusion & Future Scope**
*   **Conclusion**: System successfully enables hands-free computer interaction.
*   **Future Scope**:
    *   Voice integration for typing.
    *   Deep Learning for complex gestures (wink vs blink).
    *   Mobile App version.

---

## **Slide 11: End**
*   **Thank You!**
*   **Questions?**
