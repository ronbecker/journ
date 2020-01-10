---
layout: default
---

### What is journ?
Short and sweet? journ is a command line journal written in Python.

journ is completely run in your terminal. To use it after installing, just type journ in your terminal, and hit enter. Currently journ only uses the file journ.txt that it creates the first time you run it. In the future I want to add the ability to choose where you want your file, and what you want to name it. journ will append each new entry to the bottom of your journal file, along with the date and time the entry was created.

You can check for, and apply available updates by running `journ-upgrade` in terminal.

It's a really simple program so I don't forsee any problems. But, if you have any issues please check the [Issues](https://github.com/ronbecker/journ/issues) on GitHub. If you don't see your issue there then feel free to [create a new one](https://github.com/ronbecker/journ/issues/new).

### Getting Started
1. Install journ using `pip`:

      `pip install journ`

2. Run `journ` in your terminal. If this is your first time using journ, it will greet you, and show you where your journal file will be located.

3. Type your new journal entry after the `> ` prompt, and when you are finished hit enter.

You can open your journal in any text viewer, or you can use `cat` to view it in your terminal.

### Changelog
You can view the [Changelog](https://github.com/ronbecker/journ/blob/master/CHANGELOG.md) on GitHub.
