def outside():
    print("You are outside. It's a lovely day!\n\nDo you stroll through the garden? (g)\nDo you wander in the creepy nearby woods? (w)\nDo you go inside?(i)\n")
    choice = input().lower()
    while True:
        if choice == "g":
            return "garden"
        elif choice == "w":
            return "woods"
        elif choice == "i":
            return "initial_room"
        else:
            print("I don't understand that command...")
            choice = input().lower()