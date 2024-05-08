import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from config.spotipy import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from pprint import pprint


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
            playlist = sp.user_playlist_create(self.user_id,
                                               playlist_name,
                                               public=False,
                                               description=playlist_description)
            playlist_id = playlist['id']
            print(f"Playlist created with ID: {playlist_id}")
            print("Attempting to add songs...")
            results = [self.search(track_name=track,
                                  release_year=playlist_data[0].split('-')[0])
                                  for track in playlist_data[1]]
            uri_links = [result['tracks']['items'][0]['uri'] for result in results if result['tracks']['items']]
            print(uri_links)
            sp.user_playlist_add_tracks(user=self.user_id,playlist_id=playlist_id, tracks=uri_links)
            print("Succesfully Added Songs! Enjoy your tunes!")

        except spotipy.exceptions.SpotifyException:
            print("Authentication failed. Check you credentials.")

    def search(self, track_name: str, release_year: str):
        scope = 'user-library-read'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        query = f"track:{track_name} year:{release_year}"
        pprint(query)
        result = sp.search(q=query, limit=1, type='track')
        return result