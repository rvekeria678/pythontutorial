from spotify_manager import SpotifyManager
from bb_scraper import BB_Scraper
from dotenv import load_dotenv
import os
import re

#-----Date Logic-----#
def get_date():
    while True:
        date_input = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
        if re.match(r'\d{4}-\d{2}-\d{2}', date_input): return date_input
        else: print("Invalid format. Please enter a date in the format 'YYYY-MM-DD' .")
#-----Spotipy Logic -----#
spotify_manager = SpotifyManager(BB_Scraper(get_date()).data)