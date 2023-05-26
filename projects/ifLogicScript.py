#!/usr/bin/env python3
"""IF-LOGIC SCRIPT"""
import random

# variables
userInput = " "
genre = ["horror","action","drama","comedy","christmas"]
action = ["Lethal Weapon","Die Hard","Terminator"]
horror = ["Event Horzion", "Nightmare on elm street", "Alien"]
randHorr = random.choice(horror)
randAct = random.choice(action)

userInput = input("What is your favorite movie genre?")
userInput = userInput.strip()
    
if userInput == "horror":
    print("Oah... A fellow connoisseur")
    yesNo = input(f"Have you seen {randHorr}?: ")
    
    if yesNo == "yes":
        print("oh! That's good to hear I really enjoyed that movie. It's one of my favs.")
        movieSug = input("Do you have any suggestions?")
        print(f"Cool, I'll check out {movieSug} when I git a chance")

    else:
        print("That's to bad you should check it out when you get a chance.")

elif userInput == "action":
    print(f"Really. One of my favorite movies growning up was {randAct}.")
    wayou = input(f"What about you what was your favorite {userInput} movie growing up?")
    wayou = wayou.title()

    if wayou == action:
        print("oh. I've seen that. It's one of my favs.")

    else:
        print("Oh that sounds like a good one. I'll try to watch it when I get a chance.")


elif userInput == "comedy":
    print(f"I love {userInput}. I've seen so many movie in {userInput} that I can't even name them all.")

else:
    print("Sorry to hear that. There's plenty forms of entertainment out there.")
