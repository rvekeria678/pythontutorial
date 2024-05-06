import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from config.spotipy import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import random

class SpotifyManager:
    def __init__(self, data) -> None:
        scope = 'user-library-read'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                       client_secret=SPOTIFY_CLIENT_SECRET,
                                                       redirect_uri=SPOTIFY_REDIRECT_URI,
                                                       scope=scope))
        
        try:
            #results = sp.current_user_saved_tracks()
            
            #for idx, item in enumerate(results['items']):
            #    track = item['track']
            #    print(idx, track['artists'][0]['name'], " – ", track['name'])

            play_list = f'R-{random.randint(200,1000)}'

        except spotipy.exceptions.SpotifyException:
            print("Authentication failed. Check you credentials.")
        
        
        results = sp.current_user

SpotifyManager(1)