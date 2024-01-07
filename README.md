<p align="center">
  <img src="https://github.com/kodaline/the-catSCII-artist/blob/main/img/the_catscii_artist_logo.png?raw=true" />
</p>

# Introduction

The *catSCII artist* is a plugin that gives you random facts and uses the `cowsay` package giving them back in ascii art.
Ask the Cheshire Cat for a random fact and wait!

# Requirement

## Cheshire Cat AI

To start using the plugin you need to have the Cheshire Cat AI up and running. To do so visit the repository [here](https://github.com/cheshire-cat-ai/core) and follow the easy steps to install it.

Once you have setup the `cat`, you need to:

1. Install the plugin (`Admin page` -> `Plugins tab`)

2. Set your NINJAS_API_KEY in the plugin settings ([ninjas](https://api-ninjas.com)) or use the `danger_zone` by generating facts directly with the cat!

3. Optionally, deactivate the cats ascii art if you want to use default cowsay animals

4. and then just have fun!

If you want to dive into the plugin, consider taking a look at [dive into](dive.md) readme.

# Credits

`cowsay` for GNU/Linux was initially written in perl by Tony Monroe. More info [here](https://en.wikipedia.org/wiki/Cowsay).

# TODO

- 🔲 add custom ascii art support by using the plugin settings or by directly uploading the `.txt` file into the cat's declarative memory

- 🔲 use the files into `cats` folder to import the cats ascii arts

- 🔲 translation of the random fact in a custom language

- 🔲 when generating facts with the cat, give the list of facts already said, so to exclude repetitions

- ✅ eventually drop the use of external API service for the random facts (ninja)
