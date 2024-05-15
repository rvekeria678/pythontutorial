from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from dotenv import load_dotenv
import time
import os

load_dotenv()
#-----Constants------#
URL = 'https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0'
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
#-----Globals------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
#-----Sign In Logic-----#
SignInBtn = driver.find_element(by=By.LINK_TEXT, value='Sign in')
if SignInBtn:
    SignInBtn.click()
    username_input = driver.find_element(by=By.ID, value="username")
    username_input.send_keys(EMAIL)
    password_input = driver.find_element(by=By.ID, value="password")
    password_input.send_keys(PASSWORD)
    driver.find_element(by=By.CSS_SELECTOR, value=".login__form_action_container button").click()
#-----Job Apply-----#
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(by=By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
    )
except Exception as e:
    print(f"Error occurred: {e}")

driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button--top-card button").click()

