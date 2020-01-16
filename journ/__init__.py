"""
#---------------------------------------------------#
     journ v0.1.7 Copyright (c) 2020 Ron Becker
#---------------------------------------------------#


 journ is a command line journal program written in
 Python. It saves all your journal entries in a
 text file called journ.txt in your home directory.

 To begin using journ after installing it just type
 `journ` in terminal. A text input will appear and
 you can begin typing. After you are finished just
 hit enter. The new entry is automatically added to
 the end of journ.py with the date and time.

#---------------------------------------------------#
"""
import os
from time import gmtime, strftime
from pathlib import Path

def main():

    class App:
        def __init__(self, name, version, site, repo):
            self.name = name
            self.version = version
            self.site = site
            self.repo = repo

    app = App('journ', 'v0.1.7', 'https://ronbecker.github.io/journ', 'https://github.com/ronbecker/journ')
    # Set date and home folder varialbles
    today = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    home = str(Path.home())
    journ_file = home + "/journ.txt"

    print("")
    print("           Welcome to ", app.name, app.version)
    print("             Copyright (c) 2020\n\n")
    print("   Site: ", app.site)
    print("   Repo: ", app.repo)
    print("")
    # This chunk opens journ.txt in the users home directory
    # takes their input, and appends it to journ.txt along
    # with the date and time, and a blank line so that each
    # entry is a little more readable.
    with open (journ_file, "a") as journ_entry:
        journ_entry.write (str(today) + ": \n")
        journ_entry.write (input("> "))
        journ_entry.write ("\n\n")
        print("")
