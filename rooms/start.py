def start():
    print("Welcome to a choose your own adventure game!\n\nReady to start? (y/n)\n")
    choice = input().lower()
    while True:
        if choice == "y":
            return "initial_room"
        elif choice == "n":
            return "end"
        else:
            print("I don't understand that command...")
            choice = input().lower()
