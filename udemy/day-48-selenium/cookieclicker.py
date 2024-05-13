from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

timeout = time.time() + 5

def buy_most_expensive():
    try:
        store = driver.find_element(By.ID, value="store")
        products = store.find_elements(By.TAG_NAME, value='div')[:-1]    
        options = [product.find_element(By.TAG_NAME, value='b').text.split(' - ') for product in products]
        product_names = [option[0] for option in options]
        product_prices = [int(option[1].replace(',','')) for option in options]
    
        product_mapper = dict(zip(product_prices, products))
        price_mapper = dict(zip(product_prices, product_names))
        print(price_mapper)
        # Most Expensive Purchase
        mep = 0
        money = int(driver.find_element(By.ID, value='money').text.replace(',',''))
        for price in product_prices:
            if money >= price and price > mep:
                mep = price
    
        print(f"Purchasing {price_mapper[mep]} for {mep}")
        product_mapper[mep].click()
    except Exception as e:
        print("An error occurred while purchasing:", e)

while True:
    time.sleep(0.5)
    while True:
        if time.time() > timeout:
            timeout = time.time() + 5
            break
        driver.find_element(By.ID, value='cookie').click()
    
    buy_most_expensive()
    
    cps = driver.find_element(By.ID, value='cps').text
    print(f"cookies/seconds: {cps}")
