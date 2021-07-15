import os
import pyautogui
import intervals
import time
import webbrowser
import datetime
from datetime import datetime

def join():
    time.sleep(4)
    meet = pyautogui.locateCenterOnScreen('join.png', grayscale=False )
    if meet is not None:
        pyautogui.moveTo(meet)
        pyautogui.click()
        time.sleep(2)
        joinnow = pyautogui.locateCenterOnScreen('joinnow.png')
        pyautogui.press('enter')
    else:
        pyautogui.alert('Meeting not yet started')

def navigate():
    #teams = pyautogui.locateCenterOnScreen('app.png')
    #pyautogui.moveTo(teams)
    #pyautogui.doubleClick()
    webbrowser.open('teams.microsoft.com')
    time.sleep(10)
    Teams = pyautogui.locateCenterOnScreen('teams1.png', grayscale=False)
    if Teams is None:
        Teams = pyautogui.locateCenterOnScreen('teams2.png', grayscale=False)
    pyautogui.moveTo(Teams)
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

def maths():
    navigate()
    meet = pyautogui.locateCenterOnScreen('maths.png')
    pyautogui.moveTo(meet)
    pyautogui.click()
    join()

def advertising():
    navigate()
    meet = pyautogui.locateCenterOnScreen('advertising.png')
    pyautogui.moveTo(meet)
    pyautogui.click()
    join()

def dbs():
    navigate()
    meet = pyautogui.locateCenterOnScreen('dbs.png')
    pyautogui.moveTo(meet)
    pyautogui.click()
    join()

def daa():
    navigate()
    meet = pyautogui.locateCenterOnScreen('daa.png')
    pyautogui.moveTo(meet)
    pyautogui.click()
    join()

def flat():
    navigate()
    meet = pyautogui.locateCenterOnScreen('flat.png')
    pyautogui.moveTo(meet)
    pyautogui.click()
    join()

def es():
    navigate()
    meet = pyautogui.locateCenterOnScreen('es1.png')
    pyautogui.moveTo(meet)
    pyautogui.click()
    time.sleep(1)
    meet2 = pyautogui.locateCenterOnScreen('es2.png')
    pyautogui.moveTo(meet2)
    print(meet)
    print(meet2)
    time.sleep(1)
    pyautogui.click()
    join()

screenWidth, screenHeight = pyautogui.size()
mouseX, mouseY = pyautogui.position()

timenow = datetime.now()
day = timenow.strftime("%A")
hour = int(time.strftime("%H"))

if day == 'Monday':
    if hour >=7 and hour <= 9:
        maths()
    elif hour >9 and hour <= 11:
        flat()
    elif hour >= 12:
        pyautogui.alert('Todays classes are completed')

elif day == 'Tuesday':
    if hour >=13 and hour <= 15:
        dbs()
    elif hour >15 and hour <= 17:
        daa()
    elif hour >= 18:
        pyautogui.alert('Todays classes are completed')

elif day == 'Wednesday':
    if hour >=7 and hour <= 9:
        es()
    elif hour >9 and hour <= 11:
        advertising()
    elif hour >= 12:
        pyautogui.alert('Todays classes are completed')

elif day == 'Thursday':
    if hour >=13 and hour <= 15:
        maths()
    elif hour >15 and hour <= 17:
        flat()
    elif hour >= 18:
        pyautogui.alert('Todays classes are completed')

elif day == 'Friday':
    if hour >=7 and hour <= 9:
        dbs()
    elif hour >9 and hour <= 11:
        es()
    elif hour >= 12:
        pyautogui.alert('Todays classes are completed')

elif day == 'Saturday':
    if hour >=13 and hour <= 15:
        daa()
    elif hour >15 and hour <= 17:
        advertising()
    elif hour >= 18:
        pyautogui.alert('Todays classes are completed')

elif day == 'Sunday':
    pyautogui.alert('Today is a Holiday')
