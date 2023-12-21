from cat.mad_hatter.decorators import tool, hook, plugin
import cowsay
import random
import requests
from cat.log import log
import json
from pydantic import BaseModel, Field

class MySettings(BaseModel):
    NINJAS_API_KEY: str = Field(
        title="Paste your ninjas api key here",
        description="Put here your ninjas api key in order to use the plugin",
        default="""NINJAS_API_KEY""",
        extra={"type": "Text"}
    )

@plugin
def settings_schema():   
    return MySettings.schema()

def cat_one():
    return r"""
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
"""

def cat_two():
    return r"""
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------    
"""

def cat_three():
    return r"""
 /\_/\
( o.o )
 > ^ <
"""
animals = ['cow', 'fox', 'tux'] # default ascii art for cowsay.get_output_string()
cats = [cat_one(), cat_two(), cat_three()]

@tool(return_direct=True)
def the_catscii_artist(tool_input, cat):
    """
    Useful when you are asked for a random fact, a general fact, a fact. Input is always None.
    """
    limit = 1
    settings = cat.mad_hatter.get_plugin().load_settings()
    NINJAS_API_KEY = settings["NINJAS_API_KEY"]
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': NINJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        cat = random.choice(cats)
        res = json.loads(response.text)
        fact = res[0]["fact"]
        output = f"<pre>{cowsay.draw(fact, random.choice(cats), to_console=False)}</pre>"
    else:
        log.error("Error:", response.status_code, response.text)
        output = "No funny facts today, meowy."
    return output