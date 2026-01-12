import cv2

# Camera Settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Eye Tracking Settings (Model path)
MODEL_PATH = "face_landmarker.task"

# Gesture thresholds
# Eye Aspect Ratio (EAR) - Threshold to determine if eye is closed
BLINK_THRESHOLD = 0.14  # Adjust based on testing
BLINK_CONSEC_FRAMES = 2 # Number of frames to confirm a blink (debounce)

# Cursor Control
SMOOTHING_FACTOR = 5  # Higher = smoother but more lag (moving average buffer size)
MOUSE_SENSITIVITY = 1.5 # Multiplier for mouse movement range

# Landmark Indices (MediaPipe Face Mesh 478 landmarks)
# Left Eye
LEFT_EYE = [362, 385, 387, 263, 373, 380]
LEFT_IRIS = [474, 475, 476, 477]

# Right Eye
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_IRIS = [469, 470, 471, 472]

# Colors for drawing
COLOR_IRIS = (0, 255, 0)
COLOR_EYE = (0, 255, 255)
COLOR_TEXT = (0, 0, 255)
