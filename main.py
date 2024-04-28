import pyautogui
import pytesseract
import time
import random
import numpy as np

import masonConstents as c
# import maxConstents as c

custom_config = r'--oem 1 --psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz'

def capture_screen(region):
    return pyautogui.screenshot(region=region)

def compare_images(img1, img2):
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    if np.array_equal(arr1, arr2):
        return True
    else:
        return False

def solve_current_question():
    ss = capture_screen(c.Region1).convert('L')
    ss.save("ss.png")
    oldSS.save("oldSS.png")
    if (not(compare_images(oldSS, ss))):
        textToType = pytesseract.image_to_string(ss, config=custom_config)
        print(textToType)
        pyautogui.typewrite(textToType, interval=0.0125)
        time.sleep(0.1)
        oldSS == ss
oldSS = capture_screen(c.Region1).convert('L')

while True:
    # pyautogui.displayMousePosition()
    solve_current_question()