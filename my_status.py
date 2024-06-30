from webexteamssdk import WebexTeamsAPI
from unicornhat import UnicornHatHD

api = WebexTeamsAPI()

data = api.people.me()
print(f"{data.userName} status={data.status}")


# render emoji
hat = UnicornHatHD()
if data.status in ["call", "DoNotDisturb", "meeting", "presenting", "unknown"]:
    hat.draw_emoji('microphone')
else:
    hat.clear()
