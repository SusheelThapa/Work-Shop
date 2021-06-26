'''

Optional Assignment 2:
In selenium automation we scroll up to some limitation. After scrolling down the google will show 'show more' option. Figure out the way to click show more and then continue to scroll down again.
Hint: Use 'find_element_by_xpath' .


'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")  # Runs the driver
driver.get(rf"https://images.google.com/?gws_rd=ssl")  # Load the provided url

search_box = driver.find_element_by_xpath(rf'//*[@id="sbtc"]/div/div[2]/input')

images_to_download = input("Images to Download: ")
search_box.send_keys(images_to_download)  # Typing the search box
# Press enter so the google will search the images
search_box.send_keys([Keys.ENTER])

height_of_loaded_webpage = driver.execute_script(
    'return document.body.scrollHeight')

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    new_height_of_web_page = driver.execute_script(
        'return document.body.scrollHeight')
    print(f"New: {new_height_of_web_page}")
    if new_height_of_web_page == height_of_loaded_webpage:
        try:
            more_result = driver.find_element_by_xpath(
                '//*[@id="islmp"]/div/div/div/div/div[2]/div[2]/input')
            more_result.send_keys(Keys.ENTER)

        except:
            break
    height_of_loaded_webpage = new_height_of_web_page
    print(f"Height= {height_of_loaded_webpage}")


for i in range(1, 5):
    try:
        driver.find_element_by_xpath(
            rf'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img').screenshot(f"{images_to_download}{i}.png")
    except:
        pass
        time.sleep(2)
