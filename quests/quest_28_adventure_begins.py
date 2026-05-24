# Choose Your Own Adventure Game

def forest():
    choice = input("You enter a dark forest. Do you go 'left' or 'right'? ")
    if choice == "left":
        print("You find a treasure chest! You win!")
    else:
        print("A wild beast appears! Game over.")

def cave():
    choice = input("You enter a cave. Do you 'explore' or 'leave'? ")
    if choice == "explore":
        print("You discover ancient magic! You win!")
    else:
        print("You safely exit, but gain nothing. The end.")

def start_game():
    print("Adventure Begins!")
    path = input("Do you go to the 'forest' or the 'cave'? ")

    if path == "forest":
        forest()
    elif path == "cave":
        cave()
    else:
        print("You stand still and the adventure passes you by.")

# Start the game
start_game()

