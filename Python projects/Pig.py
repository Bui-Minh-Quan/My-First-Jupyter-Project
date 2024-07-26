import random 

def roll():
    return random.randint(1, 6)
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit() == True:
        players = int(players)
        if players > 4 or players < 2:
            print("Please enter a number from 2 to 4!")
        else:
            break
    else:
        print("Ivalid input. Please enter a number")


max_score = 20

players_score = [0 for i in range(players)]
player_turn = 0
while True:
    if player_turn >= players:
        player_turn = 0
    command = "Player number " + str(player_turn + 1) + " turn. Would you like to roll(yes/no)? press q to quit "
    should_roll = input(command).lower()
    if should_roll == "yes":
        rnd = roll()
        if rnd != 1:
            players_score[player_turn] += rnd
        else:
            players_score[player_turn] = 0
        print("Your roll number is", rnd
              , ". Current score:", players_score[player_turn])
    elif should_roll == "no":
        print("You decided not to roll."
              , ". Current score:", players_score[player_turn])
        pass
    elif should_roll == "q":
        break
    else:
        print("Invalid, try again")
        continue

    if players_score[player_turn] >= max_score:
        print("The winner is player number", player_turn + 1, "with"
              , players_score[player_turn], "points")
        break

    player_turn += 1








    




