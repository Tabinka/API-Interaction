import requests

token = "xxxx"
emoji_api = "https://emoji-api.com/emojis"

hand_waves = requests.get(emoji_api, params={"search": "waving", "access_key": token}).json()
world_emojis = requests.get(emoji_api, params={"search": "globe", "access_key": token}).json()
world = world_emojis[0]['character']

for hand_wave in hand_waves:
    print(hand_wave['character'] + world)