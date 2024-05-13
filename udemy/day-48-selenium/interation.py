from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#n_articles_total = int(driver.find_element(By.XPATH,
#                                            value='//*[@id="articlecount"]/a[1]').text.replace(',',''))

#driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').click()
#driver.find_element(By.LINK_TEXT, "Doom").click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)


#print(en_articles_total)


#driver.quit()

