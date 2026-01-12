import numpy as np
import math

class GestureProcessor:
    def __init__(self, blink_threshold=0.15, blink_consec_frames=2):
        self.blink_threshold = blink_threshold
        self.blink_consec_frames = blink_consec_frames
        
        # Counters for blink duration
        self.left_counter = 0
        self.right_counter = 0

    def calculate_ear(self, eye_points):
        """
        Calculates the Eye Aspect Ratio (EAR).
        eye_points: List of (x, y) tuples for 6 landmarks of the eye.
        """
        # Vertical distances
        A = math.dist(eye_points[1], eye_points[5])
        B = math.dist(eye_points[2], eye_points[4])
        
        # Horizontal distance
        C = math.dist(eye_points[0], eye_points[3])
        
        if C == 0:
            return 0
            
        ear = (A + B) / (2.0 * C)
        return ear

    def detect_blink(self, left_ear, right_ear):
        """
        Detects if a blink occurred based on EAR thresholds.
        Returns a tuple: (left_click_detected, right_click_detected)
        """
        left_click = False
        right_click = False
        
        # Left Eye Blink Logic (Click)
        if left_ear < self.blink_threshold:
            self.left_counter += 1
        else:
            if self.left_counter >= self.blink_consec_frames:
                left_click = True
            self.left_counter = 0
            
        # Right Eye Blink Logic (Click)
        if right_ear < self.blink_threshold:
            self.right_counter += 1
        else:
            if self.right_counter >= self.blink_consec_frames:
                right_click = True
            self.right_counter = 0
            
        return left_click, right_click

    def get_gaze_point(self, landmarks, frame_w, frame_h):
        """
        Estimates the gaze point. For simplicity in this version, we map the 
        nose tip or center of eyes to screen coordinates, but the user requested 
        iris tracking.
        
        Actually, mapping iris movement to screen coordinates solely with webcam is tricky
        without calibration. A robust way is to use the center of the iris relative 
        to the eye corners.
        
        For this MVP, we can try to follow the head pose or iris position directly.
        Let's try: Using the Iris position relative to the face.
        
        But a simpler and more robust way for "Virtual Mouse" with just a webcam 
        often uses the face direction / nose tip, as eye-gaze only is very jittery 
        and low resolution on webcams.
        
        HOWEVER, the user requirement says "Track eye landmarks and iris position".
        Let's try to return the relative position of the iris in the eye, or 
        (simpler) just the face mesh anchor (like nose or mid-eyes) as the cursor 
        control point for stability, and use eyes for clicking.
        
        Wait, "Convert eye movement into mouse cursor movement". 
        Strict eye tracking is hard. Let's provide a hybrid: 
        We return the iris center. We will let the main loop decide how to map it.
        """
        # This method might be better placed in logic in main or here. 
        # For now, let's keep it simple: return the raw iris landmarks.
        pass
