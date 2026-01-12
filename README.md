# AI Virtual Mouse

A real-time AI Virtual Mouse system that allows you to control the mouse cursor and perform clicks using eye movements and blink gestures. This project uses **OpenCV**, **MediaPipe** (Face Mesh), and **PyAutoGUI**.

## Features

- **Real-time Eye Tracking**: Controls mouse cursor using iris/face position.
- **Blink Detection**:
    - **Left Blink** → Left Click
    - **Right Blink** → Right Click
- **Smooth Movement**: Uses moving average smoothing for stable cursor control.
- **Visual Feedback**: Displays FPS and eye landmarks on the camera feed.

## Technology Stack

- **Python 3.x**
- **OpenCV** (Video processing)
- **MediaPipe** (Face & Iris landmark detection)
- **PyAutoGUI** (Mouse control)
- **NumPy** (Mathematical operations)

## Installation

1.  Clone the repository or download the source code.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the main script:
    ```bash
    python main.py
    ```
2.  **Controls**:
    - **Move Cursor**: Move your head/eyes. The system maps your face position within the camera frame to the screen.
    - **Left Click**: Blink your **Left Eye** intentionally.
    - **Right Click**: Blink your **Right Eye** intentionally.
    - **Exit**: Press `q` to quit the application.

## Configuration

You can adjust settings in `config.py`:
- `BLINK_THRESHOLD`: Sensitivity of blink detection (lower = harder to blink).
- `SMOOTHING_FACTOR`: Higher values = smoother movement but more lag.
- `CAMERA_INDEX`: Change if you have multiple cameras.

## Project Structure

- `src/`: Contains core modules (Camera, EyeTracker, GestureProcessor, CursorController).
- `main.py`: Entry point of the application.
- `config.py`: Configuration constants.
- `requirements.txt`: Python dependencies.

## Safety Mechanism
This application uses `pyautogui`. If the mouse control goes out of hand, quickly move the mouse pointer to any corner of the screen to trigger the **Fail-Safe** and terminate the program.
