from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#-----Constants-----#
URL = "https://orteil.dashnet.org/experiments/cookie/"
#-----Globals-----#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value='cookie')

timeout = time.time() + 5
#-----Cookie Bot Logic-----#
while True:
    cookie.click()

    if time.time() > timeout:
        upgrades = driver.find_elements(By.CSS_SELECTOR, value = "#store div")[:-1]

        bel_text = [el.text for el in driver.find_elements(By.CSS_SELECTOR, value="#store b")][:-1]
        prices = [int(text.split('-')[1].replace(',','')) for text in bel_text]

        price_bind_div = dict(zip(prices, upgrades))

        money = int(driver.find_element(By.ID, value='money').text.replace(',',''))

        affordable_upgrades = [cost for cost in prices if cost <= money]

        print(f"Money: {money}")
        print(f"Affordable Upgrades: {affordable_upgrades}")

        if affordable_upgrades:
            most_expensive_upgrade = max(affordable_upgrades)
            print(f"MEU: {most_expensive_upgrade}")
            
            price_bind_div[most_expensive_upgrade].click()       

        timeout = time.time() + 5