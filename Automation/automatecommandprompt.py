import os
import pyautogui
import intervals
import time
import webbrowser
import datetime
from datetime import datetime

#search = pyautogui.locateCenterOnScreen('search.png')
#pyautogui.click()
#pyautogui.write('cmd', interval=0.25)
#pyautogui.press('enter')
os.system("start cmd")
time.sleep(1)
#pyautogui.write('cd Desktop', interval=1)
#pyautogui.press('enter')
#pyautogui.write('cd Automation', interval=1)
#pyautogui.press('enter')
pyautogui.write('python automateteams.py', interval=0.1)
pyautogui.press('enter')
