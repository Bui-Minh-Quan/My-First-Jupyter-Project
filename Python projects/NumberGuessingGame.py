import random
rand = random.randint(1, 100)

top_score = 5
guess_count = 5

while True:
    number = input("Type a number ")
    guess_count -= 1
    if guess_count <= 0:
        print("Game over! The answer is", rand)
        break

    if number.isdigit():
        number = int(number)
        if number < rand:
            print("Please enter a larger number. You have", guess_count, "chances left")
        elif number > rand:
            print("Please enter a smaller number. You have", guess_count, "chances left")
        else:

            print("You are correct. Your score is", str((guess_count / top_score) * 100 + 10) )
            break
    else:
        print("Please enter a number next time. You have", guess_count, "chances left")


    

    
    

