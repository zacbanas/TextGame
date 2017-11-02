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

# Global variables
inventory = ['']
equippedItems = ['']

def cyclelist(item, move):
    """Checks user input for acceptable moves contained in a list.
        If user input is acceptable, return True"""
    item = item
    for i in item:
        if i in move:
            return True
    return False


def checkinventory(item):
    """Checks the inventory for an item"""
    global inventory
    for i in inventory:
        if item == i:
            return True
    return False

# Just a place holder for now. Replace with a new room.
def ch2freedom():
    print("You are freeeeee")

def c1darkhole():
    """Chapter Two: Inside the dark hole after c1hallway"""
    global inventory

    # Acceptable items, actions and moves
    moves = ['moveto', 'proceed', 'continue', 'walk', 'go', 'to']
    entrance = ['light', 'opening', 'door', 'crack', 'hole', 'exit']
    actions = ['talk', 'approach', 'walk', 'speak']
    npc = ['npc', 'man', 'guy', 'figure', 'person', 'entity']
    npcavailable = True

    os.system('clear')

    # If use took the torch in c1hallway() then do this
    if checkinventory('torch') is True:
        print("You crouch down end enter the dark hole...")
        time.sleep(2)
        print('Your torch illuminates the room...')
        time.sleep(2)
        print("You appear to be inside of a dark moist cave...")
        time.sleep(2)
        print("You notice a faint light at the end of the cave...")
        time.sleep(2)
        print("A figure hiding behind a rock catches your attention")
        time.sleep(2)
        print("\nWhat do you want to do?")
        # Loop checks input for moves and actions
        while True:
            move = input('>> ').lower().replace(' ', '')
            # Check to see if the input is directed towards the npc
            if npcavailable is True:
                for action in actions:
                    if action in move and cyclelist(npc, move) is True:
                        print("The man looks up at you and lustfully gazes into your eyes...")
                        time.sleep(2)
                        print("\nMan: \"Why, hello musky spirit... I have been waiting for someone")
                        print("like you to come across my path... Here, I have a gift for you....\"")
                        time.sleep(3)
                        print("\nYou receive a Slimy Trinket")
                        inventory.append('slimytrinket')
                        time.sleep(2)
                        print("\nThe man laughs as he slowly fades out of existence...")
                        time.sleep(2)
                        print("The flame on your torch blows out...")
                        time.sleep(2)
                        print("You notice a faint light at the end of the cave...")
                        time.sleep(2)
                        print("\nWhat do you want to do?")
                        npcactive = False
                        # TODO: insert a move check here
                        move = input('>> ').lower().replace(' ', '')
            # Do this is if the input is directed to movement
            for mov in moves:
                if mov in move or cyclelist(entrance, move) is True:
                    if checkinventory('slimytrinket') is False:
                        print("You ignore the figure and make your way to the opening of the cave...")
                    ch2freedom()
                    return None
            # If the input is invalid, print this then re loop
            print("Not a valid input.")

    # If the user did not take the torch in ch1hallway()
    else:
        print("You crouch down end enter the dark hole...")
        time.sleep(2)
        print("It's too dark to see anything around you except for a faint light")
        print("in the distance...")
        time.sleep(2)
        print("\nWhat do you want to do?")
        # Loop checks input for moves
        while True:
            move = input('>> ').replace(' ', '')

            for mov in moves:
                if mov in move and cyclelist(entrance, move) is True:
                    ch2freedom()
                    return None
            print("Not a valid input.")



def c1hallway():
    """Chapter One: First hallway after start()"""
    global inventory

    # Acceptable items, actions, and moves
    moves = ['go', 'forward', 'proceed', 'continue', 'walk', 'crawl']
    takeactions = ['grab', 'take', 'get', 'obtain', 'receive', ]
    items = ['torch']

    # Print Narration
    os.system('clear')
    print("A dim light starts to fill the room as you slowly open the door...")
    time.sleep(2)
    print('You step through the door way and enter into a long stone hall way')
    print("illuminated by a series of torches mounted along the walls...")
    time.sleep(2)
    print("The hall way doesn't appear to lead anywhere, except for a small")
    print("dark hole in the wall...")
    time.sleep(2)
    print("\nWhat do you want to do?")

    # Loop for user input
    while True:
        # Check to see if you have a torch in your inventory
        if checkinventory('torch') is False:
            move = input('>> ')
            move = move.lower().replace(' ', '')
            # Parts of this loop are redundant and probably unnecessary considering I have a function to loop through a
            #   list of items and actions. This was just for experimental reasons.
            for act in takeactions:
                if act in move and cyclelist(items, move):
                    inventory.append('torch')
                    print("A torch was added to your inventory")
                    move = input('>> ')
                    move = move.lower().replace(' ', '')
                    break
        else:
            move = input('>> ')
            move = move.lower().replace(' ', '')

        for mov in moves:
            if mov in move:
                c1darkhole()
                return None
        print("Not a valid input...")


def start():
    """Starts the beginning of the game."""
    # Acceptable moves
    moves = ['open', 'opendoor', 'openthedoor', 'walkthrough', 'continue', 'walk', 'go', 'forward']
    # Start narration
    os.system('clear')
    print("You wake up from what felt like an eternal sleep...")
    time.sleep(2)
    print("You seem to have lost all memories prior to this moment...")
    time.sleep(2)
    print("Your vision is foggy, but you make out the shape of a door")
    print("at the end of the room...")
    time.sleep(2)
    print("\nWhat do you want to do?")
    # Loop checks input for moves
    while True:
        move = input('>> ')
        move = move.lower().replace(' ', '')

        # Secret action in the beginning of the game. Because fuck it why not.
        if 'dunkirk' in move and 'bad' and 'sucks' in move:
            print("YOU DIED")
            exit()
        # Check to see if the user input contains an acceptable move
        for mov in moves:
            if mov in move:
                c1hallway()
                return None
        print("Not a valid input...")

if __name__ == "__main__":
    start()
