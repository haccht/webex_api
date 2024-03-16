import os
from flask import Flask, request, redirect
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

load_dotenv()


oauth = OAuth2Session(
        os.environ['CLIENT_ID'],
        redirect_uri=os.environ['REDIRECT_URL'], scope=['spark:people_read'])

authorization_url, state = oauth.authorization_url(
        'https://webexapis.com/v1/authorize')


app = Flask(__name__)

@app.route("/webex/oauth2")
def webex_oauth2():
    return redirect(authorization_url)

@app.route("/webex/oauth2/callback")
def webex_oauth2_callback():
    return oauth.fetch_token(
        'https://webexapis.com/v1/access_token',
        code=request.args['code'],
        client_secret=os.environ['CLIENT_SECRET'])
