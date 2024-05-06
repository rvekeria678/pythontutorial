from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from bb_scraper import BB_Scraper
import spotipy
import os


input_date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")

top_charts = BB_Scraper()