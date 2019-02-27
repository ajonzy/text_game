import os
import sys
sys.path.insert(0, "./rooms")

from start import start
from initial_room import initial_room
from cabin import cabin
from outside import outside
from garden import garden
from woods import woods
from fire import fire
from upstairs import upstairs
from sleep import sleep

clear = lambda: os.system('cls')

beginning = "start"

def display_room(beginning):
    room = beginning
    if room == "start":
        clear()
        room = start()
        display_room(room)
    elif room == "initial_room":
        clear()
        room = initial_room()
        display_room(room)
    elif room == "cabin":
        clear()
        room = cabin()
        display_room(room)
    elif room == "outside":
        clear()
        room = outside()
        display_room(room)
    elif room == "garden":
        clear()
        room = garden()
        display_room(room)
    elif room == "woods":
        clear()
        room = woods()
        display_room(room)
    elif room == "fire":
        clear()
        room = fire()
        display_room(room)
    elif room == "upstairs":
        clear()
        room = upstairs()
        display_room(room)
    elif room == "sleep":
        clear()
        room = sleep()
        display_room(room)
    elif room == "end":
        clear()
        print("Ok, goodbye!")

display_room(beginning)