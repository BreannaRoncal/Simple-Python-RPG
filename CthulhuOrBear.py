"""
This is a simple text-based RPG to practice getting user input.

"""

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 100:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear guarding the door.")
    print("Do you taunt the bear or take its honey?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take its honey":
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in choice and not bear_moved:
            print("The bear has moved from the door. \nDo you want to open the door or taunt the bear again?. ")
            bear_moved = True
        elif "taunt" in choice and bear_moved:
            dead("The bear gets mad and bites your leg off.")
        elif "open" in choice and bear_moved:
            gold_room()
        else:
            print("IDK what that means.")

def cthulhu_room():
    print("This is the Cthulu Room. Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print("You are dead!")
    print(why)
    exit(0)

def start():
    print("""
          You are in a dark room.
          There is a door to your right and left.
          Which one do you take?
          """)

    choice = input("> ")

    if choice.lower() == "left":
        bear_room()
    elif choice.lower() == "right":
        cthulhu_room()
    else:
        dead("You stumbled around the room until you starve to death.")

start()
