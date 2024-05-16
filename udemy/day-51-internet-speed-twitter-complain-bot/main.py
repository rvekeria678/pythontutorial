from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from dotenv import load_dotenv
from config.internet_speeds import PROMISED_DOWN, PROMISED_UP
from config.chrome import CHROME_DRIVER_PATH
import time
import os
load_dotenv()
#-----Constants------#
TWITTER_EMIAL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
WEBSPEEDTEST_URL = "https://www.speedtest.net/"
MAX_WAIT = 180
UPLOAD_LOC = (By.CSS_SELECTOR,'.upload-speed')
DOWNLOAD_LOC = (By.CSS_SELECTOR,'.download-speed')
#-----Globals------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(WEBSPEEDTEST_URL)
        self.driver.find_element(by=By.CLASS_NAME, value="start-text").click()
        #-----Wait for Test to Finish------#
        try:
            WebDriverWait(self.driver, MAX_WAIT).until(
                EC.text_to_be_present_in_element(DOWNLOAD_LOC,'')
            )
            print("Speed Calculation Successful")
        except Exception as e:
            print(f"Error Occurred: {e}")
        finally:
            #-----Retrieve Up/Down Speed Data-----#
            self.down = self.driver.find_element(*DOWNLOAD_LOC)
            self.up = self.driver.find_element(*UPLOAD_LOC)
            
            print(f"Upload Speeds: {self.up.text}")
            print(f"Download Speeds: {self.down.text}")
            
            self.driver.quit()
    def tweet_at_provider():
        pass
        
#-----Program Logic-----#
handler = InternetSpeedTwitterBot()
handler.get_internet_speed()


