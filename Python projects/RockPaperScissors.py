import random


users_win = 0
computer_win = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        print("users win :", users_win)
        print("Computer win:", computer_win)
        print("Good bye")
        break
    if user_input not in ["rock", "paper", "scissors", "q"]:
        continue
    
    rand = random.randint(1, 3)
    if rand == 1:
        print("Computer: Rock")
        if user_input == "rock": 
            print("Draw")
        elif user_input == "paper":
            print("You win")
            users_win += 1
        elif user_input == "scissors":
            print("You lose")
            computer_win += 1
    elif rand == 2:
        print("Computer: Paper")
        if user_input == "paper": 
            print("Draw")
        elif user_input == "scissors":
            print("You win")
            users_win += 1
        elif user_input == "rock":
            print("You lose")
            computer_win += 1
    elif rand == 3:
        print("Computer: Scissors")
        if user_input == "scissors": 
            print("Draw")
        elif user_input == "rock":
            print("You win")
            users_win += 1
        elif user_input == "paper":
            print("You lose")
            computer_win += 1

