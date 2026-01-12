import cv2
import sys

class CameraManager:
    def __init__(self, camera_index=0, width=640, height=480):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            print(f"Error: Could not open webcam at index {camera_index}")
            sys.exit(1)
        
        # Set resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
        self.width = width
        self.height = height

    def read_frame(self):
        """Reads a frame from the webcam, flips it horizontally (mirror effect)."""
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            return None
        
        # Mirror the frame
        frame = cv2.flip(frame, 1)
        return frame

    def release(self):
        self.cap.release()
