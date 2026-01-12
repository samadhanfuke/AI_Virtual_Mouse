import cv2
import time
import numpy as np

import config
from src.camera_manager import CameraManager
from src.eye_tracker import EyeTracker
from src.gesture_processor import GestureProcessor
from src.cursor_controller import CursorController

def main():
    # Initialize modules
    cam = CameraManager(config.CAMERA_INDEX, config.FRAME_WIDTH, config.FRAME_HEIGHT)
    eye_tracker = EyeTracker(
        refine_landmarks=config.REFINE_LANDMARKS,
        min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE
    )
    gesture_proc = GestureProcessor(
        blink_threshold=config.BLINK_THRESHOLD,
        blink_consec_frames=config.BLINK_CONSEC_FRAMES
    )
    cursor_ctrl = CursorController(smoothing_factor=config.SMOOTHING_FACTOR)

    print("AI Virtual Mouse Started.")
    print("Press 'q' to exit. Move mouse to corner to failsafe quit.")

    prev_time = 0
    
    try:
        while True:
            frame = cam.read_frame()
            if frame is None:
                break
            
            frame_h, frame_w, _ = frame.shape
            
            # Process Frame
            results = eye_tracker.process_frame(frame)
            
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    # Draw Mesh (Optional, might be too heavy, let's just draw eyes)
                    # mp.solutions.drawing_utils.draw_landmarks(...)
                    
                    # 1. Get Eye Landmarks
                    left_eye_pts = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.LEFT_EYE)
                    right_eye_pts = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.RIGHT_EYE)
                    
                    # 2. Blink Detection (Clicking)
                    left_ear = gesture_proc.calculate_ear(left_eye_pts)
                    right_ear = gesture_proc.calculate_ear(right_eye_pts)
                    
                    left_click, right_click = gesture_proc.detect_blink(left_ear, right_ear)
                    
                    if left_click:
                        print("Left Click")
                        cursor_ctrl.click('left')
                    if right_click:
                        print("Right Click")
                        cursor_ctrl.click('right')
                        
                    # 3. Mouse Movement (Gaze / Head Tracking)
                    # Requirement: "Convert eye movement into mouse cursor movement"
                    # We will use the center of the orbital landmarks or Iris if available.
                    # MediaPipe Iris landmarks: 468-477. Refined landmarks required.
                    # config.LEFT_IRIS -> indices
                    
                    left_iris = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.LEFT_IRIS)
                    right_iris = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.RIGHT_IRIS)
                    
                    if left_iris: # Valid iris detection
                        # Calculate centroid of left iris
                        lx = np.mean([p[0] for p in left_iris])
                        ly = np.mean([p[1] for p in left_iris])
                        
                        # We use the Left Eye Iris to control the mouse (or average of both)
                        # To make it usable, we map a smaller region of the camera to the full screen
                        # This "active region" avoids looking at extreme corners
                        
                        # Define Active Region (rectangle in center of frame)
                        # We can use the eye corners to define the bounding box dynamically, 
                        # but static frame-relative logic is more stable for "Head+Eye" combo movement.
                        # Wait, pure Eye tracking usually needs calibration.
                        # Implementation Trick: Use Face direction (Head) for coarse, Eye for fine?
                        # Let's stick to the prompt: "Convert eye movement". 
                        # We'll map the Iris position *relative to the Eye Corners*.
                        # BUT, that is very high sensitivity. 
                        
                        # Simpler approach: Map the raw Iris coordinate (which moves with head + eye) to screen.
                        # This acts more like a Head Pointer if you keep eyes centered, giving good control.
                        
                        # Active zone normalized (e.g., center 50% of screen)
                        # This allows the user to reach edges without breaking their neck/eyes.
                        margin_x = int(frame_w * 0.2)
                        margin_y = int(frame_h * 0.3)
                        
                        # Clamp and Normalize
                        norm_x = np.interp(lx, (margin_x, frame_w - margin_x), (0, 1))
                        norm_y = np.interp(ly, (margin_y, frame_h - margin_y), (0, 1))
                        
                        cursor_ctrl.move_cursor(norm_x, norm_y)
                    
                    # Visual Feedback
                    # Draw Eye Contours
                    cv2.polylines(frame, [np.array(left_eye_pts)], True, config.COLOR_EYE, 1)
                    cv2.polylines(frame, [np.array(right_eye_pts)], True, config.COLOR_EYE, 1)
                    # Draw Iris
                    if left_iris:
                         cv2.circle(frame, (int(np.mean([p[0] for p in left_iris])), int(np.mean([p[1] for p in left_iris]))), 2, config.COLOR_IRIS, -1)

            # FPS Calculation
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time
            cv2.putText(frame, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            
            # Show Frame
            cv2.imshow('AI Virtual Mouse', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
