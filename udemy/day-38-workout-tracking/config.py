from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

SHEETY_USERNAME = os.environ['SHEETY_USERNAME']
SHEETY_PROJECTNAME = os.environ['SHEETY_PROJECTNAME']
SHEETY_SHEETNAME = os.environ['SHEETY_SHEETNAME']
BEARER_TOKEN = os.environ['BEARER_TOKEN']

NN_HOST = 'https://trackapi.nutritionix.com'
NN_NLE_EP = '/v2/natural/exercise'

SHEETY_WORKOUT_EP = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECTNAME}/{SHEETY_SHEETNAME}"
