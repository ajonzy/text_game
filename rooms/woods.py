def woods():
    print("You wander the woods for what seems like hours before realizing you have no idea where you are!\nYou are lost :(\n\nWant to try again? (y/n)\n")
    choice = input().lower()
    while True:
        if choice == "y":
            return "initial_room"
        elif choice == "n":
            return "end"
        else:
            print("I don't understand that command...")
            choice = input().lower()