from cat.mad_hatter.decorators import tool, hook
import os.path
import json

def get_settings():
    if os.path.isfile("cat/plugins/the-catSCII-artist/settings.json"):
        with open("cat/plugins/the-catSCII-artist/settings.json", "r") as json_file:
            settings = json.load(json_file)
    else:
        with open("cat/plugins/the-catSCII-artist/settings.json", "r") as json_file:
            settings = json.load(json_file)
    return settings