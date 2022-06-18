import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

class Ballroom_Shuffle():
    scope = "user-read-recently-played"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id,
                                                   client_secret=
                                                   cred.client_secret,
                                                   redirect_uri=cred.redirect_url,
                                                   scope=scope))

    all_playlists = sp.current_user_playlists()
    playlists_info = ((all_playlists['items']))
    standard_playlists = {}
    smooth_playlists = {}
    latin_playlists = {}
    rhythm_playlists = {}
    nightclub_playlists = {}
    for i, playlist in enumerate(playlists_info):
        playlist_name = playlist['name']
        if ('Ballroom Shuffle' in playlist_name):
            if ('Standard' in playlist_name):
                standard_playlists[playlist_name.split()[1]] = playlist['id']
            elif ('Smooth' in playlist_name):
                smooth_playlists[playlist_name.split()[1]] = playlist['id']
            elif ('Latin' in playlist_name):
                latin_playlists[playlist_name.split()[1]] = playlist['id']
            elif ('Rhythm' in playlist_name):
                rhythm_playlists[playlist_name.split()[1]] = playlist['id']
            elif ('Nightclub' in playlist_name):
                nightclub_playlists[playlist_name.split()[1]] = playlist['id']

if __name__ == '__main__':
    ballroom_shuffle = Ballroom_Shuffle()
