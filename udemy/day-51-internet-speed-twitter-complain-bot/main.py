from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pprint import pprint
from dotenv import load_dotenv
from config.internet_speeds import PROMISED_DOWN, PROMISED_UP
from config.chrome import CHROME_DRIVER_PATH
import time
import os
load_dotenv()
#-----Constants------#
TWITTER_URL = ""
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
        self.get_internet_speed()

    def get_internet_speed(self) -> None:
        self.driver.get(WEBSPEEDTEST_URL)
        self.driver.find_element(by=By.CLASS_NAME, value="start-text").click()
        #-----Wait for Test to Finish------#
        try:
            WebDriverWait(self.driver, MAX_WAIT).until(
                lambda driver: driver.find_element(*UPLOAD_LOC).get_attribute("data-upload-status-value") != "NaN"
            )
            print("Speed Calculation Successful")
        except Exception as e:
            print(f"Error Occurred: {e}")
        finally:
            #-----Retrieve Up/Down Speed Data-----#
            try:
                self.down = self.driver.find_element(*DOWNLOAD_LOC).text
                self.up = self.driver.find_element(*UPLOAD_LOC).text
                            
                if not self.down or not self.up:
                    raise NoSuchElementException
            except NoSuchElementException as e:
                print(f"Failed to retrieve upload/download speed data: {e}")
            finally:
                self.down = float(self.down)
                self.up = float(self.up)
                self.driver.quit()
                
    def tweet_at_provider(self, promised_up: float, promised_down: float) -> None:
        if self.down and self.up:
            if self.down < promised_down or self.up < promised_up:
                msg = f"Het Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?"
                self.driver.get(TWITTER_URL)
        
#-----Program Logic-----#
my_bot = InternetSpeedTwitterBot()
my_bot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP)