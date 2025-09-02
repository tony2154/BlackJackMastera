import pyautogui
import cv2
import numpy as np
from config import GAME_REGION

def capture_table():
    """Captura la región definida en config.GAME_REGION y devuelve BGR (OpenCV)."""
    x, y, w, h = GAME_REGION
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame
