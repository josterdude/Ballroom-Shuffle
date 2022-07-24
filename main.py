import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

class Ballroom_Shuffle():
    def __init__(self):
        #self.scope = "user-library-modify"
        self.scope = "playlist-modify-public"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id,
                                                       client_secret=
                                                       cred.client_secret,
                                                       redirect_uri=cred.redirect_url,
                                                       scope=self.scope))
        self.user_id = '31f2tij4ghid3hnzc4ufiaieh5ny'

        self.all_playlists = self.sp.current_user_playlists()
        playlists_info = ((self.all_playlists['items']))
        self.standard_playlists = {}
        self.smooth_playlists = {}
        self.latin_playlists = {}
        self.rhythm_playlists = {}
        self.nightclub_playlists = {}
        self.valid_style_names = ['Standard', 'Smooth', 'Latin', 'Rhythm',
                             'Nightclub']
        self.valid_standard_dance_names = ['Waltz', 'Tango', 'Foxtrot', 'Viennese',
                          'Viennese Waltz', 'Quickstep']
        self.valid_smooth_dance_names = ['Waltz', 'Tango', 'Foxtrot', 'Viennese', 'Viennese Waltz']
        self.valid_latin_dance_names = ['Cha', 'Cha Cha', 'Rumba', 'Samba','Jive']
        self.valid_rhythm_dance_names = ['Cha', 'Cha Cha', 'Rumba',
                                    'Mambo','Swing', 'East Coast Swing',
                                    'ECS']
        self.valid_nightclub_dance_names = ['Salsa', 'Bachata', 'Merengue']
        for i, playlist in enumerate(playlists_info):
            playlist_name = playlist['name']
            if ('Ballroom Shuffle' in playlist_name):
                if ('Standard' in playlist_name):
                    self.standard_playlists[playlist_name.split()[1]] = playlist['id']
                elif ('Smooth' in playlist_name):
                    self.smooth_playlists[playlist_name.split()[1]] = playlist['id']
                elif ('Latin' in playlist_name):
                    self.latin_playlists[playlist_name.split()[1]] = playlist['id']
                elif ('Rhythm' in playlist_name):
                    self.rhythm_playlists[playlist_name.split()[1]] = playlist['id']
                elif ('Nightclub' in playlist_name):
                    self.nightclub_playlists[playlist_name.split()[1]] = playlist['id']

    def get_playlist(self, style_name, dance_name):
        if style_name.capitalize() == 'Standard':
            if dance_name.capitalize() in self.valid_standard_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                return self.sp.playlist(self.standard_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_standard_dance_names}).')
        elif style_name.capitalize() == 'Smooth':
            if dance_name.capitalize() in self.valid_smooth_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                return self.sp.playlist(self.smooth_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_smooth_dance_names}).')
        elif style_name.capitalize() == 'Latin':
            if dance_name.capitalize() in self.valid_latin_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                return self.sp.playlist(self.latin_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_latin_dance_names}).')
        elif style_name.capitalize() == 'Rhythm':
            if dance_name.capitalize() in self.valid_rhythm_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                if dance_name == 'East Coast Swing' or dance_name == 'ECS':
                    dance_name = 'Swing'
                return self.sp.playlist(self.rhythm_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')
        elif style_name.capitalize() == 'Nightclub':
            if dance_name.capitalize() in self.valid_rhythm_dance_names:
                return self.sp.playlist(self.nightclub_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')

    def get_playlist_tracks(self, style_name, dance_name):
        if style_name.capitalize() == 'Standard':
            if dance_name.capitalize() in self.valid_standard_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                return self.sp.playlist_tracks(self.standard_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_standard_dance_names}).')
        elif style_name.capitalize() == 'Smooth':
            if dance_name.capitalize() in self.valid_smooth_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                return self.sp.playlist_tracks(self.smooth_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_smooth_dance_names}).')
        elif style_name.capitalize() == 'Latin':
            if dance_name.capitalize() in self.valid_latin_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                return self.sp.playlist_tracks(self.latin_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_latin_dance_names}).')
        elif style_name.capitalize() == 'Rhythm':
            if dance_name.capitalize() in self.valid_rhythm_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                if dance_name == 'East Coast Swing' or dance_name == 'ECS':
                    dance_name = 'Swing'
                return self.sp.playlist_tracks(self.rhythm_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')
        elif style_name.capitalize() == 'Nightclub':
            if dance_name.capitalize() in self.valid_rhythm_dance_names:
                return self.sp.playlist_tracks(self.nightclub_playlists.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')

if __name__ == '__main__':
    ballroom_shuffle = Ballroom_Shuffle()
    quickstep = ballroom_shuffle.get_playlist('Standard', 'Quickstep')
    quickstep_tracks = ballroom_shuffle.get_playlist_tracks('Standard','Quickstep')
    ballroom_shuffle.sp.user_playlist_create('12102227950', 'test')
    #print(ballroom_shuffle.sp.user_playlists(ballroom_shuffle.user_id)['items'][0])
    #ballroom_shuffle.sp.user_playlist_unfollow(ballroom_shuffle.user_id, )

