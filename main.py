import pyautogui
import pytesseract
import time

import masonConstents as c
# import maxConstents as c

def capture_screen(region):
    return pyautogui.screenshot(region=region)

def solve_current_question():
    ss = capture_screen(c.Region1)
    ss.save("screenshot.png")
    textToType = pytesseract.image_to_string(ss)
    pyautogui.write(textToType)

while True:
    # pyautogui.displayMousePosition()
    solve_current_question()

