from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Zeph")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Leonidas")

email = driver.find_element(By.NAME, value="email")
email.send_keys("zeph123@gmail.com")

driver.find_element(By.XPATH, value="/html/body/form/button").click()