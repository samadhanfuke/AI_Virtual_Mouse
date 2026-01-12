# AI Virtual Mouse

A real-time AI Virtual Mouse system that allows you to control the mouse cursor and perform clicks using eye movements and blink gestures. This project uses **OpenCV**, **MediaPipe** (Tasks API), and **PyAutoGUI**.

## Features

- **Real-time Eye Tracking**: Controls mouse cursor using iris/face position.
    - **Cursor Control**: Move your head/eyes to move the cursor. The system maps your face position to the screen active zone.
- **Blink Detection**:
    - **Left Eye Blink** → **Left Click**
    - **Right Eye Blink** → **Right Click**
- **Smooth Movement**: Uses moving average smoothing for stable cursor control.
- **Visual Feedback**: Displays FPS, eye landmarks, and iris tracking on the camera feed.
- **Fail-Safe**: Move mouse to any corner to instantly stop the program.

## Technology Stack

- **Python 3.x**
- **OpenCV** (Video processing)
- **MediaPipe** (Face & Iris landmark detection via Tasks API)
- **PyAutoGUI** (Mouse control)
- **NumPy** (Mathematical operations)

## Installation

1.  **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd AI_Virtual_Mouse
    ```

2.  **Install Dependencies**
    Ensure you have Python installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Model File**
    The project requires `face_landmarker.task`.
    - This file is included in the repository.
    - If missing, run `python download_model.py` to fetch it.

## Usage

1.  **Run the Application**
    ```bash
    python main.py
    ```

2.  **Controls**
    - **Navigation**: The camera feed is **mirrored** for natural interaction. Move your head Left/Right/Up/Down to move the cursor accordingly.
    - **Clicking**:
        - **Blink Left Eye**: Performs a Left Mouse Click.
        - **Blink Right Eye**: Performs a Right Mouse Click.
    - **Exit**: Press `q` on your keyboard while the camera window is focused.

## Configuration (`config.py`)

You can tune the system performance in `config.py`:

- **`BLINK_THRESHOLD`**: Adjust sensitivity of blinking (Default: `0.14`). Lower this if you get random clicks; Raise it if clicks aren't registering.
- **`SMOOTHING_FACTOR`**: Controls cursor lag vs. smoothness (Default: `5`).
- **`MOUSE_SENSITIVITY`**: Multiplier for cursor range.
- **`CAMERA_INDEX`**: Change if using an external webcam.

## Troubleshooting

- **Cursor drifting / Jittery**: Increase `SMOOTHING_FACTOR` in `config.py`.
- **Clicks not working**: Ensure lighting is good. Adjust `BLINK_THRESHOLD`.
- **Crash with "FailSafeException"**: This is intentional. You moved the mouse to a corner. Restart the script.
- **MediaPipe Error**: Ensure `face_landmarker.task` is present in the project folder.

## License
This project is open-source. Feel free to modify and improve!
