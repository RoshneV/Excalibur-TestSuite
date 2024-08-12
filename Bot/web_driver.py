from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import pprint 
import time
# import db
import pyautogui
import os
# import chromedriver_autoinstaller

# os.environ['DISPLAY'] = ':0' 

def run():
    '''
    web driver =  true 
    '''
    # chromedriver_autoinstaller.install()
    # print("hello")
    # options for web driver
    options = webdriver.ChromeOptions()

    #maximizes screen
    options.add_argument("start-maximized")

    # automatically opens devtools
    # options.add_argument("--auto-open-devtools-for-tabs")

    browser = webdriver.Chrome(options )

    browser.get('https://excaliber.in/')
    
    userNameInputBox = browser.find_element(By.ID,"username")
    passwordInputBox = browser.find_element(By.ID,"password")
    loginButton = browser.find_element(By.ID,"loginbtn")

    userNameInputBox.send_keys("Testing bot")
    passwordInputBox.send_keys("password")
    coords=[[482,300,1686508022988,0],[487,297,1686508023005,0],[487,293,1686508023022,0],[488,289,1686508023038,0],[488,288,1686508023055,0],[488,287,1686508023202,0],[488,282,1686508023222,0],[488,281,1686508023239,0],[488,281,1686508023554,1]]
    for i in coords:
        pyautogui.moveTo(i[0],i[1], duration = 0.01)
    time.sleep(2)
    loginButton.click()

    # excalSession = browser.execute_script("return sessionStorage.excalsession ;")
    # print(excalSession)
    # mouse_click_db_botvalue_coll = db.Mongo(databaseName="Mouse_track",collectionName="botvalue")
    # cursor =  mouse_click_db_botvalue_coll.find({"session":f"{excalSession}"}) 
    # dict={}   
    # for i in cursor:
    #     dict.update(i)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dict)
    time.sleep(5)
run()