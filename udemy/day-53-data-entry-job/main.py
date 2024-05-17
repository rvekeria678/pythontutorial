from bs4 import BeautifulSoup
from dotenv import load_dotenv
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
cards = soup.select("")
for card in cards:
    data.append({
        "property_addr":,
        "monthly_rent":,
        "link":
    })



links = [el.get('href') for el in link_tags]

print(links)



TEST_DATA = [
    {
        "property_addr":"1",
        "monthly_rent": 1000,
        "link": "weafunapwueb"