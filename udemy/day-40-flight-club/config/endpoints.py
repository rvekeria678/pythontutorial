import os
from dotenv import load_dotenv

load_dotenv()


SHEETY_HOST = 'https://api.sheety.co'
TEQUILA_HOST = 'https://api.tequila.kiwi.com/'
TEQUILA_SEARCH_HOST = 'https://api.tequila.kiwi.com/v2'

SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')
SHEETY_PROJECTNAME = os.environ.get('SHEETY_PROJECTNAME')

SHEETY_PRICES_SHEET_EP =  f"{SHEETY_USERNAME}/{SHEETY_PROJECTNAME}/prices"
SHEETY_USERS_SHEET_EP = f"{SHEETY_USERNAME}/{SHEETY_PROJECTNAME}/users"

TEQUILA_LOCATION_EP = 'locations/query'
TEQUILA_SEARCH_EP = 'search'