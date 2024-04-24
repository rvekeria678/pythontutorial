import os
from dotenv import load_dotenv

load_dotenv()

GRAPH_ID = 'graph1'
GRAPH_NAME = 'Cycling'
TOKEN = os.environ['TOKEN']
USERNAME = os.environ['PIXELA_USERNAME']
ATOS = "yes"
NM = "yes"

HEADERS = {"X-USER-TOKEN": TOKEN}

PIXELA_EP = 'https://pixe.la/v1/users'
GRAPH_EP = f"{PIXELA_EP}/{USERNAME}/graphs"
PIXEL_POST_EP = f"{GRAPH_EP}/{GRAPH_ID}"