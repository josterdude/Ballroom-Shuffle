from cgitb import html
from flask import Flask
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('/main.html')

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    num_standard_waltz = int(request.args.get("Standard Waltz") or '0')
    num_standard_tango = int(request.args.get("Standard Tango") or '0')
    num_standard_foxtrot = int(request.args.get("Standard Foxtrot") or '0')
    num_standard_quickstep = int(request.args.get("Standard Quickstep") or '0')
    num_standard_v_waltz = int(request.args.get("Standard Viennese Waltz") or '0')
    num_smooth_waltz = int(request.args.get("Smooth Waltz") or '0')
    num_smooth_tango = int(request.args.get("Smooth Tango") or '0')
    num_smooth_foxtrot = int(request.args.get("Smooth Foxtrot") or '0')
    num_smooth_v_waltz = int(request.args.get("Smooth Viennese Waltz") or '0')
    num_latin_cha_cha = int(request.args.get("Latin Cha Cha") or '0')
    num_latin_rumba = int(request.args.get("Latin Rumba") or '0')
    num_latin_samba = int(request.args.get("Latin Samba") or '0')
    num_latin_jive = int(request.args.get("Latin Jive") or '0')
    num_rhythm_cha_cha = int(request.args.get("Rhythm Cha Cha") or '0')
    num_rhythm_rumba = int(request.args.get("Rhythm Rumba") or '0')
    num_rhythm_swing = int(request.args.get("Rhythm Swing") or '0')
    num_rhythm_mambo = int(request.args.get("Rhythm Mambo") or '0')
    num_nightclub_salsa = int(request.args.get("Nightclub Salsa") or '0')
    num_nightclub_bachata = int(request.args.get("Nightclub Bachata") or '0')
    num_nightclub_merengue = int(request.args.get("Nightclub Merengue") or '0')

    preferences = {'Standard Waltz': num_standard_waltz, 'Standard Tango': num_standard_tango, 'Standard Foxtrot': num_standard_foxtrot, 'Standard Quickstep': num_standard_quickstep, 'Standard Viennese Waltz': num_standard_v_waltz,
                    'Smooth Waltz': num_smooth_waltz, 'Smooth Tango': num_smooth_tango, 'Smooth Foxtrot': num_smooth_foxtrot, 'Smooth Viennese Waltz': num_smooth_v_waltz,
                    'Latin Cha Cha': num_latin_cha_cha, 'Latin Rumba': num_latin_rumba, 'Latin Samba': num_latin_samba, 'Latin Jive': num_latin_jive,
                    'Rhythm Cha Cha': num_rhythm_cha_cha, 'Rhythm Rumba': num_rhythm_rumba, 'Rhythm Swing': num_rhythm_swing, 'Rhythm Mambo': num_rhythm_mambo,
                    'Nightclub Salsa': num_nightclub_salsa, 'Nightclub Bachata': num_nightclub_bachata, 'Nightclub Merengue': num_nightclub_merengue}

    return render_template('/custom.html')



@app.route('/playlist')
def playlist():
    return render_template('/playlist.html')