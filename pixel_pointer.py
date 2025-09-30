import pyautogui
import time

print("Move your mouse to the top-left and bottom-right of each browser window...")
for _ in range(20):
    print(pyautogui.position())
    time.sleep(2)
