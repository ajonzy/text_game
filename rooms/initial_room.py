def initial_room():
    print("You find yourself in a room. There's a door leading outside.\n\nDo you inspect the room? (i)\nDo you go outside? (o)\n")
    choice = input().lower()
    while True:
        if choice == "i":
            return "cabin"
        elif choice == "o":
            return "outside"
        else:
            print("I don't understand that command...")
            choice = input().lower()