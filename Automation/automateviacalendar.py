import os
import pyautogui
import intervals
import time
import webbrowser
import datetime
from datetime import datetime

def navigate():
    webbrowser.open('teams.microsoft.com')
    time.sleep(10)
    Teams = pyautogui.locateCenterOnScreen('calendar1.png', grayscale=False)
    if Teams is None:
        Teams = pyautogui.locateCenterOnScreen('calendar2.png', grayscale=False)
    pyautogui.moveTo(Teams)
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(4)

def join():
    calendarjoin = pyautogui.locateCenterOnScreen('join2.png', grayscale=False)
    if calendarjoin is None:
        pyautogui.alert('Meeting not yet started')
    else:
        pyautogui.moveTo(calendarjoin)
        pyautogui.click()
        time.sleep(2)
        joinnow = pyautogui.locateCenterOnScreen('joinnow.png')
        pyautogui.moveTo(joinnow)
        pyautogui.press('enter')

navigate()
join()
