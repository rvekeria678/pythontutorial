from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

HOST = 'https://trackapi.nutritionix.com'
NLE_EP = '/v2/natural/exercise'