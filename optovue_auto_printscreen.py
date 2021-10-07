""" 
OptoVue - Optical Coherance Tomography imaging station

This script automates the tedius task of saving each slice of a 304-slice volume
PyAutoGui allows for the selection of specific regions on-screen, combined with mouse strokes & keyboard combinations

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

time.sleep(2)                           # Time to click on the screen, so that the "Down" command works to move the B-Scan slider
for i in range(3):                        # number of b-scans per volume
                             
    im = pyautogui.screenshot()
    im.save('vol1_' + str(i) + '.png')
    time.sleep(.5)                          # a little time for the OS to open the image for confirmation
    pyautogui.press('f2')
    time.sleep(.2)
    pyautogui.press('down')
    pyautogui.sleep(.05)