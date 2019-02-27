def upstairs():
    print("You climb the stairs. Upstairs is a comfy looking bed.\n\nDo you go to sleep for the day? (s)\nDo you go back downstairs? (d)\n")
    choice = input().lower()
    while True:
        if choice == "s":
            return "sleep"
        elif choice == "d":
            return "cabin"
        else:
            print("I don't understand that command...")
            choice = input().lower()