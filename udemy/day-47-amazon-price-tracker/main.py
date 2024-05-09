from config.urls import PRODUCT_URLS
from config.headers import USER_AGENT, ACCEPT_LANGUAGE
from config.email import EMAIL, PASSWORD, SMTP_ADDR
from config.paths import PRODUCTS_PATH
from bs4 import BeautifulSoup
import pandas
import requests
import smtplib
import pprint

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

price_chart = {}
'''
for product_url in PRODUCT_URLS:
    response = requests.get(url=product_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    dollars = soup.find(name='span', class_="a-price-whole").getText()
    cents = soup.find(name='span', class_="a-price-fraction").getText()
    price_chart[product_url] = float(f"{dollars}{cents}")
'''



data = pandas.read_csv(PRODUCTS_PATH)

pprint(data)