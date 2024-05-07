import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from config.spotipy import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import random
import datetime

class SpotifyManager:
    def __init__(self, playlist_data: tuple) -> None:
        scope = 'playlist-modify-private'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                       client_secret=SPOTIFY_CLIENT_SECRET,
                                                       redirect_uri=SPOTIFY_REDIRECT_URI,
                                                       scope=scope))
        try:
            user = sp.current_user()
            user_id = user['id']

            playlist_name = f'Top Hits [{playlist_data[0]}]'
            existing_playlists = sp.user_playlist(user_id)
            playlist_exists = any(playlist['name'] == playlist_name for playlist in existing_playlists['items'])

            if not playlist_exists:
                playlist_description = "A playlist created with Spotipy"
                playlist = sp.user_playlist_create(user_id,
                                               playlist_name,
                                               public=False,
                                               description=playlist_description)
                print("Playlist Created!")
            else:
                print("Playlist Creation Ignored. It Already Exists!")
        except spotipy.exceptions.SpotifyException:
            print("Authentication failed. Check you credentials.")
        
        
        results = sp.current_user