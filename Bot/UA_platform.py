from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
import pprint 
import time
# import db
import pyautogui
import os
# import chromedriver_autoinstaller

# os.environ['DISPLAY'] = ':0' 
def run():
    '''
    web driver = false
    user agent - platform mismatch (bot = true) 
    '''
    # options for web driver
    options = webdriver.ChromeOptions()
    # chromedriver_autoinstaller.install()
    #maximizes screen
    options.add_argument("start-maximized")

    # automatically opens devtools
    options.add_argument("--auto-open-devtools-for-tabs")
    
    bypass_webdriver_detection(options)
    
    change_ua_in_js_and_header(options)

    browser = webdriver.Chrome(options )

    
    browser.get('https://excaliber.in/')
    
    
    userNameInputBox = browser.find_element(By.ID,"username")
    passwordInputBox = browser.find_element(By.ID,"password")
    loginButton = browser.find_element(By.ID,"loginbtn")

    userNameInputBox.send_keys("Testing bot")
    passwordInputBox.send_keys("password")
    coords=[[545,447,1686494389708,0],[459,448,1686494389724,0],[378,448,1686494389741,0],[318,449,1686494389758,0],[283,455,1686494389774,0],[266,458,1686494389791,0],[261,458,1686494389808,0],[261,464,1686494389828,0],[274,454,1686494390491,0],[286,448,1686494390508,0],[293,444,1686494390524,0],[297,441,1686494390541,0],[297,440,1686494390563,0],[300,440,1686494390575,0],[302,439,1686494390592,0],[303,440,1686494390609,0],[303,443,1686494390675,0],[302,447,1686494390691,0]]
    for i in coords:
        pyautogui.moveTo(i[0],i[1], duration = 0.01)
    time.sleep(2)
    loginButton.click()

    # time.sleep(10)
    # excalSession = browser.execute_script("return sessionStorage.excalsession ;")
    # print(excalSession)
    # mouse_click_db_botvalue_coll = db.Mongo(databaseName="Mouse_track",collectionName="botvalue")
    # cursor =  mouse_click_db_botvalue_coll.find({"session":f"{excalSession}"})    
    # # print(cursor)
    # dict={}   
    # for i in cursor:
    #     dict.update(i)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dict)
    time.sleep(5)
# 1 b) web driver false
def bypass_webdriver_detection(options):
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    
# 1 c) js user agent - browser header user agent mismatch
def change_ua_in_js_and_header(options):
    my_user_agent = "BYPASS - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    options.add_argument(f"--user-agent={my_user_agent}")

