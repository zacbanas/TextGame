import TextGameConcept
import time
import os

def start():
    """Starts the beginning of the game."""
    # Acceptable moves
    moves = ['open', 'opendoor', 'openthedoor', 'walkthrough', 'continue', 'walk', 'go', 'forward']
    # Start narration
    #clearConsole()
    input('Press enter to start...')
    print("You wake up from what felt like an eternal sleep...")
    time.sleep(2)
    print("You seem to have lost all memories prior to this moment...")
    time.sleep(2)
    print("Your vision is foggy, but you make out the shape of a door")
    print("at the end of the room...")
    time.sleep(2)
    print("\nThe only thing to do is \'move forward\'")
    # Loop checks input for moves
    # Z - I changed this because it is more Pythonic, and easier to maintain because everything now falls under the same action.
    gameRunning = True
    while gameRunning == True:
        move = input('>> ')
        # Z - With these updates I had to remove the extra formatting because taking away the spaces wouldn't allow the user to move
        # Secret action in the beginning of the game. Because fuck it why not.
        if 'dunkirk' in move and 'bad' and 'sucks' in move:
            print("YOU DIED")
            gameRunning = False
        # Check to see if the user input contains an acceptable move
        elif move == 'Quit' or move == 'QUIT' or move == 'quit' or move == 'Q':
            gameRunning = False
        # Z - I changed this because it is more Pythonic, less code, simpler to read and still does what it was originally intended to do.
        elif move == 'move forward':
            c1hallway()
            return None
        else:
            print('You cannot do that..')
            time.sleep(1)
            print('Type: move forward')
def c1hallway():
    """Chapter One: First hallway after start()"""
    global inventory

    #Z- removed the action and items.

    #Print Narration
    #clearConsole()
    print("A dim light starts to fill the room as you slowly open the door...")
    time.sleep(2)
    print('You step through the door way and enter into a long stone hall way')
    print("illuminated by a series of torches mounted along the walls...")
    time.sleep(2)
    print("The hall way doesn't appear to lead anywhere, except for a small")
    print("dark hole in the wall...")
    time.sleep(2)
    # Z - We can't keep using open ended questions to continue the story.
    #print("\nWhat do you want to do?")
    print('You grab a torch off the wall and step cautiously towards the hole')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('You move the torch towards the opening')
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('A hand grabs the torch!')
    print('The wall starts to crumble before you')
    print('A noise pierces your ears')
    print('\nThe room starts to spin')
    time.sleep(1)
    print('Everything is spinning')
    time.sleep(1)
    print('Time stops')
    time.sleep(1)
    print('Your consciousness is fading')
    print('** FADE TO BLACK **')
    input('Hit enter to continue...')
    time.sleep(2)
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
    for i in TextGameConcept.inventory:
        if item == i:
            return True
    return False
def startScreen():
    time.sleep(3)
    print('\n' * 50)
    print('_____________________________________')
    print('      Welcome to \"TextGame\"')
    print('          A Python game')
    print('             -------')
    print('Developed by Bobby Anaya and Zac Banas')
    print('_____________________________________')