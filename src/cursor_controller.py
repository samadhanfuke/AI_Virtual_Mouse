import pyautogui
import numpy as np

class CursorController:
    def __init__(self, smoothing_factor=5):
        self.screen_w, self.screen_h = pyautogui.size()
        self.smoothing_factor = smoothing_factor
        
        # Smoothing buffers
        self.prev_x, self.prev_y = 0, 0
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0
        
        # Fail-safe (move mouse to corner to stop)
        pyautogui.FAILSAFE = True

    def move_cursor(self, x, y):
        """
        Moves the cursor to (x, y) coordinates with smoothing.
        x and y should be normalized coordinates [0, 1] relative to the frame.
        """
        # Map normalized coordinates to screen dimensions
        target_x = np.interp(x, (0, 1), (0, self.screen_w))
        target_y = np.interp(y, (0, 1), (0, self.screen_h))

        # Smoothing logic (Exponential Moving Average-ish / Linear interpolation)
        # Using the logic: current_loc = prev_loc + (target - prev_loc) / smoothing
        # This acts like a low-pass filter to reduce jitter
        
        self.clocX = self.plocX + (target_x - self.plocX) / self.smoothing_factor
        self.clocY = self.plocY + (target_y - self.plocY) / self.smoothing_factor
        
        try:
            pyautogui.moveTo(self.clocX, self.clocY)
        except pyautogui.FailSafeException:
            pass # FailSafe triggered, let the main loop handle exit if needed
            
        self.plocX, self.plocY = self.clocX, self.clocY

    def click(self, button='left'):
        """Performs a mouse click."""
        pyautogui.click(button=button)

    def scroll(self, clicks):
        """Scrolls the mouse wheel."""
        pyautogui.scroll(clicks)
