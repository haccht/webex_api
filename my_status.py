import os
import json
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from unicornhat import UnicornHatHD


def token_save(token):
    with open(ACCESS_TOKEN_FILE) as fp:
        json.dump(token, fp, indent=2)


load_dotenv()
ACCESS_TOKEN_FILE = 'access_token.json'


# load access token
with open(ACCESS_TOKEN_FILE) as fp:
    token_map = json.load(fp)

oauth = OAuth2Session(
        os.environ['CLIENT_ID'],
        token=token_map,
        auto_refresh_kwargs={
            'client_id': os.environ['CLIENT_ID'],
            'client_secret': os.environ['CLIENT_SECRET']},
        auto_refresh_url='https://webexapis.com/v1/access_token',
        token_updater=token_save)

# query api
resp = oauth.get('https://webexapis.com/v1/people/me')
data = resp.json()

print(f"{data['userName']} status={data['status']}")


# render emoji
hat = UnicornHatHD()
if data["status"] in ["call", "DoNotDisturb", "meeting", "presenting", "unknown"]:
    hat.draw_emoji('microphone')
else:
    hat.clear()
