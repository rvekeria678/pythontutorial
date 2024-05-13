from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#date = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')

#print(date.text)

events_ul = driver.find_element(By.XPATH,
                                value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

events_li = events_ul.find_elements(By.TAG_NAME, value="li")

dates = [el.find_element(By.TAG_NAME, value='time').text for el in events_li]
events = [el.find_element(By.TAG_NAME, value='a').text for el in events_li]

schedule = {}

for x in range(len(dates)):
    schedule[x] = {
        'time': dates[x],
        'name': events[x]
    }
print(schedule)

driver.quit()