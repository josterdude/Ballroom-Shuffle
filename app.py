from cgitb import html
from flask import Flask
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from main import Ballroom_Shuffle
from datetime import datetime

app = Flask(__name__)
ballroom_shuffle = Ballroom_Shuffle()
ballroom_shuffle.load_ballroom_playlists()
temporary_num = 1

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.form.get('playlist_type'):
        if request.form.get('playlist_type') == 'rounds':
            preferences = {'Standard Waltz': 1, 'Standard Tango': 1, 'Standard Foxtrot': 1, 'Standard Quickstep': 1, 'Standard Viennese Waltz': 1,
                        'Smooth Waltz': 1, 'Smooth Tango': 1, 'Smooth Foxtrot': 1, 'Smooth Viennese Waltz': 1,
                        'Latin Cha Cha': 1, 'Latin Rumba': 1, 'Latin Samba': 1, 'Latin Jive': 1,
                        'Rhythm Cha Cha': 1, 'Rhythm Rumba': 1, 'Rhythm Swing': 1, 'Rhythm Mambo': 1,
                        'Nightclub Salsa': 0, 'Nightclub Bachata': 0, 'Nightclub Merengue': 0}
            if request.form.get('Playlist Name') == '':
                playlist_name = "Temporary Rounds "
            else:
                playlist_name = request.form.get('Playlist Name')

        elif request.form.get('playlist_type') == 'standard/smooth':
            preferences = {'Standard Waltz': 1, 'Standard Tango': 1, 'Standard Foxtrot': 1, 'Standard Quickstep': 1, 'Standard Viennese Waltz': 1,
                        'Smooth Waltz': 1, 'Smooth Tango': 1, 'Smooth Foxtrot': 1, 'Smooth Viennese Waltz': 1,
                        'Latin Cha Cha': 0, 'Latin Rumba': 0, 'Latin Samba': 0, 'Latin Jive': 0,
                        'Rhythm Cha Cha': 0, 'Rhythm Rumba': 0, 'Rhythm Swing': 0, 'Rhythm Mambo': 0,
                        'Nightclub Salsa': 0, 'Nightclub Bachata': 0, 'Nightclub Merengue': 0}
            if request.form.get('Playlist Name') == '':
                playlist_name = "Temporary Standard/Smooth "
            else:
                playlist_name = request.form.get('Playlist Name')

        elif request.form.get('playlist_type') == 'latin/rhythm':
            preferences = {'Standard Waltz': 0, 'Standard Tango': 0, 'Standard Foxtrot': 0, 'Standard Quickstep': 0, 'Standard Viennese Waltz': 0,
                        'Smooth Waltz': 0, 'Smooth Tango': 0, 'Smooth Foxtrot': 0, 'Smooth Viennese Waltz': 0,
                        'Latin Cha Cha': 1, 'Latin Rumba': 1, 'Latin Samba': 1, 'Latin Jive': 1,
                        'Rhythm Cha Cha': 1, 'Rhythm Rumba': 1, 'Rhythm Swing': 1, 'Rhythm Mambo': 1,
                        'Nightclub Salsa': 0, 'Nightclub Bachata': 0, 'Nightclub Merengue': 0}
            if request.form.get('Playlist Name') == '':
                playlist_name = "Temporary Latin/Rhythm "
            else:
                playlist_name = request.form.get('Playlist Name') + " "

        elif request.form.get('playlist_type') == 'custom':
            if request.form.get('Playlist Name') == '':
                playlist_name = "Temporary Custom Playlist "
            else:
                playlist_name = request.form.get('Playlist Name') + " "
            return redirect(url_for('custom', playlist_name = playlist_name + datetime.now().strftime("%d/%m/%y %H:%M:%S")))

        return_code, return_msg, playlist_id = ballroom_shuffle.create_playlist(playlist_name + datetime.now().strftime("%d/%m/%y %H:%M:%S"), preferences)

        if return_code > 0:
            return render_template('/create_playlist_error.html', return_msg = return_msg)
        elif return_code == 0:
            return render_template('/display_playlist.html', playlist_id = playlist_id)

    return render_template('/main.html')

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    # Change "request.form" to "request.values" if breaks
    num_standard_waltz = int(request.form.get("Standard Waltz") or '0')
    num_standard_tango = int(request.form.get("Standard Tango") or '0')
    num_standard_foxtrot = int(request.form.get("Standard Foxtrot") or '0')
    num_standard_quickstep = int(request.form.get("Standard Quickstep") or '0')
    num_standard_v_waltz = int(request.form.get("Standard Viennese Waltz") or '0')
    num_smooth_waltz = int(request.form.get("Smooth Waltz") or '0')
    num_smooth_tango = int(request.form.get("Smooth Tango") or '0')
    num_smooth_foxtrot = int(request.form.get("Smooth Foxtrot") or '0')
    num_smooth_v_waltz = int(request.form.get("Smooth Viennese Waltz") or '0')
    num_latin_cha_cha = int(request.form.get("Latin Cha Cha") or '0')
    num_latin_rumba = int(request.form.get("Latin Rumba") or '0')
    num_latin_samba = int(request.form.get("Latin Samba") or '0')
    num_latin_jive = int(request.form.get("Latin Jive") or '0')
    num_rhythm_cha_cha = int(request.form.get("Rhythm Cha Cha") or '0')
    num_rhythm_rumba = int(request.form.get("Rhythm Rumba") or '0')
    num_rhythm_swing = int(request.form.get("Rhythm Swing") or '0')
    num_rhythm_mambo = int(request.form.get("Rhythm Mambo") or '0')
    num_nightclub_salsa = int(request.form.get("Nightclub Salsa") or '0')
    num_nightclub_bachata = int(request.form.get("Nightclub Bachata") or '0')
    num_nightclub_merengue = int(request.form.get("Nightclub Merengue") or '0')

    preferences = {'Standard Waltz': num_standard_waltz, 'Standard Tango': num_standard_tango, 'Standard Foxtrot': num_standard_foxtrot, 'Standard Quickstep': num_standard_quickstep, 'Standard Viennese Waltz': num_standard_v_waltz,
                    'Smooth Waltz': num_smooth_waltz, 'Smooth Tango': num_smooth_tango, 'Smooth Foxtrot': num_smooth_foxtrot, 'Smooth Viennese Waltz': num_smooth_v_waltz,
                    'Latin Cha Cha': num_latin_cha_cha, 'Latin Rumba': num_latin_rumba, 'Latin Samba': num_latin_samba, 'Latin Jive': num_latin_jive,
                    'Rhythm Cha Cha': num_rhythm_cha_cha, 'Rhythm Rumba': num_rhythm_rumba, 'Rhythm Swing': num_rhythm_swing, 'Rhythm Mambo': num_rhythm_mambo,
                    'Nightclub Salsa': num_nightclub_salsa, 'Nightclub Bachata': num_nightclub_bachata, 'Nightclub Merengue': num_nightclub_merengue}

    if request.method == "POST":
        return_code, return_msg, playlist_id = ballroom_shuffle.create_playlist(request.args.get("playlist_name"), preferences)

        if return_code > 0:
            return render_template('/create_playlist_error.html', return_msg = return_msg)
        elif return_code == 0:
            return render_template('/display_playlist.html', playlist_id = playlist_id)

    elif request.method == "GET":
        return render_template('/create_playlist.html', ballroom_shuffle = ballroom_shuffle, preferences = preferences)

@app.route('/playlist')
def playlist():
    return render_template('/display_playlist.html')