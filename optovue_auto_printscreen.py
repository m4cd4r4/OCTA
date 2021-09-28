"""
Prerequisites:
pip install pythonautogui
https://gadwin.com/printscreen/ 

GadWin is free software that enables capture & saving of screenshots in 2 steps:
Step 1 - Press 'PrintScrn'
Step 2 - Press "F2" to confirm

GadWin Options -
Choose TIFF, BMP, JPEG etc

*If screenshots are labelled out of order (For example, 1, 3, 4, 5 ,2 ,6): change File name Template to "Screen Shot"

**Recommended - Run from Python IDLE, move IDLE until only the toolbar is visible at the bottom of the screen, then press "F5" to run the script
"""

import time
import pyautogui

for i in range(304):                        # number of b-scans per volume
    time.sleep(2)                           # time to minimise any pop-ups & to click near the b-scan scroll bar
    pyautogui.press('printscreen')
    time.sleep(.5)                          # a little time for the OS to open the image for confirmation
    pyautogui.press('f2')
    time.sleep(.2)
    pyautogui.press('down')
    pyautogui.sleep(.05)