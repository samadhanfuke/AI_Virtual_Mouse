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
    
    # Initialize EyeTracker with model path
    try:
        eye_tracker = EyeTracker(model_path=config.MODEL_PATH)
    except FileNotFoundError as e:
        print(e)
        return

    gesture_proc = GestureProcessor(
        blink_threshold=config.BLINK_THRESHOLD,
        blink_consec_frames=config.BLINK_CONSEC_FRAMES
    )
    cursor_ctrl = CursorController(smoothing_factor=config.SMOOTHING_FACTOR)

    print("AI Virtual Mouse Started.")
    print("Press 'q' to exit. Move mouse to corner to failsafe quit.")

    prev_time = 0
    start_time_ms = int(time.time() * 1000)
    
    try:
        while True:
            frame = cam.read_frame()
            if frame is None:
                break
            
            frame_h, frame_w, _ = frame.shape
            
            # Timestamp for MediaPipe
            current_time_ms = int(time.time() * 1000)
            
            # Process Frame
            # Note: Timestamp must be monotonically increasing.
            results = eye_tracker.process_frame(frame, current_time_ms)
            
            # Check for landmarks (Tasks API: results.face_landmarks is a list of lists)
            if results.face_landmarks:
                for face_landmarks in results.face_landmarks:
                    # face_landmarks is a list of NormalizedLandmark
                    
                    # 1. Get Eye Landmarks
                    left_eye_pts = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.LEFT_EYE)
                    right_eye_pts = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.RIGHT_EYE)
                    
                    # 2. Blink Detection (Clicking)
                    left_ear = gesture_proc.calculate_ear(left_eye_pts)
                    right_ear = gesture_proc.calculate_ear(right_eye_pts)
                    
                    left_click, right_click = gesture_proc.detect_blink(left_ear, right_ear)
                    
                    if left_click:
                        # In a mirrored frame, MP's "Left Eye" is the User's Right Eye
                        print("Right Click")
                        cursor_ctrl.click('right')
                    if right_click:
                        # In a mirrored frame, MP's "Right Eye" is the User's Left Eye
                        print("Left Click")
                        cursor_ctrl.click('left')
                        
                    # 3. Mouse Movement (Iris Tracking)
                    left_iris = eye_tracker.get_landmark_coords(face_landmarks, frame_w, frame_h, config.LEFT_IRIS)
                    
                    if left_iris:
                         # Calculate centroid of left iris
                        lx = np.mean([p[0] for p in left_iris])
                        ly = np.mean([p[1] for p in left_iris])
                        
                        # Active zone normalized (e.g., center 50% of screen)
                        margin_x = int(frame_w * 0.2)
                        margin_y = int(frame_h * 0.3)
                        
                        # Clamp and Normalize
                        norm_x = np.interp(lx, (margin_x, frame_w - margin_x), (0, 1))
                        norm_y = np.interp(ly, (margin_y, frame_h - margin_y), (0, 1))
                        
                        cursor_ctrl.move_cursor(norm_x, norm_y)
                        
                        # Visual Feedback - Iris
                        cv2.circle(frame, (int(lx), int(ly)), 2, config.COLOR_IRIS, -1)

                    # Visual Feedback - Eyes
                    cv2.polylines(frame, [np.array(left_eye_pts)], True, config.COLOR_EYE, 1)
                    cv2.polylines(frame, [np.array(right_eye_pts)], True, config.COLOR_EYE, 1)

            # FPS Calculation
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
            prev_time = curr_time
            cv2.putText(frame, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            
            # Show Frame
            cv2.imshow('AI Virtual Mouse', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except pyautogui.FailSafeException:
        print("\n[INFO] Fail-safe triggered from mouse moving to a corner. Exiting...")
    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()
    finally:
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
