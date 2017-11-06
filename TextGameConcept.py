# Just a couple of notes 11/2/17:
#
#   1. Much of the format displayed in each room (function) differ from each other. This inconsistency is due to
#       experimenting with different ways to make the function more efficient.
#
#   2. Everything in this project could probably be cleaner and more efficient if I used classes. My plan is to slowly
#       rewrite everything with classes.
#
#   3. Many of the loops have redundancies. Cleaning these up can be added to the to do list.

import os
import time
import TextGameFunctions

# Global variables
inventory = ['']
equippedItems = ['']
armor = ['']
gold = 0
health = 100

if __name__ == "__main__":
    TextGameFunctions.start()
    TextGameFunctions.startScreen()
