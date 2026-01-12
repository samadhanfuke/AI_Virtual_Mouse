import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os

class EyeTracker:
    def __init__(self, model_path='face_landmarker.task'):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file {model_path} not found. Please run download_model.py.")

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=False,
            output_facial_transformation_matrixes=False,
            num_faces=1,
            running_mode=vision.RunningMode.VIDEO)
        
        self.detector = vision.FaceLandmarker.create_from_options(options)
    
    def process_frame(self, frame, timestamp_ms):
        """
        Processes the frame to detect face landmarks.
        frame: numpy array (BGR)
        timestamp_ms: int, timestamp in milliseconds
        Returns the detection result.
        """
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Create MP Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        # Detect
        result = self.detector.detect_for_video(mp_image, timestamp_ms)
        
        return result

    def get_landmark_coords(self, landmarks_list, frame_w, frame_h, indices):
        """
        Extracts specific landmark coordinates (x, y) for given indices.
        landmarks_list: a list of NormalizedLandmark objects (for one face)
        """
        coords = []
        for idx in indices:
            if idx < len(landmarks_list):
                lm = landmarks_list[idx]
                x, y = int(lm.x * frame_w), int(lm.y * frame_h)
                coords.append((x, y))
        return coords
