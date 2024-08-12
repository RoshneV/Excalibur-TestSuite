from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import pprint 
import time
# import db
import random
import pyautogui
import os
# import chromedriver_autoinstaller

# os.environ['DISPLAY'] = ':0' 
# print(pyautogui.size())
def run():
    '''
    web driver = false
    user agent - platform match 
    score>90(bot = true)
    '''
    # print("bad_finger")
    options = webdriver.ChromeOptions()
    #maximizes screen
    options.add_argument("start-maximized")

    # automatically opens devtools
    options.add_argument("--auto-open-devtools-for-tabs")
    # chromedriver_autoinstaller.install()
    bypass_webdriver_detection(options)
    
    change_ua_in_js_and_header(options)
    
    browser = webdriver.Chrome(options )
    action = webdriver.ActionChains(browser)
    # browser.get('https://fingerprintjs.github.io/BotD/main/')
    browser.get('https://excaliber.in/')
    js=change_platform_in_js()
    browser.execute_script(js)

    
    mse_score_greater_than_90(browser,action)
    
def bypass_webdriver_detection(options):
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    
# 1 c) js user agent - browser header user agent mismatch
def change_ua_in_js_and_header(options):
    my_user_agent = "BYPASS - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    options.add_argument(f"--user-agent={my_user_agent}")

def change_platform_in_js():
    javascript_code = """
    Object.defineProperty(navigator, 'platform', {
    get: function() {
        return 'Win64';
    }
    });
    """
    return javascript_code
def mse_score_greater_than_90(browser,action):
    userNameInputBox = browser.find_element(By.ID,"username")
    passwordInputBox = browser.find_element(By.ID,"password")
    loginButton = browser.find_element(By.ID,"loginbtn")
    userNameInputBox.send_keys("Testing bot")
    passwordInputBox.send_keys("password")
    screen_width, screen_height = pyautogui.size()
    n=random.randint(0,10)
    for i in range(n):
        x=random.randint(0,screen_width-1)
        y=random.randint(0,screen_height-1)
        pyautogui.moveTo(x,y, duration = 0.01)
    time.sleep(2)
    loginButton.click()
    time.sleep(5)
