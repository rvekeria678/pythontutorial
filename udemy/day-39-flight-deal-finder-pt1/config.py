import os
from dotenv import load_dotenv

load_dotenv()

FLIGHTSEARCH_API_KEY = os.environ.get('FLIGHTSEARCH_API_KEY')

SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')
SHEETY_PROJECTNAME = os.environ.get('SHEETY_PROJECTNAME')
SHEETY_SHEETNAME = os.environ.get('SHEETY_SHEETNAME')
SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')

SHEETY_HOST = 'https://api.sheety.co'

TEQUILA_HOST = 'https://api.tequila.kiwi.com/'
LOCATION_EP = 'locations/query'

DEPARTURE_LOC = "BOS"