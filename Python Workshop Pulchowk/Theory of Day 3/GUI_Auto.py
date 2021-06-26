'''
OFFICIAL DOCUMENTATION LINK FOR PYAUTOGUI

https://pyautogui.readthedocs.io/en/latest/index.html

'''

import pyautogui
import time

# size_of_screen = pyautogui.size()  #Return the size of your screenpy

# # pyautogui.moveTo(100,1000, duration=0) #Move the mouse to the coordinate provided in 5 second. If no duration is set it take 0 as value

# '''Comment above line to find the different position of mouse as above piece of code bring the mouse to 100,1000 and below pyautogui.position() you give u same result till you comment above line'''
# position_of_mouse = pyautogui.position()  #Return the coordinate of the position of mouse
# print(position_of_mouse) #Print the position of mouse


# pyautogui.moveRel(500,-100, duration=0) #It is just traslation of mouse by 500 left and 100 down in 1 second if no duration is given it is set to 0


# '''
# In my vs code coordination of extension tab is (x=25, y=329) -->Taken with the help of pyautogui.position()
# '''
# #Move the cursor to the respective postition
# pyautogui.moveTo(25,329,duration = 3)
# # A click where the mouse is
# pyautogui.click()  #In my case it should open the extension tab as i have moved the mouse to extension and clicked there

'''
Coordinate of extension in vs code (x=25, y=329)
'''
pyautogui.moveTo(25, 329)  # Moves the cursor into search bar
pyautogui.click() #Click on it
pyautogui.typewrite("Python MicroSoft") #Type on it
pyautogui.typewrite(['Enter'])  #Press enter
time.sleep(2)  #Freeze the program so that you can see the effect
pyautogui.click() #Click on it to close the tab

