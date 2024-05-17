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
GOOGLE_FORMS_URL = os.environ.get("GOOGLE_FORM_URL")
ADDR_INPUT_XPATH = (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
RENT_INPUT_XPATH = (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
LINK_INPUT_XPATH = (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#-----Globals------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

class FormBot:
    def __init__(self, url: str) -> None:
        self.url = url
        self.driver = webdriver.Chrome(options=chrome_options)

    def _add(self, property_addr: str, monthly_rent: str, link: str) -> None:
        self.driver.get(self.url)
        addr_input = self.driver.find_element(*ADDR_INPUT_XPATH)
        addr_input.send_keys(property_addr)
        

form = FormBot(url=GOOGLE_FORMS_URL)
form._add("My name", "is", "Zeph!")