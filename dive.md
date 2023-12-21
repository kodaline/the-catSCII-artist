<div align="center">
<pre>
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
</pre>
</div>

# Dive into

## Repo structure

```
the-catscii-artist
├── cats
│   ├── cat.txt
│   ├── cat2.txt
│   ├── cat3.txt
├── img
│   ├── catscii_artist_setting.png
│   ├── the_catscii_artist_logo.png
├── changelog.md
├── dive_into.md
├── plugin.json
├── README.md
├── requirements.txt
├──  settings.json
└── the_catscii_artist.py

```

## Overview

### Plugin settings

The plugin sets the following settings:

- `NINJAS_API_KEY`: your ninja api key, and

- `cats`: activate or deactivate the use of cats ascii art instead of default cowsay ones.

<p>
  <img src="https://raw.githubusercontent.com/kodaline/the-catSCII-artist/main/img/the_catscii_artist_settings.png"/>
</p>

### Cat Decorators

The plugin makes use of `tool` and `plugin` decorators (*@tool* and *@plugin*) of the cat's `mad_hatter`.

The `tool` decorator is used in the one and only tool of the plugin, called `the_catscii_artist`, that uses the option `return_direct=True` useful to return directly the output to the user, skipping the cat's llm chain.

The tool `docstring` is really important because it triggers the use of the tool, the choice of triggering it or not is made by the agent.

In this case the docstring is:

```
"""
Useful when you are asked for a random fact, a general fact, a fact.
Input is always None.
"""
```

It basically says to the agent: trigger `the_catscii_artist` tool if the user asks you a fact.

### Other Imports

The following imports are used:

- `cowsay`: the *artist* behind the plugin

- `random`: useful to choose a random ascii art for the fact

- `requests`: makes the request to ninja for the random fact

- `BaseModel, Field` from `pydantic`: useful for the plugin settings structure

To setup the settings the `plugin` decorator (*@plugin*) is used to override `settings_schema` method using pydantic's `MySettings` class to define the plugin settings.

### Cowsay usage

The plugin makes use of the two main methods of the cowsay package:

|        name       |                 usage                 |                    params                   |
|:-----------------:|:-------------------------------------:|:-------------------------------------------:|
|        draw       |     used for the custom ascii art     | fact, random.choice(cats), to_console=False |
| get_output_string | used for the cowsay default ascii art |         random.choice(animals), fact        |

The main difference between the two is that the `draw` accepts custom ascii art.

## Credits

The cat ascii art at the beginning of the readme is by [Felix Lee](https://montcs.bloomu.edu/Graphics/ascii-art.html).
