def start():
    print("You wake up in a dark forest.")
    print("Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ")

    if choice.lower() == 'left':
        left_path()
    elif choice.lower() == 'right':
        right_path()
    else:
        print("Invalid choice. Game over.")

def left_path():
    print("You find a river. Do you swim across or follow it?")
    choice = input("Type 'swim' or 'follow': ")

    if choice.lower() == 'swim':
        print("You were eaten by a crocodile. Game over.")
    elif choice.lower() == 'follow':
        print("You found a village and are safe. You win!")
    else:
        print("Invalid choice. Game over.")

def right_path():
    print("You find a cave. Do you enter or walk past it?")
    choice = input("Type 'enter' or 'walk': ")

    if choice.lower() == 'enter':
        print("It's dark and scary. A monster attacks you. Game over.")
    elif choice.lower() == 'walk':
        print("You walk safely and find help. You win!")
    else:
        print("Invalid choice. Game over.")

start()