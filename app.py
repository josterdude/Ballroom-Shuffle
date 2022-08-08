from cgitb import html
from flask import Flask
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('/main.html')

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    num_standard_waltz = request.args.get("Standard Waltz")
    num_standard_tango = request.args.get("Standard Tango")
    num_standard_foxtrot = request.args.get("Standard Foxtrot")
    num_standard_quickstep = request.args.get("Standard Quickstep")
    num_standard_v_waltz = request.args.get("Standard Viennese Waltz")
    num_smooth_waltz = request.args.get("Smooth Waltz")
    num_smooth_tango = request.args.get("Smooth Tango")
    num_smooth_foxtrot = request.args.get("Smooth Foxtrot")
    num_smooth_v_waltz = request.args.get("Smooth Viennese Waltz")
    num_latin_cha_cha = request.args.get("Latin Cha Cha")
    num_latin_rumba = request.args.get("Latin Rumba")
    num_latin_samba = request.args.get("Latin Samba")
    num_latin_jive = request.args.get("Latin Jive")
    num_rhythm_cha_cha = request.args.get("Rhythm Cha Cha")
    num_rhythm_rumba = request.args.get("Rhythm Rumba")
    num_rhythm_swing = request.args.get("Rhythm Swing")
    num_rhythm_mambo = request.args.get("Rhythm Mambo")
    num_nightclub_salsa = request.args.get("Nightclub Salsa")
    num_nightclub_bachata = request.args.get("Nightclub Bachata")
    num_nightclub_merengue = request.args.get("Nightclub Merengue")

    preferences = {'Standard Waltz': num_standard_waltz, 'Standard Tango': num_standard_tango, 'Standard Foxtrot': num_standard_foxtrot, 'Standard Quickstep': num_standard_quickstep, 'Standard Viennese Waltz': num_standard_v_waltz,
                    'Smooth Waltz': num_smooth_waltz, 'Smooth Tango': num_smooth_tango, 'Smooth Foxtrot': num_smooth_foxtrot, 'Smooth Viennese Waltz': num_smooth_v_waltz,
                    'Latin Cha Cha': num_latin_cha_cha, 'Latin Rumba': num_latin_rumba, 'Latin Samba': num_latin_samba, 'Latin Jive': num_latin_jive,
                    'Rhythm Cha Cha': num_rhythm_cha_cha, 'Rhythm Rumba': num_rhythm_rumba, 'Rhythm Swing': num_rhythm_swing, 'Rhythm Mambo': num_rhythm_mambo,
                    'Nightclub Salsa': num_nightclub_salsa, 'Nightclub Bachata': num_nightclub_bachata, 'Nightclub Merengue': num_nightclub_merengue}

    print(preferences)
    return render_template('/custom.html')



@app.route('/playlist')
def playlist():
    return render_template('/playlist.html')