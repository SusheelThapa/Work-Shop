from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("chromedriver.exe")  # Run the chrome driver
'''
    Below link for setting up driver in path

    https://cppsecrets.com/users/11429798104105115104101107117115104119971049754494864103109971051084699111109/Python-chromedriver-executable-needs-to-be-in-PATH.php#:~:text=Python%20%27chromedriver%27%20executable%20needs%20to%20be%20in%20PATH,need%20to%20install%20Chromedriver%20and%20set%20the%20path.

    '''

# Open the provided link in opened driver
driver.get('https://images.google.com/imghp?hl=en&gl=ar&gws_rd=ssl')


'''
    X path of google image search box

    //*[@id="sbtc"]/div/div[2]/input
    '''
search_box = driver.find_element_by_xpath(
    rf'//*[@id="sbtc"]/div/div[2]/input')  # Find the element in provided x path and store in search_box

search_box.send_keys("Earth from space")  # Type this alphabet

search_box.send_keys(Keys.ENTER)  # Press the enter key


# Below code scroll over the webpade
height_of_webpage_loaded = driver.execute_script(
    'return document.body.scrollHeight')

print(height_of_webpage_loaded)

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height_of_webpage_loaded = driver.execute_script(
        'return document.body.scrollHeight')
    print(new_height_of_webpage_loaded)
    if new_height_of_webpage_loaded == height_of_webpage_loaded:
        break
    height_of_webpage_loaded = new_height_of_webpage_loaded
'''
    Refer below link 

    https://www.geeksforgeeks.org/execute_script-driver-method-selenium-python/
    '''


# Downloading images
'''
    X Path of two image side by side 
    //*[@id = "islrg"]/div[1]/div[1]/a[1]/div[1]/img
    //*[@id = "islrg"]/div[1]/div[2]/a[1]/div[1]/img

    Diffrence is seen in Left div of a as first element corespond to 1 and second element to 2 and goes on like this
    '''
for i in range(1, 100):
    try:
        # Screenshot image should be png
        driver.find_element_by_xpath(
            rf'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img').screenshot(f"Earth{i}.png")
        '''
            .screenshot({name of image}) will take the screenshot of image present in provided x path and download it as provided file name
            '''
    except:
        pass
