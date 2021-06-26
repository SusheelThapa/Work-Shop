'''
Optional Assignment 1:
Use pyautogui to subscribe our channel(bit.ly/yt-pdsc)
Hint: In cmd type py(python will start) and then import pyautogui and type pyautogui.displayMousePosition.That way you can see the real time position of the mouse.
Use that and open the browser and use typewrite to enter the above url of our channel and then subscribe.

'''
import pyautogui
import time

'''Position of my minimize button of vscode (x=1782, y=6)'''
pyautogui.moveTo(x=1782, y=6, duration=2)
pyautogui.click()

'''Position of my brower in desktop of vscode (x=998, y=39)'''
pyautogui.moveTo(x=998, y=39, duration=2)
pyautogui.doubleClick()
time.sleep(10)

'''Typing in browser'''
pyautogui.typewrite(
    "https://www.youtube.com/channel/UCtBAL5IGsN6Hyk_deE2BQOw", interval=0.25)
pyautogui.press('enter')
time.sleep(5)

'''Position of Subscribe Button : (1704,343)'''
pyautogui.moveTo(x=1721, y=503, duration=1)
pyautogui.click()


