import json
from werkzeug.exceptions import HTTPException
from flask_oidc import OpenIDConnect
from flask import Flask, jsonify, redirect, render_template, url_for
from six.moves.urllib.parse import urlencode

# build Flask app
app = Flask(__name__)
# build OIDC object
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',    
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,       
})

oidc = OpenIDConnect(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
@oidc.require_login
def login():
    user = {"email": oidc.user_getfield('email')}
    return render_template('loggedIn.html', user=user)

@app.route('/logout')
def logout():
    oidc.logout()
    return render_template('home.html')