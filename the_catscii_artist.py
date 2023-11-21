from cat.mad_hatter.decorators import tool, hook, plugin
import cowsay
import random
import requests
from cat.log import log
import json
from pydantic import BaseModel, Field
from .hooks import get_settings

class MySettings(BaseModel):
    NINJAS_API_KEY: str = Field(
        title="Paste your ninjas api key here",
        description="Put here your ninjas api key in order to use the plugin",
        default="""NINJAS_API_KEY""",
        extra={"type": "TextArea"}
    )

@plugin
def settings_schema():   
    return MySettings.schema()

def cat_one():
    return r'''
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
'''

def cat_two():
    return r'''
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------    
'''

def cat_three():
    return r'''
 /\_/\
( o.o )
 > ^ <
'''
animals = ['cow', 'fox', 'tux']
cats = [cat_one(), cat_two(), cat_three()]

@tool
def the_catscii_artist(tool_input, cat):
    """Useful when you are asked for a random fact, a general fact, a fact. Input is always None.
    Print the fact always in a codeblock and well formatted way to display the ASCII art correctly.
    """
    limit = 1
    NINJAS_API_KEY = get_settings()["NINJAS_API_KEY"]
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': NINJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        cat = random.choice(cats)
        res = json.loads(response.text)
        fact = res[0]["fact"]
        output = cowsay.get_output_string(random.choice(animals), fact)
    else:
        log.error("Error:", response.status_code, response.text)
        output = "No funny facts today, meowy."
    log.error(output)
    return r'```\n{}```'.format(output)