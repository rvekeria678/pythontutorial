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
