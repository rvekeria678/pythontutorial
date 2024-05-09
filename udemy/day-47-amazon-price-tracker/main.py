from config.urls import PRODUCT_URLS
from config.headers import USER_AGENT, ACCEPT_LANGUAGE
from config.email import EMAIL, PASSWORD, SMTP_ADDR
from config.paths import PRODUCTS_PATH
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import requests
import smtplib

#------Constants-----#
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}
#-----Globals-----#
price_chart = {}
#-----Retrieve Local Data-----#
df = pd.read_csv(PRODUCTS_PATH)
#-----Check Watch Prices-----#
for index, row, in df.iterrows():
    print(row['url'])
    print(type(row['url']))
    response = requests.get(url=row['url'], headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'http.parser')
    #-----Filter Scrapped Price-----#
    dollars = soup.find(name='span', class_="a-price-whole").getText()
    cents = soup.find(name='span', class_="a-price-fraction").getText()
    current_price = float(f"{dollars}{cents}")
    if current_price <= row["watch_price"]:
        print("Sending an Email...")