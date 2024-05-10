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
    response = requests.get(url=row['url'], headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    #-----Filter Scrapped Price-----#
    dollars = soup.find(name='span', class_="a-price-whole").getText()
    cents = soup.find(name='span', class_="a-price-fraction").getText()
    if dollars and cents:
        current_price = float(f"{dollars}{cents}")
        if current_price <= row['wp']:
            product_title = soup.find(name='span', id="productTitle").getText()
            subject = f"Amazon Price Alert! (Price Drop: ${current_price})"
            message = f"{product_title} is now ${current_price}\n{row['url']}"
            with smtplib.SMTP(SMTP_ADDR, 587) as server:
                server.starttls()
                server.login(user=EMAIL, password=PASSWORD)
                server.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:{subject}\n\n{message}")