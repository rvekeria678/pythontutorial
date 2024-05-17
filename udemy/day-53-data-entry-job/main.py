from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pprint import pprint
from form_bot import FormBot
from config.weblinks import ZILLOW_CLONE_URL
import requests
import os
load_dotenv()
#------Constants-----#
GOOGLE_FORMS_URL = os.environ.get("GOOGLE_FORM_URL")
#-----Globals-----#
response = requests.get(ZILLOW_CLONE_URL)
soup = BeautifulSoup(response.text, 'html.parser')
data = []
#-----Scrape Logic-----#
#link_tags = soup.select(".List-c11n-8-84-3-photo-cards li .property-card-link")
cards = soup.select(".List-c11n-8-84-3-photo-cards li")

for card in cards:
    addr = card.find(attrs={"data-test":"property-card-addr"})
    price = card.find(attrs={"data-test":"property-card-price"})
    link = card.find(attrs={"data-test":"property-card-link"})

    print(addr, price, link)

    if addr != None:
        data.append({
            "property_addr": addr.getText(strip=True),
            "monthly_rent": price.getText(strip=True),
            "link": link.get('href').strip()
        })

FormBot(GOOGLE_FORMS_URL).add_data(data=data)