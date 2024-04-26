import os
from dotenv import load_dotenv

load_dotenv()


SHEETY_HOST = 'https://api.sheety.co'
TEQUILA_HOST = 'https://api.tequila.kiwi.com/'
TEQUILA_SEARCH_HOST = 'https://api.tequila.kiwi.com/v2'

SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')
SHEETY_PROJECTNAME = os.environ.get('SHEETY_PROJECTNAME')
SHEETY_SHEETNAME = os.environ.get('SHEETY_SHEETNAME')

SHEETY_PROJECT_EP = f"{SHEETY_USERNAME}/{SHEETY_PROJECTNAME}/{SHEETY_SHEETNAME}"

TEQUILA_LOCATION_EP = 'locations/query'
TEQUILA_SEARCH_EP = 'search'