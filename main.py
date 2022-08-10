from platform import platform
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
        self.allow_duplicates = False

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

    def load_ballroom_playlists(self):
        print("Loading music from source playlists...")
        self.standard_waltz = self.get_style_dance_tracks('Standard', 'Waltz')
        print("Progress: 5%")
        self.standard_tango = self.get_style_dance_tracks('Standard', 'Tango')
        print("Progress: 10%")
        self.standard_foxtrot = self.get_style_dance_tracks('Standard', 'Foxtrot')
        print("Progress: 15%")
        self.standard_quickstep = self.get_style_dance_tracks('Standard', 'Quickstep')
        print("Progress: 20%")
        self.standard_v_waltz = self.get_style_dance_tracks('Standard', 'Viennese Waltz')
        print("Progress: 25%")
        self.smooth_waltz = self.get_style_dance_tracks('Smooth', 'Waltz')
        print("Progress: 30%")
        self.smooth_tango = self.get_style_dance_tracks('Smooth', 'Tango')
        print("Progress: 35%")
        self.smooth_foxtrot = self.get_style_dance_tracks('Smooth', 'Foxtrot')
        print("Progress: 40%")
        self.smooth_v_waltz = self.get_style_dance_tracks('Smooth', 'Viennese Waltz')
        print("Progress: 45%")
        self.latin_cha_cha = self.get_style_dance_tracks('Latin', 'Cha Cha')
        print("Progress: 50%")
        self.latin_rumba = self.get_style_dance_tracks('Latin', 'Rumba')
        print("Progress: 55%")
        self.latin_samba = self.get_style_dance_tracks('Latin', 'Samba')
        print("Progress: 60%")
        self.latin_jive = self.get_style_dance_tracks('Latin', 'Jive')
        print("Progress: 65%")
        self.rhythm_cha_cha = self.get_style_dance_tracks('Rhythm', 'Cha Cha')
        print("Progress: 70%")
        self.rhythm_rumba = self.get_style_dance_tracks('Rhythm', 'Rumba')
        print("Progress: 75%")
        self.rhythm_swing = self.get_style_dance_tracks('Rhythm', 'Swing')
        print("Progress: 80%")
        self.rhythm_mambo = self.get_style_dance_tracks('Rhythm', 'Mambo')
        print("Progress: 85%")
        self.nightclub_salsa = self.get_style_dance_tracks('Nightclub', 'Salsa')
        print("Progress: 90%")
        self.nightclub_bachata = self.get_style_dance_tracks('Nightclub', 'Bachata')
        print("Progress: 95%")
        self.nightclub_merengue = self.get_style_dance_tracks('Nightclub', 'Merengue')
        print("Progress: 100%")
        print("Finished loading music from source playlists.")

    def update_all_playlists(self):
        self.all_playlists_details = self.sp.current_user_playlists()
        for playlist in self.all_playlists_details['items']:
            if not playlist['name'] in self.all_playlists.keys():
                self.all_playlists[playlist['name']] = playlist

    def get_style_dance_playlist(self, style_name, dance_name):
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
            if dance_name in self.valid_nightclub_dance_names:
                playlist_items = self.sp.playlist_tracks(self.nightclub_playlist_ids.get(dance_name))['items']
                playlist_tracks = []
                for item in playlist_items:
                    playlist_tracks.append(item['track'])
                return playlist_tracks
            else:
                exit(f'Provided dance name ({dance_name}) is not valid. Please\
                     enter a valid dance name ({self.valid_rhythm_dance_names}).')

    def create_playlist(self, playlist_name, preferences, shuffle=False):
        # Ensure provided playlist name does not already exist
        all_playlist_names = self.all_playlists.keys()
        if playlist_name in all_playlist_names:
            return 1, f"The provided playlist name ({playlist_name}) is already taken. Please provide a new playlist name.", None

        # Populate new playlist with songs
        songs_to_add_to_playlist = []

        if preferences.get('Standard Waltz') > 0:
            max_num_standard_waltz_songs = len(self.standard_waltz)
            if preferences.get('Standard Waltz') <= max_num_standard_waltz_songs:
                random_standard_waltz = np.random.choice(self.standard_waltz, size = preferences.get('Standard Waltz'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_standard_waltz]))
            else:
                return 2, f"The number of Standard Waltz songs chosen ({preferences.get('Standard Waltz')} exceeds the maximum number of Standard Waltz songs available. Please enter a value less than or equal to {max_num_standard_waltz_songs}.", None

        if preferences.get('Standard Tango') > 0:
            max_num_standard_tango_songs = len(self.standard_tango)
            if preferences.get('Standard Tango') <= max_num_standard_tango_songs:
                random_standard_tango = np.random.choice(self.standard_tango, size = preferences.get('Standard Tango'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_standard_tango]))
            else:
                return 3, f"The number of Standard Tango songs chosen ({preferences.get('Standard Tango')} exceeds the maximum number of Standard Tango songs available. Please enter a value less than or equal to {max_num_standard_tango_songs}.", None

        if preferences.get('Standard Foxtrot') > 0:
            max_num_standard_foxtrot_songs = len(self.standard_foxtrot)
            if preferences.get('Standard Foxtrot') <= max_num_standard_foxtrot_songs:
                random_standard_foxtrot = np.random.choice(self.standard_foxtrot, size = preferences.get('Standard Foxtrot'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_standard_foxtrot]))
            else:
                return 4, f"The number of Standard Foxtrot songs chosen ({preferences.get('Standard Foxtrot')} exceeds the maximum number of Standard Foxtrot songs available. Please enter a value less than or equal to {max_num_standard_foxtrot_songs}.", None

        if preferences.get('Standard Quickstep') > 0:
            max_num_standard_quickstep_songs = len(self.standard_quickstep)
            if preferences.get('Standard Quickstep') <= max_num_standard_quickstep_songs:
                random_standard_quickstep = np.random.choice(self.standard_quickstep, size = preferences.get('Standard Quickstep'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_standard_quickstep]))
            else:
                return 5, f"The number of Standard Quickstep songs chosen ({preferences.get('Standard Quickstep')} exceeds the maximum number of Standard Quickstep songs available. Please enter a value less than or equal to {max_num_standard_quickstep_songs}.", None

        if preferences.get('Standard Viennese Waltz') > 0:
            max_num_standard_v_waltz_songs = len(self.standard_v_waltz)
            if preferences.get('Standard Viennese Waltz') <= max_num_standard_v_waltz_songs:
                random_standard_v_waltz = np.random.choice(self.standard_v_waltz, size = preferences.get('Standard Viennese Waltz'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_standard_v_waltz]))
            else:
                return 6, f"The number of Standard Viennese Waltz songs chosen ({preferences.get('Standard Viennese Waltz')} exceeds the maximum number of Standard Viennese Waltz songs available. Please enter a value less than or equal to {max_num_standard_v_waltz_songs}.", None

        if preferences.get('Smooth Waltz') > 0:
            max_num_smooth_waltz_songs = len(self.smooth_waltz)
            if preferences.get('Smooth Waltz') <= max_num_smooth_waltz_songs:
                random_smooth_waltz = np.random.choice(self.smooth_waltz, size = preferences.get('Smooth Waltz'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_smooth_waltz]))
            else:
                return 7, f"The number of Smooth Waltz songs chosen ({preferences.get('Standard Waltz')} exceeds the maximum number of Smooth Waltz songs available. Please enter a value less than or equal to {max_num_smooth_waltz_songs}.", None

        if preferences.get('Smooth Tango') > 0:
            max_num_smooth_tango_songs = len(self.smooth_tango)
            if preferences.get('Smooth Tango') <= max_num_smooth_tango_songs:
                random_smooth_tango = np.random.choice(self.smooth_tango, size = preferences.get('Smooth Tango'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_smooth_tango]))
            else:
                return 8, f"The number of Smooth Tango songs chosen ({preferences.get('Smooth Tango')} exceeds the maximum number of Smooth Tango songs available. Please enter a value less than or equal to {max_num_smooth_tango_songs}.", None

        if preferences.get('Smooth Foxtrot') > 0:
            max_num_smooth_foxtrot_songs = len(self.smooth_foxtrot)
            if preferences.get('Smooth Foxtrot') <= max_num_smooth_foxtrot_songs:
                random_smooth_foxtrot = np.random.choice(self.smooth_foxtrot, size = preferences.get('Smooth Foxtrot'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_smooth_foxtrot]))
            else:
                return 9, f"The number of Smooth Foxtrot songs chosen ({preferences.get('Smooth Foxtrot')} exceeds the maximum number of Smooth Foxtrot songs available. Please enter a value less than or equal to {max_num_smooth_foxtrot_songs}.", None

        if preferences.get('Smooth Viennese Waltz') > 0:
            max_num_smooth_v_waltz_songs = len(self.smooth_v_waltz)
            if preferences.get('Smooth Viennese Waltz') <= max_num_smooth_v_waltz_songs:
                random_smooth_v_waltz = np.random.choice(self.smooth_v_waltz, size = preferences.get('Smooth Viennese Waltz'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_smooth_v_waltz]))
            else:
                return 10, f"The number of Smooth Viennese Waltz songs chosen ({preferences.get('Smooth Viennese Waltz')} exceeds the maximum number of Smooth Viennese Waltz songs available. Please enter a value less than or equal to {max_num_smooth_v_waltz_songs}.", None

        if preferences.get('Latin Cha Cha') > 0:
            max_num_latin_cha_cha_songs = len(self.latin_cha_cha)
            if preferences.get('Latin Cha Cha') <= max_num_latin_cha_cha_songs:
                random_latin_cha_cha = np.random.choice(self.latin_cha_cha, size = preferences.get('Latin Cha Cha'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_latin_cha_cha]))
            else:
                return 11, f"The number of Latin Cha Cha songs chosen ({preferences.get('Latin Cha Cha')} exceeds the maximum number of Latin Cha Cha songs available. Please enter a value less than or equal to {max_num_latin_cha_cha_songs}.", None

        if preferences.get('Latin Rumba') > 0:
            max_num_latin_rumba_songs = len(self.latin_rumba)
            if preferences.get('Latin Rumba') <= max_num_latin_rumba_songs:
                random_latin_rumba = np.random.choice(self.latin_rumba, size = preferences.get('Latin Rumba'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_latin_rumba]))
            else:
                return 12, f"The number of Latin Rumba songs chosen ({preferences.get('Latin Rumba')} exceeds the maximum number of Latin Rumba songs available. Please enter a value less than or equal to {max_num_latin_rumba_songs}.", None

        if preferences.get('Latin Samba') > 0:
            max_num_latin_samba_songs = len(self.latin_samba)
            if preferences.get('Latin Samba') <= max_num_latin_samba_songs:
                random_latin_samba = np.random.choice(self.latin_samba, size = preferences.get('Latin Samba'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_latin_samba]))
            else:
                return 13, f"The number of Latin Samba songs chosen ({preferences.get('Latin Samba')} exceeds the maximum number of Latin Samba songs available. Please enter a value less than or equal to {max_num_latin_samba_songs}.", None

        if preferences.get('Latin Jive') > 0:
            max_num_latin_jive_songs = len(self.latin_jive)
            if preferences.get('Latin Jive') <= max_num_latin_jive_songs:
                random_latin_jive = np.random.choice(self.latin_jive, size = preferences.get('Latin Jive'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_latin_jive]))
            else:
                return 14, f"The number of Latin Jive songs chosen ({preferences.get('Latin Jive')} exceeds the maximum number of Latin Jive songs available. Please enter a value less than or equal to {max_num_latin_jive_songs}.", None

        if preferences.get('Rhythm Cha Cha') > 0:
            max_num_rhythm_cha_cha_songs = len(self.rhythm_cha_cha)
            if preferences.get('Rhythm Cha Cha') <= max_num_rhythm_cha_cha_songs:
                random_rhythm_cha_cha = np.random.choice(self.rhythm_cha_cha, size = preferences.get('Rhythm Cha Cha'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_rhythm_cha_cha]))
            else:
                return 15, f"The number of Rhythm Cha Cha songs chosen ({preferences.get('Rhythm Cha Cha')} exceeds the maximum number of Rhythm Cha Cha songs available. Please enter a value less than or equal to {max_num_rhythm_cha_cha_songs}.", None

        if preferences.get('Rhythm Rumba') > 0:
            max_num_rhythm_rumba_songs = len(self.rhythm_rumba)
            if preferences.get('Rhythm Rumba') <= max_num_rhythm_rumba_songs:
                random_rhythm_rumba = np.random.choice(self.rhythm_rumba, size = preferences.get('Rhythm Rumba'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_rhythm_rumba]))
            else:
                return 16, f"The number of Rhythm Rumba songs chosen ({preferences.get('Rhythm Rumba')} exceeds the maximum number of Rhythm Rumba songs available. Please enter a value less than or equal to {max_num_rhythm_rumba_songs}.", None

        if preferences.get('Rhythm Swing') > 0:
            max_num_rhythm_swing_songs = len(self.rhythm_swing)
            if preferences.get('Rhythm Swing') <= max_num_rhythm_swing_songs:
                random_rhythm_swing = np.random.choice(self.rhythm_swing, size = preferences.get('Rhythm Swing'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_rhythm_swing]))
            else:
                return 17, f"The number of Rhythm Swing songs chosen ({preferences.get('Rhythm Swing')} exceeds the maximum number of Rhythm Swing songs available. Please enter a value less than or equal to {max_num_rhythm_swing_songs}.", None

        if preferences.get('Rhythm Mambo') > 0:
            max_num_rhythm_mambo_songs = len(self.rhythm_mambo)
            if preferences.get('Rhythm Mambo') <= max_num_rhythm_mambo_songs:
                random_rhythm_mambo = np.random.choice(self.rhythm_mambo, size = preferences.get('Rhythm Mambo'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_rhythm_mambo]))
            else:
                return 18, f"The number of Rhythm Mambo songs chosen ({preferences.get('Rhythm Mambo')} exceeds the maximum number of Rhythm Mambo songs available. Please enter a value less than or equal to {max_num_rhythm_mambo_songs}.", None

        if preferences.get('Nightclub Salsa') > 0:
            max_num_nightclub_salsa_songs = len(self.nightclub_salsa)
            if preferences.get('Nightclub Salsa') <= max_num_nightclub_salsa_songs:
                random_nightclub_salsa = np.random.choice(self.nightclub_salsa, size = preferences.get('Nightclub Salsa'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_nightclub_salsa]))
            else:
                return 19, f"The number of Nightclub Salsa songs chosen ({preferences.get('Nightclub Salsa')} exceeds the maximum number of Nightclub Salsa songs available. Please enter a value less than or equal to {max_num_nightclub_salsa_songs}.", None

        if preferences.get('Nightclub Bachata') > 0:
            max_num_nightclub_bachata_songs = len(self.nightclub_bachata)
            if preferences.get('Nightclub Bachata') <= max_num_nightclub_bachata_songs:
                random_nightclub_bachata = np.random.choice(self.nightclub_bachata, size = preferences.get('Nightclub Bachata'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_nightclub_bachata]))
            else:
                return 20, f"The number of Nightclub Bachata songs chosen ({preferences.get('Nightclub Bachata')} exceeds the maximum number of Nightclub Bachata songs available. Please enter a value less than or equal to {max_num_nightclub_bachata_songs}.", None

        if preferences.get('Nightclub Merengue') > 0:
            max_num_nightclub_merengue_songs = len(self.nightclub_merengue)
            if preferences.get('Nightclub Merengue') <= max_num_nightclub_merengue_songs:
                random_nightclub_merengue = np.random.choice(self.nightclub_merengue, size = preferences.get('Nightclub Merengue'), replace = False)
                songs_to_add_to_playlist = np.concatenate((songs_to_add_to_playlist, [song['id'] for song in random_nightclub_merengue]))
            else:
                return 21, f"The number of Nightclub Merengue songs chosen ({preferences.get('Nightclub Merengue')} exceeds the maximum number of Nightclub Merengue songs available. Please enter a value less than or equal to {max_num_nightclub_merengue_songs}.", None

        if shuffle:
            songs_to_add_to_playlist = np.random.shuffle(songs_to_add_to_playlist)

        if len(songs_to_add_to_playlist) == 0:
            return 22, "Must choose at least one song to create a playlist.", None

        # Create a playlist with provided playlist name
        self.sp.user_playlist_create(self.user_id, playlist_name)

        # Ensure newly created playlist is included in dictionary containing all playlists
        self.update_all_playlists()

        self.sp.playlist_add_items(self.all_playlists[playlist_name]['id'], songs_to_add_to_playlist)

        return 0, f"Created custom playlist: {playlist_name}", self.all_playlists[playlist_name]['id']

    # TODO: "Save the playlist" by renaming with the function user_playlist_change_details(user, playlist_id, name=None, public=True)

    def delete_playlist(self, playlist_name):
        # Ensure all playlist information is updated
        ballroom_shuffle.update_all_playlists()

        all_playlist_names = self.all_playlists.keys()
        if playlist_name in all_playlist_names:
            print(f"Removing playlist: {playlist_name}")
            ballroom_shuffle.sp.current_user_unfollow_playlist(self.all_playlists.get(playlist_name)['id'])
        else:
            print(f"Provided playlist name ({playlist_name}) does not exist. Please provide a valid playlist name.")

    def delete_temporary_playlists(self):
        # Ensure all playlist information is updated
        ballroom_shuffle.update_all_playlists()

        for playlist_name, playlist_details in self.all_playlists.items():
            if 'Temporary' in playlist_name:
                print(f"Removing playlist: {playlist_name}")
                ballroom_shuffle.sp.current_user_unfollow_playlist(playlist_details['id'])

    '''
    def custom_playback(self):
        self.scope = "user-modify-playback-state"
        # TODO: Remember to change the scope back to "playlist-modify-public"
        #ballroom_shuffle.update_all_playlists()
        custom_playlists = {}
        for i, (playlist_name, playlist_details) in enumerate(self.all_playlists.items()):
            if not 'Ballroom Shuffle' in playlist_name:
               print(f"{i}: {playlist_name}");
               custom_playlists[i] = playlist_name

        choice = int(input("Which playlist would you like to play? "))
        choice = custom_playlists[choice]
        chosen_playlist = self.all_playlists.get(choice)
        chosen_playlist_tracks = self.get_playlist_tracks(chosen_playlist.get('name'))
        for track in chosen_playlist_tracks:
            print(track['name'])
        self.sp.start_playback(context_uri=chosen_playlist.get('uri'))
    '''

if __name__ == '__main__':
    ballroom_shuffle = Ballroom_Shuffle()

    default_rounds = {'Standard Waltz': 1, 'Standard Tango': 1, 'Standard Foxtrot': 1, 'Standard Quickstep': 1, 'Standard Viennese Waltz': 1,
                      'Smooth Waltz': 1, 'Smooth Tango': 1, 'Smooth Foxtrot': 1, 'Smooth Viennese Waltz': 1,
                      'Latin Cha Cha': 1, 'Latin Rumba': 1, 'Latin Samba': 1, 'Latin Jive': 1,
                      'Rhythm Cha Cha': 1, 'Rhythm Rumba': 1, 'Rhythm Swing': 1, 'Rhythm Mambo': 1,
                      'Nightclub Salsa': 0, 'Nightclub Bachata': 0, 'Nightclub Merengue': 0}

    default_standard_smooth = {'Standard Waltz': 1, 'Standard Tango': 1, 'Standard Foxtrot': 1, 'Standard Quickstep': 1, 'Standard Viennese Waltz': 1,
                      'Smooth Waltz': 1, 'Smooth Tango': 1, 'Smooth Foxtrot': 1, 'Smooth Viennese Waltz': 1,
                      'Latin Cha Cha': 0, 'Latin Rumba': 0, 'Latin Samba': 0, 'Latin Jive': 0,
                      'Rhythm Cha Cha': 0, 'Rhythm Rumba': 0, 'Rhythm Swing': 0, 'Rhythm Mambo': 0,
                      'Nightclub Salsa': 0, 'Nightclub Bachata': 0, 'Nightclub Merengue': 0}

    default_latin_rhythm = {'Standard Waltz': 0, 'Standard Tango': 0, 'Standard Foxtrot': 0, 'Standard Quickstep': 0, 'Standard Viennese Waltz': 0,
                      'Smooth Waltz': 0, 'Smooth Tango': 0, 'Smooth Foxtrot': 0, 'Smooth Viennese Waltz': 0,
                      'Latin Cha Cha': 1, 'Latin Rumba': 1, 'Latin Samba': 1, 'Latin Jive': 1,
                      'Rhythm Cha Cha': 1, 'Rhythm Rumba': 1, 'Rhythm Swing': 1, 'Rhythm Mambo': 1,
                      'Nightclub Salsa': 0, 'Nightclub Bachata': 0, 'Nightclub Merengue': 0}

    default_nightclub = {'Standard Waltz': 0, 'Standard Tango': 0, 'Standard Foxtrot': 0, 'Standard Quickstep': 0, 'Standard Viennese Waltz': 0,
                      'Smooth Waltz': 0, 'Smooth Tango': 0, 'Smooth Foxtrot': 0, 'Smooth Viennese Waltz': 0,
                      'Latin Cha Cha': 0, 'Latin Rumba': 0, 'Latin Samba': 0, 'Latin Jive': 0,
                      'Rhythm Cha Cha': 0, 'Rhythm Rumba': 0, 'Rhythm Swing': 0, 'Rhythm Mambo': 0,
                      'Nightclub Salsa': 1, 'Nightclub Bachata': 1, 'Nightclub Merengue': 1}

    print("Welcome to Ballroom Shuffle!")
    print("1: Create new playlist")
    print("2: Delete existing playlist")
    print("3: Delete all temporary playlists")
    print("4: Custom playback")
    action = input("What would you like to do? ")
    print('===========================')

    if action == '1':
        ballroom_shuffle.load_ballroom_playlists()
        print("1: Rounds (Standard, Smooth, Latin, Rhythm)")
        print("2: Standard/Smooth (Standard and Smooth only)")
        print("3: Latin/Rhythm (Latin and Rhythm only)")
        print("4: Custom")

        playlist_type = input("Please choose your preferred styles and dances to include in your playlist from the choices above: ")
        print('===========================')
        playlist_name = input("Please enter the name for your new playlist: ")
        print('===========================')

        if playlist_type == '1':
            print(f"Creating Rounds playlist named {playlist_name} - Temporary")
            ballroom_shuffle.create_playlist(f"{playlist_name} - Temporary", default_rounds)
        elif playlist_type == '2':
            print(f"Creating Standard/Smooth playlist named {playlist_name} - Temporary")
            ballroom_shuffle.create_playlist(f"{playlist_name} - Temporary", default_standard_smooth)
        elif playlist_type == '3':
            print(f"Creating Latin/Rhythm playlist named {playlist_name} - Temporary")
            ballroom_shuffle.create_playlist(f"{playlist_name} - Temporary", default_latin_rhythm)
        elif playlist_type == '4':
            print("Please enter the number of songs you would like for each Style and Dance.")
            num_standard_waltz = int(input(f"Standard Waltz (default = 0/{len(ballroom_shuffle.standard_waltz)}): ") or '0')

            num_standard_tango = int(input(f"Standard Tango (default = 0/{len(ballroom_shuffle.standard_tango)}): ") or '0')

            num_standard_foxtrot = int(input(f"Standard Foxtrot (default = 0/{len(ballroom_shuffle.standard_foxtrot)}): ") or '0')

            num_standard_quickstep = int(input(f"Standard Quickstep (default = 0/{len(ballroom_shuffle.standard_quickstep)}): ") or '0')

            num_standard_v_waltz = int(input(f"Standard Viennese Waltz (default = 0/{len(ballroom_shuffle.standard_v_waltz)}): ") or '0')

            num_smooth_waltz = int(input(f"Smooth Waltz (default = 0/{len(ballroom_shuffle.smooth_waltz)}): ") or '0')

            num_smooth_tango = int(input(f"Smooth Tango (default = 0/{len(ballroom_shuffle.smooth_tango)}): ") or '0')

            num_smooth_foxtrot = int(input(f"Smooth Foxtrot (default = 0/{len(ballroom_shuffle.smooth_foxtrot)}): ") or '0')

            num_smooth_v_waltz = int(input(f"Smooth Viennese Waltz (default = 0/{len(ballroom_shuffle.smooth_v_waltz)}): ") or '0')

            num_latin_cha_cha = int(input(f"Latin Cha Cha (default = 0/{len(ballroom_shuffle.latin_cha_cha)}): ") or '0')

            num_latin_rumba = int(input(f"Latin Rumba (default = 0/{len(ballroom_shuffle.latin_rumba)}): ") or '0')

            num_latin_samba = int(input(f"Latin Samba (default = 0/{len(ballroom_shuffle.latin_samba)}): ") or '0')

            num_latin_jive = int(input(f"Latin Jive (default = 0/{len(ballroom_shuffle.latin_jive)}): ") or '0')

            num_rhythm_cha_cha = int(input(f"Rhythm Cha Cha (default = 0/{len(ballroom_shuffle.rhythm_cha_cha)}): ") or '0')

            num_rhythm_rumba = int(input(f"Rhythm Rumba (default = 0/{len(ballroom_shuffle.rhythm_rumba)}): ") or '0')

            num_rhythm_swing = int(input(f"Rhythm Swing (default = 0/{len(ballroom_shuffle.rhythm_swing)}): ") or '0')

            num_rhythm_mambo = int(input(f"Rhythm Mambo (default = 0/{len(ballroom_shuffle.rhythm_mambo)}): ") or '0')

            num_nightclub_salsa = int(input(f"Nightclub Salsa (default = 0/{len(ballroom_shuffle.nightclub_salsa)}): ") or '0')

            num_nightclub_bachata = int(input(f"Nightclub Bachata (default = 0/{len(ballroom_shuffle.nightclub_bachata)}): ") or '0')

            num_nightclub_merengue = int(input(f"Nightclub Merengue (default = 0/{len(ballroom_shuffle.nightclub_merengue)}): ") or '0')

            custom_playlist = {'Standard Waltz': num_standard_waltz, 'Standard Tango': num_standard_tango, 'Standard Foxtrot': num_standard_foxtrot, 'Standard Quickstep': num_standard_quickstep, 'Standard Viennese Waltz': num_standard_v_waltz,
                            'Smooth Waltz': num_smooth_waltz, 'Smooth Tango': num_smooth_tango, 'Smooth Foxtrot': num_smooth_foxtrot, 'Smooth Viennese Waltz': num_smooth_v_waltz,
                            'Latin Cha Cha': num_latin_cha_cha, 'Latin Rumba': num_latin_rumba, 'Latin Samba': num_latin_samba, 'Latin Jive': num_latin_jive,
                            'Rhythm Cha Cha': num_rhythm_cha_cha, 'Rhythm Rumba': num_rhythm_rumba, 'Rhythm Swing': num_rhythm_swing, 'Rhythm Mambo': num_rhythm_mambo,
                            'Nightclub Salsa': num_nightclub_salsa, 'Nightclub Bachata': num_nightclub_bachata, 'Nightclub Merengue': num_nightclub_merengue}

            ballroom_shuffle.create_playlist(f"{playlist_name} - Temporary", custom_playlist)
    elif action == '2':
        pass
    elif action == '3':
        ballroom_shuffle.delete_temporary_playlists()
    elif action == '4':
        ballroom_shuffle.custom_playback()

    '''
    # TODO: This is for adding songs to an existing playlist or randomly selecting new songs after presenting the selection to user
    current_playlist_songs = [song['name'] for song in ballroom_shuffle.get_playlist_tracks('test')]
    print(f"Current playlist songs: {current_playlist_songs}")
    print(f'===================')
    for song in random_latin_cha:
        if ballroom_shuffle.allow_duplicates or (song['name'] not in current_playlist_songs):
            print(f"Adding {song['name']} by {song['artists'][0]['name']} to playlist")
            songs_to_add_to_playlist.append(song['id'])
        elif song['name'] in current_playlist_songs:
            print(f"{song['name']} is already in the playlist")
            new_song = np.random.choice(latin_cha, replace=False)
            while new_song in current_playlist_songs:
                new_song = np.random.choice(latin_cha, replace=False)
            print(f"Adding {new_song['name']} by {new_song['artists'][0]['name']} to playlist instead")
            songs_to_add_to_playlist.append(new_song['id'])
        print('-------------------')
    '''
    #print(f"Adding {latin_cha[0]['track']['name']} by {latin_cha[0]['track']['artists'][0]['name']}")

# TODO: Ensure that random songs being added to the playlist do not already exist in the playlist unless the user specifies that duplicates are enabled. If duplicates are not enabled, randomly choose a new song
# TODO: Custom ordering of playlist styles and dances