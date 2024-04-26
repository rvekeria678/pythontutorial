import os
from dotenv import load_dotenv

load_dotenv()


SHEETY_HOST = 'https://api.sheety.co'
TEQUILA_HOST = 'https://api.tequila.kiwi.com/'

SHEETY_USERNAME = os.environ.get('SHEETY_USERNAME')
SHEETY_PROJECTNAME = os.environ.get('SHEETY_PROJECTNAME')
SHEETY_SHEETNAME = os.environ.get('SHEETY_SHEETNAME')

LOCATION_EP = 'locations/query'
