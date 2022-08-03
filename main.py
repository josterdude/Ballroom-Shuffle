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

    def create_playlist(self, playlist_name, preferences, shuffle=False):
        # Create a playlist called "test"
        ballroom_shuffle.sp.user_playlist_create(ballroom_shuffle.user_id, playlist_name + ' - Temporary')

        # Ensure newly created playlist is included in dictionary containing all playlists
        ballroom_shuffle.update_all_playlists()
        all_playlist_names = self.all_playlists.keys()
        if playlist_name in all_playlist_names:
            print(f"The provided playlist name ({playlist_name}) is already taken. Please provide a new playlist name.")
            return

        # Populate new playlist with songs
        songs_to_add_to_playlist = []

        if preferences.get('Standard Waltz') > 0:
            standard_waltz = ballroom_shuffle.get_style_dance_tracks('Standard', 'Waltz')
            max_num_standard_waltz_songs = len(standard_waltz)
            if preferences.get('Standard Waltz') <= max_num_standard_waltz_songs:
                songs_to_add_to_playlist += np.random.choice(standard_waltz, size = preferences.get('Standard Waltz'), replace = False)
            else:
                print(f"The number of Standard Waltz songs chosen ({preferences.get('Standard Waltz')} exceeds the maximum number of Standard Waltz songs available. Please enter a value less than or equal to {max_num_standard_waltz_songs}.")

        if preferences.get('Standard Tango') > 0:
            standard_tango = ballroom_shuffle.get_style_dance_tracks('Standard', 'Tango')
            max_num_standard_tango_songs = len(standard_tango)
            if preferences.get('Standard Tango') <= max_num_standard_tango_songs:
                songs_to_add_to_playlist += np.random.choice(standard_tango, size = preferences.get('Standard Tango'), replace = False)
            else:
                print(f"The number of Standard Tango songs chosen ({preferences.get('Standard Tango')} exceeds the maximum number of Standard Tango songs available. Please enter a value less than or equal to {max_num_standard_tango_songs}.")

        if preferences.get('Standard Foxtrot') > 0:
            standard_foxtrot = ballroom_shuffle.get_style_dance_tracks('Standard', 'Foxtrot')
            max_num_standard_foxtrot_songs = len(standard_foxtrot)
            if preferences.get('Standard Foxtrot') <= max_num_standard_foxtrot_songs:
                songs_to_add_to_playlist += np.random.choice(standard_foxtrot, size = preferences.get('Standard Foxtrot'), replace = False)
            else:
                print(f"The number of Standard Foxtrot songs chosen ({preferences.get('Standard Foxtrot')} exceeds the maximum number of Standard Foxtrot songs available. Please enter a value less than or equal to {max_num_standard_foxtrot_songs}.")

        if preferences.get('Standard Quickstep') > 0:
            standard_quickstep = ballroom_shuffle.get_style_dance_tracks('Standard', 'Quickstep')
            max_num_standard_quickstep_songs = len(standard_quickstep)
            if preferences.get('Standard Quickstep') <= max_num_standard_quickstep_songs:
                songs_to_add_to_playlist += np.random.choice(standard_quickstep, size = preferences.get('Standard Quickstep'), replace = False)
            else:
                print(f"The number of Standard Quickstep songs chosen ({preferences.get('Standard Quickstep')} exceeds the maximum number of Standard Quickstep songs available. Please enter a value less than or equal to {max_num_standard_quickstep_songs}.")

        if preferences.get('Standard Viennese Waltz') > 0:
            standard_v_waltz = ballroom_shuffle.get_style_dance_tracks('Standard', 'Viennese Waltz')
            max_num_standard_v_waltz_songs = len(standard_v_waltz)
            if preferences.get('Standard Viennese Waltz') <= max_num_standard_v_waltz_songs:
                songs_to_add_to_playlist += np.random.choice(standard_v_waltz, size = preferences.get('Standard Viennese Waltz'), replace = False)
            else:
                print(f"The number of Standard Viennese Waltz songs chosen ({preferences.get('Standard Viennese Waltz')} exceeds the maximum number of Standard Viennese Waltz songs available. Please enter a value less than or equal to {max_num_standard_v_waltz_songs}.")

        if preferences.get('Smooth Waltz') > 0:
            smooth_waltz = ballroom_shuffle.get_style_dance_tracks('Smooth', 'Waltz')
            max_num_smooth_waltz_songs = len(smooth_waltz)
            if preferences.get('Smooth Waltz') <= max_num_smooth_waltz_songs:
                songs_to_add_to_playlist += np.random.choice(smooth_waltz, size = preferences.get('Smooth Waltz'), replace = False)
            else:
                print(f"The number of Smooth Waltz songs chosen ({preferences.get('Standard Waltz')} exceeds the maximum number of Smooth Waltz songs available. Please enter a value less than or equal to {max_num_smooth_waltz_songs}.")

        if preferences.get('Smooth Tango') > 0:
            smooth_tango = ballroom_shuffle.get_style_dance_tracks('Smooth', 'Tango')
            max_num_smooth_tango_songs = len(smooth_tango)
            if preferences.get('Smooth Tango') <= max_num_smooth_tango_songs:
                songs_to_add_to_playlist += np.random.choice(smooth_tango, size = preferences.get('Smooth Tango'), replace = False)
            else:
                print(f"The number of Smooth Tango songs chosen ({preferences.get('Smooth Tango')} exceeds the maximum number of Smooth Tango songs available. Please enter a value less than or equal to {max_num_smooth_tango_songs}.")

        if preferences.get('Smooth Foxtrot') > 0:
            smooth_foxtrot = ballroom_shuffle.get_style_dance_tracks('Smooth', 'Foxtrot')
            max_num_smooth_foxtrot_songs = len(smooth_foxtrot)
            if preferences.get('Smooth Foxtrot') <= max_num_smooth_foxtrot_songs:
                songs_to_add_to_playlist += np.random.choice(smooth_foxtrot, size = preferences.get('Smooth Foxtrot'), replace = False)
            else:
                print(f"The number of Smooth Foxtrot songs chosen ({preferences.get('Smooth Foxtrot')} exceeds the maximum number of Smooth Foxtrot songs available. Please enter a value less than or equal to {max_num_smooth_foxtrot_songs}.")

        if preferences.get('Smooth Viennese Waltz') > 0:
            smooth_v_waltz = ballroom_shuffle.get_style_dance_tracks('Smooth', 'Viennese Waltz')
            max_num_smooth_v_waltz_songs = len(smooth_v_waltz)
            if preferences.get('Smooth Viennese Waltz') <= max_num_smooth_v_waltz_songs:
                songs_to_add_to_playlist += np.random.choice(smooth_v_waltz, size = preferences.get('Smooth Viennese Waltz'), replace = False)
            else:
                print(f"The number of Smooth Viennese Waltz songs chosen ({preferences.get('Smooth Viennese Waltz')} exceeds the maximum number of Smooth Viennese Waltz songs available. Please enter a value less than or equal to {max_num_smooth_v_waltz_songs}.")

        if preferences.get('Latin Cha Cha') > 0:
            latin_cha_cha = ballroom_shuffle.get_style_dance_tracks('Latin', 'Cha Cha')
            max_num_latin_cha_cha_songs = len(latin_cha_cha)
            if preferences.get('Latin Cha Cha') <= max_num_latin_cha_cha_songs:
                songs_to_add_to_playlist += np.random.choice(latin_cha_cha, size = preferences.get('Latin Cha Cha'), replace = False)
            else:
                print(f"The number of Latin Cha Cha songs chosen ({preferences.get('Latin Cha Cha')} exceeds the maximum number of Latin Cha Cha songs available. Please enter a value less than or equal to {max_num_latin_cha_cha_songs}.")

        if preferences.get('Latin Rumba') > 0:
            latin_rumba = ballroom_shuffle.get_style_dance_tracks('Latin', 'Rumba')
            max_num_latin_rumba_songs = len(latin_rumba)
            if preferences.get('Latin Rumba') <= max_num_latin_rumba_songs:
                songs_to_add_to_playlist += np.random.choice(latin_rumba, size = preferences.get('Latin Rumba'), replace = False)
            else:
                print(f"The number of Latin Rumba songs chosen ({preferences.get('Latin Rumba')} exceeds the maximum number of Latin Rumba songs available. Please enter a value less than or equal to {max_num_latin_rumba_songs}.")

        if preferences.get('Latin Samba') > 0:
            latin_samba = ballroom_shuffle.get_style_dance_tracks('Latin', 'Samba')
            max_num_latin_samba_songs = len(latin_samba)
            if preferences.get('Latin Samba') <= max_num_latin_samba_songs:
                songs_to_add_to_playlist += np.random.choice(latin_samba, size = preferences.get('Latin Samba'), replace = False)
            else:
                print(f"The number of Latin Samba songs chosen ({preferences.get('Latin Samba')} exceeds the maximum number of Latin Samba songs available. Please enter a value less than or equal to {max_num_latin_samba_songs}.")

        if preferences.get('Latin Jive') > 0:
            latin_jive = ballroom_shuffle.get_style_dance_tracks('Latin', 'Jive')
            max_num_latin_jive_songs = len(latin_jive)
            if preferences.get('Latin Jive') <= max_num_latin_jive_songs:
                songs_to_add_to_playlist += np.random.choice(latin_jive, size = preferences.get('Latin Jive'), replace = False)
            else:
                print(f"The number of Latin Jive songs chosen ({preferences.get('Latin Jive')} exceeds the maximum number of Latin Jive songs available. Please enter a value less than or equal to {max_num_latin_jive_songs}.")

        if preferences.get('Rhythm Cha Cha') > 0:
            rhythm_cha_cha = ballroom_shuffle.get_style_dance_tracks('Rhythm', 'Cha Cha')
            max_num_rhythm_cha_cha_songs = len(rhythm_cha_cha)
            if preferences.get('Rhythm Cha Cha') <= max_num_rhythm_cha_cha_songs:
                songs_to_add_to_playlist += np.random.choice(rhythm_cha_cha, size = preferences.get('Rhythm Cha Cha'), replace = False)
            else:
                print(f"The number of Rhythm Cha Cha songs chosen ({preferences.get('Rhythm Cha Cha')} exceeds the maximum number of Rhythm Cha Cha songs available. Please enter a value less than or equal to {max_num_rhythm_cha_cha_songs}.")

        if preferences.get('Rhythm Rumba') > 0:
            rhythm_rumba = ballroom_shuffle.get_style_dance_tracks('Rhythm', 'Rumba')
            max_num_rhythm_rumba_songs = len(rhythm_rumba)
            if preferences.get('Rhythm Rumba') <= max_num_rhythm_rumba_songs:
                songs_to_add_to_playlist += np.random.choice(rhythm_rumba, size = preferences.get('Rhythm Rumba'), replace = False)
            else:
                print(f"The number of Rhythm Rumba songs chosen ({preferences.get('Rhythm Rumba')} exceeds the maximum number of Rhythm Rumba songs available. Please enter a value less than or equal to {max_num_rhythm_rumba_songs}.")

        if preferences.get('Rhythm Swing') > 0:
            rhythm_swing = ballroom_shuffle.get_style_dance_tracks('Rhythm', 'Swing')
            max_num_rhythm_swing_songs = len(rhythm_swing)
            if preferences.get('Rhythm Swing') <= max_num_rhythm_swing_songs:
                songs_to_add_to_playlist += np.random.choice(rhythm_swing, size = preferences.get('Rhythm Swing'), replace = False)
            else:
                print(f"The number of Rhythm Swing songs chosen ({preferences.get('Rhythm Swing')} exceeds the maximum number of Rhythm Swing songs available. Please enter a value less than or equal to {max_num_rhythm_swing_songs}.")

        if preferences.get('Rhythm Mambo') > 0:
            rhythm_mambo = ballroom_shuffle.get_style_dance_tracks('Rhythm', 'Mambo')
            max_num_rhythm_mambo_songs = len(rhythm_mambo)
            if preferences.get('Rhythm Mambo') <= max_num_rhythm_mambo_songs:
                songs_to_add_to_playlist += np.random.choice(rhythm_mambo, size = preferences.get('Rhythm Mambo'), replace = False)
            else:
                print(f"The number of Rhythm Mambo songs chosen ({preferences.get('Rhythm Mambo')} exceeds the maximum number of Rhythm Mambo songs available. Please enter a value less than or equal to {max_num_rhythm_mambo_songs}.")

        if preferences.get('Nightclub Salsa') > 0:
            nightclub_salsa = ballroom_shuffle.get_style_dance_tracks('Nightclub', 'Salsa')
            max_num_nightclub_salsa_songs = len(nightclub_salsa)
            if preferences.get('Nightclub Salsa') <= max_num_nightclub_salsa_songs:
                songs_to_add_to_playlist += np.random.choice(nightclub_salsa, size = preferences.get('Nightclub Salsa'), replace = False)
            else:
                print(f"The number of Nightclub Salsa songs chosen ({preferences.get('Nightclub Salsa')} exceeds the maximum number of Nightclub Salsa songs available. Please enter a value less than or equal to {max_num_nightclub_salsa_songs}.")

        if preferences.get('Nightclub Bachata') > 0:
            nightclub_bachata = ballroom_shuffle.get_style_dance_tracks('Nightclub', 'Bachata')
            max_num_nightclub_bachata_songs = len(nightclub_bachata)
            if preferences.get('Nightclub Bachata') <= max_num_nightclub_bachata_songs:
                songs_to_add_to_playlist += np.random.choice(nightclub_bachata, size = preferences.get('Nightclub Bachata'), replace = False)
            else:
                print(f"The number of Nightclub Bachata songs chosen ({preferences.get('Nightclub Bachata')} exceeds the maximum number of Nightclub Bachata songs available. Please enter a value less than or equal to {max_num_nightclub_bachata_songs}.")

        if preferences.get('Nightclub Merengue') > 0:
            nightclub_merengue = ballroom_shuffle.get_style_dance_tracks('Nightclub', 'Merengue')
            max_num_nightclub_merengue_songs = len(nightclub_merengue)
            if preferences.get('Nightclub Merengue') <= max_num_nightclub_merengue_songs:
                songs_to_add_to_playlist += np.random.choice(nightclub_merengue, size = preferences.get('Nightclub Merengue'), replace = False)
            else:
                print(f"The number of Nightclub Merengue songs chosen ({preferences.get('Nightclub Merengue')} exceeds the maximum number of Nightclub Merengue songs available. Please enter a value less than or equal to {max_num_nightclub_merengue_songs}.")

        if shuffle:
            songs_to_add_to_playlist = np.random.shuffle(songs_to_add_to_playlist)

        ballroom_shuffle.sp.playlist_add_items(ballroom_shuffle.all_playlists[playlist_name + ' - Temporary']['id'], songs_to_add_to_playlist)

    # TODO: "Save the playlist" by renaming with the function user_playlist_change_details(user, playlist_id, name=None, public=True)

    def delete_playlist(self, playlist_name):
        # Ensure all playlist information is updated
        ballroom_shuffle.update_all_playlists()

        all_playlist_names = self.all_playlists.keys()
        if playlist_name in all_playlist_names:
            print(f"Removing playlist: {playlist_name}")
            ballroom_shuffle.sp.current_user_unfollow_playlist(self.all_playlists.get(playlist_name)['id'])
            self.all_playlists.pop(playlist_name)

    def delete_temporary_playlists(self):
        # Ensure all playlist information is updated
        ballroom_shuffle.update_all_playlists()

        for playlist_name, playlist_details in self.all_playlists.items():
            if 'Temporary' in playlist_name:
                print(f"Removing playlist: {playlist_name}")
                ballroom_shuffle.sp.current_user_unfollow_playlist(playlist_details['id'])
                self.all_playlists.pop(playlist_name)

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