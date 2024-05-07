import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from config.spotipy import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import random
import datetime

class SpotifyManager:
    def __init__(self) -> None:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                       client_secret=SPOTIFY_CLIENT_SECRET,
                                                       redirect_uri=SPOTIFY_REDIRECT_URI))
        self.user = sp.current_user()
        self.user_id = self.user['id']

    def create_playlist(self, playlist_data: tuple) -> None:
        scope = 'playlist-modify-private'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        try:
            playlist_name = f'{playlist_data[0]} Billboard 100'
            playlist_description = "A playlist created with Spotipy"
            self.playlist = sp.user_playlist_create(self.user_id,
                                               playlist_name,
                                               public=False,
                                               description=playlist_description)
            print("Playlist created...")
            print("Attempting to add songs...")
            tracks = [self.search(track_name=track,
                                  track_year=playlist_data[0])['tracks']['href']
                                  for track in playlist_data[1]]
            sp.playlist_add_items(self.playlist, tracks)
            print("Succesfully Added Songs! Enjoy your tunes!")

        except spotipy.exceptions.SpotifyException:
            print("Authentication failed. Check you credentials.")

    def search(self, track_name: str, track_year: str):
        scope = 'user-library-read'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        query = f"track:{track_name} year:{track_year}"
        results = sp.search(q=query, limit=1, type='track')
        return results
                