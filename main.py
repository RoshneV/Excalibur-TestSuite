import time
# import db
# import chromedriver_autoinstaller
import os
import logging
from Bot import fingerprint,UA_platform,web_driver
#log file
# logging.basicConfig(filename='TestSuiteError.log', level=logging.ERROR)

# os.environ['DISPLAY'] = ':0'
# Calling the run function with the browser argument
print("Bot1 started simulating Webdriver")
print("A same mouse movement made with webdriver ON")
time.sleep(1)
web_driver.run()
time.sleep(5)
print("Bot2 started simulating UA_Platform mismatched")
print("Webdriver is set to false")
print("platform - User Agent mismatched ")
print("A small mouse movement is simulated")
time.sleep(1)
UA_platform.run()
time.sleep(5)
print("Bot3 started simulating Bad fingerprint mouse")
print("User Agent - Platform matched")
time.sleep(1)
fingerprint.run()
time.sleep(5)