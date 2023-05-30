#!/usr/bin/env python3

# import classes
from cheatdice import *

def main():
    """runtime"""

    # player known as swapper
    swapper = Cheat_Swapper()
    # player known as loader
    loader = Cheat_Loaded_Dice()

    # both scores
    swapper_score = 0
    loader_score = 0

    # amount of games to run
    num_games = 100000
    game_num = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_num < num_games:
        swapper.roll()
        loader.roll()

        swapper.cheat()
        loader.cheat()

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loader.get_dice()))
        if sum(swapper.get_dice()) == sum(loader.get_dice()):
            #print("Draw!")
            pass
        elif sum(swapper.get_dice()) > sum(loader.get_dice()):
            #print("Dice swapper wins!")
            swapper_score+= 1
        else:
            #print("Loader wins!")
            loader_score+= 1
        game_num += 1
        
        # game is over
        print("Simulation complete")
        print("-------------------")
        print("Final scores")
        print("------------")
        print(f"Swapper won: {swapper_score}")
        print(f"Loader won: {loader_score}")

        # determine winner
        if swapper_score == loader_score:
            print("Game was draw")
        elif swapper_score > loader_score:
            print("Swapper won most games")
        else:
            print("Loader won most games")





if __name__ == "__main__":
    main()
