from cgitb import html
from flask import Flask
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('/main.html')

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    print(request.args)
    StandardWaltz = request.args.get("StandardWaltz")
    print(StandardWaltz)
    return render_template('/custom.html')



@app.route('/playlist')
def playlist():
    return render_template('/playlist.html')