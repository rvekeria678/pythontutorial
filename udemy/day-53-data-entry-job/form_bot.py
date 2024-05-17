from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv
import os
load_dotenv()
#-----Constants------#
ADDR_INPUT_XPATH = (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
RENT_INPUT_XPATH = (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
LINK_INPUT_XPATH = (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
SBMT_BUTTON_XPATH = (By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
ANTR_BUTTON_LITE = (By.LINK_TEXT, "Submit another response")
MAX_WAIT = 10
#-----Globals------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

class FormBot:
    def __init__(self, url: str) -> None:
        self.url = url
        self.driver = webdriver.Chrome(options=chrome_options)

    def add_data(self, data: list) -> None:
        self.driver.get(self.url)
        for entry in data:    
            try:
                WebDriverWait(self.driver, MAX_WAIT).until(
                    EC.element_to_be_clickable(SBMT_BUTTON_XPATH)
                )
            except Exception as e:
                print(f"Form Error: {e}")
            finally:
                addr_input = self.driver.find_element(*ADDR_INPUT_XPATH)
                addr_input.send_keys(entry["property_addr"])

                rent_input = self.driver.find_element(*RENT_INPUT_XPATH)
                rent_input.send_keys(entry["monthly_rent"])

                link_input = self.driver.find_element(*LINK_INPUT_XPATH)
                link_input.send_keys(entry["link"])
        
                self.driver.find_element(*SBMT_BUTTON_XPATH).click()
            try:
                WebDriverWait(self.driver, MAX_WAIT).until(
                    EC.element_to_be_clickable(ANTR_BUTTON_LITE)
                )
            except Exception as e:
                print(f"Failed to add another entry. Error: {e}")
            finally:
                self.driver.find_element(*ANTR_BUTTON_LITE).click()
                self.driver.close()