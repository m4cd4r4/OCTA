""" 
OptoVue - Optical Coherance Tomography image acquisition machine

This script automates the tedius task of saving each slice of a 304-slice volume
PyAutoGui allows for the selection of specific regions on-screen, combined with mouse strokes & keyboard combinations

Prerequisites:
pip install pythonautogui

**Recommended - Run from Python IDLE, move IDLE until only the toolbar is visible at the bottom of the screen, then press "F5" to run the script

v1.1 - Replaced "GadWin" with pyautogui's built-in screenshot capability
"""

import time
import pyautogui

time.sleep(2)   # Time to click on the screen, so that the "Down" command is sucessful in moving the B-Scan slider

for i in range(30):                        # number of b-scans per volume                         
    im = pyautogui.screenshot()
    im.save('vol1_' + str(i) + '.png')
    time.sleep(.15)
    pyautogui.press('down')
    pyautogui.sleep(.1)