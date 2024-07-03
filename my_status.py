from webexteamssdk import WebexTeamsAPI
from unicornhat import UnicornHatHD

hat = UnicornHatHD()

try:
    api = WebexTeamsAPI()
    data = api.people.me()
    #print(f"{data.userName} status={data.status}")

    # render emoji
    if data.status in ["call", "DoNotDisturb", "meeting", "presenting", "unknown"]:
        hat.draw_emoji('microphone')
    else:
        hat.clear()
except:
    hat.draw_emoji('error')
