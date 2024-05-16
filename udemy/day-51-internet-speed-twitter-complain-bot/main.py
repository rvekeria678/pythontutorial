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
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_all_elements_located(by=By.CSS_SELECTOR,value=".download-speed")
            )
            print("Speed Calculation Successful")
        except Exception as e:
            print(f"Error Occurred: {e}")
        finally:
            #-----Retrieve Up/Down Speed Data-----#
            time.sleep(10)
            self.down = float(self.driver.find_element(by=By.CSS_SELECTOR,
                                                       value=".download-speed").text)
            self.up = float(self.driver.find_element(by=By.CSS_SELECTOR,
                                                     value=".upload-speed").text)
            print(f"Upload Speeds: {self.up}")
            print(f"Download Speeds: {self.down}")
            

    def tweet_at_provider():
        pass
        
#-----Program Logic-----#
handler = InternetSpeedTwitterBot()
handler.get_internet_speed()


