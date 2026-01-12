import cv2
import mediapipe as mp
import numpy as np

class EyeTracker:
    def __init__(self, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=refine_landmarks,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
    
    def process_frame(self, frame):
        """
        Processes the frame to detect face landmarks.
        Returns the processing result (which contains multi_face_landmarks).
        """
        # MediaPipe requires RGB images
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False # Improve performance
        results = self.face_mesh.process(rgb_frame)
        rgb_frame.flags.writeable = True
        
        return results

    def get_landmark_coords(self, landmarks, frame_w, frame_h, indices):
        """
        Extracts specific landmark coordinates (x, y) for given indices.
        Returns a list of (x, y) tuples.
        """
        coords = []
        for idx in indices:
            lm = landmarks.landmark[idx]
            x, y = int(lm.x * frame_w), int(lm.y * frame_h)
            coords.append((x, y))
        return coords
