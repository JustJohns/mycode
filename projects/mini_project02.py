#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# player base stats variables
health = 100
energy = 100

# player stats
class Player:
    """determines player starting stats"""
    def __init__(self, health, energy):
    #potential user input name
        #self.name = userInput
        #userInput = input()

        #player starting stats
        self.health = health
        self.energy = energy

    def show_player_status(self):
        """Show player status"""
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
#player1 = Player(75, 100)
#player1.show_player_status()

def show_instructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      examine [area or item]
      status [player current status]
      '''
    '\nGet the key to garden and escape this nightmare'
    )


def show_status():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentroom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentroom]:
        print('You see a ' + rooms[currentroom]['item'])
    print("---------------------------")
    if "itemF" in rooms[currentroom]:
        print('You see a ' + rooms[currentroom]['item'])

def endGame():
    if move[0] == 'end':
        userInput = input("Are you sure?\t")
        if userInput == 'yes':
            exit()
        else:
            print("\nCan you escape this place?\n")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Outside': {
        'east': 'Hall',
        'north': 'forest',
        'west': 'forest',
        'south': 'forest'
    },
    'forest': {
        'north': 'forest',
        'south': 'forest',
        'east': 'forest',
        'west': 'forest'
    },
    'Hall': {
        'north': 'hallway',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'hallway': {
        'north': 'Master Bedroom',
        'south': 'Hall',
        'east': 'east hallway',
        'item': 'window',
    },
    'Master Bedroom': {
        'north': 'bathroom',
        'south': 'hallway',
        'item': 'bed',
    },
    'east hallway': {
        'north': 'closet'
    },
    'bathroom': {
        'item': 'mirror'
    },
    'closet': {
        'item': 'pipe'
    }


}

# start the player in the Outside
currentroom = 'Outside'

show_instructions()

# breaking this while loop means the game is over
while True:
    show_status()
    #show_player_status(self, health, energy)

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentroom]:
            # set the current room to the new room
            currentroom = rooms[currentroom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentroom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'use' first
    if move[0] == 'use':
        # if item room contains item
        # if item in room matches item player wishes to use
        if 'item' in rooms[currentroom] and move[1] in rooms[currentroom]['item']:
            # examine item
            print("")
        else:
            print("You can't do that here")

    # if player enters room with bed
    if move[0] == 'sleep':
        if 'item' in rooms[currentroom] and 'bed' in rooms[currentroom]['item']:
            Player(health, energy).health += 25
            Player(health, energy ).energy += 100
            print("You have slept in the bed and some time has passed")
        else:
            print("You can't do that here")

    if move[0] == 'status':
        print()
    
    # if they type 'examine' first
    if move[0] == 'examine':
        if 'item' in rooms[currentroom] and 'bed' in rooms[currentroom]['item']:
            print(f"It looks comfortable")
        elif 'item' in rooms[currentroom] and 'mirror' in rooms[currentroom]['item']:
            print(f"Who am I? What am I doing here?")
        else:
            print(f"It looks normal to me")
    
    # if player enters room with monster
    if 'item' in rooms[currentroom] and 'monster' in rooms[currentroom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # if player enters forest and moves 3 times in the forest they lose 
    if currentroom == 'forest':
        print('You got lost in the forest')
        break

    # Define how player wins
    if currentroom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

endGame()
            
    
  
