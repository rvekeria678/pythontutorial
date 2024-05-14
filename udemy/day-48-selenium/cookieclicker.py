from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import time

#-----Constants-----#
URL = "https://orteil.dashnet.org/experiments/cookie/"
#-----Globals-----#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

cookie = driver.find_element(By.ID, value='cookie')

upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")[:-1]
upgrade_ids = [upgrade.get_attribute("id") for upgrade in upgrades]

timeout = time.time() + 4

#-----Cookie Bot Logic-----#
while True:
    cookie.click()

    if time.time() > timeout:
        upgrade_costs = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")[:-1]
        prices = [int(cost.text.split('-')[1].strip().replace(',','')) for cost in upgrade_costs]
        all_upgrades = dict(zip(prices, upgrade_ids))
        money = int(driver.find_element(By.ID, value='money').text.replace(',',''))
        affordable_upgrades = [price for price in prices if price <= money]

        if affordable_upgrades:
            highest_price_affordable = max(affordable_upgrades)
            purchase_id = all_upgrades[highest_price_affordable]

            driver.find_element(by=By.ID, value=purchase_id).click()

        timeout = time.time() + 4