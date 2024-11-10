import os
os.system('cls' if os.name == 'nt' else 'clear')

# Day 3

# Game Dev

print("Welcome to the Treasure Land! \nYour Mission is to find the Treasure! ")
Choice1 = input('Choose between "left" or "right": ').lower()


if Choice1 == "left":
    Choice2 = input('You Wanna: "wait" or "swim": ').lower()
    if Choice2 == "wait":
        Choice3 = input('Which Color You Wanna Pick, "yellow" or "red" or "blue": ').lower()
        if Choice3 == "Red":
            print("You were Eaten by a Snack! ")
        elif Choice3 == "Yellow":
            print("You Entered into a Fire Door! ")
        elif Choice3 == "Blue":
            print("You Found The Treasure! Congratulations! You Won the Game! ")
        else:
            print("You Entered the Wrong Door! Game Over! ")
    else:
        print("Hahahaha! ")
else: 
    print("Game Over! ")
