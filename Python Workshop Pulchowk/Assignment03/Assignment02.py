'''

Assignment 2:
Download the images from google as we did today(take video reference).But instead of typing the name of what to search directly, your program should take input from the user
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe") #Runs the driver
driver.get(rf"https://images.google.com/?gws_rd=ssl") #Load the provided url

search_box = driver.find_element_by_xpath(rf'//*[@id="sbtc"]/div/div[2]/input')  #Finds the search box of google image search box

images_to_download = input("Images to Download: ") #Taking user input
search_box.send_keys(images_to_download) #Typing the search box
search_box.send_keys([Keys.ENTER]) #Press enter so the google will search the images

height_of_loaded_webpage = driver.execute_script('return document.body.scrollHeight') #Finds the height of webpage loaded


#Below loop to  scroll the page
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height_of_web_page = driver.execute_script(
        'return document.body.scrollHeight')
    print(f"New: {new_height_of_web_page}")
    if new_height_of_web_page == height_of_loaded_webpage:
        break
    height_of_loaded_webpage = new_height_of_web_page
    print(f"Height= {height_of_loaded_webpage}")



for i in range(1,15):
    try:
        driver.find_element_by_xpath(rf'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img').screenshot(f"{images_to_download}{i}.png")
    except:
        pass
        time.sleep(10)


