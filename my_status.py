from webexteamssdk import WebexTeamsAPI
from unicornhat import UnicornHatHD
from datetime import datetime
import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

access_token = os.getenv('ACCESS_TOKEN')
expires_at   = float(os.getenv('EXPIRES_AT'))

hat = UnicornHatHD()
now = datetime.now()


try:
    if expires_at - now.timestamp() < 86400.0:
        client_id     = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        refresh_token = os.getenv('REFRESH_TOKEN')

        api = WebexTeamsAPI(access_token=access_token)
        token = api.access_tokens.refresh(client_id, client_secret, refresh_token)

        print(f"{now} refreshing access_token")
        access_token = token.access_token

        dotenv.set_key(dotenv_file, "ACCESS_TOKEN",  token.access_token)
        dotenv.set_key(dotenv_file, "REFRESH_TOKEN", token.refresh_token)
        dotenv.set_key(dotenv_file, "EXPIRES_AT",    str(now.timestamp() + token.expires_in))

    api = WebexTeamsAPI(access_token=access_token)
    data = api.people.me()

    print(f"{now} {data.userName} status={data.status}")
    if data.status in ["call", "DoNotDisturb", "meeting", "presenting", "unknown"]:
        hat.draw_emoji('microphone')
    else:
        hat.clear()
except:
    hat.draw_emoji('error')
