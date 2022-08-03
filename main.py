import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
import numpy as np

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

        self.all_playlists_details = self.sp.current_user_playlists()
        self.all_playlists = {}
        for playlist in self.all_playlists_details['items']:
            playlist_name = playlist['name']
            self.all_playlists[playlist_name] = playlist
        self.standard_playlist_ids = {}
        self.smooth_playlist_ids = {}
        self.latin_playlist_ids = {}
        self.rhythm_playlist_ids = {}
        self.nightclub_playlist_ids = {}
        self.valid_style_names = ['Standard', 'Smooth', 'Latin', 'Rhythm',
                                'Nightclub']
        self.valid_standard_dance_names = ['Waltz', 'Tango', 'Foxtrot', 'Viennese',
                                        'Viennese Waltz', 'Quickstep', 'V Waltz']
        self.valid_smooth_dance_names = ['Waltz', 'Tango', 'Foxtrot', 'Viennese',
                                        'Viennese Waltz', 'V Waltz']
        self.valid_latin_dance_names = ['Cha', 'Cha Cha', 'Rumba', 'Samba','Jive']
        self.valid_rhythm_dance_names = ['Cha', 'Cha Cha', 'Rumba',
                                        'Mambo','Swing', 'East Coast Swing',
                                        'ECS']
        self.valid_nightclub_dance_names = ['Salsa', 'Bachata', 'Merengue']
        for playlist_name, playlist_details in self.all_playlists.items():
            if ('Ballroom Shuffle' in playlist_name):
                if ('Standard' in playlist_name):
                    self.standard_playlist_ids[playlist_name.split()[1]] = playlist_details['id']
                elif ('Smooth' in playlist_name):
                    self.smooth_playlist_ids[playlist_name.split()[1]] = playlist_details['id']
                elif ('Latin' in playlist_name):
                    self.latin_playlist_ids[playlist_name.split()[1]] = playlist_details['id']
                elif ('Rhythm' in playlist_name):
                    self.rhythm_playlist_ids[playlist_name.split()[1]] = playlist_details['id']
                elif ('Nightclub' in playlist_name):
                    self.nightclub_playlist_ids[playlist_name.split()[1]] = playlist_details['id']
        #print(f"Standard playlists:\n{self.standard_playlist_ids}\n-----------------")
        #print(f"Smooth playlists:\n{self.smooth_playlist_ids}\n-----------------")
        #print(f"Latin playlists:\n{self.latin_playlist_ids}\n-----------------")
        #print(f"Rhythm playlists:\n{self.rhythm_playlist_ids}\n-----------------")
        #print(f"Nightclub playlists:\n{self.nightclub_playlist_ids}\n-----------------")
        self.allow_duplicates = False

    def update_all_playlists(self):
        self.all_playlists_details = self.sp.current_user_playlists()
        for playlist in self.all_playlists_details['items']:
            if not playlist['name'] in self.all_playlists.keys():
                self.all_playlists[playlist['name']] = playlist

    def get_playlist(self, style_name, dance_name):
        if style_name == 'Standard':
            if dance_name in self.valid_standard_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                return self.sp.playlist(self.standard_playlist_ids.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_standard_dance_names}).')
        elif style_name == 'Smooth':
            if dance_name in self.valid_smooth_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                return self.sp.playlist(self.smooth_playlist_ids.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_smooth_dance_names}).')
        elif style_name == 'Latin':
            if dance_name in self.valid_latin_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                return self.sp.playlist(self.latin_playlist_ids.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_latin_dance_names}).')
        elif style_name == 'Rhythm':
            if dance_name in self.valid_rhythm_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                if dance_name == 'East Coast Swing' or dance_name == 'ECS':
                    dance_name = 'Swing'
                return self.sp.playlist(self.rhythm_playlist_ids.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')
        elif style_name == 'Nightclub':
            if dance_name in self.valid_rhythm_dance_names:
                return self.sp.playlist(self.nightclub_playlist_ids.get(dance_name))
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')

    def get_playlist_tracks(self, playlist_name):
        if playlist_name in self.all_playlists.keys():
            playlist_items = self.sp.playlist_tracks(self.all_playlists.get(playlist_name)['id'])['items']
            playlist_tracks = []
            for item in playlist_items:
                playlist_tracks.append(item['track'])
            return playlist_tracks
        else:
            print(f"Provided playlist name ({playlist_name}) does not exist.")

    def get_style_dance_tracks(self, style_name, dance_name):
        if style_name == 'Standard':
            if dance_name in self.valid_standard_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                playlist_items = self.sp.playlist_tracks(self.standard_playlist_ids.get(dance_name))['items']
                playlist_tracks = []
                for item in playlist_items:
                    playlist_tracks.append(item['track'])
                return playlist_tracks
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_standard_dance_names}).')
        elif style_name == 'Smooth':
            if dance_name in self.valid_smooth_dance_names:
                if dance_name == 'Viennese Waltz':
                    dance_name = 'Viennese'
                playlist_items = self.sp.playlist_tracks(self.smooth_playlist_ids.get(dance_name))['items']
                playlist_tracks = []
                for item in playlist_items:
                    playlist_tracks.append(item['track'])
                return playlist_tracks
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_smooth_dance_names}).')
        elif style_name == 'Latin':
            if dance_name in self.valid_latin_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                playlist_items = self.sp.playlist_tracks(self.latin_playlist_ids.get(dance_name))['items']
                playlist_tracks = []
                for item in playlist_items:
                    playlist_tracks.append(item['track'])
                return playlist_tracks
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_latin_dance_names}).')
        elif style_name == 'Rhythm':
            if dance_name in self.valid_rhythm_dance_names:
                if dance_name == 'Cha Cha':
                    dance_name = 'Cha'
                if dance_name == 'East Coast Swing' or dance_name == 'ECS':
                    dance_name = 'Swing'
                playlist_items = self.sp.playlist_tracks(self.rhythm_playlist_ids.get(dance_name))['items']
                playlist_tracks = []
                for item in playlist_items:
                    playlist_tracks.append(item['track'])
                return playlist_tracks
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')
        elif style_name == 'Nightclub':
            if dance_name in self.valid_rhythm_dance_names:
                playlist_items = self.sp.playlist_tracks(self.nightclub_playlist_ids.get(dance_name))['items']
                playlist_tracks = []
                for item in playlist_items:
                    playlist_tracks.append(item['track'])
                return playlist_tracks
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')

if __name__ == '__main__':
    ballroom_shuffle = Ballroom_Shuffle()
    #quickstep = ballroom_shuffle.get_playlist('Standard', 'Quickstep')
    #print(quickstep)
    #quickstep_tracks = ballroom_shuffle.get_playlist_tracks('Standard','Quickstep')

    # Create a playlist called "test"
    #ballroom_shuffle.sp.user_playlist_create(ballroom_shuffle.user_id, 'test')

    # Search for ID of newly created "test" playlist
    #ballroom_shuffle.update_all_playlists()
    #print(ballroom_shuffle.all_playlists.get('test'))

    # Populate playlist with songs
    latin_cha = ballroom_shuffle.get_playlist_tracks('Latin', 'Cha Cha')
    latin_rumba = ballroom_shuffle.get_playlist_tracks('Latin', 'Rumba')
    latin_samba = ballroom_shuffle.get_playlist_tracks('Latin', 'Samba')
    latin_jive = ballroom_shuffle.get_playlist_tracks('Latin', 'Jive')

    #print(f'Latin Cha Songs: \n{len(latin_cha)}')
    random_latin_cha = np.random.choice(latin_cha, size=3, replace=False)
    #print(f'Random Latin Cha Songs: {random_latin_cha}')
    for i, song in enumerate(random_latin_cha):
        print(f"Adding {song['name']} by {song['artists'][0]['name']} to playlist")
    ballroom_shuffle.sp.playlist_add_items(ballroom_shuffle.all_playlists['test']['id'], [song['id'] for song in random_latin_cha])
    #print(latin_cha[0])
    #print('======================')
    #print(f"{latin_cha[0].keys()}")
    #print(f"{latin_cha[0]['track']}")
    #print(f"Adding {latin_cha[0]['track']['name']} by {latin_cha[0]['track']['artists'][0]['name']}")
    #ballroom_shuffle.sp.playlist_add_items(ballroom_shuffle.all_playlists['test']['id'], [latin_cha[0]['track']['id']])
    '''
    print(f'Latin Rumba Songs: {latin_rumba}')
    print('======================')
    print(f'Latin Samba Songs: {latin_samba}')
    print('======================')
    print(f'Latin Jive Songs: {latin_jive}')
    '''

    # Remove a playlist called "test"
    '''
    for playlist in ballroom_shuffle.all_playlists:
        if 'test' in playlist['name']:
            print(f"Removing playlist: {playlist['name']}")
            ballroom_shuffle.sp.current_user_unfollow_playlist(playlist['id'])
    '''

    #print(ballroom_shuffle.sp.user_playlists(ballroom_shuffle.user_id)['items'][0])
    #ballroom_shuffle.sp.user_playlist_unfollow(ballroom_shuffle.user_id, )


# TODO: Ensure that random songs being added to the playlist do not already exist in the playlist unless the user specifies that duplicates are enabled. If duplicates are not enabled, randomly choose a new song