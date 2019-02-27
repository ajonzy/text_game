def sleep():
    print("You go to sleep after a long day. Get some well deserved rest :)\n\nPlay again? (y/n)\n")
    choice = input().lower()
    while True:
        if choice == "y":
            return "initial_room"
        elif choice == "n":
            return "end"
        else:
            print("I don't understand that command...")
            choice = input().lower()