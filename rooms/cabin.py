def cabin():
    print("You are in a small cabin. There is a fire going in the fireplace, and a staircase in the corner.\n\nDo you stoke the fire? (f)\nDo you go up the stairs? (u)\nDo you go outside? (o)\n")
    choice = input().lower()
    while True:
        if choice == "f":
            return "fire"
        elif choice == "u":
            return "upstairs"
        elif choice == "o":
            return "outside"
        else:
            print("I don't understand that command...")
            choice = input().lower()